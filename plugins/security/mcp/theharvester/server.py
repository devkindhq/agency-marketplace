#!/usr/bin/env python3
"""
theHarvester MCP Server - OSINT email, subdomain, IP, and LinkedIn harvesting.

Tools:
    - harvest: Run OSINT harvest on a domain
    - get_harvest_results: Retrieve results by harvest ID
    - list_active_harvests: Show running harvests
    - list_sources: Show available data sources
"""

import asyncio
import json
import logging
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Resource, TextContent, Tool
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("theharvester-mcp")


class Settings(BaseSettings):
    output_dir: str = Field(default="/app/output", alias="THEHARVESTER_OUTPUT_DIR")
    default_timeout: int = Field(default=120, alias="THEHARVESTER_TIMEOUT")
    max_concurrent: int = Field(default=2, alias="THEHARVESTER_MAX_CONCURRENT")

    class Config:
        env_prefix = "THEHARVESTER_"


settings = Settings()

FREE_SOURCES = ["crtsh", "hackertarget", "dnsdumpster", "rapiddns", "urlscan", "otx", "duckduckgo"]

ALL_SOURCES = [
    "baidu", "bevigil", "bitbucket", "brave", "bufferoverun", "censys",
    "certspotter", "commoncrawl", "crtsh", "dnsdumpster", "duckduckgo",
    "fullhunt", "github-code", "hackertarget", "hunter", "hunterhow",
    "intelx", "mojeek", "netlas", "onyphe", "otx", "rapiddns", "robtex",
    "securityTrails", "shodan", "shodanInternetDB", "subdomaincenter",
    "subdomainfinderc99", "tomba", "urlscan", "virustotal",
    "waybackarchive", "whoisxml", "yahoo", "zoomeye",
]


class HarvestResult(BaseModel):
    harvest_id: str
    domain: str
    sources: list[str]
    started_at: datetime
    completed_at: datetime | None = None
    status: str = "running"
    emails: list[str] = []
    hosts: list[str] = []
    ips: list[str] = []
    linkedin: list[str] = []
    interesting_urls: list[str] = []
    asns: list[str] = []
    error: str | None = None


harvest_results: dict[str, HarvestResult] = {}
active_harvests: set[str] = set()


def _clean_list(items: list) -> list[str]:
    return [str(i).strip() for i in items if i]


async def run_harvest(domain: str, sources: list[str], limit: int = 200, timeout: int | None = None) -> HarvestResult:
    harvest_id = str(uuid.uuid4())[:8]
    output_filename = f"harvest_{harvest_id}"
    output_dir = Path(settings.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    result = HarvestResult(harvest_id=harvest_id, domain=domain, sources=sources, started_at=datetime.now())
    harvest_results[harvest_id] = result
    active_harvests.add(harvest_id)

    # Use the venv script directly — `-m theHarvester` runs __main__.py which has no entry point call.
    # theHarvester's sanitize_filename() strips directory prefixes, so pass a bare filename
    # and set cwd=output_dir so the JSON lands where we look for it.
    cmd = [
        "/opt/theharvester/.venv/bin/theHarvester",
        "-d", domain,
        "-b", ",".join(sources),
        "-l", str(limit),
        "-f", output_filename,
        "-q",
    ]

    logger.info(f"Starting harvest {harvest_id}: {domain} via {','.join(sources)}")

    try:
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(output_dir),
        )

        _, stderr = await asyncio.wait_for(
            process.communicate(),
            timeout=float(timeout or settings.default_timeout),
        )

        result.completed_at = datetime.now()

        json_file = output_dir / f"{output_filename}.json"
        if json_file.exists():
            data = json.loads(json_file.read_text())
            result.emails = _clean_list(data.get("emails", []))
            result.hosts = _clean_list(data.get("hosts", []))
            result.ips = _clean_list(data.get("ips", []))
            result.linkedin = _clean_list(data.get("linkedin", []))
            result.interesting_urls = _clean_list(data.get("interesting_urls", []))
            result.asns = _clean_list(data.get("asns", []))

        result.status = "completed" if process.returncode == 0 else "failed"
        if process.returncode != 0:
            result.error = stderr.decode()[:500]

    except asyncio.TimeoutError:
        result.status = "timeout"
        result.error = f"Timed out after {timeout or settings.default_timeout}s"
        result.completed_at = datetime.now()

    except Exception as e:
        result.status = "error"
        result.error = str(e)
        result.completed_at = datetime.now()

    finally:
        active_harvests.discard(harvest_id)
        harvest_results[harvest_id] = result

    return result


