# Step 11 — Inference (Ollama – Dev)
**Goal:** Local dev-friendly inference.

## Install on Ubuntu VM
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve
```

## Pull a model
```bash
ollama pull llama3:8b
```

Point your tools/UI to `http://ollama.local:11434`. Use it until the 5090 arrives, then switch to vLLM.
