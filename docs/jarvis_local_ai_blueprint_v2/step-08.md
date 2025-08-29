# Step 8 — Activity Monitoring (ActivityWatch)
**Goal:** Track focus vs distraction without heavy GPU use.

## On Mac (lightweight)
- Install ActivityWatch. Enable watchers for window titles, browser URLs.  
- Export daily JSON or push to VM via a small script at day-end.

## Daily Summaries
- Cron on VM at 18:00: pull day’s raw events → produce summary (Python) → ingest as `summaries` and as RAG document.

```python
# summarize_activity.py (pseudo)
# read raw JSON, compute focus ratio, top apps/urls, time blocks
summary = {
  "focus_ratio": 0.62,
  "top_apps": ["code","terminal","youtube"],
  "breaks": [{"start":"11:30","end":"11:50"}]
}
# insert into summaries table and also POST /ingest with a markdown text
```