def format_result(result: HarvestResult) -> dict[str, Any]:
    duration = None
    if result.completed_at:
        duration = round((result.completed_at - result.started_at).total_seconds(), 1)

    return {
        "harvest_id": result.harvest_id,
        "domain": result.domain,
        "status": result.status,
        "duration_seconds": duration,
        "sources_used": result.sources,
        "summary": {
            "emails": len(result.emails),
            "hosts": len(result.hosts),
            "ips": len(result.ips),
            "linkedin": len(result.linkedin),
            "interesting_urls": len(result.interesting_urls),
        },
        "emails": result.emails[:50],
        "hosts": result.hosts[:100],
        "ips": result.ips[:50],
        "linkedin": result.linkedin[:50],
        "interesting_urls": result.interesting_urls[:20],
        "asns": result.asns[:10],
        "error": result.error,
    }


app = Server("theharvester-mcp")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="harvest",
            description=(
                "Harvest OSINT data for a domain — finds emails, subdomains, IPs, "
                "and LinkedIn profiles from public sources. "
                "Use sources='free' for fast no-API-key results."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "domain": {"type": "string", "description": "Target domain (e.g., eva.com.au)"},
                    "sources": {
                        "type": "string",
                        "description": "Comma-separated sources, or 'free' (no API key needed) or 'all'",
                        "default": "free",
                    },
                    "limit": {"type": "integer", "description": "Max results per source", "default": 200},
                    "timeout": {"type": "integer", "description": "Timeout in seconds", "default": 120},
                },
                "required": ["domain"],
            },
        ),
        Tool(
            name="get_harvest_results",
            description="Retrieve results from a previous harvest by ID.",
            inputSchema={
                "type": "object",
                "properties": {"harvest_id": {"type": "string"}},
                "required": ["harvest_id"],
            },
        ),
        Tool(
            name="list_active_harvests",
            description="List currently running harvests.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="list_sources",
            description="List all available OSINT sources.",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    try:
        if name == "harvest":
            if len(active_harvests) >= settings.max_concurrent:
                return [TextContent(type="text", text="Max concurrent harvests reached.")]

            sources_arg = arguments.get("sources", "free")
            if sources_arg == "free":
                sources = FREE_SOURCES
            elif sources_arg == "all":
                sources = ALL_SOURCES
            else:
                sources = [s.strip() for s in sources_arg.split(",")]

            result = await run_harvest(
                domain=arguments["domain"],
                sources=sources,
                limit=arguments.get("limit", 200),
                timeout=arguments.get("timeout"),
            )
            return [TextContent(type="text", text=json.dumps(format_result(result), indent=2))]

        elif name == "get_harvest_results":
            result = harvest_results.get(arguments["harvest_id"])
            if result:
                return [TextContent(type="text", text=json.dumps(format_result(result), indent=2))]
            return [TextContent(type="text", text="Harvest not found")]

        elif name == "list_active_harvests":
            active = [{"harvest_id": h, "domain": harvest_results[h].domain} for h in active_harvests if h in harvest_results]
            return [TextContent(type="text", text=json.dumps({"active_harvests": active}, indent=2))]

        elif name == "list_sources":
            return [TextContent(type="text", text=json.dumps({
                "free_sources": FREE_SOURCES,
                "all_sources": ALL_SOURCES,
                "note": "Sources like censys, shodan, intelx, virustotal require API keys",
            }, indent=2))]

        return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@app.list_resources()
async def list_resources() -> list[Resource]:
    return [
        Resource(uri=f"harvest://results/{hid}", name=f"Harvest: {r.domain}", mimeType="application/json")
        for hid, r in harvest_results.items()
        if r.status == "completed"
    ]


@app.read_resource()
async def read_resource(uri: str) -> str:
    if uri.startswith("harvest://results/"):
        hid = uri.replace("harvest://results/", "")
        result = harvest_results.get(hid)
        if result:
            return json.dumps(format_result(result), indent=2)
    return json.dumps({"error": "Resource not found"})


async def main():
    logger.info("Starting theHarvester MCP Server")
    Path(settings.output_dir).mkdir(parents=True, exist_ok=True)
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
