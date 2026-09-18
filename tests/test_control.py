import asyncio
import os
import unittest
from unittest.mock import AsyncMock, patch
from app.control import Controller

class ControlTests(unittest.IsolatedAsyncioTestCase):
    async def test_missing_credentials_never_starts_gpu(self):
        with patch.dict(os.environ,{},clear=True):
            c=Controller();c.api=AsyncMock()
            await c.request_start()
            self.assertEqual(c.phase,'unconfigured');c.api.assert_not_called()

    async def test_cannot_stop_during_generation(self):
        c=Controller();c.key='test';c.phase='ready';c.api=AsyncMock()
        self.assertTrue(await c.begin_request())
        self.assertFalse(await c.stop());c.api.assert_not_called()
        await c.end_request();self.assertEqual(c.active,0)

    async def test_cannot_start_request_during_stop(self):
        c=Controller();c.phase='stopping'
        self.assertFalse(await c.begin_request());self.assertEqual(c.active,0)

    async def test_stop_uses_exact_pod_and_checks_status(self):
        c=Controller();c.key='test';c.phase='ready'
        c.api=AsyncMock(side_effect=[{'status':'RUNNING'},{}])
        self.assertTrue(await c.stop())
        self.assertEqual(c.phase,'stopped')
        self.assertEqual(c.api.call_args_list[1].args,('POST','/action'))
        self.assertEqual(c.api.call_args_list[1].kwargs,{'json':{'action':'stop'}})

    async def test_stopped_pod_does_not_get_duplicate_stop(self):
        c=Controller();c.key='test';c.api=AsyncMock(return_value={'status':'EXITED'})
        self.assertTrue(await c.stop());self.assertEqual(c.api.call_count,1)

    async def test_api_failure_is_not_reported_as_stopped(self):
        c=Controller();c.key='test';c.api=AsyncMock(side_effect=RuntimeError())
        self.assertFalse(await c.stop());self.assertEqual(c.phase,'error')

if __name__=='__main__': unittest.main()
