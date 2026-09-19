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
from app.bridge import start_bridge

from app.state import State
state=State()
control=Controller()
control.store=state
original_lifespan=upstream.router.lifespan_context

@asynccontextmanager
async def lifespan(app):
    async with original_lifespan(app):
        await state.initialize()
        # Bootstrap directly with a precomputed bcrypt hash; plaintext never needed.
        password_hash=os.getenv('FULHOUSE_ADMIN_PASSWORD_HASH')
        if password_hash and not await Users.has_users():
            await Auths.insert_new_auth(email='steelstan@ful.house',password=password_hash,name='steelstan',role='admin')
        if control.key:
            await control.reconcile()
        bridge=await start_bridge(control)
        task=asyncio.create_task(control.idle_watch())
        try: yield
        finally:
            task.cancel()
            with suppress(asyncio.CancelledError): await task
            await bridge.cleanup()
            await control.close_tunnel()

upstream.router.lifespan_context=lifespan
router=APIRouter(prefix='/fulhouse/api',dependencies=[Depends(get_admin_user)])

@router.get('/status')
async def status():
    return {'phase':control.phase,'active':control.active,'idle_seconds':control.idle_seconds,'failure_reason':control.failure_reason}

@router.post('/start',status_code=202)
async def start():
    await control.request_start()
    return {'phase':control.phase}

@router.post('/stop')
async def stop():
    if not await control.stop(): raise HTTPException(409,'Server busy or controls unavailable')
    return {'phase':control.phase}

# Prepend routes before upstream's catch-all SPA route.
upstream.router.routes[0:0]=router.routes

from app.guard import Guard

app=Guard(upstream,state)
