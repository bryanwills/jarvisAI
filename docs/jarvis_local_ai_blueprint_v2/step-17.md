# Step 17 — LoRA Fine-Tuning (Axolotl/Unsloth)
**Goal:** Periodic adapters for style/skills.

## Tooling
- Axolotl or Unsloth (choose one).  
- Training data: curated Q/A pairs, “great responses,” recipe style, coding conventions.

## Axolotl sample config (YAML)
```yaml
base_model: /models/llama-3-8b-instruct
output_dir: /models/adapters/llama3-8b-bryan-style
load_in_4bit: true
lora_r: 16
lora_alpha: 32
lora_dropout: 0.05
train_data:
  - /data/lora/train.jsonl  # each line: {"instruction":..., "input":..., "output":...}
epochs: 2
batch_size: 8
gradient_accumulation_steps: 4
learning_rate: 2e-4
```
Load adapters at runtime; keep RAG as primary knowledge.
