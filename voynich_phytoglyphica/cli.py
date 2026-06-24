"""
Voynich Phytoglyphica — unified CLI.

  vp session   --folio f11r | --potency summa | --part root | --plant <name>
  vp plant     <name>
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
from .elaborator import elaborate_protocol, annotate_step, format_protocol_header
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

    # Step 3: run session
    sess  = _session_instance()
    state = sess.run(
        potency=potency,
        pars_plantae=part,
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

    return 0 if state.gate3_passed else 1


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

    args = parser.parse_args()

    dispatch = {
        'session':  cmd_session,
        'plant':    cmd_plant,
        'summa':    cmd_summa,
        'sections': cmd_sections,
        'compile':  cmd_compile,
        'run':      cmd_run,
    }

    if args.command not in dispatch:
        parser.print_help()
        sys.exit(0)

    sys.exit(dispatch[args.command](args))


if __name__ == '__main__':
    main()
