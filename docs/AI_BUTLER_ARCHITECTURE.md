# FUL.HOUSE — AI Butler Architecture

## Product principle

The AI Butler is the operating layer of a FUL.HOUSE.

It should work locally by default, remain useful with no Internet connection, learn from the owner over time, and become significantly smarter when optional cloud models are available.

The desired product behavior is:

**Offline first. Private by default. Smarter when connected.**

The local Butler should never feel like a disabled demo mode. It must still be able to perform everyday personal-assistant tasks without cloud inference.

---

## Two-tier intelligence model

### Tier 1 — Local Butler

Runs entirely on the user's device.

Baseline candidate: **Gemma 3 270M IT / FunctionGemma-class 270M model**, quantized for on-device use.

The local layer is responsible for:

- classifying incoming mail;
- extracting people, dates, companies, tasks, deadlines and intent;
- ranking and sorting inbox items;
- identifying newsletters, receipts, confirmations, invitations and likely spam;
- producing short summaries of messages;
- suggesting short replies from templates plus user memory;
- rewriting or polishing short messages;
- drafting simple replies when the context is narrow and well-grounded;
- routing actions to deterministic tools;
- retrieving memories from the local personal memory store;
- answering basic questions about the owner's house and activity;
- updating the House Manifest from known structured signals;
- managing local notifications, reminders and house-state events;
- executing safe, deterministic function calls such as opening a room, retrieving a document, preparing a reply draft, or filing an email.

The local model should NOT be trusted as a general-purpose reasoning engine for high-stakes legal, medical, financial or complex professional work.

For difficult tasks, it should either use deterministic tools, request cloud intelligence when allowed, or clearly state that the task exceeds the offline model's capability.

---

## Tier 2 — Connected Butler

When Internet access exists and the owner permits it, the Butler may temporarily delegate difficult reasoning to a larger cloud model.

Possible providers should be modular rather than hard-coded into the product architecture.

Cloud mode can be used for:

- long or ambiguous email threads;
- sophisticated message drafting;
- deep research;
- legal or technical document analysis;
- multi-step planning;
- difficult coding tasks;
- complex cross-source reasoning;
- interpreting large amounts of connected social/profile data;
- initial synthesis of a new owner's digital identity;
- generating major House redesign proposals.

The important product behavior is that the **cloud model is a temporary expert hired by the local Butler**, not the owner's primary memory.

Personal memory remains local unless the owner explicitly permits selected context to be sent.

---

## Smart routing

Every request should first pass through a local capability router.

Example policy:

1. Can this be completed deterministically without an LLM? Use a local tool.
2. Can the local 270M model handle it reliably? Use the local model.
3. Does it require personal memory? Retrieve the minimum relevant local memory.
4. Is the task complex and Internet/cloud access allowed? Escalate selected context to a cloud model.
5. If cloud access is unavailable, produce the best local result and explain the limitation when material.

The Butler should therefore get "smarter" when connected without becoming useless when disconnected.

---

## Why a 270M model can still be useful

A model this small should not be marketed as a tiny ChatGPT replacement.

Its strength is specialization.

For FUL.HOUSE, the valuable tasks are often narrow and repetitive:

- "Is this email important?"
- "Who sent it?"
- "Is there a deadline?"
- "What does this person want?"
- "Give me a two-sentence summary."
- "Which of my known reply patterns fits this?"
- "Create a short reply using these facts."
- "Which tool should I call?"
- "Which room/object/source does this data belong to?"

These are much more realistic on-device tasks for a specialized tiny model than open-ended general reasoning.

Google describes Gemma 3 270M as a compact model intended for task-specific fine-tuning, strong instruction following, text structuring, classification and data extraction. FunctionGemma-class variants further emphasize tool/function calling and show large gains after specialization.

Product implication:

**Do not ask one 270M model to be brilliant at everything. Train the Butler to be excellent at the owner's recurring workflows.**

---

## Personalization architecture

The Butler should not constantly retrain all base-model weights on raw user data.

Instead use four layers:

### 1. Base model

Shared compact language model installed with FUL.HOUSE.

### 2. Personal memory

Local structured and semantic storage containing facts learned about the owner.

Examples:

- people and relationships;
- projects;
- companies;
- writing preferences;
- frequent recipients;
- recurring decisions;
- important dates;
- interests;
- work history;
- house history;
- preferred tone by recipient;
- frequently used documents;
- user-approved autobiographical facts.

