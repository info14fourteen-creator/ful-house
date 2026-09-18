# Personal Learning Map

Дата: 2026-07-05
Шаг: 20. Спроектировать личную карту обучения

## Цель

Зафиксировать контракт personal learning map для poker training platform. Экран должен превращать результат диагностики в понятный маршрут роста: что изучать сейчас, какие ошибки исправлять дальше и как двигаться между уроками, тренировками и повторной диагностикой.

Этот шаг проектирует структуру, логику модулей и responsive behavior personal plan. Он не внедряет production UI, не подменяет будущие шаги 52-59 про templates/quizzes/progress logic и не дублирует result screen.

## Product Job Of The Learning Map

Личная карта обучения должна за один просмотр отвечать на пять вопросов:

1. Какой у меня текущий уровень и ближайшая цель.
2. Какие ошибки сейчас приоритетнее всего исправлять.
3. Какой урок пройти следующим.
4. Какая тренировка закрепит этот урок.
5. Когда имеет смысл вернуться к повторной диагностике.

Карта должна ощущаться как рабочий учебный маршрут, а не как gamified battle pass.

## Core Outcome Stack

### 1. Route Header

В верхней зоне должны быть:

- текущий level label;
- короткая route summary;
- `Следующий лучший шаг`;
- progress cue вроде `2 из 5 модулей в работе`.

Пример summary:

- `Сейчас рост даст дисциплина на префлопе и более уверенный фолд против давления.`

### 2. Priority Leaks Rail

Карта должна явно показывать 2-3 ключевые утечки, пришедшие из диагностики:

- название ошибки;
- короткое объяснение;
- привязанный модуль или drill.

Это создает мост между result screen и ежедневным обучением.

### 3. Route Modules

Основная структура карты: последовательность учебных блоков.

Минимальный набор типов:

- `Урок`
- `Мини-тест`
- `Тренировочные раздачи`
- `Разбор AI`
- `Повторная проверка`

Каждый модуль должен показывать:

- тип;
- короткое название;
- skill tags;
- ожидаемый результат;
- статус.

### 4. Next Action Panel

Отдельный action block обязателен:

- один primary CTA `Начать следующий урок`;
- 1-2 secondary actions;
- короткая причина, почему именно этот шаг следующий.

Пользователь не должен думать, с какого блока начинать.

### 5. Progress Memory

Карта должна хранить ощущение прогресса без leaderboards и money framing.

Разрешенные сигналы:

- completed / in progress / locked;
- streak-like signal только как учебная регулярность;
- `последняя диагностическая сессия`;
- `следующая рекомендуемая проверка`.

Не использовать:

- рейтинги;
- обещания ROI;
- casino-like levels `VIP`, `High Roller`.

## Recommended Map Anatomy

### Desktop Web

Рекомендуемый паттерн: split dashboard.

Левая колонка:

- route header;
- next action panel;
- priority leaks rail.

Правая колонка:

- модульная карта обучения;
- optional recent session note;
- quick link в result screen или hand review.

Desktop может использовать vertical module path или dense card rail, но пользователь должен видеть следующий actionable шаг без прокрутки всей карты.

### Mobile Web

Рекомендуемый паттерн: single-column stacked route.

Порядок:

1. route header;
2. next action panel;
3. priority leaks;
4. active module;
5. remaining modules;
6. optional completed history accordion.

Mobile rules:

- primary CTA всегда выше первого длинного списка;
- module cards не должны ломать tags в многослойный overlap;
- статусы должны читаться без hover;
- никакие sticky элементы не должны закрывать CTA, summary или status chips.

### Telegram Mini App

Mini App берет сокращенную learning map модель:

- текущий уровень;
- один активный модуль;
- один daily hand challenge;
- кнопка открыть полный план на web.

Mini App не должен показывать длинную карту из 6-8 блоков. Его задача: удерживать короткий ритм и возвращать пользователя в основной продукт.

### macOS App

Будущий macOS app может использовать более утилитарную desktop-карту:

- sidebar с модулями;
- main pane с активным уроком;
- persistent recent sessions/history rail;
- quick restart последнего drill.

