# FUL.HOUSE — Travel & Vacation Memory

## Core idea

Travel should be a first-class FUL.HOUSE system, not a gallery of past trips and not a generic itinerary planner.

The module should support the complete lifecycle of a real trip:

**Before Trip → During Trip → After Trip → Long-term Memory**

FUL.HOUSE should help prepare travel, accompany the user during the trip, connect real-world activity to the House, and preserve the trip as structured personal and family memory.

**FUL.HOUSE doesn't just plan where you're going. It remembers where you've been.**

The Travel system should integrate with Life Map, Wardrobe, Places & Food Memory, Calendar, Documents, Garage, Photos, Butler, House Archive and Inheritance.

---

## Product principles

1. Real travel data before generic recommendations.
2. Personal travel history before public rankings.
3. User taste and constraints before generic "top 10" lists.
4. Raw location is private; memories are curated.
5. Travel planning and travel memory are two halves of the same object.
6. The Butler should reduce coordination overhead, not create another checklist app.
7. Every inference should preserve provenance and confidence.

---

## Core entities

### Trip

The primary container for one journey.

Possible fields:

- Destination(s)
- Start/end dates
- Purpose
- Travelers
- Transport
- Reservations
- Budget
- Documents
- Packing state
- Planned places
- Actual places
- Photos/videos
- Notes
- Expenses
- Food memories
- Vehicle/road-trip data
- Generated memories

### Route

Planned or actual sequence of movement between meaningful places.

### Stay

Hotel, rental, family home, campsite or other accommodation.

### Transport Segment

Flight, train, bus, ferry, rental vehicle, private vehicle or other movement.

### Travel Place

A Place object associated with a Trip: restaurant, museum, beach, shop, landmark, hospital, service station, etc.

### Travel Memory

A structured preserved event composed from confirmed real data such as location, photos, place, time and notes.

### Travel Document

Ticket, booking, visa, insurance, reservation, rental agreement or other travel document.

---

# 1. Trip creation and detection

Trips can be created:

- Manually
- From calendar events
- From flight/train bookings in email
- From hotel/reservation emails
- From uploaded tickets/documents
- From a large location change detected by Life Map
- From explicit Butler conversation

Example:

> I noticed flights and a hotel booking for Istanbul from August 20–26. Create a trip?

The Butler should not silently create a public or permanent travel object from sensitive data. Detection creates a candidate Trip until confirmed where appropriate.

---

# 2. Before Trip — preparation

The goal is to create one coherent travel workspace rather than making the user manually coordinate calendar, email, weather, documents, maps and packing.

## Travel Brief

The Butler can build a concise briefing containing:

- Dates
- Destination
- Travelers
- Flight/train information
- Stay
- Local time zone
- Weather forecast when online
- Planned meetings/events
- Reservation schedule
- Required/selected documents
- Transfers
- Important reminders
- User-selected places

Example:

> You leave for Istanbul in four days. I have your flight, hotel and two dinner reservations. Your Tuesday meeting makes this a mixed business/leisure trip.

---

## Documents

The Butler can organize and search:

- Passport copies
- Visa documents
- Tickets
- Boarding passes where available
- Hotel confirmations
- Travel insurance
- Rental agreements
- Reservation confirmations

Sensitive documents remain private and should be encrypted/protected according to platform architecture.

The Butler may remind the user about missing/expiring items but must not claim legal/visa sufficiency without reliable current data.

---

## Wardrobe and digital packing

Travel should integrate deeply with Digital Wardrobe.

Inputs may include:

- Destination weather
- Trip duration
- Business/leisure context
- Planned activities
- Laundry availability
- Dress requirements
- User style
- Existing real clothing

The Butler builds a **Digital Suitcase** from actual wardrobe objects.

Example:

> Six days, warm weather, one business dinner. I suggest 3 T-shirts, 2 shirts, 1 lightweight jacket, 2 trousers and these sneakers. The blazer is only needed for Tuesday.

Capabilities:

- Avoid overpacking
- Detect missing categories
- Check whether selected items combine into multiple outfits
- Track packed/unpacked state
- Produce return-home laundry list
- Remember what was actually worn where if the user chooses

---

## Planning places

Planning should begin with:

1. Places the user already saved.
2. Places recommended by trusted people/household.
3. Similar places from the user's existing taste profile.
4. External discovery.

The Butler should understand travel style rather than output a generic attraction dump.

---

# 3. Travel DNA

