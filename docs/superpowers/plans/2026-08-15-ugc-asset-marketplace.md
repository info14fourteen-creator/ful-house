# UGC Asset Foundry & Marketplace Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first creator-driven asset pipeline so users can create, normalize, publish, acquire and place interoperable furniture/decor assets without requiring an internal FUL.HOUSE art team.

**Architecture:** Extend the universal HouseObject protocol from the core platform plan with a separate reusable HouseAsset layer. Creation, normalization, marketplace, inventory and placement are independent modules. Start with stylized 2D/2.5D furniture and surfaces; do not block the MVP on production-grade generative 3D.

**Tech Stack:** TypeScript application architecture from `docs/superpowers/plans/2026-08-15-ful-house-core-platform.md`; local/browser asset metadata persistence for prototype; pluggable AI Foundry provider; image/object storage behind an abstraction; deterministic validation and placement logic wherever possible.

## Global Constraints

- Follow `docs/UGC_ASSET_FOUNDRY_MARKETPLACE.md`.
- House Asset is distinct from placed HouseObject instance.
- Asset creator does not need to understand rendering-engine internals.
- Private digitization and commercial publication are separate permission flows.
- Marketplace publication requires provenance, rights declaration, moderation state and compatibility validation.
- The MVP supports stylized 2D/2.5D assets first; 3D generation is a later provider.
- Inventory ownership is independent from room placement.
- Marketplace settlement must use an economy interface; do not hard-code VIRT royalty economics into renderer or asset domain logic.
- Remix lineage is immutable provenance metadata.
- Functional media objects use provider adapters rather than embedding third-party service logic into asset definitions.
- Device performance variants/LOD are part of asset compatibility metadata.

---

### Task 1: HouseAsset domain contract

**Files:**
- Create: `app/core/assets/types.ts`
- Create: `app/core/assets/asset-registry.ts`
- Modify: `app/core/objects/types.ts`
- Test: `app/tests/core/assets.test.ts`

**Interfaces:**
- Produces: `HouseAsset`, `AssetFamily`, `AssetPlacement`, `AssetRights`, `AssetVersion`, `AssetPerformanceProfile`.

Required minimum contract:

```ts
export type AssetFamily =
  | 'FURNITURE'
  | 'RUG'
  | 'LIGHTING'
  | 'APPLIANCE'
  | 'ELECTRONICS'
  | 'WALL_FINISH'
  | 'FLOOR'
  | 'CEILING'
  | 'ART'
  | 'PLANT'
  | 'ARCHITECTURAL';

export interface HouseAsset {
  id: string;
  creatorId: string;
  family: AssetFamily;
  title: string;
  description: string;
  dimensions: { width: number; depth: number; height: number; unit: 'cm' };
  placement: { mode: 'FLOOR' | 'WALL' | 'CEILING' | 'SURFACE'; clearanceCm: number };
  materialTags: string[];
  styleTags: string[];
  performanceProfiles: string[];
  rightsId: string;
  provenanceRootId: string;
  version: number;
  status: 'DRAFT' | 'VALIDATING' | 'READY' | 'PUBLISHED' | 'REJECTED';
}
```

- [ ] Write failing tests proving one asset can be placed as multiple independent HouseObject instances.
- [ ] Verify changing a placed object's room/visibility does not mutate the shared asset definition.
- [ ] Implement registry/version validation.
- [ ] Run tests and typecheck.
- [ ] Commit as `feat: add reusable house asset domain`.

---

### Task 2: Creator input and Foundry job model

**Files:**
- Create: `app/core/assets/foundry/types.ts`
- Create: `app/core/assets/foundry/job-store.ts`
- Create: `app/providers/asset-foundry/provider.ts`
- Test: `app/tests/assets/foundry-jobs.test.ts`

**Interfaces:**
- Produces: `FoundryInput`, `FoundryJob`, `FoundryCandidate`, `AssetFoundryProvider`.

Supported MVP inputs:

```text
TEXT
IMAGE
IMAGE_PLUS_TEXT
REMIX
```

