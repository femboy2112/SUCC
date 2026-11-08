"""Focused finite regression controls; theorem proofs must be checked in THEOREMS.md."""
import unittest
from fractions import Fraction
from experiment import (source,four_poles,triangle_tests,frequency_tests,raw_orbit,
                        borrow_test,source_mass,energy,arbitrary_lag_clone,
                        dyadic_shell_energy,shadow_energy_controls,overlaps,mod_odd,
                        isometric_v_mod)

class TriangleSilverSpectrumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x,cls.c=raw_orbit(545)

    def test_authentic_source_polynomial_and_four_poles(self):
        for n in range(1,257):
            self.assertEqual(source(n),four_poles(n))
            self.assertEqual(source(n).denominator%2,1)

    def test_integer_and_fractional_2adic_seam(self):
        for k in range(1,13):
            mod=1<<k
            for n in (0,1,2,17,73,128,293):
                self.assertEqual((mod_odd(self.x[n],mod)+self.c[n])%mod,
                                 isometric_v_mod(n,mod))

    def test_triangle_kernel_and_source_plane(self):
        self.assertEqual([x['fiber_cardinality'] for x in triangle_tests()],[2,2,2])

    def test_spoofed_carry_negative_control(self):
        for k in range(1,13):
            mod=1<<k;half=mod//2
            c=11;x=37;v=(c+x)%mod
            aa,bb,dd=overlaps(v,c+half,x,mod)
            # Critically: a false raw seam passes the modular closure relation.
            self.assertEqual((aa+dd-3*bb)%mod,0)
            self.assertEqual((v-(c+half)-x)%mod,half)
            self.assertEqual((2*(v-(c+half)-x))%(2*mod),mod)

    def test_haar_seed_variance_frequency_distinct(self):
        self.assertEqual([x['frequency_count'] for x in frequency_tests()],[24,18,24])

    def test_exact_harmonic_mass_finite_enclosure(self):
        self.assertEqual([x['N'] for x in source_mass()['finite_checks']],[128,512])

    def test_arbitrary_lags_original_clone(self):
        self.assertEqual(arbitrary_lag_clone()['cases'],21)

    def test_carry_borrow_exact_and_stratified_finite(self):
        out=borrow_test(self.x,self.c)
        self.assertEqual([x['cases'] for x in out],[384]*4)
        for row in out:
            self.assertEqual(row['lower_carry_agrees']['count']+
                             row['lower_carry_differs']['count'],384)

    def test_return_energy_and_2adic_labels(self):
        for Q in (4,8,16):
            v=energy(self.x,self.c,Q,512//Q)
            self.assertLessEqual(v['W_abs_squared_float'],v['R_float']+1e-10)
            self.assertLess(v['relabel_difference_float'],1e-12)

    def test_signed_shell_reassembly_and_nonnormal_shadow(self):
        for Q in (4,8,16):
            v=dyadic_shell_energy(self.x,Q,512//Q)
            self.assertAlmostEqual(v['reconstructed_R_float'],v['direct_R_float'],places=10)
        self.assertTrue(all(x['R_shadow_float']>.8 for x in shadow_energy_controls()))

if __name__=='__main__':unittest.main()
