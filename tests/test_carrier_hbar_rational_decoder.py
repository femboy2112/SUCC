"""Root-discoverable Euclidean rational decoder at source-bounded hbar mesh."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
_SOURCE=(Path(__file__).resolve().parents[1]/"research"/"2026-11-02"/"carrier_hbar_bridge"/"rational_reconstruction_probe.py")
_spec=spec_from_file_location("_carrier_hbar_rational_reconstruction",_SOURCE)
assert _spec is not None and _spec.loader is not None
_module=module_from_spec(_spec)
_spec.loader.exec_module(_module)
CarrierHbarRationalDecoder=_module.CarrierHbarRationalDecoder
