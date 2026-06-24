"""
Plant-to-session navigator.

Bridges the IG catalog (cl8nk_navigator) to the Voynich session protocol.
Given a plant name from the catalog, derives the session parameters that
the VoynichSession expects: omega class, recommended potency/part/application,
and distance to each VMS section.
"""

from __future__ import annotations
import sys
from pathlib import Path
from typing import Optional

# cl8nk_navigator lives in imscribing_grammar/navigators/
_NAV_PATH = Path(__file__).parent.parent.parent / 'imscribing_grammar' / 'navigators'
if str(_NAV_PATH) not in sys.path:
    sys.path.insert(0, str(_NAV_PATH))

import cl8nk_navigator as _nav

_PRIM_KEYS = _nav.PRIMITIVE_KEYS  # ["Ð","Þ","Ř","Φ","ƒ","Ç","Γ","ɢ","⊙","Ħ","Σ","Ω"]

# Shavian winding values
_OMEGA_INTEGER = '𐑭'
_OMEGA_BINARY  = '𐑴'

# VMS section catalog names
_VMS_SECTIONS = {
    'astronomical':  'voynich_astronomical_section',
    'botanical':     'voynich_botanical_section',
    'biological':    'voynich_biological_section',
    'pharmaceutical':'voynich_pharmaceutical_section',
    'cosmological':  'voynich_cosmological_section',
    'recipe':        'voynich_recipe_section',
}

# Plant-part keywords for pharmacy lookup
_PART_KEYWORDS = {
    '𐑡': 'leaf',       # Þ=𐑡 branching network → leaf/flower dominant
    '𐑸': 'leaf',       # Þ=𐑸 holographic → whole-plant self-encoding
    '𐑰': 'root',       # Þ=𐑰 containment → root/rhizome
}

# Application from Ç (kinetics) value
_APPLY_KEYWORDS = {
    '𐑤': 'oral',       # Ç=𐑤 frozen-order → oral (stable delivery)
    '𐑧': 'inhalation', # Ç=𐑧 activated → inhalation
    '𐑺': 'cutaneous',  # Ç=𐑺 barrier → topical
}


def _tuple_from_entry(entry: dict) -> list[str]:
    """Extract the 12-value tuple list from a navigator result.

    resolve_system returns {'tuple': {'Ð': '𐑦', 'Þ': '𐑸', ...}}.
    Convert to ordered list using PRIMITIVE_KEYS.
    """
    t = entry.get('tuple') or entry.get('raw_tuple', {})
    if isinstance(t, dict):
        return [t.get(k, '—') for k in _PRIM_KEYS]
    if isinstance(t, (list, tuple)):
        return list(t)
    return []


def _tuple_dict(entry: dict) -> dict:
    """Return the raw dict form of the tuple (for tuple_distance)."""
    t = entry.get('tuple') or {}
    if isinstance(t, dict):
        return t
    return {k: v for k, v in zip(_PRIM_KEYS, t)}


