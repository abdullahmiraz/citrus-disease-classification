#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

PYTHON_BIN="/home/neo/.local/share/uv/tools/overleaf-latex-mcp/bin/python"
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="python3"
fi

"$PYTHON_BIN" "$DIR/scripts/sync_to_overleaf.py"
