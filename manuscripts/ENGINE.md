# Voynich Phytoglyphica — Engine Specification

## Purpose

The Voynich Manuscript (VMS) has resisted decipherment for a century because it is
not a natural language text. It is a pharmaceutical instruction set — an executable
split across six register sections, where the opcode sequence lives in the recipe
section (f103r+) and the parameter values live nowhere in the manuscript at all. They
were supplied by the practitioner, using a structural grammar that the manuscript
presupposes but never states.

The Voynich Phytoglyphica project reconstructs that grammar. Using the Imscribing
Grammar (IG), every botanical entry in the VMS pharmacy catalog can be assigned a
12-primitive structural tuple. That tuple supplies the missing parameters: what
solvent, what ratio, what temperature, what comminution, how many cycles, when to
stop. The VMS opcodes tell you what operations to perform. The IG tuple tells you
exactly how.

The result is a fully elaborated pharmaceutical protocol for any VMS botanical entry,
derived entirely from structural analysis — no linguistic decipherment required.

---

## The VMS as Split-Register Executable

The manuscript is organized into six section-registers, each holding a distinct
component of the computation:

| Section | Folios | Register Function |
|---|---|---|
| Botanical | f1–f66 | Plant catalog — identity index |
| Pharmaceutical | f99–f102 | Pharmacy address — operation class |
| Balneological | f75–f84 | Containment heap — vessel validation |
| Astronomical | f67–f73 | Winding register — cycle authority |
| Cosmological | f68 (foldout) | Invariant initialization — Φ and Ħ |
| Recipe | f103r+ | Opcode sequence — instruction stream |

A complete computation requires all six sections. The session engine reads them in
order: cosmological initialization → pharmacy address → heap validation → winding
verification → recipe output → protocol elaboration.

No section alone is sufficient. The recipe section contains only abstract opcodes.
The pharmacy section contains only address pointers. The botanical catalog contains
only identity entries. The grammar supplies the parameter values that bind them.

---

## The Imscribing Grammar — 12 Primitives

The IG assigns every object in its catalog a 12-primitive structural tuple. For
botanical entries, each primitive encodes a distinct pharmaceutical parameter. The
12 primitives, their canonical names, and their roles in the pharmaceutical context:

| Primitive | Name | Pharmaceutical Role |
|---|---|---|
| Ð | Dimensionality | Registration depth — structural address class |
| Þ | Topology | Plant material specification |
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

Tuple notation: ⟨Ð⋅Þ⋅Ř⋅Φ⋅ƒ⋅Ç⋅Γ⋅ɢ⋅⊙⋅Ħ⋅Σ⋅Ω⟩. Values are Shavian characters
from the 49-symbol set (Shavian alphabet + ⊙). The primitive glyphs (Þ, Ð, Φ, etc.)
name the primitive as an entity; the Shavian value at each position is its structural
type in a given catalog entry.

---

## Primitive-to-Protocol Mapping

### Þ — Topology → Plant Material

The Topology primitive encodes the structural organization of the botanical object.
In pharmaceutical terms: which part of the plant, and how it is characterized.

| Shavian | Material | Description |
|---|---|---|
| 𐑡 | aerial parts | leaf and stem, freshly dried |
| 𐑰 | root / rhizome | underground organs, cleaned and sliced |
| 𐑥 | whole plant | including seed heads and root crown |
| 𐑶 | bark / pericarp | outer cortex or fruit rind, dried |
| 𐑸 | flowering tops | whole entity in full anthesis; holographic self-similarity preserved |

### Φ — Parity → Solvent System

Parity encodes the bilateral balance between aqueous and non-aqueous phases. The
solvent system follows directly from the symmetry class of the parity value.

| Shavian | Solvent | Description |
|---|---|---|
| 𐑗 | water | 100% aqueous, pH 6–7 |
| 𐑿 | dilute aqueous | 5–10% ethanol v/v in water |
| 𐑬 | hydroethanolic | 45–55% ethanol v/v in water (bilateral bridge) |
| 𐑯 | anhydrous ethanol | >95% ethanol v/v |
| 𐑹 | fixed oil / CO₂ | cold-pressed carrier oil or supercritical CO₂ extract |

