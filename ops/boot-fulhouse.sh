#!/bin/bash
set -euo pipefail
# Persist the pod identity across ephemeral container replacements.
# Populate this root-only directory once over the authenticated Runpod SSH proxy.
cp -p /workspace/ssh-host-keys/ssh_host_* /etc/ssh/
chmod 600 /etc/ssh/ssh_host_*_key
chmod 644 /etc/ssh/ssh_host_*_key.pub
exec /start.sh
