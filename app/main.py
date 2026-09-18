"""Open WebUI extension. Auth stays upstream; administrative controls require admin."""
import asyncio
from contextlib import asynccontextmanager, suppress
import hmac
import json
import os
import httpx
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
from open_webui.main import app as upstream
from open_webui.utils.auth import get_admin_user
from open_webui.models.auths import Auths
from open_webui.models.users import Users
from app.control import Controller, MODEL

control=Controller()
original_lifespan=upstream.router.lifespan_context

@asynccontextmanager
async def lifespan(app):
    async with original_lifespan(app):
        # Bootstrap directly with a precomputed bcrypt hash; plaintext never needed.
        password_hash=os.getenv('FULHOUSE_ADMIN_PASSWORD_HASH')
        if password_hash and not await Users.has_users():
            await Auths.insert_new_auth(email='steelstan@ful.house',password=password_hash,name='steelstan',role='admin')
        if control.key:
            await control.stop()
        task=asyncio.create_task(control.idle_watch())
        try: yield
        finally:
            task.cancel()
            with suppress(asyncio.CancelledError): await task
            await control.close_tunnel()

upstream.router.lifespan_context=lifespan
router=APIRouter(prefix='/fulhouse/api',dependencies=[Depends(get_admin_user)])

@router.get('/status')
async def status():
    return {'phase':control.phase,'active':control.active,'idle_seconds':control.idle_seconds}

@router.post('/start',status_code=202)
async def start():
    await control.request_start()
    return {'phase':control.phase}

@router.post('/stop')
async def stop():
    if not await control.stop(): raise HTTPException(409,'Сервер занят или управление недоступно')
    return {'phase':control.phase}

# Prepend routes before upstream's catch-all SPA route.
upstream.router.routes[0:0]=router.routes

class Guard:
    def __init__(self,app): self.app=app
    async def __call__(self,scope,receive,send):
        if scope['type'] not in ('http','websocket'):
            return await self.app(scope,receive,send)
        headers=dict(scope.get('headers',[]));path=scope.get('path','')
        expected=os.getenv('FULHOUSE_ORIGIN_SECRET','')
        secret=headers.get(b'x-fulhouse-origin',b'').decode()
        if not expected or not hmac.compare_digest(secret,expected):
            if scope['type']=='websocket': return await send({'type':'websocket.close','code':1008})
            return await JSONResponse({'detail':'Forbidden'},403)(scope,receive,send)
        if scope['type']=='http':
            if path.startswith('/api/v1/auths/signup'):
                return await JSONResponse({'detail':'Регистрация закрыта'},403)(scope,receive,send)
            if scope['method'] not in ('GET','HEAD','OPTIONS'):
                origin=headers.get(b'origin',b'').decode()
                if origin and origin!=os.getenv('WEBUI_URL','https://ful.house'):
                    return await JSONResponse({'detail':'Invalid origin'},403)(scope,receive,send)
        if scope['type']=='http' and path=='/api/v1/auths/signin' and scope['method']=='POST':
            chunks=[]
            while True:
                message=await receive()
                chunks.append(message.get('body',b''))
                if sum(map(len,chunks))>16384:
                    return await JSONResponse({'detail':'Request too large'},413)(scope,receive,send)
                if not message.get('more_body'): break
            body=b''.join(chunks)
            try:
                data=json.loads(body)
                if data.get('email','').lower()=='steelstan':
                    data['email']='steelstan@ful.house'
                    body=json.dumps(data).encode()
            except (ValueError,AttributeError): pass
            scope=dict(scope)
            scope['headers']=[(k,v) for k,v in scope['headers'] if k!=b'content-length']+[(b'content-length',str(len(body)).encode())]
            original_receive=receive
            sent=False
            async def replay():
                nonlocal sent
                if not sent:
                    sent=True
                    return {'type':'http.request','body':body,'more_body':False}
                return await original_receive()
            receive=replay
        tracked=False
        if scope['type']=='http' and scope['method']=='POST' and path in ('/api/chat/completions','/ollama/api/chat','/ollama/api/generate'):
            tracked=await control.begin_request()
        try:
            return await self.app(scope,receive,send)
        finally:
            if tracked: await control.end_request()

app=Guard(upstream)
