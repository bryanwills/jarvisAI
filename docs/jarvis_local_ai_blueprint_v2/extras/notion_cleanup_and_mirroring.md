# Notion Cleanup & Mirroring to Markdown
**Goal:** Keep Markdown as canonical, mirror into Notion for UI/embeds.

## Cleanup Plan
- Create a **Home** page with 5 links: Dashboard, Projects, Notes, Recipes, Archive.  
- Standardize databases:
  - **Projects**: status, due, tags, repo link.  
  - **Notes**: tags, source, related project.  
  - **Recipes**: ingredients, steps, tags, images.
- Archive unused templates; keep a small curated set.

## Mirroring
- From VM, a script exports changed Markdown → Notion via API (or MCP tool).  
- Attach source path metadata so you can trace back to disk.  
- Prefer one-way sync initially to avoid conflicts.
