"""Root SUCC test discovery for exact Q(i) cosmic fingerprint experiments."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

_SOURCE = (Path(__file__).resolve().parents[1] / 'research' / '2026-11-02'
           / 'cosmic_fingerprint' / 'cosmic_fingerprint_probe.py')
_spec = spec_from_file_location('_cosmic_fingerprint_probe', _SOURCE)
assert _spec and _spec.loader
_module = module_from_spec(_spec)
sys.modules[_spec.name] = _module
_spec.loader.exec_module(_module)
CosmicFingerprintExact = _module.CosmicFingerprintExact
