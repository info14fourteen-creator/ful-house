# Fullhouse AI implementation plan

Goal: private Open WebUI at https://ful.house with Homebrew monochrome styling and a Matrix waiting screen.

Architecture: Cloudflare Pages proxies to a separate Heroku Open WebUI container. Postgres persists users and chats independently of dyno restarts. A small ASGI extension provides authenticated Runpod controls and a private SSH bridge to the existing Ollama pod. GPU auto-stop only runs when no inference is active. Deployment is blocked until hosting budget and credentials are ready.

Approved design: Open WebUI chat, files, desktop/mobile layouts; steelstan admin; no public signup; green on black using the user's Terminal Homebrew profile; animated Matrix during model startup; actual status instead of simulated percentage; root ful.house; legacy archive; changes pushed to GitHub.

## Files and verification
- [x] archive/2026-09-19-legacy-site and hash manifest preserve existing content and local edits.
- [ ] app/static/homebrew.css and matrix.js: theme and loading/status UI; respect reduced motion, keyboard navigation and small screens.
- [ ] Dockerfile and app/entrypoint.sh: pinned official Open WebUI image; app config from env only; persistent external database; disable public signup and remote tools by default.
- [ ] app/control.py: same-origin admin-only start/stop/status; exact pod id only; timeout and in-flight protection; no keys in responses.
- [ ] pages/_worker.js: streaming reverse proxy; preserve WebSockets; bypass caching private responses; upstream secret protects direct origin.
- [ ] tests: authorization denial, origin enforcement, idle shutdown blocked during inference, upstream failures and path validation.
- [ ] deploy: Heroku and Cloudflare; publish from clean verified commit; smoke test root, login denial and model status; test real inference only with GPU budget.

## Operations
Never commit .env, SSH keys, passwords, tokens or user data. Existing site's archive is repository-only, not web-served. The approved GPU test resource is stopped. Obtain an application-scoped Runpod API credential before automatic start/stop can work. Do not use an interactive OAuth session as a backend credential. Password in prior clipboard must be reconfirmed through local secure setup if no longer present.
