#!/usr/bin/env python3
"""
Pull Overleaf Project to Local Repository.
Downloads the live project zip from Overleaf and updates local workspace files.
"""

import os
import sys
import io
import pickle
import zipfile
from pathlib import Path
import requests

PROJECT_ID = "6a9bddc9c9b98e33cf78aed2"
BASE_DIR = Path(__file__).resolve().parent.parent

def main():
    os.chdir(BASE_DIR)
    auth_file = BASE_DIR / ".olauth"
    
    if not auth_file.exists():
        print("❌ Error: .olauth session file not found. Please run 'ols login' first.")
        sys.exit(1)

    with open(auth_file, "rb") as f:
        auth = pickle.load(f)

    session = requests.Session()
    session.cookies.update(auth["cookie"])
    session.headers.update({"User-Agent": "Mozilla/5.0 citrus-pull-sync"})

    print("📥 Downloading live project from Overleaf...")
    resp = session.get(f"https://www.overleaf.com/project/{PROJECT_ID}/download/zip", timeout=120)
    
    if resp.status_code != 200:
        print(f"❌ Error downloading project zip from Overleaf: {resp.status_code}")
        sys.exit(1)

    try:
        zf = zipfile.ZipFile(io.BytesIO(resp.content))
    except Exception as e:
        print(f"❌ Error opening Overleaf zip: {e}")
        sys.exit(1)

    updated_count = 0
    identical_count = 0

    for name in zf.namelist():
        remote_bytes = zf.read(name)
        target_path = BASE_DIR / name
        
        # Ensure parent dirs exist
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        if target_path.exists() and target_path.read_bytes() == remote_bytes:
            identical_count += 1
            print(f"  ➖ Unchanged: {name}")
        else:
            target_path.write_bytes(remote_bytes)
            updated_count += 1
            print(f"  📥 Updated from Overleaf: {name}")

    print(f"\n✨ Pull Complete: {updated_count} updated, {identical_count} unchanged.")

if __name__ == "__main__":
    main()