- [ ] Write failing tests creating a Foundry job from a sketch/photo plus description.
- [ ] Implement explicit job states: `QUEUED`, `ANALYZING`, `NORMALIZING`, `NEEDS_REVIEW`, `FAILED`, `APPROVED`.
- [ ] Preserve original creator inputs as provenance references.
- [ ] Ensure AI provider output is treated as candidate metadata, never trusted directly as published asset data.
- [ ] Run tests.
- [ ] Commit as `feat: add asset foundry job pipeline`.

---

### Task 3: Deterministic normalization and validation

**Files:**
- Create: `app/core/assets/foundry/normalize.ts`
- Create: `app/core/assets/foundry/validate.ts`
- Create: `app/core/assets/foundry/compatibility.ts`
- Test: `app/tests/assets/normalization.test.ts`

**Interfaces:**
- Produces: `normalizeCandidate()`, `validateAsset()`, `CompatibilityReport`.

- [ ] Write failing tests for invalid scale, missing placement anchor, excessive dimensions and unsupported performance profile.
- [ ] Implement normalization of units, category tags, placement metadata and safe defaults.
- [ ] Implement validation that rejects malformed or impossible placement metadata instead of silently fixing everything.
- [ ] Produce creator-readable validation errors.
- [ ] Run tests.
- [ ] Commit as `feat: normalize and validate foundry assets`.

---

### Task 4: MVP visual asset representation

**Files:**
- Create: `app/core/assets/render/types.ts`
- Create: `app/core/assets/render/asset-renderer.ts`
- Create: `app/ui/assets/asset-preview/**`
- Test: `app/tests/assets/rendering.test.ts`

**Interfaces:**
- Produces: `AssetVisualVariant`, `PerformanceClass`, `renderAssetPreview()`.

- [ ] Implement stylized 2D/2.5D image/sprite asset support with transparent background, canonical orientation and bounding box.
- [ ] Support at least `MOBILE_LITE` and `DESKTOP` visual variants.
- [ ] Add placement preview in an empty prototype room.
- [ ] Add test proving renderer selects compatible variant by device performance profile.
- [ ] Do not implement generative 3D in this task.
- [ ] Run tests and visual smoke check.
- [ ] Commit as `feat: add mvp asset renderer`.

---

### Task 5: Creator review and approval UX

**Files:**
- Create: `app/ui/creator/foundry-review/**`
- Create: `app/core/assets/foundry/approval.ts`
- Test: `app/tests/assets/approval.test.ts`

**Interfaces:**
- Produces creator edit/approve flow for title, dimensions, placement, tags, preview and rights declaration.

- [ ] Write failing test proving an AI candidate cannot be published before creator approval.
- [ ] Build review UI showing original input beside normalized output.
- [ ] Allow creator corrections to dimensions/category/placement metadata.
- [ ] Store corrections as explicit human-authored provenance.
- [ ] Run tests.
- [ ] Commit as `feat: add creator foundry approval flow`.

---

### Task 6: Rights, provenance and publication policy

**Files:**
- Create: `app/core/assets/rights/types.ts`
- Create: `app/core/assets/rights/policy.ts`
- Create: `app/core/assets/provenance.ts`
- Test: `app/tests/assets/rights.test.ts`

**Interfaces:**
- Produces: `AssetRightsDeclaration`, `PublicationPolicy`, `AssetProvenance`.

Publication modes:

```text
PRIVATE_PERSONAL
FREE_PUBLIC
PAID_ORIGINAL
LICENSED_BRAND
REMIX_PUBLIC
```

- [ ] Test that personal digitization of a branded object can remain private without granting paid publication rights.
- [ ] Test that paid publication requires creator rights declaration.
- [ ] Persist original creator and remix-parent ids immutably.
- [ ] Add moderation state independent of rights state.
- [ ] Run tests.
- [ ] Commit as `feat: add asset rights and provenance`.

---

### Task 7: Marketplace catalog

**Files:**
- Create: `app/core/marketplace/types.ts`
- Create: `app/core/marketplace/catalog.ts`
- Create: `app/ui/marketplace/**`
- Test: `app/tests/marketplace/catalog.test.ts`

**Interfaces:**
- Produces: `MarketplaceListing`, catalog search/filtering, listing detail view.

