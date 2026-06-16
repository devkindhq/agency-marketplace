#!/usr/bin/env bash
# Agency Marketplace — Claude Code plugins & skills
# Source: https://github.com/devkindhq/agency-marketplace
set -euo pipefail

MARKETPLACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MARKETPLACE_NAME="agency-marketplace"

if ! command -v docker &> /dev/null; then
  echo "Warning: Docker not found. The security plugin requires Docker."
  echo "Install Docker from: https://docs.docker.com/get-docker/"
fi

echo "Installing $MARKETPLACE_NAME from $MARKETPLACE_DIR"

# Register the marketplace
claude plugin marketplace add "$MARKETPLACE_DIR"

# Install all domain plugins (MCP servers declared in each plugin's .mcp.json load automatically)
claude plugin install evidence-dev@"$MARKETPLACE_NAME"
claude plugin install seo@"$MARKETPLACE_NAME"
claude plugin install security@"$MARKETPLACE_NAME"

# Security plugin MCP (whatweb) pulls devkind/whatweb-mcp:latest from Docker Hub on first use

echo "Done. Restart Claude Code or start a new session to activate skills."
