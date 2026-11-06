"""Run the Main XX research-local receipts (fronts A, B-numerics, C) inside the main suite.

The research directories keep their own unittest modules next to their probes;
this loader puts them under the mandated ``unittest discover -s tests`` gate.
No π-normality claim is tested anywhere: these are finite exact receipts.
"""
import importlib.util
import sys
import unittest
from pathlib import Path

FORGE = Path(__file__).resolve().parents[1] / "research" / "2026-11-05" / "main_xx_forge"
MODULES = {
    "main_xx_front_a_tests": FORGE / "front_a" / "test_front_a.py",
    "main_xx_front_b_numerics_tests": FORGE / "front_b" / "numerics" / "test_carry_transport.py",
    "main_xx_front_c_tests": FORGE / "front_c" / "test_front_c.py",
}


def _load(name, path):
    if str(path.parent) not in sys.path:
        sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for name, path in MODULES.items():
        suite.addTests(loader.loadTestsFromModule(_load(name, path)))
    return suite


if __name__ == "__main__":
    unittest.main()