def lookup(plant_name: str) -> dict:
    """
    Look up a plant in the IG catalog and return session parameters.

    Returns a dict with:
        name, tuple, omega_class, omega_shavian,
        pars_plantae, applicatio,
        distances: {section_name: float},
        recommended_potency: 'summa'|None
    """
    _nav.load_catalog()
    entry = _nav.resolve_system(plant_name)
    if entry is None:
        raise KeyError(f'Plant not found in catalog: {plant_name!r}')

    t = _tuple_from_entry(entry)   # ordered list for display / indexing
    if not t:
        raise ValueError(f'No tuple data for {plant_name!r}')

    # Ω is index 11
    omega_val = t[11] if len(t) > 11 else ''
    if omega_val == _OMEGA_INTEGER:
        omega_class = 'integer'
    elif omega_val == _OMEGA_BINARY:
        omega_class = 'binary'
    else:
        omega_class = 'other'

    # Þ (index 1) → recommended plant part
    thorn_val = t[1] if len(t) > 1 else ''
    pars_plantae = _PART_KEYWORDS.get(thorn_val)

    # Ç (index 5) → recommended application
    kin_val = t[5] if len(t) > 5 else ''
    applicatio = _APPLY_KEYWORDS.get(kin_val)

    # Distances to all VMS sections
    plant_dict = _tuple_dict(entry)
    distances: dict[str, float] = {}
    for section_label, catalog_name in _VMS_SECTIONS.items():
        sec = _nav.resolve_system(catalog_name)
        if sec:
            sec_dict = _tuple_dict(sec)
            if sec_dict:
                d, _ = _nav.tuple_distance(plant_dict, sec_dict)
                distances[section_label] = d

    # A plant at d=0 to astronomical section is "wormwood-class" → summa
    d_astro = distances.get('astronomical', float('inf'))
    recommended_potency = 'summa' if d_astro == 0.0 else None

    return {
        'name':                 plant_name,
        'tuple':                t,
        'omega_class':          omega_class,
        'omega_shavian':        omega_val,
        'pars_plantae':         pars_plantae,
        'applicatio':           applicatio,
        'distances':            distances,
        'recommended_potency':  recommended_potency,
        'd_astronomical':       d_astro,
    }


def list_vms_plants() -> list[str]:
    """Return all catalog entries that have 'voynich' in their name or description."""
    _nav.load_catalog()
    systems = _nav.list_catalog_systems()
    return [s for s in systems if 'voynich' in s.lower()]


# Phytoglyphica baseline: fixed for all VMS botanical entries.
_BASELINE = {'Ð': '𐑦', 'Þ': '𐑸', 'Ř': '𐑾', 'Φ': '𐑬', 'ƒ': '𐑱'}


def _is_phytoglyphica(entry: dict) -> bool:
    """True if the entry carries the phytoglyphica baseline tuple (flat catalog dict)."""
    return all(entry.get(k) == v for k, v in _BASELINE.items())


_TYPE_RE = __import__('re').compile(
    r'Type\s+(XI|IX|VIII|VII|VI|IV|III|II|X|V|I)'
)


def list_phytoglyphica(query: str | None = None) -> list[dict]:
    """
    Return all phytoglyphica botanical entries from the catalog.

    Each result dict has: name, description, tuple (dict), type_label.

    If query is given, filter to entries whose name or description contains
    the query string (case-insensitive).
    """
    _nav.load_catalog()

    results = []
    for raw in _nav.CATALOG:
        if not _is_phytoglyphica(raw):
            continue
        name = raw.get('name', '')
        desc = raw.get('description', '')
        if query and query.lower() not in name.lower() and query.lower() not in desc.lower():
            continue
        m = _TYPE_RE.search(desc)
        type_label = m.group(0) if m else ''
        results.append({
            'name':        name,
            'description': desc,
            'tuple':       {k: raw.get(k, '') for k in _PRIM_KEYS},
            'type_label':  type_label,
        })

    results.sort(key=lambda r: (r['type_label'], r['name']))
    return results


def section_tuples() -> dict[str, list[str]]:
    """Return the catalog tuples for all six VMS sections."""
    _nav.load_catalog()
    result = {}
    for label, name in _VMS_SECTIONS.items():
        entry = _nav.resolve_system(name)
        if entry:
            result[label] = _tuple_from_entry(entry)
    return result


def section_distances(tuple_vals: list[str]) -> dict[str, float]:
    """
    Compute distances from a raw tuple list to all six VMS sections.

    tuple_vals must be a 12-element list in PRIMITIVE_KEYS order.
    Returns {section_label: float}.
    """
    _nav.load_catalog()
    plant_dict = {k: v for k, v in zip(_PRIM_KEYS, tuple_vals)}
    distances: dict[str, float] = {}
    for section_label, catalog_name in _VMS_SECTIONS.items():
        sec = _nav.resolve_system(catalog_name)
        if sec:
            sec_dict = _tuple_dict(sec)
            if sec_dict:
                d, _ = _nav.tuple_distance(plant_dict, sec_dict)
                distances[section_label] = d
    return distances
