# src/scanner.py

import os
import json

def load_config(config_path="vibetrail.config.json"):
    with open(config_path, 'r') as f:
        return json.load(f)

def scan_directory(config):
    base_path = os.path.abspath(config["scan_path"])
    ignore_dirs = set(config.get("ignore_dirs", []))
    allowed_extensions = set(config.get("allowed_extensions", []))

    print(f"📂 Scanning base path: {base_path}")
    print(f"⛔ Ignoring folders: {ignore_dirs}")
    print(f"✅ Allowed extensions: {allowed_extensions}")

    collected_files = []

    for root, dirs, files in os.walk(base_path):
        print(f"🔎 Searching: {root}")
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            if any(file.endswith(ext) for ext in allowed_extensions):
                full_path = os.path.join(root, file)
                collected_files.append(full_path)

    return collected_files

# Example usage
if __name__ == "__main__":
    config = load_config()
    files = scan_directory(config)
    for f in files:
        print(f)
