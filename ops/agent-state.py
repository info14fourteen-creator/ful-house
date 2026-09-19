#!/usr/bin/env python3
"""Root-side persistence for an untrusted developer's chroot workspace."""
import os
from pathlib import Path, PurePosixPath
import sys
import tarfile

WORK = Path('/opt/fulhouse-agent-root/workspace')
ARCHIVE = Path('/workspace/agent-state.tar.gz')
MAX_BYTES = 256 * 1024 * 1024
SKIP = {'node_modules', '.venv', '__pycache__', '.cache'}

def restore():
    if not ARCHIVE.exists():
        return
    with tarfile.open(ARCHIVE, 'r:gz') as archive:
        total = 0
        count = 0
        for member in archive:
            total += member.size
            count += 1
            if total > MAX_BYTES or count > 50000:
                raise ValueError('Workspace archive exceeds safety limit')
            name = PurePosixPath(member.name)
            if name.is_absolute() or '..' in name.parts or not name.parts:
                continue
            if not (member.isdir() or member.isfile()):
                continue
            target = WORK.joinpath(*name.parts)
            # Refuse existing symlinks too, including symlink parents.
            if any(WORK.joinpath(*name.parts[:i]).is_symlink() for i in range(1, len(name.parts) + 1)):
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if member.isdir():
                target.mkdir(exist_ok=True)
            else:
                flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW
                with os.fdopen(os.open(target, flags, 0o600), 'wb') as out:
                    source = archive.extractfile(member)
                    while chunk := source.read(1024 * 1024):
                        out.write(chunk)
            os.chown(target, 2001, 2001)
            os.chmod(target, (member.mode & 0o777) | (0o700 if member.isdir() else 0o600))
    # Implicit parent directories created for nested members also belong to dev.
    for root, dirs, files in os.walk(WORK, followlinks=False):
        for path in [Path(root), *(Path(root) / name for name in dirs)]:
            if not path.is_symlink():
                os.chown(path, 2001, 2001)


def save():
    temporary = ARCHIVE.with_suffix('.tmp')
    total = 0
    count = 0
    def regular_only(member):
        nonlocal total, count
        if SKIP.intersection(PurePosixPath(member.name).parts):
            return None
        if not (member.isdir() or member.isfile()):
            return None
        total += member.size
        count += 1
        if total > MAX_BYTES or count > 50000:
            raise ValueError('Workspace exceeds 256 MiB / 50000 files; previous snapshot retained')
        return member
    with tarfile.open(temporary, 'w:gz', dereference=False) as archive:
        for path in WORK.iterdir():
            archive.add(path, arcname=path.name, filter=regular_only)
    temporary.replace(ARCHIVE)

if __name__ == '__main__':
    {'save': save, 'restore': restore}[sys.argv[1]]()
