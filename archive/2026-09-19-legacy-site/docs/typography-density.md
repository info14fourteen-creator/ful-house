# Typography, Sizing And Density

Дата: 2026-07-05
Шаг: 14. Определить типографику, размеры, плотность интерфейса

## Цель

Зафиксировать типографическую систему и scale будущей poker training platform так, чтобы интерфейс ощущался плотным, инструментальным и современным, но оставался читаемым на desktop web, mobile web, Telegram Mini App и в будущем macOS app.

Этот шаг не меняет текущий светлый B2B UI напрямую. Он создает contract для следующих экранов и migration away from текущего `Inter + roomy SaaS` паттерна.

## Арт-направление типографики

- Тон: poker room + training lab, а не fintech dashboard и не casino poster.
- Иерархия: крупные уверенные headlines, плотные labels, спокойный body copy.
- Читаемость: длинные статьи и объяснения AI не должны превращаться в декоративный display UI.
- Плотность: игровые и диагностические экраны компактнее контентных страниц.

## Font System

### 1. Display / Headline Family

Рекомендуемая primary family для hero, section headlines и rank/result emphasis:

- `"Manrope", "Inter", "Segoe UI", sans-serif`

Почему:

- Manrope выглядит собраннее и плотнее текущего Inter;
- хорошо работает в кириллице;
- сохраняет tech/product характер без luxury-gambling стилизации.

Использование:

- hero headline;
- section titles;
- уровень игрока;
- titles карточек AI-агентов;
- major CTA blocks.

### 2. UI / Body Family

Рекомендуемая рабочая family для body copy, labels, tables, chips и navigation:

- `"Inter", "Segoe UI", sans-serif`

Почему:

- нейтральна и привычна для интерфейсов;
- хорошо держит маленькие размеры;
- подойдет и для web, и для будущего macOS wrapper stage.

Использование:

- body text;
- article copy;
- HUD labels;
- navigation;
- button labels;
- metadata.

### 3. Mono / Analytical Family

Для hand history, spot IDs, ranges, stack sizes и технических чисел:

- `"JetBrains Mono", "SFMono-Regular", "Menlo", monospace`

Использование ограниченное:

- hand history lines;
- chip/stack values в debug или analysis states;
- internal IDs и compact table data.

Не использовать mono для длинного body copy или крупных hero screens.

## Type Scale

### Desktop Scale

- `display-hero`: 60/64, weight 800, letter-spacing -0.03em
- `display-section`: 42/46, weight 780, letter-spacing -0.02em
- `heading-1`: 32/38, weight 760
- `heading-2`: 26/32, weight 740
- `heading-3`: 22/28, weight 720
- `title-card`: 18/24, weight 700
- `body-lg`: 18/30, weight 450
- `body`: 16/26, weight 450
- `body-sm`: 14/22, weight 450
- `label`: 13/18, weight 700, letter-spacing 0.02em
- `caption`: 12/16, weight 600
- `micro`: 11/14, weight 650, letter-spacing 0.04em

### Mobile Scale

- `display-hero-mobile`: 38/42, weight 800, letter-spacing -0.025em
- `display-section-mobile`: 30/34, weight 760
- `heading-1-mobile`: 24/30, weight 740
- `heading-2-mobile`: 21/27, weight 720
- `heading-3-mobile`: 18/24, weight 700
- `body-mobile`: 16/24, weight 450
- `body-sm-mobile`: 14/21, weight 450
- `label-mobile`: 13/18, weight 700
- `caption-mobile`: 12/16, weight 600

## Font Weight Rules

- 800: только hero, major level result, key statements.
- 760-780: section headings и important card titles.
- 700-720: nav, buttons, HUD labels, stat titles.
- 450-500: body copy и explanations.
- 600-650: captions, metadata, uppercase labels.

Нельзя делать весь экран semi-bold. Для poker UI плотность должна рождаться от контраста размеров и spacing, а не от сплошного жирного текста.

## Line Length And Reading Rules

- Hero copy: максимум 10-12 слов в строке на desktop.
- Section intro: 55-72 символа в строке.
- Article body: 60-76 символов в строке.
- HUD explanations: 28-40 символов в строке.
- Mobile article body: избегать строк длиннее 38-42 символов в среднем.

Для длинных объяснений AI лучше давать 2-4 коротких абзаца, чем одну длинную стену текста.

## Density Modes

Продукту нужны три режима плотности, а не один универсальный.

### 1. Immersive Table Density

Для hero with poker table, live training table, diagnostic session:

- вертикальные gap: 12, 16, 20;
- card padding: 16-20;
- controls height: 44-52;
- captions компактные;
- surrounding text минимален.

Цель: максимум внимания на решение игрока и состояние стола.

### 2. Analytical HUD Density

