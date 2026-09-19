#!/usr/bin/env bash
set -euo pipefail
# MFS ignores POSIX modes. The developer sees only this ext4 chroot, never MFS.
agent_root=/opt/fulhouse-agent-root
if [ ! -f "$agent_root/.ready" ]; then
    mkdir -p "$agent_root"
    if [ -s /workspace/agent-rootfs.tar.gz ]; then
        tar -xzf /workspace/agent-rootfs.tar.gz -C "$agent_root"
    else
        export DEBIAN_FRONTEND=noninteractive
        apt-get update -qq
        apt-get install -y --no-install-recommends busybox-static git python3 ca-certificates
        python3 /workspace/build-agent-root.py
        python3 /workspace/install-agent-node.py
        chown 2001:2001 "$agent_root/workspace"
        chmod 700 "$agent_root/workspace"
        tar --exclude=./workspace/'*' --exclude=./.ready -czf /workspace/agent-rootfs.tar.gz.tmp -C "$agent_root" .
        mv /workspace/agent-rootfs.tar.gz.tmp /workspace/agent-rootfs.tar.gz
    fi
    cp /etc/resolv.conf "$agent_root/etc/resolv.conf"
    python3 /workspace/agent-state.py restore
    touch "$agent_root/.ready"
fi
