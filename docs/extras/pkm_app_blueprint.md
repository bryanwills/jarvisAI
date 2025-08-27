# PKM App Blueprint (Electron + Next.js + TS + Prisma)
**Goal:** Start your own Obsidian/Notion-like app with **Markdown as the truth**.

## Architecture
- **Electron** shell + **Next.js** UI (React/TS).  
- **Prisma** to Postgres (optional), but store note bodies as Markdown files on disk.  
- Local HTTP API (for ingestion to read).  
- Sync via Syncthing/rclone outside the app.

## Features v0
- Vault browser (folders/files).  
- Editor (MD with frontmatter).  
- Tags, backlinks, quick add.  
- Search (local + vector optional later).

## Project Skeleton
```
pkm-app/
  apps/desktop-electron/
  apps/web-next/
  packages/ui/
  packages/shared/
```

## Next Steps
- Start with editor + file watcher.  
- Add hotkeys (quick capture).  
- Later: iPad Pencil support via a drawing/whiteboard component that exports to PNG+MD.
