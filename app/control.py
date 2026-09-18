"""Single-pod lifecycle, pinned SSH tunnel, and idle shutdown."""
import asyncio
import json
import logging
import os
from pathlib import Path
import time
import httpx

MODEL = 'huihui_ai/qwen3-coder-abliterated:30b'

class Controller:
    def __init__(self):
        self.pod = os.getenv('RUNPOD_POD_ID', '1bwx2p5a5bhe6g')
        self.key = os.getenv('RUNPOD_API_KEY', '')
        self.phase = 'stopped' if self.key else 'unconfigured'
        self.active = 0
        self.last_activity = time.monotonic()
        self.idle_seconds = int(os.getenv('GPU_IDLE_SECONDS', '600'))
        self.lock = asyncio.Lock()
        self.job = None
        self.tunnel = None

    async def api(self, method, suffix='', **kwargs):
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.request(method, f'https://api.runpod.io/v2/pods/{self.pod}{suffix}', headers={'Authorization': f'Bearer {self.key}'}, **kwargs)
            r.raise_for_status()
            return r.json() if r.content else {}

    async def reconcile(self):
        """Reconnect to an existing rental after a web restart without releasing its GPU."""
        try:
            pod = await self.api('GET')
            if pod['status'] in ('RUNNING', 'STARTING', 'PROVISIONING'):
                await self.request_start()
            else:
                self.phase = 'stopped'
        except Exception:
            self.phase = 'error'
            logging.exception('GPU state reconciliation failed')

    async def request_start(self):
        async with self.lock:
            if not self.key or not os.getenv('RUNPOD_SSH_KEY') or not os.getenv('RUNPOD_SSH_HOST_KEY'):
                self.phase = 'unconfigured'
                return
            if self.phase in ('starting', 'loading', 'ready', 'stopping'):
                return
            self.phase = 'starting'
            self.job = asyncio.create_task(self.start())

    async def start(self):
        try:
            pod = await self.api('GET')
            if pod['status'] in ('EXITED', 'STOPPED'):
                await self.api('POST', '/action', json={'action': 'start'})
            for _ in range(90):
                pod = await self.api('GET')
                direct = pod.get('ssh', {}).get('direct')
                if pod['status'] == 'RUNNING' and direct:
                    break
                await asyncio.sleep(3)
            else:
                raise TimeoutError('Pod did not become ready')
            private = Path('/tmp/fulhouse-ssh'); private.mkdir(mode=0o700, exist_ok=True)
            key = private/'key'; key.write_text(os.environ['RUNPOD_SSH_KEY'].replace('\\n','\n').strip()+'\n'); key.chmod(0o600)
            known = private/'known_hosts'; known.write_text('fulhouse-runpod '+os.environ['RUNPOD_SSH_HOST_KEY'].strip()+'\n'); known.chmod(0o600)
            args=['ssh','-i',str(key),'-p',str(int(direct['port'])),'-o','StrictHostKeyChecking=yes','-o','HostKeyAlias=fulhouse-runpod','-o',f'UserKnownHostsFile={known}','-o','ConnectTimeout=10','-o','ServerAliveInterval=15','-o','BatchMode=yes',f"root@{direct['host']}"]
            self.phase = 'loading'
            for attempt in range(15):
                proc=await asyncio.create_subprocess_exec(*args,'curl -fsS http://127.0.0.1:11434/api/version >/dev/null || (nohup bash /workspace/start-model.sh >/workspace/ollama.log 2>&1 </dev/null &)',stdout=asyncio.subprocess.DEVNULL,stderr=asyncio.subprocess.DEVNULL)
                if await proc.wait() == 0: break
                await asyncio.sleep(3)
            else: raise RuntimeError('SSH not ready')
            self.tunnel=await asyncio.create_subprocess_exec(*args[:-1],'-o','ExitOnForwardFailure=yes','-N','-L','127.0.0.1:11434:127.0.0.1:11434',args[-1],stdout=asyncio.subprocess.DEVNULL,stderr=asyncio.subprocess.DEVNULL)
            for _ in range(30):
                try:
                    async with httpx.AsyncClient(timeout=5) as client:
                        r=await client.get('http://127.0.0.1:11434/api/version');r.raise_for_status()
                    break
                except (httpx.HTTPError,OSError): await asyncio.sleep(2)
            else: raise TimeoutError('Ollama not available')
            async with httpx.AsyncClient(timeout=180) as client:
                r=await client.post('http://127.0.0.1:11434/api/generate',json={'model':MODEL,'prompt':'','stream':False,'keep_alive':-1});r.raise_for_status()
            self.phase='ready';self.last_activity=time.monotonic()
        except Exception:
            logging.exception("GPU startup failed")
            # Failed provisioning must not leave a newly started GPU billing silently.
            try: await self.api('POST','/action',json={'action':'stop'})
            except Exception: pass
            self.phase='error'
            await self.close_tunnel()

    async def close_tunnel(self):
        if self.tunnel and self.tunnel.returncode is None:
            self.tunnel.terminate()
            await self.tunnel.wait()
        self.tunnel=None

    async def stop(self):
        async with self.lock:
            if self.active or self.phase in ('starting','loading'):
                return False
            if not self.key: return False
            self.phase='stopping'
            try:
                pod=await self.api('GET')
                if pod['status'] not in ('EXITED','STOPPED'):
                    await self.api('POST','/action',json={'action':'stop'})
                await self.close_tunnel()
                self.phase='stopped'
                return True
            except Exception:
                self.phase='error'
                return False

    async def idle_watch(self):
        while True:
            await asyncio.sleep(20)
            if self.key and not self.active and (self.phase=='error' or (self.phase=='ready' and time.monotonic()-self.last_activity >= self.idle_seconds)):
                await self.stop()

    async def begin_request(self):
        async with self.lock:
            if self.phase!='ready': return False
            self.active+=1
            self.last_activity=time.monotonic()
            return True

    async def end_request(self):
        async with self.lock:
            self.active=max(0,self.active-1)
            self.last_activity=time.monotonic()
