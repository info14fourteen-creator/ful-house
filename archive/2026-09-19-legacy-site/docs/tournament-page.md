# Tournament Page

Дата: 2026-07-05
Шаг: 22. Спроектировать страницу турниров

## Цель

Зафиксировать contract страницы турниров для poker training platform. Страница должна объяснять турнирные форматы, показывать curated calendar и направлять пользователя в образовательные материалы без превращения раздела в gambling lobby, betting board или копию новостной ленты.

Этот шаг проектирует structure, hierarchy и responsive behavior страницы турниров. Он не реализует production UI, не импортирует live calendar и не подменяет будущие шаги 23, 35, 61-64.

## Product Job Of The Tournament Page

Страница турниров должна делать четыре вещи одновременно:

1. помогать пользователю быстро понять, какие турниры и форматы ему сейчас релевантны;
2. объяснять difference между MTT, satellite, bounty, turbo, freezeout и deepstack;
3. связывать турнирный календарь с обучением, диагностикой и личным планом;
4. давать only-source/linked coverage внешних серий и площадок без копипаста чужих материалов.

Страница должна ощущаться как training-oriented tournament hub, а не как афиша для игры на деньги.

## In-Scope Content Types

Первая версия страницы должна поддерживать четыре типа контента:

- featured tournament series overview;
- upcoming calendar cards with source links;
- format explainer modules;
- training bridge into articles, glossary, diagnostics и personal plan.

Новости о сериях могут появляться здесь только как короткий context layer. Полноценный RSS/news feed остается на отдельной странице.

## Primary Outcome Stack

### 1. Tournament Hero

На первом экране должны быть:

- breadcrumbs;
- page label `Турниры`;
- H1;
- короткий dek с educational framing;
- visible play-money / informational note;
- primary CTA;
- optional compact filters preview.

Primary CTA допустим только в учебной логике:

- `Понять форматы турниров`
- `Открыть MTT-гайд`
- `Пройти диагностику`

Hero не должен выглядеть как sportsbook calendar или casino lobby splash.

### 2. Featured Series And Context

Сразу после hero нужен controlled context block:

- 1 featured series or season overview;
- 2-3 facts, почему это важно знать игроку;
- short explainer, для кого формат релевантен;
- link на собственный guide или explainer.

Этот блок должен давать orientation, а не просто перечислять бренды WSOP/WPT/EPT.

### 3. Tournament Calendar Layer

Основной рабочий модуль страницы:

- карточки или rows ближайших турниров/серий;
- source label;
- date window;
- format tags;
- level relevance;
- short own summary;
- external source link.

Каждая карточка должна отвечать на вопрос: "почему это полезно знать ученику платформы".

### 4. Format Education Rail

Рядом или ниже календаря нужен блок обучения:

- MTT basics;
- satellite explained;
- bounty explained;
- turbo vs deepstack;
- stack pressure / ICM primer;
- glossary shortcuts.

Tournament page не должна зависеть только от freshness. Evergreen format education обязателен.

### 5. Training Bridge

Внизу страницы нужен перевод в действие:

- `Тренировать турнирные решения`;
- `Открыть статью про календарь`;
- `Перейти в личный план`;
- `Daily hand challenge`.

Пользователь должен уходить не только во внешний источник, но и обратно в продукт.

## Recommended Page Anatomy

### Desktop Web

Рекомендуемый паттерн: hero + two-layer hub.

Верх:

- hero;
- compact filter row;
- featured series module.

Средний слой:

- main calendar column;
- side education rail.

Нижний слой:

- format explainer cards;
- related articles;
- training CTA band.

Desktop rules:

- calendar должен оставаться scan-friendly, без перегруженных таблиц на всю ширину;
- source links и tags должны быть видимыми без hover;
- educational rail не должен превращаться в вторую новостную ленту;
- нельзя строить интерфейс как poker room lobby с buy-in emphasis.

### Mobile Web

Рекомендуемый паттерн: single-column tournament stack.

Порядок:

1. hero;
2. compact filters chips;
3. featured series;
4. calendar cards;
5. format explainers;
6. related guide;
7. training bridge.

Mobile rules:

- filters должны складываться в horizontal chips row без overlap и без критической зависимости от точного попадания;
- date/source/format meta не должны ломать карточки при длинных названиях серий;
- external link CTA должен оставаться отделенным от internal learning CTA;
- никаких широких таблиц, требующих horizontal scroll.

### Telegram Mini App