FUL.HOUSE can gradually learn a user-controlled travel preference profile from confirmed past behavior and explicit feedback.

Possible traits:

- Beach vs city
- Dense itinerary vs slow travel
- Walking tolerance
- Early vs late starts
- Luxury vs budget sensitivity
- Boutique vs chain hotels
- Food-focused travel
- Museums/culture
- Nature
- Shopping
- Nightlife
- Family-oriented preferences
- Business travel habits
- Preferred flight times
- Preferred seat/cabin where explicitly known
- Rental-car usage

The system must distinguish explicit preferences from inferred ones.

Example:

> You usually prefer walkable city trips with restaurants and architecture. This resort is mostly isolated and resort-only, so it may be a weaker fit for you.

Travel DNA should be editable and deletable.

---

# 4. During Trip — travel companion

During an active Trip, the Butler should switch into a travel-aware mode.

It can answer:

> What's next today?

> Where was that restaurant I saved?

> What's nearby that matches what I actually like?

> Which clothes did I pack for dinner?

> Where did I leave the rental agreement?

> What's the address of my hotel?

> What restaurant did I like near here last time?

Where online/current information is required, cloud/web assistance may be used according to user settings.

---

## Context awareness

During travel, the Butler may combine authorized signals:

- Current location
- Trip schedule
- Time
- Weather
- Saved places
- Reservations
- Transport
- Wardrobe
- Food preferences

It should not constantly interrupt the user. Proactive prompts should be sparse, useful and configurable.

Examples:

> Your dinner reservation is in 50 minutes and is about 25 minutes away.

> Rain is expected later. The lightweight jacket you packed is suitable.

---

# 5. Life Map integration

Life Map supplies actual movement and candidate visits.

The Travel system should reconstruct meaningful travel routes from semantic events rather than expose a raw GPS spaghetti line by default.

Example day:

Hotel → Galata → Cafe → Museum → Restaurant → Hotel

Candidate events can be confirmed during or after the trip.

The user may view the raw route privately if enabled, but long-term archive should prefer meaningful semantic locations over unnecessary coordinate retention.

---

# 6. Places & Food integration

Every confirmed restaurant/cafe visit can link to Places & Food Memory.

A Trip can show:

- Restaurants visited
- Dishes tried
- Loved/disliked dishes
- Delivery orders
- Favorite places
- Places worth returning to

Example:

> You tried 11 restaurants on this trip. You marked three dishes as favorites.

The food memory remains useful after the trip ends.

---

# 7. Photos and media

With permission, travel photos/videos can be clustered by:

- Date/time
- Location
- Place
- Event
- People where allowed
- Trip day

The goal is not to create another cloud photo library.

The Travel system should organize media around real events.

Example:

Day 2
- Bosphorus walk
- Dinner at X
- 54 photos
- 3 videos

Original media can remain in the user's existing photo provider while FUL.HOUSE stores references/derived metadata where architecture permits.

---

# 8. Travel Memory Book

After the trip, the Butler can propose a generated structured memory book.

Example:

Istanbul — August 2026
6 days
18 meaningful places
342 photos
7 restaurants
2 favorite places
1 hotel
46 km walked

Potential contents:

- Map
- Day-by-day route
- Selected photos
- Stays
- Food
- Notes
- Purchases
- People
- Favorite moments
- Trip summary

Generated narrative must be grounded in confirmed data and clearly avoid invented experiences.

The user can edit every part before saving or sharing.

---

# 9. Digital souvenirs

Real travel can change the House.

A confirmed Trip may create a subtle digital souvenir/object associated with the trip.

Examples:

- Small object on a shelf
- Postcard
- Travel book
- Map pin
- Framed photograph

The object opens the Trip/Travel Memory.

This should represent real experience, not random collectible speculation.

---

# 10. Spending and expense memory

Optional travel expense tracking may use:

- Manual entry
- Receipts
- Email confirmations
- Card/bank transaction imports where explicitly connected

The system can categorize:

- Transport
- Stay
- Food
- Shopping
- Activities
- Other

This can answer:

> What did this trip actually cost?

But financial data must remain private by default and should not be required for the core travel experience.

---

# 11. Road trips and Garage

For vehicle-based travel, Trip can link to Digital Garage.

Possible information:

- Vehicle used
- Starting/ending mileage
- Fuel/charging stops
- Service events
- Tire/maintenance readiness
- Route
- Toll/parking records

