"""Root-discoverable regression for the additive unit–unit SUCC research proof forge.

Exact finite arithmetic only. Mathematical all-n theorems are in
research/2026-11-02/unit_unit_differential/PROOFS.md.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_SOURCE = (Path(__file__).resolve().parents[1] / "research" / "2026-11-02"
           / "unit_unit_differential" / "unit_unit_exact_probe.py")
_spec = spec_from_file_location("_unit_unit_exact_probe", _SOURCE)
assert _spec is not None and _spec.loader is not None
_module = module_from_spec(_spec)
_spec.loader.exec_module(_module)
UnitUnitDifferential = _module.UnitUnitDifferential
