# FUL.HOUSE — Digital Wardrobe & Personal Stylist

## Core idea

The FUL.HOUSE wardrobe should digitize the user's real clothes, shoes, watches, bags, jewelry and accessories, then use that inventory to help the owner decide what to wear, what to buy, what to care for, what is missing and what is rarely used.

It is not a fashion mood board and not a generic AI stylist.

**It should know what the user actually owns.**

The Wardrobe becomes another real-life subsystem of the House, generated from the owner's actual belongings and habits.

---

## Core principle

FUL.HOUSE should prefer real inventory over fictional catalog content.

The system should answer:

> What can I wear from things I already own?

before answering:

> What else can I buy?

Recommendations become useful because they are constrained by the user's actual wardrobe, body/fit preferences, weather, calendar context and personal style.

---

## How items are digitized

Users can add items through:

- Photo of a single item
- Several photos from different angles
- Short video
- Photo of the user wearing the item
- Screenshot/product link
- Purchase receipt/email
- Barcode/QR where useful
- Manual entry

AI can extract or infer candidate metadata such as:

- Category
- Brand
- Model/product name
- Color
- Pattern
- Material
- Size
- Fit
- Season
- Formality
- Condition
- Purchase date
- Price where available
- Care instructions

Inferred fields must be distinguishable from confirmed values.

---

## Real digital object

Each real item becomes a functional object in the Wardrobe.

Example:

Navy wool blazer
- Brand: Canali
- Size: 50
- Purchased: 2026
- Condition: good
- Last worn: 12 days ago
- Worn: 23 recorded times
- Dry clean only
- Works well with: 8 saved combinations

The visual object can be stylized to match House art direction, but should remain recognizable.

---

## Wardrobe zones

Possible physical sections:

- Jackets/coats
- Shirts/tops
- Trousers/jeans
- Dresses/skirts
- Shoes
- Watches
- Jewelry
- Bags
- Accessories
- Sportswear
- Formalwear
- Seasonal storage
- Laundry/care area

The user should not need to manually build these categories if AI can organize them reliably.

---

## Personal stylist

The Butler can act as a stylist over the user's actual inventory.

Examples:

> What should I wear tonight?

> I have a business dinner. Give me three options.

> What works with these shoes?

> Build an outfit around this jacket.

> I don't want to wear black today.

> Give me something casual under 30°C weather.

The system should consider authorized context such as:

- Weather
- Calendar/event type
- Location
- Time of day
- Dress code
- User's historical preferences
- Recent outfit repetition
- Laundry/availability status

---

## Outfit memory

FUL.HOUSE can save complete outfits as combinations.

Possible signals:

- User manually saves outfit
- User photographs outfit
- Calendar + wardrobe selection
- User marks outfit as liked/disliked
- User notes compliment/comfort problems

Example outfit:

Business dinner
- Navy blazer
- White shirt
- Grey trousers
- Brown loafers
- Steel watch

Feedback:
- Comfortable: yes
- Would wear again: yes
- Context: dinner/business

The Butler gradually learns combinations the owner actually likes.

---

## Wear history

Optional wear tracking can help answer:

> When did I last wear this?

> Which clothes do I never use?

> Am I repeating this outfit too often this week?

> Which shoes have I worn most this year?

Tracking should be lightweight and privacy-first. It may come from user confirmation, outfit photos or explicit selection rather than constant camera inference.

---

## Fit and body preferences

The Wardrobe may store user-controlled fit preferences such as:

- Preferred sizes by brand/category
- Tight/regular/oversized preference
- Sleeve/trouser length preferences
- Shoe sizing by brand
- Alteration notes

Sensitive body measurements should remain private and optional.

The goal is practical fit assistance, not body judgment.

---

## Shopping assistant

A future online Butler can help evaluate purchases against the existing wardrobe.

Example:

> Do I need these shoes?

Butler:

> You already own two very similar brown loafers. This pair would mostly duplicate them.

Or:

> This jacket would work with 11 items you already own and fills a gap in your lighter formalwear.

This creates a strong anti-impulse-shopping utility rather than merely another affiliate funnel.

If commerce is added, recommendations should clearly distinguish user benefit from sponsored/affiliate content.

---

## Care and maintenance

The Wardrobe can remember how items should be maintained.

Examples:

- Dry cleaning
- Washing temperature
- Leather care
- Shoe polishing
- Watch servicing
- Jewelry maintenance
- Seasonal storage

Butler examples:

> These shoes haven't been conditioned in six months.

> This blazer is marked dry-clean-only.

> Your winter coats can move to seasonal storage.

