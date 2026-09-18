# FUL.HOUSE — Kitchen & Recipe Intelligence

## Core idea

The FUL.HOUSE kitchen should not be a generic recipe library. It should be a personalized culinary space generated from the user's real interests, saved content, cooking behavior and family history.

**Your kitchen should remember what you actually like to eat.**

The system can ingest cooking-related content the user explicitly connects or shares, extract recipes, normalize them into usable cooking instructions, calculate nutrition, learn preferences over time and turn saved recipes into persistent objects inside the digital house.

---

## Product principle

FUL.HOUSE should prefer the user's existing food interests over generic discovery.

The system should answer:

> What have I already seen, saved, liked, cooked and enjoyed?

before answering:

> What random recipe exists on the internet?

The kitchen becomes a personal food memory rather than another content feed.

---

## How the kitchen appears

The Kitchen can be created in several ways:

1. AI detects a strong cooking/food interest from authorized sources.
2. User explicitly unlocks a Kitchen.
3. User saves the first recipe into FUL.HOUSE.
4. Food-related activity across connected sources reaches a threshold and the Butler suggests creating one.

Example Butler message:

> You save a lot of cooking videos. Would you like me to build you a kitchen and organize the recipes?

The user must approve before private source data is imported into the room.

---

# 1. Supported recipe sources

The Kitchen should be able to ingest recipes from multiple user-authorized sources.

Possible inputs:

- Shared video URL
- Shared social post URL
- Saved/liked cooking content where platform APIs permit access
- YouTube cooking videos
- Instagram/Reels content where access is available
- TikTok cooking content where access is available
- Pinterest content where access is available
- Web pages
- Plain text
- Messages
- Screenshots
- Photos of printed recipes
- Photos of handwritten recipes
- PDFs/documents
- Manual dictation
- Voice notes

The product must not assume APIs expose full viewing/like histories. Source capabilities differ and can change. The ingestion architecture should therefore support both connected-account imports and explicit share-to-FUL workflows.

---

# 2. Recipe extraction pipeline

Every imported item is processed through a structured recipe pipeline.

**Source → Content extraction → Recipe detection → Ingredient extraction → Quantity normalization → Step extraction → Cooking metadata → Nutrition → Personal recipe record**

### Recipe detection

The system first decides whether the source actually contains a recipe.

Possible outcomes:

- Complete recipe
- Partial recipe
- Cooking inspiration without enough detail
- Restaurant/food recommendation rather than a recipe
- Not food related

Do not fabricate a complete recipe when the source does not provide enough evidence without marking estimates clearly.

---

# 3. Ingredient normalization

Social cooking content is often imprecise:

- "a little oil"
- "some cream"
- "one cup"
- "a handful"
- "season to taste"

FUL.HOUSE should turn this into a usable standardized representation.

Example normalized ingredient:

```text
Chicken breast — 400 g
Olive oil — 10 g
Cream 20% — 150 g
Parmesan — 40 g
Salt — 4 g
Black pepper — 1 g
```

### Important provenance rule

Every quantity should carry a source/provenance state such as:

- SOURCE_EXACT
- SOURCE_APPROXIMATE
- AI_ESTIMATE
- USER_CORRECTED

Example UI:

> Cream — ~150 g  
> AI estimate based on video

This prevents false precision.

---

# 4. Unit conversion

Recipes should be normalizable into the user's preferred measurement system.

Examples:

- grams
- kilograms
- milliliters
- liters
- teaspoons
- tablespoons
- cups
- ounces
- pounds

The user can select a default system, but the original measurement should be preserved.

For ambiguous ingredients, conversions should use ingredient-specific density only when reliable data exists.

---

# 5. Portion scaling

Every structured recipe should support automatic scaling.

Example:

Original: 4 portions

User selects: 2 portions

FUL.HOUSE recalculates:

- ingredient quantities
- total calories
- per-portion calories
- macro totals

Recipes should preserve practical cooking constraints. For example, "1 egg" should not blindly become "0.25 egg" without offering a sensible interpretation.

---

# 6. Nutrition

Nutrition calculation should use a structured food/nutrition data source rather than allowing the language model to invent calorie values.

The model's role is to identify and map ingredients. A deterministic nutrition layer should calculate totals.

Possible output:

```text
Total: 1,484 kcal
Per portion: 371 kcal
Protein: 42 g
Fat: 18 g
Carbohydrates: 12 g
```

Optional future values:

- fiber
- sugar
- sodium
- saturated fat
- micronutrients

### Confidence

Nutrition should support confidence indicators where ingredient identity or quantity is uncertain.

For example:

> Estimated nutrition — two ingredient quantities were inferred from the video.

