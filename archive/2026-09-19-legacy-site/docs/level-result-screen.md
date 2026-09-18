# Level Result Screen

Дата: 2026-07-05
Шаг: 19. Спроектировать экран результата уровня

## Цель

Зафиксировать контракт экрана результата уровня для poker training platform. Экран должен завершать диагностическую сессию ясным вердиктом, объяснять сильные и слабые стороны игрока и направлять его в следующий учебный маршрут без casino/gambling framing.

Этот шаг проектирует структуру, copy hierarchy и responsive behavior result screen. Он не внедряет production UI, не определяет scoring formulas и не подменяет будущие шаги по learning map, lesson templates или hand trainer logic.

## Product Job Of The Result Screen

Экран результата должен за один просмотр отвечать на пять вопросов:

1. Какой уровень система определила сейчас.
2. Почему результат именно такой.
3. Какие 3 ошибки мешают расти дальше.
4. Какие 2-3 сильные стороны уже есть.
5. Что делать следующим шагом: урок, тренировка, повторная диагностика.

Результат должен ощущаться как учебный разбор, а не как gamified win/loss screen.

## Core Outcome Stack

### 1. Level Verdict

Главный блок:

- level label `Beginner`, `Recreational`, `Intermediate` и т.д.;
- RU-пояснение уровня;
- короткая one-line summary;
- optional confidence marker вроде `оценка после 12 учебных раздач`.

Примеры summary:

- `Вы понимаете базовые правила, но пока часто переплачиваете коллами.`
- `Префлоп уже дисциплинированнее среднего, но давление на поздних улицах сбивает план.`

Ограничения:

- без фраз `вы почти профи`;
- без обещаний выигрыша;
- без shaming wording.

### 2. Why We Think So

Короткий explainability block:

- `Сильнее всего: preflop discipline, value recognition`
- `Проседает: fold vs pressure, play out of position`

Это bridge между live HUD и детальным разбором. Пользователь должен понимать, что уровень присвоен по качеству решений, а не по одной удачной раздаче.

### 3. Top Leaks

Обязательный блок из 3 приоритетных ошибок.

Структура каждой строки:

- название ошибки;
- короткое объяснение;
- actionable rewrite `что делать вместо этого`.

Примеры:

- `Лишние коллы вне позиции`
- `Слишком редкий фолд на силу`
- `Ставки без понятной цели`

Этот блок должен быть выше длинных hand reviews и ниже level verdict.

### 4. Strengths

Нужен отдельный блок с 2-3 сильными сторонами.

Причина:

- экран не должен быть только про ошибки;
- strengths помогают удержать мотивацию и показать персонализацию;
- это полезно для будущего curriculum routing.

Формат:

- `Аккуратный вход в банк на ранних позициях`
- `Хорошо замечаете value spot против пассивного соперника`

### 5. Next Best Route

Главный action block после результата.

Обязательные элементы:

- `Следующий лучший урок`
- `Следующая тренировка`
- `Повторить диагностику позже`

Порядок приоритета:

1. lesson;
2. targeted drill;
3. optional retry.

Экран результата должен вести в обучение, а не оставлять пользователя в тупике после вердикта.

## Recommended Screen Anatomy

### Desktop Web

Рекомендуемый паттерн: two-column analytical summary.

Левая колонка:

- level verdict hero;
- why we think so;
- top leaks.

Правая колонка:

- strengths;
- next best route;
- 1 featured hand insight;
- compact note about play-money/educational framing.

Desktop может использовать более широкую компоновку с sticky action rail, но без перегруза solver-like tables.

### Mobile Web

Рекомендуемый паттерн: single-column stacked result.

Порядок:

1. level verdict;
2. short explanation;
3. top leaks;
4. strengths;
5. next route CTA stack;
6. optional hand insight accordion.

Mobile rules:

- не больше 1 primary CTA в видимой зоне сразу;
- labels и chips не должны ломаться в 3-4 строки;
- плотные score tables скрывать за раскрывающимся блоком;
- никакие floating cards не должны перекрывать CTA или summary.

