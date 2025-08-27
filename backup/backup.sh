#!/usr/bin/env bash
set -euo pipefail

STAMP=$(date +%F)
BACKUP_DIR=/backup/$STAMP
mkdir -p "$BACKUP_DIR"

echo "[*] Dumping Postgres databases..."
PGPASSWORD=${PGPASSWORD:-change-me} pg_dump -U ${PGUSER:-jarvis} -h ${PGHOST:-db} -F c -f "$BACKUP_DIR/jarvis.dump" ${PGDATABASE:-jarvis}

if command -v rclone >/dev/null 2>&1; then
  echo "[*] Uploading to Supabase via rclone..."
  rclone copy "$BACKUP_DIR" "${RCLONE_REMOTE:-supabase}:${RCLONE_BUCKET:-jarvis-backups}/$STAMP/"
else
  echo "[!] rclone not found; skipping remote upload."
fi

echo "[✓] Backup complete: $BACKUP_DIR"
