# Poker Platform Progress

## 2026-07-05

### Step 1. Зафиксировать позиционирование

- Work done: оформлено позиционирование AI poker trainer: образовательная play-money платформа, не casino/gambling.
- Files changed: `docs/product-positioning.md`.
- Verification: документ создан и привязан к safety-рамке продукта.
- Blockers: нет.

### Step 2. Составить sitemap

- Work done: создана карта страниц первой версии, URL-структура и MVP-приоритеты.
- Files changed: `docs/site-map.md`.
- Verification: sitemap покрывает главную, диагностику, обучение, статьи, турниры, RSS и responsible play.
- Blockers: нет.

### Step 3. Описать ключевые user journeys

- Work done: описаны основные сценарии для диагностики, новичка, любителя, среднего игрока, MTT-игрока, читателя новостей и возвращающегося пользователя.
- Files changed: `docs/user-journeys.md`.
- Verification: сценарии связаны с уровнями, AI-агентами, обучением и RSS/контентом.
- Blockers: нет.

### Step 4. Утвердить уровни игроков 0-6

- Work done: описана шкала уровней от First Hand до Pro Lab и правило присвоения уровня по качеству решений.
- Files changed: `docs/player-levels.md`.
- Verification: уровни покрывают новичков, любителей, regular/grinder и advanced/pro training.
- Blockers: нет.

### Step 5. Описать метрики диагностики уровня

- Work done: зафиксированы метрики preflop, position, aggression, calling/fold discipline, value, bluff logic, board texture, pot odds, multi-street и tournament pressure.
- Files changed: `docs/diagnostic-metrics.md`.
- Verification: метрики ориентированы на решения, а не на краткосрочный выигрыш/проигрыш.
- Blockers: нет.

### Step 6. Описать 10 типов ошибок игрока

- Work done: создана taxonomy ошибок и формат объяснения ошибки пользователю.
- Files changed: `docs/error-taxonomy.md`.
- Verification: ошибки связаны с будущими тренировками и Coach Agent.
- Blockers: нет.

### Step 7. Описать AI-агентов и их роли

- Work done: описаны Game Engine, Skill Evaluator, Curriculum Agent, Coach Agent, игровые боты и Safety Agent.
- Files changed: `docs/ai-agents.md`.
- Verification: зафиксировано правило, что LLM не управляет правилами покера, а только выбирает легальные действия/объясняет.
- Blockers: нет.

### Step 8. Определить MVP: статический интерактивный прототип, backend, Telegram Mini App и macOS roadmap

- Planned: зафиксировать границы первой поставки, отделить статический интерактивный прототип от backend-этапа и описать роль Telegram Mini App и будущего macOS app.
- Done: создан документ с поэтапным MVP-контуром: static interactive prototype, backend foundation, Telegram Mini App roadmap и macOS thin-client roadmap с сохранением play-money/educational рамки.
- Files changed: `docs/mvp-scope.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web закреплен как основная поверхность первой поставки с полной mock-диагностикой, контентом и AI training flow.
- Mobile impact: mobile web включен в static prototype как обязательная адаптивная поверхность без отдельного урезанного scope.
- Telegram Mini App impact: mini app определен как короткая surface для 3-5 раздач, daily hand challenge и возврата в основной продукт после backend stage.
- macOS impact: macOS app определен как будущий thin client/wrapper над общей логикой, а не отдельная самостоятельная версия на первом этапе.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md` и текущий `POKER_PLATFORM_PROGRESS.md`; новый документ покрывает все четыре поверхности и не дублирует предыдущие шаги 1-7.
- Remaining: шаги 9-12 должны наполнить MVP контентом первой недели, SEO-ядром, юридическими ограничениями и acceptance criteria.
- Blockers: нет.

### Publishing access discovery. Соседние проекты 4TEEN / Tronix Rent

- Work done: проверены соседние проекты `ASTS/4teen-website-seo-release*`, `tron-energy-broker` и Cloudflare/Heroku/GitHub следы публикации.
- Files changed: `docs/publishing-access.md`.
- Verification: подтверждены GitHub CLI, Heroku CLI, GitHub Pages для `ASTS`; для `ful-house` Pages пока не включен; Cloudflare/Wrangler требует повторной проверки логина.
- Blockers: GitHub Pages для `ful-house` нужно включить отдельным действием перед публикацией.

### Process update. Сверка после каждого шага и платформы

- Planned: учесть требование сверяться после каждого из 72 шагов и не забыть desktop, mobile, Telegram Mini App и macOS app.
- Done: добавлен обязательный формат сверки после каждого инкремента и отдельные требования по платформам.
- Files changed: `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web закреплен как основная рабочая поверхность.
- Mobile impact: mobile web закреплен как обязательная удобная версия, не вторичный обрезок.
- Telegram Mini App impact: mini app добавлен как отдельная продуктовая поверхность для быстрых диагностик и daily hand.
- macOS impact: macOS app добавлен как будущий desktop-клиент в духе Tronix Rent.
- Verification: план и прогресс обновлены, новая структура сверки добавлена в документы.
- Remaining: обновить prompt автоматизации, чтобы каждый запуск соблюдал новую сверку.
- Blockers: нет.

### Step 9. Составить список контента для первой недели

- Planned: составить приоритетный список контента первой недели запуска, который поддерживает диагностику, обучение, новости, турниры и возврат пользователя без ухода в real-money или копипаст внешних статей.
- Done: создан недельный контентный план с 22 единицами контента, разбитыми по дням, форматам и четырем поверхностям продукта; зафиксированы hero copy, обучающие страницы, AI identity блоки, news/tournament материалы и return-модули.
- Files changed: `docs/week-one-content-plan.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил понятный контентный порядок для главной, обучающих страниц, статей, новостей и турниров как полноценного content hub.
- Mobile impact: mobile web заранее учтен через короткие intro-блоки, card-summary и вертикальные форматы чтения без перегруза экрана.
- Telegram Mini App impact: для mini app выделены короткие surface-форматы: daily hand challenge, next lesson, краткие summaries статей и новостей с переходом в основной web-продукт.
- macOS impact: контент спроектирован секциями и модулями, которые позже можно перенести в sidebar/library и быстрые открытия будущего macOS app.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `docs/site-map.md`, `docs/user-journeys.md`, `docs/mvp-scope.md` и текущий `POKER_PLATFORM_PROGRESS.md`; новый план не дублирует шаги 1-8 и не забирает работу у будущих шагов 25-36 глубже необходимого.
- Remaining: следующий шаг 10 должен собрать SEO-ядро на основе этого недельного плана и приоритетных обучающих/редакционных тем.
- Blockers: нет.