### Telegram Mini App

Mini App берет сокращенную result-модель:

- level verdict;
- 2 главные ошибки;
- 1 следующий шаг;
- кнопка открыть полный план на web.

Mini App result должен быть быстрым, вертикальным и без тяжелых аналитических таблиц.

### macOS App

Будущий macOS app может использовать desktop result pattern с более утилитарной правой панелью:

- verdict header;
- persistent progress sidebar;
- recent sessions link;
- quick reopen lesson.

Названия уровней, leaks и next-route labels должны совпадать с web.

## Information Hierarchy

Порядок важности на экране:

1. level verdict;
2. top leaks;
3. next best route;
4. strengths;
5. supporting hand insight;
6. deeper metric details.

Если экран тесный, full metric grids и secondary chips убираются первыми. Вердикт и следующий шаг всегда должны быть видны без лишнего скролла на основном viewport.

## Metric Presentation Rules

Экран результата может показать больше сигналов, чем live HUD, но не должен превращаться в raw spreadsheet.

Разрешено:

- 4-6 metric bars или chips;
- grouped skills вроде `Префлоп`, `Позиция`, `Агрессия`, `Pot odds`;
- short status wording `сильно`, `нестабильно`, `зона роста`.

Не стоит показывать:

- длинную numeric table из 10+ строк в первом экране;
- непонятные solver-like проценты без контекста;
- ranking language в духе leaderboards.

Полный разбор можно вынести в `Подробнее о решениях` или отдельный hand review section.

## Hand Review Preview

Result screen должен содержать только teaser hand-review, а не полный replay.

Рекомендуемый модуль:

- `Ключевая раздача сессии`
- board snapshot;
- 1 ошибка или сильное решение;
- CTA `Разобрать эту раздачу`.

Это создает мост к будущим шагам 52-59, но не подменяет их.

## Tone Of Voice

Тон результата:

- спокойный;
- точный;
- обучающий;
- без унижения;
- без hype.

Хорошие формулировки:

- `Сейчас ваш лучший результат связан с аккуратной игрой на префлопе.`
- `Следующий рост даст дисциплина против позднего давления.`
- `Начните с короткого урока и 5 тренировочных спотов.`

Плохие формулировки:

- `Вы пока слабый игрок`
- `Ещё немного и начнете плюсовать`
- `Разнесете стол после этого урока`

## State Model

Экран результата должен поддерживать минимум четыре состояния:

1. `Fresh result`
   Итог только что завершенной диагностики.
2. `Expanded details`
   Пользователь раскрыл deeper metrics или featured hand.
3. `Route selected`
   Пользователь выбрал lesson/drill как следующий шаг.
4. `Repeat diagnostic prompt`
   Пользователю показано, когда имеет смысл пройти диагностику снова.

## CTA Contract

Primary CTA:

- `Начать следующий урок`

Secondary CTAs:

- `Пройти тренировку по ошибкам`
- `Разобрать ключевую раздачу`
- `Повторить диагностику позже`

Запрещенные CTA:

- `Играть на деньги`
- `Испытать удачу`
- `Выигрывать больше`

## Accessibility And Clarity

- verdict нельзя кодировать только цветом;
- level label должен сопровождаться текстовым пояснением;
- metric bars должны иметь text labels;
- на mobile ключевые блоки должны читаться без горизонтального скролла;
- длинные leak descriptions сворачивать до 2 строк preview.

## Relationship To Other Steps

Этот spec опирается на:

- `docs/player-levels.md`
- `docs/diagnostic-metrics.md`
- `docs/diagnostic-hud.md`
- `docs/legal-constraints.md`

Этот spec подготавливает:

- Step 20: personal learning map;
- Step 44-48: scoring and final level scale;
- Step 52-55: hand review, personal plan и progress modules.

Он не подменяет scoring engine, curriculum logic или контент самих уроков.
