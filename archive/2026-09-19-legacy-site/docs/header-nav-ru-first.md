# RU-First Header And Navigation

Дата: 2026-07-05
Шаг: 15. Спроектировать header/nav для RU-first сайта

## Цель

Зафиксировать навигационный контракт первой версии poker training platform для четырех поверхностей: desktop web, mobile web, Telegram Mini App и будущего macOS app. Навигация должна вести пользователя в диагностику, обучение, контент и personal plan без casino/gambling framing.

Этот шаг проектирует структуру и поведение навигации. Он не внедряет финальный UI и не подменяет будущие шаги hero/layout/screens.

## RU-First Principle

- Базовый язык первой версии: русский.
- Английская версия остается secondary surface, а не источник терминов по умолчанию.
- Poker terms можно оставлять на английском, если это отраслевой стандарт и рядом есть понятная RU-formулировка.
- Navigation labels должны быть короткими, чтобы не ломать mobile, Telegram Mini App и будущий desktop shell.

## Primary Navigation Goals

- быстро отправить нового пользователя в диагностику;
- дать ясный путь в обучение и библиотеку;
- не смешивать articles, news и tournaments в одну перегруженную группу;
- сохранить доступ к personal plan и AI table как product surfaces, а не marketing pages;
- удержать responsible play framing видимым без перегруза header.

## Top-Level Information Architecture

Рекомендуемый набор primary destinations:

1. `Диагностика`
2. `Обучение`
3. `Тренажер`
4. `Статьи`
5. `Турниры`
6. `Новости`

Вторичные destinations:

- `План`
- `О проекте`
- `Responsible Play`

System destinations:

- `RU / EN`
- `Войти`
- `Определить уровень`

## Recommended Header Composition

### Left zone

- brand mark;
- wordmark `Фулхаус Poker AI`;
- optional micro-label `Play-money training platform`.

### Center zone

- primary navigation links на desktop;
- current-section highlight;
- optional compact divider between product and content clusters.

### Right zone

- language switch;
- `Войти` или `Мой план` для возвращающегося пользователя;
- primary CTA `Определить уровень`.

## Navigation Clusters

### Product cluster

- `Диагностика`
- `Обучение`
- `Тренажер`
- `План`

Это основная продуктовая ось. Она отвечает за action-first сценарии и должна визуально доминировать над content/navigation links.

### Content cluster

- `Статьи`
- `Турниры`
- `Новости`

Контентные разделы не должны перетягивать внимание у primary CTA, но должны быть доступны с первого экрана и в desktop, и в mobile.

### Trust cluster

- `О проекте`
- `Responsible Play`

Эти ссылки можно прятать во вторичный слой desktop navigation или mobile drawer, но они должны оставаться легко достижимыми.

## Label Rules

- `Диагностика` лучше, чем `Тест` или `Оценка`, потому что слово сразу объясняет продуктовую функцию.
- `Обучение` лучше, чем `Курсы`, потому что путь персонализирован и шире статичного курса.
- `Тренажер` лучше, чем `Играть`, чтобы не создавать casino-style ожидание.
- `Новости` и `Турниры` держать отдельно: пользователь должен сразу понимать, где editorial feed, а где calendar/format coverage.
- `План` использовать как краткое имя personal learning route.
- Не использовать labels вроде `Касса`, `Ставки`, `Игры на деньги`, `Лобби`.

## Desktop Web Navigation Spec

### Header layout

- sticky header;
- высота 76-80px;
- brand слева, nav по центру, actions справа;
- primary CTA всегда видим в первом ряду;
- не более 6 primary links одновременно.

### Recommended desktop order

1. `Диагностика`
2. `Обучение`
3. `Тренажер`
4. `Статьи`
5. `Турниры`
6. `Новости`

Secondary actions справа:

- `План`
- `RU / EN`
- `Войти`
- primary CTA `Определить уровень`

### Overflow rule

Если ширины не хватает, убирать в secondary/menu сначала `Новости`, потом `Турниры`, но не `Диагностика`, `Обучение` и `Тренажер`.

## Mobile Web Navigation Spec

### Header layout

- compact sticky header 60-68px;
- brand слева;
- одна заметная CTA-кнопка или pill `Диагностика`;
- menu icon справа.

