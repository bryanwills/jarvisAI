# Step 13 — Second Brain / PKM (Vault + Sync + Notion)
**Goal:** Markdown vault as the source of truth. No Docker on Mac.

## Vault
- Use `~/SecondBrain` on Mac. Folders: `inbox/ notes/ projects/ journal/ recipes/ code-snippets/`.
- Edit with your preferred editor (Cursor, VSCode, or a lightweight Markdown app).

## Sync
- **Syncthing** Mac ↔ R630 VM (real-time, free).  
- From VM → **Google Drive** via **rclone** nightly.

## Notion mirror
- Periodic export/import workflow: R630 pulls from vault → pushes to Notion via API (MCP or custom script).  
- See `extras/notion_cleanup_and_mirroring.md` for a clean Notion structure.

## Ingestion
- The VM watches the vault mirror and posts to `/ingest` (Step 7).

## Bonus
- Optionally open the vault with Obsidian/Logseq/Joplin on iOS/macOS; keep **Markdown** canonical.
