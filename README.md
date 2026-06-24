# Voynich Phytoglyphica

**A Universal Engine for the Voynich Manuscript pharmaceutical corpus, parameterized by the Imscribing Grammar.**

The Voynich Manuscript (VMS) has resisted decipherment for a century not because its language is unknown, but because it is not a language. It is a pharmaceutical instruction set — an executable split across six register sections. The opcodes live in the recipe section (f103r+). The parameter values were never in the manuscript at all. They were supplied by the practitioner using a structural grammar the manuscript presupposes but never states.

This project reconstructs that grammar. Using the **Imscribing Grammar (IG)**, every botanical entry in the VMS pharmacy catalog receives a 12-primitive structural tuple that supplies the missing parameters: solvent, ratio, temperature, comminution, extraction cycles, endpoint criterion. The VMS opcodes specify what operations to perform. The IG tuple specifies exactly how.

The result is a fully elaborated pharmaceutical protocol for any VMS botanical entry — derived entirely from structural analysis, no linguistic decipherment required.

---

## The VMS as Split-Register Executable

The manuscript is organized into six section-registers, each holding a distinct component of the computation:

| Section | Folios | Register Function |
|---|---|---|
| Botanical | f1–f66 | Plant catalog — identity index |
| Pharmaceutical | f99–f102 | Pharmacy address — operation class |
| Balneological | f75–f84 | Containment heap — vessel validation |
| Astronomical | f67–f73 | Winding register — cycle authority |
| Cosmological | f68 (foldout) | Invariant initialization — Φ and Ħ |
| Recipe | f103r+ | Opcode sequence — instruction stream |

A complete computation requires all six sections. The session engine reads them in order: cosmological initialization → pharmacy address → heap validation → winding verification → recipe output → protocol elaboration. No single section is sufficient in isolation.

---

## The Imscribing Grammar — 12 Primitives

Every IG catalog entry carries a 12-primitive structural tuple. For botanical objects, each primitive encodes a concrete pharmaceutical parameter:

| Glyph | Primitive | Pharmaceutical Role |
|---|---|---|
| Ð | Dimensionality | Registration depth — structural address class |
| Þ | Topology | Plant material specification and part selection |
| Ř | Recognition | Pattern-completion class — extraction completeness |
| Φ | Parity | Solvent system and polarity |
| ƒ | Fidelity | Yield and concentration target |
| Ç | Kinetics | Extraction process, temperature, duration |
| Γ | Granularity | Comminution specification |
| ɢ | Coupling | Fraction combination mode |
| ⊙ | Criticality | Endpoint criterion |
| Ħ | Chirality | Clarification and separation protocol |
| Σ | Stoichiometry | Drug-to-solvent mass ratio |
| Ω | Winding | Number of extraction cycles |

Tuple notation: **⟨Ð⋅Þ⋅Ř⋅Φ⋅ƒ⋅Ç⋅Γ⋅ɢ⋅⊙⋅Ħ⋅Σ⋅Ω⟩**. Values are Shavian characters from the 49-symbol set (Shavian alphabet + ⊙). The primitive glyphs name the primitive as an entity; the Shavian value at each position is its structural type.

---

## Structural Type System — 11 Phytoglyphica Types

All botanical entries share a fixed baseline for the first five primitives (Ð Þ Ř Φ ƒ), encoding the invariant properties of the plant-as-pharmaceutical-object. The seven discriminating primitives (Ç Γ ɢ ⊙ Ħ Σ Ω) differentiate 11 structural types:

