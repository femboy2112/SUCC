"""Independent-style adversarial finite controls for TT-01..05; no proof of pi normality."""
import cmath
import unittest
from fractions import Fraction
from math import sqrt
import temporal_joining_probe as tj
import probe

class SourceClockTest(unittest.TestCase):
    def test_original_mod16_all_residues(self):
        for n in range(-64,80):
            self.assertEqual(tj.source_mod16(n),tj.source_mod16_formula(n))
    def test_source_phase_rotates_by_one_or_minus_three(self):
        for n in range(-50,51):
            d=(tj.source_mod16(n)-tj.source_mod16(n+1))%16
            self.assertEqual(d,15 if n%2==0 else 3)
            self.assertAlmostEqual(abs(tj.w(n)-tj.w_formula(n)),0,places=12)
    def test_source_clock_exact_nonzero_complex_reference(self):
        want=tj.e(-1/16)*(1+1j)/2
        self.assertLess(abs(tj.source_clock_kernel(1,1,1,1)-want),1e-12)
    def test_clock_lag_calibration_not_independent(self):
        for q in [16,256]:
            depth=1 if q==16 else 2
            pairs={(probe.stable_clock(n,depth),probe.stable_clock(n+1,depth)) for n in range(q)}
            self.assertEqual(len(pairs),q)
            self.assertEqual(len({a for a,b in pairs}),q)
            self.assertEqual(len({b for a,b in pairs}),q)

class CircleInterferometerTest(unittest.TestCase):
    def test_exact_two_readout_inverse(self):
        for x in [Fraction(0),Fraction(1,15),Fraction(1,17),Fraction(3,29)]:
            for B in [8,16,32]:
                for h in [-2,-1,1,2,5]:
                    true=tj.weyl_shell(B,h,x)
                    approx,corrected=tj.reconstructed_weyl(B,h,x)
                    self.assertLess(abs(true-corrected),1e-10)
                    self.assertLess(abs(true-approx),sqrt(2)/B+1e-10)
    def test_constant_coherent_counterseed_nonzero(self):
        # Completed source seed s=-pi/16 gives z_n=0 identically.
        expected=tj.e(-1/16)*(1+1j)/2
        for B in (8,16,32):
            self.assertLess(abs(tj.twisted_shell(B,1,Fraction(0))-expected),1e-12)
            self.assertLess(abs(tj.weyl_shell(B,1,Fraction(0))-1),1e-12)
    def test_nontrivial_clock_with_circle_temporal_phase(self):
        # 1/15 is a fixed nonnormal radix-16 point; h-16j=-15 is resonant there.
        expected=tj.source_clock_kernel(1,1,1,1)
        for B in [16,32]:
            value=tj.temporal_character(B,Fraction(1,15),1,1,1,1,1,1)
            self.assertLess(abs(value-expected),1e-11)
    def test_exact_temporal_reduction_for_any_rational_x(self):
        for x in [Fraction(1,15),Fraction(1,17),Fraction(3,29)]:
            for B in (16,32):
                q=16
                v=tj.temporal_character(B,x,1,1,3,2,1,1)
                rhs=sum(tj.e((probe.stable_clock(n,1)-probe.stable_clock(n+1,1))/q)
                        *tj.e(float((3-32)*tj.phase_rational(x,n)))
                        for n in range(B,2*B))/B
                self.assertLess(abs(v-rhs),1e-11)

class CriticalSourceTest(unittest.TestCase):
    def test_green_lag_exact_finite_source(self):
        for n in range(1,12):
            for k in range(1,5):
                self.assertTrue(tj.lag_green_finite(n,k,extra_depth=7))
    def test_certified_original_seam_counts(self):
        expected={8:0,16:3,32:2,64:8,96:4}
        for B,count in expected.items():
            report=tj.critical_pulse(B)
            self.assertEqual(report['seam_hits'],count)
            self.assertEqual(report['pi_normality'],'OPEN')
    def test_wrong_seed_maximal_seam_is_not_normality(self):
        # Coherent wrong seed: u=1-T, A=q-1, D=1 if qT<1.
        for B in (8,16,32,64):
            k=probe.critical_depth(B);q=16**k
            for n in range(B,2*B):
                _,upper=probe.green_bounds(n,6)
                self.assertLess(q*upper,1)
            result=sum(-tj.w(n) for n in range(B,2*B))/B
            expected=-tj.e(-1/16)*(1+1j)/2
            self.assertLess(abs(result-expected),1e-12)

if __name__=='__main__':
    unittest.main()
