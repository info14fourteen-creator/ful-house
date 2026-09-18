import unittest
from unittest.mock import AsyncMock
from app.control import Controller

class NetworkTests(unittest.IsolatedAsyncioTestCase):
    def controller(self):
        c=Controller();c.key='test';c.volume='volume';c.store=AsyncMock()
        return c
    def pod(self):
        return {'id':'owned','name':'fulhouse-network-gpu','mounts':{'network':[{'volumeId':'volume'}]}}
    async def test_stop_keeps_network_disk(self):
        c=self.controller();c.phase='ready'
        c.request=AsyncMock(side_effect=[{'pods':[self.pod()]},self.pod(),{}])
        self.assertTrue(await c.stop())
        self.assertEqual([x.args for x in c.request.call_args_list],[('GET','/pods'),('GET','/pods/owned'),('DELETE','/pods/owned')])
        c.store.set_pod.assert_awaited_with('')
    async def test_duplicate_workers_fail_closed(self):
        c=self.controller();c.request=AsyncMock(return_value={'pods':[self.pod(),self.pod()]})
        with self.assertRaises(RuntimeError):await c.discover()
        self.assertEqual(c.request.await_count,1)
    async def test_incomplete_inventory_fails_closed(self):
        c=self.controller()
        for response in [{},{'pods':[],'pagination':{'hasNextPage':True}}]:
            c.request=AsyncMock(return_value=response)
            with self.assertRaises(RuntimeError):await c.discover()
    async def test_unrelated_workers_untouched(self):
        c=self.controller();pod=self.pod();pod['mounts']['network'][0]['volumeId']='other'
        c.request=AsyncMock(return_value={'pods':[pod]})
        self.assertTrue(await c.stop());self.assertEqual(c.request.await_count,1)
