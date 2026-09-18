# AI Agent Cards

Дата: 2026-07-05
Шаг: 17. Спроектировать карточки AI-агентов

## Цель

Зафиксировать контракт карточек AI-агентов для poker training platform. Карточки должны быстро объяснять роль соперника или системного агента, направлять пользователя в подходящий тренировочный сценарий и оставаться согласованными на desktop web, mobile web, Telegram Mini App и будущем macOS app.

Этот шаг проектирует только card system для AI-агентов. Он не подменяет Step 7 с описанием ролей агентов и не забирает работу у будущих шагов про HUD, result screen, curriculum map или hand trainer.

## Card Job

Карточка AI-агента должна за несколько секунд отвечать на четыре вопроса:

1. Кто это: игровой бот или системный AI-агент.
2. Чему он учит: какой leak, навык или pressure spot тренируется.
3. Для кого он подходит: уровень игрока и режим использования.
4. Что делать дальше: начать тренировку, посмотреть разбор или открыть описание.

## Agent Groups

Нужно разделить карточки на две группы, чтобы не смешивать gameplay и orchestration.

### Training Opponents

- Beginner Bot
- Calling Station Bot
- Tight Regular Bot
- Aggressor Bot
- GTO-ish Bot
- Tournament Bot

Это основные карточки для user-facing sections на главной, в тренажере и в плане обучения.

### System AI

- Skill Evaluator
- Coach Agent
- Curriculum Agent
- Safety Agent

Эти карточки нужны как supporting layer в explainers, result screens и product pages. Их не стоит показывать как равноправные "соперники" за столом.

### Engine Exclusion

Game Engine не должен оформляться как глянцевая AI-card рядом с ботами. Его лучше показывать как infrastructure badge или explanatory row `Правила, легальные действия, pot logic`. Это удерживает продукт от ложного впечатления, что LLM управляет механикой покера.

## Recommended Placement

### Desktop web

- отдельная секция под первым экраном;
- 3-column grid для Training Opponents;
- 2-column compact grid или rail для System AI;
- cards не должны попадать в первый viewport вместо hero CTA.

### Mobile web

- vertical stack или horizontal snap carousel только для Training Opponents;
- System AI лучше свернуть в accordion/cards-list ниже;
- карточки должны читаться без hover и без плотных side labels.

### Telegram Mini App

- максимум 2-3 короткие карточки в одном потоке;
- приоритет: `Beginner Bot`, `Aggressor Bot`, `Coach Agent`;
- остальные карточки открывать по кнопке `Еще агенты`.

### macOS app

- cards могут жить в right-side recommendation rail или library grid;
- уместен более плотный desktop layout с быстрым запуском тренировки;
- структура и названия должны совпадать с web, чтобы не было product drift.

## Card Anatomy

Каждая карточка Training Opponent должна состоять из следующих слоев.

### 1. Identity row

- short agent label;
- type badge: `AI-соперник`;
- difficulty chip или recommended level range.

Примеры:

- `Новичковый бот`
- `Calling Station`
- `Tight Regular`

### 2. Core promise

Один короткий headline, который объясняет тренировочную ценность:

- `Учит value betting против частых коллов`
- `Наказывает автоколлы и слабую защиту диапазона`
- `Помогает освоить первые решения без перегруза`

Headline должен быть instructional, а не hype-driven.

### 3. Skill focus

2-4 compact tags:

- `Preflop`
- `Value`
- `Fold discipline`
- `ICM`
- `Tilt resistance`

Теги нужны как быстрый фильтр и будущий bridge к diagnostic metrics.

### 4. Description

Одно короткое описание в 2-3 строках:

- как бот обычно играет;
- какую типичную ошибку пользователя вскрывает;
- без длинной теории внутри карточки.

### 5. Recommended for

Строка формата:

`Подходит: Beginner-Intermediate`

или

`Подходит: Advanced / Grinder`

### 6. Primary action

Варианты CTA:

- `Тренироваться`
- `Смотреть споты`
- `Добавить в план`

На главной лучше использовать один базовый CTA `Тренироваться`, чтобы не распылять действия.

### 7. Secondary insight

Небольшая supporting row:

- `Часто коллирует флоп и терн`
- `Давит 3-bet и c-bet линиями`
- `Разбирает ошибки после раздачи`

Эта строка помогает различать карточки без раскрытия детального модала.

## System AI Card Anatomy

Карточки системных агентов должны быть компактнее и спокойнее визуально.