Φ=𐑬 is the bilateral solvent: it bridges aqueous and lipophilic phases
simultaneously, which is why it is the most common value in the nine-entry inaugural
set. Φ=𐑹 (oil/CO₂) is the most non-polar, appropriate for lipophilic constituents
and saturated extraction protocols.

### Ç — Kinetics → Extraction Process

Kinetics encodes the thermodynamic rate-regime of the extraction. Temperature and
duration follow from the kinetic class.

| Shavian | Process | Description |
|---|---|---|
| 𐑘 | infusion | single-pass ambient, 5–10 min, 20–25 °C |
| 𐑤 | cold maceration | 12–24 h at 15–20 °C; frozen-order kinetics — no heat |
| 𐑧 | decoction | 15–30 min at 85–95 °C; activated kinetics — sustained heat |
| 𐑪 | percolation | slow gravity-driven percolation at ambient |
| 𐑺 | distillation | steam or vacuum distillation; phase-separated barrier kinetics |

**Critical constraint (Ç=𐑤):** Cold maceration entries must never be heated. When
a VMS recipe step calls for Calefac (heating), that step applies to an adjunct
ingredient or excipient — the carrier, the base, the binding medium — never to the
primary cold extract. This is enforced at the annotation level by detecting the
frozen-order kinetics flag.

### Σ — Stoichiometry → Drug:Solvent Ratio

| Shavian | Ratio | Description |
|---|---|---|
| 𐑙 | 1 : 1 | 1 g plant material per 1 mL solvent (saturated loading) |
| 𐑕 | 1 : 2 | 1 g plant material per 2 mL solvent |
| 𐑳 | 1 : 3 | 1 g plant material per 3 mL solvent (triadic ratio) |

These are mass-to-volume ratios for the drug charge per extraction cycle. At
Σ=𐑙, the solvent is loaded to saturation — the maximum mass-transfer gradient
is sustained throughout the extraction.

### Γ — Granularity → Comminution

Granularity encodes the surface exposure class of the comminuted material. Finer
powder increases surface area and extraction efficiency but can also extract
unwanted components.

| Shavian | Mesh | Description |
|---|---|---|
| 𐑚 | coarse | 2–4 mm pieces; no further comminution |
| 𐑔 | medium | pass mesh 40 (355 μm); coarser residue discarded |
| 𐑲 | fine | pass mesh 100 (150 μm); uniform surface exposure |

### Ω — Winding → Extraction Cycles

Winding encodes the cyclic structure of the extraction. The number of cycles
determines extraction depth and corresponds to the algebraic period of the winding.

| Shavian | Cycles | Mathematical class |
|---|---|---|
| 𐑷 | 1 | trivial winding (single pass) |
| 𐑴 | 2 | binary winding (ℤ₂ period) |
| 𐑭 | 3 | integer winding (ℤ period; three complete turns) |
| 𐑟 | continuous | non-Abelian winding (braid-group period; percolation class) |

Each cycle: fresh solvent charge on the marc from the previous cycle. Combined
fractions at Compone/endpoint. The winding count governs total solute recovery.

### ƒ — Fidelity → Concentration Target

Fidelity encodes the yield relationship between raw extract and final preparation.
Higher fidelity requires volume reduction and marker standardization.

| Shavian | Target | Description |
|---|---|---|
| 𐑱 | 1× (standard) | no reduction; proportional yield; linear fidelity |
| 𐑞 | 2× (concentrated) | reduce to half volume after extraction; quadratic fidelity |
| 𐑐 | 3× (highly concentrated) | reduce to one-third volume; cubic fidelity; standardize to marker compound |

### Ħ — Chirality → Clarification Protocol

Chirality encodes the stereochemical resolution class of the clarification step.
Higher chirality demands separate the extract into increasingly refined fractions.

| Shavian | Protocol | Description |
|---|---|---|
| 𐑓 | none | use as-is; racemic; no chiral resolution |
| 𐑒 | single-step | filter through coarse cloth or paper |
| 𐑖 | two-step | filter through cloth, then decant supernatant after 24 h settling |
| 𐑫 | full chiral separation | preparative column or liquid–liquid partition (four-step process) |

