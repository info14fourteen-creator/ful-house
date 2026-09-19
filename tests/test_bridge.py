import asyncio
import unittest
from aiohttp import web
from aiohttp.test_utils import TestServer, TestClient
from app.control import Controller
from unittest.mock import AsyncMock

class StreamAccounting(unittest.IsolatedAsyncioTestCase):
    async def test_active_stream_blocks_shutdown_until_finished(self):
        control=Controller();control.key='test';control.phase='ready';control.api=AsyncMock(return_value={'status':'EXITED'})
        stream_open=asyncio.Event();finish=asyncio.Event()
        async def generation():
            self.assertTrue(await control.begin_request());stream_open.set()
            try: await finish.wait()
            finally: await control.end_request()
        task=asyncio.create_task(generation());await stream_open.wait()
        self.assertFalse(await control.stop())
        finish.set();await task
        self.assertTrue(await control.stop())

    async def test_disconnected_stream_releases_request_counter(self):
        control=Controller();control.phase='ready';started=asyncio.Event()
        async def generation():
            await control.begin_request();started.set()
            try: await asyncio.Event().wait()
            finally: await control.end_request()
        task=asyncio.create_task(generation());await started.wait();task.cancel()
        with self.assertRaises(asyncio.CancelledError): await task
        self.assertEqual(control.active,0)

class RealBridgeTests(unittest.IsolatedAsyncioTestCase):
    async def test_real_stream_keeps_gpu_active_until_upstream_finishes(self):
        from aiohttp import ClientSession
        from app.bridge import start_bridge
        control=Controller();control.key='test';control.phase='ready';control.api=AsyncMock(return_value={'status':'EXITED'})
        release=asyncio.Event()
        async def stream(request):
            response=web.StreamResponse(headers={'Content-Type':'application/x-ndjson'})
            await response.prepare(request);await response.write(b'{"done":false}\n')
            await release.wait();await response.write(b'{"done":true}\n');await response.write_eof();return response
        upstream=web.Application();upstream.router.add_post('/api/chat',stream)
        runner=web.AppRunner(upstream);await runner.setup()
        await web.TCPSite(runner,'127.0.0.1',11434).start()
        bridge=await start_bridge(control)
        try:
            async with ClientSession() as session:
                async with session.post('http://127.0.0.1:11435/api/chat',json={'model':'test'}) as response:
                    self.assertIn(b'false',await response.content.readline())
                    self.assertEqual(control.active,1)
                    self.assertFalse(await control.stop())
                    release.set();self.assertIn(b'true',await response.read())
                for _ in range(20):
                    if not control.active:break
                    await asyncio.sleep(.01)
                self.assertEqual(control.active,0)
        finally:
            release.set();await bridge.cleanup();await runner.cleanup()

    async def test_embed_falls_back_to_legacy_embeddings_endpoint(self):
        from aiohttp import ClientSession
        from app.bridge import start_bridge
        control=Controller();control.key='test';control.phase='ready';control.api=AsyncMock(return_value={'status':'EXITED'})
        calls=[]
        async def embed(request):
            calls.append('/api/embed')
            return web.json_response({'error':'missing'}, status=404)
        async def embeddings(request):
            calls.append('/api/embeddings')
            payload=await request.json()
            self.assertEqual(payload['model'], 'nomic-embed-text:latest')
            self.assertEqual(payload['prompt'], 'hello')
            return web.json_response({'embedding':[0.1,0.2]})
        upstream=web.Application();upstream.router.add_post('/api/embed',embed);upstream.router.add_post('/api/embeddings',embeddings)
        runner=web.AppRunner(upstream);await runner.setup()
        await web.TCPSite(runner,'127.0.0.1',11434).start()
        bridge=await start_bridge(control)
        try:
            async with ClientSession() as session:
                async with session.post('http://127.0.0.1:11435/api/embed',json={'input':'hello'}) as response:
                    self.assertEqual(response.status, 200)
                    self.assertEqual(await response.json(), {'model':'nomic-embed-text:latest','embeddings':[[0.1,0.2]]})
            self.assertEqual(calls, ['/api/embed','/api/embeddings'])
        finally:
            await bridge.cleanup();await runner.cleanup()
