"""Explicit finite Galois character table: virtual averaging vs selected evaluation."""
import unittest
from fractions import Fraction as F
from math import gcd
from galois_selector import (phase,units15_with_characters,prime_characters,
                              table_test,run)

class GaloisSelectorTests(unittest.TestCase):
    def test_exact_original_n1_fingerprint(self):
        out=run()
        self.assertEqual(out['original_prefix'][0]['n'],1)
        self.assertEqual(out['selected_real_time_character_cancellation'],'OPEN')
        self.assertTrue(all(x['numerator_coprime'] for x in out['original_prefix']))

    def test_orthogonal_character_tables(self):
        for d,tab in [(15,units15_with_characters())]+[(p,prime_characters(p)) for p in (7,11,17)]:
            group=[u for u in range(1,d) if gcd(u,d)==1]
            for i,a in enumerate(tab):
                for j,b in enumerate(tab):
                    inner=sum(a[u]*b[u].conjugate() for u in group)/len(group)
                    self.assertLess(abs(inner-(1 if i==j else 0)),5e-12)

    def test_original_mean_and_nontrivial_energy(self):
        a=table_test(15,47,1,units15_with_characters())
        self.assertAlmostEqual(a['trivial_mean_abs_float'],1/8)
        self.assertAlmostEqual(a['nontrivial_L2_energy_float'],63/64)
        self.assertAlmostEqual(a['selected_phase_abs_float'],1)

    def test_mutation_noncoprime_changes_trivial_mean(self):
        actual=table_test(15,3,1,units15_with_characters())
        self.assertAlmostEqual(actual['trivial_mean_abs_float'],.25)
        self.assertNotAlmostEqual(actual['trivial_mean_abs_float'],.125)

    def test_prime_gauss_calibration(self):
        for p in (7,11,17):
            for h in (1,2,3):
                row=table_test(p,2,h,prime_characters(p))
                self.assertAlmostEqual(row['trivial_mean_abs_float'],1/(p-1),places=10)
                self.assertAlmostEqual(row['nontrivial_L2_energy_float'],1-1/(p-1)**2,places=10)

if __name__=='__main__': unittest.main()
