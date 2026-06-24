# Voynich Phytoglyphica

A computational engine for the pharmaceutical corpus of the Voynich Manuscript.

---

## The Voynich Manuscript

Beinecke MS 408 (Yale University) is a vellum codex of roughly 240 pages, radiocarbon-dated 1404–1438. Its script and language remain unread by conventional means. It is divided into six visually distinct sections, each illustrated in a style unlike any other medieval manuscript:

- **Botanical** (f1–f66): one large plant illustration per page, roots prominently shown, accompanied by running script. Many plants are unidentified or stylized beyond species recognition.
- **Pharmaceutical** (f99–f102): columns of jars, flasks, and labeled containers — a catalog of pharmaceutical vessels organized by type and label.
- **Balneological** (f75–f84): networks of pools connected by tubes, figures immersed in green and blue fluid. The structural role is vessel validation and heap containment.
- **Astronomical** (f67–f73): circular diagrams with zodiac imagery, sun and moon markers, month annotations.
- **Cosmological** (f68, six-page foldout): the largest single piece in the manuscript. Concentric rings annotated with symbols. The outermost ring establishes the two parameters that all sessions inherit: solvent polarity (Φ) and chirality tier (Ħ).
- **Recipe** (f103r+): no illustrations. Dense text in paragraph form, the only section that reads as a sequential instruction stream.

The recipe section contains no plant images and no parameter values. The botanical section contains no instructions. The pharmaceutical section contains no quantities. Each section is incomplete in isolation.

---

## What This Engine Does

The VMS is a split-register executable. Its six sections are six registers of a single computation:

| Section | Folios | Gate | Role |
|---|---|---|---|
| Cosmological | f68 foldout | `INIT` | Invariant `INIT`ialization — sets Φ (solvent) and Ħ (chirality) for all sessions |
| Botanical | f1–f66 | `ADDR` | Identity gate — confirms the plant resolves within the botanical section's structural field |
| Pharmaceutical | f99–f102 | `GATE 1` | Pharmacy address — maps potency × plant-part → folio entry |
| Balneological | f75–f84 | `GATE 2` | Heap validation — FSPLIT/FFUSE containment test |
| Astronomical | f67–f73 | `GATE 3` | Winding authority — verifies Ω against multi-source majority |
| Recipe | f103r+ | `OUTPUT` | Opcode stream — instruction sequence selected and elaborated |

The opcodes are in the recipe section. The parameter values are nowhere in the manuscript. A medieval practitioner supplied them from knowledge of the plant's structural character. This engine reconstructs that parameter-supply mechanism: given a plant name, it derives the full 12-parameter tuple and runs the complete seven-gate session, producing an elaborated pharmaceutical protocol.

---

## The Seven-Gate Session

Each run of the engine executes seven gates in order:

**`INIT`** — the cosmological foldout (f68) `INIT`ializes two invariants that hold for all sessions: Φ (solvent polarity, here hydroethanolic 45–55% EtOH) and Ħ (chirality tier, here Frobenius minimum). These are read once from the foldout and applied to every subsequent gate.

**`ADDR`** — the botanical section (f1–f66) is the identity gate. Before the pharmaceutical section is queried, the session confirms that the plant's structural tuple falls within the botanical section's structural field: d(plant, botanical) ≤ 1.5. This gate was always implied by the manuscript's architecture — the botanical illustrations are not decorative headers for the pharmaceutical section, they are a prior confirmation register. Entries that are not botanical objects fail here.

**`GATE 1`** — the pharmaceutical section (f99–f102) is queried by potency class and plant part. A specific folio entry (e.g. `f11r/p6 → folium/flos → extractio → mixtura`) is selected as the `GATE 1` address. This determines the operation class and form (tinctura, decoctum, mixtura, etc.).

**`GATE 2`** — the balneological section (f75–f84) provides the heap register. The session checks whether the selected heap folio (indexed by the `GATE 1` folio number mod 20) has sufficient capacity for the recipe's instruction count: `FSPLIT ≥ n_ops` and `FFUSE/FSPLIT ≥ 0.60`. Either condition passes Gate 2.

