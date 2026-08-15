# FUL.HOUSE — Life Map & Location Memory

## Core idea

With explicit permission, FUL.HOUSE can use device location to build a private semantic map of the user's real life.

The system should not merely store GPS coordinates. It should transform authorized location signals into meaningful candidate events and relationships: places visited, trips, routines, restaurants, vehicle service visits, travel memories and other contexts that can enrich the House.

**Coordinates are data. Places become memories only with context and user control.**

---

## Semantic location pipeline

Location signal → map matching → candidate place → dwell/event inference → contextual evidence → confidence → Butler confirmation when needed → memory/object connection.

Examples:

- Restaurant visit → Places & Food Memory
- Airport → Travel event
- Hotel → Travel memory
- Auto service → Garage service event
- Repeated workplace → possible work context
- Repeated gym → activity context

The system should avoid converting brief drive-bys into visits.

---

## Confidence model

Candidate events can use:

- Dwell duration
- Distance from place centroid/boundary
- Repeat visits
- Time of day
- Calendar context
- Photos taken nearby
- Receipts/email confirmations
- Delivery/reservation data
- User corrections

Low-confidence events should not silently become permanent memories.

Example:

> You spent about 70 minutes near this restaurant yesterday. Were you there?

User correction becomes training signal for future place inference.

---

## Life Map

The user can view a private map of meaningful places rather than an indiscriminate surveillance trail.

Possible categories:

- Home
- Work
- Food
- Travel
- Family
- Automotive
- Shopping
- Recreation
- Saved/favorite places
- User-created categories

The map should support time-based exploration such as month/year/trip without forcing every raw coordinate into the interface.

---

## Butler usage

Examples:

> Where was that cafe I visited in Istanbul last year?

> Which auto service did I use last time?

> What restaurants did I like near this hotel?

> When was the last time I visited this place?

> Show me places from my 2027 trip.

The Butler answers from the user's authorized memory and clearly distinguishes confirmed memories from inferred candidates.

---

## Cross-house connections

Life Map is an infrastructure layer feeding other parts of FUL.HOUSE:

Location → Places → Kitchen/Taste

Location → Garage → Service history

Location → Travel → Photos/Albums

Location → Events → House Archive

Location should not become a separate gimmick. Its value is connecting real-world activity to the digital house.

---

## Privacy and safety architecture

Location data is among the most sensitive data in FUL.HOUSE.

Requirements:

1. Explicit opt-in.
2. Clear explanation of collection mode.
3. Raw location private by default.
4. Public House never exposes current location by default.
5. Public sharing is independent from collection permission.
6. Sensitive places receive stronger protection.
7. Users can pause collection.
8. Users can delete ranges or all location history.
9. Users can correct place inference.
10. Current/recent location must never be exposed to visitors unless explicitly enabled for a specific purpose.
11. Heirs do not automatically receive unrestricted raw location history.
12. Prefer local/on-device processing where practical for map matching, clustering and personal routine inference.

---

## Retention strategy

A privacy-forward implementation should consider storing semantic memories long-term while minimizing indefinite storage of unnecessary raw coordinates.

Example:

Raw coordinates → resolve confirmed restaurant visit → preserve Visit object → discard or downsample raw trace according to user settings.

This reduces sensitivity while retaining useful memory.

---

## MVP

1. Explicit location permission.
2. Recent/candidate place detection.
3. Map matching.
4. Dwell-time filtering.
5. Butler asks confirmation for uncertain meaningful visits.
6. Confirmed visits become typed events.
7. Connect restaurant visits to Places & Food Memory.
8. Connect auto-service visits to Garage.
9. Private Life Map UI.
10. Delete/pause controls.

---

## Key principle

**FUL.HOUSE should know where the user's life happened without turning the House into a tracking product.**