"""
Voynich Phytoglyphica — unified CLI.

  vp session   --folio f11r | --potency summa | --part root | --plant <name>
  vp plant     <name>
  vp list                          # browse all catalog entries by structural type
  vp search    <keyword>           # keyword search across name + description
  vp summa
  vp sections
  vp compile   [--log FILE]
  vp run       <plant_name>        # full pipeline: catalog → session → recipe
  vp imscribe                      # interactive wizard for unknown entries

Run `vp <command> --help` for per-command options.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_HERE   = Path(__file__).parent.parent
_DATA   = _HERE / 'data'
_ENGINE = _HERE.parent / 'lang' / 'voynich-engine'

# ensure voynich_engine is importable
if str(_ENGINE) not in sys.path:
    sys.path.insert(0, str(_ENGINE))

from voynich_engine.session import VoynichSession
from . import navigator as nav
from .elaborator import elaborate_protocol, annotate_step, format_protocol_header, dosage_specification
from .imscriber import run_assessment


def _session_instance() -> VoynichSession:
    trans = _DATA / 'LSI_ivtff_0d.txt'
    return VoynichSession(
        data_dir=str(_DATA),
        transcription=str(trans) if trans.exists() else None,
    )


# ---------------------------------------------------------------------------
# vp session
# ---------------------------------------------------------------------------

def cmd_session(args: argparse.Namespace) -> int:
    sess  = _session_instance()
    state = sess.run(
        folio=args.folio,
        para=args.para,
        potency=args.potency,
        pars_plantae=args.part,
        applicatio=args.apply,
        forma=args.forma,
    )
    sess.report(state)
    return 0 if state.gate3_passed else 1


def _add_session_args(p: argparse.ArgumentParser) -> None:
    p.add_argument('--folio',   metavar='F',    help='Pharmaceutical folio (e.g. f11r)')
    p.add_argument('--para',    metavar='N', type=int)
    p.add_argument('--potency', metavar='P',    help='summa / alta / media / debilis')
    p.add_argument('--part',    metavar='PART', help='root / leaf / flower')
    p.add_argument('--apply',   metavar='APP',  help='oral / inhalation / cutaneous')
    p.add_argument('--forma',   metavar='FORM', help='pulvis / tinctura / decoctum …')


# ---------------------------------------------------------------------------
# vp plant
# ---------------------------------------------------------------------------

def cmd_plant(args: argparse.Namespace) -> int:
    try:
        info = nav.lookup(args.name)
    except KeyError as e:
        print(f'Not found: {e}')
        return 1

    PRIM = ['Ð','Þ','Ř','Φ','ƒ','Ç','Γ','ɢ','⊙','Ħ','Σ','Ω']
    width = 72
    print('═' * width)
    print(f'  PLANT  {info["name"]}')
    print('─' * width)
    t = info['tuple']
    if t:
        print('  Tuple  ⟨' + '⋅'.join(t) + '⟩')
    print(f'  Ω      {info["omega_shavian"]}  ({info["omega_class"]} winding)')
    print('─' * width)
    print('  Distances to VMS sections:')
    for sec, d in sorted(info['distances'].items(), key=lambda x: x[1]):
        marker = ' ◀ d=0' if d == 0.0 else ''
        print(f'    {sec:<16} d = {d:.4f}{marker}')
    print('─' * width)
    if info['recommended_potency']:
        print(f'  Recommended potency : {info["recommended_potency"]}  (d=0 to astronomical section)')
    if info['pars_plantae']:
        print(f'  Recommended part    : {info["pars_plantae"]}')
    if info['applicatio']:
        print(f'  Recommended apply   : {info["applicatio"]}')
    print('═' * width)
    return 0


# ---------------------------------------------------------------------------
# vp summa
# ---------------------------------------------------------------------------

def cmd_summa(_args: argparse.Namespace) -> int:
    sess = _session_instance()
    hits = sess.find_entries(potency='summa')
    print(f'Summa potency entries ({len(hits)}):')
    for e in hits:
        print(f'  {e.folio}/p{e.para}  n_ops={e.n_ops:2d}  '
              f'{e.pars_plantae:<32}  {e.forma}')
    return 0


# ---------------------------------------------------------------------------
# vp sections
# ---------------------------------------------------------------------------

def cmd_sections(_args: argparse.Namespace) -> int:
    tuples = nav.section_tuples()
    PRIM   = ['Ð','Þ','Ř','Φ','ƒ','Ç','Γ','ɢ','⊙','Ħ','Σ','Ω']
    width  = 80
    print('═' * width)
    print('  VMS SECTION TUPLES  (catalog-sourced)')
    print('─' * width)
    print(f'  {"Section":<16}  ' + '  '.join(f'{p:<3}' for p in PRIM))
    print('─' * width)
    order = ['botanical','pharmaceutical','biological','astronomical','cosmological','recipe']
    for sec in order:
        t = tuples.get(sec, [])
        row = '  '.join(f'{v:<3}' for v in t) if t else '—'
        print(f'  {sec:<16}  {row}')
    print('═' * width)
    return 0


# ---------------------------------------------------------------------------
# vp compile
# ---------------------------------------------------------------------------

def cmd_compile(args: argparse.Namespace) -> int:
    sys.path.insert(0, str(_ENGINE))
    from voynich_engine.compiler import compile_corpus, write_log, peak_folios

    trans = _DATA / 'LSI_ivtff_0d.txt'
    if not trans.exists():
        print(f'Transcription not found: {trans}')
        return 1

    print(f'Compiling {trans} …')
    result = compile_corpus(trans, verbose=True)
    print(f'\nFolios    : {result["folio_count"]}')
    print(f'Instructions: {result["total_instructions"]}')
    print(f'Registers : {result["total_registers"]}')
    print(f'Entropy Δ : {result["entropy_delta"]:.8f} J/K')
    print('\nPeak folios:')
    for name, regs in peak_folios(result):
        print(f'  {name}: {regs}')

    if args.log:
        write_log(result, args.log)
        print(f'\nLog written → {args.log}')
    return 0


# ---------------------------------------------------------------------------
# vp run  (full pipeline: plant name → catalog → session → recipe)
# ---------------------------------------------------------------------------

def cmd_run(args: argparse.Namespace) -> int:
    # Step 1: catalog lookup
    try:
        info = nav.lookup(args.plant)
    except KeyError:
        print(f'Plant not found in catalog: {args.plant!r}')
        print('Tip: try vp plant <name> to verify the catalog entry name.')
        return 1

    tuple_vals = info['tuple']
    print(f'  IG catalog entry   : {info["name"]}')
    print(f'  Tuple              : ⟨{"⋅".join(tuple_vals)}⟩')
    print(f'  d(plant, astro)    : {info["d_astronomical"]:.4f}')
    print()

    # Derive protocol from plant tuple before session
    protocol = elaborate_protocol(tuple_vals)

    # Print protocol header
    for line in format_protocol_header(info['name'], tuple_vals, protocol):
        print(line)
    print()

    # Step 2: Gate 1 selection — potency + part only (applicatio is a kinetics
    # parameter that informs the recipe elaboration, not a pharmacy selection key)
    potency = info['recommended_potency']
    part    = info['pars_plantae']

    # Step 3: run session — pass d_botanical for the ADDR gate
    d_botanical = info['distances'].get('botanical')
    sess  = _session_instance()
    state = sess.run(
        potency=potency,
        pars_plantae=part,
        d_botanical=d_botanical,
    )

    # Step 4: report session
    sess.report(state)

    # Step 5: elaborated recipe output
    if state.gate3_passed and state.recipe:
        width = 72
        print()
        print('═' * width)
        print('  ELABORATED RECIPE OUTPUT')
        print('─' * width)
        for r in state.recipe:
            print(f'  {r["folio"]}/p{r["para"]}  ({r["n_steps"]} steps, {r["n_ops"]} ops)')
            for step in r['steps']:
                print(f'  {step}')
                for note in annotate_step(step, protocol):
                    print(note)
            print()
        print('═' * width)

    # Step 6: dosage specification — always displayed at end
    print()
    for line in dosage_specification(tuple_vals, info['d_astronomical']):
        print(line)

    return 0 if state.gate3_passed else 1


# ---------------------------------------------------------------------------
# vp list  (browse all phytoglyphica catalog entries by structural type)
# ---------------------------------------------------------------------------

_TYPE_NAMES = {
    'Type I':    'Aromatic Baseline',
    'Type II':   'Tropane',
    'Type III':  'Cardiac Glycoside',
    'Type IV':   'Non-Critical Aromatic',
    'Type V':    'Eternal / Axiom A',
    'Type VI':   'Adaptogen',
    'Type VII':  'β-Carboline',
    'Type VIII': 'Caffeine-Purine',
    'Type IX':   'Opioid Alkaloid',
    'Type X':    'Triterpene Saponin',
    'Type XI':   'Fungal Interface',
}


def cmd_list(_args: argparse.Namespace) -> int:
    entries = nav.list_phytoglyphica()
    if not entries:
        print('No phytoglyphica entries found in catalog.')
        return 1

    # only show entries that carry a structural type label
    labeled   = [e for e in entries if e['type_label']]
    unlabeled = len(entries) - len(labeled)

    # group by type_label (already sorted)
    from itertools import groupby
    width = 72
    print('═' * width)
    print(f'  VOYNICH PHYTOGLYPHICA  —  {len(labeled)} catalog entries  ({11} types)')
    print('─' * width)
    for type_label, group in groupby(labeled, key=lambda e: e['type_label']):
        display = f'{type_label}  {_TYPE_NAMES.get(type_label, "")}'
        print(f'\n  ▸ {display}')
        for e in group:
            # pull Latin name + family from description  "Latin | Family — ..."
            desc = e['description']
            bio = ''
            if '|' in desc and '—' in desc:
                bio = desc.split('|')[0].strip()
            elif '|' in desc:
                bio = desc.split('|')[0].strip()
            line = f'    {e["name"]:<32}  {bio}'
            print(line[:width])

    print()
    print('─' * width)
    if unlabeled:
        print(f'  ({unlabeled} pre-existing catalog entries share the phytoglyphica baseline'
              f' but have no type label — use vp plant <name> to access them)')
    print('  Use: vp plant <name>  or  vp run <name>')
    print('  Or:  vp search <keyword>  to filter by name, family, or compound class')
    print('═' * width)
    return 0


# ---------------------------------------------------------------------------
# vp search  (keyword search across name + description)
# ---------------------------------------------------------------------------

def cmd_search(args: argparse.Namespace) -> int:
    query = args.query
    entries = nav.list_phytoglyphica(query=query)
    width = 72
    print('═' * width)
    if not entries:
        print(f'  No entries matching {query!r}')
        print('═' * width)
        return 1

    print(f'  SEARCH  {query!r}  →  {len(entries)} match{"es" if len(entries) != 1 else ""}')
    print('─' * width)
    for e in entries:
        type_label = e['type_label'] or '?'
        desc = e['description']
        # brief: up to first period or 60 chars, whichever comes first
        brief_start = desc.find('—')
        brief = desc[brief_start + 1:].strip() if brief_start != -1 else desc
        if '.' in brief:
            brief = brief[:brief.index('.') + 1]
        brief = brief[:58]
        print(f'  {e["name"]:<32}  [{type_label}]')
        print(f'    {brief}')
    print('═' * width)
    return 0


# ---------------------------------------------------------------------------
# vp imscribe  (interactive wizard for unknown entries)
# ---------------------------------------------------------------------------

def cmd_imscribe(args: argparse.Namespace) -> int:
    catalog_path = _DATA / 'IG_catalog.json'
    return run_assessment(catalog_path=catalog_path)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        prog='vp',
        description='Voynich Phytoglyphica — Universal Engine session protocol',
    )
    sub = parser.add_subparsers(dest='command', metavar='COMMAND')

    # session
    p_sess = sub.add_parser('session', help='Run the six-gate Voynich session')
    _add_session_args(p_sess)

    # plant
    p_plant = sub.add_parser('plant', help='Look up a plant in the IG catalog')
    p_plant.add_argument('name', help='Catalog entry name (e.g. artemisia_absinthium)')

    # list
    sub.add_parser('list', help='Browse all phytoglyphica catalog entries by structural type')

    # search
    p_search = sub.add_parser('search', help='Keyword search across plant name and description')
    p_search.add_argument('query', help='Keyword (e.g. artemisia, Lamiaceae, tropane)')

    # summa
    sub.add_parser('summa', help='List all summa potency pharmaceutical entries')

    # sections
    sub.add_parser('sections', help='Show catalog-sourced tuples for all six VMS sections')

    # compile
    p_comp = sub.add_parser('compile', help='Compile the EVA transcription to IMASM')
    p_comp.add_argument('--log', metavar='FILE', help='Write full instruction log')

    # run
    p_run = sub.add_parser('run', help='Full pipeline: plant name → catalog → session → recipe')
    p_run.add_argument('plant', help='Catalog entry name (e.g. artemisia_absinthium)')

    # imscribe
    sub.add_parser('imscribe', help='Interactive wizard: assess an unknown plant and derive its structural tuple')

    args = parser.parse_args()

    dispatch = {
        'session':  cmd_session,
        'plant':    cmd_plant,
        'list':     cmd_list,
        'search':   cmd_search,
        'summa':    cmd_summa,
        'sections': cmd_sections,
        'compile':  cmd_compile,
        'run':      cmd_run,
        'imscribe': cmd_imscribe,
    }

    if args.command not in dispatch:
        parser.print_help()
        sys.exit(0)

    sys.exit(dispatch[args.command](args))


if __name__ == '__main__':
    main()