---

# 7. Step-by-step recipe generation

The Kitchen should convert messy source content into clear cooking instructions.

Each step can include:

- ingredient quantity used at this step
- preparation action
- temperature
- duration
- visual cue
- timer
- equipment

Example:

### Step 3 of 8

Heat a pan over medium-high heat.
Add 10 g olive oil.
Add 400 g chicken and cook for approximately 4 minutes until browned on the first side.

`START 4:00 TIMER`

The step sequence should distinguish source-derived instructions from AI-reconstructed steps when necessary.

---

# 8. Cook with Butler mode

The AI Butler becomes a cooking assistant.

Possible interaction:

> Butler, start the chicken recipe.

Butler:

> Step 1 of 8. Cut 400 g of chicken breast into bite-sized pieces.

When ready:

> Next.

Butler:

> Heat the pan. Add 10 g of oil. I'll start a four-minute timer when you say ready.

Capabilities:

- hands-free step navigation
- timers
- ingredient reminders
- quantity conversion
- substitution suggestions
- portion scaling
- repeat last instruction
- explain a cooking technique
- keep the screen in cooking mode

The Butler should remain useful offline for saved recipes and local recipe memory where device capabilities permit.

Cloud AI can optionally assist with more difficult interpretation or substitutions.

---

# 9. Personal culinary memory

Saving is not enough. FUL.HOUSE should learn what the user actually cooks and enjoys.

Each recipe can have behavioral states:

- Seen
- Saved
- Cooked
- Loved
- Would cook again
- Disliked
- Modified
- Family favorite

The Kitchen can learn patterns such as:

- preferred cuisines
- common ingredients
- disliked ingredients
- preferred cooking duration
- spice tolerance
- vegetarian/vegan preferences
- allergies explicitly provided by the user
- typical serving size
- weekday vs weekend cooking behavior

Example Butler inference:

> You often save one-hour recipes but rarely cook them. Most of the dishes you repeat take under 30 minutes.

This should be treated as a soft preference, not an immutable profile.

---

# 10. Personal corrections make recipes better

If AI estimates an ingredient incorrectly, the user's correction becomes part of the personal recipe.

Example:

AI:

> 150 g cream

User:

> I actually use 100 g.

The system should save the modified version without altering the source record.

Possible states:

- Original extracted recipe
- User version
- Household/family version

This allows recipes to evolve naturally.

---

# 11. What's in my fridge?

A future Kitchen capability should match available ingredients against the user's personal recipe collection.

Example:

> I have chicken, eggs, tomatoes and cheese.

Butler:

> You have three saved recipes that fit. One is the chicken dish you saved from Instagram four months ago.

The priority order should be:

1. User's saved/cooked recipes
2. Household/family recipes
3. Trusted external recipe sources
4. Newly generated recipes, if allowed

The system should avoid presenting hallucinated recipes as previously saved content.

---

# 12. Ingredient substitutions

The Butler can suggest substitutions based on:

- available ingredients
- dietary restrictions
- user's past substitutions
- recipe structure

Examples:

- cream → yogurt where appropriate
- parmesan → another hard cheese
- chicken → tofu when recipe structure supports it

Substitutions should warn when they materially change cooking time, texture, allergens or nutrition.

---

# 13. Dietary and health preferences

The Kitchen may support explicit user preferences such as:

- calorie target
- protein target
- low sodium
- vegetarian
- vegan
- halal
- kosher
- allergies
- intolerances

These are sensitive personal settings and should never be inferred as medical facts from casual behavior.

FUL.HOUSE can personalize recipes around declared preferences, but should not position itself as medical nutrition treatment without an appropriate medical product layer.

---

# 14. Kitchen as a room

Recipes should have spatial representation inside the house.

Possible objects:

- Recipe book → personal recipe collection
- Fridge → ingredients/inventory
- Pantry → staple ingredients
- Counter → currently selected recipe
- Oven/stove → Cook with Butler mode
- Family shelf → inherited recipes
- Photo frame → food memories
- Shopping note → grocery list

The room must remain functional rather than decorative.

---

# 15. Recipe objects

A recipe is a first-class FUL.HOUSE object.

Possible fields:

```text
id
owner_id
household_id
title
source_type
source_url
source_media_reference
source_author
source_original_text
ingredients[]
steps[]
portions
nutrition
nutrition_confidence
cuisine
tags
prep_time
cook_time
total_time
user_rating
status
created_at
last_cooked_at
visibility
provenance
```

Ingredients should preserve both normalized and original quantities.

---

# 16. Food video understanding

Video ingestion can combine:

- captions/transcript
- visible on-screen text
- description
- detected ingredients/objects
- timestamps
- audio speech

