# Step 16 — vLLM on Threadripper + RTX 5090
**Goal:** High-throughput, OpenAI-compatible API.

## NVIDIA setup (Ubuntu)
Install NVIDIA drivers + CUDA, then `nvidia-container-toolkit`.

```bash
sudo apt-get update
sudo apt-get install -y nvidia-driver-555
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -fsSL https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list |   sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

## vLLM Docker
```bash
docker run --gpus all -p 8000:8000 --name vllm   -v /models:/models vllm/vllm-openai:latest   --model /models/llama-3-70b-instruct-q4 --max-model-len 8192
```

Reverse proxy at `https://llm.local/openai/v1`. Switch your apps by env var.
