from http.cookies import SimpleCookie
import hmac
import json
import os
from starlette.responses import JSONResponse

class Guard:
    def __init__(self,app,limiter=None): self.app=app;self.limiter=limiter
    async def __call__(self,scope,receive,send):
        if scope['type'] not in ('http','websocket'):
            return await self.app(scope,receive,send)
        headers=dict(scope.get('headers',[]));path=scope.get('path','')
        expected=os.getenv('FULHOUSE_ORIGIN_SECRET','')
        secret=headers.get(b'x-fulhouse-origin',b'').decode()
        if not expected or not hmac.compare_digest(secret,expected):
            if scope['type']=='websocket': return await send({'type':'websocket.close','code':1008})
            return await JSONResponse({'detail':'Forbidden'},403)(scope,receive,send)
        if self.limiter:
            token=''
            authorization=headers.get(b'authorization',b'').decode()
            if authorization.lower().startswith('bearer '):token=authorization[7:].strip()
            else:
                cookies=SimpleCookie()
                try:cookies.load(headers.get(b'cookie',b'').decode())
                except Exception:pass
                if 'token' in cookies:token=cookies['token'].value
            signout=scope['type']=='http' and scope.get('method')=='POST' and path=='/api/v1/auths/signout'
            signin=path=='/api/v1/auths/signin'
            if token and not signin and not signout and self.limiter.is_revoked(token):
                if scope['type']=='websocket':return await send({'type':'websocket.close','code':1008})
                return await JSONResponse({'detail':'Session expired'},401)(scope,receive,send)
        if scope['type']=='http':
            if path.startswith('/api/v1/auths/signup'):
                return await JSONResponse({'detail':'Registration is closed'},403)(scope,receive,send)
            if scope['method'] not in ('GET','HEAD','OPTIONS'):
                origin=headers.get(b'origin',b'').decode()
                if origin and origin!=os.getenv('WEBUI_URL','https://ful.house'):
                    return await JSONResponse({'detail':'Invalid origin'},403)(scope,receive,send)
        if self.limiter and token and signout:
            try:await self.limiter.revoke(token)
            except Exception:return await JSONResponse({'detail':'Unavailable'},503)(scope,receive,send)
        if scope['type']=='http' and path=='/api/v1/auths/signin' and scope['method']=='POST':
            if self.limiter:
                client=self.limiter.client_key(headers)
                try:
                    allowed=await self.limiter.allow_login(client)
                except Exception:
                    return await JSONResponse({'detail':'Unavailable'},503)(scope,receive,send)
                if not allowed:
                    return await JSONResponse({'detail':'Unavailable'},429,headers={'Retry-After':'900'})(scope,receive,send)
                original_send=send
                async def limited_send(message):
                    if message['type']=='http.response.start' and message['status']==200:
                        await self.limiter.reset_login(client)
                    await original_send(message)
                send=limited_send
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
        return await self.app(scope,receive,send)

