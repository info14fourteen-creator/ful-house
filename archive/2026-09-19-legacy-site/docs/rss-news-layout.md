# RSS / News Layout

Дата: 2026-07-05
Шаг: 23. Спроектировать RSS/news layout

## Цель

Зафиксировать contract страницы RSS/news для poker training platform. Страница должна собирать внешние покерные новости и RSS-источники как curated link hub с собственными summaries, source attribution и переходами в обучение без превращения раздела в копию media portal, gambling feed или content scraper.

Этот шаг проектирует structure, hierarchy и responsive behavior страницы RSS/news. Он не реализует production UI, не подключает реальные RSS fetch flows и не подменяет будущие шаги 61-63, 65-70.

## Product Job Of The RSS / News Page

Страница RSS/news должна делать четыре вещи одновременно:

1. быстро показывать, что нового произошло в poker ecosystem и почему это важно ученику;
2. разводить external-source coverage, tournament updates и собственные editorial explanations;
3. удерживать продукт в educational/play-money framing, а не в медийно-казиношной подаче;
4. направлять пользователя из новости в полезное действие: guide, glossary, tournament page, diagnostics или personal plan.

Страница должна ощущаться как learning-oriented news desk, а не как endless content feed.

## In-Scope Content Types

Первая версия страницы должна поддерживать четыре типа контента:

- featured news brief;
- RSS/news cards с source link и собственным summary;
- topic clusters: tournaments, strategy, industry, platform updates;
- training bridge и editorial explainer links.

Полные перепечатки статей, длинные цитаты и scraped body text не входят в scope.

## Primary Outcome Stack

### 1. News Hero

На первом экране должны быть:

- breadcrumbs;
- page label `Новости и RSS`;
- H1;
- короткий dek с разъяснением, что это curated external-source hub;
- visible informational / source-based note;
- primary CTA;
- optional compact topic chips preview.

Primary CTA допустим только в учебной логике:

- `Открыть турнирный раздел`
- `Читать обучающие статьи`
- `Пройти диагностику`

Hero не должен выглядеть как медийный таблоид или gambling-promotional splash.

### 2. Featured Brief

Сразу после hero нужен выделенный featured module:

- 1 ключевой инфоповод;
- собственный summary на 2-4 строки;
- label с темой;
- source attribution;
- optional internal explainer link;
- external source link.

Featured brief должен отвечать на вопрос: "что произошло и почему это полезно знать игроку/ученику прямо сейчас".

### 3. News Feed Layer

Основной рабочий модуль страницы:

- grid или stacked list новостных карточек;
- headline;
- source name;
- publish time/date;
- topic tag;
- short own summary;
- external source CTA;
- optional internal follow-up CTA.

Каждая карточка должна содержать только metadata и собственный краткий пересказ без копирования full article text.

### 4. Topic Cluster Rail

Рядом или ниже фида нужен controlled context layer:

- `Турниры`
- `Стратегия`
- `Индустрия`
- `Что прочитать дальше`
- `Glossary`

Этот блок нужен, чтобы news page не жила только freshness-сигналом и оставалась частью product IA.

### 5. Training Bridge

Внизу страницы обязателен продуктовый возврат:

- related guide или article;
- переход в tournament page;
- next lesson / personal plan;
- daily hand challenge.

Пользователь не должен уходить только во внешний источник и теряться.

## Recommended Page Anatomy

### Desktop Web

Рекомендуемый паттерн: editorial hub with controlled feed.

Верх:

- hero;
- topic chips;
- featured brief.

Средний слой:

- main news feed column;
- side context rail.

Нижний слой:

- grouped topic blocks;
- related internal reading;
- training CTA band.

Desktop rules:

- headline, source и summary должны читаться с первого взгляда;
- external и internal CTA должны быть визуально разведены;
- feed нельзя растягивать в шумную бесконечную ленту без editorial hierarchy;
- source attribution должен быть видимым без hover;
- нельзя использовать casino-like urgency cues или flashing highlight patterns.

### Mobile Web

Рекомендуемый паттерн: single-column summary feed.

Порядок:

1. hero;
2. topic chips;
3. featured brief;
4. stacked news cards;
5. topic clusters;
6. training bridge.

Mobile rules:

- news cards должны быть вертикальными и сканируемыми большим пальцем;
- source/date/topic meta не должны ломать сетку при длинных RU и EN названиях;
- summary length нужно ограничивать, чтобы не превращать карточки в тяжелые text walls;
- external link CTA и internal learning CTA нельзя ставить в overlapping button row;
- никаких wide tables или hover-only behaviors.

### Telegram Mini App

