# FUL.HOUSE — Childhood, Growth, Health & Wellbeing

## Core idea

FUL.HOUSE should allow a family to build a child's digital history from early childhood while progressively transferring control, privacy and eventually ownership to the child as they mature.

This is not a parental surveillance product and not an AI replacement for pediatricians or psychologists.

It is a structured childhood memory, health record, development journal and future personal House.

**Parents help build the beginning of a child's House. They do not own the child's digital life forever.**

---

# 1. Child House

A child can have a dedicated Child House connected to a Family House.

In early childhood, parents or authorized guardians manage it. Over time, the child receives increasing ability to contribute, control privacy and manage their own spaces.

The House itself should visually grow with the child:

- Nursery
- Kids Room
- School-age room
- Teen space
- Independent House

The transformation should be driven by real life rather than arbitrary game levels.

Examples of events that can shape the space:

- First word
- First steps
- First birthday
- First drawing
- First school day
- Favorite books
- Sports
- Music
- Hobbies
- Projects
- Travel
- Achievements
- Pets
- Friends and selected memories

---

# 2. Structured childhood memory

The purpose is to transform thousands of disconnected photos, documents and parental notes into a coherent timeline.

Potential memory objects:

- Photos/videos
- Milestones
- Drawings
- Voice recordings
- School achievements
- Trips
- Favorite books
- Hobbies
- Sports
- Family events
- Pets
- Places
- Family recipes

Example timeline:

Age 1 → first steps
Age 3 → first trip abroad
Age 6 → first school day
Age 9 → first football competition
Age 12 → first coding project

The system should preserve original media and clearly distinguish parent-authored memories from AI-generated summaries.

---

# 3. Growth Book

The Child House can contain a private Growth Book.

Possible measurements:

- Height
- Weight
- Head circumference for young children where relevant
- Developmental milestones
- Teeth
- Vision-related records
- Sleep notes
- Nutrition notes

Measurements should be timestamped and sourced.

Growth comparisons should use recognized age-appropriate reference data where available rather than LLM estimation.

The Butler may identify changes worth discussing with a clinician but must not diagnose from growth data.

Example:

> This measurement differs from the previous growth trend. It may be worth discussing at the next pediatric visit.

---

# 4. Vaccination Passport

FUL.HOUSE should maintain a structured vaccination record.

Each vaccination event can include:

- Vaccine
- Disease(s) covered
- Dose number
- Date
- Clinic
- Clinician
- Manufacturer
- Batch/lot where available
- Certificate/photo/document
- Recorded reaction/notes
- Next expected dose when supported by an authoritative schedule

Users can photograph or upload vaccination records. AI may extract structured data, but uncertain fields must be marked for confirmation.

## Schedule architecture

FUL.HOUSE must separate:

**Observed fact** → vaccination actually recorded for this child.

from

**Recommendation** → what a selected current schedule suggests.

Vaccination schedules vary by country, age, medical context and time.

The system should therefore store:

- Schedule jurisdiction/source
- Version/date
- Applicable age range
- Recommendation provenance

Never silently treat one country's schedule as universal.

---

# 5. Medical Vault

The Child House can contain a highly private Medical Vault.

Potential records:

- Vaccinations
- Allergies
- Clinician-recorded diagnoses
- Current/past medications
- Prescriptions
- Laboratory results
- Imaging/reports
- Discharge summaries
- Procedures
- Insurance documents
- Relevant family-provided notes
- Medical contacts

The Butler can help retrieve and summarize stored information.

Examples:

> Show the latest blood test.

> When was the last vaccination?

> Prepare a concise history for a new pediatrician.

A generated clinician summary can include age, allergies, medications, vaccination status, relevant recorded history, recent health events and questions the family wants to ask.

AI summaries must retain provenance back to original records.

---

# 6. Child Health Butler

The user-facing experience may feel like a mini pediatric assistant, but internally it should be treated as a Child Health Butler rather than a diagnostic physician.

It can:

- Organize symptoms over time
- Ask structured follow-up questions
- Maintain Health Events
- Retrieve relevant history
- Explain general health information
- Surface warning signs that warrant medical attention
- Help prepare for a clinician visit
- Summarize a health episode

It must not present uncertain diagnosis as established medical fact or replace professional pediatric care.

Example Health Event:

2026-08-15
- Fever: 38.4 C
- Cough
- Started around 14:00
- Parent observations
- Subsequent temperature readings
- Clinician visit/result if one occurs

Over time the parent can ask:

> When was the last similar fever episode?

and the Butler retrieves the child's actual history.

---

# 7. Development & Wellbeing

FUL.HOUSE can support development and wellbeing without attempting to become an autonomous child psychologist.

For younger children, structured observations can include:

- Speech/language
- Movement
- Play
- Social interaction
- Sleep
- Eating
- Independence

For older children and teenagers, owner/guardian-permitted areas may include:

- School
- Interests
- Sleep
- Stress
- Mood check-ins
- Friendships
- Activities
- Behavioral changes

Validated age-appropriate screening instruments may be supported where licensing and clinical requirements allow, but results must be presented with appropriate context and should not be converted into diagnoses by a generic LLM.

---

# 8. Privacy transition as the child grows

A child's data model must change with age and maturity.

A young child's House is primarily guardian-managed.

As the child grows, FUL.HOUSE should progressively introduce:

- Their own login/account
- Their own rooms
- Their own connected services
- Private spaces
- Controls over what parents can view
- Controls over what visitors can view
- Clear separation between family memories and personal communications

A teenager's private conversation with their Butler must not automatically become a parental transcript.

