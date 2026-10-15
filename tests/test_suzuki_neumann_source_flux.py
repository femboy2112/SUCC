"""Authentic Weil/Suzuki first low mode contact-corrected Neumann dual flux."""
import unittest
from fractions import Fraction as F
from observational_succ import suzuki_neumann_source_flux as g

class AuthenticNeumannFlux(unittest.TestCase):
    def test_exact_weighted_exponential_source_factors(self):
        for lam in (F(1,2),F(-1,2),F(-5,2),F(-33,2)):
            r=g.weighted_exponential(lam)
            self.assertLessEqual(r.lo,r.hi)
            # Decaying Gamma kernel correlates positively with decreasing
            # linear source test 1-2t; increasing exp correlates negatively.
            if lam<0:self.assertGreaterEqual(r.hi,0)
            else:self.assertLessEqual(r.lo,0)

    def test_original_prime_gamma_contact_flux_interval_and_parity(self):
        for J in (1,2,4,8,16):
            x=g.genuine_infinite_first_flux(J)
            lo,hi=x["full_infinite_source_flux_interval"]
            self.assertLessEqual(lo,hi)
            self.assertEqual(x["original_prime_powers"],((2,2),))
            self.assertEqual(x["half_density"],F(1,2))
            self.assertFalse(x["original_30_mode_Gram_computed"])
            self.assertFalse(x["rh_proved"])
        # A strict ORIGINAL infinite source sign statement, not a
        # truncated toy: positive tail is bounded in rational arithmetic.
        x=g.genuine_infinite_first_flux(16)
        lo,hi=x["full_infinite_source_flux_interval"]
        self.assertGreater(lo,-F(1,500))
        self.assertLess(hi,-F(1,1000))

    def test_original_source_true_one_direction_shorting_improvement(self):
        c=g.first_true_dual_gauge_resolvent_bound(16)
        self.assertGreater(c["source_flux_squared_rigorous_lower"],F(1,1000000))
        self.assertGreater(c["ungauged_true_high_variational_upper_strict"],
                           c["optimized_true_high_variational_upper_strict"])
        self.assertEqual(c["precise_high_metric"],"K=(-Delta_N)^-1_NOT_IDENTITY")
        self.assertTrue(c["one_original_source_low_direction_gauge_certified"])
        self.assertFalse(c["source_full_30_low_short_positive"])
        self.assertFalse(c["rh_proved"])

    def test_independent_mpmath_flux_holdout(self):
        try:import mpmath as mp
        except ImportError:self.skipTest("optional high-precision diagnostic")
        mp.mp.dps=75
        b=mp.log(2);w=b/mp.sqrt(2)
        C=mp.euler+mp.pi/2+3*b+mp.log(mp.pi)
        def integrand(t):
            return (1-2*t)*(-4*(mp.exp(t/2)+mp.exp(-t/2)-2)+C*t/2+
                   w*max(0,t-b)-
                   sum(4/mp.mpf(4*j+1)**2*(1-mp.exp(-mp.mpf(4*j+1)*t/2))
                       for j in range(16)))
        original=2*(mp.quad(integrand,[0,b])+mp.quad(integrand,[b,1]))
        box=g.finite_signed_first_flux(16)
        lo=mp.mpf(box.lo.numerator)/box.lo.denominator
        hi=mp.mpf(box.hi.numerator)/box.hi.denominator
        self.assertLessEqual(lo,original)
        self.assertGreaterEqual(hi,original)

    def test_false_half_density_or_float_clock_refused(self):
        for fn in (
            lambda:g.weighted_exponential(0.5),
            lambda:g.weighted_exponential(-129),
            lambda:g.finite_signed_first_flux(0),
            lambda:g.finite_signed_first_flux(65),
            lambda:g.genuine_infinite_first_flux(5.0),
        ):
            with self.assertRaises((g.SourceFluxError,)):fn()

if __name__=="__main__":
    unittest.main()
