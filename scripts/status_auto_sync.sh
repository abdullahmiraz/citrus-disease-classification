#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

PID_FILE="$DIR/.auto_sync.pid"
LOG_FILE="$DIR/.auto_sync.log"

if [ -f "$PID_FILE" ] && ps -p "$(cat "$PID_FILE")" > /dev/null 2>&1; then
    echo "🟢 Auto-sync daemon is RUNNING (PID: $(cat "$PID_FILE"))."
else
    echo "🔴 Auto-sync daemon is STOPPED."
fi

if [ -f "$LOG_FILE" ]; then
    echo ""
    echo "📜 Recent log output (last 10 lines):"
    echo "-------------------------------------"
    tail -n 10 "$LOG_FILE"
fi
