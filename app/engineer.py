"""Scoped engineering tools. Provider credentials never enter model messages."""
import asyncio
import base64
import json
import os
import re
import shlex
from urllib.parse import quote
import httpx

REPO='info14fourteen-creator/ful-house'
ACCOUNT='c49619f872e97a2fc43b245069d4a00f'
APP='fulhouse-ai'
WORKSPACE_LOCK=asyncio.Lock()
BRANCH=re.compile(r'^agent/[a-zA-Z0-9][a-zA-Z0-9_/-]{0,90}$')


def admin(user):
    if not user or user.get('role')!='admin':
        raise PermissionError('Administrator access required')


def safe_path(path):
    if not path or path.startswith('/') or '\\' in path or any(p in ('','.', '..') for p in path.split('/')):
        raise ValueError('Invalid repository path')
    if any(p.startswith('.env') or p in ('.git','.github') or p.endswith(('.pem','.key')) for p in path.split('/')):
        raise ValueError('Secrets and workflow paths are not writable by this tool')
    return path


def branch_name(branch):
    if not BRANCH.fullmatch(branch) or '..' in branch or '//' in branch or branch.endswith('/'):
        raise ValueError('Use an agent/ branch; shared branches cannot be overwritten')
    return branch


async def request(service,method,path,**kwargs):
    if service=='github':
        base=f'https://api.github.com/repos/{REPO}/'; key=os.getenv('FULHOUSE_GITHUB_TOKEN','');headers={'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
    elif service=='heroku':
        base=f'https://api.heroku.com/apps/{APP}/';key=os.getenv('FULHOUSE_HEROKU_TOKEN','');headers={'Accept':'application/vnd.heroku+json; version=3'}
    elif service=='cloudflare':
        base=f'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/pages/projects/ful-house/';key=os.getenv('FULHOUSE_CLOUDFLARE_TOKEN','');headers={}
    else: raise ValueError('Unknown service')
    if not key:raise RuntimeError(f'{service} credentials are not configured')
    headers['Authorization']='Bearer '+key
    async with httpx.AsyncClient(timeout=30,follow_redirects=False) as client:
        response=await client.request(method,base+path,headers=headers,**kwargs)
    if response.status_code>=400:
        # Upstream bodies can contain private URLs or credentials: return only status.
        raise RuntimeError(f'{service} request failed: HTTP {response.status_code}')
    return response.json() if response.content else {}


async def repository(path='',ref='main'):
    if len(ref)>150:raise ValueError('Revision too long')
    if path:
        safe_path(path)
        data=await request('github','GET','contents/'+quote(path,safe='/'),params={'ref':ref})
        if isinstance(data,list):return [{'path':x['path'],'type':x['type']} for x in data][:300]
        if data.get('size',0)>50000:raise ValueError('File too large; inspect in the workspace')
        return {'path':path,'sha':data['sha'],'content':base64.b64decode(data.get('content','')).decode('utf-8',errors='replace')}
    data=await request('github','GET','git/trees/'+quote(ref,safe=''),params={'recursive':'1'})
    return {'ref':ref,'truncated':data.get('truncated',False),'files':[x['path'] for x in data.get('tree',[]) if x['type']=='blob' and not x['path'].startswith('archive/')][:500]}


async def commit_files(branch,message,files):
    branch_name(branch)
    if not message or not files or len(files)>25:raise ValueError('Provide a commit message and 1–25 files')
    if sum(len(v.encode()) for v in files.values())>200000:raise ValueError('Commit exceeds tool size limit')
    for path in files:safe_path(path)
    try:
        tip=await request('github','GET','git/ref/heads/'+quote(branch,safe='/'))
    except RuntimeError as exc:
        if 'HTTP 404' not in str(exc):raise
        tip=await request('github','GET','git/ref/heads/main')
        await request('github','POST','git/refs',json={'ref':'refs/heads/'+branch,'sha':tip['object']['sha']})
    parent=tip['object']['sha'];commit=await request('github','GET','git/commits/'+parent)
    tree=await request('github','POST','git/trees',json={'base_tree':commit['tree']['sha'],'tree':[{'path':p,'mode':'100644','type':'blob','content':v} for p,v in files.items()]})
    new=await request('github','POST','git/commits',json={'message':message,'tree':tree['sha'],'parents':[parent]})
    await request('github','PATCH','git/refs/heads/'+quote(branch,safe='/'),json={'sha':new['sha'],'force':False})
    return {'branch':branch,'sha':new['sha'],'url':f'https://github.com/{REPO}/commit/{new["sha"]}'}


async def open_pull_request(branch,title,body):
    branch_name(branch)
    result=await request('github','POST','pulls',json={'head':branch,'base':'main','title':title,'body':body,'draft':True})
    return {'url':result['html_url'],'number':result['number']}


async def project_status():
    from app.main import control
    out={
        'project':REPO,
        'gpu':{'phase':control.phase,'active_jobs':control.active},
        'openai':{
            'api_configured':bool(os.getenv('OPENAI_API_KEY') or os.getenv('CODEX_API_KEY')),
            'model':os.getenv('FULHOUSE_OPENAI_MODEL','gpt-5.2-codex'),
        },
    }
    for service,path in [('github','actions/workflows/fulhouse-deploy.yml/runs?per_page=5'),('heroku','dynos'),('cloudflare','deployments')]:
        try:
            data=await request(service,'GET',path)
            if service=='github':out[service]=[{'id':x['id'],'status':x['status'],'conclusion':x['conclusion'],'url':x['html_url']} for x in data.get('workflow_runs',[])[:5]]
            elif service=='heroku':out[service]=[{'name':x['name'],'state':x['state'],'size':x['size']} for x in data]
            else:out[service]=[{'id':x['id'],'url':x['url'],'stage':x.get('latest_stage',{})} for x in data.get('result',[])[:3]]
        except RuntimeError as exc:out[service]={'error':str(exc)}
    return out


async def deploy(target,ref):
    if target not in ('cloudflare','heroku'):raise ValueError('Choose cloudflare or heroku')
    if target=='cloudflare' and not os.getenv('FULHOUSE_CLOUDFLARE_TOKEN'):raise RuntimeError('Cloudflare deployment not configured')
    if ref!='main':
        raise ValueError('Production deploys use main. Open a pull request for agent/ changes first.')
    commit=await request('github','GET','commits/main')
    sha=commit['sha']
    await request('github','POST','actions/workflows/fulhouse-deploy.yml/dispatches',json={'ref':'main','inputs':{'target':target,'revision':sha}})
    return {'status':'queued','target':target,'revision':sha,'url':f'https://github.com/{REPO}/actions/workflows/fulhouse-deploy.yml','next':'Use project_status to check completion; queued is not deployed.'}


async def workspace(command,timeout_seconds=60):
    async with WORKSPACE_LOCK:
        return await _workspace(command,timeout_seconds)


async def _workspace(command,timeout_seconds=60):
    from app.main import control
    if not command or len(command)>20000:raise ValueError('Provide a command up to 20000 characters')
    timeout_seconds=max(1,min(int(timeout_seconds),120))
    if not await control.begin_request():raise RuntimeError('GPU workspace is not ready; start the server first')
    try:
        pod=await control.api('GET');direct=pod.get('ssh',{}).get('direct')
        if not direct or not control.owns(pod):raise RuntimeError('Owned workspace is unavailable')
        # Quoting is required even though the enclosed command is intentionally a shell program.
        inner='cd /workspace && '+command
        remote=f'test -f /opt/fulhouse-agent-root/.ready || {{ echo "Workspace is still preparing; retry shortly."; exit 75; }}; timeout --signal=TERM --kill-after=5 {timeout_seconds}s prlimit --nproc=128 --nofile=256 --as=4294967296 --cpu=120 chroot --userspec=2001:2001 /opt/fulhouse-agent-root /usr/bin/env -i HOME=/workspace PATH=/usr/local/bin:/usr/bin:/bin LANG=C.UTF-8 /bin/bash --noprofile --norc -c '+shlex.quote(inner)
        args=['ssh','-i','/tmp/fulhouse-ssh/key','-p',str(int(direct['port'])),'-o','StrictHostKeyChecking=yes','-o','HostKeyAlias=fulhouse-runpod','-o','UserKnownHostsFile=/tmp/fulhouse-ssh/known_hosts','-o','BatchMode=yes','-o','ConnectTimeout=10','root@'+direct['host'],remote]
        proc=await asyncio.create_subprocess_exec(*args,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.STDOUT)
        # Drain output continuously, retaining a bounded prefix in memory.
        output=bytearray()
        async def drain():
            while chunk:=await proc.stdout.read(4096):
                if len(output)<24000:output.extend(chunk[:24000-len(output)])
            await proc.wait()
        try:
            try:await asyncio.wait_for(drain(),timeout_seconds+20)
            except asyncio.TimeoutError:
                proc.kill();await proc.wait();raise RuntimeError('Workspace command timed out')
        finally:
            # One workspace command at a time; reap detached descendants too.
            cleanup=await asyncio.create_subprocess_exec(*args[:-1], '(pkill -KILL -u 2001 || test $? = 1) && /usr/bin/python3 /workspace/agent-state.py save', stdout=asyncio.subprocess.DEVNULL,stderr=asyncio.subprocess.DEVNULL)
            try:await asyncio.wait_for(cleanup.wait(),60)
            except asyncio.TimeoutError:
                cleanup.kill();await cleanup.wait();raise RuntimeError('Workspace process cleanup failed')
            if cleanup.returncode:raise RuntimeError('Workspace process cleanup failed')
        return {'exit_code':proc.returncode,'output':output.decode(errors='replace'),'output_limit_bytes':24000}
    finally:await control.end_request()