### Step 10. Составить SEO-ядро

- Planned: собрать первичное SEO-ядро для poker trainer-платформы вокруг обучения покеру, правил, комбинаций, турниров и тренажера решений без ухода в casino/real-money интенты.
- Done: создан отдельный SEO-документ с keyword clusters, RU-first терминами, keyword-to-page mapping, internal linking contract, metadata direction и safety/exclusion списком; ядро связано с sitemap, недельным контент-планом и четырьмя поверхностями продукта.
- Files changed: `docs/seo-core.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил основу для будущих hub pages, article titles, навигационных связей и метаданных вокруг AI trainer и poker learning intent.
- Mobile impact: mobile web получил те же SEO-кластеры с поправкой на короткие intro-блоки, summary-first copy и чтение без горизонтального скролла.
- Telegram Mini App impact: mini app не рассматривается как primary SEO surface, но keyword themes закреплены для deep-link copy, daily hand summaries и возврата пользователя в индексируемый web-контент.
- macOS impact: будущий macOS app получил согласованную taxonomy разделов и library-модулей, чтобы названия экранов и saved content не расходились с web SEO-структурой.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `docs/site-map.md`, `docs/week-one-content-plan.md` и текущий `POKER_PLATFORM_PROGRESS.md`; новый `docs/seo-core.md` закрывает Step 10 и не дублирует глубоко будущие шаги 25-36.
- Remaining: следующий шаг 11 должен зафиксировать юридические ограничения и связать их с SEO/safety wording на страницах.
- Blockers: нет.

### Step 11. Составить юридические ограничения

- Planned: зафиксировать обязательные юридические и safety-ограничения для play-money/educational poker platform, включая 18+, no income promises, safe wording и правила для news/tournament surfaces.
- Done: создан отдельный документ с product/legal constraints, запрещенными и обязательными паттернами, copy/SEO guardrails и surface-specific rules для desktop web, mobile web, Telegram Mini App и будущего macOS app.
- Files changed: `docs/legal-constraints.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил четкий safety-контур для hero, diagnostic flow, article/news/tournament sections и будущих AI explanation screens без casino wording и money mechanics.
- Mobile impact: mobile web получил требования к компактным, читаемым safety-labels и дисклеймерам без overlap на узком экране и без потери educational framing.
- Telegram Mini App impact: mini app получил отдельные ограничения на короткий wording, visible 18+/play-money framing и запрет на любые real-money или betting-like flows.
- macOS impact: будущий macOS app закреплен как клиент той же educational/play-money системы без wallet/profit language и без расхождения с web safety-контуром.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `docs/product-positioning.md`, `docs/mvp-scope.md`, `docs/seo-core.md` и текущий `POKER_PLATFORM_PROGRESS.md`; новый документ закрывает Step 11 и не дублирует Step 1 или Step 10 сверх необходимого.
- Remaining: следующий шаг 12 должен превратить product, safety и platform requirements в acceptance criteria первой версии.
- Blockers: нет.

### Step 12. Подготовить acceptance criteria для desktop, mobile, Telegram Mini App и macOS-roadmap первой версии

- Planned: собрать единый acceptance-контракт первой версии на основе уже утвержденных positioning, MVP scope, sitemap и legal constraints без дублирования предыдущих шагов.
- Done: создан документ с общими критериями приемки v1 и отдельными acceptance criteria для desktop web, mobile web, Telegram Mini App roadmap, macOS app roadmap, а также с общими safety/content stop-conditions и verification checklist.
- Files changed: `docs/v1-acceptance-criteria.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил проверяемый список обязательных экранов, UX-сценариев и layout-ожиданий для первой поставки.
- Mobile impact: mobile web получил отдельные критерии по вертикальному потоку, отсутствию overlap, thumb-friendly actions и читаемости safety/content blocks.
- Telegram Mini App impact: mini app закреплен как short-session roadmap surface с компактным scope и общими data/safety contracts, а не как урезанная копия desktop.
- macOS impact: macOS roadmap зафиксирован как thin-client stage над общей логикой с ясными будущими сценариями и без отдельного product drift.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `docs/mvp-scope.md`, `docs/legal-constraints.md`, `docs/site-map.md` и текущий `POKER_PLATFORM_PROGRESS.md`; новый документ не повторяет шаги 8 и 11, а переводит их в критерии приемки.
- Remaining: следующий шаг 13 должен перейти от продуктового контракта к визуальной палитре и дизайн-системе.
- Blockers: нет.

### Step 13. Собрать визуальную палитру

- Planned: собрать темную визуальную палитру для AI poker trainer с felt green, chip red и gold accents, чтобы она направляла будущую дизайн-систему и не возвращала проект в светлый B2B-стиль текущего сайта.
- Done: создан документ палитры с core color tokens, gradient directions, usage rules, accessibility notes, migration note from current light theme и surface-specific guidance для desktop web, mobile web, Telegram Mini App и будущего macOS app.
- Files changed: `docs/visual-palette.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил базовую color architecture для table layer, training HUD, content rail и dark shell без casino-neon визуального шума.
- Mobile impact: mobile web получил ограничения по контрасту, компактности оттенков и правила, чтобы CTA, review labels и игровой UI оставались читаемыми на узком экране.
- Telegram Mini App impact: mini app получил сокращенный token set и guidance избегать тяжелых градиентов и glow-эффектов, чтобы сохранить скорость и простоту коротких сессий.
- macOS impact: будущий macOS app получил совместимую dark palette для sidebar, session history, compact chrome и training desktop shell без расхождения с web-версией.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, текущий `POKER_PLATFORM_PROGRESS.md` и существующая светлая палитра в `assets/styles.css`; новый `docs/visual-palette.md` закрывает только Step 13 и готовит Step 14 без дублирования типографики или layout-решений.
- Remaining: следующий шаг 14 должен зафиксировать типографику, размеры и общую плотность интерфейса поверх этой палитры.
- Blockers: нет.

