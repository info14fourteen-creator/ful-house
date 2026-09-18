# Publishing Access Map

Дата проверки: 2026-07-05

Цель: понять, какие уже настроенные доступы можно использовать для публикации текущего проекта `ФУЛХАУС сайт`.

## Найденные соседние проекты

### 4TEEN / Tronix Rent

Основные кандидаты:

- `/Users/stanataev/Documents/ASTS/4teen-website-seo-release`
- `/Users/stanataev/Documents/ASTS/4teen-website-seo-release2`
- `/Users/stanataev/Documents/tron-energy-broker`

`4teen-website-seo-release2` использует:

- Next.js 16 app router;
- OpenNext adapter for Cloudflare Workers;
- Wrangler;
- `wrangler.jsonc`;
- deploy script: `pnpm run cf:deploy`;
- worker name: `4teen-website`;
- Cloudflare direct worker URL указан в README: `https://4teen-website.stan-at.workers.dev`.

`tron-energy-broker` использует:

- Node/TypeScript backend;
- Heroku remote: `https://git.heroku.com/energy-desk-tron.git`;
- Heroku app: `energy-desk-tron`;
- `heroku-postbuild`: `pnpm build`.

## Доступы, которые подтверждены

### GitHub

- GitHub CLI авторизован под `info14fourteen-creator`.
- Token scope включает `repo`.
- Репозиторий текущего проекта доступен: `https://github.com/info14fourteen-creator/ful-house`.
- `ful-house` публичный, default branch: `main`.
- `ASTS` публичный, default branch: `main`.
- `tron-energy-broker` приватный, default branch: `main`.

### GitHub Pages

- У `info14fourteen-creator/ASTS` GitHub Pages включен:
  - URL: `https://info14fourteen-creator.github.io/ASTS/`
  - build type: `workflow`
  - source branch: `main`
  - HTTPS enforced: true
- У `info14fourteen-creator/ful-house` GitHub Pages пока не включен: API вернул `404`.

### Heroku

- Heroku CLI авторизован как `genesis@4teen.me`.
- Доступные app names:
  - `energy-desk-tron`
  - `fourteen-allocation-worker`
  - `fourteen-wallet-api`

### Cloudflare / Wrangler

- В соседнем проекте есть рабочий Cloudflare Workers стек через OpenNext.
- `wrangler` установлен и запускается.
- `wrangler whoami` завис на "Getting User settings", поэтому Cloudflare login надо перепроверить перед реальным деплоем.

## Рекомендация для текущего сайта

Текущий `ФУЛХАУС сайт` - статический HTML/CSS/JS без `package.json`, `vercel.json`, `netlify.toml`, `wrangler.toml` и build step.

Самый быстрый путь публикации:

1. Включить GitHub Pages для `info14fourteen-creator/ful-house`.
2. Использовать source `main` + root `/` или GitHub Actions workflow для Pages.
3. Публиковать статические HTML/CSS/JS напрямую.

Cloudflare Workers/OpenNext стоит использовать позже, если проект мигрирует в Next.js с backend/API/AI-agent routes.

Heroku не подходит для текущего статического сайта как первый выбор. Он уместен для backend/API, например для будущего evaluator service, hand history API или RSS ingestion service.

## Что не делать автоматически

- Не переносить секреты из соседних `.env` файлов.
- Не печатать API keys, mnemonic, private keys, deploy tokens.
- Не включать real-money poker, депозиты, выплаты или gambling-функции.
- Не деплоить на Heroku/Cloudflare без явной команды, потому что это изменяет внешнюю инфраструктуру.

## Следующий практичный шаг

Когда нужно будет публиковать MVP:

1. Создать или включить GitHub Pages для `ful-house`.
2. Проверить локально все HTML-страницы.
3. Обновить `sitemap.xml`, `robots.txt`, canonical URLs.
4. Запушить в `main`.
5. Проверить опубликованный URL.
