# AI-агенты платформы

Дата: 2026-07-05

## Архитектурное правило

LLM не управляет правилами покера. Колода, порядок действий, банк, легальные действия и определение победителя находятся в детерминированном Game Engine. AI-агенты могут выбирать из легальных действий, объяснять и обучать, но не менять правила игры.

## Game Engine

Отвечает за:

- shuffle/deal;
- blinds/button;
- legal actions;
- pot and side pots;
- street transitions;
- showdown;
- hand history.

## Skill Evaluator

Оценивает решения игрока по метрикам диагностики и присваивает уровень 0-6.

Вход: hand history, actions, position, stack, pot, board, bot styles.

Выход: level, style, leaks, strengths, recommended curriculum.

## Curriculum Agent

Собирает персональный маршрут обучения из модулей.

Пример: "Preflop discipline -> Position basics -> Value betting -> Pot odds -> Calling Station drills".

## Coach Agent

Объясняет отдельные раздачи простым языком. Должен говорить коротко, практично и без обещаний заработка.

## Beginner Bot

Слабый соперник для новичка. Делает понятные ошибки, не давит сложными линиями.

## Calling Station Bot

Часто коллирует. Нужен для тренировки value betting и отказа от бессмысленного блефа.

## Tight Regular Bot

Играет узко и дисциплинированно. Учит уважать сильные диапазоны.

## Aggressor Bot

Часто ставит и рейзит. Проверяет tilt resistance, защиту диапазона и умение не сдаваться автоматически.

## GTO-ish Bot

Играет ближе к сбалансированной стратегии. Нужен для advanced/grinder уровней.

## Tournament Bot

Создает MTT-ситуации: short stack, resteal, bubble, pay jumps, bounty, final table pressure.

## Safety Agent

Проверяет тексты и AI-ответы:

- нет обещаний дохода;
- нет инструкций по обходу законов;
- нет real-money призывов;
- есть play-money/educational framing;
- есть responsible play, где это уместно.
