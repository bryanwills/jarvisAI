# Step 4 — Repos & Tooling
**Goal:** Prepare repos and core tools you already use.

## Repos
- `jarvisAI` (your main repo): add a `/deploy` folder to hold compose files/envs.
- `jarvis-LLM-guy` fork: explore patterns; keep it separate to upstream PRs.

## IDE & AI Tools
- Cursor IDE (with MCP to filesystem/Notion).
- Claude Desktop/CLI (no API key usage for now), ChatGPT + API key.
- AgentOS, SST/opencode (optional accelerators).

## Wakatime / Code tracking
- Keep them; we’ll ingest daily summaries into RAG (step 8/14).

## Repo layout suggestion
```
jarvisAI/
  deploy/
    compose/           # docker-compose stacks
    env/               # .env samples
  ingestion/
    watchers/          # fswatch scripts
    services/          # API to chunk/embed/upsert
  orchestration/
    langchain/
    llamaindex/
  tools/
    n8n/
  docs/                # these .md files (or link to separate repo)
```
