import os
import unittest
from unittest.mock import AsyncMock, patch
from app.control import Controller


class CapacityTests(unittest.IsolatedAsyncioTestCase):
    def gpu(self, name='NVIDIA L40S', price=1.09, dc='US-TX-3', memory=48):
        return {'id':name,'secure':True,'memory':memory,'price':{'secure':price},
                'dataCenters':[{'id':dc,'availability':'LOW'}]}

    async def select(self, gpus):
        controller=Controller()
        controller.request=AsyncMock(return_value={'gpus':gpus})
        with patch.dict(os.environ, {'RUNPOD_DATA_CENTER':'US-TX-3','GPU_MAX_HOURLY_USD':'1.09'}, clear=True):
            return await controller.select_gpu()

    async def test_prefers_l40s_when_available(self):
        self.assertEqual(await self.select([self.gpu('NVIDIA A40',.49),self.gpu()]),'NVIDIA L40S')

    async def test_falls_back_within_same_location_and_budget(self):
        self.assertEqual(await self.select([self.gpu(dc='US-TX-4'),self.gpu('NVIDIA A40',.49)]),'NVIDIA A40')

    async def test_rejects_over_budget_low_memory_or_wrong_location(self):
        for gpu in [self.gpu(price=1.10),self.gpu(memory=24),self.gpu(dc='US-TX-4')]:
            with self.assertRaises(RuntimeError):await self.select([gpu])

    async def test_unavailable_or_unpriced_capacity_never_allocates(self):
        gpu=self.gpu();gpu['dataCenters'][0]['availability']='NONE'
        with self.assertRaises(RuntimeError):await self.select([gpu])
        gpu=self.gpu();gpu['price']={}
        with self.assertRaises(RuntimeError):await self.select([gpu])
