# First Screen With Poker Table

Дата: 2026-07-05
Шаг: 16. Спроектировать первый экран с покерным столом

## Цель

Зафиксировать контракт первого экрана главной страницы для AI poker training platform. Экран должен сразу вести в диагностику уровня, показывать покерный стол как основную product-surface и оставаться читаемым на desktop web, mobile web, Telegram Mini App и в будущем macOS app.

Этот шаг проектирует hero-screen и его поведение. Он не внедряет финальный production UI и не подменяет будущие шаги по карточкам агентов, HUD или result screens.

## Product Job Of The First Screen

Первый экран должен за 3-5 секунд ответить на четыре вопроса:

1. Что это: AI trainer по покеру, а не casino.
2. Что делать дальше: пройти короткую диагностику.
3. Как это работает: сыграть несколько учебных раздач против AI.
4. Что получит пользователь: уровень, ошибки и персональный план.

## Core Message Stack

### Eyebrow

- `18+`
- `Play-money training platform`

Eyebrow должен быть коротким и не выглядеть как warning banner, но сразу удерживать safe framing.

### Hero headline

Рекомендуемая идея:

`Сыграйте несколько учебных раздач и узнайте свой уровень игры в покер.`

Требования к headline:

- фокус на диагностике и обучении;
- без обещаний выигрыша, дохода или `обыгрыша поля`;
- максимум 2 строки на desktop и 3-4 строки на mobile;
- не использовать casino-style hype wording.

### Supporting copy

Рекомендуемая смысловая структура:

- 10-20 учебных раздач;
- AI оценивает решения, а не luck;
- после сессии пользователь получает уровень, 3 ошибки и следующий урок.

Supporting copy должен быть короче текущего B2B-абзаца и работать как product explanation, а не как marketing essay.

## Primary Composition

### Desktop web

Рекомендуемая композиция: split hero `content left / table right`.

Левая зона:

- eyebrow;
- headline;
- short supporting copy;
- primary CTA `Определить мой уровень`;
- secondary CTA `Как работает диагностика`;
- compact trust row: `18+`, `Play-money only`, `Без real-money игры`.

Правая зона:

- stylized poker table;
- 5-seat training setup;
- player cards, board area, pot, stack pills;
- one highlighted AI seat;
- compact diagnostic preview card поверх стола.

Правило:

- стол должен ощущаться как настоящий core surface продукта, а не фоновой баннер;
- CTA и текст не должны накладываться на карты, банк или HUD preview.

### Mobile web

Рекомендуемая композиция: stacked hero `content top / compact table below`.

Порядок:

1. eyebrow + safety labels;
2. headline;
3. short copy;
4. primary CTA;
5. secondary CTA;
6. compact vertical poker table;
7. 2-3 diagnostic chips.

Mobile-правила:

- headline ужимается до mobile display scale;
- CTA и safety labels видны без horizontal scroll;
- table crop допускается, но board, hero cards и primary action preview должны оставаться видимыми;
- никакие floating badges не перекрывают CTA.

## Poker Table Spec For Hero

Стол не должен быть фотореалистичным casino image. Это product illustration / interface mock.

Обязательные элементы:

- felt-based oval or rounded-rect table;
- центр стола под pot/board;
- место пользователя снизу;
- 2-4 AI opponents вокруг;
- chip stacks как учебные markers, без money UI;
- action glow или highlight только у активного decision state.

Опциональные элементы:

- мягкая линия dealer/button;
- simplified action pills `Fold`, `Call`, `Raise`;
- hand label вроде `A♠ K♠`;
- preview caption `AI анализирует решение`.

Запрещено:

- slot/casino imagery;
- jackpots, bonus chips, payout numbers;
- flashing win language;
- crowded HUD, который превращает hero в полноценный game screen.

## Diagnostic Preview Module

На первом экране нужен маленький preview аналитики, чтобы продукт читался как training lab, а не просто poker media site.

Рекомендуемый модуль:

- title `После 10 раздач вы получите`;
- 3 compact rows:
  - `Уровень игры`
  - `Главные ошибки`
  - `Следующий урок`

Desktop:

- модуль может частично перекрывать правую часть стола.

Mobile:

- модуль лучше ставить под столом или в нижней части table card, если он не создает overlap.

## CTA Contract

### Primary CTA

`Определить мой уровень`

Роль:

- запустить diagnostic flow;
- быть самым заметным action на экране;
- визуально доминировать над вторичным CTA.

### Secondary CTA

`Как работает диагностика`

Роль:

- объяснить механику без ухода со страницы;
- помочь тем, кто не готов сразу начать.

Запрещенные CTA:

- `Играть на деньги`
- `Сесть за стол`
- `Начать выигрывать`
- `Заработать покером`

## Information Density

Hero должен жить в режиме `Immersive Table Density` из typography contract.

Что оставить:

- один headline;
- один supporting paragraph;
- максимум 2 CTA;
- 3 trust labels;
- 1 compact analytics preview.

Что не добавлять на этом шаге:

- длинные explanation blocks;
- grid из AI-агентов;
- tournament/news cards внутри первого viewport;
- полный hand history;
- сложный footer-like disclaimer wall.

## Surface Guidance

### Desktop web

- hero высотой примерно 720-820px;
- navigation и hero должны работать как единый первый fold;
- справа можно использовать более богатую table illustration и depth layers;
- первый CTA должен оставаться видим сразу после загрузки без скролла.

### Mobile web

- first screen должен помещать headline, CTA и верх стола в первый viewport;
- safe labels должны быть короткими;
- элементы стола не должны становиться мельче практической читаемости;
- preferred layout без overlap и без двустрочных CTA.

### Telegram Mini App

- этот hero не переносится один в один;
- Mini App берет ту же message stack, но в коротком виде: headline, CTA, 1 compact table preview;
- secondary CTA может уходить в sheet или следующий экран;
- главный акцент на quick level check, а не на long-form marketing hero.

### macOS app

- будущий app может использовать похожий split-shell как стартовый dashboard;
- table preview и diagnostic summary хорошо переносятся в desktop window;
- hero wording и action labels должны совпадать с web, чтобы не было product drift.

## Motion And Mood

- мягкий ambient glow вокруг active seat или CTA;
- subtle chip/board shimmer допустим только как вторичный акцент;
- нельзя строить экран на агрессивной анимации;
- motion должен подчеркивать focus on decision, а не азарт.

## Migration Note From Current Homepage

Текущая `index.html` использует B2B hero с фото и общим описанием международных проектов. Для poker-платформы первый экран должен заменить:

- B2B headline на diagnostic-first poker headline;
- photo background на table-centric product scene;
- CTA `Направления работы` на `Определить мой уровень`;
- business metrics row на training/trust signals.

## Acceptance Line For Step 16

Шаг 16 считается закрытым, если команда понимает:

- как должен выглядеть и работать первый экран poker platform;
- какая message hierarchy обязательна в первом viewport;
- как table, CTA и diagnostic preview делят пространство без overlap;
- как этот hero адаптируется под desktop web, mobile web, Telegram Mini App и будущий macOS app;
- какие элементы допустимы, а какие нельзя приносить из casino/gambling паттернов.
