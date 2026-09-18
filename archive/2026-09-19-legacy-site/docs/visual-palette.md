# Visual Palette

Дата: 2026-07-05
Шаг: 13. Собрать визуальную палитру

## Цель

Зафиксировать темную палитру для AI poker training platform так, чтобы интерфейс ощущался как poker room + training lab, но не скатывался в casino neon. Палитра должна работать для desktop web, mobile web, Telegram Mini App и будущего macOS app.

## Арт-дирекшн

- Основа: глубокий черный и графит вместо светлого B2B-интерфейса текущего сайта.
- Пространство: темные слои с ощущением стола, сукна, аналитической панели и HUD.
- Акценты: felt green как основной product accent, chip red для ошибок/pressure states, muted gold для прогресса, рангов и premium-like emphasis без обещаний выигрыша.
- Режим использования: 80-85% интерфейса должны оставаться темными и нейтральными; цвет нужен для иерархии, статусов и CTA, а не для постоянного свечения.

## Core Tokens

### Neutrals

- `--bg-canvas: #05070b` - самый глубокий фон сайта и app shell.
- `--bg-elevated: #0b1220` - основной приподнятый слой, панели и секции.
- `--bg-surface: #101826` - карточки, drawers, info blocks.
- `--bg-surface-2: #162133` - hover/secondary panels/HUD modules.
- `--bg-inset: #1b2a1f` - приглушенный felt-backed inset для зон стола.
- `--line-soft: rgba(255, 255, 255, 0.08)` - тонкие границы.
- `--line-strong: rgba(148, 163, 184, 0.24)` - контуры активных областей.

### Text

- `--text-primary: #f5f7fb` - основной текст на темном фоне.
- `--text-secondary: #c7d2e0` - вторичный текст, описания.
- `--text-muted: #8b9aaf` - captions, metadata, timestamps.
- `--text-disabled: #5d697b` - disabled states.
- `--text-on-accent: #f8fafc` - текст на насыщенных CTA.

### Poker Accents

- `--felt-green: #0f8a5f` - главный брендовый accent для primary CTA и active states.
- `--felt-green-deep: #0a5f43` - pressed/hover состояние и плотные плашки.
- `--felt-green-glow: rgba(15, 138, 95, 0.28)` - мягкое свечение вокруг активного training focus.
- `--chip-red: #c44536` - ошибки, pressure spots, danger states.
- `--chip-red-deep: #8f2e24` - pressed/dense error states.
- `--gold: #d4a63a` - progress, rank, lesson unlock, trophy meta.
- `--gold-dim: #8d6a1d` - muted gold для outline/badge states.

### Utility States

- `--info-blue: #4d7cff` - informational system messages и neutral tips.
- `--success: #18b26b` - completion/safe confirmation.
- `--warning: #e6a23c` - caution without panic.
- `--danger: #d05a4e` - destructive/system warnings.

## Surface Mapping

### 1. Poker Table Layer

- стол и игровые области должны опираться на `--bg-canvas`, `--bg-elevated`, `--bg-inset`;
- felt green используется локально: betting ring, active seat halo, confirm CTA, progress strips;
- gold только как secondary highlight: rank badge, streak, learning milestone;
- red только для mistake review, risk marker и fold-pressure annotation.

### 2. Training Lab Layer

- диагностический HUD, side panels и score breakdowns должны быть графитовыми, а не зелеными;
- charts, score pills и focus states используют green/gold/red экономно;
- нейтральный фон должен оставаться темнее контента, чтобы карточки и карты не терялись.

### 3. Content Layer

- статьи, glossary, rules pages и tournament/news blocks требуют highest readability:
- body copy на `--text-primary`, supporting copy на `--text-secondary`;
- длинные тексты не должны сидеть на чистом черном фоне, лучше `--bg-elevated` или `--bg-surface`;
- ссылки и inline emphasis используют felt green, а не red/gold.

## Recommended Gradients

- Hero/table backdrop:
  `linear-gradient(180deg, #040609 0%, #07111a 42%, #0b1c17 100%)`
- CTA/button accent:
  `linear-gradient(135deg, #0f8a5f 0%, #0a5f43 100%)`
- Premium/rank accent:
  `linear-gradient(135deg, #d4a63a 0%, #8d6a1d 100%)`
- Danger/review accent:
  `linear-gradient(135deg, #c44536 0%, #8f2e24 100%)`

## Usage Rules

- Не использовать яркий casino-style neon green на больших плоскостях.
- Не смешивать green, red и gold в одном компоненте без явной роли.
- Primary CTA в одном viewport должен быть один; secondary CTA лучше делать outline/graphite.
- Красный не использовать для мотивационных CTA, только для risk/error/review semantics.
- Золото не использовать для цены, денег или payout-ассоциаций.
- На мобильном не опираться на subtle glow как единственный indicator состояния: нужен контраст по заливке, бордеру или тексту.

## Accessibility And Contrast

- Основной текст должен держать высокий контраст на `--bg-elevated` и `--bg-surface`.
- Мелкий текст на mobile не использовать в `--text-muted`, если блок критичен для понимания hand result или next action.
- Green CTA и red review states должны иметь читаемый текст без reliance на цвет alone.
- Границы интерактивных зон на mobile и Telegram Mini App должны быть заметны даже при плохой яркости экрана.

## Surface Notes

### Desktop web

- Можно использовать более глубокие фоновые градиенты, крупные table backdrops и layered shadows.
- В широком layout палитра должна помогать разделять table, HUD и content rail.

### Mobile web

- Темные слои должны быть упрощены: меньше одновременных оттенков в одном экране.
- Primary green CTA и red review labels должны быть крупнее и контрастнее, чем на desktop.

### Telegram Mini App

- Нужен сокращенный набор токенов: `bg-canvas`, `bg-surface`, `text-primary`, `text-secondary`, `felt-green`, `chip-red`, `gold`.
- Избегать тяжелых градиентов и длинных glow-цепочек, чтобы интерфейс оставался быстрым.

### macOS app

- Палитра должна переноситься в desktop-client без ощущения web skin.
- Graphite surfaces и subdued gold подходят для sidebar, session history и compact desktop chrome.

## Migration Note From Current Site

Текущий сайт использует светлую B2B-палитру с teal/amber на белом фоне. Для poker-платформы сохраняется идея green + warm accent, но:

- белый фон уходит из базовой схемы;
- teal смещается в felt green;
- amber смещается в muted gold;
- графит становится основой UI, а не вспомогательным цветом;
- контентные и игровые слои получают отдельные темные поверхности.

## Initial CSS Variable Draft

```css
:root {
  --bg-canvas: #05070b;
  --bg-elevated: #0b1220;
  --bg-surface: #101826;
  --bg-surface-2: #162133;
  --bg-inset: #1b2a1f;
  --line-soft: rgba(255, 255, 255, 0.08);
  --line-strong: rgba(148, 163, 184, 0.24);
  --text-primary: #f5f7fb;
  --text-secondary: #c7d2e0;
  --text-muted: #8b9aaf;
  --text-disabled: #5d697b;
  --text-on-accent: #f8fafc;
  --felt-green: #0f8a5f;
  --felt-green-deep: #0a5f43;
  --felt-green-glow: rgba(15, 138, 95, 0.28);
  --chip-red: #c44536;
  --chip-red-deep: #8f2e24;
  --gold: #d4a63a;
  --gold-dim: #8d6a1d;
  --info-blue: #4d7cff;
  --success: #18b26b;
  --warning: #e6a23c;
  --danger: #d05a4e;
}
```
