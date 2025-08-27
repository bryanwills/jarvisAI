# Step 18 — Cost & Growth (Start Free → Migrate)
**Goal:** Concrete path with migration details.

## Start Free (R630 + Mac)
- **Run**: Postgres+pgvector, ingestion service, OpenWebUI, n8n on the Ubuntu VM.  
- **Dev inference**: Ollama on the VM (or on Mac if you prefer).  
- **ActivityWatch**: Mac-only watchers; export JSON to VM nightly.  
- **Backups**: pg_dump to NAS (when powered) + rclone to Supabase.

## Exact setup steps
1. Create Ubuntu VM (8 vCPU, 16GB RAM, 200GB SSD).  
2. Install Docker + Portainer; deploy `db.yml` (Step 5).  
3. Deploy `openwebui + ollama` compose (Step 12) or run Ollama system-wide.  
4. Deploy **ingestion** FastAPI (Step 6) + watchers (Step 7).  
5. Install ActivityWatch on Mac; daily export → VM script (Step 8).  
6. Wire **LlamaIndex** (Step 9) + **LangChain** agents (Step 10).  
7. Add n8n flows (Step 14) + Focus Coach (Step 15).

## Migrate Inference & LoRA to 5090
1. Stand up 5090 box; install NVIDIA drivers + `nvidia-container-toolkit`.  
2. Create `/models` on NVMe RAID; download quant models.  
3. Run **vLLM** Docker with OpenAI-compatible API (Step 16).  
4. Change your **LLM_BASE_URL** env var in OpenWebUI, LangChain, LlamaIndex from Ollama → vLLM.  
5. Install Axolotl/Unsloth; mount training data; run LoRA to produce adapter in `/models/adapters/...`.  
6. Update inference config to **load adapter** (or keep LoRA for certain agents only).  
7. Keep **RAG DB** on R630 or move to 5090 NVMe (recommended). Update connection strings.
