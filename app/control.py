"""Single-pod lifecycle, pinned SSH tunnel, and idle shutdown."""
import asyncio
import json
import logging
import os
from pathlib import Path
import time
import httpx

MODEL = 'huihui_ai/qwen3-coder-abliterated:30b'
EMBEDDING_MODEL = 'nomic-embed-text:latest'

class Controller:
    def __init__(self):
        self.pod = os.getenv('RUNPOD_POD_ID', '')
        self.volume = os.getenv('RUNPOD_NETWORK_VOLUME_ID', '')
        self.store = None
        self.key = os.getenv('RUNPOD_API_KEY', '')
        self.phase = 'stopped' if self.key else 'unconfigured'
        self.active = 0
        self.active_started = []
        self.last_activity = time.monotonic()
        self.idle_seconds = int(os.getenv('GPU_IDLE_SECONDS', '600'))
        self.request_max_seconds = int(os.getenv('GPU_REQUEST_MAX_SECONDS', '900'))
        self.lock = asyncio.Lock()
        self.job = None
        self.failure_reason = ''
        self.startup_started = None
        self.tunnel = None

    async def request(self, method, path, **kwargs):
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.request(method, f'https://api.runpod.io/v2{path}', headers={'Authorization': f'Bearer {self.key}'}, **kwargs)
            r.raise_for_status()
            return r.json() if r.content else {}

    async def api(self,method,suffix='',**kwargs):
        return await self.request(method,f'/pods/{self.pod}{suffix}',**kwargs)

    def owns(self,pod):
        return pod.get('name')=='fulhouse-network-gpu' and any(v.get('volumeId')==self.volume for v in pod.get('mounts',{}).get('network',[]))

    async def discover(self):
        result=await self.request('GET','/pods')
        if not isinstance(result,dict) or not isinstance(result.get('pods'),list) or result.get('pagination',{}).get('hasNextPage'):
            raise RuntimeError('Incomplete pod inventory; refusing allocation')
        pods=result['pods']
        owned=[p for p in pods if self.owns(p)]
        if len(owned)>1:raise RuntimeError('Multiple Fullhouse workers; refusing duplicate allocation')
        self.pod=owned[0]['id'] if owned else ''
        await self.store.set_pod(self.pod)

    async def reconcile(self):
        """Reconnect to an existing rental after a web restart without releasing its GPU."""
        try:
            if self.volume:
                await self.discover()
                if not self.pod:
                    self.phase='stopped'
                    return
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
            self.failure_reason = ''
            self.startup_started = time.monotonic()
            self.job = asyncio.create_task(self.start())

    async def select_gpu(self):
        """Choose available local capacity before renting, within the existing cap."""
        preferred=os.getenv('RUNPOD_GPU_IDS',
            'NVIDIA L40S,NVIDIA RTX 6000 Ada Generation,NVIDIA L40,NVIDIA RTX A6000,NVIDIA A40').split(',')
        catalog=await self.request('GET','/catalog/gpus',params={
            'include':'AVAILABILITY','product':'POD','cloud':'SECURE','minCudaVersion':'12.8'})
        by_id={gpu['id']:gpu for gpu in catalog.get('gpus',[])}
        for gpu_id in map(str.strip,preferred):
            gpu=by_id.get(gpu_id,{})
            price=gpu.get('price',{}).get('secure')
            local=any(dc.get('id')==os.environ['RUNPOD_DATA_CENTER'] and
                      dc.get('availability') in ('LOW','MEDIUM','HIGH')
                      for dc in gpu.get('dataCenters',[]))
            if (gpu.get('secure') and gpu.get('memory',0)>=48 and local and
                    isinstance(price,(int,float)) and 0<price<=float(os.getenv('GPU_MAX_HOURLY_USD','1.09'))):
                logging.warning('GPU startup: selected gpu=%s hourly_usd=%.2f',gpu_id,price)
                return gpu_id
        raise RuntimeError('No compatible GPU capacity at the model volume location within the hourly limit')

    async def start(self):
        started=time.monotonic()
        def milestone(name):
            logging.warning('GPU startup: %s elapsed_seconds=%.2f',name,time.monotonic()-started)
        milestone('requested')
        try:
            if self.volume:
                await self.discover()
                if not self.pod:
                    gpu_id=await self.select_gpu()
                    pod=await self.request('POST','/pods',json={
                        'name':'fulhouse-network-gpu','cloud':'SECURE',
                        'dataCenterIds':[os.environ['RUNPOD_DATA_CENTER']],
                        'gpu':{'id':gpu_id,'count':1,'minCudaVersion':'12.8'},
                        'image':'runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404',
                        'args':'/workspace/boot-fulhouse.sh','disk':20,'ports':['22/tcp'],
                        'env':{'PUBLIC_KEY':os.environ['RUNPOD_SSH_PUBLIC_KEY']},
                        'mounts':{'network':[{'path':'/workspace','volumeId':self.volume}]}})
                    self.pod=pod['id']
                    await self.store.set_pod(self.pod)
                    if float(pod['cost'])>float(os.getenv('GPU_MAX_HOURLY_USD','1.09')):
                        raise RuntimeError('GPU price exceeds configured limit')
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
            milestone('pod_running')
            private = Path('/tmp/fulhouse-ssh'); private.mkdir(mode=0o700, exist_ok=True)
            key = private/'key'; key.write_text(os.environ['RUNPOD_SSH_KEY'].replace('\\n','\n').strip()+'\n'); key.chmod(0o600)
            known = private/'known_hosts'; known.write_text('fulhouse-runpod '+os.environ['RUNPOD_SSH_HOST_KEY'].strip()+'\n'); known.chmod(0o600)
            args=['ssh','-i',str(key),'-p',str(int(direct['port'])),'-o','StrictHostKeyChecking=yes','-o','HostKeyAlias=fulhouse-runpod','-o',f'UserKnownHostsFile={known}','-o','ConnectTimeout=10','-o','ServerAliveInterval=15','-o','BatchMode=yes',f"root@{direct['host']}"]
            self.phase = 'loading'
            for attempt in range(15):
                pod=await self.api('GET')
                endpoint=pod.get('ssh',{}).get('direct')
                if endpoint:
                    args[4]=str(int(endpoint['port']))
                    args[-1]=f"root@{endpoint['host']}"
                proc=await asyncio.create_subprocess_exec(*args,'curl --max-time 5 -fsS http://127.0.0.1:11434/api/version >/dev/null || (nohup bash /workspace/start-model.sh >/workspace/ollama.log 2>&1 </dev/null &)',stdout=asyncio.subprocess.DEVNULL,stderr=asyncio.subprocess.PIPE)
                _,ssh_error=await proc.communicate()
                if proc.returncode == 0: break
                logging.warning('SSH connection failed: %s',ssh_error.decode(errors='replace')[-600:])
                await asyncio.sleep(3)
            else: raise RuntimeError('SSH not ready')
            milestone('ssh_ready')
            self.tunnel=await asyncio.create_subprocess_exec(*args[:-1],'-o','ExitOnForwardFailure=yes','-N','-L','127.0.0.1:11434:127.0.0.1:11434',args[-1],stdout=asyncio.subprocess.DEVNULL,stderr=asyncio.subprocess.DEVNULL)
            for _ in range(30):
                try:
                    async with httpx.AsyncClient(timeout=5) as client:
                        r=await client.get('http://127.0.0.1:11434/api/version');r.raise_for_status()
                    break
                except (httpx.HTTPError,OSError): await asyncio.sleep(2)
            else: raise TimeoutError('Ollama not available')
            milestone('ollama_available')
            async with httpx.AsyncClient(timeout=600) as client:
                r=await client.post('http://127.0.0.1:11434/api/pull',json={'model':EMBEDDING_MODEL,'stream':False});r.raise_for_status()
            milestone('embedding_model_ready')
            async with httpx.AsyncClient(timeout=180) as client:
                r=await client.post('http://127.0.0.1:11434/api/generate',json={'model':MODEL,'prompt':'','stream':False,'keep_alive':-1});r.raise_for_status()
            milestone('model_ready')
            self.phase='ready';self.last_activity=time.monotonic()
        except Exception as exc:
            if 'No compatible GPU capacity' in str(exc) or (isinstance(exc,httpx.HTTPStatusError) and exc.response.status_code==400 and 'no longer any instances' in exc.response.text):
                self.failure_reason='capacity'
            else:self.failure_reason='startup'
            logging.exception("GPU startup failed")
            # Failed provisioning must not leave a newly started GPU billing silently.
            try:
                if self.pod:
                    if self.volume:
                        pod=await self.api('GET')
                        if self.owns(pod):
                            await self.api('DELETE')
                            self.pod=''
                            await self.store.set_pod('')
                    else: await self.api('POST','/action',json={'action':'stop'})
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
                if self.volume:
                    await self.discover()
                    if self.pod:
                        pod=await self.api('GET')
                        if not self.owns(pod):raise RuntimeError('Pod ownership mismatch')
                        await self.api('DELETE')
                        self.pod=''
                        await self.store.set_pod('')
                    await self.close_tunnel()
                    self.phase='stopped'
                    return True
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
            self.reap_stale_requests()
            if self.key and not self.active and (self.phase=='error' or (self.phase=='ready' and time.monotonic()-self.last_activity >= self.idle_seconds)):
                await self.stop()

    def reap_stale_requests(self):
        now=time.monotonic()
        fresh=[started for started in self.active_started if now-started <= self.request_max_seconds]
        if len(fresh) != len(self.active_started):
            logging.warning('GPU request accounting: reaped stale active requests stale=%s active_before=%s',len(self.active_started)-len(fresh),self.active)
        self.active_started=fresh
        self.active=len(fresh)

    async def begin_request(self):
        async with self.lock:
            self.reap_stale_requests()
            if self.phase!='ready': return False
            self.active_started.append(time.monotonic())
            self.active=len(self.active_started)
            self.last_activity=time.monotonic()
            return True

    async def end_request(self):
        async with self.lock:
            if self.active_started:self.active_started.pop(0)
            self.active=len(self.active_started)
            self.last_activity=time.monotonic()