### Mobile first row

- brand;
- compact CTA `Уровень`;
- menu button.

### Mobile drawer contents

1. `Определить уровень`
2. `Обучение`
3. `Тренажер`
4. `Мой план`
5. `Статьи`
6. `Турниры`
7. `Новости`
8. `О проекте`
9. `Responsible Play`
10. `RU / EN`

### Mobile behavior rules

- touch targets минимум 44px;
- drawer links в один столбец;
- не использовать двухуровневое выпадающее меню;
- current section должен быть явно подсвечен не только цветом, но и weight/background;
- CTA и burger не должны перекрывать title и safe-area inset.

## Telegram Mini App Navigation Spec

### Core principle

Mini App не должен копировать полный web header. Нужна короткая навигация под быстрые сессии.

### Recommended tabs

1. `Диагностика`
2. `Задание`
3. `План`
4. `Еще`

`Еще` раскрывает:

- `Статьи`
- `Турниры`
- `Новости`
- `Responsible Play`

### Mini App rules

- primary action всегда связан с короткой diagnostic/training session;
- news/articles не должны мешать quick-return workflow;
- labels максимально короткие;
- top chrome должен учитывать Telegram WebApp safe areas и не дублировать системный header.

## Future macOS App Navigation Spec

### Shell approach

Для macOS app логичнее не web-like top nav, а desktop sidebar shell.

### Sidebar structure

1. `Диагностика`
2. `План`
3. `Тренажер`
4. `Статьи`
5. `Турниры`
6. `Новости`
7. `Responsible Play`
8. `О проекте`

Utility zone:

- account;
- session history;
- quick launch `Новая раздача`.

### macOS rules

- сохранить те же разделы и labels, что на web;
- сделать `План` и `История` более заметными, чем на mobile;
- не строить отдельную macOS IA с другими названиями экранов.

## CTA Strategy

### Primary CTA

`Определить уровень`

Роль:

- запуск первого diagnostic flow;
- возврат пользователя в core action;
- главный CTA на desktop, mobile и landing-like surfaces.

### Secondary CTAs

- `Открыть план`
- `Сыграть раздачу`
- `Читать статью`

Secondary CTA не должен визуально спорить с `Определить уровень`.

## State Model

### New visitor

- видит brand, primary nav и CTA `Определить уровень`;
- `План` может быть hidden или вести на объяснение benefits/sign-in.

### Returning user

- CTA справа может меняться на `Продолжить обучение`;
- `План` становится persistent navigation item;
- можно показать last activity indicator около `План`.

### In-session user

- full top nav на desktop может сворачиваться в compact mode;
- на mobile и Mini App важно удержать quick exit/back to plan без лишних links;
- во время hand flow secondary content links должны уходить из первого ряда.

## URL/Section Mapping

- `/` - главная
- `/diagnostics/` - диагностика
- `/learn/` - обучение
- `/trainer/` - тренажер
- `/plan/` - личный план
- `/articles/` - статьи
- `/tournaments/` - турниры
- `/news/` - RSS/news
- `/responsible-play/` - responsible play
- `/about/` - о проекте

RU-first slug strategy можно обсудить позже, но на первом этапе лучше сохранить короткие латинские URL и русский UI copy.

## Responsive Guardrails

- Не допускать переноса primary nav в две строки на desktop.
- На tablet-width сначала упрощать actions, потом links.
- На mobile header не должен занимать слишком много вертикали над столом и CTA.
- В content pages header должен оставаться компактнее, чем на marketing-like hero sections.

## Safety And Tone Guardrails

- Навигация не должна использовать азартные/promotional формулировки.
- Нельзя ставить в header wording, обещающий выигрыш, доход или betting excitement.
- `Тренажер` и `Диагностика` должны звучать как обучение и практика, а не лобби казино.
- Responsible play entry должен присутствовать минимум во drawer/footer, даже если не виден в primary row.

## Implementation Notes For Next Steps

- Step 16 должен встроить этот header contract в hero с покерным столом без потери главного CTA.
- Step 24 должен проверить, что desktop/mobile states не ломают labels и не дают overlap.
- Когда начнется реальный UI rewrite, текущую B2B navigation structure из `index.html` нужно будет заменить на product-first IA из этого документа.
