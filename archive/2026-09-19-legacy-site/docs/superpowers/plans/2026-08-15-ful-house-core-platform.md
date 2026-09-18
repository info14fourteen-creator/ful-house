# FUL.HOUSE Core Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the existing static ful.house repository into the first working foundation for a privacy-first digital House with room-scoped Butler contexts, functional House Objects, trusted-device security, local-first memory, compute routing, and future inheritance support.

**Architecture:** Do not attempt to implement the full product vision in one release. First establish the universal primitives that every future room depends on: House, Room, HouseObject, ButlerContext, Capability, MemoryRecord, Device, Vault and permission policy. The UI can remain lightweight while these contracts stabilize; specialized rooms such as Kitchen, Garage, Wardrobe, Travel and Health then become plugins/configurations over the same primitives rather than separate applications.

**Tech Stack:** Existing static HTML/CSS/JS site for the current public shell; new application code should use TypeScript and a component-based web application architecture selected during Task 1 after repository/toolchain audit. Browser persistence for the prototype must use IndexedDB/WebCrypto. Production sync must be end-to-end encrypted and transport-agnostic. Local AI runtime must implement the compute-ladder contract from `docs/BUTLER_RUNTIME_DEVICE_SYNC_AND_COMPUTE_LADDER.md` rather than hard-coding a single model provider.

## Global Constraints

- Local first: private House data is processed locally whenever practical.
- The Butler is not the model. Butler Identity, Memory, Skills and active Model are separate concepts.
- Use the smallest sufficient compute tier for each task.
- Room determines primary Butler context, tools, permissions and visual uniform.
- Cross-room access is capability-based; a room does not receive another room's unrestricted memory.
- House Objects use one universal object protocol and can be `REAL`, `WISH` or `DIGITAL`.
- Private Vault documents are encrypted at rest and are never public by default.
- A six-digit PIN may unlock a trusted device UX but must not be the cryptographic root secret.
- Every trusted device has its own key and can be individually revoked.
- Cloud AI receives only the minimum task-specific context allowed by policy.
- Current location, health data, private documents and credentials are never public by default.
- Inactivity is not proof of death. Inheritance is an owner-configured claim process with a waiting period and cancellation on verified owner activity.
- Existing public website files must remain deployable while the new application foundation is introduced.

---

## File Structure Target

The exact framework bootstrap is decided in Task 1, but the domain boundaries below are mandatory:

```text
app/
  core/
    house/
    rooms/
    objects/
    butler/
    memory/
    permissions/
    devices/
    vault/
    sync/
    inheritance/
  rooms/
    living-room/
    kitchen/
    garage/
    wardrobe/
    travel/
    library/
    media/
    office/
  providers/
    ai/
    media/
    storage/
  ui/
    house/
    butler/
    rooms/
    objects/
  tests/
```

No room may bypass `permissions`, `memory` or `objects` to access another room's internal data directly.

---

### Task 1: Repository and application bootstrap

**Files:**
- Inspect: `README.md`, `index.html`, `assets/**`, `docs/**`
- Create: application package/config files appropriate to the selected TypeScript web stack
- Create: `app/core/**` skeleton
- Create: `app/tests/smoke/**`

**Interfaces:**
- Produces: runnable development app, test runner, formatter/linter, typed build, and a route/screen that renders a minimal empty House.

- [ ] Audit the current repository and document how the existing static site is deployed before changing build behavior.
- [ ] Choose the smallest component-based TypeScript web stack compatible with that deployment. Prefer a client-first architecture for the prototype; do not introduce a server framework merely to render an empty House.
- [ ] Add one failing smoke test asserting that the app can instantiate and render a House with an id and owner id.
- [ ] Run the test and confirm failure before implementation.
- [ ] Implement only enough application bootstrap and `House` model to make the smoke test pass.
- [ ] Run tests, typecheck and production build.
- [ ] Verify the existing public static pages remain reachable/deployable or explicitly isolate the new app under a non-conflicting path during migration.
- [ ] Commit as `feat: bootstrap ful house application core`.

