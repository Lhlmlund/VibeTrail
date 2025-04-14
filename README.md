# 🚀 VibeTrail – AI-Assisted Code Memory for Developers

**VibeTrail** is an intelligent Git-integrated companion that automatically summarizes and tracks your evolving codebase — powered by AI. Whether you're branching out or deep in the zone, VibeTrail ensures your project's memory is always clear, updated, and accessible.

---





## ⚙️ What it does:

 Scans your codebase and auto-summarizes relevant files

 Saves AI-friendly summaries in both Markdown and JSON

 Builds long-term GPT-compatible memory for ongoing conversations

 Keeps track of file changes with smart hashing

 Detects active Git branches for contextual tracking

 Hooks into Git pre-commit to update memory automatically

 Saves OpenAI tokens with offline/mock modes for testing


## 🌍 Why VibeTrail?
Use it to create the illusion of persistent AI memory — without relying on expensive cloud APIs or massive context windows.
It’s your trail map. Your memory vault. Your AI’s brain — powered by your repo.

Track your path. Remember the code.
🧠 VibeTrail.







## 🔧 Getting Started

### 📥 Clone & Set Up
```bash
git clone https://github.com/your-org/vibetrail-project.git
cd vibetrail-project

# Install Git hooks (tracked in .vibe-hooks/)
python setup_hooks.py
```

---

##  (Optional) Initial Memory Scan on Main
```bash
# Generate summaries and build memory for the main branch
python src/runner.py --mock --limit 20 --branch main
python memory_builder.py --branch main
```

---

##  Ideal Branch Workflow

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

##  Ownership & Origin

> *VibeTrail* is an original open-source AI development tool created by **Linus Holmlund**, 2025.  
> This repository serves as the official source of truth and first public use of the name and project.

© 2025 Linus Holmlund – All rights reserved.

---

### ASCII Banner
```text
╔════════════════════════════════════╗
║        🧠 VibeTrail Ascent        			║
║   Track your path. Remember the code.   		║
╚════════════════════════════════════╝
```

---

## 🌐 Official site: [https://vibetrail.dev](https://vibetrail.dev)

---
