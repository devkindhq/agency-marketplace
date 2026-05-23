#!/usr/bin/env python3
"""
WhatWeb MCP Server

A Model Context Protocol server that provides web technology
fingerprinting using WhatWeb.

Tools:
    - whatweb_scan: Identify web technologies on a target
    - get_scan_results: Retrieve previous scan results
    - list_active_scans: Show running scans
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
from mcp.types import (
    Resource,
    TextContent,
    Tool,
)
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("whatweb-mcp")


class Settings(BaseSettings):
    output_dir: str = Field(default="/app/output", alias="WHATWEB_OUTPUT_DIR")
    default_timeout: int = Field(default=300, alias="WHATWEB_TIMEOUT")
    max_concurrent_scans: int = Field(default=2, alias="WHATWEB_MAX_CONCURRENT")

    class Config:
        env_prefix = "WHATWEB_"


settings = Settings()


class Technology(BaseModel):
    name: str
    version: str | None = None
    string: str | None = None
    certainty: int | None = None


class ScanResult(BaseModel):
    scan_id: str
    target: str
    started_at: datetime
    completed_at: datetime | None = None
    status: str = "running"
    technologies: list[Technology] = []
    http_status: int | None = None
    title: str | None = None
    ip: str | None = None
    country: str | None = None
    stats: dict[str, Any] = {}
    error: str | None = None
    raw_output: str | None = None


scan_results: dict[str, ScanResult] = {}
active_scans: set[str] = set()

AGGRESSION_LEVELS = {
    "stealthy": 1,
    "passive": 1,
    "polite": 2,
    "normal": 3,
    "aggressive": 4,
}


def parse_whatweb_json(output: str) -> tuple[list[Technology], dict[str, Any]]:
    technologies = []
    metadata = {}

    try:
        data = json.loads(output)
        if isinstance(data, list) and len(data) > 0:
            result = data[0]
            metadata["http_status"] = result.get("http_status")
            metadata["target"] = result.get("target")

            plugins = result.get("plugins", {})
            for plugin_name, plugin_data in plugins.items():
                tech = Technology(name=plugin_name)

                if isinstance(plugin_data, dict):
                    if "version" in plugin_data:
                        versions = plugin_data["version"]
                        if isinstance(versions, list) and versions:
                            tech.version = versions[0]
                    if "string" in plugin_data:
                        strings = plugin_data["string"]
                        if isinstance(strings, list) and strings:
                            tech.string = strings[0]

                technologies.append(tech)
    except json.JSONDecodeError as e:
        logger.warning(f"Error parsing whatweb output: {e}")

    return technologies, metadata


async def run_whatweb_scan(
    target: str,
    aggression: str = "normal",
    timeout: int | None = None,
) -> ScanResult:
    scan_id = str(uuid.uuid4())[:8]
    output_file = Path(settings.output_dir) / f"whatweb_{scan_id}.json"

    result = ScanResult(
        scan_id=scan_id,
        target=target,
        started_at=datetime.now(),
    )
    scan_results[scan_id] = result
    active_scans.add(scan_id)

    aggression_level = AGGRESSION_LEVELS.get(aggression, 3)

    # Uses create_subprocess_exec (args array, no shell) — safe against injection
    cmd = [
        "whatweb",
        "-a", str(aggression_level),
        "--log-json", str(output_file),
        target,
    ]

    logger.info(f"Starting whatweb scan {scan_id} for target: {target}")

    try:
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await asyncio.wait_for(
            process.communicate(),
            timeout=float(timeout or settings.default_timeout),
        )

        result.completed_at = datetime.now()

        if output_file.exists():
            output_content = output_file.read_text()
            result.raw_output = output_content
            result.technologies, metadata = parse_whatweb_json(output_content)
            result.http_status = metadata.get("http_status")

        result.stats = {
            "total_technologies": len(result.technologies),
            "technologies": [t.name for t in result.technologies],
        }

        result.status = "completed" if process.returncode == 0 else "failed"
        if process.returncode != 0:
            result.error = stderr.decode()

    except asyncio.TimeoutError:
        result.status = "timeout"
        result.error = f"Scan timed out after {timeout or settings.default_timeout} seconds"
        result.completed_at = datetime.now()

    except Exception as e:
        result.status = "error"
        result.error = str(e)
        result.completed_at = datetime.now()

    finally:
        active_scans.discard(scan_id)
        scan_results[scan_id] = result

    return result


def format_scan_summary(result: ScanResult) -> dict[str, Any]:
    techs = []
    for t in result.technologies[:50]:
        techs.append({
            "name": t.name,
            "version": t.version,
            "string": t.string,
        })

    return {
        "scan_id": result.scan_id,
        "target": result.target,
        "status": result.status,
        "http_status": result.http_status,
        "stats": result.stats,
        "technologies": techs,
        "error": result.error,
    }


app = Server("whatweb-mcp")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="whatweb_scan",
            description="Identify web technologies, CMS, frameworks, and server software. "
            "Detects WordPress, Drupal, Apache, nginx, jQuery, and hundreds more.",
            inputSchema={
                "type": "object",
                "properties": {
                    "target": {
                        "type": "string",
                        "description": "Target URL or domain (e.g., https://example.com)",
                    },
                    "aggression": {
                        "type": "string",
                        "enum": ["stealthy", "passive", "polite", "normal", "aggressive"],
                        "description": "Scan aggression level",
                        "default": "normal",
                    },
                    "timeout": {
                        "type": "integer",
                        "description": "Timeout in seconds",
                        "default": 300,
                    },
                },
                "required": ["target"],
            },
        ),
        Tool(
            name="get_scan_results",
            description="Retrieve results from a previous scan by scan ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "scan_id": {"type": "string", "description": "Scan ID"},
                },
                "required": ["scan_id"],
            },
        ),
        Tool(
            name="list_active_scans",
            description="List currently running scans.",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    try:
        if name == "whatweb_scan":
            if len(active_scans) >= settings.max_concurrent_scans:
                return [TextContent(type="text", text="Max concurrent scans reached.")]

            result = await run_whatweb_scan(
                target=arguments["target"],
                aggression=arguments.get("aggression", "normal"),
                timeout=arguments.get("timeout"),
            )

            return [TextContent(type="text", text=json.dumps(format_scan_summary(result), indent=2))]

        elif name == "get_scan_results":
            result = scan_results.get(arguments["scan_id"])
            if result:
                return [TextContent(type="text", text=json.dumps(format_scan_summary(result), indent=2))]
            return [TextContent(type="text", text="Scan not found")]

        elif name == "list_active_scans":
            active = [{"scan_id": s, "target": scan_results[s].target} for s in active_scans if s in scan_results]
            return [TextContent(type="text", text=json.dumps({"active_scans": active}, indent=2))]

        return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@app.list_resources()
async def list_resources() -> list[Resource]:
    return [
        Resource(
            uri=f"whatweb://results/{scan_id}",
            name=f"WhatWeb: {result.target}",
            mimeType="application/json",
        )
        for scan_id, result in scan_results.items()
        if result.status == "completed"
    ]


@app.read_resource()
async def read_resource(uri: str) -> str:
    if uri.startswith("whatweb://results/"):
        scan_id = uri.replace("whatweb://results/", "")
        result = scan_results.get(scan_id)
        if result:
            return json.dumps(format_scan_summary(result), indent=2)
    return json.dumps({"error": "Resource not found"})


async def main():
    logger.info("Starting WhatWeb MCP Server")
    Path(settings.output_dir).mkdir(parents=True, exist_ok=True)

    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
