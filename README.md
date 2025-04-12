# After cloning
git clone https://github.com/your-org/vibetrail-project.git
cd vibetrail-project

# Install VibeTrail Git hooks (tracked in .vibe-hooks/)
python setup_hooks.py

# (Optional) Generate initial summaries
python src/runner.py --mock --limit 20 --branch main
python memory_builder.py --branch main