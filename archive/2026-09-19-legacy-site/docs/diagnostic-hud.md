# Diagnostic HUD

Дата: 2026-07-05
Шаг: 18. Спроектировать HUD диагностики

## Цель

Зафиксировать контракт диагностического HUD для poker training platform. HUD должен помогать пользователю понимать ход оценки во время учебных раздач, не заслонять стол и не превращать экран в перегруженный solver-like интерфейс.

Этот шаг проектирует структуру, приоритеты и responsive behavior HUD. Он не внедряет production UI и не подменяет будущие шаги по экрану результата уровня, scoring logic или финальному игровому прототипу.

## Product Job Of The HUD

HUD отвечает на четыре вопроса прямо во время сессии:

1. На какой раздаче и каком этапе диагностики находится пользователь.
2. Какой decision spot сейчас оценивается.
3. Какие сигналы уровня уже видит система.
4. Что произойдет после завершения короткой серии раздач.

HUD должен поддерживать confidence и focus. Пользователь должен чувствовать, что его учат и анализируют, а не просто показывают декоративный poker overlay.

## Core HUD Modules

### 1. Session Progress

Обязательные поля:

- `Раздача 4 из 12`
- `Флоп` / `Терн` / `Ривер` / `Префлоп`
- optional timer только если он не давит на новичка

Роль:

- удерживать чувство короткой, конечной сессии;
- показывать, что диагностика оценивает серию решений, а не одну lucky hand.

### 2. Active Skill Lens

HUD должен показывать, какой навык сейчас в фокусе.

Примеры labels:

- `Позиция`
- `Префлоп дисциплина`
- `Fold vs Call`
- `Размер ставки`
- `Опасная доска`

Правило:

- одновременно подсвечивать только 1 primary lens и максимум 1 secondary lens;
- не показывать весь список метрик сразу.

### 3. Running Read

Компактный блок с промежуточным impression без финального вердикта.

Примеры:

- `Чаще верные решения против пассивных линий`
- `Есть лишние коллы вне позиции`
- `Сильный старт на префлопе`

Ограничения:

- wording короткий и практичный;
- без фраз в стиле `вы почти профи`;
- без обещаний выигрыша или денег.

### 4. Next Outcome Preview

Нижний или боковой mini-module:

- `После серии вы получите уровень`
- `3 главные ошибки`
- `Следующий урок`

Этот модуль связывает live HUD с будущим result screen и объясняет, зачем пользователь проходит диагностику до конца.

## Information Hierarchy

HUD должен работать по приоритетам:

1. текущий decision state;
2. progress по сессии;
3. active skill lens;
4. running read;
5. next outcome preview.

Если экран тесный, secondary copy и декоративные chips убираются первыми. Board, player actions и pot никогда не должны уступать место HUD-метаданным.

## Layout Contract

### Desktop Web

Рекомендуемый паттерн: table as primary surface + compact analytical rail.

Состав:

- table в центре;
- HUD rail справа или слева шириной около 280-340px;
- один floating status chip над столом допустим;
- critical actions пользователя остаются в нижней safe zone.

Desktop HUD может включать:

- session progress;
- active skill lens;
- running read;
- compact metric chips;
- hidden/collapsible helper note `Оцениваем решения, а не luck`.

Нельзя:

- перекрывать board cards;
- ставить широкую панель поверх action buttons;
- превращать rail в длинный article-like текст.

### Mobile Web

Рекомендуемый паттерн: stacked compact HUD вокруг стола.

Порядок:

1. top progress strip;
2. table;
3. active lens chip row;
4. running read card;
5. action area.

Mobile rules:

- HUD должен жить в 2-3 компактных блоках, а не в постоянной боковой панели;
- длинные explanations сворачивать в `Почему это важно`;
- critical controls должны оставаться в зоне большого пальца;
- ни один HUD badge не должен перекрывать карты, pot или CTA.

### Telegram Mini App

Mini App берет только essential subset:

- progress;
- active lens;
- 1-line running read.

Без heavy rail, dense chips и длинных coach notes. Основной сценарий mini app: короткая диагностика 3-5 раздач, поэтому HUD должен быть быстрее и тише, чем на desktop web.

### macOS App

Будущий macOS app может использовать desktop analytical rail почти без изменений, но с более утилитарным shell:

- persistent side panel;
- collapsible hand notes;
- compact history-aware HUD.

Названия навыков и логика статусов должны совпадать с web, чтобы не было product drift.

## Metric Visibility Rules

HUD не должен сразу показывать полную score table из `docs/diagnostic-metrics.md`.

Во время live-сессии показываем только:

- current focus;
- 1-2 intermediate reads;
- optional confidence chip вроде `Собираем картину`.

Полная детализация метрик уходит в result screen и hand review.

Причина:

- новичок теряется от 8-10 параллельных сигналов;
- live HUD должен помогать действовать, а не читать отчет;
- мобильный экран не выдержит solver-density без overlap.

## Tone Of Voice

HUD copy должна быть:

- короткой;
- нейтрально-обучающей;
- конкретной;
- без осуждения.

Хорошие примеры:

- `Пока вы аккуратны на префлопе`
- `Есть лишний колл против силы`
- `Оцениваем решение на опасной доске`

Плохие примеры:

- `Вы сливаете фишки`
- `Так играют слабые`
- `Ещё немного и начнете выигрывать`

## State Model

HUD должен поддерживать минимум пять состояний:

1. `Intro state`
   Короткое объяснение, что сейчас начнется оценка серии решений.
2. `Decision live state`
   Основной режим с progress, lens и running read.
3. `Action locked state`
   После выбора действия HUD кратко фиксирует оценку без финального judgement.
4. `Hand transition state`
   Короткий bridge между раздачами: что уже заметили и сколько осталось.
5. `Session complete state`
   Переход к screen результата уровня и personal route.

## Density And Motion

HUD должен использовать `Analytical HUD Density` из `docs/typography-density.md`.

Рекомендации:

- card padding 14-18;
- row height 36-44;
- chips компактные, но читаемые;
- subtle glow только у active lens или progress pulse.

Нельзя:

- мигающие warning patterns;
- агрессивные красные вспышки;
- постоянную анимацию на каждом update.

## Accessibility And Clarity

- основной прогресс и active lens нельзя кодировать только цветом;
- chips и labels должны иметь text meaning, а не только icon meaning;
- running read должен читаться с первого взгляда за 1-2 секунды;
- на mobile critical HUD text не должен уходить в 3-4 строки.

## Relationship To Future Steps

Этот HUD spec подготавливает:

- Step 19: screen результата уровня;
- Step 37-48: hand model, legal actions, scenarios и scoring;
- Step 52: hand review template;
- будущий training table UI.

Он не определяет финальные numeric thresholds или evaluator formulas. Это останется за diagnostic/scoring steps позже.

## Migration Note From Current Site

Текущий сайт не содержит игрового или аналитического HUD. Это значит, что внедрение потребует новой темной surface architecture, а не адаптации существующих B2B cards и section blocks из `index.html` и `assets/styles.css`.

## Acceptance Line For Step 18

Шаг 18 считается закрытым, если команда понимает:

- какие модули входят в диагностический HUD;
- что пользователь видит во время live-диагностики, а что откладывается до result screen;
- как HUD не конфликтует со столом и action controls на desktop web и mobile web;
- какой сокращенный набор HUD нужен для Telegram Mini App;
- как будущий macOS app может использовать тот же аналитический контракт.
