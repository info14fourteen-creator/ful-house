"""Bind the Heroku port immediately while Open WebUI imports and initializes."""
import asyncio
import importlib
import logging
from starlette.responses import PlainTextResponse

loaded=None
context=None
loading=None
startup_error=False

async def initialize():
    global loaded,context,startup_error
    try:
        module=await asyncio.to_thread(importlib.import_module,'app.main')
        context=module.upstream.router.lifespan_context(module.upstream)
        await context.__aenter__()
        loaded=module.app
    except Exception:
        startup_error=True
        logging.exception('Open WebUI startup failed')

async def app(scope,receive,send):
    global loading
    if scope['type']=='lifespan':
        while True:
            message=await receive()
            if message['type']=='lifespan.startup':
                loading=asyncio.create_task(initialize())
                await send({'type':'lifespan.startup.complete'})
            elif message['type']=='lifespan.shutdown':
                if loaded and context: await context.__aexit__(None,None,None)
                elif loading: loading.cancel()
                await send({'type':'lifespan.shutdown.complete'})
                return
    elif loaded:
        await loaded(scope,receive,send)
    elif scope['type']=='websocket':
        await send({'type':'websocket.close','code':1013})
    else:
        await PlainTextResponse('Interface startup failed.' if startup_error else 'Fullhouse is starting. Refresh the page in a few seconds.',status_code=503,headers={'Retry-After':'5','Cache-Control':'no-store','X-Fullhouse-State':'error' if startup_error else 'starting'})(scope,receive,send)
