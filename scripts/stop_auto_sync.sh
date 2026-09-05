#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

PID_FILE="$DIR/.auto_sync.pid"

if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        kill "$PID" 2>/dev/null || true
        echo "🛑 Auto-sync daemon stopped (PID: $PID)."
    else
        echo "ℹ️  Auto-sync daemon was not running."
    fi
    rm -f "$PID_FILE"
else
    echo "ℹ️  No running auto-sync daemon found."
fi
