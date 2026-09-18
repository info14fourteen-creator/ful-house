import os,unittest
from unittest.mock import patch,AsyncMock
import httpx
from starlette.responses import JSONResponse
from app.guard import Guard
from app.state import State

class SignoutTests(unittest.IsolatedAsyncioTestCase):
    async def test_revoked_bearer_and_cookie_cannot_access_chat_but_can_login(self):
        state=State()
        async def revoke(token):
            import hashlib
            state.revoked.add(hashlib.sha256(token.encode()).hexdigest())
        state.revoke=AsyncMock(side_effect=revoke)
        state.allow_login=AsyncMock(return_value=True);state.reset_login=AsyncMock()
        async def endpoint(scope,receive,send):await JSONResponse({'ok':True})(scope,receive,send)
        with patch.dict(os.environ,{'FULHOUSE_ORIGIN_SECRET':'test','WEBUI_SECRET_KEY':'test'}):
            async with httpx.AsyncClient(transport=httpx.ASGITransport(app=Guard(endpoint,state)),base_url='https://ful.house',headers={'x-fulhouse-origin':'test'}) as c:
                self.assertEqual((await c.get('/api/v1/chats/',headers={'Authorization':'Bearer token-a'})).status_code,200)
                self.assertEqual((await c.post('/api/v1/auths/signout',headers={'Authorization':'Bearer token-a'})).status_code,200)
                for headers in [{'Authorization':'Bearer token-a'},{'Cookie':'token=token-a'}]:
                    self.assertEqual((await c.get('/api/v1/chats/',headers=headers)).status_code,401)
                self.assertEqual((await c.get('/api/v1/chats/',headers={'Authorization':'Bearer different-token'})).status_code,200)
                self.assertEqual((await c.post('/api/v1/auths/signin',headers={'Cookie':'token=token-a'},json={'email':'steelstan','password':'test'})).status_code,200)