Для score breakdown, coach notes, level result, hand review:

- вертикальные gap: 10, 12, 16;
- card padding: 14-18;
- data rows: 36-44 height;
- chip/badge elements компактные, но не микроскопические.

Цель: уместить больше аналитики без ощущения тесноты.

### 3. Reading Density

Для rules pages, glossary, strategy articles, tournament/news summaries:

- вертикальные gap: 18, 24, 32;
- paragraph spacing: 14-18;
- content cards padding: 20-28;
- длинные тексты держать в более спокойном ритме.

Цель: не тащить игровую плотность в длинный обучающий контент.

## Spacing Scale

Базовая scale:

- `4`
- `8`
- `12`
- `16`
- `20`
- `24`
- `32`
- `40`
- `48`
- `64`
- `80`

Правило:

- 4/8 использовать внутри chips, icons, inline label groups;
- 12/16/20 использовать для form controls, metric rows, compact cards;
- 24/32 использовать для section internals;
- 40/48/64 использовать для page rhythm;
- 80 только для desktop hero separations.

## Component Sizing Guidance

### Navigation

- desktop nav item height: 40-44
- mobile nav touch target: минимум 44
- header height desktop: 72-80
- header height mobile: 60-68

### Buttons

- primary desktop: height 48
- primary mobile: height 48-52
- compact secondary: height 40-44
- icon-only touch target: минимум 44x44

### Cards And Panels

- compact card radius: 14
- standard panel radius: 18
- hero/table surface radius: 24
- dense stat card padding: 14-16
- content card padding: 20-24

### Inputs And Choice Controls

- segmented choice height: 44-48
- quiz answer tile min-height: 52
- bottom action bar mobile: 56-64

## Surface-Specific Rules

### Desktop Web

- можно использовать двухколоночные композиции с плотным analytics rail;
- hero и result screens могут держать крупный display scale;
- side panels и HUD могут идти в analytical density mode;
- reading surfaces должны иметь отдельную content width, а не растягиваться на весь экран.

### Mobile Web

- headline scale нужно резко ужимать, но не терять характер;
- action cluster должен оставаться в пределах большого пальца;
- chips, labels и captions нельзя делать меньше 12px в критичных состояниях;
- если на экране есть board, hand, stack и CTA, secondary metadata нужно сворачивать или переносить вниз.

### Telegram Mini App

- использовать только compact subsets type scale;
- headline максимум уровня `heading-1-mobile`, без огромных display-зон;
- минимум декоративных текстовых блоков;
- primary focus на short diagnosis, result summary и next lesson CTA.

### macOS App

- можно сохранить desktop scale, но чуть уменьшить vertical whitespace;
- sidebar, history list и session launcher должны быть плотнее, чем marketing-like web sections;
- mono style полезен для hand history, stack details и review tables.

## Current Site Migration Notes

Сейчас `assets/styles.css` использует:

- `Inter` как единственную family;
- светлый SaaS rhythm;
- hero `54px`;
- radius `8px`;
- относительно воздушные секции и B2B copy rhythm.

Для poker platform migration нужно:

- добавить dual family model: Manrope for display, Inter for UI/body;
- увеличить distinction между hero / section / HUD / article scales;
- поднять border radius на surface-компонентах;
- сделать игровые и аналитические блоки плотнее, чем контентные статьи;
- не переносить текущую white-space model в diagnostic table screens.

## CSS Token Draft

```css
:root {
  --font-display: "Manrope", "Inter", "Segoe UI", sans-serif;
  --font-ui: "Inter", "Segoe UI", sans-serif;
  --font-mono: "JetBrains Mono", "SFMono-Regular", "Menlo", monospace;

  --text-hero: 60px;
  --text-h1: 32px;
  --text-h2: 26px;
  --text-h3: 22px;
  --text-body-lg: 18px;
  --text-body: 16px;
  --text-body-sm: 14px;
  --text-label: 13px;
  --text-caption: 12px;

  --leading-hero: 1.06;
  --leading-heading: 1.2;
  --leading-body: 1.6;
  --leading-dense: 1.4;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-7: 32px;
  --space-8: 40px;
  --space-9: 48px;
  --space-10: 64px;

  --radius-sm: 14px;
  --radius-md: 18px;
  --radius-lg: 24px;
  --control-height-sm: 40px;
  --control-height-md: 48px;
  --control-height-lg: 52px;
}
```

## Decision Summary

Step 14 считается закрытым, если команда зафиксировала:

- primary display family и UI/body family;
- отдельный mono style для analytical states;
- desktop/mobile type scale;
- три режима плотности: table, HUD, reading;
- spacing and sizing rules для четырех поверхностей;
- понятный migration path от текущего светлого B2B front-end к poker training UI.
