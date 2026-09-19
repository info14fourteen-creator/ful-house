#!/usr/bin/env python3
"""Install an official Node 22 release after checking its published SHA-256."""
import hashlib
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import urllib.request

ROOT=Path('/opt/fulhouse-agent-root')
BASE='https://nodejs.org/dist/latest-v22.x/'
manifest=urllib.request.urlopen(BASE+'SHASUMS256.txt',timeout=30).read().decode()
checksum, filename=next(line.split() for line in manifest.splitlines() if re.fullmatch(r'[0-9a-f]{64}  node-v22\.[0-9]+\.[0-9]+-linux-x64\.tar\.xz',line))
with tempfile.TemporaryDirectory(prefix='fulhouse-node-') as directory:
    archive=Path(directory)/filename
    digest=hashlib.sha256()
    with urllib.request.urlopen(BASE+filename,timeout=90) as response, archive.open('wb') as out:
        while chunk:=response.read(1024*1024):
            digest.update(chunk);out.write(chunk)
    if digest.hexdigest()!=checksum:raise RuntimeError('Node release checksum mismatch')
    destination=ROOT/'usr/local';destination.mkdir(parents=True,exist_ok=True)
    subprocess.run(['tar','-xJf',str(archive),'--strip-components=1','-C',str(destination)],check=True)
for name,target in [('node','/usr/local/bin/node'),('npm','/usr/local/lib/node_modules/npm/bin/npm-cli.js'),('npx','/usr/local/lib/node_modules/npm/bin/npx-cli.js')]:
    path=ROOT/'usr/bin'/name
    if not path.exists():path.symlink_to(target)
output=subprocess.run(['ldd',str(ROOT/'usr/local/bin/node')],capture_output=True,text=True,check=True).stdout
for dependency in re.findall(r'(/[^\s()]+)',output):
    source=Path(dependency);target=ROOT/str(source).lstrip('/')
    target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists():shutil.copy2(source,target,follow_symlinks=True)
(ROOT/'etc/fulhouse-node-release').write_text(f'{filename}\nsha256 {checksum}\n')
print('Verified Node archive:',filename,checksum)