### 3. Personal behavior model / adapter

A small adapter or specialized model may periodically learn recurring behavior patterns, such as:

- how the owner writes to friends versus clients;
- preferred reply length;
- common email actions;
- vocabulary and language switching;
- which messages the owner considers important;
- which recommendations they accept or reject.

This adapter should learn style and behavior more than factual memory.

### 4. Deterministic tools

Calendar, mail, contacts, files, social connectors, House state, commerce, reminders and other capabilities should be exposed as structured functions.

The model decides **what** needs to happen; deterministic code performs the action.

---

## Mail Butler

Email is a strong first real-world use case because it provides frequent recurring interactions and high-value personal signals.

### Offline-capable workflow

When mail has already synchronized to the device, the Butler can locally:

- categorize messages;
- extract tasks;
- summarize threads;
- identify known people;
- propose replies;
- learn whether the owner archives, responds, delegates or ignores similar messages;
- update the owner's relationship graph and project context;
- prepare actions for later synchronization.

Sending or receiving new remote mail obviously requires a network connection, but understanding synchronized mail does not need cloud AI.

### Drafting strategy

For simple replies:

`message + relevant thread context + recipient relationship + user style memory + known facts -> local draft`

For complex replies:

`local Butler prepares minimum necessary context -> optional cloud model -> local Butler reviews/grounds output -> user receives draft`

This prevents the cloud model from becoming the permanent keeper of personal context.

---

## Butler memory lifecycle

The Butler should distinguish between:

- **ephemeral context** — temporary details used for one task;
- **working memory** — active projects and conversations;
- **long-term memory** — stable facts and preferences;
- **archive memory** — historical data retained because the owner wants the House to remember it.

Not everything should automatically become permanent memory.

The owner must be able to inspect, correct, delete and export what the Butler believes about them.

A useful product view could be:

**What my Butler knows about me**

This should be a first-class privacy feature, not a hidden debug screen.

---

## Privacy rule

A strong FUL.HOUSE promise:

> **Your Butler knows you. FUL.HOUSE doesn't have to.**

Default architecture:

- personal memory encrypted locally;
- model inference local whenever possible;
- explicit permission for cloud escalation;
- minimum-context disclosure to external models;
- per-source privacy controls;
- user-visible activity log of what was sent to cloud providers;
- ability to disable cloud AI entirely.

---

## House integration

The Butler is not a chat window bolted onto the product.

It exists inside the House and controls the environment.

Examples:

- LinkedIn connection creates professional signals and may unlock an Office.
- Instagram analysis creates albums or discovers hobbies that unlock new rooms.
- GitHub activity updates the Workshop.
- A new professional service creates an object in the owner's Office.
- Unread important messages may appear as physical mail on the Butler's desk.
- Long absence creates dust and environmental decay.
- Return triggers a Butler briefing.
- Completed work and earned VIRT visibly affect the House.

The Butler therefore converts digital activity into spatial state.

---

## Example return briefing

A returning owner might hear:

> Welcome home. While you were away, 18 people visited. Two clients asked about your contract-review service. I prepared three email replies for you. Your GitHub project was updated, so I refreshed the Workshop. You earned 420 VIRT. Also, the cat knocked over a plant.

The important point is that most of this briefing can be assembled locally from structured events and local memory. A large cloud model is optional, not mandatory.

---

## Technical direction for MVP

Recommended experiments:

1. Quantized Gemma 3 270M IT as baseline local language model.
2. FunctionGemma-style function-call model for routing and deterministic actions.
3. Local SQLite database for structured memory.
4. Local embeddings/vector index for semantic retrieval.
5. Small task-specific classifiers where they outperform a general tiny LLM.
6. Cloud-model gateway with strict context minimization.
7. House Manifest as structured JSON generated/updated from Butler decisions.
8. Local encrypted event log for memory provenance.

Do not lock the product to a single base model. The local-model abstraction should allow replacement as better sub-1B models appear.

---

## Product metric

The core test is not "Does the local model answer every question?"

It is:

**How much of the owner's ordinary digital life can the Butler handle privately, locally and at zero inference cost?**

Cloud intelligence should then increase quality for exceptional tasks rather than subsidize every mundane interaction.
