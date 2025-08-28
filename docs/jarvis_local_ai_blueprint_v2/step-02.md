# Step 2 — Hardware Plan & Storage Sizing
**Goal:** Decide where each workload runs.

## Now (R630)
- ESXi 8 → Ubuntu VM → Docker + Portainer.
- Run Postgres+pgvector, OpenWebUI, ingestion service, n8n, and small models (Ollama) for dev.
- Store **models/embeddings** on local SSD if possible (fast). NAS for archives.

## Target (Threadripper 9000 Pro + RTX 5090)
- vLLM for high-throughput inference (OpenAI-compatible API).
- LoRA fine-tuning with Axolotl/Unsloth.
- NVMe Gen4 RAID for models + embeddings; NAS for raw docs, screen recordings, backups.

## Sizing
- Models: 8B (4–12GB), 70B (35–90GB quant). LoRA: MB–GB.
- Embeddings: modest; plan a few GB.
- Video/image generation models (SDXL/Flux) can be tens of GB.
