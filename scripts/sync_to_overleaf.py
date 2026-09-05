#!/usr/bin/env python3
"""
Full CRUD Mirror Sync for Citrus Disease Classification Manuscript to Overleaf.
Locked exclusively to Overleaf Project ID: 6a9bddc9c9b98e33cf78aed2

Features:
- Create (C): Uploads newly added local manuscript or figure files.
- Read / Compare (R): Tracks remote tree vs local files.
- Update (U): Replaces modified files in place.
- Delete (D): Removes remote files on Overleaf if deleted locally.
"""

import os
import sys
import fnmatch
import hashlib
import pickle
from pathlib import Path
import bs4
import requests

PROJECT_ID = "6a9bddc9c9b98e33cf78aed2"
BASE_DIR = Path(__file__).resolve().parent.parent

def get_local_files_to_sync():
    """Scan local repo and filter by .olignore to get exact list of files to keep on Overleaf."""
    olignore_path = BASE_DIR / ".olignore"
    ignore_patterns = []
    if olignore_path.exists():
        with open(olignore_path, "r") as f:
            ignore_patterns = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    local_files = {}
    for p in BASE_DIR.rglob("*"):
        if p.is_file():
            rel_path = p.relative_to(BASE_DIR).as_posix()
            # Check if ignored
            if any(fnmatch.fnmatch(rel_path, pat) or fnmatch.fnmatch(p.name, pat) for pat in ignore_patterns):
                continue
            # Double check: only sync manuscript source and figure assets
            if rel_path.startswith(".") or rel_path.startswith("scripts/") or rel_path.startswith("submission-guide/") or rel_path.startswith("diagrams/") or rel_path.startswith("docs/"):
                continue
            local_files[rel_path] = p
    return local_files

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
    session.headers.update({"User-Agent": "Mozilla/5.0 citrus-crud-sync"})

    # 1. Fetch CSRF token
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
    headers = {"X-Csrf-Token": csrf, "X-Requested-With": "XMLHttpRequest"}

    # 2. Fetch project tree from socket / REST
    from overleaf_mcp.tools.olsync import _fetch_project_tree
    tree_res = _fetch_project_tree(session, PROJECT_ID)
    if not tree_res.ok or not tree_res.data:
        print(f"❌ Error fetching Overleaf project tree: {tree_res.error}")
        sys.exit(1)

    root_folder = tree_res.data.get("rootFolder", [{}])[0]
    root_folder_id = root_folder.get("_id")

    # Build remote map of {relative_path: (type, id, folder_id)}
    remote_files = {}
    folder_map = {"": root_folder_id}  # rel_dir -> folder_id

    # Root docs & fileRefs
    for d in root_folder.get("docs", []):
        remote_files[d["name"]] = ("doc", d["_id"], root_folder_id)
    for f in root_folder.get("fileRefs", []):
        remote_files[f["name"]] = ("file", f["_id"], root_folder_id)

    # Subfolders
    for sub in root_folder.get("folders", []):
        fol_name = sub["name"]
        fol_id = sub["_id"]
        folder_map[fol_name] = fol_id
        for d in sub.get("docs", []):
            remote_files[f"{fol_name}/{d['name']}"] = ("doc", d["_id"], fol_id)
        for f in sub.get("fileRefs", []):
            remote_files[f"{fol_name}/{f['name']}"] = ("file", f["_id"], fol_id)

    local_files = get_local_files_to_sync()

    # 3. DELETE phase: Remove files from Overleaf that no longer exist locally
    deleted_count = 0
    for rem_path, (ent_type, ent_id, fol_id) in remote_files.items():
        if rem_path not in local_files:
            endpoint = "doc" if ent_type == "doc" else "file"
            del_resp = session.delete(f"https://www.overleaf.com/project/{PROJECT_ID}/{endpoint}/{ent_id}", headers=headers)
            if del_resp.status_code in (200, 204):
                print(f"  🗑️  Deleted from Overleaf: {rem_path}")
                deleted_count += 1
            else:
                print(f"  ⚠️  Failed to delete {rem_path}: {del_resp.status_code}")

    # 4. CREATE & UPDATE phase: Upload new and modified files
    uploaded_count = 0
    for rel_path, local_path in sorted(local_files.items()):
        # Determine parent folder
        rel_dir = os.path.dirname(rel_path)
        file_name = os.path.basename(rel_path)

        # Create remote folder if missing
        if rel_dir and rel_dir not in folder_map:
            create_fol = session.post(
                f"https://www.overleaf.com/project/{PROJECT_ID}/folder",
                headers=headers,
                json={"name": rel_dir, "parent_folder_id": root_folder_id}
            )
            if create_fol.status_code == 200:
                folder_map[rel_dir] = create_fol.json().get("_id")
                print(f"  📁 Created remote folder: {rel_dir}/")

        target_folder_id = folder_map.get(rel_dir, root_folder_id)
        content = local_path.read_bytes()
        mime_type = "image/png" if rel_path.endswith(".png") else "application/octet-stream"

        up_resp = session.post(
            f"https://www.overleaf.com/project/{PROJECT_ID}/upload",
            params={"folder_id": target_folder_id, "_csrf": csrf},
            data={"name": file_name, "relativePath": "null"},
            files={"qqfile": (file_name, content, mime_type)},
            headers=headers
        )
        if up_resp.status_code == 200 and up_resp.json().get("success"):
            print(f"  ✅ Synced: {rel_path}")
            uploaded_count += 1
        else:
            print(f"  ⚠️ Failed to sync {rel_path}: {up_resp.status_code} {up_resp.text[:100]}")

    print(f"\n✨ CRUD Sync complete: {uploaded_count} synced, {deleted_count} removed.")

if __name__ == "__main__":
    main()
