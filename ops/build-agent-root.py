#!/usr/bin/env python3
"""Copy a small trusted Python/Git runtime; never copy host settings or secrets."""
from pathlib import Path
import re
import shutil
import subprocess
import sys

root = Path('/opt/fulhouse-agent-root')
seen = set()
def binary(path):
    source=Path(path)
    if not source.exists() or str(source) in seen:
        return
    seen.add(str(source))
    target=root / str(source).lstrip('/')
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source,target,follow_symlinks=True)
    target.chmod(target.stat().st_mode & 0o777)
    output=subprocess.run(['ldd',str(source)],capture_output=True,text=True).stdout
    for dependency in re.findall(r'(/[^\s()]+)',output):
        binary(dependency)

for path in ['/bin/bash','/bin/sh','/usr/bin/env','/usr/bin/python3','/usr/bin/git','/usr/bin/ssh','/usr/bin/busybox']:
    binary(path)
version=subprocess.check_output(['/usr/bin/python3','-c','import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")'],text=True).strip()
for path in [f'/usr/lib/python{version}','/usr/lib/git-core','/usr/share/git-core','/etc/ssl/certs']:
    source=Path(path)
    if source.exists():
        shutil.copytree(source,root / path.lstrip('/'),dirs_exist_ok=True,symlinks=False)
for path in list((root/'usr/lib').rglob('*.so'))+list((root/'usr/lib/git-core').glob('*')):
    if path.is_file():
        original='/' + str(path.relative_to(root))
        binary(original)
for name in subprocess.check_output(['/usr/bin/busybox','--list'],text=True).splitlines():
    dest=root/'bin'/name
    if not dest.exists():dest.symlink_to('/usr/bin/busybox')
for path in ['tmp','workspace','etc','dev','proc']:(root/path).mkdir(parents=True,exist_ok=True)
(root/'etc/passwd').write_text('root:x:0:0:root:/root:/bin/bash\nfulhouse-dev:x:2001:2001:Developer:/workspace:/bin/bash\n')
(root/'etc/group').write_text('root:x:0:\nfulhouse-dev:x:2001:\n')
(root/'etc/nsswitch.conf').write_text('passwd: files\ngroup: files\nhosts: files dns\n')
(root/'etc/hosts').write_text('127.0.0.1 localhost\n')
(root/'dev/null').touch();(root/'dev/null').chmod(0o666)
(root/'tmp').chmod(0o1777)

(root/'usr/lib/ssl').mkdir(parents=True,exist_ok=True)
for name, target in [('cert.pem','/etc/ssl/certs/ca-certificates.crt'),('certs','/etc/ssl/certs')]:
    path=root/'usr/lib/ssl'/name
    if not path.exists():path.symlink_to(target)
