from .navigator import lookup, list_vms_plants, section_tuples
from . import navigator

import sys
from pathlib import Path
_ENGINE = Path(__file__).parent.parent.parent / 'lang' / 'voynich-engine'
if str(_ENGINE) not in sys.path:
    sys.path.insert(0, str(_ENGINE))

from voynich_engine.session import VoynichSession, SessionState

__version__ = '1.0.0'
__all__ = [
    'VoynichSession',
    'SessionState',
    'lookup',
    'list_vms_plants',
    'section_tuples',
    'navigator',
]
