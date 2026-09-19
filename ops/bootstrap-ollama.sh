#!/bin/bash
# Run on a newly provisioned official Runpod PyTorch pod, once.
set -euo pipefail
mkdir -p /workspace/runtime /workspace/ssh-host-keys
chmod 700 /workspace/ssh-host-keys
cp -p /etc/ssh/ssh_host_* /workspace/ssh-host-keys/
curl -fsSL --retry 3 'https://ollama.com/download/ollama-linux-amd64.tar.zst?version=0.34.2' | zstd -d | tar -xf - -C /workspace/runtime
# Copy ops/start-model.sh and ops/boot-fulhouse.sh to /workspace before this step.
nohup bash /workspace/start-model.sh >/workspace/ollama.log 2>&1 </dev/null &
for n in $(seq 1 30); do
  if curl -fsS http://127.0.0.1:11434/api/version >/dev/null; then break; fi
  sleep 2
done
OLLAMA_HOST=127.0.0.1:11434 /workspace/runtime/bin/ollama pull nomic-embed-text:latest
OLLAMA_HOST=127.0.0.1:11434 /workspace/runtime/bin/ollama pull huihui_ai/qwen3-coder-abliterated:30b
# Only after completion, set Pod args to /workspace/boot-fulhouse.sh.