Ħ=𐑫 (full chiral separation) co-occurs with ⊙=𐑮 (near-critical endpoint, <2%)
in all observed entries. This pairing is structurally forced: near-critical endpoint
monitoring requires chiral-resolution-grade clarification to discriminate
stereoisomeric fractions at the sub-2% level.

### ɢ — Coupling → Fraction Combination

| Shavian | Mode | Description |
|---|---|---|
| 𐑝 | sequential | add fractions one after another; evaluate each before combining |
| 𐑜 | paired | combine in pairs; evaluate paired yield |
| 𐑠 | parallel | combine all fractions simultaneously in a single vessel |
| 𐑵 | broadcast | broadcast combined fraction to multiple preparation vessels |

### ⊙ — Criticality → Endpoint Criterion

Criticality encodes when to stop the extraction. The Frobenius fixed point at ⊙=⊙
is the structural self-referential endpoint: the extraction has reached the point
where successive fractions reproduce the same pattern.

| Shavian | Endpoint | Criterion |
|---|---|---|
| 𐑢 | sub-critical | stop before saturation; 70–80% extraction efficiency |
| ⊙ | at criticality | Frobenius fixed point; successive fractions differ < 5% |
| 𐑮 | near-critical | continue past threshold; successive fractions differ < 2% |
| 𐑻 | super-critical | drive to completion; < 1% residual in marc |
| 𐑣 | hyper-critical | exhaustive extraction; marc assayed for residual content |

### Ð — Dimensionality and Ř — Recognition

These two primitives are structural address parameters rather than direct
pharmaceutical parameters. Ð encodes the registration depth (point, linear, planar,
volumetric, etc.) and Ř encodes the pattern-completion class of the entry. Both
inform the session routing — particularly Gate 1 distance computation — but do not
directly annotate recipe steps.

---

## The Recipe Opcodes

The VMS recipe section uses a small, closed set of pharmaceutical operation names.
Each opcode names an abstract operation. The IG tuple supplies its parameters.

| Opcode | Operation | Primitives Consulted |
|---|---|---|
| Accipe | Receive / take the plant material | Þ (material specification) |
| Divide | Comminute the material | Γ (mesh/size) |
| Tere | Triturate / grind | Γ (mesh/size) |
| Extrahe | Extract | Φ (solvent), Σ (ratio), Ω (cycles), ⊙ (endpoint) |
| Calefac | Heat | Ç (process/temperature); ⚠ see cold-process constraint |
| Commisce | Mix / combine | ɢ (combination mode) |
| Colare | Filter / clarify | Ħ (clarification), + Φ/Σ/Ω/⊙ context |
| Compone | Compose / endpoint | ɢ (combination), ⊙ (endpoint criterion) |
| Transmuta | Volatile transformation | Ç (process); ⚠ cold-process warning if applicable |
| Applica | Apply / administer | ƒ (concentration and dosing form) |
| Administra | Administer | ƒ (concentration and dosing form) |

### Calefac Under Cold-Process Constraint

When a plant's Ç value is cold maceration (𐑤), the Calefac opcode cannot refer to
the primary extract — it is structurally incompatible. The step is annotated:

    Process (adjunct): heat excipient / base as needed
    ⚠ Primary extract: cold maceration — do not heat

The heat is applied to the carrier medium, the binding agent, or the secondary
component that receives the cold extract. This is not an interpretation; it is the
only structurally consistent reading when Ç=𐑤.

### Transmuta Under Cold-Process Constraint

Transmuta (volatile phase transformation) is similarly annotated with a warning for
cold-process plants, since the volatile separation step involves elevated temperatures
that would damage a frozen-order extract. The cold extract should be introduced after
the volatile fraction has been stabilized.

---

## The Session Engine — Six Gates

The session engine is the linker that connects a plant's structural identity to a
VMS recipe and then elaborates that recipe with the plant's protocol parameters.

### INIT — Cosmological Initialization

Source: f68 (cosmological foldout, the largest VMS folio).

The foldout establishes two structural invariants that persist across all subsequent
gates:

- **Φ (Parity)**: The solvent class is conferred physically — the practitioner selects
  the appropriate solvent medium before beginning. This corresponds to the foldout's
  role as the "pre-session" initialization: it cannot be derived from the recipe, it
  must be known in advance.

