"""Root-discoverable exact causal echo / positive moment countermodel tests."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
_SOURCE=(Path(__file__).resolve().parents[1]/"research"/"2026-11-02"/"causal_echo_tomography"/"causal_echo_probe.py")
_spec=spec_from_file_location("_causal_echo_tomography_probe",_SOURCE)
assert _spec is not None and _spec.loader is not None
_module=module_from_spec(_spec)
_spec.loader.exec_module(_module)
CausalEchoTests=_module.CausalEchoTests
