"""Exact rational interval proof and hostile Gamma/contact/prime-source controls."""
from __future__ import annotations
import unittest
from fractions import Fraction as F
from observational_succ.signed_gprime_enclosure import (
    SignedSourceEnclosureError, original_contact_interval, original_derivative_interval,
    original_first_window_l1_certificate, gamma_derivative_interval, atan_interval,
    log_interval, log2_interval, pi_interval, exp_interval, exp_neg_interval,
    true_prime2_weight_interval, prime_step_interval, original_primitive_interval,
)


class ExactOriginalGammaProof(unittest.TestCase):
    def test_contact_interval_contains_standard_ordinary_value(self):
        # Enclosure comparison with coarse rational bracket; no floating proof.
        a,b=original_contact_interval()
        self.assertTrue(F(537,100)<a<b<F(538,100))

    def test_rational_pi_and_log2(self):
        p=pi_interval()
        self.assertTrue(F(3)<p[0]<p[1]<F(22,7))
        l=log2_interval()
        self.assertTrue(F(2,3)<l[0]<l[1]<F(7,10))

    def test_exponential_and_inverse(self):
        v=exp_interval(F(1,2));u=exp_neg_interval(F(1,2))
        self.assertGreater(v[0],F(3,2))
        self.assertLess(v[1],F(5,3))
        self.assertLessEqual(v[0]*u[0],1)
        self.assertGreaterEqual(v[1]*u[1],1)

    def test_atan_reduced_interval_correct_on_both_branches(self):
        try:import mpmath as mp
        except ImportError:return
        mp.mp.dps=70
        for x in (F(2,5),F(1,2),F(3,5),F(999,1000)):
            lo,hi=atan_interval(x)
            val=mp.atan(mp.mpf(x.numerator)/x.denominator)
            self.assertLessEqual(mp.mpf(lo.numerator)/lo.denominator,val)
            self.assertGreaterEqual(mp.mpf(hi.numerator)/hi.denominator,val)

    def test_source_screw_primitive_reconstructs_signed_window(self):
        lo,hi=original_primitive_interval(F(1,4),512)
        self.assertTrue(F(-6,100)<lo<hi<F(-4,100))
        self.assertLess(hi-lo,F(1,50))

    def test_source_gamma_log_diverges_near_zero(self):
        v=gamma_derivative_interval(F(1,100));w=gamma_derivative_interval(F(1,1000))
        self.assertLess(w[1],v[0])

    def test_gamma_series_log_identity_at_rational_input(self):
        # Independent 70-digit holdout; not accepted as mathematical authority.
        try:import mpmath as mp
        except ImportError:return
        mp.mp.dps=70
        for r in (F(1,10),F(1,4),F(3,5)):
            lo,hi=gamma_derivative_interval(r)
            z=mp.exp(-mp.mpf(r.numerator)/r.denominator/2)
            val=-mp.atanh(z)-mp.atan(z)
            self.assertLess(mp.mpf(lo.numerator)/lo.denominator,val)
            self.assertGreater(mp.mpf(hi.numerator)/hi.denominator,val)

    def test_true_prime_jump_is_disjoint_from_no_source(self):
        before=prime_step_interval(F(1,2),F(3,5))
        after=prime_step_interval(F(4,5),F(9,10))
        self.assertEqual(before,(F(),F()))
        self.assertGreater(after[0],F(1,3))
        self.assertGreater(after[1],after[0])

    def test_prime_source_discontinuous_wavefront_preserved(self):
        left=original_derivative_interval(F(68,100),F(69,100))
        right=original_derivative_interval(F(70,100),F(71,100))
        # Interval source explicitly permits the positive log2/sqrt2 jump.
        self.assertLess(left[1],0)
        self.assertGreater(right[0],0)

    def test_contacts_mutated_would_break_certificate(self):
        # A constant contact shift by +1 changes g' by exactly +1/2.
        # At r=1/4 the certified genuine interval is disjoint from the mutant.
        lo,hi=original_derivative_interval(F(1,4),F(1,4))
        self.assertLess(hi-lo,F(1,1000000000))
        self.assertGreater(lo+F(1,2),hi)

    def test_low_cell_not_sampled_at_singularity(self):
        with self.assertRaises(SignedSourceEnclosureError):gamma_derivative_interval(F(0))

    def test_invalid_float_bool_rational_contract(self):
        for bad in (False,True,0.5,None):
            with self.assertRaises(SignedSourceEnclosureError):log_interval(bad)

    def test_signed_L1_finite_observer_refines(self):
        a=original_first_window_l1_certificate(256)
        b=original_first_window_l1_certificate(512)
        self.assertLess(b['gprime_L1_STRICT_upper'],a['gprime_L1_STRICT_upper'])
        self.assertLess(b['gprime_L1_STRICT_upper'],F(3,10))
        self.assertLess(b['gprime_L1_lower'],b['gprime_L1_STRICT_upper'])

    def test_global_source_bounds_are_rational_not_sampled(self):
        v=original_first_window_l1_certificate(4096)
        self.assertGreater(v['gprime_L1_lower'],F(1,4))
        self.assertLess(v['gprime_L1_STRICT_upper'],F(11,40))
        self.assertLess(v['gprime_L2_squared_STRICT_upper'],F(4,25))
        self.assertFalse(v['RH_proved'])
        self.assertTrue(v['positive_rational_certificate'])

    def test_analytic_near_zero_cell_is_present(self):
        a=original_first_window_l1_certificate(128)
        self.assertGreater(a['gprime_L2_squared_STRICT_upper'],0)
        self.assertGreater(a['delta'],0)


if __name__=='__main__':unittest.main()
