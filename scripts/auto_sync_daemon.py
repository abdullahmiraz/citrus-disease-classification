#!/usr/bin/env python3
"""
Continuous Background Auto-Sync Daemon for Citrus Paper Repository:
- Overleaf Sync: Triggers 30 seconds after any manuscript/figure file change.
- Git & GitHub Sync: Auto-commits and pushes 10 minutes after any repository changes.
"""

import os
import sys
import time
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OVERLEAF_SCRIPT = BASE_DIR / "scripts" / "sync_to_overleaf.py"
PYTHON_BIN = "/home/neo/.local/share/uv/tools/overleaf-latex-mcp/bin/python"
sys.path.insert(0, str(BASE_DIR / "scripts"))
from sync_to_overleaf import get_local_files_to_sync

def get_overleaf_state():
    """Return dictionary of {rel_path: (size, mtime)} for all local files destined for Overleaf."""
    local_map = get_local_files_to_sync()
    state = {}
    for rel_path, p in local_map.items():
        if p.exists():
            stat = p.stat()
            state[rel_path] = (stat.st_size, stat.st_mtime)
    return state

def check_git_dirty():
    try:
        res = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            check=True
        )
        return bool(res.stdout.strip())
    except Exception:
        return False

def sync_to_overleaf():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ⚡ Auto-syncing changes to Overleaf...")
    try:
        res = subprocess.run(
            [PYTHON_BIN, str(OVERLEAF_SCRIPT)],
            cwd=BASE_DIR,
            capture_output=True,
            text=True
        )
        if res.returncode == 0:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ✅ Overleaf sync completed successfully.")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ⚠️ Overleaf sync output:\n{res.stderr or res.stdout}")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ❌ Overleaf sync error: {e}")

def git_commit_and_push():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 🚀 Auto-committing and pushing changes to GitHub...")
    try:
        subprocess.run(["git", "add", "-A"], cwd=BASE_DIR, check=True)
        # Check if there are staged changes
        staged = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=BASE_DIR)
        if staged.returncode != 0:
            msg = f"auto: periodic update ({time.strftime('%Y-%m-%d %H:%M:%S')})"
            subprocess.run(["git", "commit", "-m", msg], cwd=BASE_DIR, check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, check=True)
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ✅ Git push completed.")
        else:
            # Check unpushed commits
            unpushed = subprocess.run(["git", "log", "origin/main..HEAD", "--oneline"], cwd=BASE_DIR, capture_output=True, text=True)
            if unpushed.stdout.strip():
                subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, check=True)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ✅ Unpushed commits sent to GitHub.")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ❌ Git auto-push error: {e}")

def main():
    print("=" * 60)
    print("🤖 Citrus Research Paper Auto-Sync Daemon Started")
    print(f"📂 Workspace: {BASE_DIR}")
    print("⏱️  Overleaf auto-sync: 30s debounce after changes")
    print("⏱️  Git/GitHub auto-push: 10m debounce after changes")
    print("=" * 60)

    last_overleaf_state = get_overleaf_state()
    overleaf_change_time = None

    git_change_time = None
    last_git_dirty = check_git_dirty()

    OVERLEAF_DELAY = 30   # 30 seconds
    GIT_DELAY = 600       # 10 minutes (600 seconds)

    while True:
        try:
            time.sleep(2)
            now = time.time()

            # 1. Check Overleaf file changes (CRUD)
            current_state = get_overleaf_state()
            if current_state != last_overleaf_state:
                last_overleaf_state = current_state
                overleaf_change_time = now
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 📝 Detected manuscript changes (CRUD). Syncing to Overleaf in 30s...")

            # Trigger Overleaf sync when 30s has passed since last change
            if overleaf_change_time is not None and (now - overleaf_change_time >= OVERLEAF_DELAY):
                sync_to_overleaf()
                overleaf_change_time = None
                last_overleaf_state = get_overleaf_state()

            # 2. Check Git changes
            current_git_dirty = check_git_dirty()
            if current_git_dirty and not last_git_dirty:
                git_change_time = now
                last_git_dirty = True
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 📝 Detected Git repository changes. Auto-pushing to GitHub in 10m...")
            elif not current_git_dirty:
                last_git_dirty = False

            # Trigger Git commit & push when 10m has passed since first detected change
            if git_change_time is not None and (now - git_change_time >= GIT_DELAY):
                if check_git_dirty():
                    git_commit_and_push()
                git_change_time = None
                last_git_dirty = check_git_dirty()

        except KeyboardInterrupt:
            print("\n👋 Auto-sync daemon stopped.")
            break
        except Exception as e:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Loop exception: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
