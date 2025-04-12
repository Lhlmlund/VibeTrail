# src/runner.py

import argparse
from scanner import scan_directory, load_config
from summarizer import summarize_file, config as summarizer_config
from writer import write_summary
import subprocess


def get_git_branch():
    try:
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], stderr=subprocess.DEVNULL
        )
        return branch.decode("utf-8").strip()
    except Exception:
        return None


def main():
    # CLI flags
    parser = argparse.ArgumentParser(description="Run VibeTrail AI summarizer.")
    parser.add_argument("--mock", action="store_true", help="Run in mock mode (no OpenAI usage)")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of files to summarize")
    parser.add_argument("--branch", type=str, help="Override Git branch name")
    args = parser.parse_args()

    # Load and merge config
    config = load_config()

    # Get Git branch (or override from CLI)
    branch_name = args.branch or get_git_branch() or "no-git"

    # Pretty print
    print("\n==============================")
    if branch_name != "no-git":
        print(f"🌿 Git branch detected: {branch_name}")
    else:
        print("🌿 Git branch not detected (not in a Git repo)")
    print("==============================\n")

    config["branch_name"] = branch_name
    config["mock_ai"] = args.mock or config.get("mock_ai", False)
    config["file_limit"] = args.limit

    summarizer_config.update(config)

    print(f"🔍 Scanning directory: {config['scan_path']}")
    files = scan_directory(config)

    if config["file_limit"]:
        files = files[:config["file_limit"]]
        print(f"🔎 Limiting to first {config['file_limit']} files.")

    print(f"🧾 Files to summarize: {len(files)}")

    for i, file_path in enumerate(files):
        print(f"[{i+1}/{len(files)}] 🧠 Summarizing: {file_path}")
        summary = summarize_file(file_path)

        print(f"✅ Summary returned: {summary is not None}")
        if summary:
            print(f"📝 Summary preview: {summary[:60].strip()}...")
            write_summary(file_path, summary, branch_name=branch_name)
        else:
            print(f"⚠️ Skipped (no summary): {file_path}")

    print("\n✅ All summaries generated. You’ll find them in:")
    print(f"📁 summaries/{branch_name}/\n")


if __name__ == "__main__":
    main()
