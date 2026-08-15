# FUL.HOUSE — Product Architecture Gaps & Next Systems

## Strategic definition

FUL.HOUSE is no longer best understood as only a virtual or digital house.

**FUL.HOUSE is a personal operating system for real and digital life, presented through the metaphor of a living house.**

The major layers are:

- **House** — spatial/visual interface
- **Rooms** — contexts, permission boundaries and specialized workflows
- **Objects** — functional representations of real, wished-for and digital things
- **Butler** — conversational/agent interface
- **Personal Memory Graph** — structured memory with provenance
- **Compute Ladder** — local-first distributed intelligence across devices, Home Brain and optional cloud experts
- **Life/Relationship Graphs** — people, events, places and shared history
- **VIRT** — progression and economic layer
- **Family Graph** — continuity across children, independent Houses and inheritance
- **Marketplace** — creator-driven expansion of the world

The House metaphor should remain the user-facing experience even as the underlying platform grows into a personal operating system.

---

# Product principle: the owner outranks inference

AI can discover, suggest and organize the House, but explicit owner intent always overrides AI inference.

If AI infers a minimalist room and the owner wants a maximalist Japanese room, the owner wins.

Generated state must remain explainable, editable and reversible.

---

# P0 — Systems still missing from the foundation

## 1. First 10 Minutes / Magic Moment

The project is detailed over years of use but the first session needs its own product design.

Primary goal:

**Within 3–10 minutes the user should experience: “This is actually my House.”**

Target flow:

Landing → Create House → Meet Butler → connect one high-signal source or provide one meaningful input → AI extracts identity signals → a visible room/object transformation happens → Butler explains why → owner edits/approves → first shareable House state.

Do not require 10 integrations before the product becomes interesting.

This requires its own onboarding specification and experimentation plan.

---

## 2. Real Home Digital Twin

FUL.HOUSE must support digitizing the user's actual physical home through photos, video and manual editing.

Potential real objects:

- furniture
- appliances
- HVAC
- water filters
- boiler
- router/network equipment
- televisions
- kitchen appliances
- lighting
- fixtures
- home systems

A REAL object can contain model, serial/identifier where desired, purchase date, receipt, warranty, manual, service history and maintenance reminders.

The Butler should answer practical questions about actual owned objects.

The digital home may intentionally differ from reality. Users can place WISH and DIGITAL objects alongside REAL objects.

---

## 3. Household / Multi-owner model

Not every House has exactly one adult owner.

Introduce `Household` and explicit roles such as:

- Owner
- Co-owner
- Household Member
- Child/Dependent
- Family
- Collaborator
- Guest

A married couple or partners can jointly own a Family House without one being reduced to a visitor.

Data ownership can still remain object-specific and person-specific inside a shared House.

---

## 4. Security Center and Recovery

Create a user-facing Security / Control Room.

It should show:

- trusted devices
- device scopes
- connected services
- cloud AI policy
- public/private rooms
- pending access requests
- heirs/trustees
- backup status
- recent security events

Critical question supported by the product:

> What does FUL.HOUSE know about me?

Recovery must be separate from inheritance.

Potential recovery mechanisms:

- recovery key
- trusted device approval
- encrypted backup
- trusted people / threshold recovery

No single six-digit PIN is the cryptographic root of the House.

---

## 5. Unified Timeline and Commitment Graph

Every room currently risks inventing its own reminders/tasks.

Create a shared `Commitment` model for:

- vehicle service
- filter replacement
- doctor appointment
- vaccination
- travel check-in
- work deadline
- training session
- warranty expiration
- document renewal

Butler should be able to summarize what actually requires attention across the entire House.

Add a unified `House Timeline` for confirmed past and future events.

---

## 6. Search across the House

Global Butler Search is mandatory for long-lived Houses.

Examples:

- Find the contract with X.
- When was I last at this restaurant?
- Show photos from the vehicle repair.
- Which book was I reading during that trip?
- When did we replace this filter?

Search must honor room and data permissions and show provenance for answers.

---

## 7. Data lifecycle and forgetting

FUL.HOUSE should deliberately support forgetting.

