# Article Page

Дата: 2026-07-05
Шаг: 21. Спроектировать страницу статьи

## Цель

Зафиксировать editorial article page contract для poker training platform. Страница должна поддерживать собственные SEO-материалы сайта: правила, обучающие гайды, разборы ошибок, style explainers и tournament education articles.

Этот шаг проектирует структуру, hierarchy и responsive behavior страницы статьи. Он не внедряет production UI, не пишет сами статьи и не подменяет будущие шаги 22-23 про tournaments и RSS/news layout.

## Product Job Of The Article Page

Страница статьи должна делать четыре вещи одновременно:

1. быстро объяснять тему и пользу материала;
2. удерживать фокус на обучении и разборе решений, а не на gambling framing;
3. подсказывать следующий полезный шаг: диагностика, тренировка, related guide;
4. связывать editorial content с остальными продуктовым surfaces: планом, тренажером, glossary, турнирами и новостями.

Статья должна ощущаться как часть training platform, а не как оторванный blog engine.

## Article Types In Scope

Первая версия должна поддерживать как минимум четыре editorial типа:

- foundation guide: правила, комбинации, позиции, preflop basics;
- mistake explainer: call discipline, overcalling, bad bluff spots, passive lines;
- style/profile article: tight, loose, aggressive, passive;
- tournament education article: как читать календарь, форматы MTT, satellite, bounty.

Все типы используют одну layout-system, но могут менять акценты в hero meta, callout blocks и next-step CTA.

## Core Outcome Stack

### 1. Article Hero

В первом экране должны быть:

- breadcrumbs;
- topic tag;
- H1;
- короткий dek на 2-3 строки;
- meta row: дата, reading time, level relevance;
- visible educational framing;
- primary next-step CTA.

Primary CTA должен зависеть от типа статьи:

- `Пройти диагностику`
- `Открыть тренажер`
- `Перейти к следующему уроку`

Hero не должен выглядеть как media portal splash с доминирующим баннером. Текст и действие важнее декоративной картинки.

### 2. Reading Column

Основная колонка статьи должна быть построена вокруг удобного deep reading:

- комфортная measure;
- clear type rhythm;
- section headings;
- bullet lists там, где это реально помогает;
- inline glossary links;
- table/image/callout slots для poker education cases.

Контент должен читатьcя как guide from a coach, а не как generic SEO wall.

### 3. Utility Rail

Рядом с текстом нужен utility layer, особенно на desktop:

- progress-aware CTA;
- sticky table of contents;
- related concept chips;
- quick jump в glossary;
- responsible play / play-money micro-label;
- optional mini-card `Что тренировать после статьи`.

Этот rail должен усиливать reading flow, а не бороться с ним.

### 4. Training Bridge

Ниже основной статьи обязателен блок, который переводит чтение в действие:

- следующий урок;
- 3-5 тренировочных раздач;
- связанная ошибка из taxonomy;
- возврат в personal plan или diagnostic flow.

Статья не должна заканчиваться тупиком.

### 5. Related Content Block

Нужен controlled recommendation layer:

- 2-3 related articles;
- 1 glossary link group;
- optional tournament/news context link, если это помогает теме.

Не превращать нижний блок в бесконечную editorial ленту.

## Recommended Page Anatomy

### Desktop Web

Рекомендуемый паттерн: three-zone reading shell.

Левая зона:

- breadcrumbs;
- topic system;
- optional section jump or small meta stack.

Центральная зона:

- article hero;
- reading column;
- callouts, charts, examples;
- training bridge.

Правая зона:

- sticky table of contents;
- next-step CTA card;
- related concepts;
- responsible play micro-note.

Desktop rules:

- reading column должна оставаться главным визуальным потоком;
- sticky rail не должен перекрывать article body;
- рядом можно держать training CTA, но не solver-like dashboards.

### Mobile Web

Рекомендуемый паттерн: single-column reading stack.

Порядок:

1. breadcrumbs;
2. topic tag;
3. H1 и dek;
4. meta row;
5. primary CTA;
6. optional jump menu;
7. article body;
8. training bridge;
9. related content.

