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


def dosage_specification(tuple_values: list[str], d_astronomical: float) -> list[str]:
    """
    Derive specific dosage from the structural tuple and d_astronomical.

    Encoding (per VOYNICH_LIFTED.md phytoglyphic morphology→instruction mapping):
      Ç  → preparation form + base serving volume
      Σ  → dose frequency (compound-count complexity)
      Ω  → course duration (winding period determines treatment length)
      Ħ  → chirality safety modifier (more stereocenters → lower range)
      d_astronomical → potency tier (summa/alta/media/debilis) → dose multiplier
    """
    def _v(key: str) -> str:
        idx = _PRIM_IDX.get(key)
        return tuple_values[idx] if idx is not None and idx < len(tuple_values) else ''

    kin   = _v('Ç')
    sigma = _v('Σ')
    omega = _v('Ω')
    hbar  = _v('Ħ')

    # Potency tier from d_astronomical
    if d_astronomical == 0.0:
        tier, tier_label = 2.0, 'summa'
    elif d_astronomical <= 0.40:
        tier, tier_label = 1.5, 'alta'
    elif d_astronomical <= 1.00:
        tier, tier_label = 1.0, 'media'
    else:
        tier, tier_label = 0.5, 'debilis'

    # Preparation form + base serving volume (from Ç)
    _FORM_BASE = {
        '𐑘': ('infusion (tea)',          150, 200, 'mL',    None),
        '𐑤': ('tincture (cold maceration)', 2,  2, 'mL',   None),
        '𐑧': ('decoction',               150, 200, 'mL',    None),
        '𐑪': ('percolate tincture',        2,  2, 'mL',    None),
        '𐑺': ('essential oil / distillate', 2,  3, 'drops', 'in 5 mL carrier'),
    }
    form_name, base_lo, base_hi, unit, qualifier = _FORM_BASE.get(
        kin, ('preparation', 2, 2, 'mL', None)
    )

    # Apply potency multiplier
    if unit == 'drops':
        lo = round(base_lo * tier)
        hi = round(base_hi * tier)
    else:
        lo = round(base_lo * (tier / 1.0))   # mL or mL-tea
        hi = round(base_hi * (tier / 1.0))
    if lo == hi:
        dose_str = f'{lo} {unit}'
    else:
        dose_str = f'{lo}–{hi} {unit}'
    if qualifier:
        dose_str += f'  ({qualifier})'

    # Chirality safety note (from Ħ)
    _HBAR_NOTE = {
        '𐑓': '',
        '𐑒': '',
        '𐑖': '',
        '𐑫': 'use lower end of range (>4 stereocenters — chirality-sensitive)',
    }
    chiral_note = _HBAR_NOTE.get(hbar, '')

    # Frequency (from Σ + Ω)
    if omega == '𐑷':   # trivial winding
        freq = '2 × daily  (or as needed for single-use plants)'
    elif omega == '𐑴': # binary winding — two phases
        freq = '2 × daily  (one dose per extraction phase)'
    else:
        if sigma == '𐑙':   # single dominant compound
            freq = '2 × daily'
        else:
            freq = '3 × daily'

    # Course duration (from Ω + ⊙)
    crit = _v('⊙')
    if omega == '𐑭':
        if crit == '⊙':
            course = 'up to 6 weeks, then 2-week break before resuming'
        else:
            course = '4–6 weeks'
    elif omega == '𐑴':
        course = '2–4 weeks (acute course)'
    elif omega == '𐑷':
        course = 'as needed (short course or single use)'
    else:
        course = '4–6 weeks'

    # Daily total — calculation differs by form
    _SIGMA_RATIO = {'𐑙': 1, '𐑕': 2, '𐑳': 3}
    ratio = _SIGMA_RATIO.get(sigma, 3)
    doses_per_day = int(freq[0])
    daily_lines = []
    if kin in ('𐑤', '𐑪'):
        # Tincture: convert mL → dried herb equivalent via ratio
        herb_lo = round(lo * doses_per_day / ratio, 1)
        herb_hi = round(hi * doses_per_day / ratio, 1)
        vol_lo  = lo * doses_per_day
        vol_hi  = hi * doses_per_day
        vol_str = f'{vol_lo} mL' if vol_lo == vol_hi else f'{vol_lo}–{vol_hi} mL'
        herb_str = (f'{herb_lo} g' if herb_lo == herb_hi else f'{herb_lo}–{herb_hi} g')
        daily_lines.append(
            f'  Daily total  : {vol_str} tincture  ≡  {herb_str} dried herb/day  (1:{ratio} ratio)'
        )
    elif kin in ('𐑘', '𐑧'):
        # Infusion / decoction: report prepared volume only
        vol_lo = lo * doses_per_day
        vol_hi = hi * doses_per_day
        vol_str = f'{vol_lo} mL' if vol_lo == vol_hi else f'{vol_lo}–{vol_hi} mL'
        daily_lines.append(f'  Daily total  : {vol_str} prepared {form_name.split(" ")[0]}/day')
    elif kin == '𐑺':
        drop_lo = lo * doses_per_day
        drop_hi = hi * doses_per_day
        drop_str = f'{drop_lo}' if drop_lo == drop_hi else f'{drop_lo}–{drop_hi}'
        daily_lines.append(f'  Daily total  : {drop_str} drops in carrier/day')

    width = 72
    lines = ['─' * width, '  DOSAGE']
    lines.append('─' * width)
    lines.append(f'  Form         : {form_name}')
    lines.append(f'  Serving      : {dose_str}')
    lines.append(f'  Frequency    : {freq}')
    lines.append(f'  Course       : {course}')
    lines += daily_lines
    lines.append(f'  Potency tier : {tier_label}  (d_astronomical = {d_astronomical:.4f})')
    if chiral_note:
        lines.append(f'  ⚠ {chiral_note}')
    lines.append('═' * width)
    return lines


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