---

### Task 2: Universal House, Room and HouseObject domain model

**Files:**
- Create: `app/core/house/types.ts`
- Create: `app/core/rooms/types.ts`
- Create: `app/core/objects/types.ts`
- Create: `app/core/objects/object-registry.ts`
- Test: `app/tests/core/objects.test.ts`

**Interfaces:**
- Produces: `House`, `Room`, `HouseObject`, `ObjectReality`, `ObjectVisibility`, `ObjectAction`, `ObjectRegistry`.

Required contracts:

```ts
export type ObjectReality = 'REAL' | 'WISH' | 'DIGITAL';
export type ObjectVisibility = 'PRIVATE' | 'HOUSEHOLD' | 'PUBLIC';

export interface HouseObject {
  id: string;
  houseId: string;
  roomId: string;
  type: string;
  title: string;
  reality: ObjectReality;
  visibility: ObjectVisibility;
  sourceIds: string[];
  actionIds: string[];
  memoryIds: string[];
  createdAt: string;
  updatedAt: string;
}

export interface Room {
  id: string;
  houseId: string;
  type: string;
  title: string;
  primarySkillId: string;
  allowedCapabilityIds: string[];
}
```

- [ ] Write failing tests for registering a `REAL` sofa, a `WISH` sofa and a `DIGITAL` television without creating separate domain models for each reality state.
- [ ] Run tests and verify failure.
- [ ] Implement the contracts and registry with explicit validation for owner/house/room identity.
- [ ] Add tests proving objects expose actions by id rather than embedding arbitrary executable code in persisted object data.
- [ ] Run tests and typecheck.
- [ ] Commit as `feat: add universal house object protocol`.

---

### Task 3: Room-scoped Butler context and uniforms

**Files:**
- Create: `app/core/butler/types.ts`
- Create: `app/core/butler/context-router.ts`
- Create: `app/core/butler/skill-registry.ts`
- Create: `app/core/butler/uniform-registry.ts`
- Test: `app/tests/core/butler-context.test.ts`

**Interfaces:**
- Produces: `ButlerIdentity`, `ButlerSkill`, `ButlerContext`, `UniformDescriptor`, `activateRoomContext(roomId)`.

Required behavior:

```text
Kitchen -> Chef skill + chef uniform + Kitchen capabilities
Garage -> Mechanic skill + mechanic uniform + Garage capabilities
Wardrobe -> Stylist skill + stylist uniform + Wardrobe capabilities
Travel -> Concierge skill + concierge uniform + Travel capabilities
Library -> Librarian/Research skill
Media -> Media/Music skill
Office -> Work skill
Health -> Health Assistant skill
```

- [ ] Write failing tests showing that entering Kitchen activates Chef context and entering Garage replaces the primary context with Mechanic without changing Butler identity.
- [ ] Add a test proving Butler identity remains constant across room changes.
- [ ] Implement context routing and uniform metadata.
- [ ] Add one UI proof: moving between two prototype rooms visibly changes Butler uniform/role label.
- [ ] Run unit tests and a browser interaction test.
- [ ] Commit as `feat: add room scoped butler contexts`.

---

### Task 4: Capability-based cross-room requests

**Files:**
- Create: `app/core/permissions/capabilities.ts`
- Create: `app/core/permissions/policy-engine.ts`
- Create: `app/core/rooms/cross-room-bus.ts`
- Test: `app/tests/core/cross-room-permissions.test.ts`

**Interfaces:**
- Produces: `Capability`, `CapabilityRequest`, `CapabilityResult`, `PolicyDecision`, `requestCapability()`.

Example allowed flow:

```text
Travel asks Wardrobe: getPackingCandidates(tripConstraints)
Travel asks Health: getTravelConstraints()
Travel does NOT read Medical Vault directly.
```

