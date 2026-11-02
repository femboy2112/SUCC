"""Discoverable exact authentic carrier/selected-cofiber tests (source unchanged)."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_SOURCE = (Path(__file__).resolve().parents[1] / "research" / "2026-11-02"
           / "oily_hbar_seam" / "oily_hbar_probe.py")
_spec = spec_from_file_location("_oily_hbar_selected_probe", _SOURCE)
assert _spec is not None and _spec.loader is not None
_module = module_from_spec(_spec)
_spec.loader.exec_module(_module)
OilyHbarSelectedProbe = _module.OilyHbarSelectedProbe
