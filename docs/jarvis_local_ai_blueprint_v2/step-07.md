# Step 7 — Ingestion Pipeline (Files, GitHub, OCR)
**Goal:** Automate data flow into RAG.

## Files (Mac → Server)
- Use **Syncthing** between Mac and R630 to mirror `~/SecondBrain` and selected project folders to the VM.  
- On the VM, a small watcher (inotifywait) calls `/ingest` for changed files.

```bash
# On Ubuntu VM:
sudo apt-get update && sudo apt-get install -y inotify-tools jq

watch_dir=/data/ingest
while inotifywait -r -e modify,create,move,close_write "$watch_dir"; do
  find "$watch_dir" -type f -mmin -1 | while read f; do
    text=$(sed 's/\r$//' "$f")
    jq -n --arg path "$f" --arg text "$text" '{path:$path, text:$text, type:"file", source:"vault"}'       | curl -s -X POST http://ingest.local:8001/ingest -H "Content-Type: application/json" -d @-
  done
done
```

## GitHub
- Use a cron to `git pull` your repos mirror on the VM; on change → ingest diffs and new files.

## OCR for images/PDFs
- Install **tesseract** on VM; pre-process PDFs/images → text → ingest.
