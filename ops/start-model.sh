#!/usr/bin/env bash
set -euo pipefail
# Boot and controller recovery may race; only one server owns this local lock.
exec 9>/tmp/fulhouse-ollama.lock
flock -n 9 || exit 0
export OLLAMA_HOST=127.0.0.1:11434
export OLLAMA_MODELS=/workspace/ollama
export OLLAMA_CONTEXT_LENGTH=32768
export OLLAMA_NUM_PARALLEL=1
export LD_LIBRARY_PATH=/workspace/runtime/lib/ollama:${LD_LIBRARY_PATH:-}
exec /workspace/runtime/bin/ollama serve
