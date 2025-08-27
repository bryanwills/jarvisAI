# Git Instructions – Add Docs & Phase A Stack

Use these steps on your workstation where you have access to GitHub.

```bash
# 1) Clone your repo
git clone https://github.com/bryanwills/jarvisAI.git
cd jarvisAI

# 2) Create a docs branch and add the Markdown docs from the previous ZIP
git checkout -b docs/bundle-v2
# Place the contents of jarvis_local_ai_blueprint_v2.zip into ./docs/
git add docs
git commit -m "docs: add full implementation plan and 21 detailed steps"
git push -u origin docs/bundle-v2
# gh pr create --fill --assignee @bryanwills --base main --head docs/bundle-v2

# 3) Create a stack branch and add this Phase A stack
git checkout -b feat/phase-a-stack
unzip ~/Downloads/jarvis_phaseA_stack_v2.zip -d .
git add docker-compose.yml ingestion prisma deploy .env.example backup
git commit -m "feat(stack): Phase A docker stack (db, ollama, openwebui, ingestion, n8n) + prisma schema + backup"
git push -u origin feat/phase-a-stack
# gh pr create --fill --assignee @bryanwills --base main --head feat/phase-a-stack
```
