#!/usr/bin/env bash
set -euo pipefail

MARKETPLACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MARKETPLACE_NAME="agency-marketplace"

echo "Installing $MARKETPLACE_NAME from $MARKETPLACE_DIR"

# Register the marketplace
claude plugin marketplace add "$MARKETPLACE_DIR"

# Install all domain plugins
claude plugin install seo@"$MARKETPLACE_NAME"

echo "Done. Restart Claude Code or start a new session to activate skills."
