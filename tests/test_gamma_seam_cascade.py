"""Fast root-discoverable original-source Gamma seam/cascade regression."""
import importlib.util
from pathlib import Path
from fractions import Fraction
import unittest

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'research'/'2026-11-02'/'gamma_seam_cascade'/'seam_cascade.py'
spec=importlib.util.spec_from_file_location('root_gamma_seam_cascade',path)
s=importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)


class GammaSeamCascadeRootTests(unittest.TestCase):
    def test_seam_finite_exact_original_source(self):
        self.assertEqual(s.r(1),Fraction(47,15))
        for n in range(0,10):
            for m in range(n,12):
                for b in (m,m+1,m+3):
                    self.assertTrue(s.verify_glue(n,m,b))

    def test_haar_energy_and_monotone_coherence(self):
        z=[(Fraction((i%4 in (0,1))-(i%4 in (2,3))),Fraction()) for i in range(64)]
        levels=s.exact_energy_cascade(z)
        self.assertEqual(levels[0][1],1)
        self.assertTrue(all(0<=r[3]<=r[1]<=1 for r in levels))
        self.assertEqual(sum((r[2] for r in levels),Fraction()),1-levels[-1][3])

    def test_coherent_changed_real_seed_fails_energy(self):
        z=[(Fraction(1),Fraction())]*64  # gauge-equivalent to e(h/5)
        levels=s.exact_energy_cascade(z)
        self.assertTrue(all(r[2]==0 for r in levels))
        self.assertEqual(levels[-1][3],1)


if __name__=='__main__':
    unittest.main()