Possible retention policies:

- KEEP
- ARCHIVE
- FORGET_AFTER
- DERIVED_MEMORY_ONLY

Example:

Raw GPS traces can be deleted after producing a confirmed semantic Trip/Visit memory, depending on owner settings.

Raw communications may not need indefinite retention after an approved derived memory is created.

**Forgetting is a privacy feature, not data loss.**

---

# P1 — High-utility missing systems

## 8. Pantry / Fridge / Freezer inventory

Kitchen should understand what food is actually available.

Possible inputs:

- photo/video
- receipt import
- barcode
- manual add
- grocery integration where available

Objects:

- Fridge
- Freezer
- Pantry
- Drinks/Wine storage

Butler can prioritize ingredients nearing expiry and match them against the owner's saved recipes and taste profile.

---

## 9. Receipts, purchases and warranties

Create a universal purchase ingestion pipeline.

Receipt/photo/email → extract merchant, date, items, price, warranty evidence → link to relevant House Objects.

Examples:

- television → Real Home
- clothing → Wardrobe
- car part → Garage
- pet product → Pets
- groceries → Kitchen/Pantry

A purchase record should not automatically become public.

---

## 10. Universal Wishlist / WISH graph

`WISH` should apply beyond furniture.

Possible wished-for objects:

- furniture
- vehicle
- watch
- book
- appliance
- clothing
- trip
- property

Butler can understand compatibility with what the user already owns and, where permitted, monitor availability/price through online services.

---

## 11. Communications and Mailbox

Create a communications layer separate from long-term Relationship Memory.

Potential channels:

- email
- House visitor messages
- business inquiries
- selected messaging providers where integrations permit

Butler can triage, summarize, identify requests and draft responses locally where possible.

Communication Memory must not automatically become permanent Relationship Memory.

---

## 12. Calendar and Planner

Calendar needs first-class status rather than being merely an integration.

Represent it through Clock / Planner / Calendar Desk objects.

Rooms can create permissioned commitments into the shared planner.

The Butler can answer:

- What matters today?
- When am I free?
- What deadlines are coming from any room?

Private event content remains private by default.

---

## 13. Relationship Graph

This requires a dedicated future specification.

Core entities:

- Person
- Relationship
- Encounter
- Shared Event
- Shared Memory
- Trust/Permission relationship

Potential query:

> Who was the designer I met in Istanbul two years ago?

Principle:

**Remember relationships, not surveil people.**

FUL.HOUSE should not automatically build invasive dossiers or psychological profiles of non-users from private communications.

---

## 14. Life Events

Introduce `LifeEvent` as a first-class object above individual memories.

Examples:

- birth
- marriage
- divorce
- move
- new job
- graduation
- buying/selling a home
- starting/selling a company
- product launch
- citizenship/residency event
- death

A Life Event can connect multiple rooms and memories and become a major point in the House Timeline.

---

## 15. Multiple Houses

One person may own or participate in several Houses:

- Personal House
- Family House
- Business House
- Creator Studio
- Vacation House

Each independent House has its own Butler identity and permission boundary.

The same human identity can have roles across multiple Houses.

---

## 16. Guest Access Graph

Visitor access is not binary.

Potential roles:

- Public Visitor
- Neighbor
- Friend
- Family
- Client
- Collaborator
- Household Member
- Temporary Guest

Access should be capability/object/room scoped.

A client may see Office but not family albums. A family member may see Kitchen memories but not business documents.

---

## 17. Public Butler vs Owner Butler context

The same House must expose different Butler contexts.

Owner context can access owner-authorized private memory.

Public/visitor context can access only explicitly published capabilities and memories.

This separation must be enforced by permissions/data retrieval, not only by prompting a model to keep secrets.

---

## 18. AI auditability and correction

Every meaningful inference should support:

> Why do you think that?

Example:

`You seem to like Japanese food.`

Evidence:
- 6 saved recipes
- 4 restaurant visits
- explicit preference

Owner can correct the inference. Explicit correction outranks inferred memory while provenance remains available.

---

# P2 — Expansion systems

