"""Include the additive adaptive-boundary dossier in native discovery."""
import importlib.util
from pathlib import Path
import sys
import unittest


def load_tests(loader, standard_tests, pattern):
    directory = (Path(__file__).resolve().parents[1] / "research" /
                 "2026-11-12" / "adaptive_boundary_resolution")
    suite = unittest.TestSuite()
    sys.path.insert(0, str(directory))
    try:
        for path in sorted(directory.glob("test_*.py")):
            name = "_adaptive_boundary_" + path.stem
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            suite.addTests(loader.loadTestsFromModule(module))
    finally:
        sys.path.pop(0)
    return suite
