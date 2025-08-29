# Step 14 — n8n Automations
**Goal:** Wire common workflows.

## Examples
- `create_reminder` (webhook) → macOS notif / email / SMS.  
- `log_meal` → insert into `events` + update `summaries`.  
- `daily_digest` (cron 18:00) → summarize activity + notes → save to DB + push a digest.  
- `mealforge_pipeline` → recipe suggestions + shopping list.

Expose **only inside LAN/Tailscale** with basic auth.
