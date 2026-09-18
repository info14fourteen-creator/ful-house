import os
import json
import unittest
from unittest.mock import patch
import httpx
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.guard import Guard

async def echo(scope,receive,send):
    request=Request(scope,receive)
    body=await request.body()
    await JSONResponse({'body':body.decode()})(scope,receive,send)

class GuardTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.env=patch.dict(os.environ,{'FULHOUSE_ORIGIN_SECRET':'test-secret','WEBUI_URL':'https://ful.house'})
        self.env.start()
        self.client=httpx.AsyncClient(transport=httpx.ASGITransport(app=Guard(echo)),base_url='https://ful.house')
    async def asyncTearDown(self):
        await self.client.aclose();self.env.stop()
    async def test_direct_origin_blocked(self):
        r=await self.client.get('/');self.assertEqual(r.status_code,403)
    async def test_signup_always_blocked(self):
        r=await self.client.post('/api/v1/auths/signup',headers={'X-Fulhouse-Origin':'test-secret'});self.assertEqual(r.status_code,403)
    async def test_foreign_origin_blocked(self):
        r=await self.client.post('/fulhouse/api/start',headers={'X-Fulhouse-Origin':'test-secret','Origin':'https://evil.example'});self.assertEqual(r.status_code,403)
    async def test_login_alias(self):
        r=await self.client.post('/api/v1/auths/signin',headers={'X-Fulhouse-Origin':'test-secret','Origin':'https://ful.house'},json={'email':'steelstan','password':'example'})
        self.assertEqual(r.status_code,200)
        self.assertEqual(json.loads(r.json()['body'])['email'],'steelstan@ful.house')
    async def test_large_login_body_rejected(self):
        r=await self.client.post('/api/v1/auths/signin',headers={'X-Fulhouse-Origin':'test-secret'},content=b'x'*16385);self.assertEqual(r.status_code,413)
