# Responsive States Audit

Дата: 2026-07-05
Шаг: 24. Проверить desktop и mobile responsive состояния

## Цель

Свести в один contract responsive-состояния для уже спроектированных экранов блока 2, чтобы следующие UI-итерации не расходились между desktop web и mobile web и заранее учитывали производные поверхности Telegram Mini App и будущего macOS app.

Этот шаг не внедряет production UI и не меняет текущую light B2B-верстку. Он проверяет, что design-specs шагов 15-23 согласованы между собой по breakpoint logic, priority stack и anti-overlap rules.

## Проверенные источники

- `docs/platform-targets.md`
- `docs/header-nav-ru-first.md`
- `docs/first-screen-poker-table.md`
- `docs/ai-agent-cards.md`
- `docs/diagnostic-hud.md`
- `docs/level-result-screen.md`
- `docs/personal-learning-map.md`
- `docs/article-page.md`
- `docs/tournament-page.md`
- `docs/rss-news-layout.md`
- текущие `index.html` и `assets/styles.css` как reference точки миграции

## Responsive Baseline

### Recommended breakpoints

- `Desktop XL`: 1440px+ для широкого стола, двухколоночных аналитических экранов и богатых content rails.
- `Desktop / Laptop`: 1024-1439px для основного MVP layout.
- `Tablet / Large Mobile`: 768-1023px как переходный stacked режим без desktop hover-dependencies.
- `Mobile`: 480-767px как основной вертикальный runtime для mobile web.
- `Compact Mobile`: 320-479px как stress-case для длинных RU labels, chips и stacked CTAs.

### Global layout rules

1. Все primary CTAs должны уходить в vertical stacking раньше, чем начнется overlap с длинными RU подписями.
2. Ни один ключевой экран не должен зависеть от hover для чтения state, метрик, source attribution или navigation.
3. Desktop split layouts обязаны иметь заранее определенный stacked fallback на 1023px и ниже.
4. Chips, tags и meta rows должны переноситься в 2 строки максимум; дальше допускается упрощение secondary metadata.
5. Любые card grids на mobile превращаются в single-column stack.
6. Широкие таблицы не допускаются на mobile; calendar, HUD и result blocks проектируются как cards/lists.

## Cross-Screen Audit

### 1. Header / Navigation

Desktop состояние из `docs/header-nav-ru-first.md` согласовано:

- top-level nav остается видимым;
- primary CTA `Определить уровень` держится отдельно от secondary links;
- language/system actions не конкурируют с главным продуктовым действием.

Mobile состояние согласовано:

- compact header + drawer вместо двухуровневого меню;
- короткие labels без зависания на одной строке;
- thumb-friendly tap targets;
- отсутствует зависимость от hover и узких inline action rows.

### 2. First Screen / Poker Table Hero

Desktop состояние из `docs/first-screen-poker-table.md` согласовано:

- `content left / table right`;
- крупный diagnostic CTA выше fold;
- trust/safety labels остаются рядом с message hierarchy, а не теряются под иллюстрацией.

Mobile состояние согласовано:

- вертикальный порядок: message -> CTA -> compact table preview -> supporting proof;
- hero copy ограничен по длине;
- table preview не должен выталкивать CTA ниже первого экрана;
- long labels не должны наслаиваться на felt/table art.

### 3. AI Agent Cards

Desktop состояние из `docs/ai-agent-cards.md` согласовано:

- grid карточек для training opponents;
- более компактный блок system AI;
- role tags и difficulty labels читаются без hover.

Mobile состояние согласовано:

- один столбец;
- actions и tags не живут в одной плотной строке;
- длинные agent names и descriptors допускают перенос;
- карточки не требуют side-by-side сравнения.

### 4. Diagnostic HUD

Desktop состояние из `docs/diagnostic-hud.md` согласовано:

- analytical rail остается рядом со столом;
- board, pot и action controls не перекрываются;
- промежуточные сигналы короче финальной аналитики result screen.

Mobile состояние согласовано:

- top progress strip;
- active lens chips;
- short running read;
- secondary metrics скрываются или сворачиваются;
- no overlap между HUD и action controls.

### 5. Level Result Screen

Desktop состояние из `docs/level-result-screen.md` согласовано:

- two-column verdict + action rail;
- leaks/strengths/next-route разведены по hierarchy;
- screen не скатывается в solver-dashboard.

Mobile состояние согласовано:

- single-column stack;
- verdict и 2-3 ключевые ошибки идут раньше вторичных breakdowns;
- CTA не уходит ниже длинных explanatory sections.

### 6. Personal Learning Map

Desktop состояние из `docs/personal-learning-map.md` согласовано:

- dashboard pattern;
- next action виден сразу;
- module map и route summary отделены от editorial blocks.

Mobile состояние согласовано:

- active module first;
- stacked milestones;
- статусы и chips не должны ломать ритм;
- все progress/CTA блоки доступны без hover.

### 7. Article Page

Desktop состояние из `docs/article-page.md` согласовано:

- reading column доминирует;
- utility rail sticky, но не перекрывает body;
- training bridge идет после чтения, а не спорит с ним.

Mobile состояние согласовано:

- TOC сворачивается;
- callouts и media slots обязаны помещаться без horizontal scroll;
- длинные RU headings, tags и meta chips не overlap.

### 8. Tournament Page

Desktop состояние из `docs/tournament-page.md` согласовано:

- hero + featured context + calendar + education rail;
- calendar остается scan-friendly, без full-width data tables;
- external source links отделены от internal learning actions.

Mobile состояние согласовано:

- compact filter chips;
- single-column tournament cards;
- meta stack переносится безопасно;
- wide tables запрещены.

### 9. RSS / News Layout

Desktop состояние из `docs/rss-news-layout.md` согласовано:

- featured brief + feed + context rail;
- source attribution видим без hover;
- feed не превращается в бесконечный шум.

Mobile состояние согласовано:

- summary-first stacked cards;
- source/date/topic мета не должна ломать карточку;
- external/internal CTA разведены по строкам при нехватке ширины.

## Shared Mobile Risk List

Перед будущей реализацией нужно отдельно держать под контролем:

- длинные RU-заголовки и labels в hero, cards, result verdicts и tournament series names;
- одновременное присутствие chips, tags, source meta и CTA в одной карточке;
- sticky-поведение header и utility-rail, чтобы оно не съедало полезную высоту на mobile;
- безопасные отступы вокруг action bars для poker table и diagnostic HUD;
- отсутствие горизонтального скролла в article callouts, tournament/calendar items и news cards.

## Telegram Mini App Implications

- Все desktop/mobile экраны уже имеют lightweight derivative, а не пытаются переноситься 1:1.
- Mini App должен наследовать только summary-first модули: quick diagnostic, short result, one active lesson, compact news/tournament highlights.
- Heavy rails, longform reading и multi-panel analytics остаются на web/macOS surfaces.

## macOS App Implications

- Все desktop-модули уже описаны как совместимые с sidebar + main-pane shell.
- macOS не требует отдельной visual language; ему нужен более утилитарный chrome поверх той же IA и token-system.
- Текущий responsive audit снижает риск product drift между full web desktop и будущим thin-client app.

## Migration Note For Current Site

Текущие `index.html` и `assets/styles.css` все еще описывают светлый B2B-сайт. Для будущего UI-переезда это означает:

- существующие breakpoints нельзя переносить автоматически без ревизии;
- новая poker IA требует более раннего stacking поведения для CTA, chips и utility panels;
- responsive contract уже определен на уровне продукта и должен направлять последующие HTML/CSS шаги.

## Acceptance Check For Next UI Steps

Следующие визуальные/кодовые шаги можно считать корректными только если:

1. один и тот же экран читается без overlap на 1440px, 1024px, 768px, 390px и 320px;
2. primary CTA остается видимым в первом экране или первом логическом блоке;
3. навигация, cards, HUD, result и content screens не требуют hover;
4. нет horizontal scroll в основных пользовательских сценариях mobile web;
5. Telegram Mini App и macOS используют те же labels и route logic, но не копируют web layout буквально.

## Result

Responsive states для design-specs шагов 15-23 согласованы. Desktop и mobile contracts не конфликтуют между собой, а производные требования для Telegram Mini App и macOS app уже зафиксированы как controlled adaptations, а не отдельные продукты.