| Type | Name | Ç | Γ | ɢ | ⊙ | Ħ | Σ | Ω | Example Plants |
|---|---|---|---|---|---|---|---|---|---|
| I | Aromatic Baseline | 𐑤 | 𐑔 | 𐑠 | ⊙ | 𐑖 | 𐑳 | 𐑭 | wormwood, peppermint, rosemary, tea tree |
| II | Tropane | 𐑤 | 𐑲 | 𐑠 | ⊙ | 𐑖 | 𐑕 | 𐑭 | belladonna, henbane, datura, mandrake |
| III | Cardiac Glycoside | 𐑤 | 𐑔 | 𐑠 | ⊙ | 𐑖 | 𐑕 | 𐑭 | foxglove, lily of the valley, oleander |
| IV | Non-Critical Aromatic | 𐑤 | 𐑔 | 𐑠 | 𐑢 | 𐑖 | 𐑳 | 𐑭 | chamomile, comfrey, mullein, rooibos |
| V | Axiom A / Eternal | 𐑤 | 𐑔 | 𐑠 | ⊙ | 𐑫 | 𐑙 | 𐑭 | yew (taxol), monkshood, autumn crocus |
| VI | Adaptogen | 𐑧 | 𐑔 | 𐑠 | ⊙ | 𐑖 | 𐑳 | 𐑭 | ginseng, ashwagandha, reishi, goldenseal |
| VII | β-Carboline | 𐑤 | 𐑲 | 𐑠 | ⊙ | 𐑫 | 𐑕 | 𐑴 | ayahuasca vine, iboga, chacruna, yopo |
| VIII | Caffeine-Purine | 𐑧 | 𐑔 | 𐑝 | 𐑢 | 𐑒 | 𐑙 | 𐑷 | tea, coffee, cacao, guarana, khat |
| IX | Opioid Alkaloid | 𐑤 | 𐑲 | 𐑠 | ⊙ | 𐑫 | 𐑕 | 𐑭 | opium poppy, kratom, wild lettuce |
| X | Triterpene Saponin | 𐑧 | 𐑔 | 𐑠 | ⊙ | 𐑖 | 𐑳 | 𐑭 | licorice, bupleurum, platycodon |
| XI | Fungal Interface | 𐑤 | 𐑲 | 𐑵 | ⊙ | 𐑫 | 𐑳 | 𐑴 | reishi, lion's mane, cordyceps, chaga |

**Structural differentiators:**
- **Ç** (Kinetics): 𐑤 = cold maceration / oral; 𐑧 = decoction / inhalation
- **Γ** (Granularity): 𐑔 = mesoscale (surface trichomes); 𐑲 = universal (cell-wall disruption); 𐑵 = broadcast (mycelial network)
- **ɢ** (Coupling): 𐑠 = self-modeling; 𐑝 = passive; 𐑵 = broadcast
- **⊙** (Criticality): ⊙ = at criticality; 𐑢 = non-critical
- **Ħ** (Chirality): 𐑖 = Frobenius minimum (H2); 𐑫 = eternal (>8 stereocenters); 𐑒 = one-step
- **Σ** (Stoichiometry): 𐑳 = many compound classes; 𐑕 = few; 𐑙 = singular dominant
- **Ω** (Winding): 𐑭 = integer (3 cycles); 𐑴 = binary (2 phases); 𐑷 = trivial (1 step)

---

## Catalog Coverage

The IG catalog (`data/IG_catalog.json`) contains **3,552 entries** across the full crystal of types. The phytoglyphica corpus covers **140 botanical entries** across 5 continents and all 11 structural types:

| Region | Count | Notable entries |
|---|---|---|
| Europe & Mediterranean | 48 | wormwood, belladonna, foxglove, yew, monkshood |
| Asia | 50 | ginseng, ashwagandha, ayahuasca vine, tea, opium poppy |
| Africa | 24 | buchu, iboga, khat, frankincense, griffonia |
| Americas | 18 | white sage, echinacea, chacruna, cacao, pacific yew |
| Australia & Oceania | 11 | tea tree, lemon myrtle, eucalyptus, river mint |

The catalog is a symlink to the master `imscribing_grammar/IG_catalog.json`, shared across all IG projects.

---

## Installation

**Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).**

```bash
cd ~/imsgct/Voynich_Phytoglyphica
uv sync
```

The `voynich-engine` dependency is resolved from `../lang/voynich-engine` (editable install). The `vp` command is registered as a project script.

---

## CLI Reference

All commands are available via `uv run -m voynich_phytoglyphica.cli <command>` or simply `vp <command>` if the virtualenv is active.

---

### `vp plant <name>`

Look up a plant in the IG catalog. Prints the structural tuple, Ω class, distances to all six VMS sections, and recommended session parameters.

