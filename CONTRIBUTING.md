# Contributing to Agency Marketplace

## Adding a new plugin

Each plugin lives under `plugins/<name>/` and must follow this structure:

```
plugins/<name>/
  .claude-plugin/plugin.json   # manifest
  skills/<skill-name>/SKILL.md # one directory per skill (auto-discovered)
  .mcp.json                    # optional: MCP server declarations
  mcp/<tool>/                  # optional: Docker files for MCP servers
```

### plugin.json required fields
- `name` — matches the directory name
- `version` — semver string
- `description` — one sentence, keyword-rich
- `author.name`
- `license` — e.g. `"MIT"`

Do NOT include a `skills` array — skills are auto-discovered from the `skills/` directory.

## Adding a skill

Create `plugins/<name>/skills/<skill-name>/SKILL.md`. Every SKILL.md must include:
1. A YAML frontmatter block with `name` and `description`
2. A `## When to use` section with specific trigger phrases
3. At least one usage example
4. A defined output format
5. A `## Parallelisation` line stating whether it is safe to run concurrently

## Version bumping (important)

When you add or change anything in a plugin, bump the version in BOTH:
1. `plugins/<name>/.claude-plugin/plugin.json`
2. `.claude-plugin/marketplace.json` — the registry entry for that plugin

The cache is keyed by version. If only one is bumped, reinstall is skipped.

After bumping, force reinstall:
```bash
claude plugin uninstall <name>@agency-marketplace && claude plugin install <name>@agency-marketplace
```

## Pull request process

- One plugin or skill per PR
- Include a description of what the skill does and when Claude should invoke it
- Ensure your SKILL.md has all required sections listed above
- Bump versions in both files before opening the PR
