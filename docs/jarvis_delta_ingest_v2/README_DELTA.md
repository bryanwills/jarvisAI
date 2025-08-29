# Delta Ingest Utilities

Date: 2025-08-27

This package provides an incremental ingestion script and schedules for your RAG pipeline.

## Install
```bash
sudo mkdir -p /opt/jarvis-ingest
sudo cp delta_ingest.py ingest.yaml /opt/jarvis-ingest/
sudo chmod +x /opt/jarvis-ingest/delta_ingest.py
```

## Run once
```bash
INGEST_API_URL=http://localhost:8001/ingest python3 /opt/jarvis-ingest/delta_ingest.py --config /opt/jarvis-ingest/ingest.yaml --profile hot
```

## systemd timers
```bash
sudo cp systemd/jarvis-delta@.service /etc/systemd/system/
sudo cp systemd/jarvis-delta-hot.timer /etc/systemd/system/
sudo cp systemd/jarvis-delta-warm.timer /etc/systemd/system/
sudo cp systemd/jarvis-delta-cold.timer /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable --now jarvis-delta-hot.timer
sudo systemctl enable --now jarvis-delta-warm.timer
sudo systemctl enable --now jarvis-delta-cold.timer

systemctl list-timers | grep jarvis-delta
```