**`GATE 3`** — the astronomical section (f67–f73) is the winding authority. Three independent transcription sources vote on the Ω value (f69, paragraphs 1–4; para 3 is the all-source lock state). A majority of 3/3 or 2/3 passes Gate 3. Ω determines the number of extraction cycles (1, 2, or 3).

**`OUTPUT`** — recipe folios (f103r+) proximal to the `GATE 1` entry are selected and ranked. Each recipe folio carries an opcode sequence (Accipe, Extrahe, Calefac, Divide, Transmuta, etc.).

**`ELABORATION`** — each opcode is annotated with the concrete parameter values from the plant's structural tuple: what material to take, what solvent at what ratio, what temperature, what grind size, how many cycles, what endpoint criterion.

---

## Structural Types — The VMS Botanical Categories

The VMS botanical catalog organizes plants by pharmaceutical operating mode, not by taxonomy. This engine identifies 11 structural types within the corpus. Each type has a fixed parameter tuple; membership is determined by the plant's morphological self-report system and compound profile:

| Type | Name | Ç | Γ | ɢ | ⊙ | Ħ | Σ | Ω | Example entries |
|---|---|---|---|---|---|---|---|---|---|
| I | Aromatic Baseline | 𐑤 | 𐑔 | 𐑠 | ⊙ | 𐑖 | 𐑳 | 𐑭 | wormwood, peppermint, rosemary, tea tree |
| II | Tropane | 𐑤 | 𐑲 | 𐑠 | ⊙ | 𐑖 | 𐑕 | 𐑭 | belladonna, henbane, datura, mandrake |
| III | Cardiac Glycoside | 𐑤 | 𐑔 | 𐑠 | ⊙ | 𐑖 | 𐑕 | 𐑭 | foxglove, lily of the valley, oleander |
| IV | Non-Critical Aromatic | 𐑤 | 𐑔 | 𐑠 | 𐑢 | 𐑖 | 𐑳 | 𐑭 | chamomile, comfrey, mullein, rooibos |
| V | Eternal / Axiom A | 𐑤 | 𐑔 | 𐑠 | ⊙ | 𐑫 | 𐑙 | 𐑭 | yew, monkshood, autumn crocus |
| VI | Adaptogen | 𐑧 | 𐑔 | 𐑠 | ⊙ | 𐑖 | 𐑳 | 𐑭 | ginseng, ashwagandha, goldenseal, echinacea |
| VII | β-Carboline | 𐑤 | 𐑲 | 𐑠 | ⊙ | 𐑫 | 𐑕 | 𐑴 | ayahuasca vine, iboga, chacruna, yopo |
| VIII | Caffeine-Purine | 𐑧 | 𐑔 | 𐑝 | 𐑢 | 𐑒 | 𐑙 | 𐑷 | tea, coffee, cacao, khat, guarana |
| IX | Opioid Alkaloid | 𐑤 | 𐑲 | 𐑠 | ⊙ | 𐑫 | 𐑕 | 𐑭 | opium poppy, kratom, wild lettuce |
| X | Triterpene Saponin | 𐑧 | 𐑔 | 𐑠 | ⊙ | 𐑖 | 𐑳 | 𐑭 | licorice, bupleurum, platycodon |
| XI | Fungal Interface | 𐑤 | 𐑲 | 𐑵 | ⊙ | 𐑫 | 𐑳 | 𐑴 | reishi, lion's mane, cordyceps, chaga |

The seven discriminating parameters (column headers after the type name) are:

| Parameter | What it encodes in the VMS context |
|---|---|
| **Ç** Kinetics | 𐑤 cold maceration / oral; 𐑧 decoction / respiratory |
| **Γ** Granularity | 𐑔 surface trichomes; 𐑲 cell-wall disruption; 𐑵 mycelial network |
| **ɢ** Coupling | 𐑠 self-modeling (plant encodes its own identity); 𐑝 passive; 𐑵 broadcast |
| **⊙** Criticality | ⊙ structurally self-evident; 𐑢 structurally opaque |
| **Ħ** Chirality | 𐑖 Frobenius minimum (H2); 𐑫 eternal (>8 stereocenters); 𐑒 one-step |
| **Σ** Stoichiometry | 𐑳 many compound classes; 𐑕 few; 𐑙 singular |
| **Ω** Winding | 𐑭 3 cycles (integer); 𐑴 2 cycles (binary); 𐑷 1 cycle (trivial) |

