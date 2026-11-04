"""Run source-marked beta and Weyl cases through the repository's native discovery."""
from pathlib import Path
import subprocess
import sys
import unittest


RESEARCH = Path(__file__).resolve().parents[1] / "research/2026-11-04/europa_weyl"


class EuropaWeylResearchTests(unittest.TestCase):
    def test_marked_source_operators(self):
        subprocess.run([sys.executable, "-m", "unittest", "-q", "test_finite_weyl"],
                       cwd=RESEARCH / "weyl", check=True)

    def test_completed_beta_and_source_slices(self):
        subprocess.run([sys.executable, "-m", "unittest", "-q", "test_europa_probe"],
                       cwd=RESEARCH / "beta", check=True)
