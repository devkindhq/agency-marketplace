#!/usr/bin/env bash
set -euo pipefail

MARKETPLACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MARKETPLACE_NAME="agency-marketplace"

echo "Installing $MARKETPLACE_NAME from $MARKETPLACE_DIR"

# Register the marketplace
claude plugin marketplace add "$MARKETPLACE_DIR"

# Install all domain plugins (MCP servers declared in each plugin's .mcp.json load automatically)
claude plugin install seo@"$MARKETPLACE_NAME"
claude plugin install security@"$MARKETPLACE_NAME"

# Security plugin MCP (whatweb) pulls devkind/whatweb-mcp:latest from Docker Hub on first use

echo "Done. Restart Claude Code or start a new session to activate skills."