The first five parameters (Ð Þ Ř Φ ƒ) are the same for all VMS botanical entries — they encode what "plant" means as a pharmaceutical object in the VMS register system: frozen-order extraction, holographic self-similarity, full-spectrum recognition, hydroethanolic solvent, standard concentration.

---

## Self-Report: How the VMS Botanical Illustrations Function

The botanical illustrations are not decorative. They encode pharmaceutical parameters directly in the plant's morphology. This is the **ɢ (coupling)** parameter, and the VMS botanical section is organized around it.

A **self-modeling** plant **(ɢ = 𐑠)** shows you what to do and how much. Foxglove's leaf-size gradient up the stem IS the cardiac glycoside concentration gradient — the largest leaves at the base have the highest glycoside content. Kratom's leaf vein color (red vs white) IS the pharmacological distinction between sedating and stimulating chemotypes. Peppermint's broadly serrate leaf edge encodes menthol extraction kinetics. The VMS illustrator rendered these features because they were the practitioner's guide.

A **non-critical** plant **(⊙ = 𐑢)** lacks this. Chamomile's petal reflex does not tell you the chamazulene content. Rooibos's needle-like leaves do not encode aspalathin levels. These plants are pharmacologically active but structurally opaque — the illustration alone cannot parameterize the protocol.

A **fungal interface** entry **(ɢ = 𐑵)** uses broadcast coupling — the mycelial network is the pharmaceutical architecture itself, and the "illustration" of the fruiting body is only the visible terminus of a larger system.

The **⊙** (criticality) parameter encodes whether the self-report is complete enough to constitute a univocal structural verdict. Type IV entries (non-critical aromatics) pass the self-modeling test but fail criticality: aromatic trichomes are present, but the morphology does not fully specify the extraction mode. Type I entries pass both.

---

## Corpus Coverage

The pharmaceutical corpus covered by this engine spans **140 botanical entries** across 5 continents and all 11 structural types:

| Region | Count | Notable entries |
|---|---|---|
| Europe & Mediterranean | 48 | wormwood, belladonna, foxglove, yew, monkshood |
| Asia | 50 | ginseng, ashwagandha, ayahuasca vine, tea, opium poppy |
| Africa | 24 | buchu, iboga, khat, frankincense, griffonia |
| Americas | 18 | white sage, echinacea, chacruna, cacao, pacific yew |
| Australia & Oceania | 11 | tea tree, lemon myrtle, eucalyptus, river mint |

Source: *Ars Phytoglyphica Expanded* — 154 entries (140 unique; 14 are cross-references).

---

