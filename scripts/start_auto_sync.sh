#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

PID_FILE="$DIR/.auto_sync.pid"
LOG_FILE="$DIR/.auto_sync.log"

if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        echo "⚠️  Auto-sync daemon is already running (PID: $PID)."
        echo "   View logs with: tail -f .auto_sync.log"
        exit 0
    fi
fi

PYTHON_BIN="/home/neo/.local/share/uv/tools/overleaf-latex-mcp/bin/python"
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="python3"
fi

nohup "$PYTHON_BIN" -u "$DIR/scripts/auto_sync_daemon.py" </dev/null >> "$LOG_FILE" 2>&1 &
NEW_PID=$!
disown $NEW_PID
echo "$NEW_PID" > "$PID_FILE"

echo "✅ Auto-sync daemon started in background (PID: $NEW_PID)."
echo "   - Overleaf sync: 30s after changes"
echo "   - Git/GitHub push: 10m after changes"
echo "   - Log file: .auto_sync.log"