- [ ] Write failing tests filtering listings by room/category/style/price/performance compatibility.
- [ ] Implement listing state independent of asset publication state.
- [ ] Build marketplace browse/detail UI using generated previews.
- [ ] Show creator, provenance, compatibility and rights/remix information.
- [ ] Run tests.
- [ ] Commit as `feat: add house asset marketplace catalog`.

---

### Task 8: Inventory and entitlement

**Files:**
- Create: `app/core/inventory/types.ts`
- Create: `app/core/inventory/inventory-store.ts`
- Create: `app/core/inventory/acquisition.ts`
- Test: `app/tests/inventory/inventory.test.ts`

**Interfaces:**
- Produces: `InventoryEntitlement`, `AcquisitionSource`, `acquireAsset()`, `canPlaceAsset()`.

- [ ] Test created, purchased, free, inherited and gifted acquisition sources.
- [ ] Test that inventory persists when all placed instances are deleted.
- [ ] Test an unowned paid asset cannot be permanently placed outside preview mode.
- [ ] Implement economy adapter interface with fake/test provider; no real VIRT settlement yet.
- [ ] Run tests.
- [ ] Commit as `feat: add persistent house inventory`.

---

### Task 9: Room placement engine

**Files:**
- Create: `app/core/assets/placement/types.ts`
- Create: `app/core/assets/placement/placement-engine.ts`
- Create: `app/ui/house/placement-mode/**`
- Test: `app/tests/assets/placement.test.ts`

**Interfaces:**
- Produces: `PlacementCandidate`, `PlacementResult`, `placeAsset()`.

- [ ] Test floor item placement, wall item placement and collision rejection.
- [ ] Implement snap/anchor behavior for MVP room geometry.
- [ ] Support preview placement for unowned marketplace items without persisting ownership.
- [ ] Persist placement as HouseObject referencing asset id/version.
- [ ] Run tests and browser placement flow.
- [ ] Commit as `feat: place inventory assets in rooms`.

---

### Task 10: Try in My House

**Files:**
- Create: `app/core/assets/preview/try-in-house.ts`
- Modify: `app/ui/marketplace/**`
- Test: `app/tests/assets/try-in-house.test.ts`

**Interfaces:**
- Produces non-destructive preview session.

- [ ] Write failing test proving preview does not modify inventory or permanent room layout.
- [ ] Add `See this in my House` action from marketplace listing.
- [ ] Render temporary placement candidates using current room geometry/style.
- [ ] Allow purchase/acquisition transition from preview to owned placement through inventory/economy interfaces.
- [ ] Run tests.
- [ ] Commit as `feat: add try in my house preview`.

---

### Task 11: Collections

**Files:**
- Create: `app/core/assets/collections/types.ts`
- Create: `app/core/assets/collections/store.ts`
- Create: `app/ui/marketplace/collections/**`
- Test: `app/tests/assets/collections.test.ts`

**Interfaces:**
- Produces: `AssetCollection`, collection entitlement and partial placement.

- [ ] Test collection contains multiple assets without duplicating asset definitions.
- [ ] Support collection preview and acquisition.
- [ ] Allow user to place only selected assets from an owned collection.
- [ ] Run tests.
- [ ] Commit as `feat: add creator asset collections`.

---

### Task 12: Remix graph

**Files:**
- Create: `app/core/assets/remix/types.ts`
- Create: `app/core/assets/remix/remix-service.ts`
- Test: `app/tests/assets/remix.test.ts`

**Interfaces:**
- Produces: `RemixPolicy`, `RemixEdge`, `createRemixDraft()`.

- [ ] Test `NO_REMIX` rejects derived draft.
- [ ] Test attributed remix stores immutable parent linkage.
- [ ] Test royalty metadata is stored as policy reference, not calculated by renderer.
- [ ] Show lineage in creator and marketplace views.
- [ ] Run tests.
- [ ] Commit as `feat: add asset remix provenance graph`.

---

### Task 13: Surface assets

**Files:**
- Create: `app/core/assets/surfaces/types.ts`
- Create: `app/core/assets/surfaces/apply-surface.ts`
- Test: `app/tests/assets/surfaces.test.ts`

**Interfaces:**
- Produces repeatable wall/floor/ceiling material assets.

