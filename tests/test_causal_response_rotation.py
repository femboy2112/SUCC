"""Root test discovery: exact causal-response Fourier and phase-retrieval probes.

Imports the self-contained stdlib test class on a unique module name; avoids
implicit path shadowing of historical research utilities.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_SOURCE = (Path(__file__).resolve().parents[1] / "research" / "2026-11-02"
           / "causal_response_rotation" / "causal_rotation_probe.py")
_spec = spec_from_file_location("_causal_response_rotation_probe", _SOURCE)
assert _spec is not None and _spec.loader is not None
_module = module_from_spec(_spec)
_spec.loader.exec_module(_module)
CausalResponseTest = _module.CausalResponseTest
