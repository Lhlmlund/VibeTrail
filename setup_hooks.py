# setup_hooks.py

import os
import shutil
import stat

def make_executable(path):
    if os.name != 'nt':  # Unix
        st = os.stat(path)
        os.chmod(path, st.st_mode | stat.S_IEXEC)

def install_hooks(source=".vibe-hooks", target=".git/hooks"):
    if not os.path.isdir(source):
        print(f"❌ Source hook folder '{source}' not found.")
        return

    if not os.path.isdir(target):
        print(f"❌ Target Git hook folder '{target}' not found. Is this a Git repo?")
        return

    for hook_file in os.listdir(source):
        src_path = os.path.join(source, hook_file)
        dst_path = os.path.join(target, hook_file)

        shutil.copyfile(src_path, dst_path)
        make_executable(dst_path)
        print(f"✅ Installed hook: {hook_file}")

    print("🧠 All hooks installed successfully.")

if __name__ == "__main__":
    install_hooks()
