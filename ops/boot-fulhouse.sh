#!/bin/bash
set -euo pipefail
# Persist the pod identity across ephemeral container replacements.
# Populate this root-only directory once over the authenticated Runpod SSH proxy.
cp -p /workspace/ssh-host-keys/ssh_host_* /etc/ssh/
chmod 600 /etc/ssh/ssh_host_*_key
chmod 644 /etc/ssh/ssh_host_*_key.pub
# Load the existing model while the base image initializes SSH. No downloads.
# The controller still verifies readiness through its pinned SSH tunnel.
nohup bash /workspace/start-model.sh >/workspace/ollama.log 2>&1 </dev/null &
(
    started=$SECONDS
    for attempt in {1..60}; do
        if curl --max-time 2 -fsS http://127.0.0.1:11434/api/version >/dev/null; then
            echo "Model startup: service available seconds=$((SECONDS-started))"
            curl --max-time 180 -fsS http://127.0.0.1:11434/api/generate \
                -H 'Content-Type: application/json' \
                -d '{"model":"huihui_ai/qwen3-coder-abliterated:30b","prompt":"","stream":false,"keep_alive":-1}' >/dev/null
            echo "Model startup: preload complete seconds=$((SECONDS-started))"
            exit 0
        fi
        sleep 1
    done
    echo 'Model startup: service readiness timed out' >&2
    exit 1
) >/workspace/model-startup.log 2>&1 </dev/null &
if [ -f /workspace/provision-agent.sh ]; then
    nohup bash /workspace/provision-agent.sh >/workspace/agent-provision.log 2>&1 </dev/null &
fi
exec /start.sh
