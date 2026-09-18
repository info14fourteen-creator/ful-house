# FUL.HOUSE — UGC Asset Foundry, Marketplace & Creator Economy

## Core idea

FUL.HOUSE should not depend on an internal art team to create the world's furniture, walls, carpets, appliances, decor and room styles.

The platform should define the **rules, standards and tools**. The visual world itself should be created and expanded by users.

A person can draw, photograph, describe, remix or upload an object. AI converts that input into a standardized FUL.HOUSE asset that can be safely placed inside compatible Houses.

**We build the laws of the world. Users build the world.**

---

# 1. House Asset

A House Asset is a reusable standardized visual object or surface used inside a House.

Possible asset families:

- Furniture
- Rugs/carpets
- Lighting
- Appliances
- Electronics
- Kitchen objects
- Bathroom objects
- Doors
- Windows
- Wall finishes
- Flooring
- Ceiling finishes
- Paint/materials
- Art
- Plants
- Garage equipment
- Garden objects
- Architectural elements
- Room layouts
- Full room packs
- Full style/architecture packs

The creator should not need to understand 3D-engine implementation details.

---

# 2. Asset reality states

Every compatible House Asset can use the broader FUL.HOUSE object reality model:

- `REAL` — represents a real physical item owned by the user.
- `WISH` — item the user wants or dreams about but does not currently own.
- `DIGITAL` — virtual-only item.

A single asset can evolve.

Example:

DIGITAL designer sofa → becomes a physical manufactured product → receives a REAL product mapping.

Personal digitization and commercial publication are separate permissions.

---

# 3. Asset Foundry

The **Asset Foundry** turns raw human input into a standardized asset.

Accepted creator inputs can include:

- Text prompt
- Hand drawing
- Photo
- Multiple photos
- Short video
- Existing supported 3D asset
- Remix of another FUL.HOUSE asset

Example:

> Create an Italian 1970s futuristic lounge chair in dark brown leather.

or upload a drawing/photo.

The Foundry produces a normalized candidate asset.

---

# 4. FUL.HOUSE Asset Standard

Every published asset must expose structured metadata rather than behaving as an arbitrary raw file.

Example schema fields:

- Asset id
- Creator id
- Asset family/category
- Name
- Description
- Dimensions
- Scale
- Orientation
- Placement mode
- Floor/wall/ceiling anchors
- Required clearances
- Collision volume
- Materials
- Color variants
- Style tags
- Room compatibility
- Device performance class
- Level-of-detail variants
- Lighting/shadow behavior
- Animation hooks if applicable
- Interaction/action hooks if applicable
- Reality state compatibility
- Rights/license metadata
- Remix policy
- Provenance chain
- Moderation status
- Version

The user publishes a **FUL.HOUSE object**, not merely a Blender file.

---

# 5. AI normalization pipeline

Candidate assets pass through an automated Foundry pipeline.

Input
→ interpretation
→ geometry/material normalization
→ scale estimation
→ anchor generation
→ collision generation
→ LOD generation
→ mobile optimization
→ metadata generation
→ style/category tagging
→ rights/moderation checks
→ compatibility testing
→ preview generation
→ creator approval
→ publication

The creator should not need to know what LOD, collision meshes or mobile budgets are.

FUL.HOUSE owns the normalization burden.

---

# 6. Compatibility testing

Before marketplace publication, assets should be automatically tested in synthetic House environments.

Test scenarios should include:

- Small rooms
- Large rooms
- Different floor heights
- Different wall materials
- Different lighting
- Mobile rendering budget
- Desktop rendering budget
- Collision with walls/floors
- Placement rotation
- Multiple copies of the same asset
- Combination with common furniture classes

The Foundry should auto-repair safe technical defects where possible or return a clear creator-facing validation error.

---

# 7. Creator publication modes

A creator can choose:

- Private asset
- Shared free asset
- Paid marketplace asset
- Collection-only asset
- Remixable asset
- Non-remixable asset
- Remixable with royalty

Publication requires explicit rights confirmation.

Digitizing a real branded item for personal use does not automatically grant marketplace rights.

---

# 8. Marketplace

The marketplace is the public discovery and acquisition layer for House Assets.

Users can browse by:

- Room
- Object type
- Style
- Creator
- Collection
- Price
- Popularity
- New releases
- Performance/device compatibility
- REAL/WISH/DIGITAL compatibility

A purchase adds the asset entitlement to the buyer's House Inventory.

Initial settlement can use VIRT as the internal platform economy, subject to the separate economy specification.

---

# 9. House Inventory

A user's Inventory tracks assets they can place in owned Houses.

Inventory sources:

- Created by user
- Purchased
- Free acquisition
- Personal digitization
- Inherited
- Gifted
- Licensed through collection

Inventory is independent from current placement.

Moving to a new House does not destroy owned assets.

---

# 10. Creator Studio

Creators should have a dedicated Studio/Workshop inside their own House.

The Studio can show:

- Published assets
- Drafts
- Sales
- Collections
- Remix lineage
- Ratings/usage where appropriate
- Earnings

Visitors can experience objects spatially rather than only seeing product cards.

Example:

