import asyncio
import unittest
from unittest.mock import AsyncMock,patch
from app import engineer

class GuardTests(unittest.TestCase):
    def test_admin_required(self):
        for user in [None,{}, {'role':'user'}]:
            with self.assertRaises(PermissionError):engineer.admin(user)
        engineer.admin({'role':'admin'})
    def test_paths_cannot_escape_or_overwrite_workflows(self):
        for path in ['../x','/etc/passwd','a/../b','.github/workflows/a.yml','.env','foo/.env.production','a\\b','a//b','key.pem']:
            with self.assertRaises(ValueError):engineer.safe_path(path)
        self.assertEqual(engineer.safe_path('app/main.py'),'app/main.py')

    def test_repository_names_are_owner_slash_name(self):
        for repo in ['repo-only','owner/repo/extra','../repo','owner/../repo','owner repo/name']:
            with self.assertRaises(ValueError):engineer.repo_name(repo)
        self.assertEqual(engineer.repo_name('owner/repo'),'owner/repo')
    def test_branch_restricts_shared_refs(self):
        for branch in ['main','codex/x','agent/../main','agent/x//y','agent/x/','agent/$(id)']:
            with self.assertRaises(ValueError):engineer.branch_name(branch)
        self.assertEqual(engineer.branch_name('agent/add-tests'),'agent/add-tests')

class BrokerTests(unittest.IsolatedAsyncioTestCase):

    async def test_github_repositories_uses_account_inventory(self):
        call=AsyncMock(return_value=[{'full_name':'org/IPDS','private':True,'default_branch':'main','updated_at':'today','description':'IPDS project'}])
        with patch.object(engineer,'github_request',call):
            result=await engineer.github_repositories('ipds')
        self.assertEqual(result['repositories'][0]['full_name'],'org/IPDS')
        call.assert_awaited_once()
    async def test_deploy_pins_resolved_commit(self):
        call=AsyncMock(side_effect=[{'sha':'a'*40},{}])
        with patch.object(engineer,'request',call):
            result=await engineer.deploy('heroku','main')
        self.assertEqual(result['status'],'queued')
        args=call.call_args_list[1]
        self.assertEqual(args.kwargs['json']['inputs']['revision'],'a'*40)
        self.assertEqual(args.kwargs['json']['ref'],'main')
    async def test_production_requires_main(self):
        with self.assertRaises(ValueError):await engineer.deploy('heroku','agent/unreviewed')
    async def test_no_unknown_deploy_target(self):
        with self.assertRaises(ValueError):await engineer.deploy('other','main')
    async def test_commit_rejects_protected_paths_before_request(self):
        call=AsyncMock()
        with patch.object(engineer,'request',call):
            with self.assertRaises(ValueError):await engineer.commit_files('owner/repo','agent/a','bad',{'.github/workflows/a.yml':'bad'})
        call.assert_not_called()
    async def test_upstream_error_does_not_include_response_secret(self):
        import httpx
        response=httpx.Response(403,json={'error':'SECRET_VALUE'})
        client=AsyncMock();client.__aenter__.return_value=client;client.request.return_value=response
        with patch.object(engineer.httpx,'AsyncClient',return_value=client),patch.dict(engineer.os.environ,{'FULHOUSE_GITHUB_TOKEN':'PRIVATE_TOKEN'}):
            with self.assertRaisesRegex(RuntimeError,'github request failed: HTTP 403') as caught:
                await engineer.request('github','GET','contents/x')
        self.assertNotIn('SECRET',str(caught.exception))
