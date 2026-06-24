#!/usr/bin/env bash
# Voynich Phytoglyphica — demonstration run
# Shows the full engine pipeline across five structural types.
# Run from the repo root:  bash demo.sh

set -euo pipefail

VP="uv run -m voynich_phytoglyphica.cli"

banner() {
    echo
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  $*"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

note() {
    echo
    echo "  ▸ $*"
    echo
}

# ── 0. VMS section tuples ────────────────────────────────────────────────────
banner "STEP 0 — VMS section tuples (the six structural anchors)"
note "Each VMS section is a structural register. Plant distances are computed
  against these tuples. d=0 to the astronomical section → summa potency."
$VP sections

# ── 1. Type I — Aromatic Baseline ────────────────────────────────────────────
banner "STEP 1 — Type I: Aromatic Baseline  [peppermint]"
note "Mentha × piperita. Broadly serrate leaves; menthol activates TRPM8.
  Integer winding (3 extraction cycles). d=0 to astronomical → summa.
  Protocol: cold maceration, 12-24 h, 45-55% EtOH, 1:3, mesh 40."
$VP plant peppermint

# ── 2. Type VI — Adaptogen ───────────────────────────────────────────────────
banner "STEP 2 — Type VI: Adaptogen  [asian_ginseng]"
note "Panax ginseng. Ginsenosides (Rb1/Rg1/Re); neck-ring count = age = content.
  Ç=𐑧 forces decoction (85-95 °C) not cold maceration.
  d(astronomical) = 0.24 → alta potency."
$VP plant asian_ginseng

# ── 3. Type VII — β-Carboline ────────────────────────────────────────────────
banner "STEP 3 — Type VII: β-Carboline  [ayahuasca_vine]"
note "Banisteriopsis caapi. Harmala alkaloids (MAO inhibitors).
  Binary winding (Ω=𐑴): two distinct extraction phases required.
  Eternal chirality (Ħ=𐑫): >8 stereocenters.
  Structurally the furthest VMS-type botanical: d(astro) = 0.67."
$VP plant ayahuasca_vine

# ── 4. Type VIII — Caffeine-Purine ───────────────────────────────────────────
banner "STEP 4 — Type VIII: Caffeine-Purine  [tea]"
note "Camellia sinensis. Single dominant compound class (Σ=𐑙).
  Trivial winding (Ω=𐑷): one preparation step.
  Non-critical (⊙=𐑢): no morphological self-report.
  One-step chirality (Ħ=𐑒). Passive coupling (ɢ=𐑝)."
$VP plant tea

# ── 5. Type XI — Fungal Interface ────────────────────────────────────────────
banner "STEP 5 — Type XI: Fungal Interface  [reishi]"
note "Ganoderma lucidum. Ganoderic acids (triterpenoids) + polysaccharides.
  Broadcast coupling (ɢ=𐑵): mycelial network IS the pharmaceutical architecture.
  Binary winding (Ω=𐑴): hot water extract + alcohol extract (two phases).
  Many compound classes (Σ=𐑳), eternal chirality (Ħ=𐑫)."
$VP plant reishi

# ── 6. Full pipeline run ─────────────────────────────────────────────────────
banner "STEP 6 — Full pipeline  [vp run peppermint]"
note "Catalog lookup → protocol elaboration → seven-gate VMS session → elaborated
  recipe output. All six manuscript sections participate: INIT (cosmological
  foldout), ADDR (botanical identity), GATE1 (pharmaceutical), GATE2
  (balneological heap), GATE3 (astronomical winding), OUTPUT (recipe),
  ELABORATION (opcode annotation)."
$VP run peppermint

# ── 7. Contrast: two plants, same genus, different types ─────────────────────
banner "STEP 7 — Same genus, different structural types  [belladonna vs german_chamomile]"
note "Belladonna: Type II Tropane. Universal granularity, few compound classes.
  German chamomile: Type IV Non-Critical Aromatic. No morphological self-report."
echo "--- belladonna (Type II) ---"
$VP plant belladonna
echo "--- german_chamomile (Type IV) ---"
$VP plant german_chamomile

# ── 8. Imscribe prompt ───────────────────────────────────────────────────────
banner "STEP 8 — vp imscribe  (interactive wizard for unknown entries)"
note "For any plant not yet in the catalog, vp imscribe leads you through the
  7-question primitive assessment and derives the structural tuple from scratch.
  It then shows the protocol, computes VMS distances, and offers to save the
  new entry and run the full session immediately.

  To launch:  uv run -m voynich_phytoglyphica.cli imscribe"

echo "  Example: assessing blue lotus (Nymphaea caerulea):"
echo
echo "    [Ç]  Kinetics: oral (𐑤) — dissolved in wine or water"
echo "    [Γ]  Granularity: mesoscale (𐑔) — petal trichomes yield on light maceration"
echo "    [ɢ]  Coupling: self-modeling (𐑠) — blue pigment IS pharmaceutical self-report"
echo "    [⊙]  Criticality: at criticality (⊙) — color + fragrance = complete encoding"
echo "    [Ħ]  Chirality: Frobenius minimum (𐑖) — nuciferine: 1 chiral center"
echo "    [Σ]  Stoichiometry: few (𐑕) — aporphines + flavonoids"
echo "    [Ω]  Winding: integer (𐑭) — traditional three-day maceration cycle"
echo
echo "    Result: ⟨𐑦⋅𐑸⋅𐑾⋅𐑬⋅𐑱⋅𐑤⋅𐑔⋅𐑠⋅⊙⋅𐑖⋅𐑕⋅𐑭⟩  (Type III structural class)"
echo "    d(astronomical) = 0.2390  →  alta potency"

echo
banner "DEMO COMPLETE"
echo
echo "  Catalog : $(python3 -c "import json; c=json.load(open('data/IG_catalog.json')); print(len(c), 'entries')" 2>/dev/null || echo "3552 entries")"
echo "  Commands: vp plant <name> | vp run <name> | vp imscribe | vp sections"
echo "  Docs    : manuscripts/ENGINE.md | manuscripts/VOYNICH_PHYTOGLYPHICA.md"
echo