Mini App использует облегченный derivative:

- ближайший tournament highlight;
- 1-2 quick format cards;
- daily challenge, связанный с tournament pressure;
- CTA `Смотреть полный календарь на сайте`.

Mini App не должен везти full calendar wall. Только short-return layer.

### macOS App

Будущий macOS app может использовать two-pane shell:

- sidebar filters and series list;
- main pane with event details and explainer modules;
- lower utility area for notes/history.

Названия форматов, labels и training bridges должны совпадать с web-taxonomy.

## Information Hierarchy

Порядок важности:

1. что это за турнирный раздел и зачем он пользователю;
2. ближайшие или featured события;
3. понимание форматов;
4. переход в обучение и тренировки;
5. supporting metadata и внешние ссылки.

Если места мало, secondary decorations и лишние series summaries сокращаются первыми. Не жертвовать clarity календаря и format education.

## Core Modules

### Required modules

- tournament hero;
- featured series/context block;
- calendar list or card grid;
- format explainer module;
- source attribution pattern;
- training bridge;
- responsible play / informational note.

### Recommended modules

- filters by format and skill level;
- `Что смотреть новичку` helper block;
- glossary shortcuts;
- related article cards;
- editorial note `Почему это важно сейчас`.

## Calendar Data Contract

Каждый calendar item должен поддерживать минимум:

- title;
- series name;
- date or date range;
- format type;
- level relevance;
- short own summary;
- source name;
- source URL.

Опционально:

- region/timezone note;
- stage tag `upcoming`, `running`, `results`;
- explainer link.

Страница не должна зависеть от buy-in, prize-pool promises или financial temptation copy.

## Filters And Sorting

Первая версия может проектироваться с простыми фильтрами:

- `Все`
- `MTT`
- `Satellite`
- `Bounty`
- `Turbo`
- `Deepstack`

И skill filters:

- `Новичку`
- `Уже играл`
- `Продвинутым`

Sorting priority:

1. featured editorial pick;
2. актуальность по дате;
3. relevance к учебным форматам.

Не сортировать вокруг money-first signals.

## Copy And Tone Rules

- писать как guide/editorial assistant, а не как tournament promoter;
- объяснять формат, риски ошибки и контекст выбора;
- подчеркивать informational/use-for-study nature внешних серий;
- избегать hype wording и доходных обещаний.

Допустимые micro-labels:

- `Формат`
- `Информационный обзор`
- `Что изучить перед MTT`
- `Подходит для Intermediate`

Недопустимые формулировки:

- `Зарегистрируйся и выигрывай`
- `Лучшие турниры для заработка`
- `Гарантированный ROI`
- `Играй на деньги`

## Relation To Other Surfaces

### Articles

Tournament page может ссылаться на explainers, но не заменяет longform article page. Если теме нужен глубокий разбор, пользователь должен уйти в статью.

### News

Tournament page использует news only as context snippets and source links. Полная лента новостей остается на отдельной RSS/news surface.

### Diagnostic And Plan

Для пользователей с leak в push/fold, ICM или short-stack decisions страница должна иметь bridge в диагностику, турнирные сценарии и personal plan.

## Safety And Compliance Guardrails

- only educational/play-money framing;
- visible 18+ and responsible play reference в footer или rail;
- никакого депозита, кассы, регистрации в room или betting CTA;
- внешние турниры показываются как informational references с линком на источник;
- не копировать описания турниров целиком из внешних источников.

## Responsive Acceptance Notes

### Desktop

- calendar cards/rows читаются без потери source/date/format метаданных;
- featured block и education rail не конфликтуют за основной фокус;
- training CTA заметен без ощущения рекламы.

### Mobile

- filters, meta chips и CTA не overlap даже при длинных RU-заголовках;
- карты серий и событий читаются без horizontal scroll;
- internal и external actions явно различимы.

### Telegram Mini App

- только один приоритетный tournament highlight за экран;
- короткие summaries;
- clear return CTA в web.

### macOS

- возможна двухпанельная модель без новой IA;
- tournament section остается частью общей learning system.

## Definition Of Done For This Step

Шаг 22 считается закрытым, если команда понимает:

- как должна работать отдельная tournament page без смешения с news/article surfaces;
- какие обязательные модули нужны для desktop web и mobile web;
- какой облегченный contract нужен для Telegram Mini App;
- как будущий macOS app может переиспользовать ту же IA и taxonomy;
- какие safety/copyright boundaries действуют для внешних турнирных данных.
