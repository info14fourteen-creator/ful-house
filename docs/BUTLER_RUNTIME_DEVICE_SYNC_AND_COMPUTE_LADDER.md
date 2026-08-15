# FUL.HOUSE — Butler Runtime, Device Sync & Compute Ladder

## Core idea

The Butler must be experienced as one continuous identity even though its intelligence may run across multiple devices and models with very different capabilities.

**The Butler is not the model.**

A model is only one compute engine available to the Butler at a particular moment.

The Butler itself is composed of four separable layers:

1. Butler Identity
2. Butler Memory
3. Butler Skills
4. Butler Runtime / Models

This separation allows FUL.HOUSE to preserve a consistent personality and memory while dynamically choosing the cheapest, fastest, most private and sufficiently capable compute path for every task.

---

# 1. Compute ladder

FUL.HOUSE should use a privacy-first compute ladder.

Preferred order:

**Tier 0 — Deterministic local tools**

Use no LLM where simple code is enough.

Examples:
- Timers
- Calendar arithmetic
- Reminder lookup
- Recipe scaling
- Calorie summation from a trusted database
- Maintenance interval calculations
- Searching indexed local documents
- Simple sorting/filtering
- Known command execution

This is the cheapest, fastest and most reliable tier.

---

**Tier 1 — Tiny Local Butler**

Runs directly on low-power devices such as phones, tablets and lightweight laptops.

Typical duties:
- Intent classification
- Short message drafting
- Email triage
- Summarization of small inputs
- Structured extraction
- Tool selection
- Personal memory lookup orchestration
- Short conversational responses
- Offline help

The exact model can vary by device generation.

The system should treat model size as replaceable implementation detail rather than product identity.

---

**Tier 2 — Strong Local Device Model**

Runs when the current device has sufficient CPU/GPU/NPU, memory, battery and thermal headroom.

Examples:
- Modern laptop
- High-end desktop
- High-end phone/tablet where practical

Typical duties:
- Longer drafting
- Multi-document summarization
- More nuanced personal assistance
- Local RAG over larger private context
- More complex planning
- Richer language generation
- Some multimodal analysis where locally supported

---

**Tier 3 — Home Brain**

A user-designated trusted machine inside the household, such as a Mac mini, PC, NAS-class system or future dedicated FUL.HOUSE hub.

It can host:
- Larger local model
- Full encrypted Personal Memory Graph replica
- Embedding/indexing services
- Photo/video processing
- Local document parsing
- Background memory consolidation
- Heavy multimodal jobs
- Household-wide automation

The Home Brain should be reachable from approved personal devices through end-to-end encrypted authenticated channels.

The Home Brain is optional. FUL.HOUSE must remain usable without one.

---

**Tier 4 — Cloud Expert**

Used only when permitted by user settings and when the task materially benefits from larger reasoning or current online information.

Possible providers:
- OpenAI
- Google
- Anthropic
- Other approved providers
- FUL.HOUSE hosted models

Cloud is an escalation target, not the default owner of personal memory.

Only the minimum necessary context should be sent.

Examples:
- Complex legal drafting
- Difficult multimodal vehicle analysis
- Current travel research
- Current medical guidance lookup from authoritative sources
- Deep long-form writing
- Complex coding or planning

---

# 2. Routing principle

Every Butler request should pass through a Compute Router.

The Router estimates:

- Task type
- Required capabilities
- Privacy sensitivity
- Context size
- Need for current internet data
- Latency requirement
- Device power state
- Available RAM/VRAM/NPU
- Battery status
- Thermal state
- Network quality
- User cloud permissions
- Cost policy
- Skill-specific constraints

Then it selects the lowest tier likely to complete the task safely and well.

**Use the smallest sufficient brain.**

---

# 3. Example routing decisions

## Example A — Email triage

Task:
> Which emails need my attention?

Flow:
1. Deterministic mail metadata filters.
2. Tiny local model classifies priority and intent.
3. Personal Memory Graph adds context about known contacts/projects.
4. No cloud needed.

---

## Example B — Draft a short reply

Task:
> Reply that I can meet Thursday after 3.

Flow:
1. Tiny local model drafts.
2. Calendar tool validates availability.
3. User approves before sending.

---

## Example C — Complex contract review

Task:
> Review this 40-page contract and tell me the risks.

Possible flow:
1. Local document parser extracts text.
2. Home Brain indexes and summarizes sections.
3. Router determines complex legal reasoning is beneficial.
4. If cloud is allowed, send only required clauses/structured context to a Cloud Expert.
5. Final answer returns through Butler with provenance and cloud-use disclosure.

---

## Example D — Offline cooking

Task:
> What was the recipe I saved last month?

Flow:
1. Local memory search.
2. Deterministic recipe retrieval.
3. Tiny local model presents steps.
4. No internet required.

---

## Example E — Vehicle problem

Task:
> What does this warning light mean?

Flow:
1. Local vehicle profile identifies exact model.
2. Local vision model/tool if available.
3. Search local/manual data.
4. If uncertain and online permission exists, escalate to authoritative current sources/cloud vision.
5. Safety-critical uncertainty is preserved in the final answer.