- [ ] Write a failing test where Travel requests wardrobe packing candidates and receives a constrained response.
- [ ] Write a failing test where Travel attempts raw Medical Vault access and receives `DENY`.
- [ ] Implement policy evaluation using house, room, owner, capability and sensitivity metadata.
- [ ] Ensure capability responses can be redacted/aggregated before leaving the source room.
- [ ] Run tests.
- [ ] Commit as `feat: enforce cross room capability permissions`.

---

### Task 5: Personal Memory Graph with provenance

**Files:**
- Create: `app/core/memory/types.ts`
- Create: `app/core/memory/memory-store.ts`
- Create: `app/core/memory/query.ts`
- Test: `app/tests/core/memory.test.ts`

**Interfaces:**
- Produces: `MemoryRecord`, `MemorySource`, `MemorySensitivity`, `MemoryQuery`.

Required fields:

```ts
export interface MemoryRecord {
  id: string;
  houseId: string;
  subjectId: string;
  predicate: string;
  object: unknown;
  sourceId: string;
  timestamp: string;
  confidence: number;
  sensitivity: 'PUBLIC' | 'PRIVATE' | 'SENSITIVE' | 'HIGHLY_SENSITIVE';
  ownerId: string;
  deviceId?: string;
}
```

- [ ] Write failing tests for storing a preference, vehicle service event and restaurant visit with provenance.
- [ ] Write a test proving a public query cannot return `HIGHLY_SENSITIVE` records.
- [ ] Implement local memory persistence behind a storage interface.
- [ ] Add deterministic conflict rules: explicit user correction outranks inference; newer explicit correction supersedes older inference without deleting provenance.
- [ ] Run tests.
- [ ] Commit as `feat: add provenance aware personal memory graph`.

---

### Task 6: Compute Ladder router

**Files:**
- Create: `app/core/butler/compute/types.ts`
- Create: `app/core/butler/compute/router.ts`
- Create: `app/providers/ai/local-provider.ts`
- Create: `app/providers/ai/home-brain-provider.ts`
- Create: `app/providers/ai/cloud-provider.ts`
- Test: `app/tests/core/compute-router.test.ts`

**Interfaces:**
- Produces: `ComputeTier`, `TaskEnvelope`, `ComputePolicy`, `ComputeDecision`, `routeTask()`.

Required tiers:

```text
T0 deterministic tools
T1 tiny local model
T2 strong local device model
T3 Home Brain
T4 Cloud Expert
```

- [ ] Write failing routing tests: calculator -> T0; short private rewrite -> T1; large local document analysis on capable laptop -> T2; overnight photo indexing -> T3; current complex research with cloud allowed -> T4.
- [ ] Add tests proving cloud is never selected when `cloudPolicy = NEVER`.
- [ ] Add tests proving `ASK` returns an escalation request rather than silently transmitting context.
- [ ] Implement routing using task complexity, required modality, freshness, device capabilities, privacy, latency and cost policy.
- [ ] Implement task decomposition so one request can use multiple tiers without sending full House memory to every tier.
- [ ] Log routing decisions locally without storing sensitive prompt bodies by default.
- [ ] Run tests.
- [ ] Commit as `feat: add butler compute ladder router`.

---

### Task 7: Trusted devices and House key hierarchy

**Files:**
- Create: `app/core/devices/types.ts`
- Create: `app/core/devices/device-registry.ts`
- Create: `app/core/devices/pairing.ts`
- Create: `app/core/vault/crypto.ts`
- Test: `app/tests/core/device-pairing.test.ts`

**Interfaces:**
- Produces: `TrustedDevice`, `DeviceScope`, `PairingChallenge`, `HouseKeyEnvelope`.

- [ ] Write failing tests for adding iPhone, Mac and iPad as independent trusted devices.
- [ ] Write a test proving revoking the Mac does not revoke the iPhone.
- [ ] Write a test proving a six-digit UI PIN alone cannot reconstruct the House master key.
- [ ] Implement WebCrypto-based prototype key generation and per-device wrapped key envelopes.
- [ ] Implement pairing challenge flow suitable for QR/deep-link confirmation from an existing trusted device.
- [ ] Support device scopes such as `FULL`, `NO_MEDICAL`, `NO_VAULT`, `PUBLIC_ONLY`.
- [ ] Run tests and document which pieces are prototype-only and require native secure-enclave/keychain integration on mobile/desktop clients.
- [ ] Commit as `feat: add trusted device key hierarchy`.

