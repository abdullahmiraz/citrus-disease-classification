#!/usr/bin/env bash
set -e

# Citrus Fruit Disease Classification manuscript on Overleaf
OVERLEAF_PROJECT_ID="6a9bddc9c9b98e33cf78aed2"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

if [ ! -f ".olauth" ]; then
    echo "🔑 Overleaf session not found. Please run 'ols login' first."
    exit 1
fi

echo "🚀 Syncing manuscript files to Overleaf project ID: $OVERLEAF_PROJECT_ID..."
ols -l -n "$OVERLEAF_PROJECT_ID"

echo "✅ Sync complete!"
