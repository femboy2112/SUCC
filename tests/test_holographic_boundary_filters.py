"""Include the additive boundary-filter dossier in normal test discovery."""
import importlib.util
from pathlib import Path
import sys
import unittest


def load_tests(loader, standard_tests, pattern):
    directory = (Path(__file__).resolve().parents[1] / "research" /
                 "2026-11-12" / "holographic_boundary_filters")
    suite = unittest.TestSuite()
    sys.path.insert(0, str(directory))
    try:
        for path in sorted(directory.glob("test_*.py")):
            name = "_holographic_boundary_" + path.stem
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            suite.addTests(loader.loadTestsFromModule(module))
    finally:
        sys.path.pop(0)
    return suite
