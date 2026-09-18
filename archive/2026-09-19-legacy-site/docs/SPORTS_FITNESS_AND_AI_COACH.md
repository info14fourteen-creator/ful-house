# FUL.HOUSE — Sports, Fitness & AI Coach

## Core idea

Sports and fitness should become a real room/area generated from the user's actual activity, equipment, goals and connected sources.

The room is both a visual record of physical activity and a useful adaptive training assistant.

**The Sports Room should reflect what the owner actually does, not what they clicked as an interest.**

---

## Room forms

The physical representation can adapt to activity:

- Running Corner
- Home Gym
- Strength Room
- Cycling Corner
- Swimming display
- Football area
- Tennis area
- Yoga/mobility space
- Mixed Sports Room

Multiple sports can coexist.

Real equipment can be digitized as House Objects and linked to training plans.

---

## Input sources

Subject to API/platform availability and explicit permission:

- Apple Health / HealthKit-capable client
- Google Health Connect-capable client
- Garmin
- Strava
- WHOOP
- Oura
- Other fitness trackers
- Manual workouts
- Equipment photos
- User-entered height/weight/goals

Provider adapters should normalize external data into FUL.HOUSE activity records rather than leaking provider-specific schemas throughout the domain.

---

## Fitness profile

Potential fields:

- Age
- Height
- Weight
- Training experience
- Goals
- Preferred activities
- Available days/time
- Available equipment
- Relevant limitations explicitly provided by user
- Training history

Sensitive health data is private and permission-scoped. Sports Room should request only the minimum Health capability needed for a task.

---

## Weight and body measurements

Weight/height updates can contribute to House maintenance/progression, but rewards must use reasonable intervals and meaningful-change logic.

A user can correct erroneous measurements without receiving additional VIRT.

The system should preserve measurement provenance: manual, connected scale, health provider, imported record.

Do not reward weight loss itself. Reward accurate maintenance of the profile and healthy engagement with chosen plans, not a particular body size or rapid change.

---

## AI Coach Butler Mode

Entering Sports Room activates Coach context/uniform.

The Coach can:

- Build training plans
- Adapt plans to equipment
- Adapt to schedule
- Track completion
- Respond to perceived difficulty
- Suggest progression/regression
- Create travel workouts
- Explain exercises
- Summarize training history
- Help maintain consistency

The Coach is the same Butler identity with a Sports skill and Sports permissions.

---

## Adaptive plan model

A plan is not a static PDF.

Inputs can include:

- Goal
- Available days
- Session duration
- Equipment
- Recent training
- User feedback
- Travel/calendar constraints
- Recovery signals where explicitly authorized

Example:

User: `Squats were too easy.`

The next appropriate session can adjust progression within defined safety rules.

If the user misses a week, the system should not blindly continue progressive overload as if nothing happened.

---

## Cross-room capabilities

### Travel → Sports
Travel can request a travel-friendly plan.

### Sports → Travel
Sports can request trip duration, schedule and available hotel/gym context without reading the entire Travel archive.

### Sports → Wardrobe
Can request available sportswear/equipment for packing.

### Sports → Health
Can request explicitly permitted constraints relevant to exercise. It does not receive unrestricted Medical Vault contents.

### Sports → Calendar
Can request available training windows if authorized.

---

## Safety boundaries

The Coach is not a physician or physical therapist.

It should:

- avoid diagnosing injury
- avoid encouraging training through alarming symptoms
- clearly distinguish general fitness guidance from medical advice
- route concerning symptoms toward appropriate professional evaluation
- respect age-specific restrictions for child accounts

Training recommendations should be conservative when user history is incomplete.

---

## Achievements

Achievements should represent meaningful milestones, not compulsive streak mechanics.

Examples:

- First Workout
- First 5K
- First 10K
- 25 workouts
- 100 workouts
- First month with a consistent plan
- First cycling distance milestone
- First swimming milestone
- Personal best milestones where appropriate

Avoid achievements that reward dangerous extremes, excessive exercise or unhealthy weight change.

---

## Sports rewards

Examples:

- Create Sports Corner → Discovery Reward
- Connect first supported tracker → Discovery Reward
- Complete initial fitness profile → Contribution Reward
- Valid measurement update after reasonable interval → Maintenance Reward
- Meaningful verified milestone → Achievement Reward

Raw step count or kilometers should not mint unlimited VIRT.

Diminishing returns, milestone bands and verification levels are required.

---

## Earned Sports Objects

Achievements can create non-purchasable objects:

- medals
- trophies
- route maps
- race bib displays
- equipment stands
- special wall objects

These objects retain achievement provenance and can be visible publicly only if the owner chooses.

---

## Real equipment digitization

Users can photograph real equipment:

- treadmill
- dumbbells
- bicycle
- trainer
- yoga mat
- rack
- rowing machine

FUL.HOUSE can create recognizable digital objects and record useful metadata.

The Coach can build plans around equipment the user actually owns.

---

## Travel mode

When a trip is active, Coach can generate a temporary plan using available time and equipment.

Example:

> You will be away for 8 days and the hotel has no gym. I can replace your normal sessions with three 25-minute bodyweight sessions.

Travel mode should not permanently rewrite the base plan unless the user approves.

---

## Child/teen integration

Child House sports features require age-appropriate design and guardian/privacy rules.

Do not use adult training or weight-loss assumptions for children.

Sports achievements for children should emphasize participation, skills and age-appropriate progress rather than body composition.

---

## Local-first AI

Routine Sports Room tasks should run through the smallest sufficient compute tier:

- logging workout → deterministic/T0
- simple summary → local/T1
- plan adjustment → local strong/T2 where capable
- deeper analysis → Home Brain/T3
- current external research or difficult reasoning → Cloud/T4 only when policy permits

Private fitness history should not be sent wholesale to cloud providers.

---

## MVP

1. Create Sports Room.
2. Manual fitness profile.
3. Height/weight history with provenance.
4. Manual workout logging.
5. Digitize basic real equipment.
6. Coach generates a simple goal/equipment/schedule-aware plan.
7. Workout completion and difficulty feedback.
8. Deterministic milestone achievements.
9. VIRT reward integration.
10. Travel capability hook.

Later:
- tracker adapters
- recovery integrations
- richer exercise library
- motion/video feedback where technically and safely appropriate
- advanced periodization

---

## Key principle

**The Coach should help the owner use the body, time and equipment they actually have, while the Sports Room becomes a visual history of what they have genuinely done.**