Mini App использует lightweight derivative:

- 1 featured brief;
- 3-5 compact news items;
- topic shortcut в tournaments или lessons;
- CTA `Открыть полную ленту на сайте`.

Mini App не должен тянуть тяжелый multi-card feed с большим количеством meta и long summaries.

### macOS App

Будущий macOS app может использовать two-pane news reader:

- sidebar с topic clusters и saved items;
- main pane с featured brief и compact feed;
- utility area для перехода в guides, plan и tournament section.

Taxonomy тем, labels и attribution pattern должны совпадать с web.

## Information Hierarchy

Порядок важности:

1. что нового и почему это важно;
2. source attribution и доверие к происхождению материала;
3. краткий собственный summary;
4. internal context and learning bridge;
5. supporting metadata.

Если места мало, сокращаются decorative chips и secondary summaries. Не жертвовать source clarity и actionability.

## Core Modules

### Required modules

- news hero;
- featured brief;
- news feed cards;
- visible source attribution pattern;
- topic clusters or context rail;
- training bridge;
- informational / educational note.

### Recommended modules

- filter chips by topic;
- `Почему это важно` inline note;
- related tournament/article cards;
- save-for-later state for future signed-in versions;
- glossary shortcuts.

## News Card Contract

Каждая news card должна поддерживать минимум:

- headline;
- source name;
- source URL;
- publish date/time;
- topic tag;
- short own summary;
- external link CTA.

Опционально:

- related internal page;
- tournament relevance label;
- level relevance label;
- note `обновлено`.

Карточка не должна содержать полный внешний лид, body copy или длинные цитаты.

## Topic Model

Базовые кластеры для первой версии:

- `Турниры`
- `Стратегия`
- `Индустрия`
- `Платформа`
- `Подкасты и видео`

Эти кластеры должны быть одинаковыми для web navigation, будущего RSS config и derivative surfaces.

## Sorting And Freshness Rules

Приоритет выдачи:

1. featured editorial pick;
2. свежесть новости;
3. полезность для обучения;
4. близость к tournament/article surfaces.

Не строить сортировку вокруг scandal/hype wording или money-first attraction.

## Copy And Tone Rules

- писать как curator и coach, а не как media outlet с кликбейтом;
- кратко объяснять контекст и полезность;
- не обещать заработок, инсайды или value-from-news;
- при внешних материалах всегда добавлять свой explanatory angle.

Допустимые micro-labels:

- `Краткий разбор`
- `Источник`
- `Почему это важно`
- `Перейти к гиду`

Недопустимые формулировки:

- `Срочно заходи в турнир`
- `Не упусти профит`
- `Шокирующая новость для игроков`

## Source Attribution And Copyright Guardrails

- каждая новость должна явно показывать источник;
- можно использовать headline-level reference и собственный короткий summary;
- full article text, bulk quotes и копирование нескольких абзацев не допускаются;
- при наличии спорных формулировок предпочтителен neutral rewrite;
- source link должен вести на оригинал, а не на rehosted copy.

## Responsive And Interaction Rules

- chips и filters должны переноситься без overlap;
- длинные source names и mixed-language headlines должны корректно переноситься;
- news cards должны иметь clear tap targets;
- external link icon/label должен быть понятным и не конфликтовать с internal CTA;
- на mobile и Mini App приоритет у featured brief и 3-5 верхних карточек, остальной feed можно скрывать за `Показать еще`.

## Relationship To Adjacent Pages

- tournament page отвечает за calendar и format education;
- article page отвечает за longform guides и explainers;
- RSS/news page отвечает за freshness, source aggregation и routing.

Если инфоповод требует глубокой трактовки, RSS/news карточка должна вести в собственную статью, а не пытаться заменить ее.

## Surface-Specific Acceptance Notes

### Desktop web

- visible hierarchy между featured brief, feed и context rail;
- source attribution и CTA различимы без hover;
- feed не выглядит как generic media portal.

### Mobile web

- нет horizontal scroll;
- нет overlap headline/meta/buttons;
- summaries остаются короткими и читаемыми.

### Telegram Mini App

- только compact subset;
- акцент на быстрый возврат в web-guides и tournament page;
- без heavy multi-column behavior.

### macOS app

- same taxonomy and labels;
- возможна saved-reading model в будущей версии;
- reading shell должен оставаться утилитарным, а не browser clone.

## Out Of Scope

Этот шаг не делает:

- live RSS ingestion;
- backend caching;
- user personalization feed;
- own article RSS output;
- production implementation карточек и фильтров.

Эти части переходят в будущие шаги 61-67 и более позднюю инженерную стадию.
