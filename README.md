# Fullhouse AI

Private Open WebUI at https://ful.house with a Homebrew green monochrome theme, Pravetz 8A details and a Matrix animation while the GPU starts. Admin login: `steelstan`. Public signup is disabled.

## Infrastructure

- Cloudflare Pages project `ful-house` proxies to Heroku `fulhouse-ai`. Theme assets and the cold-start page are served at the edge.
- Heroku Standard-2X (1 GB, $50/month) and Postgres essential-0 ($5/month). Chats and accounts persist in Postgres.
- Runpod workers use NVIDIA L40S at up to $1.09/hour. A separate 40 GB network volume `0tx6fqunoc` in US-TX-3 keeps the runtime, model and SSH identity ($2.80/month). Idle shutdown deletes only the worker, never the network volume; the next login creates a worker on available capacity without downloading the model again.
- Ollama 0.34.2, model `huihui_ai/qwen3-coder-abliterated:30b`, stored under `/workspace/ollama`, with 32K context. Ollama only listens on loopback and is reached through a pinned SSH tunnel.

A successful terminal login starts the GPU and shows the Matrix loading screen until readiness. The administrator can also start and stop it from the chat page. The controller stops it after 600 seconds without inference. A local bridge counts the complete Ollama request stream, including background requests, and blocks shutdown while requests are active. Failed startup attempts trigger a stop; API errors are retried. This is application-managed shutdown, not a provider billing cap: a prolonged Heroku or Runpod outage can delay it. After a web application restart, the controller reconnects to an already running pod and re-enables the idle timer, without releasing its GPU.

## Secrets

Keep secrets in Heroku config vars and ignored local `.env` files. Cloudflare and Heroku share `FULHOUSE_ORIGIN_SECRET`. The Runpod API key exists only in Heroku config vars. Never commit credentials, private SSH keys or conversations.

Required config: `DATABASE_URL`, `WEBUI_SECRET_KEY`, `FULHOUSE_ORIGIN_SECRET`, `FULHOUSE_ADMIN_PASSWORD_HASH`, `RUNPOD_API_KEY`, `RUNPOD_NETWORK_VOLUME_ID`, `RUNPOD_DATA_CENTER`, `RUNPOD_SSH_PUBLIC_KEY`, `GPU_MAX_HOURLY_USD`, `RUNPOD_SSH_KEY`, `RUNPOD_SSH_HOST_KEY`.

Runpod replaces the container on stop/start. Its SSH host keys are therefore stored on the private network volume in `/workspace/ssh-host-keys`. Pod container arguments point to `/workspace/boot-fulhouse.sh` (source in `ops/`), which restores them and explicitly sets private-key permissions to 0600 before the official startup script. Network storage does not preserve the expected Unix modes. Verify the initial public host key over the authenticated Runpod SSH proxy before pinning it in Heroku. Never disable host-key verification.

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
.venv/bin/pip install httpx==0.28.1 aiohttp==3.13.3 starlette==0.49.3 bcrypt==4.3.0 psycopg[binary]==3.3.4
.venv/bin/python -m unittest discover -s tests -v
```

Tests cover request/stop exclusion, API failure handling, login alias, blocked signup, origin checks and streamed inference accounting. Live validation must additionally check login, model startup after a complete pod stop, an actual model response, and shutdown.

## Scope and archive

The legacy website, including previously uncommitted local work, is preserved in `archive/2026-09-19-legacy-site`, with a SHA-256 manifest. It is excluded from both deployments. The original local website folder also remains intact.

File uploads currently use ephemeral Heroku storage; do not use this deployment as a document archive. Code execution, code interpreter and web search are disabled. Image generation is a separate future integration; this deployment provides the coding chat model.

Login attempts are limited per source IP: 12 attempts per window, followed by a 15-minute lock. Successful authentication resets the counter. Failed login never deletes user data.

## Inactivity

A shared edge-served script covers chat, terminal login and the cold-start page. After 60 seconds without trusted mouse, touch, keyboard or wheel input, a full-screen green Matrix animation covers the page. The first wake input dismisses it without submitting or clicking controls underneath. Background inference and polling do not reset this timer. Activity is synchronized between tabs.

After 20 minutes of human inactivity, authenticated tabs call the upstream signout endpoint, clear local authentication and return to `/auth`. The single-process server persists revoked-token fingerprints in Postgres and loads them at startup; no extra Redis service is needed. Wall-clock deadlines are checked before wake input and on page visibility changes, so a sleeping laptop cannot revive an expired session. When offline, local authentication is cleared and the private page is left; the signout request cannot be guaranteed to reach the server until connectivity exists. This is a browser idle logout, not an API-token lifetime policy.

Run timer boundary and wake-event tests with `node --test tests/test_idle.cjs`.
