"""
Interactive imscription wizard for unknown phytoglyphica entries.

Walks the user through the 12-primitive assessment, computes the structural
tuple, shows Gate 1 distances, and optionally adds the entry to the catalog.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Optional

# ── Phytoglyphica baseline (fixed for all VMS plant entries) ─────────────────
# Ð Þ Ř Φ ƒ — frozen order, leaf-dominant, full-spectrum, balanced, concentration
BASELINE = {
    'Ð': '𐑦',  # frozen order — extraction sequence is fixed
    'Þ': '𐑸',  # leaf-dominant pharmaceutical organ
    'Ř': '𐑾',  # full-spectrum recognition
    'Φ': '𐑬',  # balanced potency
    'ƒ': '𐑱',  # concentration-dependent
}

PRIMITIVE_ORDER = ['Ð', 'Þ', 'Ř', 'Φ', 'ƒ', 'Ç', 'Γ', 'ɢ', '⊙', 'Ħ', 'Σ', 'Ω']

# ── Assessment questions for the 7 discriminating primitives ─────────────────
QUESTIONS = [
    {
        'primitive': 'Ç',
        'name': 'Kinetics — application route',
        'prompt': (
            'How does this plant\'s pharmaceutical action enter the body?'
        ),
        'options': [
            ('𐑤', 'Oral — dissolved in water, brewed, eaten, or tincture'),
            ('𐑧', 'Respiratory / decoction — steam inhalation, smoke, or strong boiling extraction'),
            ('𐑺', 'Cutaneous — topical application, skin absorption'),
        ],
    },
    {
        'primitive': 'Γ',
        'name': 'Granularity — extraction scale',
        'prompt': (
            'At what scale does extraction operate?'
        ),
        'options': [
            ('𐑔', 'Mesoscale — surface trichomes or oil glands yield on light mechanical action'),
            ('𐑲', 'Universal — requires cell-wall disruption: hard boiling, fermentation, or complex alkaloid matrix'),
            ('𐑵', 'Broadcast — mycelial or fungal network structure (for fungi only)'),
        ],
    },
    {
        'primitive': 'ɢ',
        'name': 'Coupling — self-modeling',
        'prompt': (
            'Does the plant\'s morphology encode its own pharmaceutical identity?'
        ),
        'options': [
            ('𐑠', 'Self-modeling — color, smell, texture, or architecture IS the self-report'),
            ('𐑝', 'Passive — no morphological self-report; content must be measured externally'),
            ('𐑵', 'Broadcast — mycelial or systemic communication (for fungi only)'),
        ],
    },
    {
        'primitive': '⊙',
        'name': 'Criticality',
        'prompt': (
            'Is this plant at structural criticality?\n'
            '  (Criticality = self-report present AND pharmaceutical identity structurally encoded)'
        ),
        'options': [
            ('⊙', 'At criticality — morphological self-report is unambiguous and complete'),
            ('𐑢', 'Non-critical — structurally opaque; criticality not reached'),
        ],
    },
    {
        'primitive': 'Ħ',
        'name': 'Chirality — stereochemical complexity',
        'prompt': (
            'What is the stereochemical complexity of the active compounds?'
        ),
        'options': [
            ('𐑖', 'Frobenius minimum (H2) — 1-2 stereocenters; standard pharmaceutical chirality'),
            ('𐑫', 'Eternal — >8 stereocenters, rigid scaffold, evolutionary permanence (taxanes, aconitine, steroids)'),
            ('𐑒', 'One-step — single chiral center; simple biosynthesis or single enzyme step'),
        ],
    },
    {
        'primitive': 'Σ',
        'name': 'Stoichiometry — compound class diversity',
        'prompt': (
            'How many distinct compound families define the pharmaceutical activity?'
        ),
        'options': [
            ('𐑳', 'Many — three or more distinct compound families (e.g. monoterpenes + sesquiterpenes + phenolics)'),
            ('𐑕', 'Few — two to four compound classes'),
            ('𐑙', 'Singular — one dominant compound class defines all pharmaceutical activity'),
        ],
    },
    {
        'primitive': 'Ω',
        'name': 'Winding — preparation phases',
        'prompt': (
            'How many distinct preparation phases does the protocol require?'
        ),
        'options': [
            ('𐑭', 'Integer — continuous multi-step protocol, variable depth (tea → tincture → decoction)'),
            ('𐑴', 'Binary — exactly two required phases (e.g. hot water + alcohol; MAOI + tryptamine)'),
            ('𐑷', 'Trivial — single step or no preparation (eat fresh, chew, add to water)'),
        ],
    },
]


def _hr(char: str = '─', width: int = 72) -> str:
    return char * width


def _ask_choice(question: dict) -> str:
    """Present a question and return the Shavian glyph of the chosen option."""
    print()
    print(f"  [{question['primitive']}]  {question['name']}")
    print(f"  {question['prompt']}")
    print()
    for i, (glyph, label) in enumerate(question['options'], 1):
        print(f"    {i}.  {glyph}  {label}")
    print()
    while True:
        raw = input('  Choice (number): ').strip()
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(question['options']):
                return question['options'][idx][0]
        print(f"  Please enter a number from 1 to {len(question['options'])}.")


def _ask_yn(prompt: str) -> bool:
    while True:
        raw = input(f'  {prompt} [y/n]: ').strip().lower()
        if raw in ('y', 'yes'):
            return True
        if raw in ('n', 'no'):
            return False


def _ask_str(prompt: str, required: bool = False) -> str:
    while True:
        raw = input(f'  {prompt}: ').strip()
        if raw or not required:
            return raw
        print('  (required)')


def run_assessment(catalog_path: Optional[Path] = None) -> int:
    """
    Interactive imscription wizard.  Returns 0 on success, 1 on abort.
    """
    width = 72
    print()
    print('═' * width)
    print('  VP IMSCRIBE — Structural Imscription Wizard')
    print('─' * width)
    print('  Leads you through the 12-primitive assessment for an unknown')
    print('  phytoglyphica entry.  The phytoglyphica baseline (Ð Þ Ř Φ ƒ)')
    print('  is fixed.  You will assess the 7 discriminating primitives.')
    print(_hr())

    try:
        # ── Identity ────────────────────────────────────────────────────────
        print()
        print('  IDENTITY')
        common   = _ask_str('Common name (will become the catalog key, e.g. blue_lotus)', required=True)
        key      = common.lower().replace(' ', '_').replace('-', '_')
        latin    = _ask_str('Latin name (e.g. Nymphaea caerulea Savigny)')
        family   = _ask_str('Family (e.g. Nymphaeaceae)')
        note     = _ask_str('One-line note (pharmaceutical character, key compounds, etc.)')

        # ── Baseline display ────────────────────────────────────────────────
        print()
        print(_hr())
        print('  PHYTOGLYPHICA BASELINE  (fixed for all VMS plant entries)')
        print(_hr())
        for prim in ['Ð', 'Þ', 'Ř', 'Φ', 'ƒ']:
            print(f'    {prim}  =  {BASELINE[prim]}')
        print()
        print('  Now assessing the 7 discriminating primitives ...')
        print(_hr())

        # ── Assessment loop ─────────────────────────────────────────────────
        assessed: dict[str, str] = {}
        for q in QUESTIONS:
            assessed[q['primitive']] = _ask_choice(q)

        # ── Build tuple ─────────────────────────────────────────────────────
        full = {**BASELINE, **assessed}
        tuple_vals = [full[p] for p in PRIMITIVE_ORDER]

        # ── Show tuple ──────────────────────────────────────────────────────
        print()
        print(_hr('═'))
        print('  IMSCRIPTION RESULT')
        print(_hr())
        print(f'  Name   : {key}')
        if latin:
            print(f'  Latin  : {latin}')
        if family:
            print(f'  Family : {family}')
        print(f'  Tuple  : ⟨{"⋅".join(tuple_vals)}⟩')
        print()
        print('  Primitive breakdown:')
        for prim in PRIMITIVE_ORDER:
            val = full[prim]
            tag = '  [baseline]' if prim in BASELINE else ''
            print(f'    {prim}  =  {val}{tag}')

        # ── Elaborate protocol ───────────────────────────────────────────────
        try:
            from .elaborator import elaborate_protocol, format_protocol_header
            protocol = elaborate_protocol(tuple_vals)
            print()
            print(_hr())
            for line in format_protocol_header(key, tuple_vals, protocol):
                print(line)
        except Exception:
            pass  # elaboration is informational; don't abort on failure

        # ── Distances to VMS sections ────────────────────────────────────────
        d_astronomical = float('inf')
        try:
            from . import navigator as nav
            dists = nav.section_distances(tuple_vals)
            d_astronomical = dists.get('astronomical', float('inf'))
            print()
            print(_hr())
            print('  Distances to VMS sections:')
            for sec, d in sorted(dists.items(), key=lambda x: x[1]):
                marker = ' ◀ d=0' if d == 0.0 else ''
                print(f'    {sec:<16} d = {d:.4f}{marker}')
        except Exception:
            pass

        # ── Dosage specification ─────────────────────────────────────────────
        try:
            from .elaborator import dosage_specification
            print()
            for line in dosage_specification(tuple_vals, d_astronomical):
                print(line)
        except Exception:
            pass

        # ── Catalog save ─────────────────────────────────────────────────────
        print()
        print(_hr())
        save = _ask_yn('Add this entry to the IG catalog?')
        if save:
            if catalog_path is None:
                catalog_path = Path(__file__).parent.parent / 'data' / 'IG_catalog.json'
            with open(catalog_path, encoding='utf-8') as f:
                catalog = json.load(f)
            existing = {e['name'] for e in catalog}
            if key in existing:
                print(f'  Entry "{key}" already exists in the catalog. Skipping save.')
            else:
                parts = []
                if latin:
                    parts.append(latin)
                if family:
                    parts.append(family)
                if note:
                    parts.append(note)
                desc = ' | '.join(parts) if parts else key
                entry = {'name': key, 'description': desc}
                for prim, val in zip(PRIMITIVE_ORDER, tuple_vals):
                    entry[prim] = val
                catalog.append(entry)
                with open(catalog_path, 'w', encoding='utf-8') as f:
                    json.dump(catalog, f, indent=2, ensure_ascii=False)
                print(f'  Saved: {key} added to catalog ({len(catalog)} entries total).')

        # ── Optional session run ─────────────────────────────────────────────
        run_session = _ask_yn('Run full VMS session with this tuple now?')
        if run_session:
            import argparse
            from .cli import cmd_run as _cmd_run
            # ensure entry exists in catalog for lookup
            if save and key not in (e['name'] for e in json.load(open(catalog_path, encoding='utf-8'))):
                print('  (entry not in catalog; cannot run session)')
            else:
                ns = argparse.Namespace(plant=key)
                return _cmd_run(ns)

        print()
        print('  Imscription complete.')
        print('═' * width)
        return 0

    except (KeyboardInterrupt, EOFError):
        print('\n  Aborted.')
        return 1
