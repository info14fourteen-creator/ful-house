"""
title: Fullhouse engineering
version: 1.0.0
"""
import json
from app import engineer

class Tools:
    async def project_status(self, __user__: dict = None) -> str:
        """Check Fullhouse deployment jobs, Heroku, Cloudflare, GPU status and connected tool state."""
        engineer.admin(__user__)
        return json.dumps(await engineer.project_status(),ensure_ascii=False)


    async def openwebui_files(self, query: str = '', limit: int = 20, __user__: dict = None) -> str:
        """List files uploaded to Open WebUI, including attached PDFs processed into text. Use this before saying an attachment is inaccessible."""
        engineer.admin(__user__)
        return json.dumps(await engineer.openwebui_files(query,limit),ensure_ascii=False)

    async def openwebui_file_content(self, file_id: str, max_chars: int = 50000, __user__: dict = None) -> str:
        """Read processed text content for an Open WebUI uploaded file by id. Increase max_chars up to 200000 for long PDFs."""
        engineer.admin(__user__)
        return json.dumps(await engineer.openwebui_file_content(file_id,max_chars),ensure_ascii=False)

    async def github_repositories(self, query: str = '', limit: int = 100, __user__: dict = None) -> str:
        """List GitHub repositories available to the configured account. Optional query filters by name or description."""
        engineer.admin(__user__)
        return json.dumps(await engineer.github_repositories(query,limit),ensure_ascii=False)

    async def repository(self, repo: str = 'info14fourteen-creator/ful-house', path: str = '', ref: str = 'main', __user__: dict = None) -> str:
        """Read a GitHub repository file or list project files. repo is owner/name. Empty path lists files; ref is a branch or commit."""
        engineer.admin(__user__)
        return json.dumps(await engineer.repository(repo,path,ref),ensure_ascii=False)

    async def commit_files(self, repo: str, branch: str, message: str, files: dict[str,str], __user__: dict = None) -> str:
        """Commit text files to an agent/ branch of a GitHub repo. repo is owner/name. files maps repository paths to full new contents. Never use main."""
        engineer.admin(__user__)
        return json.dumps(await engineer.commit_files(repo,branch,message,files),ensure_ascii=False)

    async def open_pull_request(self, repo: str, branch: str, title: str, body: str, __user__: dict = None) -> str:
        """Open a draft pull request from an existing agent/ branch to main in the selected repo. Include changes and test evidence."""
        engineer.admin(__user__)
        return json.dumps(await engineer.open_pull_request(repo,branch,title,body),ensure_ascii=False)

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
