# Step 12 — OpenWebUI
**Goal:** A local chat UI for testing.

## Docker Compose
```yaml
services:
  openwebui:
    image: ghcr.io/open-webui/open-webui:latest
    restart: unless-stopped
    environment:
      OLLAMA_BASE_URL: http://ollama:11434
    ports: ["3001:8080"]
    depends_on: [ollama]

  ollama:
    image: ollama/ollama:latest
    restart: unless-stopped
    volumes:
      - ollama:/root/.ollama
    ports: ["11434:11434"]
volumes:
  ollama:
```