Safety/legal exceptions and parental-control behavior must be designed according to applicable law and platform requirements, not improvised by the AI.

---

# 9. Child builds their own present

Before full independence, an older child/teen can begin building their own House by connecting authorized accounts.

Examples:

Spotify → Music Room
Instagram → selected memories/interests
YouTube → selected interests/content
GitHub → Workshop
Gaming services → Gaming Room where supported
Sports/activity sources → Sports area
School/portfolio → Projects/Achievements

This creates an important transition:

**Parents contributed the past. The child begins building the present.**

The child should not have to start a blank digital identity at adulthood.

---

# 10. Progressive Ownership

The Child House is designed from the beginning to become the child's property/control space.

Possible transition stages:

### Guardian-managed
Parents/guardians create and maintain the early House.

### Shared stewardship
The child gains their own account, can create spaces, connect services and manage selected privacy.

### Independent ownership
At an appropriate configured/legal age and after required account/identity steps, control transfers to the child.

Age alone should not be the only implementation rule globally. Jurisdiction, platform policy and family/account configuration may affect timing and required consent.

---

# 11. Move Out

At independence, the Child House can separate from the Family House.

Possible experience:

> Your House is ready to become yours.

The child receives their own address such as:

`ful.house/name`

Their childhood history remains part of their House subject to privacy and shared-memory rules.

Example metadata:

House established: 2026
Independent since: 2044

The visual metaphor can be literal: the child's space moves from the family property into its own location in the FUL.HOUSE neighborhood.

---

# 12. Connected House

Moving out does not require severing family relationships.

An independent House can remain connected to the Family House.

Possible shared connections:

- Family trips
- Shared photos
- Family pets
- Family recipes
- Family events
- Selected places
- Shared heritage objects

The connection is permissioned. Independence changes access rights even when memories remain linked.

---

# 13. Family Estate

Families may choose a broader Family Estate model.

Instead of every adult House being visually unrelated, multiple independent Houses can exist within a shared family space.

Important distinction:

**Family Estate is a relationship between independently permissioned Houses, not a master account that permanently owns every family member's data.**

Possible representation:

Family Estate
- Parent House
- Parent/Partner House
- Adult Child House
- Adult Child House
- Ancestral/Archive Houses where inherited

Over generations, this can become a navigable family history.

---

# 14. Shared Memory Graph

FUL.HOUSE should avoid blindly duplicating family memories into every account.

Instead, a shared memory can be a single logical object with participant-specific permissions and views.

Example:

Trip #8472 — Italy
Participants:
- Parent A
- Parent B
- Child A
- Child B

Each participant can have:

- Their own photos
- Their own notes
- Their own privacy settings
- Their own derived memories

while still referencing the same family Trip.

This model can apply to:

- Trips
- Pets
- Restaurants
- Family events
- Vehicles
- Recipes
- Albums
- Places

The Family House can show the shared family perspective while individual Houses show personal perspectives.

---

# 15. Medical ownership transition

Medical data requires special handling during independence.

The child's historical Medical Vault should transition into their own private control when legally and operationally appropriate.

Parents should not automatically retain indefinite access to an adult child's medical data merely because they originally uploaded it.

The system needs explicit rules for:

- Guardian access
- Child access
- Transition age/state
- Revocation
- Emergency access if implemented
- Shared records
- Export
- Deletion/retention obligations

These rules require jurisdiction-specific legal review before implementation.

---

# 16. Travel integration

Family travel can connect Child House, Medical Vault and Travel.

Before a trip, the Butler may help check authorized records such as:

- Insurance document present
- Vaccination certificate stored
- Required regular medications included in packing checklist
- Relevant prescription/document available

This should be presented as organizational assistance, not medical clearance to travel.

---

# 17. Inheritance vs childhood transfer

FUL.HOUSE has two distinct continuity mechanisms.

### Inheritance
An existing owner passes selected House assets/memories/control according to inheritance rules.

### Childhood transfer
Parents/guardians progressively hand a child's own digital history to that child.

These must not be treated as the same legal/product event.

Childhood transfer is fundamentally about returning control of the person's own history to them.

---

# 18. Core privacy principles

1. Child health data is highly sensitive and private by default.
2. Public House objects must never expose medical records by default.
3. Parent access should evolve as the child matures and applicable law requires.
4. Private Butler conversations are not automatically family-visible.
5. AI-generated summaries must remain linked to source records.
6. Health recommendations must distinguish authoritative guidance from AI interpretation.
7. The child should eventually control their own digital history.
8. Shared family memories do not imply shared access to every associated private record.
9. Account separation must preserve provenance and relationships without silently copying sensitive data.
10. Location, medical and psychological/wellbeing data require especially strict access controls.

---

# 19. MVP direction

This is too sensitive and broad to ship as one undifferentiated feature.

Recommended early scope:

1. Child House linked to Family House.
2. Childhood timeline/memories.
3. Growth Book.
4. Vaccination Passport.
5. Private Medical Vault document storage.
6. Guardian permissions.
7. Shared family memory data model.
8. Architecture designed for future ownership transfer.

Later phases:

- Child Health Butler
- Development/wellbeing tools
- Teen self-managed rooms
- Connected accounts
- Progressive privacy
- Move Out
- Connected Houses
- Family Estate
- Full Medical Vault ownership transition

---

## Key product principles

**A child's House should grow with the child.**

**Parents build the beginning. The child builds the present. Eventually the House becomes theirs.**

**Family history can remain connected without requiring family members to surrender individual privacy.**