### Step 14. Определить типографику, размеры, плотность интерфейса

- Planned: зафиксировать шрифтовую систему, type scale, spacing scale и density modes для poker training platform так, чтобы будущий редизайн не унаследовал светлый B2B-ритм текущего сайта и оставался согласованным на desktop web, mobile web, Telegram Mini App и macOS app.
- Done: создан дизайн-контракт типографики и плотности интерфейса с display/UI/mono families, desktop/mobile scale, тремя density modes, component sizing guidance, surface-specific rules и migration notes от текущего `Inter`-only светлого фронтенда.
- Files changed: `docs/typography-density.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил базовые правила для hero, section headings, analytics rail, table/HUD density и content width, чтобы следующие экраны не расползались между marketing и trainer UI.
- Mobile impact: mobile web получил отдельный scale, thumb-friendly control sizing и ограничения на captions/metadata, чтобы будущие игровые и контентные экраны не ломались на узком вьюпорте.
- Telegram Mini App impact: mini app получил сокращенный типографический диапазон и compact density guidance для коротких диагностических и result-сценариев без тяжелых текстовых блоков.
- macOS impact: будущий macOS app получил совместимые desktop typography/density rules для sidebar, history и training shell без визуального расхождения с web-версией.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `docs/visual-palette.md`, текущий `POKER_PLATFORM_PROGRESS.md`, а также существующие `index.html` и `assets/styles.css`; новый `docs/typography-density.md` закрывает только Step 14 и не забирает работу у будущих layout-шагов 15-24.
- Remaining: следующий шаг 15 должен перевести palette и typography contract в структуру header/navigation для RU-first poker сайта.
- Blockers: нет.

### Step 15. Спроектировать header/nav для RU-first сайта

- Planned: зафиксировать RU-first header/navigation contract для poker training platform так, чтобы он направлял пользователя в диагностику, обучение, тренажер и контент, не дублировал текущую B2B IA и оставался согласованным на desktop web, mobile web, Telegram Mini App и macOS app.
- Done: создан navigation-spec с IA-кластерами, top-level labels, desktop/mobile behavior rules, Telegram Mini App tab model, macOS sidebar mapping, CTA strategy, state model и responsive/safety guardrails без захода в финальный visual implementation.
- Files changed: `docs/header-nav-ru-first.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил product-first header order, sticky behavior, overflow rules и приоритет CTA `Определить уровень` вместо текущей service-oriented B2B navigation.
- Mobile impact: mobile web получил compact header + drawer model с thumb-friendly targets и короткими labels без двухуровневых меню и overlap-рисков.
- Telegram Mini App impact: mini app получил отдельную короткую tab/navigation model для быстрых диагностик и возврата в план без копирования full web header.
- macOS impact: будущий macOS app получил согласованную sidebar IA с теми же названиями разделов и акцентом на plan/history/quick launch вместо browser-like top nav.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `docs/visual-palette.md`, `docs/typography-density.md`, текущий `POKER_PLATFORM_PROGRESS.md`, а также существующая навигация в `index.html` и стили header в `assets/styles.css`; новый `docs/header-nav-ru-first.md` закрывает только Step 15 и не забирает работу у шагов 16-24.
- Remaining: следующий шаг 16 должен превратить navigation contract в первый экран с покерным столом и встроенным action-first hero.
- Blockers: нет.

### Step 16. Спроектировать первый экран с покерным столом