## 19. Garden and Plants

Digitize real plants and gardens.

Track:
- species
- photos over time
- watering
- fertilizing
- repotting
- location/light
- care reminders

Garden can contain REAL, WISH and DIGITAL plants/assets.

---

## 20. Education, Knowledge and Tutor

Expand Library into a Knowledge layer:

- books
- courses
- diplomas
- certifications
- notes
- skills
- languages
- learning goals

Entering this context can activate Tutor/Librarian Butler mode.

Learning achievements can create earned House Objects without incentivizing meaningless activity farming.

---

## 21. Deeper Office / Work OS

Office requires a dedicated specification covering:

- projects
- clients
- deliverables
- portfolio
- contracts
- invoices
- meetings
- commitments
- products/services
- creator/business reputation

The Office can eventually become a spatial personal work operating system.

---

## 22. Reputation, orders, escrow and disputes

A marketplace for real work cannot stop at listing and payment.

Required future states:

`ORDERED → ACCEPTED → DELIVERED → APPROVED`

plus cancellation/refund/dispute states.

Reputation should emphasize verified outcomes, repeat customers, delivery history and provenance rather than relying only on generic five-star ratings.

---

## 23. Notification policy

Butler must not become a push-notification spam engine.

Potential urgency policies:

- NOW
- TODAY
- WHEN_I_ENTER_ROOM
- DAILY_BRIEF
- WEEKLY_BRIEF
- SILENT

Each room proposes events; a central attention policy decides when the owner should actually be interrupted.

---

## 24. Physical ↔ Digital bridge

Support optional QR/NFC identifiers that open a specific House Object.

Examples:

- appliance
- vehicle
- plant
- storage box
- document container

This creates a low-cost bridge between physical possessions and their digital twins.

---

## 25. Import / Export / Portability

A long-lived House cannot be a data hostage system.

Support:

**Import my life**

and

**Export my House**

Export should include user-owned structured data, provenance, relationships where legally/permission-wise exportable, memories, object metadata, recipes, vehicles, pets, achievements and other portable records.

Encrypted/private data export must preserve security.

---

## 26. House Time Machine

The House should eventually preserve meaningful historical states.

Example:

> Show my House in 2028.

The owner can see rooms, objects, work, vehicle, pets and other state from that period.

This is derived from versioned events and provenance rather than storing endless full snapshots.

---

# Product hierarchy going forward

When evaluating any new feature, classify it into this stack:

1. **Life** — real event, object, person, preference or activity
2. **Memory** — structured record with provenance
3. **Room** — context and permission boundary
4. **Object** — spatial/functional representation
5. **Butler Skill** — action/reasoning interface
6. **Compute** — smallest sufficient tier
7. **Progression** — optional VIRT/achievement effect
8. **Sharing** — explicit visibility/capability rules
9. **Continuity** — sync, backup, child transfer, inheritance, export

A feature that cannot be located cleanly in this stack is probably underspecified.

---

# Priority order

## P0
1. First 10 Minutes / Magic Moment
2. Real Home Digital Twin
3. Household / multi-owner model
4. Unified Timeline + Commitments
5. Search
6. Security Center + recovery
7. Data lifecycle / forgetting

## P1
8. Pantry/Fridge
9. Receipts/Purchases
10. Communications
11. Calendar/Planner
12. Relationship Graph
13. Life Events
14. Multiple Houses
15. Guest Access Graph
16. Public Butler separation

## P2
17. Garden
18. Education/Tutor
19. Deeper Office
20. Reputation/orders/disputes
21. Notification policy
22. QR/NFC bridge
23. Import/Export
24. Time Machine

---

# North-star framing

FUL.HOUSE should remain understandable in one sentence even as its capabilities grow:

**Your life has a home.**

The product is not trying to replace every app with a room-shaped clone. Existing services remain specialized tools. FUL.HOUSE connects the user's life across them, remembers what matters under the user's control, gives that information a spatial home, and lets one personal Butler help across contexts.

The success condition is not the number of integrations or rooms.

The success condition is that the House becomes more useful and more recognizably the owner's as real life accumulates.