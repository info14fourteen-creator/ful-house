"""Loopback-only Ollama bridge tracks the full inference stream, including background jobs."""
import json
from aiohttp import ClientSession, ClientTimeout, web
from app.control import MODEL, EMBEDDING_MODEL


async def _proxy_embed(session, data):
    """Return Ollama /api/embed output, falling back to legacy /api/embeddings."""
    payload = json.loads(data.decode() or '{}')
    payload.setdefault('model', EMBEDDING_MODEL)
    async with session.post('http://127.0.0.1:11434/api/embed', json=payload) as result:
        if result.status != 404:
            text = await result.text()
            if result.status >= 400:
                raise web.HTTPBadGateway(text=text)
            return json.loads(text or '{}')
    inputs = payload.get('input', payload.get('prompt', ''))
    if isinstance(inputs, str):
        prompts = [inputs]
    else:
        prompts = [str(item) for item in inputs]
    embeddings = []
    for prompt in prompts:
        async with session.post('http://127.0.0.1:11434/api/embeddings', json={'model': payload.get('model') or EMBEDDING_MODEL, 'prompt': prompt}) as result:
            text = await result.text()
            if result.status >= 400:
                raise web.HTTPBadGateway(text=text)
            embeddings.append(json.loads(text or '{}').get('embedding', []))
    return {'model': payload.get('model') or EMBEDDING_MODEL, 'embeddings': embeddings}

async def start_bridge(control):
    async def proxy(request):
        if request.path == '/api/tags' and control.phase != 'ready':
            return web.json_response({'models':[{'name':MODEL,'model':MODEL}]})
        if request.path == '/api/version' and control.phase != 'ready':
            return web.json_response({'version':'unavailable'},status=503)
        tracked=request.path in ('/api/chat','/api/generate','/api/embed','/api/embeddings','/v1/chat/completions','/v1/completions')
        if tracked:
            if not await control.begin_request():
                return web.json_response({'error':'Server stopped. Click “Start”.'},status=503)
        elif control.phase != 'ready':
            return web.json_response({'error':'Server stopped'},status=503)
        try:
            data=await request.read()
            async with ClientSession(timeout=ClientTimeout(total=None,sock_connect=10,sock_read=300)) as session:
                if request.path == '/api/embed':
                    return web.json_response(await _proxy_embed(session, data))
                async with session.request(request.method,'http://127.0.0.1:11434'+request.path_qs,data=data,headers={'Content-Type':request.headers.get('Content-Type','application/json')}) as result:
                    response=web.StreamResponse(status=result.status,headers={'Content-Type':result.headers.get('Content-Type','application/json')})
                    await response.prepare(request)
                    async for chunk in result.content.iter_any(): await response.write(chunk)
                    await response.write_eof()
                    return response
        finally:
            if tracked: await control.end_request()
    app=web.Application(client_max_size=32*1024*1024)
    app.router.add_route('*','/{path:.*}',proxy)
    runner=web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner,'127.0.0.1',11435).start()
    return runner