- Planned: зафиксировать контракт первого экрана главной страницы с покерным столом, diagnostic-first hero, safety framing и адаптацией под desktop web, mobile web, Telegram Mini App и будущий macOS app без ухода в соседние экранные шаги.
- Done: создан отдельный first-screen spec с message hierarchy, split/staked layouts, table illustration rules, diagnostic preview module, CTA contract, mobile constraints, migration note от текущего B2B hero и запретами на casino/gambling паттерны.
- Files changed: `docs/first-screen-poker-table.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил ясный hero contract `content left / table right` с заметным CTA диагностики, trust labels и table-centric product scene вместо текущего B2B photo hero.
- Mobile impact: mobile web получил вертикальную hero-структуру с ограничениями против overlap, короткими safety labels, компактным table preview и thumb-friendly CTA order.
- Telegram Mini App impact: mini app получил сокращенную message stack для quick level check и table preview без попытки копировать full web hero один в один.
- macOS impact: будущий macOS app получил совместимый стартовый dashboard pattern со split-shell, table preview и diagnostic summary без расхождения с web wording.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `docs/header-nav-ru-first.md`, `docs/visual-palette.md`, `docs/typography-density.md`, `docs/legal-constraints.md`, текущий `index.html`, `assets/styles.css` и `POKER_PLATFORM_PROGRESS.md`; новый документ закрывает только Step 16 и готовит шаги 17-24 без дублирования их детальной UI-работы.
- Remaining: следующий шаг 17 должен спроектировать карточки AI-агентов как следующий слой после hero-screen.
- Blockers: нет.

### Step 17. Спроектировать карточки AI-агентов

- Planned: зафиксировать card-system для AI-агентов так, чтобы он опирался на уже описанные роли из Step 7 и соседние дизайн-спеки, но не дублировал их и не забирал работу у HUD/result/persona screens.
- Done: создан отдельный spec карточек AI-агентов с разделением на training opponents и system AI, anatomy карточки, visual/content rules, placement guidance и responsive contract для desktop web, mobile web, Telegram Mini App и будущего macOS app.
- Files changed: `docs/ai-agent-cards.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил структуру секции с grid карточек ботов и компактным блоком system AI, которую можно безопасно встроить под hero без смешения с news/tournament content.
- Mobile impact: mobile web получил ограничения на card stacking, CTA sizing, tags wrapping и читаемость длинных agent labels без overlap на узком экране.
- Telegram Mini App impact: mini app получил укороченную модель agent cards с максимум 2-3 ключевыми карточками в одном потоке и компактным summary-first контентом.
- macOS impact: будущий macOS app получил согласованную card/list hybrid модель для sidebar/library и quick training launch без расхождения названий и ролей агентов с web.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, текущий `POKER_PLATFORM_PROGRESS.md`, `docs/ai-agents.md`, `docs/first-screen-poker-table.md`, `docs/header-nav-ru-first.md` и `docs/typography-density.md`; новый документ закрывает только Step 17 и сохраняет границы следующих шагов 18-20 и 28.
- Remaining: следующий шаг 18 должен спроектировать HUD диагностики и использовать согласованные skill tags, level markers и card-to-drill связи из текущего card spec.
- Blockers: нет.

### Step 18. Спроектировать HUD диагностики

- Planned: зафиксировать contract диагностического HUD для live-сессий так, чтобы он показывал progress, active skill lens и промежуточную аналитику без перегруза стола и без дублирования будущего result screen.
- Done: создан отдельный HUD spec с module hierarchy, layout rules, state model, tone of voice, metric visibility boundaries и responsive guidance для desktop web, mobile web, Telegram Mini App и будущего macOS app.
- Files changed: `docs/diagnostic-hud.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил analytical rail contract и правила, как держать progress/readouts рядом со столом без перекрытия board, pot и action controls.
- Mobile impact: mobile web получил compact HUD stack с приоритетом top progress strip, active lens chips и короткого running read без overlap на узком экране.
- Telegram Mini App impact: mini app получил сокращенный HUD subset для быстрых 3-5 hand diagnostics без heavy panels и длинных пояснений.
- macOS impact: будущий macOS app получил совместимую persistent side-panel модель, которая использует те же skill labels и state transitions, что и web-версия.
- Verification: сверены `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, текущий `POKER_PLATFORM_PROGRESS.md`, `docs/diagnostic-metrics.md`, `docs/ai-agent-cards.md`, `docs/first-screen-poker-table.md` и `docs/typography-density.md`; новый `docs/diagnostic-hud.md` закрывает только Step 18 и не забирает scoring/result работу у шагов 19 и 37-48.
- Remaining: следующий шаг 19 должен спроектировать экран результата уровня и использовать границы live HUD vs post-session analytics из текущего spec.
- Blockers: нет.

### 2026-07-05 — Step 18

- Planned: спроектировать HUD диагностики для live-сессий с учетом desktop web, mobile web, Telegram Mini App и будущего macOS app.
- Done: создан `docs/diagnostic-hud.md` с иерархией модулей HUD, state model, responsive layout rules, visibility boundaries для метрик и safety/tone guidance; прогресс обновлен.
- Files changed: `docs/diagnostic-hud.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: описан боковой analytical rail и правила сохранения свободной table surface без перекрытия board и action area.
- Mobile impact: описан компактный stacked HUD без overlap, с top progress strip и короткими аналитическими блоками.
- Telegram Mini App impact: зафиксирован минимальный HUD subset для коротких диагностик и возврата в основной web flow.
- macOS impact: закреплен будущий persistent-side-panel подход над общей логикой и теми же skill labels.
- Verification: выполнена сверка roadmap и progress; документ сопоставлен с `docs/diagnostic-metrics.md`, `docs/ai-agent-cards.md`, `docs/first-screen-poker-table.md` и `docs/typography-density.md`.
- Remaining: следующий инкремент должен взять Step 19 и спроектировать screen результата уровня.
- Blockers: нет.

### 2026-07-05 — Step 19

- Planned: спроектировать экран результата уровня после диагностической сессии с учетом desktop web, mobile web, Telegram Mini App и будущего macOS app.
- Done: создан `docs/level-result-screen.md` с verdict hierarchy, top leaks/strengths/next-route блоками, responsive layout contract, CTA rules, metric visibility boundaries и tone/safety guidance; прогресс обновлен.
- Files changed: `docs/level-result-screen.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: описан two-column result pattern с level verdict, leaks и action rail без перегруза solver-like таблицами.
- Mobile impact: описан single-column stacked result screen с приоритетом verdict, коротких actionable leaks и CTA без overlap на узком экране.
- Telegram Mini App impact: зафиксирован сокращенный result subset с уровнем, 2 главными ошибками и переходом в полный web-план.
- macOS impact: закреплен совместимый desktop result pattern с утилитарной sidebar-моделью и теми же level/route labels.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, текущего `POKER_PLATFORM_PROGRESS.md`, а также связанных документов `docs/player-levels.md`, `docs/diagnostic-metrics.md`, `docs/diagnostic-hud.md` и `docs/legal-constraints.md`; новый spec закрывает только Step 19 и не забирает работу у Step 20 или scoring-шагов 44-48.
- Remaining: следующий инкремент должен взять Step 20 и спроектировать личную карту обучения.
- Blockers: нет.

### 2026-07-05 — Step 20

