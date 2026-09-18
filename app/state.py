"""Small durable control state; no passwords or model messages are stored here."""
from datetime import datetime, timezone, timedelta
import hashlib
import hmac
import os
import psycopg

class State:
    def connection(self):
        return psycopg.AsyncConnection.connect(os.environ['DATABASE_URL'],connect_timeout=10)

    async def initialize(self):
        async with await self.connection() as conn:
            await conn.execute('CREATE TABLE IF NOT EXISTS fulhouse_runtime (id TEXT PRIMARY KEY, pod_id TEXT)')
            await conn.execute('CREATE TABLE IF NOT EXISTS fulhouse_login_attempts (client TEXT PRIMARY KEY, attempts INTEGER NOT NULL, started TIMESTAMPTZ NOT NULL, blocked_until TIMESTAMPTZ)')

    async def get_pod(self):
        async with await self.connection() as conn:
            cur=await conn.execute("SELECT pod_id FROM fulhouse_runtime WHERE id='gpu'")
            row=await cur.fetchone()
            return row[0] if row else ''

    async def set_pod(self,pod):
        async with await self.connection() as conn:
            await conn.execute("INSERT INTO fulhouse_runtime(id,pod_id) VALUES ('gpu',%s) ON CONFLICT(id) DO UPDATE SET pod_id=EXCLUDED.pod_id",(pod,))

    def client_key(self,headers):
        return hmac.new(os.environ['WEBUI_SECRET_KEY'].encode(),headers.get(b'cf-connecting-ip',b'unknown'),hashlib.sha256).hexdigest()

    async def allow_login(self,client):
        now=datetime.now(timezone.utc)
        async with await self.connection() as conn:
            await conn.execute('INSERT INTO fulhouse_login_attempts VALUES (%s,0,%s,NULL) ON CONFLICT DO NOTHING',(client,now))
            cur=await conn.execute('SELECT attempts,started,blocked_until FROM fulhouse_login_attempts WHERE client=%s FOR UPDATE',(client,))
            attempts,started,blocked=await cur.fetchone()
            if blocked and blocked>now:return False
            if now-started>=timedelta(minutes=15):attempts=0;started=now
            attempts+=1
            blocked=now+timedelta(minutes=15) if attempts>=12 else None
            await conn.execute('UPDATE fulhouse_login_attempts SET attempts=%s,started=%s,blocked_until=%s WHERE client=%s',(attempts,started,blocked,client))
            return True

    async def reset_login(self,client):
        async with await self.connection() as conn:
            await conn.execute('DELETE FROM fulhouse_login_attempts WHERE client=%s',(client,))
