"""Expose the isolated research probes to SUCC's mandatory unittest gate."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys
import unittest


RESEARCH = Path(__file__).resolve().parents[1] / "research/2026-11-18/causal_235_local_dynamics"


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    sys.path.insert(0, str(RESEARCH))
    try:
        for name in ("test_fibonacci_235", "test_mixed_causal_shadow", "test_local_affine"):
            spec = spec_from_file_location("causal_235_"+name, RESEARCH/(name+".py"))
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            suite.addTests(loader.loadTestsFromModule(module))
    finally:
        sys.path.pop(0)
    return suite
