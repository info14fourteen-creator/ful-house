# FUL.HOUSE — Digital Garage & Vehicle Assistant

## Core idea

The FUL.HOUSE Garage should contain digital versions of the user's real vehicles and act as a useful ownership memory and assistance layer.

A vehicle is not just a decorative 3D object. It has identity, documents, maintenance history, mileage, service events, problems, photos and memories.

**Digitize your real car. Let the Butler remember how to take care of it.**

---

## Vehicle digitization

Users can create a vehicle from:

- Photos
- Short walk-around video
- VIN where the user chooses to provide it
- Make/model/year
- Trim/engine/drivetrain
- License plate where desired (private by default)
- Odometer reading
- Documents/manuals

The visual representation should preserve recognizable characteristics such as color, body style, wheels and selected modifications while adapting to the House art direction.

MVP does not require photorealistic 3D reconstruction. A stylized recognizable 2D/2.5D representation is sufficient.

---

## Vehicle Memory

Each vehicle receives a persistent timeline.

Example:

BMW X5 — 2023
Current mileage: 47,820 km

History:
- 2026-03-12 — oil changed at 39,200 km
- 2026-05-04 — front tires replaced
- 2026-08-01 — inspection
- 2026-08-14 — owner reported intermittent whistle on startup

Potential stored events:

- Purchase
- Registration
- Mileage updates
- Oil/filter changes
- Tires
- Brakes
- Battery
- Inspections
- Repairs
- Accidents/damage
- Modifications
- Recalls
- Insurance events
- Service visits
- Diagnostic reports
- Receipts/invoices
- Photos/videos

---

## Maintenance assistant

The Butler should answer questions using the specific vehicle profile, manufacturer guidance where reliable data is available, and the user's actual maintenance history.

Examples:

> When should I change the oil?

> When did I replace these tires?

> What was done at my last service?

> Which workshop did I use last time?

> What maintenance is coming up?

The system should distinguish manufacturer recommendations, owner-configured intervals and inferred reminders.

---

## Maintenance reminders

Possible triggers:

- Mileage
- Time since last service
- Manufacturer interval
- User-defined interval
- Document expiration
- Insurance expiration
- Seasonal tire change
- Inspection deadline
- Recall information where authoritative sources are available

Mileage can initially be entered manually or extracted from dashboard photos. Later integrations may provide vehicle telemetry where supported and authorized.

---

## Show Butler diagnostic mode

The owner can use camera, photo, video, audio or text to describe a problem.

Examples:

- Dashboard warning light photo
- Strange sound recording
- Fluid under vehicle photo
- Tire damage photo
- Smoke/video
- Written symptom description

The Butler combines this input with vehicle identity and service history.

It should provide:

1. What the signal/symptom may mean.
2. Several plausible causes where appropriate.
3. Safe basic checks the user can perform.
4. Urgency assessment.
5. What information to give a mechanic.
6. Relevant previous vehicle history.

---

## Safety boundary

The Butler must not present uncertain remote diagnosis as confirmed fact.

For safety-critical symptoms involving brakes, steering, fire/smoke, severe overheating, major fluid loss, tire integrity or other potentially dangerous conditions, it should prioritize stopping/avoiding driving and professional inspection as appropriate.

The product is an ownership assistant, not a replacement for a qualified mechanic or emergency service.

Confidence/provenance should be visible:

- Confirmed from vehicle manual/data
- Confirmed from user's service record
- Likely interpretation
- Possible cause
- Requires professional diagnosis

---

## Location integration

Life Map can connect real-world service visits to Vehicle Memory.

Example:

> You spent two hours at this auto service today. Was the BMW serviced there?

After confirmation, the Butler can ask for receipt/photo and extract:

- Work performed
- Parts
- Mileage
- Cost
- Recommended next service

Repeated service locations can become known Garage relationships.

If a problem occurs away from the user's normal area, online Butler mode may help discover nearby appropriate service providers.

---

## Documents

Garage can securely organize vehicle-related documents:

- Registration
- Insurance
- Service invoices
- Inspection documents
- Warranty
- Manuals
- Purchase documents

Documents are private by default.

The Butler can answer questions from them locally where possible.

Sensitive identifiers should not be exposed in the public House.

---

## AI architecture

Routine Garage tasks should prefer local Butler capabilities:

- Search Vehicle Memory
- Summarize service history
- Extract simple document fields
- Track intervals
- Explain known stored information
- Draft a description for a mechanic

Online/cloud escalation can be used for harder multimodal diagnosis, current recall lookup, current service information or complex technical research, subject to the user's cloud/privacy settings.

Only the minimum necessary context should be sent to external models.

---

## House representation

Vehicles physically appear in the Garage.

Possible functional objects:

- Vehicle → opens Vehicle Memory
- Toolbox → maintenance
- Service book → timeline
- Tire rack → tire history
- Cabinet → private documents
- Workbench → current issues/tasks

Older/sold vehicles can move to Garage Archive rather than disappear.

---

## Ownership history and memories

Vehicle history can include more than maintenance:

- Trips
- Photos
- Purchase story
- Milestones
- First drive
- Countries/cities visited
- Family memories

Example archived vehicle:

BMW X5
Owned 2026–2031
124,000 km
18 recorded service events
32 trips preserved

---

## Inheritance

The owner can choose whether a vehicle's digital record transfers with the House.

This can preserve:

- Vehicle history
- Maintenance records
- Documents selected for inheritance
- Photos/trips
- Ownership story

Sensitive documents require explicit inheritance permissions and should not automatically transfer merely because the decorative vehicle is inherited.

---

## MVP

1. Add vehicle manually.
2. Upload photos.
3. Create stylized digital representation.
4. Store make/model/year/trim/mileage.
5. Vehicle Memory timeline.
6. Add service event manually or from receipt/photo.
7. Maintenance reminders.
8. Butler Q&A over vehicle profile/history.
9. Dashboard-warning photo explanation with safety boundaries.
10. Life Map connection for confirmed service visits.

Later:

- Video-based vehicle reconstruction
- VIN decoding integrations
- Manufacturer maintenance databases
- Recall lookup
- OBD/vehicle telemetry integrations
- Insurance/service integrations
- Rich audio/video diagnostic assistance

---

## Key principle

**The Garage should look like the user's real garage, but its value comes from remembering everything the owner normally forgets about the cars inside it.**