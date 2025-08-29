# jarvisAI – README (Skeleton)
**Mission:** Local, private “Jarvis” using RAG + LoRA.  
**Stacks:** Postgres/pgvector, LlamaIndex, LangChain/LangGraph, Ollama/vLLM, n8n, ActivityWatch.

## Quickstart
1. `docker compose -f deploy/compose/db.yml up -d`  
2. Start ingestion service (see /ingestion/services).  
3. Start OpenWebUI + Ollama (dev) or point to vLLM (prod).  
4. Configure env vars in `/deploy/env/*.env`.

## Roadmap
- Focus Coach, MealForge tools, LoRA adapters, “recipe→video” generator.
