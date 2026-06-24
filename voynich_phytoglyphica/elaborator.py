"""
Recipe elaborator — derives exact protocol parameters from an IG structural tuple.

Each of the 12 primitives encodes a concrete pharmaceutical parameter:

  Þ  (Topology)     → plant material specification & part selection
  Φ  (Parity)       → solvent system and polarity
  Ç  (Kinetics)     → extraction process, temperature, duration
  Σ  (Stoichiometry)→ drug:solvent mass ratio
  Γ  (Granularity)  → comminution specification
  Ω  (Winding)      → number of extraction cycles
  ƒ  (Fidelity)     → yield / concentration target
  Ħ  (Chirality)    → clarification / separation steps
  ɢ  (Coupling)     → fraction combination mode
  ⊙  (Criticality)  → threshold / endpoint criterion
  Ð  (Dimensionality)→ registration depth (structural note)
  Ř  (Recognition)  → pattern-completion class (structural note)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Primitive → protocol parameter tables
# ---------------------------------------------------------------------------

# Þ: plant topology → material type
_THORN = {
    '𐑡': ('aerial parts', 'leaf and stem, freshly dried'),
    '𐑰': ('root / rhizome', 'underground organs, cleaned and sliced'),
    '𐑥': ('whole plant', 'including seed heads and root crown'),
    '𐑶': ('bark / pericarp', 'outer cortex or fruit rind, dried'),
    '𐑸': ('flowering tops', 'whole entity in full anthesis, holographic self-similarity preserved'),
}

# Φ: parity → solvent system
_PHI = {
    '𐑗': ('water', '100% aqueous, pH 6–7'),
    '𐑿': ('dilute aqueous', '5–10% ethanol v/v in water'),
    '𐑬': ('hydroethanolic', '45–55% ethanol v/v in water (bilateral bridge)'),
    '𐑯': ('anhydrous ethanol', '>95% ethanol v/v'),
    '𐑹': ('fixed oil / CO₂', 'cold-pressed oil or supercritical CO₂ extract'),
}

# Ç: kinetics → process type and conditions
_KIN = {
    '𐑘': ('infusion', 'single-pass ambient infusion, 5–10 min, 20–25 °C'),
    '𐑤': ('cold maceration', '12–24 h maceration at 15–20 °C; frozen-order kinetics — no heat'),
    '𐑧': ('decoction', '15–30 min at 85–95 °C; activated kinetics — sustained heat'),
    '𐑪': ('percolation', 'slow percolation at ambient; diffusive kinetics — gravity-driven'),
    '𐑺': ('distillation', 'steam or vacuum distillation; barrier kinetics — phase-separated'),
}

# Σ: stoichiometry → drug:solvent ratio (w/v, g per mL)
_SIGMA = {
    '𐑙': ('1 : 1', '1 g plant material per 1 mL solvent (saturated)'),
    '𐑕': ('1 : 2', '1 g plant material per 2 mL solvent'),
    '𐑳': ('1 : 3', '1 g plant material per 3 mL solvent (triadic ratio)'),
}

# Γ: granularity → comminution specification
_GAMMA = {
    '𐑚': ('coarsely cut', '2–4 mm pieces; no further comminution'),
    '𐑔': ('moderately powdered', 'pass mesh 40 (355 μm); coarser residue discarded'),
    '𐑲': ('finely powdered', 'pass mesh 100 (150 μm); uniform surface exposure'),
}

# Ω: winding → extraction cycles
_OMEGA = {
    '𐑷': ('1 cycle', 'single extraction; trivial winding'),
    '𐑴': ('2 cycles', 'binary extraction; binary winding (ℤ₂-period)'),
    '𐑭': ('3 cycles', 'triple extraction; integer winding (ℤ-period, three complete turns)'),
    '𐑟': ('continuous', 'continuous percolation; non-Abelian winding (braid-group period)'),
}

# ƒ: fidelity → concentration target
_FIDELITY = {
    '𐑱': ('1× (standard)', 'no reduction; linear fidelity — proportional yield'),
    '𐑞': ('2× (concentrated)', 'reduce to half volume after extraction; quadratic fidelity'),
    '𐑐': ('3× (highly concentrated)', 'reduce to one-third volume; cubic fidelity; standardize to marker compound'),
}

# Ħ: chirality → clarification / separation
_HBAR = {
    '𐑓': ('racemic / no separation', 'use as-is; no chiral resolution'),
    '𐑒': ('single-step clarification', 'filter through coarse cloth or paper'),
    '𐑖': ('two-step clarification', 'filter through cloth, then decant supernatant after 24 h settling'),
    '𐑫': ('full chiral separation', 'preparative column or liquid–liquid partition (four-step)'),
}

# ɢ: coupling → fraction combination mode
_COUPLING = {
    '𐑝': ('sequential', 'add fractions one after another; evaluate each before combining'),
    '𐑜': ('paired', 'combine fractions in pairs; evaluate paired yield'),
    '𐑠': ('parallel', 'combine all fractions simultaneously in a single vessel'),
    '𐑵': ('broadcast', 'broadcast combined fraction to multiple preparation vessels'),
}

# ⊙: criticality → endpoint / threshold criterion
_CRIT = {
    '𐑢': ('sub-critical', 'stop before saturation; 70–80% extraction efficiency'),
    '⊙':  ('at criticality', 'extract to Frobenius fixed point; monitor until successive fractions differ < 5%'),
    '𐑮': ('near-critical', 'continue past threshold; successive fractions differ < 2%'),
    '𐑻': ('super-critical', 'drive to completion; < 1% residual in marc'),
    '𐑣': ('hyper-critical', 'exhaustive extraction; marc assayed for residual'),
}

# Primitive key order (matches tuple list index)
_PRIM_KEYS = ['Ð', 'Þ', 'Ř', 'Φ', 'ƒ', 'Ç', 'Γ', 'ɢ', '⊙', 'Ħ', 'Σ', 'Ω']
_PRIM_IDX  = {k: i for i, k in enumerate(_PRIM_KEYS)}


def elaborate_protocol(tuple_values: list[str]) -> dict:
    """
    Derive concrete pharmaceutical protocol parameters from a 12-value IG tuple.

    tuple_values: ordered list [Ð, Þ, Ř, Φ, ƒ, Ç, Γ, ɢ, ⊙, Ħ, Σ, Ω]

    Returns a dict with human-readable protocol fields.
    """
    def _get(key: str, table: dict) -> tuple[str, str]:
        idx = _PRIM_IDX.get(key)
        val = tuple_values[idx] if idx is not None and idx < len(tuple_values) else ''
        return table.get(val, ('—', f'unrecognised value {val!r}'))

    thorn_name,  thorn_desc  = _get('Þ',  _THORN)
    phi_name,    phi_desc    = _get('Φ',  _PHI)
    kin_name,    kin_desc    = _get('Ç',  _KIN)
    sigma_name,  sigma_desc  = _get('Σ',  _SIGMA)
    gamma_name,  gamma_desc  = _get('Γ',  _GAMMA)
    omega_name,  omega_desc  = _get('Ω',  _OMEGA)
    fid_name,    fid_desc    = _get('ƒ',  _FIDELITY)
    hbar_name,   hbar_desc   = _get('Ħ',  _HBAR)
    coup_name,   coup_desc   = _get('ɢ',  _COUPLING)
    crit_name,   crit_desc   = _get('⊙',  _CRIT)

    return {
        'material':       (thorn_name, thorn_desc),
        'solvent':        (phi_name, phi_desc),
        'process':        (kin_name, kin_desc),
        'ratio':          (sigma_name, sigma_desc),
        'comminution':    (gamma_name, gamma_desc),
        'cycles':         (omega_name, omega_desc),
        'concentration':  (fid_name, fid_desc),
        'clarification':  (hbar_name, hbar_desc),
        'combination':    (coup_name, coup_desc),
        'endpoint':       (crit_name, crit_desc),
    }


# Mapping from recipe step keywords to elaborated commentary
_STEP_ELABORATORS = {
    'divide':   'comminution',
    'tere':     'comminution',
    'calefac':  'process',
    'commisce': 'combination',
    'extrahe':  ('process', 'solvent', 'ratio'),
    'colare':   'clarification',
    'accipe':   'material',
    'compone':  ('combination', 'endpoint'),
    'applica':  None,
    'transmuta':'process',
}


def annotate_step(step_text: str, protocol: dict) -> list[str]:
    """
    Given a recipe step string, return annotation lines derived from the plant's
    protocol parameters.
    """
    lower = step_text.lower()
    notes = []
    proc_name, proc_desc = protocol['process']

    if 'divide' in lower or 'tere' in lower:
        name, desc = protocol['comminution']
        notes.append(f'    Comminution: {name} — {desc}')

    if 'extrahe' in lower or 'colare' in lower:
        _, sol = protocol['solvent']
        _, rat = protocol['ratio']
        _, cyc = protocol['cycles']
        _, clar = protocol['clarification']
        notes.append(f'    Solvent:  {sol}')
        notes.append(f'    Ratio:    {rat}')
        notes.append(f'    Cycles:   {cyc}')
        notes.append(f'    Endpoint: {protocol["endpoint"][1]}')
        if 'colare' in lower:
            notes.append(f'    Clarification: {clar}')

    if 'calefac' in lower:
        # If the plant's Ç is cold-process, Calefac applies to an adjunct
        # ingredient or excipient in the recipe, not the primary extract.
        if 'no heat' in proc_desc or 'cold' in proc_desc:
            notes.append(f'    Process (adjunct): heat excipient / base as needed')
            notes.append(f'    ⚠ Primary extract: {proc_desc} — do not heat')
        else:
            notes.append(f'    Process:  {proc_desc}')

    if 'commisce' in lower or 'compone' in lower:
        _, comb = protocol['combination']
        notes.append(f'    Combination: {comb}')
        if 'compone' in lower:
            _, endp = protocol['endpoint']
            notes.append(f'    Endpoint:    {endp}')

    if 'accipe' in lower:
        _, mat = protocol['material']
        notes.append(f'    Material: {mat}')

    if 'transmuta' in lower:
        # Volatile transformation — show full process detail; warn if cold-process plant
        notes.append(f'    Volatile phase: {proc_desc}')
        if 'no heat' in proc_desc or 'cold' in proc_desc:
            notes.append(f'    ⚠ Cold-process plant: protect extract from elevated temperature during transformation')

    if 'applica' in lower or 'administra' in lower:
        _, conc = protocol['concentration']
        notes.append(f'    Dosing form: {conc}')

    return notes


def format_protocol_header(plant_name: str, tuple_values: list[str],
                            protocol: dict) -> list[str]:
    """Render a complete protocol summary block for display."""
    lines = []
    width = 72
    lines.append('═' * width)
    lines.append(f'  ELABORATED PROTOCOL  {plant_name}')
    lines.append('─' * width)
    lines.append(f'  Tuple       ⟨{"⋅".join(tuple_values)}⟩')
    lines.append('─' * width)

    rows = [
        ('Material',      protocol['material']),
        ('Comminution',   protocol['comminution']),
        ('Solvent',       protocol['solvent']),
        ('Process',       protocol['process']),
        ('Ratio',         protocol['ratio']),
        ('Cycles',        protocol['cycles']),
        ('Endpoint',      protocol['endpoint']),
        ('Clarification', protocol['clarification']),
        ('Combination',   protocol['combination']),
        ('Concentration', protocol['concentration']),
    ]
    for label, (name, desc) in rows:
        lines.append(f'  {label:<14} {name}')
        lines.append(f'               {desc}')
    lines.append('═' * width)
    return lines
