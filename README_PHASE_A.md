# Phase A Stack (Docker)

Date: 2025-08-27

Services:
- **db**: Postgres + pgvector
- **ingestion**: FastAPI embeddings & upsert API
- **ollama**: Local LLM server (dev)
- **openwebui**: Chat UI
- **n8n**: Automations (configured for n8n.bryanwills.dev)

## Quickstart
```bash
cp .env.example .env
# Edit .env and set secure passwords/secrets

docker compose up -d --build

# Pull a small model for dev
docker exec -it jarvis_ollama ollama pull llama3:8b

# Health checks
curl http://localhost:8001/health
open http://localhost:3001    # OpenWebUI
open http://localhost:5678    # n8n
```

### Notes
- Prisma manages metadata tables. Vector search uses raw SQL against `chunks.embedding` (pgvector). You can add a small service method to run similarity search:
```sql
SELECT id, document_id, chunk_idx, 1 - (embedding <=> $1) AS score
FROM chunks
ORDER BY embedding <-> $1
LIMIT 5;
```
- Supabase backups: edit `backup/backup.sh` and add a cron on the VM.
