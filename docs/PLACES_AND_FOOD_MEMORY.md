# FUL.HOUSE — Places & Food Memory

## Core idea

FUL.HOUSE should remember not only what the user cooks, but where they actually eat, what they order, which dishes they love, and the context around those experiences.

The system should build a private-first personal food and place memory from explicitly authorized signals such as location history, restaurant visits, delivery history, shared links, receipts, photos, calendar context, manual notes and connected services where APIs permit.

The priority order for recommendations should be:

1. User's own history and explicit preferences.
2. Trusted household/family/friend recommendations where permitted.
3. External discovery and public ratings.

The product should know the user's taste, not merely repeat the internet's average rating.

---

## Core entities

### Place
A physical venue such as restaurant, cafe, bakery, bar, market or food court.

### Visit
A specific real-world visit with timestamp, duration where available, companions/context if explicitly known, dishes, notes, photos and user feedback.

### Order
A delivery or takeaway event, including provider, restaurant, dishes, frequency, price where available and explicit feedback.

### Dish
The central food identity object linking restaurants, delivery, Kitchen recipes and personal taste.

Example Dish graph:

Tom Yum
- Cooked at home × 4
- Ordered × 11
- Restaurant visits × 3
- Saved recipes × 6
- Loved: yes

---

## Location-assisted place memory

With explicit user permission, FUL.HOUSE can receive device location signals and map-match them against known places.

The system should not treat every GPS coordinate as a meaningful event. It should infer candidate visits from dwell time, repeated presence, map place boundaries and contextual evidence.

Example:

> You were at Afsona for about 1 hour 12 minutes yesterday. Save this as a restaurant visit?

Repeated visits can create stronger confidence:

> You've been here three times recently. Would you like me to remember this as one of your regular places?

Raw location history is private by default and should never become publicly visible merely because location access was granted.

Location permission and public sharing are separate decisions.

---

## Data sources

Potential sources, subject to platform/API availability and explicit user authorization:

- Device location history
- Google Maps / Apple Maps saved places or history where available
- Food delivery services
- Restaurant reservation services
- Instagram / social posts with place information
- Photos with location metadata
- Receipts
- Email confirmations
- Calendar events
- Bank transaction descriptions when explicitly connected
- URLs shared to FUL.HOUSE
- Manual Butler conversations

Example:

> Butler, I loved the plov at this place yesterday.

The Butler should resolve the likely Place from recent location context, ask for confirmation when uncertain, and create the Visit + Dish memory.

---

## Taste memory

The system should learn from explicit signals rather than treating every purchase as preference.

Possible feedback:

- Loved
- Liked
- Okay
- Disliked
- Would order again
- Would visit again
- Favorite

It can also learn soft signals such as repeated ordering, but should distinguish inferred preference from explicit preference.

Example:

> You've ordered Pepperoni from this restaurant 9 times. Should I mark it as a favorite?

---

## Context memory

Places can be useful for different situations.

Possible contexts:

- Family
- Date
- Business
- Fast lunch
- Breakfast
- Delivery
- Late night
- Celebration
- Coffee/work
- Travel

This enables personal recommendations such as:

> Where should we go with the family tonight?

The Butler should prefer known successful places matching the context before generic web discovery.

---

## Kitchen connection

Dish is the bridge between Places and Kitchen.

Restaurant → Dish → Memory → Kitchen → Recipe

Example:

> I want to cook something like the pasta I had there last month.

FUL.HOUSE can retrieve the Place, Visit, Dish, photos/menu description if available, then create a clearly labeled home interpretation. It must not claim to possess the restaurant's original recipe unless that recipe was actually published or provided.

Reverse direction:

Kitchen Recipe → Taste → Restaurant/Delivery discovery

Example:

> Find something I can order that tastes similar to the chicken I cooked yesterday.

---

## Delivery memory

FUL.HOUSE should understand repeat ordering patterns where authorized.

Example restaurant memory:

Bellissimo Pizza
- Ordered 14 times
- Frequent: Pepperoni, Caesar, Cola Zero
- Typical context: late evening

The Butler can answer:

> What do I usually order from here?

or eventually assist with reordering through supported provider integrations.

Purchases must always require appropriate user confirmation.

---

## Social layer

Users may optionally publish selected recommendations as part of their House.

Example:

Stan recommends in Tashkent
- 5 restaurants
- 3 coffee shops
- 2 breakfast places

Public recommendations should be deliberately selected. Private visit history and raw location data remain private.

This allows visitors to discover places through people whose taste they know rather than anonymous aggregate ratings alone.

---

## House representation

Potential spatial representations:

- Dining Room
- Map Table
- World map wall
- Restaurant memory shelf
- Travel food albums
- Favorite dishes book

Places are functional objects, not decoration. Opening a Place can show selected visits, dishes, photos, notes and recommendation status.

---

## Archive and inheritance

Selected place memories can become part of the House Archive and, if the owner permits, inheritance.

Examples:

- Places Dad Loved
- Family restaurants
- First-date restaurant
- Favorite cafe in Istanbul
- Childhood bakery

A place can remain in the family archive even if the real business later closes.

Raw historical location trails should not automatically transfer to heirs. Inheritance should operate on explicitly preserved memories/places rather than unrestricted surveillance history.

---

## Privacy principles

1. Location access is opt-in.
2. Raw location is private by default.
3. Granting location access never means public sharing.
4. Candidate visits can require confirmation depending on confidence and user settings.
5. Sensitive locations should receive additional protection and should not be surfaced casually.
6. Users can delete visits, places and raw history.
7. Inferred preferences must be distinguishable from explicit user preferences.
8. Public recommendations are separately selected.

---

## MVP

1. Manual place/dish addition.
2. Share URL/photo/receipt to FUL.HOUSE.
3. AI resolves candidate restaurant and dishes.
4. Loved / Okay / Disliked feedback.
5. Place + Visit + Dish data model.
6. Kitchen linkage.
7. Butler can answer questions from saved food memory.
8. Optional foreground/recent location-assisted suggestion where platform permissions allow.

Later phases can add continuous location intelligence, delivery integrations, reservation history and automated discovery.

---

## Key principle

**FUL.HOUSE should remember where your real life happened, but the owner controls what becomes a memory and what remains private data.**