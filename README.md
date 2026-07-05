# Voynich Manuscript: Phytoglyphica Project

[![Language](https://img.shields.io/badge/language-Python-blue)](https://github.com/badges/shields)
[![IG Tier](https://img.shields.io/badge/IG-O%E2%82%82-blueviolet)](https://github.com/badges/shields)
[![μ∘δ=id](https://img.shields.io/badge/%CE%BC%E2%88%98%CE%B4%3Did-open-critical)](https://github.com/badges/shields)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/badges/shields)
[![Author](https://img.shields.io/badge/author-Lando%E2%8A%97%E2%8A%99perator-informational)](https://github.com/badges/shields) [![Type](https://img.shields.io/badge/type-%E2%9F%A8%F0%90%91%A6%F0%90%91%B8%F0%90%91%BE%F0%90%91%B9%F0%90%90%B8%F0%90%91%82%F0%90%91%A7%F0%90%91%94%F0%90%91%9D%E2%8A%99%F0%90%91%96%F0%90%91%B3%F0%90%91%AD%E2%9F%A9-blue)](https://github.com/badges/shields) [![Tier](https://img.shields.io/badge/tier-O%E2%88%9E-blueviolet)](https://github.com/badges/shields)

**What it is.** The document and data project arguing that the Voynich Manuscript is a phytoglyphic pharmacopeia: a structured botanical database plus a recipe engine, read through the Imscribing Grammar.

**What it does.** Collects the definitive manuscript writeup, the engine specification, the botanical companion, and the full machine-extracted enumeration of pharmacy and recipe entries, alongside the Lean companion files that machine-verify the grammar.

**Why it matters.** It reframes the Voynich from "undeciphered text" to executable pharmaceutical database: six sections as six registers of one computation, with three plant walkthroughs reaching structural distance d = 0 to d = 1.0. The computational engine that runs this lives in `imsgct/lang/voynich-engine`; this project is the documentary and botanical layer.

**How to use it.** Start with `VOYNICH.md` (the definitive version), then `ENGINE.md` for the session protocol. The Lean grammar is verified in `imsgct/p4rakernel/p4ramill`.

- **Canonical lifted copy:** `imsgct/ig-docs/voynich_lifted/`
- **Source manuscripts:** `imsgct/Voynich_Phytoglyphica/manuscripts/`

---

## Key claims (verified through IG tool calls)

1. The manuscript is a pharmaceutical database: ~1,491 botanical entries and ~1,076 procedural recipes.
2. It is a split-register executable: six sections are six registers of a single computation.
3. Eleven structural botanical types, organized by pharmaceutical operating mode.
4. A seven-gate session engine produces complete pharmaceutical protocols from IG tuples.
5. Three complete walkthroughs: *Artemisia absinthium* (d=0.0000), *Mandragora officinarum* (d=0.8367), *Ricinus communis* (d=1.0).

## Documents

| File | Role |
|------|------|
| `VOYNICH.md` | **Definitive version.** "A Lost Phytoglyphic Pharmacopeia": full session spec, 11-type classification, 7-gate engine, illustrations |
| `ENGINE.md` | Engine spec: IG primitive → pharmaceutical parameter mapping, recipe opcodes, 7-gate protocol, session-invariance theorems |
| `VOYNICH_BOTANICAL_COMPANION_LIFTED.md` | Botanical companion with plant walkthroughs |
| `VOYNICH_COMPLETE_LISTING.md` | Full enumeration of pharmacy + recipe entries |
| `VOYNICH_ANNOTATED_FOLIOS.html` | Annotated folio images |

Earlier versions (inaugural run, state-machine framing, dissolved/analytic, single-folio) are preserved in-repo for reference.

## Supporting assets

- **`images/`** SVG type cards, phyllotaxis, trichome kinetics, continental distribution, Urpflanze master key, plant pairs, structural diagrams, folio collections.
- **Lean companion** `Core.lean`, `Imscription.lean`, `Crystal.lean`, `AgentSelf.lean`, `IGMorphism.lean`, `Catalog.lean`, `Consciousness.lean`, `TierCrossing.lean`, `BotanicalWalkthrough.lean`, `GeneticCode.lean`.
- **Data** `voynich_pharmacy.json` (pharmacy entries), `voynich_recipe_bio.json` (recipes), `voynich_findings.json` (structural findings).
