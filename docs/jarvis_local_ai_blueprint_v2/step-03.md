# Step 3 — Networking & DNS Baseline
**Goal:** Reach services reliably from your Mac without running Docker on it.

## Recommended
- **Tailscale**: private mesh to your R630 VM and (later) 5090 box.
- **Reverse proxy**: Traefik or Nginx on the Ubuntu VM. Terminate TLS locally with your domain.
- **Split DNS** later when Ubiquiti arrives. For now, add to `/etc/hosts` on Mac for internal testing:
```bash
sudo nano /etc/hosts
172.16.1.50   llm.local db.local openwebui.local n8n.local
```

## ESXi UI Access
If `esxi.bryanwills.org` hangs due to AT&T DNS/gateway, prefer:
- Direct IP internally (e.g., `https://172.16.1.34`)
- Or Tailscale “MagicDNS” with a stable hostname.
See `extras/dns_and_home_network_notes.md`.
