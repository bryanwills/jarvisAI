# Step 9 — RAG Indexes (LlamaIndex)
**Goal:** Build separate indexes and a router.

## Install
```bash
pip install llama-index pgvector
```

## Indexes
- Index A: **Notes/PKM/Blog**  
- Index B: **Code/Repos/Docs**  
- Use metadata filters (tags: `notes`, `code`, `recipes`, etc.).

## Router Query Engine
Let the system pick an index based on the query. Add re-ranking if desired.

## Agentic RAG
- The agent can: refine queries → re-retrieve → call tools (MealForge, calendar) → produce final answer.  
- See `extras/agentic_rag.md` for patterns.
