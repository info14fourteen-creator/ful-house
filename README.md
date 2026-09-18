# Fullhouse AI

Private Open WebUI at https://ful.house with a Homebrew green monochrome theme, Pravetz 8A details and a Matrix animation while the GPU starts. Admin login: `steelstan`. Public signup is disabled.

## Infrastructure

- Cloudflare Pages project `ful-house` proxies to Heroku `fulhouse-ai`. Theme assets and the cold-start page are served at the edge.
- Heroku Standard-2X (1 GB, $50/month) and Postgres essential-0 ($5/month). Chats and accounts persist in Postgres.
- Runpod pod `1bwx2p5a5bhe6g`, NVIDIA L40S, $1.09/hour while running. Its 40 GB persistent disk is billed separately even when stopped.
- Ollama model `huihui_ai/qwen3-coder-abliterated:30b`, stored under `/workspace/ollama`, with 32K context. Ollama only listens on loopback and is reached through a pinned SSH tunnel.

The administrator starts and stops the GPU from the chat page. The controller stops it after 600 seconds without inference. A local bridge counts the complete Ollama request stream, including background requests, and blocks shutdown while requests are active. Failed startup attempts trigger a stop; API errors are retried. This is application-managed shutdown, not a provider billing cap: a prolonged Heroku or Runpod outage can delay it. After a web application restart, the controller reconnects to an already running pod and re-enables the idle timer, without releasing its GPU.

## Secrets

Keep secrets in Heroku config vars and ignored local `.env` files. Cloudflare and Heroku share `FULHOUSE_ORIGIN_SECRET`. The Runpod API key exists only in Heroku config vars. Never commit credentials, private SSH keys or conversations.

Required config: `DATABASE_URL`, `WEBUI_SECRET_KEY`, `FULHOUSE_ORIGIN_SECRET`, `FULHOUSE_ADMIN_PASSWORD_HASH`, `RUNPOD_API_KEY`, `RUNPOD_POD_ID`, `RUNPOD_SSH_KEY`, `RUNPOD_SSH_HOST_KEY`.

Runpod replaces the container on stop/start. Its SSH host keys are therefore stored in root-only `/workspace/ssh-host-keys`. Pod container arguments point to `/workspace/boot-fulhouse.sh` (source in `ops/`), which restores them before the official startup script. Verify the initial public host key over the authenticated Runpod SSH proxy before pinning it in Heroku. Never disable host-key verification.

## Deploy

Heroku builds the pinned upstream Docker image using `heroku.yml`:

```sh
git push heroku HEAD:main
wrangler pages deploy pages --project-name ful-house --branch main
```

Keep `pages/static` and `app/static` synchronized. Cloudflare compatibility date must not be in the future in UTC. Deploying or changing Heroku config restarts the web process and temporarily shows the startup page.

## Validation

```sh
python3 -m venv .venv
.venv/bin/pip install httpx==0.28.1 aiohttp==3.13.3 starlette==0.49.3 bcrypt==4.3.0
.venv/bin/python -m unittest discover -s tests -v
```

Tests cover request/stop exclusion, API failure handling, login alias, blocked signup, origin checks and streamed inference accounting. Live validation must additionally check login, model startup after a complete pod stop, an actual model response, and shutdown.

## Scope and archive

The legacy website, including previously uncommitted local work, is preserved in `archive/2026-09-19-legacy-site`, with a SHA-256 manifest. It is excluded from both deployments. The original local website folder also remains intact.

File uploads currently use ephemeral Heroku storage; do not use this deployment as a document archive. Code execution, code interpreter and web search are disabled. Image generation is a separate future integration; this deployment provides the coding chat model.