The extraction system should prefer explicit evidence.

Example:

Transcript says "two eggs" → high confidence.

Video appears to show cream but quantity is unknown → ingredient high confidence, quantity low confidence.

This distinction matters.

---

# 17. Save from social media

The ideal user action is extremely small.

Possible workflow:

`Share → FUL.HOUSE → Save to Kitchen`

The Butler then processes the content in the background of the user experience and later reports:

> I extracted the recipe. The creator didn't specify how much cream was used, so I estimated 150 g. Want to keep that?

Where platform integrations support saved/liked content, the Kitchen may also offer controlled imports.

It should never silently ingest a user's entire social history.

---

# 18. Family recipes

The Kitchen becomes particularly valuable when linked with House inheritance.

Users can add:

- handwritten recipes
- old family cookbooks
- photographs of recipe cards
- voice recordings
- family notes

Example:

A photo of a grandmother's handwritten recipe is uploaded.

FUL.HOUSE creates:

1. Original scan
2. Transcription
3. Structured ingredient list
4. Step-by-step version
5. Optional nutrition calculation

The original artifact is always preserved alongside the normalized version.

---

# 19. Inheritance

Kitchen memory can transfer with the house according to inheritance permissions.

Potential inherited items:

- Family recipes
- User-created recipes
- Recipe modifications
- Food memories
- Historical cooking notes
- Family favorite collections

This can create multigenerational culinary archives.

Example future view:

```text
Family Kitchen
├── Grandmother's recipes
├── Dad's favorites
├── Mom's baking
└── My recipes
```

This is a stronger emotional artifact than a generic recipe cloud account.

---

# 20. Privacy

Food preferences can reveal sensitive information.

Rules:

1. Saved recipe history is private by default.
2. Connected likes/viewing history is private by default.
3. Dietary settings are private by default.
4. Allergies are never publicly exposed automatically.
5. Individual recipes can be published or shared explicitly.
6. Family recipes can have household-only visibility.
7. Source provenance should remain available to the owner.

---

# 21. Public sharing

Users may explicitly publish selected recipes inside their house.

A visitor can enter the Kitchen and see only approved public objects.

Possible future interactions:

- View recipe
- Save a copy to own Kitchen
- Buy a premium recipe/collection using VIRT
- Follow a cook/creator
- Request a cooking service/class

This can connect Kitchen to the broader FUL.HOUSE work marketplace later.

---

# 22. Marketplace potential

Possible future real work/products:

- Chef recipe collections
- Personalized meal plans
- Cooking classes
- Nutrition-aware recipe adaptation
- Family cookbook digitization service
- Premium cooking guides

VIRT can be used inside the platform for these products if marketplace rules permit.

This is deliberately not part of the first Kitchen MVP.

---

# 23. Core loops

## Discovery loop

See cooking content → send/save to FUL.HOUSE → recipe extracted → Kitchen grows.

## Cooking loop

Choose saved recipe → Cook with Butler → mark Cooked/Loved/Modified → personal model improves.

## Memory loop

Cook recipe repeatedly → modifications accumulate → recipe becomes household version → eventually becomes part of family history.

## Personalization loop

Save → cook → rate → modify → Butler learns → recommendations improve.

---

# 24. MVP

The first Kitchen version should prove one thing:

**Can FUL.HOUSE reliably turn messy food content into a recipe the user actually wants to cook again?**

MVP scope:

1. Save recipe from URL, text or shared video.
2. Extract title and ingredients.
3. Normalize quantities into grams/ml where possible.
4. Preserve uncertainty/provenance.
5. Generate clear cooking steps.
6. Calculate calories and basic macros using structured nutrition data.
7. Scale portions.
8. Save recipe to Kitchen.
9. Cook with Butler step mode.
10. Mark Cooked / Loved / Disliked / Modified.
11. Store preference signals locally/personal memory where possible.
12. Keep recipes private by default.

Not required for MVP:

- full fridge inventory automation
- grocery delivery integration
- automatic weekly meal plans
- medical diet plans
- public recipe marketplace
- full social-platform history ingestion

---

# 25. Long-term direction

The Kitchen can become a personal food agent that understands:

- what the user watches
- what they save
- what they actually cook
- what they enjoy
- what they avoid
- how much time they normally spend cooking
- what exists in the household pantry
- family culinary history

The end state is not:

> Here are ten popular chicken recipes.

It is:

> You have chicken in the fridge. You usually want dinner in under 30 minutes. Here are two dishes you've cooked and liked before, plus one recipe you saved last week and haven't tried yet.

That is the difference between a recipe search engine and a house that actually knows its owner.