- Planned: спроектировать личную карту обучения, которая переводит результат диагностики в последовательный маршрут уроков, тренировок и повторной проверки на desktop web, mobile web, Telegram Mini App и будущем macOS app.
- Done: создан `docs/personal-learning-map.md` с route header, priority leaks rail, module system, next action panel, routing boundaries, responsive behavior rules, CTA contract и handoff-требованиями для будущих шагов 52-55; прогресс обновлен без дублирования result-screen логики.
- Files changed: `docs/personal-learning-map.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил dashboard-паттерн personal plan с видимым next action, route summary и модульной картой без смешения с editorial content.
- Mobile impact: mobile web получил single-column plan flow с приоритетом active module и CTA, без hover-зависимостей и с явными ограничениями против overlap tags/status chips.
- Telegram Mini App impact: mini app получил сокращенную модель personal plan с одним активным модулем, daily hand challenge и переходом в полный web-план.
- macOS impact: будущий macOS app получил утилитарный sidebar + main-pane contract для history, quick relaunch и тех же module/status labels, что и на web.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, а также связанных документов `docs/level-result-screen.md`, `docs/diagnostic-hud.md`, `docs/header-nav-ru-first.md`, `docs/ai-agent-cards.md` и `docs/error-taxonomy.md`; новый spec закрывает только Step 20 и готовит шаги 21 и 52-55.
- Remaining: следующий инкремент должен взять Step 21 и спроектировать страницу статьи, не смешивая editorial layout с personal plan.
- Blockers: нет.

### 2026-07-05 — Step 21

- Planned: спроектировать reusable страницу статьи для poker training platform так, чтобы она поддерживала SEO-материалы, обучающие гайды и разборы ошибок без смешения с tournament/news hub или фактическим написанием статей.
- Done: создан `docs/article-page.md` с article hero, reading column, utility rail, training bridge, related content block, responsive behavior rules, editorial/safety copy guardrails и cross-surface contract для desktop web, mobile web, Telegram Mini App и будущего macOS app; прогресс обновлен без дублирования шагов 22-23 и 29-35.
- Files changed: `docs/article-page.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил clear longform article shell с reading-first колонкой, sticky utility rail и bridge в диагностику, план и связанные guides.
- Mobile impact: mobile web получил single-column article flow с compact TOC, ранним CTA и ограничениями против horizontal scroll и overlap длинных RU-заголовков, tags и meta chips.
- Telegram Mini App impact: mini app получил short-form derivative contract для summaries и return CTA в основной web article вместо тяжелого long-read layout.
- macOS impact: будущий macOS app получил library-style article reader contract с shared tags, section names и переходами в training surfaces без product drift.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, а также связанных документов `docs/header-nav-ru-first.md`, `docs/personal-learning-map.md`, `docs/legal-constraints.md`, `docs/seo-core.md` и `docs/site-map.md`; новый spec закрывает только Step 21 и не забирает работу у tournaments/RSS/content-writing шагов.
- Remaining: следующий инкремент должен взять Step 22 и спроектировать страницу турниров с учетом article/news boundaries, уже зафиксированных в article template.
- Blockers: нет.

### 2026-07-05 — Step 22

- Planned: спроектировать отдельную страницу турниров для poker training platform так, чтобы она связывала curated calendar, объяснение форматов и учебные переходы, не смешиваясь с full news feed или longform article layout.
- Done: создан `docs/tournament-page.md` с hero, featured series/context block, calendar data contract, format education rail, training bridge, responsive behavior rules, filters/sorting guidance и safety/copyright guardrails для desktop web, mobile web, Telegram Mini App и будущего macOS app; прогресс обновлен без захода в реализацию live data или RSS layout.
- Files changed: `docs/tournament-page.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил tournament hub contract с разделением calendar layer, educational rail и internal training CTA без lobby-like или sportsbook-like подачи.
- Mobile impact: mobile web получил single-column tournament stack с chip filters, безопасной meta-структурой карточек и явным запретом на horizontal scroll и overlap длинных RU-названий серий.
- Telegram Mini App impact: mini app получил сокращенный tournament derivative с одним highlight, 1-2 format cards и возвратом в основной web-календарь и учебные материалы.
- macOS impact: будущий macOS app получил совместимую two-pane tournament shell и общую taxonomy форматов/series без отдельного product drift.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, а также связанных документов `docs/article-page.md`, `docs/site-map.md`, `docs/header-nav-ru-first.md`, `docs/seo-core.md` и `docs/legal-constraints.md`; новый spec закрывает только Step 22 и сохраняет границы будущих шагов 23, 35 и 61-64.
- Remaining: следующий инкремент должен взять Step 23 и спроектировать RSS/news layout отдельно от tournament hub.
- Blockers: нет.

### 2026-07-05 — Step 23

- Planned: спроектировать отдельный RSS/news layout для poker training platform как curated external-source hub с собственными summaries, source attribution и переходами в обучение без смешения с tournament calendar или longform article shell.
- Done: создан `docs/rss-news-layout.md` с hero, featured brief, news feed layer, topic clusters, training bridge, responsive behavior rules, source/copyright guardrails и cross-surface contract для desktop web, mobile web, Telegram Mini App и будущего macOS app; прогресс обновлен без захода в live RSS implementation.
- Files changed: `docs/rss-news-layout.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил contract news hub с разделением featured brief, external-source feed и context rail без скатывания в media-portal или gambling-promotional подачу.
- Mobile impact: mobile web получил single-column summary feed с ограничениями против overlap meta/buttons, horizontal scroll и перегруженных карточек на узком экране.
- Telegram Mini App impact: mini app получил compact derivative news subset с 1 featured brief, 3-5 краткими items и возвратом в основной web feed и related guides.
- macOS impact: будущий macOS app получил совместимую two-pane news reader модель с той же taxonomy тем, attribution pattern и переходами в guides/tournaments/plan.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, а также связанных документов `docs/article-page.md`, `docs/tournament-page.md`, `docs/legal-constraints.md`, `docs/seo-core.md` и `docs/site-map.md`; новый spec закрывает только Step 23 и сохраняет границы будущих шагов 61-63 и 65-70.
- Remaining: следующий инкремент должен взять Step 24 и проверить desktop/mobile responsive states уже на уровне собранных design specs блока 2.
- Blockers: нет.

