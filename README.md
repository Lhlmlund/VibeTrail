# 🚀 VibeTrail – AI-Assisted Code Memory for Developers

**VibeTrail** is an intelligent Git-integrated companion that automatically summarizes and tracks your evolving codebase — powered by AI. Whether you're branching out or deep in the zone, VibeTrail ensures your project's memory is always clear, updated, and accessible.

---

## 🔧 Getting Started

### 📥 Clone & Set Up
```bash
git clone https://github.com/your-org/vibetrail-project.git
cd vibetrail-project

# Install Git hooks (tracked in .vibe-hooks/)
python setup_hooks.py
```

---

## 🧪 (Optional) Initial Memory Scan on Main
```bash
# Generate summaries and build memory for the main branch
python src/runner.py --mock --limit 20 --branch main
python memory_builder.py --branch main
```

---

## 🌿 Ideal Branch Workflow

```bash
# Create or switch to a new branch
git checkout -b feature/amazing-idea

# Summarize files in the new branch
python src/runner.py --branch feature-amazing-idea

# (Optional) Generate memory for the new branch
python memory_builder.py --branch feature-amazing-idea

# Now commit as usual
git add .
git commit -m "Initial work"
```

---

## 🧠 Ownership & Origin

> *VibeTrail* is an original open-source AI development tool created by **Linus Holmlund**, 2025.  
> This repository serves as the official source of truth and first public use of the name and project.

© 2025 Linus Holmlund – All rights reserved.

---

### 🌄 Optional ASCII Banner (Add to your terminal header or README flair)
```text
╔════════════════════════════════════╗
║        🧠 VibeTrail Ascent        			║
║   Track your path. Remember the code.   		║
╚════════════════════════════════════╝
```

---

## 🧭 Next Steps

- Add your `LICENSE` to the root directory
- Set up your domain: `vibetrail.ai` or `vibetrail.dev`
- Begin sharing with confidence — this is your trail now


🌐 Official site: [https://vibetrail.dev](https://vibetrail.dev)

---
