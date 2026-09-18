# Fullhouse AI

Private Open WebUI deployment for ful.house. Personal Homebrew green-monochrome theme inspired by Pravetz 8A, with a Matrix-style model startup screen.

Legacy website, including previously uncommitted local work, is preserved in `archive/2026-09-19-legacy-site`. The adjacent SHA-256 manifest verifies the archive. Archive files are not deployed.

Status: deployment in preparation. Infrastructure, login and model controls must pass smoke tests before being declared ready.

Secrets belong only in ignored `.env` files and hosting secret stores. The repository must never contain credentials or conversations.

## Deployment prerequisites

- Hosting budget approval is pending (proposed Heroku Basic plus Postgres).
- Set `FULHOUSE_ADMIN_PASSWORD_HASH` to the bcrypt hash of the chosen admin password. Never put plaintext credentials in this repository.
- Set an application-scoped `RUNPOD_API_KEY`, the existing dedicated `RUNPOD_SSH_KEY`, and pinned `RUNPOD_SSH_HOST_KEY` in the hosting secret store.
- Set `WEBUI_SECRET_KEY`, `FULHOUSE_ORIGIN_SECRET` and `DATABASE_URL`. Cloudflare Pages and Heroku must share the origin secret.
- Finish container smoke tests before publishing. Verify the image tag, static asset paths, database initialization, login alias and streaming/WebSockets.
- The current request counter covers HTTP chat routes. Before enabling idle-stop in production, count actual Ollama inference traffic through a local bridge as Open WebUI can dispatch background jobs after its HTTP response ends. Verify shutdown on host restart and recovery after Runpod API outages.

## Local validation

`python3 -m venv .venv && .venv/bin/pip install httpx==0.28.1`

`.venv/bin/python -m unittest discover -s tests -v`

The six controller unit tests cover fail-closed missing credentials, request/stop exclusion, idempotent stop, and API failure. They are not an end-to-end deployment test.