Before a road trip, Butler can use Vehicle Memory to surface relevant maintenance concerns.

Example:

> You're planning a 1,200 km road trip. Your next oil service is due in about 900 km based on your configured interval.

Safety-critical guidance must follow Garage safety boundaries.

---

# 12. Travel with family / household

Trips can optionally be shared among House members or invited travelers.

Possible shared objects:

- Itinerary
- Reservations
- Packing responsibilities
- Shared places
- Shared photos
- Shared expenses

Private personal data should remain scoped per participant.

A family Trip should not automatically expose one member's private calendar, location history or messages to others.

---

# 13. Butler travel agent role

The Butler is the conversational interface across the entire trip.

Before:

> Prepare my Istanbul trip.

During:

> What are we doing next?

After:

> Show me the restaurants I liked.

Years later:

> Where did we stay in Istanbul in 2026?

The same conversational agent should access the same persistent Trip object through its lifecycle.

---

# 14. Offline-first behavior

Travel is exactly where connectivity may be unreliable.

FUL.HOUSE should preserve an offline travel pack when possible:

- Core itinerary
- Hotel address
- Transport details
- Selected documents/confirmations
- Saved places
- Packing list
- Essential Trip notes

The local Butler should be able to search this data without internet.

Cloud assistance can enhance planning and current discovery when connectivity exists.

---

# 15. Privacy

Travel creates especially sensitive data.

Requirements:

1. Current location private by default.
2. Active Trip status private by default.
3. Future travel plans private by default.
4. Public sharing occurs only by explicit selection.
5. Raw location traces are not automatically published or inherited.
6. Photos remain subject to their own permissions.
7. Financial data remains private.
8. Travel companions' data must not be exposed without permission.
9. Users can remove individual events or entire Trips.
10. Generated memories must retain provenance.

Avoid publicly signaling that a user's home is unoccupied because they are traveling.

---

# 16. Archive and inheritance

Selected Trips can become permanent House Archive objects.

The owner chooses which parts can be inherited:

- Travel Memory Book
- Selected photos
- Favorite places
- Notes
- Routes
- Stories
- Digital souvenirs

Sensitive operational details such as passport copies, payment data, unrestricted location traces or booking credentials should not automatically transfer.

Example future experience:

> Dad's Istanbul — 2026

An heir can explore the preserved route, photos, favorite restaurants and selected memories without receiving the entire private surveillance history of the original owner.

---

# 17. House representation

Potential room:

**Map Room / Travel Room**

Functional objects:

- Large world map → Trips
- Suitcase → upcoming/current Trip and packing
- Passport drawer → private travel documents
- Shelf → Travel Memory Books
- Souvenirs → individual Trips
- Globe → destination discovery
- Photo table → selected travel albums

The room should visibly evolve as real travel history accumulates.

---

# 18. Core loops

## Preparation loop

Detected/created Trip → Butler gathers reservations/documents → Wardrobe packs → places selected → Trip ready.

## During-trip loop

Schedule + location + saved places + current context → Butler assists → actual events are captured.

## Memory loop

Trip ends → semantic events + photos + food + notes → Travel Memory Book → preserved in House.

## Personalization loop

Confirmed travel behavior → Travel DNA improves → future planning becomes more personal.

## Inheritance loop

Selected Trip memories → House Archive → heir can explore family travel history.

---

# 19. MVP

The MVP should prove that FUL.HOUSE can turn a real trip into a useful object before, during and after travel.

### MVP Phase 1

1. Create Trip manually or from forwarded/shared booking information.
2. Add dates, destination, stay and transport.
3. Butler creates Travel Brief.
4. Link to Calendar.
5. Build packing list from Digital Wardrobe.
6. Add saved places.
7. Optional location-assisted visit detection through Life Map.
8. Connect restaurant visits to Places & Food Memory.
9. Associate photos with Trip by time/location where permitted.
10. Generate post-trip Travel Memory summary.
11. Save Trip in Map Room.
12. User controls public/private/archive state.

### Later phases

- Email auto-detection of travel bookings
- Rich reservation integrations
- Live flight/train status
- Hotel and transportation APIs
- Shared family trips
- Expense imports
- Advanced travel recommendations
- Offline map packs
- Current safety/travel advisory assistance
- Road-trip telemetry
- Rich inherited travel archives

---

## Key product principle

**Travel in FUL.HOUSE is not content to consume. It is real life to prepare, experience, understand and remember.**