---

# 4. Task decomposition

A single user request does not have to run entirely on one tier.

The Butler should break complex tasks into sub-tasks and route each independently.

Example:

> Plan my trip and pack my suitcase.

Subtasks:
- Read calendar → deterministic/local
- Retrieve travel preferences → local memory
- Current weather → internet
- Flight/hotel research → cloud/web
- Wardrobe inventory → local
- Outfit optimization → strong local/Home Brain
- Final conversational response → current-device model

This prevents sending entire private context to the cloud merely because one subtask requires internet access.

---

# 5. Privacy classes

Every memory/object should have a privacy classification usable by the Router.

Suggested classes:

### P0 — Public
Safe to expose publicly.

### P1 — Personal
Normal private preferences/history.

### P2 — Sensitive
Financial details, private messages, precise location history, personal documents.

### P3 — Highly Sensitive
Medical records, child wellbeing data, identity documents, secrets/credentials.

Skills can declare which classes they are allowed to read and which may be sent externally.

Default principle:

- P0 may be used anywhere.
- P1 can leave device only if user cloud policy permits.
- P2 requires stronger minimization and explicit policy.
- P3 should remain local by default and require very specific permission for external processing.

---

# 6. Cloud policies

User chooses a Butler cloud policy.

Possible presets:

### Local Only
Never use external AI.

### Ask Before Cloud
Butler requests permission each time cloud escalation is needed.

### Smart Private
Cloud can be used automatically for low-sensitivity tasks, but sensitive classes require permission.

### Best Available
Use cloud automatically when it significantly improves quality, subject to hard privacy exclusions.

The user can additionally allow/deny specific providers.

---

# 7. Butler Memory is not chat history

Synchronization should not revolve around copying full conversational transcripts between devices.

FUL.HOUSE should maintain a structured Personal Memory Graph.

Example edges:

Stan → owns → Vehicle BMW-X5
BMW-X5 → last_service → ServiceEvent-392
Stan → likes → Jazz
Stan → visited → Restaurant-73
Stan → cooked → Recipe-28
Stan → parent_of → ChildHouse-2

Each memory fact can include:

- ID
- Type
- Value
- Source
- Timestamp
- Confidence
- Owner
- Privacy class
- Provenance
- Device that created/updated it
- Expiration/retention policy where applicable
- Version/vector clock

---

# 8. Device synchronization

Approved devices synchronize encrypted graph changes rather than naïve database snapshots.

Each device maintains:

- Device ID
- Device keys
- Capability profile
- Local cache policy
- Last sync checkpoint

Synchronization should support offline-first operation.

Example:

1. Phone records a confirmed restaurant visit while offline.
2. Event is stored locally with a local version.
3. Phone reconnects.
4. Encrypted event delta syncs to Home Brain/other approved replicas.
5. House graph merges the new event.
6. Other devices receive the updated semantic object.

---

# 9. Conflict resolution

Conflicts are inevitable across devices.

FUL.HOUSE should avoid last-write-wins for important human facts when possible.

Examples:

- User corrects favorite restaurant on phone.
- Home Brain independently infers another preference.

Explicit user statements outrank inferred signals.

Suggested precedence:

1. Explicit user correction
2. Explicit user action
3. Trusted imported fact
4. High-confidence inference
5. Low-confidence inference

Conflicting high-value facts can be kept as candidates until resolved.

---

# 10. Capability registry

Every device registers its current capabilities.

Example:

Device: iPhone
- RAM: available snapshot
- NPU: yes
- Local model: tiny
- Camera: yes
- GPS: yes
- Battery: 62%
- Thermal: normal

Device: Mac mini Home Brain
- RAM: 32 GB
- GPU acceleration: yes
- Local model: 8B
- Always-on: yes
- Full memory index: yes

The Router should use real current capability state rather than hardcoded device names.

---

# 11. Dynamic model selection

Model selection can change during a session.

Example:

User asks a simple question on phone → Tiny Local.

Then uploads 50 documents → Router delegates indexing to Home Brain.

Then asks for strategic synthesis → Strong Local or Cloud Expert.

The visible Butler remains the same character throughout.

The user should not feel that they are switching bots.

---

# 12. Home Brain background jobs

When available, Home Brain can perform non-urgent heavy tasks while respecting power/privacy settings.

Examples:

- Reindex new documents
- Generate embeddings
- Deduplicate photos
- Build travel timelines
- Analyze recipe library
- Update wardrobe metadata
- Consolidate memory graph
- Prepare daily/weekly Butler briefing
- Locally fine-tune/update optional personal adapters

The House can surface a human-friendly summary:

> I organized 214 new photos and linked 37 of them to your Istanbul trip.

No promise of background completion should be made unless the system actually supports persistent execution.

---

# 13. Local adapters and personalization

Personalization should primarily live in structured memory and preferences.

Optional local adapters/LoRA can encode style and behavioral tendencies, not critical factual memory.

