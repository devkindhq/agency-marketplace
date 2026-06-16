---
name: harvester
description: OSINT domain intelligence skill — use when asked to research a company domain, find email addresses, subdomains, hosts, or employee names associated with a target domain for stack analysis or security reconnaissance.
---

# theHarvester — OSINT Domain Intelligence

## When to use
Invoke when the user asks to:
- "Find emails for domain X" / "what emails are associated with company.com"
- "Research subdomains of target.com"
- "Find employee names at company.com for outreach"
- "Run OSINT on this domain"
- "What hosts are associated with this company?"
- Any sales or security context where gathering publicly available information about a domain is the goal

**Important legal/ethical constraint:** Only use against domains you own or have explicit written permission to research. Unauthorised OSINT may be illegal in your jurisdiction.

## Tools Required
- `mcp__plugin_security_theharvester__harvest_domain` — primary tool for running theHarvester
- `mcp__plugin_security_theharvester__get_harvest_results` — for retrieving results of a previous harvest

## Usage

### Basic harvest
```
harvest_domain(domain="target.com", sources="free")
```
Uses only free/passive sources (default). Safe for initial prospecting.

### Targeted harvest for sales outreach
```
harvest_domain(domain="target.com", sources="linkedin,hunter,dnsdumpster", limit=50)
```

### Available sources
- `free` — all free passive sources (recommended starting point)
- `all` — all sources including active ones (use with caution)
- Individual sources: `linkedin`, `hunter`, `dnsdumpster`, `crtsh`, `hackertarget`, `rapiddns`, `sublist3r`, `threatminer`, `urlscan`

## Output Format

Return a structured report with these sections:

### Domain Intelligence Report: [domain]
**Emails found:** list or "none found"
**Subdomains:** list (up to 20, note total count)
**Hosts/IPs:** list
**Employee names:** list or "none found"

### Sales Intelligence Summary
- Company size signal (based on subdomain diversity)
- Tech signals visible in subdomain names (e.g., `jira.company.com` -> uses Jira)
- Recommended outreach targets (email patterns if found)

## Parallelisation
Safe — each harvest runs against a different domain with no shared state. Multiple harvester agents can run simultaneously against different domains.

## Machine-readable Return Contract
When invoked by an orchestrator collecting intelligence on multiple domains:
```json
{
  "domain": "<target domain>",
  "emails": ["<email1>", "<email2>"],
  "subdomains": ["<sub1>", "<sub2>"],
  "employee_names": ["<name1>"],
  "sales_signals": ["<signal1>", "<signal2>"]
}
```