### 2026-07-05 — Step 24

- Planned: проверить desktop и mobile responsive состояния на уровне уже собранных design-specs блока 2 и зафиксировать общие breakpoint/risk rules без перехода в production implementation.
- Done: создан `docs/responsive-states-audit.md` с breakpoint baseline, cross-screen responsive audit для navigation, hero, AI cards, HUD, result screen, personal plan, article, tournaments и RSS/news, а также с общими mobile risk checks и адаптациями для Telegram Mini App и будущего macOS app.
- Files changed: `docs/responsive-states-audit.md`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил единый responsive contract для split layouts, rails, calendar/feed shells и table-centric screens, чтобы следующие UI-этапы не расходились по структуре.
- Mobile impact: mobile web получил consolidated anti-overlap rules, stacked fallbacks, chip/meta/CTA ограничения и explicit запрет на horizontal scroll в ключевых сценариях.
- Telegram Mini App impact: mini app закреплен как lightweight derivative с summary-first modules вместо буквального переноса desktop/mobile layouts.
- macOS impact: будущий macOS app получил подтверждение, что desktop-patterns уже совместимы с sidebar + main-pane shell без отдельного IA drift.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, `docs/header-nav-ru-first.md`, `docs/first-screen-poker-table.md`, `docs/ai-agent-cards.md`, `docs/diagnostic-hud.md`, `docs/level-result-screen.md`, `docs/personal-learning-map.md`, `docs/article-page.md`, `docs/tournament-page.md`, `docs/rss-news-layout.md`, а также текущих `index.html` и `assets/styles.css` как migration reference.
- Remaining: следующий инкремент должен взять Step 25 и начать переписывать главную под poker AI trainer уже с опорой на зафиксированный responsive contract.
- Blockers: нет.

### 2026-07-05 — Step 25

- Planned: переписать главную под poker AI trainer с action-first hero, poker-first навигацией и homepage feed, который связывает диагностику, обучение, статьи, турниры и новости без ухода в casino framing.
- Done: обновлена `index.html` под более целостную AI poker trainer home IA: header приведен к product/content кластерам, hero получил safety kicker и diagnostic-first CTA, добавлен явный `Статьи` home-feed блок и отдельный `Обучение` блок про decision-based learning loop; в `assets/styles.css` добавлены недостающие стили для нового hero/meta/header и сохранены mobile-breakpoint правила.
- Files changed: `index.html`, `assets/styles.css`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил более точную product-first главную с top-nav `Диагностика / Обучение / Тренажер / Статьи / Турниры / Новости`, отдельной secondary ссылкой `План` и более явной связью между verdict, контентом и следующим модулем.
- Mobile impact: mobile web сохранил компактный drawer, а новый header/hero контент подтвержден без overlap; `План` скрыт из первой строки и остается доступным через mobile menu, новые `Статьи` и hero kicker не ломают текущие брейкпоинты.
- Telegram Mini App impact: copy и IA главной теперь лучше мапятся на mini app message stack: quick level check, compact learning return и короткий content bridge без casino wording.
- macOS impact: home IA и routing labels стали ближе к будущему desktop shell с теми же продуктными разделами и логикой `diagnostic -> plan -> learning content`.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, `docs/header-nav-ru-first.md`, `docs/first-screen-poker-table.md`, `docs/week-one-content-plan.md` и `docs/site-map.md`; локально поднят `python3 -m http.server 4173`, страница проверена в in-app browser на `http://127.0.0.1:4173/index.html`: desktop title/url корректны, клик по `Как работает диагностика` переводит на `#diagnostic`, console errors/warnings отсутствуют, mobile viewport 390x844 открывает burger-nav без поломки layout.
- Remaining: следующий инкремент должен взять Step 26 и дописать сам блок `Как работает диагностика` глубже по контенту, не трогая уже выровненный home IA сверх необходимости.
- Blockers: нет.

### 2026-07-05 — Step 26

- Planned: дописать блок `Как работает диагностика` на главной так, чтобы он яснее объяснял short-session flow, live evaluation и переход от verdict к личному маршруту на desktop web, mobile web, Telegram Mini App и будущем macOS app.
- Done: расширен diagnostic section в `index.html`: добавлены short-session intro card, factual blocks о метриках и ритме сессии, обновлён 4-step flow с упором на decision spots и HUD read, а также отдельный outcome bridge в личный план; в `assets/styles.css` добавлены новые layout/card styles для diagnostic shell и сохранены responsive fallbacks без выхода за границы Step 26.
- Files changed: `index.html`, `assets/styles.css`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил более содержательный diagnostic block с двухколоночным пояснением, который лучше связывает hero, live evaluation и финальный переход в personal plan.
- Mobile impact: mobile web получил stacked diagnostic shell без горизонтального скролла; новые intro/fact/result cards складываются в один поток и остаются читаемыми на ширине 390px.
- Telegram Mini App impact: структура секции теперь лучше мапится на mini app flow как `short session -> active metric -> result -> next lesson`, даже без переноса полного desktop layout.
- macOS impact: будущий macOS app получил более чёткий текстовый контракт для onboarding/dashboard explanation рядом с table view и route handoff.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, `docs/diagnostic-hud.md`, `docs/personal-learning-map.md` и текущей home-реализации; страница проверена в in-app browser на `http://127.0.0.1:4173/index.html`: desktop title/url корректны, блок содержит новые тексты `10-20 учебных рук вместо длинной анкеты` и `После диагностики`, клик по `Посмотреть, как verdict переходит в план` переводит на `#plan`, console errors/warnings отсутствуют; mobile viewport `390x844` на `#diagnostic` показывает `scrollWidth === clientWidth`, без overlap и без horizontal scroll.
- Remaining: следующий инкремент должен взять Step 27 и наполнить блок/страницу про уровни игроков глубже по содержанию.
- Blockers: нет.

