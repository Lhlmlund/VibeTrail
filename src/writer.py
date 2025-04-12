# src/writer.py

import os
import json

def write_summary(file_path, summary, output_dir="summaries", branch_name="no-git"):
    # Create a clean, branch-specific subfolder
    branch_dir = os.path.join(output_dir, branch_name)
    os.makedirs(branch_dir, exist_ok=True)
    print(f"📁 Writing to branch folder: {branch_dir}")

    # Make filename safe and unique
    relative_path = os.path.relpath(file_path, start=os.getcwd())
    safe_filename = relative_path.replace('/', '__').replace('\\', '__')

    # MARKDOWN output
    md_path = os.path.join(branch_dir, f"{safe_filename}.md")
    print(f"📝 Writing markdown to: {md_path}")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Summary of `{file_path}`\n\n")
        f.write(f"**Branch:** `{branch_name}`\n\n")
        f.write(summary.strip() + "\n\n")

    # JSON output
    json_path = os.path.join(branch_dir, f"{safe_filename}.json")
    print(f"📦 Writing JSON to: {json_path}")
    json_data = {
        "file": file_path,
        "summary": summary,
        "branch": branch_name
    }
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)

    print(f"[✓] Saved summary (Markdown + JSON) under: {branch_dir}")