Care instructions should come from confirmed garment labels/product data where possible rather than unsupported AI guesses.

---

## Laundry state

Optional item state:

- Ready
- Worn / needs wash
- Laundry
- Dry cleaning
- Repair
- Storage
- Lent out

This makes recommendations operationally useful.

The Butler should not recommend the perfect shirt if it is currently at the dry cleaner, a small but apparently controversial requirement for software designers.

---

## Repair and tailoring

Items can have maintenance history:

- Altered sleeves
- Replaced buttons
- Shoe repair
- Watch service
- Jewelry repair

Life Map can optionally remember preferred tailor, cobbler, cleaner or watch service after confirmed visits.

---

## Calendar and weather integration

Strong cross-system loop:

Calendar + Location + Weather + Wardrobe → Outfit recommendation

Example:

> Tomorrow: 31°C, outdoor lunch, then business meeting.

The Butler can suggest an outfit using real owned items and explain why.

Cloud/current-data mode can supply weather when internet is available, while core inventory and preference reasoning remain local where possible.

---

## Travel packing

The Wardrobe can become highly useful for trips.

Example:

> I'm going to Istanbul for five days. Pack me a capsule wardrobe.

Inputs:

- Destination/weather
- Trip duration
- Calendar/context
- Luggage constraints
- User style
- Actual available wardrobe

Output:

- Packing list
- Outfit combinations by day/context
- Missing essentials

Packed items can be temporarily marked unavailable at home.

---

## Wardrobe + Life Map

Possible connections:

- Travel destination → packing
- Dry cleaner visit → item state update
- Tailor visit → alteration event
- Shopping location → purchase candidate
- Event venue → outfit context

Location should assist memory, not silently infer sensitive activity without user control.

---

## Wardrobe + social/content sources

With permission, the system can learn style signals from:

- Instagram saved/liked fashion content
- Pinterest boards
- Product screenshots/links
- Fashion creators the user explicitly follows or saves

These are preference signals, not proof of ownership.

The system must distinguish:

**Owned**

from

**Interested in**

from

**Recommended**

---

## Digital fitting / visualization

Later versions may allow the user to visualize combinations on a personal avatar/digital twin.

This is a separate technical layer and should not block the MVP.

A useful MVP can work with item images, flat lays and outfit cards before photorealistic virtual try-on exists.

---

## Public vs private wardrobe

The Wardrobe is private by default.

Users may optionally display selected items or collections in their public House, such as:

- Watch collection
- Sneaker collection
- Favorite outfits
- Fashion archive

Sizes, receipts, prices, purchase history and private inventory remain hidden unless explicitly shared.

---

## Archive and inheritance

Selected items can become part of the House Archive.

This matters particularly for meaningful objects:

- Watches
- Jewelry
- Wedding clothing
- Family heirlooms
- Vintage pieces
- Items attached to important memories

Example:

Grandfather's watch
- Photos
- Story
- Service history
- Ownership timeline
- Intended heir

Digital inheritance can preserve the history even when the physical item changes hands.

Sensitive purchase/payment information does not automatically transfer.

---

## Butler interactions

Examples:

> What should I wear today?

> Find my black belt.

> What size am I in this brand?

> Which jacket works with these trousers?

> What haven't I worn in six months?

> Build me a packing list for Dubai.

> When did I service this watch?

> Which things need repair?

> Do I already own something similar to this?

The core value is memory + inventory + context, not generic style generation.

---

## AI architecture

Local Butler responsibilities can include:

- Search and reason over inventory
- Remember sizes/preferences
- Build combinations from structured item metadata
- Track wear/care history
- Answer questions about owned items
- Draft packing lists

Cloud models can optionally improve:

- Visual item recognition
- Product identification
- Fashion reasoning
- Virtual try-on
- Current weather/context
- Product comparison

Private inventory remains locally controlled where architecture permits, and only minimum required context should be sent to cloud providers.

---

## MVP

1. Create Wardrobe room.
2. Add item from photo.
3. AI extracts candidate category/color/brand/material.
4. User confirms metadata.
5. Organize real inventory.
6. Save outfits.
7. Butler creates outfit suggestions from owned items.
8. Track simple state: ready/laundry/repair/storage.
9. Store sizes and care notes.
10. Basic calendar/weather-aware suggestions when available.

Later:

- Automatic product recognition
- Purchase/receipt integrations
- Wear detection from photos
- Travel packing automation
- Shopping comparison
- Tailor/dry cleaner integrations
- Virtual try-on
- Rich collection/archive/inheritance

---

## Key principle

**The FUL.HOUSE Wardrobe is valuable because it knows what is already hanging in the user's real closet.**