### 2026-07-05 — Step 27

- Planned: наполнить блок про уровни игроков на главной глубже по содержанию, чтобы пользователь лучше понимал разницу между verdict-уровнями и тем, какой учебный маршрут следует за каждым уровнем на desktop web, mobile web, Telegram Mini App и будущем macOS app.
- Done: расширена секция `#levels` в `index.html`: добавлены overview-card про смысл verdict, factual blocks про логику оценки и post-verdict flow, переработаны все level cards с более точными описаниями и focus-тегами, а также добавлен footer bridge в личный план; в `assets/styles.css` добавлены layout и responsive styles для нового levels-shell, overview/footer cards и compact level tags без выхода за границы Step 27.
- Files changed: `index.html`, `assets/styles.css`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил более содержательный levels-block с отдельной explanatory колонкой, углублёнными описаниями уровней 0-6 и явным мостом от verdict к personal plan без смешения с соседними editorial sections.
- Mobile impact: mobile web получил stacked levels-shell; на ширине 390px overview, factual cards, level cards и footer bridge складываются в один поток без horizontal scroll и без overlap текста/тегов.
- Telegram Mini App impact: контентный контракт уровней стал яснее для mini app surface как `verdict -> главный leak -> next lesson`, даже если полный grid уровней туда не переносится.
- macOS impact: будущий macOS app получил более чёткий текстовый контракт для level taxonomy и handoff из результата в route/history screens с теми же названиями уровней и focus areas.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, `docs/player-levels.md`, `docs/personal-learning-map.md` и текущей home-реализации; `index.html` проверен на корректный parse; страница открыта в in-app browser на `http://127.0.0.1:4173/index.html#levels`: desktop viewport `1280x720` показывает `scrollWidth === clientWidth`, 6 `level-tag` элементов и пустой console error/warn log, mobile viewport `390x844` также показывает `scrollWidth === clientWidth`, single-column `level-grid` и отсутствие overlap по границам карточек.
- Remaining: следующий инкремент должен взять Step 28 и глубже наполнить блок про AI-соперников, используя уже выровненные level/focus labels.
- Blockers: нет.

### 2026-07-05 — Step 28

- Planned: углубить блок `AI-соперники` на главной, чтобы пользователь понимал роли training opponents и system AI, их связь с leaks/уровнями и как этот слой переносится на desktop web, mobile web, Telegram Mini App и будущий macOS app.
- Done: секция `#agents` в `index.html` переработана в полноценный AI-opponents block: добавлены overview-card и explanatory points, отдельный training-opponents grid на 6 карточек с level ranges, focus tags и leak descriptions, compact system-AI panel с Skill Evaluator / Coach / Curriculum / Safety Agent, а также footer bridge обратно в диагностику; в `assets/styles.css` добавлены layout/tags/system-card styles и локальный contrast fix для заголовка секции на светлом `alt`-фоне.
- Files changed: `index.html`, `assets/styles.css`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил более содержательный AI section с разделением gameplay и orchestration layers, шестью учебными opponent cards и отдельным system AI block без смешения с casino-подачей.
- Mobile impact: mobile web получил single-column flow для overview, opponent cards, system AI и footer CTA; на ширине `390px` секция проходит без horizontal scroll и без overlap тегов/карточек.
- Telegram Mini App impact: контентный контракт стал явнее для mini app surface как `2-3 ключевых opponent profiles + compact coach/evaluator explanation`, даже если полный desktop grid туда не переносится.
- macOS impact: будущий macOS app получил более точную library/sidebar taxonomy для quick launch opponents и separate system-AI explanation layer с теми же названиями ролей.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, `docs/ai-agents.md`, `docs/ai-agent-cards.md` и текущей home-реализации; секция проверена в in-app browser на `http://127.0.0.1:4173/index.html#agents`: desktop viewport `1280x720` показывает 6 `.agent-card`, 4 `.system-agent-card`, `scrollWidth === clientWidth`, читаемый заголовок секции и пустой console error/warn log; mobile viewport `390x844` также показывает `scrollWidth === clientWidth`, single-column `.agent-grid` / `.system-agent-grid` и отсутствие overlap.
- Remaining: следующий инкремент должен взять Step 29 и написать страницу `Правила Texas Hold'em`, не расползаясь обратно в home IA.
- Blockers: нет.

### 2026-07-05 — Step 29

