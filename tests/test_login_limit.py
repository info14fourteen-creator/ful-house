import os
import unittest
from unittest.mock import AsyncMock, Mock, patch
import httpx
from app.guard import Guard
from starlette.responses import JSONResponse

class LoginLimitTests(unittest.IsolatedAsyncioTestCase):
    async def run_login(self,allowed=True,status=200,error=False):
        limiter=Mock();limiter.is_revoked.return_value=False;limiter.client_key.return_value='client'
        limiter.allow_login=AsyncMock(return_value=allowed,side_effect=RuntimeError() if error else None)
        limiter.reset_login=AsyncMock()
        calls=[]
        async def endpoint(scope,receive,send):
            calls.append(1)
            await JSONResponse({'ok':status==200},status)(scope,receive,send)
        with patch.dict(os.environ,{'FULHOUSE_ORIGIN_SECRET':'test'}):
            async with httpx.AsyncClient(transport=httpx.ASGITransport(app=Guard(endpoint,limiter)),base_url='https://ful.house') as c:
                response=await c.post('/api/v1/auths/signin',headers={'x-fulhouse-origin':'test'},json={'email':'steelstan','password':'test'})
        return response,limiter,calls
    async def test_lock_blocks_upstream(self):
        r,l,calls=await self.run_login(allowed=False)
        self.assertEqual(r.status_code,429);self.assertEqual(calls,[]);l.reset_login.assert_not_awaited()
    async def test_failed_auth_keeps_counter(self):
        r,l,_=await self.run_login(status=400)
        self.assertEqual(r.status_code,400);l.reset_login.assert_not_awaited()
    async def test_success_resets_counter(self):
        r,l,_=await self.run_login()
        self.assertEqual(r.status_code,200);l.reset_login.assert_awaited_once_with('client')
    async def test_storage_error_fails_closed(self):
        r,l,calls=await self.run_login(error=True)
        self.assertEqual(r.status_code,503);self.assertEqual(calls,[])