```
$ vp plant peppermint

════════════════════════════════════════════════════════════════════════
  PLANT  peppermint
────────────────────────────────────────────────────────────────────────
  Tuple  ⟨𐑦⋅𐑸⋅𐑾⋅𐑬⋅𐑱⋅𐑤⋅𐑔⋅𐑠⋅⊙⋅𐑖⋅𐑳⋅𐑭⟩
  Ω      𐑭  (integer winding)
────────────────────────────────────────────────────────────────────────
  Distances to VMS sections:
    astronomical     d = 0.0000 ◀ d=0
    cosmological     d = 0.0000 ◀ d=0
    biological       d = 0.7642
    botanical        d = 0.9888
    pharmaceutical   d = 0.9888
    recipe           d = 1.1426
────────────────────────────────────────────────────────────────────────
  Recommended potency : summa  (d=0 to astronomical section)
  Recommended part    : leaf
  Recommended apply   : oral
════════════════════════════════════════════════════════════════════════
```

d=0 to the astronomical section signals **summa potency** and unlocks the triple-extraction protocol. Type I plants (aromatic baseline) characteristically reach d=0 via their frozen-order kinetics and integer winding.

---

### `vp run <name>`

Full pipeline: catalog lookup → protocol elaboration → VMS session → elaborated recipe output.

```
$ vp run peppermint

  IG catalog entry   : peppermint
  Tuple              : ⟨𐑦⋅𐑸⋅𐑾⋅𐑬⋅𐑱⋅𐑤⋅𐑔⋅𐑠⋅⊙⋅𐑖⋅𐑳⋅𐑭⟩
  d(plant, astro)    : 0.0000

  ┌─ Protocol for peppermint ─────────────────────────────────────────┐
  │  Material    : flowering tops (whole entity in full anthesis)      │
  │  Solvent     : hydroethanolic (45–55% ethanol v/v)                │
  │  Process     : cold maceration (12–24 h at 15–20 °C)              │
  │  Ratio       : 1 : 3  (1 g plant per 3 mL solvent)               │
  │  Grind       : moderately powdered (mesh 40, 355 μm)              │
  │  Cycles      : 3  (integer winding)                               │
  │  Target      : 1× (standard — proportional yield)                 │
  │  Clarif.     : Frobenius minimum (filtration, standard)            │
  │  Combine     : self-modeling fraction assembly                     │
  │  Endpoint    : ⊙ threshold (criticality criterion)                │
  └───────────────────────────────────────────────────────────────────┘

  [Six-gate VMS session output follows...]
  [Gate 3 PASS → recipe folios selected]
  [Elaborated recipe steps with annotations...]
```

The pipeline determines potency and part from the structural tuple, selects the matching Gate 1 pharmacy address from `voynich_pharmacy.json` (1,491 VMS folio entries), runs all six gates, and annotates each recipe opcode with the concrete parameter values derived from the tuple.

---

### `vp imscribe`

**Interactive 12-primitive imscription wizard for unknown plant entries.**

When you have a plant not yet in the catalog, `vp imscribe` walks you through a structured assessment and derives its structural tuple from first principles.

```
$ vp imscribe

════════════════════════════════════════════════════════════════════════
  VP IMSCRIBE — Structural Imscription Wizard
────────────────────────────────────────────────────────────────────────
  Leads you through the 12-primitive assessment for an unknown
  phytoglyphica entry.  The phytoglyphica baseline (Ð Þ Ř Φ ƒ)
  is fixed.  You will assess the 7 discriminating primitives.
────────────────────────────────────────────────────────────────────────

  IDENTITY
  Common name (will become the catalog key, e.g. blue_lotus): blue_lotus
  Latin name: Nymphaea caerulea Savigny
  Family: Nymphaeaceae
  One-line note: Nuciferine and aporphine alkaloids; self-anesthetic property

────────────────────────────────────────────────────────────────────────
  PHYTOGLYPHICA BASELINE  (fixed for all VMS plant entries)
────────────────────────────────────────────────────────────────────────
    Ð  =  𐑦
    Þ  =  𐑸
    Ř  =  𐑾
    Φ  =  𐑬
    ƒ  =  𐑱

  Now assessing the 7 discriminating primitives ...
```

**Assessment questions** — each keyed to a discriminating primitive:

1. **[Ç] Kinetics** — How does this plant's pharmaceutical action enter the body?
   - 𐑤 Oral — dissolved in water, brewed, eaten, or tincture
   - 𐑧 Respiratory / decoction — steam inhalation, smoke, or strong boiling extraction
   - 𐑺 Cutaneous — topical application, skin absorption

