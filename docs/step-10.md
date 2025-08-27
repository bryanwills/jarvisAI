# Step 10 — Agents & Tools (LangChain/LangGraph)
**Goal:** Give Jarvis actions.

## Install
```bash
pip install langchain langgraph requests psycopg2-binary
```

## Tools
- `search_notes` — SQL + vector search with filters.  
- `mealforge` — HTTP calls to MealForge service.  
- `remind` — call n8n webhook.  
- `calendar` — read/write ICS or local CalDAV.

## LangGraph
Define a state machine: retrieve → reason → decide tools → act → finalize.  
Keep **side effects** (reminders, edits) behind explicit user approval until you trust it.