This makes personalization portable across model upgrades.

A model can be replaced without losing the Butler's identity.

---

# 14. Model upgrade path

The user may move from one device generation to another.

FUL.HOUSE should preserve:

- Butler Identity
- Memory Graph
- Skills
- Preferences
- Permissions
- Personal adapter where compatible

Then attach the best available runtime model on the new device.

This prevents the absurd situation where buying a new phone effectively causes the Butler to develop amnesia.

---

# 15. Skills influence routing

Each Butler Skill declares runtime needs.

Example Skill manifest:

Chef
- Needs: Kitchen Memory, timers, nutrition tools
- Preferred tier: Tiny/Strong Local
- Internet: optional
- Cloud: optional for complex recipe extraction

Mechanic
- Needs: Vehicle Memory, camera/audio, manuals
- Preferred tier: Strong Local/Home Brain
- Cloud: optional for difficult multimodal/current lookup

Health Assistant
- Needs: Medical Vault with strict P3 access
- Preferred tier: Local/Home Brain
- Cloud: restricted and explicit by policy

Travel Concierge
- Needs: Travel Memory, Life Map, web/current data
- Preferred tier: local orchestration + cloud/web sub-tasks

---

# 16. Visual Butler continuity

Changing compute tier must not visually replace the Butler.

Instead, the Butler may subtly indicate state:

- Offline/local mode
- Home Brain connected
- Consulting an Expert

But these are states of the same Butler, not different personalities.

Example:

> This needs current information. I'm consulting an online expert.

The response still comes from the Butler.

---

# 17. Network resilience

FUL.HOUSE should degrade gracefully.

If internet disappears:

- Local memory remains searchable.
- Tiny/strong local model remains usable.
- Cached documents remain available.
- Offline Kitchen, Garage, Wardrobe and House functions continue.
- Cloud-only sub-tasks are queued or reported unavailable.

The Butler should explain limitations rather than fail silently.

---

# 18. Battery and thermal awareness

Compute choice should respect device health.

Examples:

- Low battery → avoid heavy local model if Home Brain available.
- Device overheating → offload to Home Brain/cloud if permitted.
- Poor network → prefer local.
- Metered network → avoid large cloud transfer unless allowed.

User can choose performance modes:

- Privacy First
- Balanced
- Battery Saver
- Maximum Intelligence

---

# 19. Cost awareness

Cloud inference has cost.

The Router should understand provider/model cost and user limits.

Possible controls:

- Monthly cloud budget
- Per-task maximum
- Free-only mode
- Prefer personal API key
- Prefer FUL.HOUSE bundled credits

The Butler can say:

> I can do this locally with a shorter analysis, or use a cloud expert for a deeper review.

---

# 20. Security model

Core requirements:

- Per-device cryptographic identity
- Encrypted local storage
- End-to-end encrypted sync for private graph data where architecture permits
- Remote device revocation
- Key rotation
- Trusted recovery mechanism
- Explicit Home Brain pairing
- No automatic trust merely because devices share a network
- Cloud context minimization
- Audit log for sensitive external processing

---

# 21. Explainability

For sensitive or expensive tasks, the user should be able to see:

- Which device processed it
- Which model/provider was used
- Whether cloud was used
- What categories of data were shared
- Which sources informed the answer

This can live behind a simple "How did you answer this?" control rather than cluttering normal conversation.

---

# 22. Failure and fallback logic

If a selected tier fails:

1. Retry locally when appropriate.
2. Fall back to a lower-compute deterministic answer if possible.
3. Escalate upward only if user policy permits.
4. Preserve partial work.
5. Never silently send sensitive data to cloud merely because local inference failed.

---

# 23. Core architecture

Conceptually:

User Request
↓
Intent + Skill Resolver
↓
Privacy Classifier
↓
Context Builder
↓
Compute Router
↓
Deterministic / Tiny Local / Strong Local / Home Brain / Cloud Expert
↓
Tool Execution
↓
Memory Update Candidate
↓
Policy/Provenance Check
↓
Personal Memory Graph
↓
Butler Response

---

# 24. Product principles

**The Butler is not the model.**

**Use the smallest sufficient brain.**

**Local first. Home second. Cloud when needed.**

**Complex tasks may be split across multiple compute tiers.**

**Personal memory stays structurally separate from model weights.**

**A stronger device should make the same Butler smarter, not create a different Butler.**

**Cloud intelligence is borrowed. Butler identity remains at home.**

---

# 25. MVP architecture

A realistic first implementation can use three tiers rather than all five:

1. Deterministic tools
2. Tiny/medium local model on current device
3. Optional cloud expert

Memory Graph and Router abstractions should still be designed so Home Brain and stronger local tiers can be added later without redesigning the Butler identity layer.

Early MVP must prove:

- Offline Butler still works
- Same memory across two approved devices
- Router can choose local vs cloud
- Sensitive data can be excluded from cloud context
- Butler identity feels continuous regardless of backend model

Home Brain becomes the next major infrastructure milestone after this foundation is stable.