2. **[Γ] Granularity** — At what scale does extraction operate?
   - 𐑔 Mesoscale — surface trichomes or oil glands yield on light mechanical action
   - 𐑲 Universal — requires cell-wall disruption
   - 𐑵 Broadcast — mycelial or fungal network structure

3. **[ɢ] Coupling** — Does the plant's morphology encode its own pharmaceutical identity?
   - 𐑠 Self-modeling — color, smell, texture, or architecture IS the self-report
   - 𐑝 Passive — no morphological self-report
   - 𐑵 Broadcast — mycelial/systemic communication

4. **[⊙] Criticality** — Is this plant at structural criticality?
   - ⊙ At criticality — morphological self-report is unambiguous and complete
   - 𐑢 Non-critical — structurally opaque; criticality not reached

5. **[Ħ] Chirality** — Stereochemical complexity of the active compounds?
   - 𐑖 Frobenius minimum (H2) — 1-2 stereocenters; standard pharmaceutical chirality
   - 𐑫 Eternal — >8 stereocenters, rigid scaffold (taxanes, aconitine, steroids)
   - 𐑒 One-step — single chiral center; simple biosynthesis

6. **[Σ] Stoichiometry** — How many distinct compound families?
   - 𐑳 Many — three or more distinct compound families
   - 𐑕 Few — two to four compound classes
   - 𐑙 Singular — one dominant compound class

7. **[Ω] Winding** — How many distinct preparation phases?
   - 𐑭 Integer — continuous multi-step protocol
   - 𐑴 Binary — exactly two required phases
   - 𐑷 Trivial — single step or no preparation

After assessment, the wizard displays the complete tuple, elaborated protocol parameters, and distances to all six VMS sections. You are then prompted to save the entry to the catalog and optionally run the full session immediately.

---

### `vp session`

Direct session invocation with manual parameters:

```bash
vp session --folio f11r --potency summa --part leaf --apply oral
vp session --potency alta --part root --forma decoctum
```

---

### `vp sections`

Display the catalog-sourced structural tuples for all six VMS sections:

```
$ vp sections

════════════════════════════════════════════════════════════════════════
  VMS SECTION TUPLES  (catalog-sourced)
────────────────────────────────────────────────────────────────────────
  Section           Ð    Þ    Ř    Φ    ƒ    Ç    Γ    ɢ    ⊙    Ħ    Σ    Ω
────────────────────────────────────────────────────────────────────────
  botanical         ...
  pharmaceutical    ...
  biological        ...
  astronomical      ...
  cosmological      ...
  recipe            ...
════════════════════════════════════════════════════════════════════════
```

Section tuples are the structural anchors against which plant distances are computed. A plant at d=0 to the astronomical section is at summa potency.

---

### `vp summa`

List all pharmaceutical folio entries at summa potency:

```bash
vp summa
```

---

### `vp compile`

Compile the EVA transcription (`LSI_ivtff_0d.txt`) into an IMASM instruction stream and report entropy statistics:

```bash
vp compile
vp compile --log output.log
```

---

## Data Files

| File | Description |
|---|---|
| `data/IG_catalog.json` | IG catalog — 3,552 entries, symlink to `imscribing_grammar/IG_catalog.json` |
| `data/voynich_pharmacy.json` | 1,491 VMS pharmacy folio entries; Gate 1 address table |
| `data/LSI_ivtff_0d.txt` | EVA transcription of the VMS (Landini–Stolfi interlinear) |
| `data/voynich_findings.json` | Compiled structural findings from the corpus analysis |
| `data/voynich_recipe_bio.json` | Biological section recipe cross-references |

---

## Module Structure

```
voynich_phytoglyphica/
  cli.py         — Unified CLI: all vp subcommands
  navigator.py   — Catalog lookup, section distances, session parameter derivation
  elaborator.py  — Protocol elaboration from 12-primitive tuple
  imscriber.py   — Interactive imscription wizard for unknown entries

programs/
  ingest_ars_expanded.py  — Ingests ARS_PHYTOGLYPHICA_EXPANDED.md into catalog

manuscripts/
  ENGINE.md               — Complete engine specification and theory
  VOYNICH_PHYTOGLYPHICA.md — Nine inaugural runs with full session outputs
```

