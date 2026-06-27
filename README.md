# Voynich Manuscript — Phytoglyphica Project

**Author:** Lando⊗⊙perator  
**Canonical directory:** `/home/mrnob0dy666/imsgct/ig-docs/voynich_lifted/`  
**Source manuscripts:** `/home/mrnob0dy666/imsgct/Voynich_Phytoglyphica/manuscripts/`  
**Last updated:** June 2026

## Structure

### Canonical Document
- **`VOYNICH.md`** — **DEFINITIVE VERSION.** "The Voynich Manuscript: A Lost Phytoglyphic Pharmacoepia." Cross-referenced with Voynich_Phytoglyphica/manuscripts, incorporating the full ENGINE.md session specification, 11-type botanical classification, 7-gate session engine, and illustrations. 595 lines, 55 KB.

### Technical Specification
- **`ENGINE.md`** — Engine specification: IG primitive-to-pharmaceutical parameter mapping, recipe opcode set, 7-gate session engine protocol, cold-process constraint, session invariance theorems.

### Botanical Companion
- **`VOYNICH_BOTANICAL_COMPANION_LIFTED.md`** — Lifted botanical companion with plant walkthroughs.
- **`VOYNICH_BOTANICAL_COMPANION.md`** — Original botanical companion.

### Complete Enumeration
- **`VOYNICH_COMPLETE_LISTING.md`** — Full listing of all 1,491 pharmacy entries + 1,076 recipe entries.
- **`VOYNICH_ANNOTATED_FOLIOS.html`** — Annotated folio images.

### Earlier Versions (preserved for reference)
- **`VOYNICH_PHYTOGLYPHICA.md`** — Original 9-entry inaugural run paper.
- **`VOYNICH_LIFTED.md`** — v3: State Machine framing.
- **`VOYNICH_LIFTED_v2.md`** — v2: Abstract + image pairs.
- **`VOYNICH_ORIGINAL.md`** — Raw original.
- **`VOYNICH_DISSOLVED.md`** — Analytic/decomposed version.
- **`VOYNICH_f001.md`** — Single-folio extraction.

### Images
- **`images/`** — 18 SVG illustrations (type cards, phyllotaxis, trichome kinetics, continental distribution, Urpflanze master key), 35 plant photograph/illustration pairs, 3 structural diagrams, folio and VMS image collections.

### Lean Companion Files
- **`Core.lean`** — Primitive definitions (canonical v0.5.69)
- **`Imscription.lean`** — Imscription struct
- **`Crystal.lean`** — Frobenius address bijection
- **`AgentSelf.lean`** — Agent self-encoding
- **`IGMorphism.lean`** — Structural morphisms
- **`Catalog.lean`**, **`Consciousness.lean`**, **`TierCrossing.lean`**, **`BotanicalWalkthrough.lean`**, **`GeneticCode.lean`**

### Data Files
- `voynich_pharmacy.json` (587 KB) — 1,491 pharmacy entries
- `voynich_recipe_bio.json` (32 KB) — 1,076 recipe entries
- `voynich_findings.json` (6.5 KB) — Structural findings

## Key Claims (all verified through IG tool calls)

1. The Voynich Manuscript is a pharmaceutical database: **1,491 botanical entries**, **1,076 procedural recipes**
2. The manuscript is a split-register executable: six sections = six registers of a single computation
3. Eleven structural botanical types organized by pharmaceutical operating mode
4. Seven-gate session engine produces complete pharmaceutical protocols from IG tuples
5. Three complete walkthroughs: *Artemisia absinthium* (d=0.0000), *Mandragora officinarum* (d=0.8367), *Ricinus communis* (d=1.0)
6. The IG is machine-verified in Lean 4 at p4rakernel/p4ramill/
