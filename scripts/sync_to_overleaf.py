#!/usr/bin/env python3
"""
Sync citrus disease classification manuscript and figures to Overleaf.
Locked exclusively to project ID: 6a9bddc9c9b98e33cf78aed2
"""

import os
import sys
import pickle
import requests
import bs4
from pathlib import Path

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
    session.headers.update({"User-Agent": "Mozilla/5.0 citrus-overleaf-sync"})

    # 1. Fetch CSRF token and editor info
    print(f"🔄 Connecting to Overleaf project: {PROJECT_ID}...")
    resp = session.get(f"https://www.overleaf.com/project/{PROJECT_ID}")
    if resp.status_code != 200:
        print(f"❌ Error: Failed to open project ({resp.status_code}). Session may have expired.")
        sys.exit(1)

    soup = bs4.BeautifulSoup(resp.content, "html.parser")
    csrf_meta = soup.find("meta", {"name": "ol-csrfToken"})
    if not csrf_meta:
        print("❌ Error: Could not extract CSRF token.")
        sys.exit(1)
    csrf = csrf_meta.get("content")

    # 2. Get project root folder and figures folder ID
    from overleaf_mcp.tools.olsync import _fetch_project_tree
    tree_res = _fetch_project_tree(session, PROJECT_ID)
    if not tree_res.ok or not tree_res.data:
        print(f"⚠️ Warning: Could not fetch socket tree, checking entities directly...")
        root_folder_id = None
        figures_folder_id = None
    else:
        root_folder = tree_res.data.get("rootFolder", [{}])[0]
        root_folder_id = root_folder.get("_id")
        figures_folder_id = None
        for f in root_folder.get("folders", []):
            if f.get("name") == "figures":
                figures_folder_id = f.get("_id")
                break

    # If figures folder doesn't exist, create it
    if not figures_folder_id:
        create_fol = session.post(
            f"https://www.overleaf.com/project/{PROJECT_ID}/folder",
            headers={"X-Csrf-Token": csrf},
            json={"name": "figures", "parent_folder_id": root_folder_id}
        )
        if create_fol.status_code == 200:
            figures_folder_id = create_fol.json().get("_id")

    # 3. Target files to sync
    root_files = ["main.tex", "references.bib", "ijcaArticle.cls", "ijcaArticle.bst"]
    figure_files = sorted([p.name for p in (BASE_DIR / "figures").glob("*.png")])

    print(f"📤 Uploading {len(root_files)} root files...")
    for rf in root_files:
        fpath = BASE_DIR / rf
        if not fpath.exists():
            continue
        content = fpath.read_bytes()
        up = session.post(
            f"https://www.overleaf.com/project/{PROJECT_ID}/upload",
            params={"folder_id": root_folder_id, "_csrf": csrf},
            data={"name": rf, "relativePath": "null"},
            files={"qqfile": (rf, content, "application/octet-stream")},
            headers={"X-Csrf-Token": csrf, "X-Requested-With": "XMLHttpRequest"}
        )
        if up.status_code == 200:
            print(f"  ✅ {rf}")
        else:
            print(f"  ⚠️ {rf} -> {up.status_code}")

    print(f"📤 Uploading {len(figure_files)} figure assets...")
    for ff in figure_files:
        fpath = BASE_DIR / "figures" / ff
        content = fpath.read_bytes()
        up = session.post(
            f"https://www.overleaf.com/project/{PROJECT_ID}/upload",
            params={"folder_id": figures_folder_id, "_csrf": csrf},
            data={"name": ff, "relativePath": "null"},
            files={"qqfile": (ff, content, "image/png")},
            headers={"X-Csrf-Token": csrf, "X-Requested-With": "XMLHttpRequest"}
        )
        if up.status_code == 200:
            print(f"  ✅ figures/{ff}")
        else:
            print(f"  ⚠️ figures/{ff} -> {up.status_code}")

    print(f"\n🎉 Sync complete! All files up-to-date on Overleaf.")

if __name__ == "__main__":
    main()