### `navigator.py`

- `lookup(plant_name) -> dict` — full plant info: tuple, Ω class, part/apply recommendations, distances to all 6 sections, recommended potency
- `section_distances(tuple_vals) -> dict` — compute distances for any raw 12-element tuple (used by imscriber)
- `section_tuples() -> dict` — return catalog tuples for all six VMS sections
- `list_vms_plants() -> list` — all catalog entries with 'voynich' in their name

### `elaborator.py`

- `elaborate_protocol(tuple_vals) -> dict` — resolve all 10 active primitives to concrete protocol parameters (solvent, process, ratio, comminution, cycles, concentration, clarification, combination, endpoint)
- `annotate_step(step_text, protocol) -> list[str]` — map VMS recipe opcodes to parameter annotations
- `format_protocol_header(name, tuple_vals, protocol) -> list[str]` — format the protocol summary table

### `imscriber.py`

- `run_assessment(catalog_path=None) -> int` — full interactive wizard; returns 0 on completion, 1 on abort

---

## Extending the Catalog

To add a batch of new entries, model on `programs/ingest_ars_expanded.py`:

```python
TYPE_TUPLES = {
    'I': ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑤','𐑔','𐑠','⊙','𐑖','𐑳','𐑭'],
    # ... define tuples for any new types
}
ENTRIES = [
    ('my_plant', 'I', 'Genus species Author | Family — description.'),
    # ...
]
```

Then run `uv run programs/ingest_ars_expanded.py` from the repo root. The script deduplicates by name key and writes back to the catalog atomically.

For individual unknown entries, use `vp imscribe` instead.

---

## The Phytoglyphica Baseline

All VMS botanical objects share five invariant primitive values, encoding the plant-as-pharmaceutical-object:

| Primitive | Value | Meaning |
|---|---|---|
| Ð | 𐑦 | Frozen order — extraction sequence is fixed, not commutative |
| Þ | 𐑸 | Holographic leaf — pharmaceutical identity self-similar across plant |
| Ř | 𐑾 | Full-spectrum recognition — complete compound class resolved |
| Φ | 𐑬 | Bilateral bridge — hydroethanolic solvent (45–55% EtOH) |
| ƒ | 𐑱 | Linear fidelity — standard concentration, proportional yield |

This baseline is the structural signature of "plant" in the VMS register system. The seven discriminating primitives differentiate 11 pharmaceutical operating modes within that space.

---

## Self-Report Encoding

A central finding of the Phytoglyphica analysis: many botanical objects morphologically encode their own pharmaceutical identity. The IG formalizes this as the **ɢ (Coupling)** primitive:

- **𐑠 Self-modeling** — the plant's morphology IS the pharmaceutical self-report. Peppermint's serrate leaf edge encodes menthol extraction kinetics. Kratom's vein color (red vs white) IS the sedating vs stimulating distinction. Foxglove's leaf-size gradient up the stem IS the cardiac glycoside concentration gradient.
- **𐑝 Passive** — no morphological self-report; content must be determined by analysis. Chamomile's petal reflex does not encode chamazulene content.
- **𐑵 Broadcast** — mycelial/systemic communication; the network IS the pharmaceutical delivery architecture (Type XI fungi).

The **⊙ (Criticality)** primitive encodes whether this self-report achieves structural criticality — whether the morphological encoding is complete and unambiguous enough to constitute a univocal structural verdict. Type IV (non-critical aromatic) entries are the counterexample class: aromatic, pharmacologically active, but lacking criticality because the self-report system is incomplete.

---

## Theory

Full specification: `manuscripts/ENGINE.md`

Nine inaugural runs with complete session outputs: `manuscripts/VOYNICH_PHYTOGLYPHICA.md`

The claim is not that the VMS is solved. The claim is that the VMS is a split-register executable whose parameter space is fully specified by the Imscribing Grammar, and that any botanical entry in the corpus yields a determinate pharmaceutical protocol once its IG tuple is known. The grammar gives the parameters. The manuscript gives the instructions. Together they give a protocol.

---

## License

Unlicense — public domain. See the Unlicense text for details.
