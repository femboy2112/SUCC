"""First TRUE source Suzuki g_J Legendre P1 derivative H¹ energy envelopes."""
import unittest
from fractions import Fraction as F
from observational_succ import one_object_true_derivative as d
from observational_succ import source_weil_hierarchy as src

def contains(a,x):
    return a.lo<=x<=a.hi

class OriginalDerivativeSourceTests(unittest.TestCase):
    def test_original_screw_integral_zero_and_prime_window(self):
        for J in (1,2,4):
            zero=d.original_screw_primitive_positive(F(),J)
            self.assertTrue(zero.lo<=0<=zero.hi)
            self.assertLess(zero.hi-zero.lo,F(1,10**18))
            for r in (F(1,8),F(1,2),F(3,4),F(1)):
                p=d.original_screw_primitive_positive(r,J)
                q=d.original_screw_signed_primitive(-r,J)
                self.assertEqual((p.lo,p.hi),(-q.hi,-q.lo))
                self.assertLess(p.hi-p.lo,F(1,10**18))

    def test_derivative_of_true_odd_low_mode_is_even(self):
        for J in (1,2,3):
            for x in (F(0),F(1,8),F(1,4),F(3,8),F(1,2)):
                right=d.genuine_first_legendre_derivative_at(x,J)
                left=d.genuine_first_legendre_derivative_at(-x,J)
                self.assertEqual((right.lo,right.hi),(left.lo,left.hi))
                self.assertTrue(right.lo<=right.hi)

    def test_first_legendre_true_derivative_energy_with_explicit_interval(self):
        for J,N in ((1,16),(2,64),(3,128)):
            cert=d.original_first_legendre_H1_energy(J,N)
            self.assertEqual(cert["original_true_prime_powers"],((2,2),))
            self.assertEqual(cert["Legendre_mode"],1)
            self.assertEqual(cert["source_node_variation_upper"],
                             2*cert["source_lipschitz_g"]/N)
            self.assertLessEqual(cert["unprojected_GJ_P1_derivative_L2_squared_lower"],
                                 cert["unprojected_GJ_P1_derivative_L2_squared_upper"])
            self.assertFalse(cert["genuine_30_mode_Q_projection_done"])
            self.assertFalse(cert["original_residual_DY_included"])
            self.assertFalse(cert["RH_proved"])

    def test_true_finite_low_energy_bound_improves_with_grid(self):
        vals=[d.original_first_legendre_H1_energy(2,N)
              for N in (8,16,32)]
        widths=[x["unprojected_GJ_P1_derivative_L2_squared_upper"]-
                x["unprojected_GJ_P1_derivative_L2_squared_lower"] for x in vals]
        self.assertGreater(widths[0],widths[1])
        self.assertGreater(widths[1],widths[2])

    def test_mpmath_original_suzuki_integral_holdout(self):
        try:import mpmath as mp
        except ImportError:self.skipTest("optional original high precision diagnostic")
        from observational_succ.gaussian_weil_certificates import signed_suzuki_g
        mp.mp.dps=70
        for J in (1,3):
            for t in (F(1,4),F(1,2),F(3,4)):
                cert=d.original_screw_primitive_positive(t,J)
                rr=mp.mpf(t.numerator)/t.denominator
                split=mp.log(2)
                pts=[mp.mpf(0)]+([split] if rr>split else [])+[rr]
                value=sum((mp.quad(lambda s:signed_suzuki_g(s,J,dps=70),
                                   [u,v]) for u,v in zip(pts,pts[1:])),mp.mpf(0))
                lo=mp.mpf(cert.lo.numerator)/cert.lo.denominator
                hi=mp.mpf(cert.hi.numerator)/cert.hi.denominator
                self.assertLessEqual(lo,value)
                self.assertGreaterEqual(hi,value)

    def test_forged_source_parameters_fail(self):
        for fn in (
            lambda:d.original_screw_primitive_positive(.5,2),
            lambda:d.original_screw_primitive_positive(F(2),2),
            lambda:d.original_screw_primitive_positive(F(1,2),0),
            lambda:d.genuine_first_legendre_derivative_at(F(3,4),2),
            lambda:d.original_first_legendre_H1_energy(0,16),
            lambda:d.original_first_legendre_H1_energy(2,1),
            lambda:d.original_first_legendre_H1_energy(2,512.0),
        ):
            with self.assertRaises(d.DerivativeSourceError):fn()

if __name__=="__main__":
    unittest.main()