---

### Task 8: Private Desk / Vault

**Files:**
- Create: `app/core/vault/types.ts`
- Create: `app/core/vault/vault-store.ts`
- Create: `app/ui/rooms/private-desk/**`
- Test: `app/tests/core/vault.test.ts`

**Interfaces:**
- Produces: encrypted `VaultDocument`, local open/import/delete/export operations and device-scope checks.

- [ ] Write failing tests for storing birth certificate metadata and encrypted bytes locally.
- [ ] Test that `PUBLIC_ONLY` and `NO_VAULT` devices cannot decrypt Vault contents.
- [ ] Implement encrypted local storage with metadata minimized outside the ciphertext.
- [ ] Implement the physical UX metaphor: private desk/drawer opens only after local authentication.
- [ ] Ensure documents never become House Objects with public visibility unless an explicit derived/share object is created.
- [ ] Run tests and browser flow.
- [ ] Commit as `feat: add encrypted private desk vault`.

---

### Task 9: Device synchronization protocol

**Files:**
- Create: `app/core/sync/types.ts`
- Create: `app/core/sync/change-log.ts`
- Create: `app/core/sync/merge.ts`
- Create: `app/core/sync/transport.ts`
- Test: `app/tests/core/sync.test.ts`

**Interfaces:**
- Produces: encrypted change envelopes, logical clocks/version metadata, deterministic merge rules and transport abstraction.

- [ ] Write failing test: iPhone adds restaurant memory offline, Mac adds wardrobe item offline, later sync preserves both.
- [ ] Write failing conflict test: inferred preference on Mac vs explicit correction on iPhone; explicit correction wins while both provenance records remain.
- [ ] Implement append-only local change log and deterministic merge.
- [ ] Encrypt sync payloads before transport; transport must never require plaintext House data.
- [ ] Keep media blobs and memory metadata independently syncable to avoid forcing full photo libraries onto weak devices.
- [ ] Run tests.
- [ ] Commit as `feat: add encrypted house sync protocol`.

---

### Task 10: Home Brain discovery and delegation

**Files:**
- Create: `app/core/butler/compute/home-brain.ts`
- Create: `app/core/devices/capability-profile.ts`
- Test: `app/tests/core/home-brain.test.ts`

**Interfaces:**
- Produces: `DeviceCapabilityProfile`, `HomeBrainStatus`, delegation handshake.

- [ ] Write failing tests showing a capable desktop can advertise T3 and a phone can delegate an allowed task to it.
- [ ] Ensure Home Brain receives only the task capability and context slice authorized by policy.
- [ ] Implement availability/fallback behavior: unavailable Home Brain returns task to router for T1/T2/T4 decision.
- [ ] Add background-job contract for indexing, embeddings and media analysis.
- [ ] Run tests.
- [ ] Commit as `feat: add home brain delegation`.

---

### Task 11: Functional media objects and provider adapters

**Files:**
- Create: `app/providers/media/types.ts`
- Create: `app/providers/media/provider-registry.ts`
- Create: `app/rooms/media/media-object-actions.ts`
- Test: `app/tests/rooms/media.test.ts`

**Interfaces:**
- Produces provider modes `NATIVE`, `EMBEDDED`, `LINKED` and media actions such as `play`, `pause`, `openProvider`.

- [ ] Write failing tests proving a television object can use an embedded provider while a book object can fall back to linked provider behavior.
- [ ] Implement provider adapters without making YouTube, Spotify, LitRes or any single service part of the core domain model.
- [ ] Add a capability declaration so commercial/API restrictions can disable embedding without breaking the room.
- [ ] Build one prototype embedded video provider and one linked book/music provider.
- [ ] Run