- Planned: написать страницу `Правила Texas Hold'em` как foundation guide для уровней First Hand - Beginner, чтобы она объясняла структуру раздачи, позиции, legal actions и шоудаун без ухода в соседние статьи про комбинации или preflop-стратегию.
- Done: обновлена `texas-holdem-rules.html` в полноценный учебный материал: расширены hero и jump navigation, добавлены секции про button/small blind/big blind и порядок хода, уточнен flow улиц, добавлен отдельный блок про showdown/split pot, усилены beginner mistake/FAQ блоки и сохранен bridge обратно в диагностику и учебную практику.
- Files changed: `texas-holdem-rules.html`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил более цельную rules-page с ясной структурой `основы -> позиции -> hand flow -> actions -> showdown -> mistakes -> FAQ`, которая лучше связывает longform reading с product CTA и не выглядит как оторванный SEO-текст.
- Mobile impact: mobile web сохранил single-column reading flow без horizontal scroll; jump links, hero CTA и новые content blocks проходят на ширине `390px` без overlap и с читаемыми длинными RU-заголовками.
- Telegram Mini App impact: content contract страницы стал яснее для будущих summary-версий в mini app: теперь легко выделяются короткие блоки `позиции`, `улицы`, `actions` и `showdown` для derivative reading surface с ссылкой на полный web-guide.
- macOS impact: будущий macOS app получил более четкий foundation-library article contract для встроенного reader view и перехода из статьи в диагностику/тренировки с теми же section labels.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, `POKER_PLATFORM_PROGRESS.md`, `docs/article-page.md` и `docs/legal-constraints.md`; страница проверена через in-app browser на `http://127.0.0.1:4173/texas-holdem-rules.html`: desktop viewport по умолчанию показывает корректные `title/url`, 7 jump links, 4 FAQ items, `#showdown` anchor navigation, `scrollWidth === clientWidth` и пустой console error/warn log; mobile viewport `390x844` показывает 2 hero CTA, 5 mistake cards, переход по CTA к `#hand-flow`, `scrollWidth === clientWidth` и отсутствие console errors/warnings.
- Remaining: следующий инкремент должен взять Step 30 и написать страницу `Комбинации покера`, используя новый rules-guide как foundation reference без дублирования этой структуры.
- Blockers: нет.

### 2026-07-05 — Step 30

- Planned: написать страницу `Комбинации покера` как foundation guide для уровней First Hand - Beginner, чтобы она объясняла порядок комбинаций, правило лучших пяти карт, kicker/split pot и частые ошибки чтения board без ухода в соседние статьи про позиции или preflop.
- Done: создана новая страница `poker-combinations.html` с hero, jump navigation, ranking-блоком комбинаций, объяснением правила пяти карт, секцией про kicker и сравнение одинаковых рук, блоком чтения board, beginner mistakes, FAQ и bridge обратно в правила/диагностику; дополнительно добавлены входы на новую страницу из `index.html` и `texas-holdem-rules.html`, а mobile-friendly ranking layout переведен в карточки вместо узкой таблицы.
- Files changed: `poker-combinations.html`, `index.html`, `texas-holdem-rules.html`, `assets/styles.css`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: desktop web получил отдельный foundation-guide по комбинациям с полноценной article-структурой и связкой `главная -> комбинации -> диагностика`, а также дополнительный CTA на новой learning page из home content feed и rules-guide.
- Mobile impact: mobile web получил single-column combinations page без horizontal scroll на ширине `390px`; ranking-блок собран карточками, hero/jump links/FAQ остаются читаемыми без overlap текста и CTA.
- Telegram Mini App impact: контентный контракт по комбинациям теперь выделен в отдельный источник, из которого можно безопасно собрать короткие summary-модули про hand ranking, kicker и split pot с переходом в полный web-guide.
- macOS impact: будущий macOS app получил еще один foundation-library article contract с теми же section labels и переходами в rules/diagnostic flow без product drift.
- Verification: выполнена сверка `POKER_PLATFORM_PLAN.md`, `docs/platform-targets.md`, текущего `POKER_PLATFORM_PROGRESS.md`, `texas-holdem-rules.html` и home content flow; in-app browser проверил flow `http://127.0.0.1:4173/index.html#articles -> Открыть комбинации -> http://127.0.0.1:4173/poker-combinations.html -> Кикер и сравнение -> #kicker`; desktop viewport `1280x720` показывает корректные `title/url`, один CTA с `href="poker-combinations.html"` на home, рабочий jump link `#kicker`, `scrollWidth === clientWidth` и пустой console error/warn log; mobile viewport `390x844` на `poker-combinations.html#ranking` показывает `scrollWidth === clientWidth`, 2 hero CTA, карточный ranking-block без overlap и пустой console error/warn log.
- Remaining: следующий инкремент должен взять Step 31 и написать страницу `Позиции за столом`, используя rules/combinations guides как foundation references без дублирования этих материалов.
- Blockers: нет.

### 2026-07-05 — Manual correction after user review

- Planned: остановить текстовый/лендинговый дрейф, убрать белые области на poker-страницах и сделать реальный игровой прототип вместо статичного preview.
- Done: `index.html` hero-table заменен на интерактивный учебный симулятор с колодой, раздачей карт, streets, ботами, pot, action buttons, live coach, hand log и простой оценкой 5/7-card hands; `assets/styles.css` получил темный poker override и game UI; `assets/site.js` получил vanilla JS game engine; CSS/JS подключены с cache-busting.
- Files changed: `index.html`, `assets/styles.css`, `assets/site.js`, `texas-holdem-rules.html`, `poker-combinations.html`, `POKER_PLATFORM_PROGRESS.md`.
- Desktop impact: первый экран теперь показывает игровой стол, ботов, карты, банк и кнопки Fold / Check-Call / Bet-Raise без белых секций вокруг poker UI.
- Mobile impact: на ширине 390px game shell идет выше hero-copy, горизонтального overflow нет, action bar доступен в первом экране или сразу у нижней границы первого экрана.
- Telegram Mini App impact: прототип использует тот же short-session contract, который позже можно перенести в Mini App как 3-5 hand challenge.
- macOS impact: game engine пока frontend-only, но формат state/render/action можно позже вынести в общий модуль для macOS thin client.
- Verification: `node --check assets/site.js`; in-app browser `http://localhost:8080/?v=...`; console errors/warnings отсутствуют; desktop 1280x820: action bar visible, no horizontal overflow; mobile 390x844: no horizontal overflow; click Bet/Raise переводит руку на flop, меняет pot/log/coach; New Hand создает новую руку.
- Remaining: следующий настоящий продуктовый шаг - вынести симулятор из hero в полноценный game screen/route, добавить устойчивую betting state machine, side pots, позиции/blinds rotation, session result screen и сохранение hand history.
- Blockers: нет.
