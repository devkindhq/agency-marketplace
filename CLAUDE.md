# Agency Marketplace — Claude Notes

## Plugin Versioning (Important)

When adding or modifying a plugin (new skills, MCP changes, etc.), **both** version fields must be bumped or the plugin system will skip the update:

1. `plugins/<name>/.claude-plugin/plugin.json` — the plugin's own version
2. `.claude-plugin/marketplace.json` — the registry entry for that plugin

The cache is keyed by version: `~/.claude/plugins/cache/agency-marketplace/<name>/<version>/`. If the installed version matches the marketplace declaration, reinstall is skipped even if files changed.

After bumping versions, force a reinstall:
```bash
claude plugin uninstall <name>@agency-marketplace && claude plugin install <name>@agency-marketplace
```

## Plugin Structure

```
plugins/<name>/
  .claude-plugin/plugin.json   # manifest — name, version (NO skills array — auto-discovered)
  .mcp.json                    # MCP server declarations (auto-registered on install)
  skills/<skill-name>/SKILL.md # skills are discovered automatically from this directory
  mcp/<tool>/                  # Docker files for MCP servers
```

## MCP Servers

- `security/whatweb` — published to Docker Hub as `devkind/whatweb-mcp:latest`
- Docker image pulls automatically on first `whatweb_scan` call — no manual build needed
- To update: rebuild locally, push to `devkind/whatweb-mcp:latest`, users get it on next Docker pull

## install.sh

Registers the marketplace and installs all plugins. Run once per machine:
```bash
./install.sh
```