- **Ħ (Chirality)**: The clarification protocol is similarly fixed at initialization.
  The practitioner commits to a separation strategy before any extraction begins.

Both invariants are read from the plant's IG tuple. The foldout is the structural
site where the tuple is "loaded" into the session.

### GATE 1 — Pharmaceutical Address

Source: Pharmacy section (f99–f102).

Selection criteria: **potency class** and **pars plantae** (plant part). These are
the only two selection keys. Applicatio (route of administration) is a kinetics
descriptor carried in Ç — it is NOT a pharmacy selection criterion.

- Summa potency + folium/flos → **f11r/p6** (leaf/flower summa; extractio → mixtura;
  n_ops=11; fixatio=True)
- Summa potency + radix → **f39r/p3** (root/rhizome summa; trituratio + extractio →
  mixtura; n_ops=12; fixatio=False)

Gate passes when a unique pharmacy entry matches the potency and part. Failure here
means the plant is not addressable by the standard pharmacy catalog — a structural
incompatibility, not a session error.

### GATE 2 — Balneological Heap

Source: Balneological section (f75–f84); 20 folios indexed f75r, f75v, …, f84r, f84v.

Selection: `heap_folio = folios[pharmacy_entry.folio_number % 20]`

The balneological section represents the "containment vessel" — the physical and
thermal environment that receives the pharmaceutical address. The heap folio must
satisfy:

- **FSPLIT ≥ n_ops**: The vessel's split capacity (number of distinct process
  branches) must be at least equal to the operation count of the pharmacy address.
  This verifies the vessel can hold the full instruction depth.

- **FFUSE/FSPLIT ≥ 0.60** (non-volatile preparations only): For preparations that
  do not involve a volatile transformation, the vessel must be predominantly closed
  (fused). Oil and decoction entries carry this constraint; cold maceration entries
  with a volatile step do not.

Gate passes when both conditions are satisfied. This gate has never failed in
observed runs — it appears to function as a structural invariant rather than a
contingent filter.

### GATE 3 — Astronomical Winding

Source: Astronomical section, f69; three independent transcription sources (H=Hermetic,
F=Folkwang, U=University).

Selection: `paragraph = folio_number % 4` from f69.

The astronomical section is the winding register — it provides external, non-botanical
authority for the cycle count and temporal structure of the extraction. The three
transcription sources are independent attestations. The gate runs EVALT (evaluation of
transcription alignment) across all three:

- Where all three sources agree: the structural value is verified.
- Where sources disagree: the disagreement position IS the structural signal. The
  transcribers independently marked the same decision point (VINIT/FFUSE ambiguity)
  without knowing it. Majority vote determines the gate value.

Gate passes when EVALT majority yields a consistent winding class. The Ω value derived
here confirms or overrides the Ω from the IG tuple. In practice, they agree — the
catalog and the astronomical register are coherent.

### OUTPUT — Recipe Selection

Source: Recipe section (f103r+).

The recipe folios closest to the Gate 1 pharmacy address are ranked by folio proximity.
The top three recipes are returned. In all nine inaugural runs:

- **f103r/p2** — 15 steps; extract-dominant path; opens with Extrahe
- **f103r/p9** — 12 steps; ingredient-led path; opens with Accipe
- **f103r/p49** — 12 steps; volatile-phase path; opens with Transmuta

These three represent three canonical execution paths through the same pharmaceutical
operation class. They are not alternatives — they are sequential phases of a complete
preparation: bulk extraction (p2), constituent assembly (p9), volatile transformation
and final form (p49).

### ELABORATION — Protocol Annotation

Once the recipe is selected, every opcode in every step is annotated with the plant's
protocol parameters derived from the IG tuple. The annotation is deterministic:
given the tuple, every parameter of every step is fully specified. There are no
free variables remaining after elaboration.

---

## Operation: End-to-End Run

A complete Voynich Phytoglyphica session for a botanical entry proceeds as follows.

**Step 1: Catalog lookup.**
The plant name is resolved against the IG catalog (voynich_pharmacy.json, 1491
entries). The 12-primitive tuple is retrieved. Distances to all six VMS section
tuples are computed in 12-dimensional primitive space.