## Installation

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
cd ~/imsgct/Voynich_Phytoglyphica
uv sync
```

---

## CLI Reference

```bash
uv run -m voynich_phytoglyphica.cli <command>
# or, with virtualenv active:
vp <command>
```

---

### `vp plant <name>`

Look up a plant and print its structural tuple, Ω class, distances to all six VMS sections, and recommended session parameters. Distance to the astronomical section determines potency class; d=0 → summa (full triple-extraction protocol).

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

Type I plants (aromatic baseline) reach d=0 to the astronomical section because their frozen-order kinetics and integer winding match the astronomical register's winding authority exactly.

---

### `vp run <name>`

Full pipeline: structural tuple → protocol elaboration → seven-gate VMS session → annotated recipe output. Every VMS opcode is annotated with the concrete parameter values derived from the plant's tuple.

```
$ vp run peppermint

  IG catalog entry   : peppermint
  Tuple              : ⟨𐑦⋅𐑸⋅𐑾⋅𐑬⋅𐑱⋅𐑤⋅𐑔⋅𐑠⋅⊙⋅𐑖⋅𐑳⋅𐑭⟩
  d(plant, astro)    : 0.0000

  ELABORATED PROTOCOL  peppermint
  ────────────────────────────────────────────────────────────
  Material       flowering tops  (whole entity in anthesis)
  Comminution    moderately powdered  (mesh 40, 355 μm)
  Solvent        hydroethanolic  (45–55% EtOH, from foldout Φ)
  Process        cold maceration  (12–24 h at 15–20 °C)
  Ratio          1 : 3  (1 g plant per 3 mL solvent)
  Cycles         3  (integer winding — three complete turns)
  Endpoint       ⊙ threshold  (monitor until Δ < 5% per cycle)
  Clarification  two-step  (cloth filter → 24 h decant)
  Combination    parallel  (all fractions combined)
  Concentration  1×  (standard, no reduction)

  `INIT`  cosmological foldout — Ħ=𐑖 conferred, Φ=𐑬 set
  `ADDR`  botanical identity  d(plant,botanical)=0.9888  ≤1.5  PASS
  GATE1 SUMMA — f11r/p6  folium/flos  mixtura  n_ops=11
  GATE2 COMPILED — heap f80v  FSPLIT=34≥11 ✓  FFUSE/FSPLIT=0.94≥0.60 ✓
  GATE3 f69/p4 — EVALT 3/3 sources  Ω=𐑭  PASS
  `OUTPUT`  f103r/p2 (15 ops)  f103r/p9 (13 ops)  f103r/p49 (12 ops)

  RECIPE  f103r/p2
    Step 1: Extrahe/colare  →  cold macerate 15–20 °C, filter cloth
    Step 2: Calefac/commisce  →  [cold-process constraint: hold temperature]
    Step 3: Divide/tere  →  mesh 40 (355 μm) grinding pass
    ...
```

The `GATE 1` address (`f11r/p6`) is a real folio and paragraph in the VMS pharmaceutical section. The recipe folios (`f103r/p2`, `f103r/p9`, `f103r/p49`) are real folios in the VMS recipe section. The session is a direct read of the manuscript.

---

### `vp imscribe`

Interactive assessment wizard for a plant not yet in the corpus. Leads you through 7 questions keyed to the discriminating VMS parameters and derives the structural tuple from first principles.

```
$ vp imscribe

════════════════════════════════════════════════════════════════════════
  VP IMSCRIBE — Structural Imscription Wizard
────────────────────────────────────────────────────────────────────────
  Common name: blue_lotus
  Latin name:  Nymphaea caerulea Savigny
  Family:      Nymphaeaceae
  Note:        nuciferine and aporphine alkaloids; self-anesthetic

  [Ç]  How does the pharmaceutical action enter the body?
        1. 𐑤  oral — tincture, infusion, eaten
        2. 𐑧  respiratory / decoction — smoke, steam, boiling
        3. 𐑺  cutaneous — topical, skin absorption
  Choice: 1

  [ɢ]  Does the plant morphologically encode its own pharmaceutical identity?
        1. 𐑠  self-modeling — color/smell/architecture IS the self-report
        2. 𐑝  passive — content must be measured externally
        3. 𐑵  broadcast — mycelial/systemic (fungi only)
  Choice: 1

  ... (7 questions total)

  Result: ⟨𐑦⋅𐑸⋅𐑾⋅𐑬⋅𐑱⋅𐑤⋅𐑔⋅𐑠⋅⊙⋅𐑖⋅𐑕⋅𐑭⟩  (Type III structural class)
  d(astronomical) = 0.2390  →  alta potency

  Add to catalog? [y/n]: y
  Run full VMS session now? [y/n]: y
