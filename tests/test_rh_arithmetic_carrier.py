"""Exact finite falsification controls for the Lagarias arithmetic RH carrier."""
import unittest
from fractions import Fraction as F

from observational_succ.rh_arithmetic_carrier import (
    ArithmeticCarrierError, divisor_sum, harmonic_number,
    lagarias_source_inequality, low_carrier_prefix_receipt
)
from observational_succ.source_weil_hierarchy import exp_pos, log_iv, iv


class LagariasCarrierTests(unittest.TestCase):
    def test_harmonic_and_sigma_from_independent_divisor_oracle(self):
        self.assertEqual(harmonic_number(1),F(1))
        self.assertEqual(harmonic_number(6),F(49,20))
        self.assertEqual(divisor_sum(6),12)
        self.assertEqual(divisor_sum(12),28)
        for n in range(1,129):
            independent=sum(d for d in range(1,n+1) if n%d==0)
            self.assertEqual(divisor_sum(n),independent)

    def test_true_source_intervals_n1_equality(self):
        r=lagarias_source_inequality(1)
        self.assertEqual(r["inequality_rhs_rational_interval"],(F(1),F(1)))
        self.assertEqual(r["status"],"FINITE_CERTIFIED_HOLDS")
        self.assertTrue(r["only_equality_at_n1_in_classical_statement"])
        self.assertFalse(r["universal_all_n_verified"])

    def test_sampled_lagarias_strict_not_universal(self):
        for n in (2,3,4,5,6,8,9,10,12,24,36,48,60):
            r=lagarias_source_inequality(n)
            self.assertTrue(r["actual_source"])
            self.assertEqual(r["status"],"FINITE_CERTIFIED_HOLDS")
            self.assertLess(r["true_sigma"],r["inequality_rhs_rational_interval"][0])
            self.assertFalse(r["RH_proved"])

    def test_counterfeit_sigma_violation_cannot_refute_RH(self):
        fake=lagarias_source_inequality(6,counterfeit_sigma_increment=100)
        self.assertEqual(fake["status"],"FINITE_CERTIFIED_VIOLATION")
        self.assertFalse(fake["actual_source"])
        self.assertEqual(fake["delta_fake"],100)
        authentic=lagarias_source_inequality(6)
        self.assertEqual(authentic["status"],"FINITE_CERTIFIED_HOLDS")

    def test_positive_prefix_is_not_global_proof(self):
        r=low_carrier_prefix_receipt(25)
        self.assertEqual(r["checked"],25)
        self.assertEqual(r["first_unchecked_integer"],26)
        self.assertTrue(r["all_checked_finite_inequalities_certified"])
        self.assertEqual(r["global_RH_classification_from_prefix"],"UNRESOLVED")
        self.assertFalse(r["RH_proved"])

    def test_typed_guard_against_float_fake_negative_and_nzero(self):
        for n in (0,129,-3,True,1.5):
            with self.assertRaises(ArithmeticCarrierError):
                lagarias_source_inequality(n)
        with self.assertRaises(ArithmeticCarrierError):
            lagarias_source_inequality(6,counterfeit_sigma_increment=-1)
        with self.assertRaises(ArithmeticCarrierError):
            lagarias_source_inequality(6,counterfeit_sigma_increment=F(1,2))


if __name__=="__main__":
    unittest.main()
