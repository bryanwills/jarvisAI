# Step 1 — Key Concepts & Choices
**Goal:** Align on how you’ll “teach” the model and keep it current.

## Concepts
- **Training from scratch:** impractical for solo devs.
- **Fine-tuning:** use **LoRA/QLoRA** adapters to nudge behavior/style/skills. Trained periodically.
- **RAG:** continuously index your data (notes, code, logs) into a vector DB. At query time, retrieve relevant chunks.
- **Agentic RAG:** multi-step reasoning with retrieval + tools.

## Your Strategy
- Rely on **RAG** for knowledge freshness (daily ingestion).
- Use **LoRA** occasionally to codify your tone, coding style, MealForge prompt style, etc.
- Keep everything **local** for privacy; back up personal data only.
