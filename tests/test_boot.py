import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch
from app import boot


class BootTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        boot.loaded = None
        boot.context = None
        boot.startup_error = False

    async def test_only_serves_application_after_lifespan_ready(self):
        context = SimpleNamespace(__aenter__=AsyncMock())
        application = AsyncMock()
        module = SimpleNamespace(app=application, upstream=SimpleNamespace(
            router=SimpleNamespace(lifespan_context=Mock(return_value=context))))
        with patch.object(boot.importlib, 'import_module', return_value=module), \
                self.assertLogs(level='WARNING') as logs:
            await boot.initialize()
        context.__aenter__.assert_awaited_once()
        self.assertIs(boot.loaded, application)
        self.assertIn('imports complete seconds=', ' '.join(logs.output))
        self.assertIn('ready lifespan_seconds=', ' '.join(logs.output))

    async def test_failed_lifespan_never_exposes_application(self):
        context = SimpleNamespace(__aenter__=AsyncMock(side_effect=RuntimeError('test')))
        module = SimpleNamespace(app=AsyncMock(), upstream=SimpleNamespace(
            router=SimpleNamespace(lifespan_context=Mock(return_value=context))))
        with patch.object(boot.importlib, 'import_module', return_value=module), \
                self.assertLogs(level='WARNING'):
            await boot.initialize()
        self.assertIsNone(boot.loaded)
        self.assertTrue(boot.startup_error)
