"""Preregistered post-commit heldout p-birth tests and exact SHA digest."""
import subprocess,sys,unittest
from pathlib import Path

class GammaHeldout(unittest.TestCase):
    def test_six_fresh_births_and_hostile_mutations(self):
        root=Path(__file__).resolve().parents[1]
        p=subprocess.run([sys.executable,str(root/"research"/"2026-11-04"/"gamma_pigeonhole"/"heldout_probe.py")],
                         capture_output=True,text=True,check=True,timeout=90)
        self.assertIn("FRESH_HOLDOUTS_6_PASS",p.stdout)
        self.assertIn("845730b09ea18e4eaa30645aa948d98f9e753be2428fa8e587f36da9acbeaf29",p.stdout)