Mobile rules:

- TOC превращается в compact accordion или chips row;
- CTA нельзя прятать ниже первого длинного абзаца;
- callouts, tables и quote blocks должны помещаться без горизонтального скролла;
- tags, meta chips и CTA не должны overlap даже при длинных RU-заголовках.

### Telegram Mini App

Mini App не должен открывать full longform article page как есть. Для него нужен short-form derivative:

- короткий summary;
- 3 key takeaways;
- один CTA в урок или challenge;
- кнопка `Читать полностью на сайте`.

Mini App может использовать articles как return/education surface, но не как primary long-read environment.

### macOS App

Будущий macOS app может использовать article reader как библиотечный режим:

- sidebar с разделами;
- main reading pane;
- related training card справа или снизу;
- быстрый возврат в plan/history.

Названия разделов, tags и CTA должны совпадать с web, чтобы библиотека не раздваивалась по IA.

## Information Hierarchy

Порядок важности на статье:

1. тема и обещанная польза;
2. образовательный контекст и уровень читателя;
3. основной текст;
4. actionable training bridge;
5. related reading;
6. supporting metadata.

Если места мало, secondary metadata и extra related links сокращаются первыми. Не жертвовать H1/dek/CTA ради визуального шума.

## Content Modules

### Required modules

- article hero;
- reading body;
- at least one coach-style callout;
- training bridge;
- related articles;
- responsible play micro-note;
- source attribution block, если статья связана с новостью, турниром или внешним поводом.

### Recommended modules

- sticky table of contents;
- skill tags;
- glossary inline links;
- beginner note / intermediate note blocks;
- hand example block;
- FAQ mini-section для evergreen guides.

## Tone And Copy Rules

- объяснять решения, а не обещать результат в деньгах;
- писать как учебный разбор, а не как sensational poker media;
- избегать casino/betting language;
- при внешних инфоповодах давать собственный explanatory angle вместо перепечатки.

Допустимые micro-labels:

- `Учебный материал`
- `Для уровня Beginner - Intermediate`
- `Разбор ошибки`
- `Tournament guide`

Недопустимые формулировки:

- `Как заработать на покере`
- `Гарантированный профит`
- `Секрет победы за столом`

## Media And Layout Rules

- hero image optional, not required;
- если изображение используется, оно должно поддерживать тему статьи, а не доминировать над reading start;
- таблицы диапазонов, списки комбинаций и hand examples должны иметь compact dark treatment;
- рекламных баннеров, агрессивных popups и inline distractions быть не должно.

## SEO And Metadata Notes

- H1 один на страницу;
- title и description должны следовать safety-рамке из `docs/seo-core.md` и `docs/legal-constraints.md`;
- article template должен поддерживать evergreen guides и timely explainers без копирования чужих текстов;
- internal links должны связывать статью с diagnostic, learning map, glossary и related guides.

## Cross-Surface Behavior Rules

### Desktop Web

- longform reading + utility rail;
- clear bridges в диагностику и тренировки;
- no content sprawl into tournament/news feeds inside the main reading column.

### Mobile Web

- summary-first intro;
- no horizontal overflow in tables/callouts;
- CTA and reading navigation remain reachable without overlap.

### Telegram Mini App

- article content only as compact summary surface;
- deep reading should hand off to web;
- return action prioritized over endless scroll.

### macOS App

- library-like reading mode;
- easy switch between article and training surfaces;
- shared tags and module names with web.

## Boundaries For Adjacent Steps

Этот шаг не должен:

- проектировать tournaments page целиком;
- проектировать RSS/news hub layout;
- писать сами статьи шагов 29-35;
- вводить final article schema implementation.

Он должен только задать reusable article-page contract для будущих editorial страниц.

## Definition Of Done

Шаг 21 считается закрытым, если команда понимает:

- как должна выглядеть и работать одна статья в рамках poker training platform;
- как статья соединяется с диагностикой, обучением, glossary, news и tournaments;
- какие ограничения обязательны для desktop web, mobile web, Telegram Mini App и будущего macOS app;
- как сохранить educational/play-money framing внутри editorial template.