```

After the assessment, the wizard shows the elaborated protocol, computes distances to all six VMS sections, and optionally runs the complete seven-gate session.

---

### `vp session`

Direct session invocation with manual VMS parameters:

```bash
vp session --folio f11r --potency summa --part leaf --apply oral
vp session --potency alta --part root --forma decoctum
```

---

### `vp sections`

Show the structural tuples for all six VMS sections — the structural anchors against which plant distances are computed:

```
$ vp sections

  Section           Ð    Þ    Ř    Φ    ƒ    Ç    Γ    ɢ    ⊙    Ħ    Σ    Ω
  ─────────────────────────────────────────────────────────────────────────────
  botanical         𐑦    𐑡    𐑾    𐑬    𐑱    𐑤    𐑔    𐑠    ⊙    𐑖    𐑳    𐑴
  pharmaceutical    𐑦    𐑡    𐑾    𐑬    𐑱    𐑤    𐑔    𐑠    ⊙    𐑖    𐑳    𐑴
  biological        𐑦    𐑰    𐑾    𐑬    𐑱    𐑤    𐑔    𐑠    ⊙    𐑖    𐑳    𐑴
  astronomical      𐑦    𐑸    𐑾    𐑬    𐑱    𐑤    𐑔    𐑠    ⊙    𐑖    𐑳    𐑭
  cosmological      𐑦    𐑸    𐑾    𐑬    𐑱    𐑤    𐑔    𐑠    ⊙    𐑖    𐑳    𐑭
  recipe            𐑦    𐑡    𐑽    𐑬    𐑱    𐑤    𐑚    𐑠    ⊙    𐑒    𐑳    𐑴
```

The astronomical and cosmological sections share a tuple; their d=0 to Type I plants is why those plants reach summa potency. The recipe section has a distinctive Ħ=𐑒 (one-step chirality), reflecting the single-pass character of the opcode stream.

---

### `vp summa`

List all pharmaceutical folio entries at summa potency (used for `GATE 1` selection).

### `vp compile`

Compile the EVA transcription into an IMASM instruction stream with entropy statistics:

```bash
vp compile
vp compile --log output.log
```

---

## Data Files

| File | Contents |
|---|---|
| `data/LSI_ivtff_0d.txt` | EVA transcription of the VMS (Landini–Stolfi interlinear format) — the source text for all six sections |
| `data/voynich_pharmacy.json` | 1,491 pharmaceutical folio entries (f99–f102) parsed from the VMS; `GATE 1` address table |
| `data/voynich_recipe_bio.json` | Recipe section cross-references from the biological folio range |
| `data/voynich_findings.json` | Compiled structural findings from corpus analysis |
| `data/IG_catalog.json` | Structural catalog — 3,552 entries including 140 phytoglyphica entries; symlink to master catalog |

---

## Module Structure

```
voynich_phytoglyphica/
  cli.py         — All vp subcommands
  navigator.py   — Plant lookup, section distance computation, session parameter derivation
  elaborator.py  — Protocol elaboration from structural tuple
  imscriber.py   — Interactive assessment wizard

programs/
  ingest_ars_expanded.py  — Batch ingestion script for ARS_PHYTOGLYPHICA_EXPANDED

manuscripts/
  ENGINE.md               — Full engine specification
  VOYNICH_PHYTOGLYPHICA.md — Nine inaugural session runs with complete output
```

---

## Adding Entries

For individual unknowns: `vp imscribe`.

For batch ingestion, model on `programs/ingest_ars_expanded.py` — define a type tuple dict and an entries list, then run from the repo root. The script deduplicates by catalog key.

---

## Theory and Results

Full engine specification: `manuscripts/ENGINE.md`

Nine complete session runs across the inaugural corpus (wormwood, mandrake, ricin, opium, celandine, belladonna, henbane, foxglove, St. John's wort): `manuscripts/VOYNICH_PHYTOGLYPHICA.md`

The position of this project: the VMS resisted decipherment because it is not a cipher. It is a split-register executable whose six sections together constitute a complete computation, where the parameter values were externally supplied by the practitioner. Once the structural parameter space is known, any botanical entry in the corpus yields a determinate pharmaceutical protocol. The manuscript gives the instruction stream. The plant's structural type gives the parameters.

---

## Disclaimer

The *Voynich Phytogylphica* is provided **(1)** for education and edification and **(2)** free of strings or attachments, a loosing which proceeds bi-directionally  

This is to say, the author will not be held responsible for any effects resulting from the application of the information found herein this project

Don't be dumb

---

## License

Unlicense — public domain.
