# Step 20 — Security & Backups
**Goal:** Local-first privacy with reliable backups.

## Security
- VLAN for AI servers; firewall allow from Mac and VPS only.  
- Tailscale for remote access; disable public exposure.  
- Secrets in Vaultwarden/HashiCorp Vault.

## Backups
Nightly:
```bash
# pg_dump
PGPASSWORD=change-me pg_dump -U jarvis -h db -F c -f /backup/jarvis_$(date +%F).dump jarvis
# rclone to Supabase (S3 compatible) – configure `rclone config` once
rclone copy /backup supabase:jarvis-backups/$(date +%F)/
```
Verify weekly restores on a test container.
