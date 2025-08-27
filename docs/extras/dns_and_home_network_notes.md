# DNS & Home Network Notes
- AT&T gateway limits custom DNS → rely on `hosts` file or Tailscale MagicDNS for now.  
- Later with Ubiquiti: run Pi-hole/AdGuard Home internally; make your router hand them out via DHCP.  
- External Pi-hole on VPS helps road‑warrior devices but cannot resolve your **internal** hostnames unless you tunnel (Tailscale) and split DNS rules point *.local to the LAN resolver.
