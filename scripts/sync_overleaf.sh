#!/usr/bin/env bash
set -e

# STRICT CONFIGURATION: Locked exclusively to this citrus disease classification paper
PROJECT_NAME="Comparative Performance and Computational Complexity Analysis of Pre-Trained Deep Learning Models for Citrus Fruit Disease Classification"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

if [ ! -f ".olauth" ]; then
    echo "🔑 Overleaf session not found. Please authenticate with 'ols login'."
    exit 1
fi

echo "🚀 Syncing local manuscript files exclusively to Overleaf project: '$PROJECT_NAME'..."
ols -l -n "$PROJECT_NAME"

echo "✅ Sync completed successfully!"
