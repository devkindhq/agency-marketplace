---
name: tech-detector
description: Detect the technology stack of any website. Use when someone shares a URL, asks "what are they running", "what's their stack", or wants to audit a site or research a competitor. Runs WhatWeb scan and returns stack insights and analysis angles.
tools: [mcp__plugin_security_whatweb__whatweb_scan]
---

# Tech Detector — Stack Analysis

## When to use this skill

Trigger when:
- Someone shares a URL and wants to know what it's built on
- "What tech does [company] use?"
- "What are they running?"
- "Auditing a site before a meeting [company]?" + a URL is provided
- Researching what a client or competitor is running
- Competitor analysis

## How to run the scan

Call `mcp__plugin_security_whatweb__whatweb_scan` with:
- `target`: the URL provided
- `aggression`: `normal` (default — non-intrusive, safe for live sites)

## How to interpret and present results

Always present findings in three sections:

### 1. Stack Summary
Plain-English summary of what they're running. Group by:
- **Platform/CMS** — Shopify, WordPress, Webflow, custom, etc.
- **Frontend** — React, Vue, jQuery, Bootstrap, etc.
- **Infrastructure** — Cloudflare, AWS, Vercel, Fastly, etc.
- **Analytics/Marketing** — GTM, GA4, HubSpot, Intercom, etc.

### 2. What This Tells Us
Interpret the stack in business terms:
- How old/modern is the tech?
- Are they likely on a legacy setup or cutting-edge?
- What pain points does this stack typically have?
- What does the presence of certain tools suggest about their team size / budget?

### 3. Analysis Angles
Map detected tech to specific opportunities:

| Detected | Observation |
|----------|-------------|
| Shopify (Bootstrap/jQuery theme) | Likely older theme — performance and modernisation opportunity |
| Shopify (no GTM/analytics) | Analytics gap — no conversion tracking in place |
| WordPress | Common maintenance pain points: performance, security, plugin sprawl |
| Webflow | Hosted CMS constraints — custom dev or migration may be needed at scale |
| No identifiable platform | Likely custom build — dev team dependency, higher maintenance cost |
| jQuery / Bootstrap (no modern framework) | Legacy frontend — migration to React/Vue may be warranted |
| No HTTPS / missing HSTS | Basic security gap, quick to address |
| Google Tag Manager | Active marketing instrumentation in place |
| Cloudflare | Performance and security aware — sophisticated infra |
| Vercel / Next.js | Modern stack, likely needs backend/API or design system work |
| No CDN detected | Performance risk — static assets served from origin |

## Output format

Keep it tight and actionable. Example:

---
**[Company] — Tech Stack**

**Platform:** Shopify
**Frontend:** Bootstrap, jQuery (legacy theme)
**CDN:** Cloudflare
**Analytics:** Google Tag Manager

**What this tells us:**
They're on a standard Shopify setup with an older theme stack (Bootstrap/jQuery). GTM presence means there's an active marketing team. Cloudflare suggests someone technical is involved, even if their dev team is small.

**Analysis angles:**
- Custom Shopify theme (modern, performance-focused) — Bootstrap/jQuery theme is likely slow
- Headless Shopify if they're hitting platform limits
- Analytics depth — GTM is present, tracking baseline is in place
---

## Parallelisation
Safe — this skill is stateless and read-only (HTTP scan only). Multiple tech-detector agents can run simultaneously against different URLs with no conflicts or side effects.

## Machine-readable Return Contract
When invoked by an orchestrator agent collecting results for multiple targets, return a JSON envelope alongside the markdown report:
```json
{
  "url": "<scanned URL>",
  "cms": "<platform or null>",
  "stack": ["<tech1>", "<tech2>"],
  "analysis_angles": ["<angle1>", "<angle2>"]
}
```
The orchestrator uses this to aggregate and sort results without parsing the markdown.

## Notes

- If http_status is not 200, flag it ("site may be down or blocking scanners")
- If very few technologies detected (<5), note that the site may be behind a heavy proxy or WAF masking the stack — suggest running with `aggression: aggressive` for a deeper look
- Never present raw scan JSON to the user — always translate to the format above
- If no URL is provided, ask for one before running