Обязательные поля:

- agent name;
- short role line;
- input/output hint;
- one action или link на объяснение.

Пример структуры:

- `Skill Evaluator`
- `Определяет уровень по качеству решений`
- `Вход: hand history -> Выход: leaks, strengths, next lesson`
- CTA `Как считается уровень`

## Visual Direction

Карточки должны ощущаться как training tools, а не как casino avatars.

### Base styling

- dark graphite shell;
- subtle felt or grid texture;
- green highlight for learning-positive states;
- red accent только для pressure/aggression markers;
- gold использовать точечно для advanced/pro labels, не как основной заливочный цвет.

### Avatar approach

Не использовать фотореалистичные персонажи или poker-celebrity imagery. Предпочтительно:

- abstract portrait silhouettes;
- icon-driven marks;
- seat markers;
- minimal illustrated badges.

Это снижает визуальный шум и облегчает перенос между четырьмя поверхностями.

### Interaction states

- default;
- hover/focus for desktop;
- active/pressed for mobile;
- selected/in-plan state;
- locked or `позже` state для advanced bots на низких уровнях.

## Content Rules

- Никаких обещаний выигрыша или заработка.
- Никакого real-money wording.
- Описывать стиль бота через решения и pressure patterns, а не через "легкие деньги" или "побеждай поле".
- Текст должен быть короче, чем полноценный lesson card.
- Английские poker terms допустимы, если они нужны для точности и не ломают RU-first reading.

## Recommended Agent Copy Angles

### Beginner Bot

- главный смысл: безопасный вход в первые учебные раздачи;
- фокус: правила, очередность действий, простые value spots;
- рекомендованный уровень: First Hand / Beginner.

### Calling Station Bot

- главный смысл: учит добирать value и меньше блефовать в пустоту;
- фокус: thin value, sizing basics, fold to bad bluffs;
- рекомендованный уровень: Beginner / Recreational.

### Tight Regular Bot

- главный смысл: учит уважать сильный диапазон и позицию;
- фокус: preflop discipline, selective aggression;
- рекомендованный уровень: Recreational / Intermediate.

### Aggressor Bot

- главный смысл: проверяет реакцию на давление;
- фокус: defense, re-raise logic, emotional control;
- рекомендованный уровень: Intermediate / Advanced.

### GTO-ish Bot

- главный смысл: тренирует сбалансированные линии и план на несколько улиц;
- фокус: range thinking, bluff mix, board coverage;
- рекомендованный уровень: Advanced / Grinder.

### Tournament Bot

- главный смысл: переносит пользователя в MTT/ICM pressure;
- фокус: short stack, push-fold, bubble decisions;
- рекомендованный уровень: Intermediate / Grinder.

## Responsive Rules

### Desktop web

- card min width: 280-320px;
- grid gap держать в диапазоне 20-24px;
- headline и tags должны помещаться без скачков высоты в одной строке или аккуратно в двух.

### Mobile web

- одна карточка в ряд;
- padding компактнее desktop, но CTA не меньше 44px высоты;
- длинные названия вроде `Tournament Bot` и `Calling Station` не должны ломать badge row;
- tags разрешено переносить на две строки, но не больше.

### Telegram Mini App

- упор на compact summary, 1 CTA и 2 skill tags;
- избегать тяжелых background layers и сложных тени;
- текст должен помещаться в 4-6 коротких строк без скролла внутри карточки.

### macOS app

- допускается более плотная grid/list hybrid layout;
- secondary actions можно показывать сразу, если есть место в sidebar/detail shell;
- hover/focus states должны быть пригодны для pointer-driven desktop usage.

## Section Composition Guidance

Рекомендуемая web-секция:

1. heading `Выберите AI-соперника под свою слабую зону`
2. short intro line про play-money training
3. training-opponent grid
4. compact block `Как помогают системные AI-агенты`

Не стоит в этой секции:

- смешивать news/tournament cards;
- показывать full agent biographies;
- добавлять больше 6 opponent cards в первом слое;
- перегружать карточки метриками, которые логичнее показать в HUD или result screen.

## Handoff To Future Steps

Этот card spec должен направлять следующие шаги, но не заменяет их:

- Step 18: HUD диагностики использует те же skill tags и level markers;
- Step 19: result screen может ссылаться на подходящего бота для доработки leak;
- Step 20: personal learning map использует карточки как вход в drills;
- Step 28: контентный блок `AI-соперники` может брать отсюда структуру и краткие copy angles.
