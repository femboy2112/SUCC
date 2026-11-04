"""Root-discoverable regression for authenticated carrier-relative hbar source tests.

Exact Fraction oracles live only in additive research package. No import
of historical oracle modules, and no modification of canonical sources.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_MODULE_PATH=(Path(__file__).resolve().parents[1] / "research" / "2026-11-02"
              / "carrier_hbar_bridge" / "carrier_hbar_exact_probe.py")
_spec=spec_from_file_location("_carrier_hbar_exact_probe",_MODULE_PATH)
assert _spec is not None and _spec.loader is not None
_module=module_from_spec(_spec)
_spec.loader.exec_module(_module)
CarrierHBarExact=_module.CarrierHBarExact