A visitor sits in a creator's chair and selects:

> Add to my House — 320 VIRT

The creator's House becomes their storefront.

---

# 11. Collections and room packs

Creators can publish coordinated sets.

Example:

**Kyoto Collection**
- Sofa
- Chairs
- Lamps
- Table
- Rug
- Wall finish
- Flooring
- Door

Collections may support one-click room styling.

Later, creators can publish:

- Room Packs
- Architecture Packs
- Seasonal Packs
- Theme Packs

The platform should support partial use: buying a collection does not require applying it wholesale.

---

# 12. Remix Graph

Assets can optionally support derivative creation.

Possible policies:

- No remix
- Remix allowed with attribution
- Remix allowed with automatic royalty

Every derivative stores lineage.

Example:

Asset A → Remix B → Remix C

The marketplace can preserve creator attribution and route agreed royalty shares through the internal economy.

The exact royalty policy belongs to the VIRT/economy specification and must not be hard-coded into the asset renderer.

---

# 13. Auto Furnish

AI should help users decorate without manually positioning every object.

Example commands:

> Furnish this room using only assets I already own.

> Make this living room warmer and more minimal.

> Furnish this room with a 5,000 VIRT budget.

The Auto Furnish engine can use:

- Room geometry
- Existing items
- User style profile
- Inventory
- Marketplace catalog
- Device performance constraints
- Object compatibility metadata

It should propose arrangements before paid purchases are finalized.

---

# 14. Try in My House

Marketplace discovery should support contextual preview.

From another user's room or marketplace listing:

> See this in my House

FUL.HOUSE renders the candidate object or collection into the user's real room configuration before purchase.

This can later become a bridge to physical commerce for REAL products, but the initial product should focus on virtual placement and ownership.

---

# 15. Walls, floors and surfaces

The same creator economy must apply to surfaces, not only 3D furniture.

Asset classes include:

- WallFinishAsset
- FloorAsset
- CeilingAsset
- PaintAsset
- PanelAsset
- TileAsset
- WallpaperAsset

These use repeatable material/texture rules and room-scale metadata rather than furniture placement anchors.

They still follow the same rights, provenance, marketplace and collection systems.

---

# 16. Functional appliances and electronics

Some assets are not purely visual.

Examples:

- Television
- Music system
- Smart display
- Lamp
- Record player
- Bookshelf

Functional objects can expose permitted HouseObject actions such as:

- play
- pause
- openProvider
- changeState
- displayContent

Media/service providers remain adapters. The asset does not hard-code YouTube, Spotify or another provider into the core object schema.

---

# 17. Rights and brand protection

FUL.HOUSE must distinguish:

### Personal digitization
A user digitizes an item they own for their private House.

### Original commercial creation
The creator owns/controls rights and can publish commercially.

### Licensed branded asset
A verified brand or licensed creator publishes an authorized representation.

A photo of a branded real-world product cannot automatically become a sellable marketplace asset.

Marketplace publication requires stronger rights/moderation checks than private digitization.

---

# 18. Provenance and digital history

Assets preserve meaningful provenance:

- Original creator
- Creation date
- Remix lineage
- Collection origin
- Acquisition source
- Ownership/inheritance events where appropriate

This can create long-lived digital objects without requiring speculative blockchain mechanics.

Example:

> Chair created in 2027
> Original creator: Alex
> Part of this family House since 2028
> Inherited in 2051

---

# 19. Performance classes

Not every asset can render equally on every device.

Each asset should expose one or more compatible performance profiles.

Example:

- Mobile Lite
- Mobile High
- Desktop
- Home Brain render/export

The renderer selects an appropriate LOD/material set without changing the user's ownership of the asset.

This integrates with the Butler Compute Ladder but remains a rendering concern rather than an AI identity concern.

---

# 20. Moderation and quality

Marketplace publication requires automated and potentially human review for:

- Copyright/trademark concerns
- Pornographic/violent/prohibited content
- Malicious payloads
- Broken geometry
- Extreme resource usage
- Misleading previews
- Spam/duplicates
- Hidden or off-scene geometry
- Unsafe external links/actions

Private personal assets can have a lighter moderation path but still must respect technical security constraints.

---

# 21. MVP

Do not launch a full 3D creator economy first.

Recommended MVP:

1. Define Asset Standard.
2. Support a limited furniture category set.
3. Upload image/sketch + text description.
4. AI creates/normalizes a stylized 2D/2.5D asset.
5. Creator approves metadata and preview.
6. Publish free or paid asset.
7. Inventory ownership.
8. Place asset in room.
9. Collections.
10. Basic remix lineage.
11. Auto Furnish using owned assets only.
12. Try in My House preview.

Later:

- Rich 3D generation
- Video capture
- Full material/surface marketplace
- Advanced royalties
- Creator storefronts
- Brand programs
- Physical product mapping
- Room/architecture packs

---

## Key principles

**The platform creates standards, not the catalog.**

**AI turns human creativity into interoperable House Assets.**

**Anything users create should work across compatible Houses without requiring them to become 3D engineers.**

**The House world should grow because creators want to add to it, not because FUL.HOUSE hires an infinite furniture department.**