Названия модулей, статусов и skill tags должны совпадать с web.

## Module System

### Required Statuses

- `Рекомендуем сейчас`
- `В работе`
- `Готово`
- `Скоро`
- `Повторить позже`

### Required Module Types

1. foundation lesson;
2. decision drill;
3. quiz check;
4. AI review;
5. re-diagnostic checkpoint.

### Recommended Module Fields

- module id;
- title;
- type;
- target skill;
- estimated session length;
- recommended level range;
- unlock condition;
- CTA label.

Это нужно для будущих шагов 52-59 и чтобы plan surface не расходился между четырьмя платформами.

## Information Hierarchy

Порядок важности на экране:

1. следующий лучший шаг;
2. приоритетные ошибки;
3. активный модуль;
4. путь следующих 2-3 модулей;
5. completed history;
6. deeper analytics.

Если экран тесный, completed history и secondary metadata скрываются первыми. Пользователь всегда должен быстро понимать, что делать сейчас.

## Routing Logic Boundaries

Learning map должен использовать только понятные учебные причины для маршрута:

- слабая дисциплина префлопа;
- ошибки вне позиции;
- переизбыток коллов;
- плохая работа с давлением;
- пропуск value spots.

Пока не стоит закладывать:

- сложные adaptive branches на десятки вариантов;
- solver-like path trees;
- social comparison;
- real-money progression.

Первая версия должна быть управляемой и объяснимой.

## Cross-Surface Behavior Rules

### Desktop Web

- поддерживать развернутую карту пути и быстрые переходы между модулями;
- держать result-to-plan transition в 1 клик;
- не смешивать editorial content с учебным маршрутом в основной колонке.

### Mobile Web

- поддерживать короткие учебные сессии;
- давать возможность быстро вернуться к активному модулю;
- не перегружать экран completed items по умолчанию.

### Telegram Mini App

- показывать только active-now subset;
- сокращать descriptions до 1-2 строк;
- использовать карту как reminder/return surface, а не full dashboard.

### macOS App

- усиливать utility pattern: history, recent drills, quick relaunch;
- сохранять ту же route logic и labels, что на web;
- не строить отдельную desktop-only taxonomy.

## Tone Of Voice

Тон карты обучения:

- спокойный;
- направляющий;
- прикладной;
- без стыда;
- без hype.

Хорошие формулировки:

- `Начните с короткого урока по входу в банк с ранних позиций.`
- `После этого закрепите навык в 5 тренировочных спотах.`
- `К повторной диагностике лучше вернуться после двух модулей.`

Плохие формулировки:

- `Прокачайтесь до профи за вечер`
- `Разнесете поле после этих уроков`
- `Ваш путь к стабильному заработку`

## CTA Contract

Primary CTA:

- `Начать следующий урок`

Secondary CTAs:

- `Пройти тренировку`
- `Открыть прошлый результат`
- `Повторить диагностику позже`

Запрещенные CTA:

- `Играть на деньги`
- `Поставить на уровень`
- `Открыть прибыльные столы`

## Dependencies And Handoffs

Learning map опирается на:

- Step 4: уровни игроков;
- Step 5: диагностические метрики;
- Step 6: taxonomy ошибок;
- Step 15: navigation contract;
- Step 18: live HUD;
- Step 19: level result screen.

Learning map передает требования в:

- Step 52: шаблон разбора одной раздачи;
- Step 53: шаблон персонального плана;
- Step 54: модуль `следующий лучший урок`;
- Step 55: прогресс по модулям.

## Out Of Scope

Этот шаг не описывает:

- точные scoring formulas;
- hand engine implementation;
- backend sync;
- финальную визуальную реализацию карточек и графов;
- авторизацию и cloud history.

## Acceptance Notes For The Next UI Step

Step 20 можно считать закрытым, если:

- из result screen есть ясный переход в personal plan;
- карта показывает current level, top leaks, next module и дальнейший путь;
- на mobile нет зависимости от hover и нет overlap длинных labels/CTA;
- mini app и macOS трактуются как адаптации общей route logic, а не отдельные продукты;
- copy остается educational/play-money only.