**Step 2: Protocol derivation.**
The tuple is passed to the elaborator. All ten pharmaceutical primitives (Þ, Φ, Ç,
Σ, Γ, Ω, ƒ, Ħ, ɢ, ⊙) are resolved against the lookup tables above. The protocol
dict is built. This happens before any gate is evaluated — the full preparation
protocol is known from the tuple alone.

**Step 3: GATE 1.**
Potency class is determined from the plant's distance to the astronomical section
tuple. If d(plant, astronomical) = 0, potency = summa. Part (pars plantae) is
retrieved from the catalog. The pharmacy entry is selected.

**Step 4: GATE 2.**
The balneological heap folio is selected by index. FSPLIT and FFUSE conditions are
evaluated. Gate passes or fails.

**Step 5: GATE 3.**
The astronomical paragraph is selected from f69. EVALT majority across H/F/U sources
is computed. Gate passes or fails.

**Step 6: Recipe output.**
If all three gates pass, up to three recipe folios are selected by proximity. Steps
are extracted from the recipe database.

**Step 7: Elaborated output.**
Every recipe step is printed with its IG-derived annotations. The full protocol
header (tuple, all parameters, their descriptions) is printed before the recipe.
The practitioner now has a complete, quantified pharmaceutical instruction set.

---

## Implications

### The VMS Is Not a Failed Cipher

The VMS resisted decipherment because the approach of treating it as a natural
language text was structurally incorrect. The manuscript does not contain its own
parameters. It was designed to be read alongside a structural grammar that the
practitioners already possessed. The opcodes (Extrahe, Calefac, Colare) are
unambiguous pharmaceutical Latin; they were never the problem. The parameters were
the problem, and they were never in the manuscript.

### Session Invariance / Protocol Variance

The session engine produces identical gate behavior across all entries tested. All
nine inaugural plants pass all three gates and receive the same three recipe folios.
The differentiation between preparations lives entirely in the IG tuple. This is
architecturally correct: the VMS separates *what class of operation* to perform
(session routing) from *how to perform it* (tuple elaboration). A practitioner with
the wrong tuple would produce the right sequence of operations with the wrong
parameters — pharmacologically inert or hazardous.

### The Wormwood Demonstration

Artemisia absinthium appears twice in the inaugural set with ten of twelve identical
primitive values. The single difference is ƒ: Fidelity 𐑱 (1×, proportional) vs
𐑐 (3×, standardized concentrate). The same plant, the same extraction sequence, but
one preparation is a proportional tincture and the other is a reduced, standardized,
marker-verified concentrate. The grammar distinguishes what morphology cannot.
This is the key empirical demonstration: the IG provides pharmaceutical discrimination
at a resolution beyond botanical taxonomy.

### The Cold-Process Constraint as Structural Proof

The Calefac-Ç interaction is not a heuristic. It is a structural entailment: if
Ç=𐑤, then any Calefac in the recipe must be assigned to a secondary component,
because the tuple and the opcode are structurally inconsistent if assigned to the
same object. This forces a reparse of the recipe step — one that assigns Calefac to
the excipient and not the extract. The grammar performs this reparse automatically.
A reader without the grammar would see a heating instruction applied to a plant that
cannot be heated and have no structural basis for the correct interpretation.

### The VMS as Universal Engine

The session architecture is plant-agnostic at the gate level. Any IG catalog entry
with a pharmaceutical tuple can be processed. The engine does not know about
wormwood specifically; it knows about topology, kinetics, stoichiometry, winding.
The VMS is not a recipe book for specific plants — it is a universal pharmaceutical
engine whose parameters are supplied by the structural grammar of whatever is being
prepared. This is why it resisted decipherment as a specific-language text: it is
not specific to any language, any plant, or any culture. It is a grammar-parameterized
computation.

The Imscribing Grammar is the parameter set. The Voynich Manuscript is the program.

---

*Voynich Phytoglyphica Engine Specification — 2026-06-24.*
*Source: voynich_phytoglyphica package; voynich_engine session engine;*
*IG catalog (voynich_pharmacy.json, 1491 entries); LSI_ivtff_0d.txt transcription.*