- [ ] Add `WALL_FINISH`, `FLOOR` and `CEILING` preview/apply tests.
- [ ] Model coverage/tiling scale separately from furniture dimensions.
- [ ] Support surface assets inside collections.
- [ ] Run tests.
- [ ] Commit as `feat: add marketplace surface assets`.

---

### Task 14: Auto Furnish MVP

**Files:**
- Create: `app/core/assets/auto-furnish/types.ts`
- Create: `app/core/assets/auto-furnish/planner.ts`
- Create: `app/ui/house/auto-furnish/**`
- Test: `app/tests/assets/auto-furnish.test.ts`

**Interfaces:**
- Produces: `AutoFurnishRequest`, `AutoFurnishPlan`, `applyFurnishPlan()`.

MVP constraint: owned inventory only.

- [ ] Test planner respects room geometry and inventory ownership.
- [ ] Test planner never purchases marketplace items in MVP.
- [ ] Implement deterministic candidate filtering before any AI ranking: room compatibility, placement, collision, performance class.
- [ ] Allow AI/heuristic ranking of remaining valid combinations by style preference.
- [ ] Show proposed layout and require explicit apply action.
- [ ] Run tests.
- [ ] Commit as `feat: add owned inventory auto furnish`.

---

### Task 15: Creator Studio storefront

**Files:**
- Create: `app/ui/creator/studio/**`
- Create: `app/core/creator/types.ts`
- Test: `app/tests/creator/studio.test.ts`

**Interfaces:**
- Produces creator profile/store view with published assets, collections and drafts.

- [ ] Build Studio showing spatial previews plus normal searchable catalog fallback.
- [ ] Allow visitor to open an asset and route to marketplace acquisition.
- [ ] Do not expose creator private drafts to visitors.
- [ ] Run tests.
- [ ] Commit as `feat: add creator studio storefront`.

---

### Task 16: Marketplace moderation and abuse controls

**Files:**
- Create: `app/core/assets/moderation/types.ts`
- Create: `app/core/assets/moderation/pipeline.ts`
- Test: `app/tests/assets/moderation.test.ts`

**Interfaces:**
- Produces: `ModerationResult`, `TechnicalSafetyResult`, `PublicationGate`.

- [ ] Test technically invalid, malicious-link and unreviewed-rights assets cannot publish.
- [ ] Separate technical validation from content/rights moderation.
- [ ] Add duplicate/spam signal hooks without auto-deleting creator work.
- [ ] Ensure moderation failures return actionable reasons and preserve private draft.
- [ ] Run tests.
- [ ] Commit as `feat: add asset publication moderation gates`.

---

### Task 17: End-to-end creator-to-room test

**Files:**
- Create: `app/tests/e2e/creator-marketplace-house.spec.ts`
- Modify relevant UI modules only if test reveals integration defects.

**Scenario:**

```text
Creator uploads chair sketch + prompt
→ Foundry candidate generated
→ creator corrects dimensions
→ rights declared
→ validation passes
→ asset published free
→ second user opens Marketplace
→ Try in My House
→ acquires asset
→ asset appears in Inventory
→ places it in Living Room
→ room stores HouseObject referencing HouseAsset
```

- [ ] Write complete E2E test before integration fixes.
- [ ] Run and record failing boundary.
- [ ] Fix only the failing integrations.
- [ ] Run all asset, marketplace, inventory and core tests.
- [ ] Run typecheck and production build.
- [ ] Commit as `test: verify creator marketplace house flow`.

---

## Post-MVP plans, not part of this implementation

Create separate specs/plans before implementing:

- Generative 3D Foundry
- Advanced automatic mesh repair and LOD generation
- Marketplace royalty/VIRT settlement
- Verified brand marketplace
- Physical product purchase/affiliate mappings
- Full Room Packs and Architecture Packs
- Gift/trade/resale policy
- Creator analytics
- Human moderation operations
- Collaborative creation

---

## Acceptance criteria

The milestone is complete when a non-3D-artist can submit an image/sketch and description, approve a normalized interoperable asset, publish it, another user can discover and preview it in their own House, acquire it into Inventory and place it in a room. The platform must preserve creator provenance and rights state throughout the flow, while remaining independent of any single AI generation or rendering provider.