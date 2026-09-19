"""
title: Fullhouse engineering
version: 1.0.0
"""
import json
from app import engineer

class Tools:
    async def project_status(self, __user__: dict = None) -> str:
        """Check the configured GitHub deployment jobs, Heroku, Cloudflare and GPU status."""
        engineer.admin(__user__)
        return json.dumps(await engineer.project_status(),ensure_ascii=False)

    async def repository(self, path: str = '', ref: str = 'main', __user__: dict = None) -> str:
        """Read a ful-house repository file or list project files. Empty path lists files; ref is a branch or commit."""
        engineer.admin(__user__)
        return json.dumps(await engineer.repository(path,ref),ensure_ascii=False)

    async def commit_files(self, branch: str, message: str, files: dict[str,str], __user__: dict = None) -> str:
        """Commit text files to an agent/ branch of ful-house. files maps repository paths to full new contents. Never use main."""
        engineer.admin(__user__)
        return json.dumps(await engineer.commit_files(branch,message,files),ensure_ascii=False)

    async def open_pull_request(self, branch: str, title: str, body: str, __user__: dict = None) -> str:
        """Open a draft pull request from an existing agent/ branch to main. Include changes and test evidence."""
        engineer.admin(__user__)
        return json.dumps(await engineer.open_pull_request(branch,title,body),ensure_ascii=False)

    async def deploy(self, target: str, ref: str, __user__: dict = None) -> str:
        """Deploy a user-requested revision of ful-house. target is cloudflare or heroku; ref must be main. Agent changes go through a pull request first. Then check project_status."""
        engineer.admin(__user__)
        return json.dumps(await engineer.deploy(target,ref),ensure_ascii=False)

    async def workspace(self, command: str, timeout_seconds: int = 60, __user__: dict = None) -> str:
        """Run shell commands, edit files, clone the public repository and run tests as a non-root developer inside an isolated filesystem. Persistent directory: /workspace. Timeout maximum 120 seconds. No cloud credentials are exposed."""
        engineer.admin(__user__)
        return json.dumps(await engineer.workspace(command,timeout_seconds),ensure_ascii=False)

    async def openai_codex(self, prompt: str, context: str = '', max_output_tokens: int = 4000, __user__: dict = None) -> str:
        """Delegate a coding question or plan to the OpenAI Codex model through the Responses API. The API key is server-side and never exposed."""
        engineer.admin(__user__)
        return json.dumps(await engineer.openai_codex(prompt,context,max_output_tokens),ensure_ascii=False)
