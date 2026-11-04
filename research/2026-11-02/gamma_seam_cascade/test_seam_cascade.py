"""Standalone exact tests for original Gamma source seam and Haar cascade."""
from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest

P=Path(__file__).resolve().parent/'seam_cascade.py'
spec=importlib.util.spec_from_file_location('gamma_seam_exact',P)
s=importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)


class SeamCascadeTests(unittest.TestCase):
    def test_original_four_poles(self):
        for n in range(1,151):
            self.assertEqual(s.r(n),s.r_combined(n))
        self.assertEqual(s.r(1),Fraction(47,15))

    def test_finite_triple_gluing(self):
        for n in range(12):
            for m in range(n,16):
                for b in range(m,18):
                    self.assertTrue(s.verify_glue(n,m,b))

    def test_wrong_orientation_rejected(self):
        for bad in ((-1,0,1),(2,1,3),(1,3,2)):
            with self.assertRaises(ValueError):
                s.verify_glue(*bad)
        self.assertNotEqual(s.future_seam(1,4),-s.future_seam(1,4))

    def test_rational_tails_below_positive_gamma_upper(self):
        for n in range(1,24):
            F=s.future_seam(n,n+80)
            self.assertGreater(F,0)
            self.assertLess(F,s.tail_upper(n))

    def test_late_window_and_seam_error_bounds(self):
        for a in (1,4,16,128):
            self.assertGreater(s.left_cutoff_rephase_bound_over_pi(3,a),0)
            self.assertLess(s.late_source_character_l1_bound_over_pi(3,a),Fraction(3,30*a))
        for n,m,b in ((1,2,5),(9,16,31),(23,64,79)):
            self.assertEqual(s.seamed_state(n,m),s.seamed_state(n,b))

    def test_coherent_and_alternating_controls(self):
        one=(Fraction(1),Fraction())
        rows=s.exact_energy_cascade([one]*32)
        self.assertEqual(rows[0][1],1)
        self.assertTrue(all(row[2]==0 for row in rows))
        self.assertEqual(rows[-1][3],1)
        z=[(Fraction(1 if i%2==0 else -1),Fraction()) for i in range(32)]
        rows=s.exact_energy_cascade(z)
        self.assertEqual(rows[0][3],0)
        self.assertTrue(all(x[1]==0 for x in rows[1:]))

    def test_general_gaussian_rational_energy_identity(self):
        z=[(Fraction((i*3)%7,7),Fraction((i*i)%11,11)) for i in range(64)]
        rows=s.scale_energies(z)
        for j in range(len(rows)-1):
            self.assertEqual(rows[j][3],rows[j+1][1])
            E,W,P=rows[j][1:]
            self.assertEqual(P,2*E-W)
            C,frac=s.prefix_energy_ceiling(64,rows[j][0],E)
            self.assertGreaterEqual(C,0)
            self.assertGreater(frac,0)

    def test_positive_gamma_moments_are_not_signed_energy(self):
        for k in range(50):
            self.assertGreater(s.source_gamma_seam_sum_moments(k),0)


if __name__=='__main__':
    unittest.main()
