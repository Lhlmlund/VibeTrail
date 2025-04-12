
# memory_builder.py

import os
import json
import argparse
import hashlib

def compute_file_hash(filepath):
    """Compute SHA-256 hash of a file's content."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def load_previous_hashes(hash_path):
    if os.path.exists(hash_path):
        with open(hash_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_current_hashes(hashes, hash_path):
    os.makedirs(os.path.dirname(hash_path), exist_ok=True)
    with open(hash_path, 'w', encoding='utf-8') as f:
        json.dump(hashes, f, indent=2)

def build_memory_file(branch, summaries_dir='summaries', memory_dir='memory'):
    branch_dir = os.path.join(summaries_dir, branch)
    memory_path = os.path.join(memory_dir, f"{branch}.gpt.md")
    hash_path = os.path.join(memory_dir, "hashes", f"{branch}.json")

    if not os.path.exists(branch_dir):
        print(f"❌ No summaries found for branch: {branch}")
        return

    os.makedirs(memory_dir, exist_ok=True)
    previous_hashes = load_previous_hashes(hash_path)
    current_hashes = {}

    with open(memory_path, 'w', encoding='utf-8') as mem_file:
        mem_file.write(f"# GPT Project Memory — Branch: {branch}\n\n---\n\n")

        for filename in os.listdir(branch_dir):
            if not filename.endswith('.json'):
                continue

            json_path = os.path.join(branch_dir, filename)
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            file_path = data.get("file")
            summary = data.get("summary", "No summary available")
            if not file_path or not os.path.exists(file_path):
                continue

            current_hash = compute_file_hash(file_path)
            current_hashes[file_path] = current_hash

            if previous_hashes.get(file_path) == current_hash:
                print(f"⏩ Skipping unchanged: {file_path}")
                continue

            print(f"🧠 Adding to memory: {file_path}")
            mem_file.write(f"## File: {file_path}\n\n")
            mem_file.write("**Summary:**\n")
            mem_file.write(summary.strip() + "\n\n---\n\n")

    save_current_hashes(current_hashes, hash_path)
    print(f"✅ Memory file updated at: {memory_path}")
    print(f"🔐 Hashes saved at: {hash_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build GPT-compatible memory file from JSON summaries.")
    parser.add_argument('--branch', type=str, required=True, help="Git branch name to load summaries from.")
    args = parser.parse_args()

    build_memory_file(args.branch)
