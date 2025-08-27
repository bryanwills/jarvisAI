# Agentic RAG – Deep Dive & Patterns
**Idea:** Let an agent coordinate retrieval + tools over multiple turns to achieve goals.

## Core Loop
1) Analyze query → 2) Choose index/tool → 3) Retrieve → 4) Reason → 5) If uncertain, refine query/choose a different index → 6) (Optional) call an action tool (MealForge, n8n) → 7) Finalize.

## Patterns
- **Router-first**: classify to Notes vs Code index.  
- **Multi-hop**: retrieve summary → follow links → deeper retrieval.  
- **Cite & ground**: always include top-k sources back to the user.  
- **Plan-then-act**: generate a plan, show to user, then execute tools.  

Use **LangGraph** to make this reliable; store state (messages, chosen tools) for auditability.
