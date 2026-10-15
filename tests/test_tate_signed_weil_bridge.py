"""Signed Tate/Weil numerical diagnostic with rigorous source-cutoff firewall.

The inherited compact_weil_tent has an analytic bound on its Archimedean
ladder remainder, not a fully certified mpmath quadrature. No sign
certificate is asserted by this test.
"""
import unittest
from fractions import Fraction as F

from observational_succ.tate_signed_weil_bridge import compare_signed_weil_tent


class SignedWeilSourceAdapterTests(unittest.TestCase):
    def test_true_prime_gamma_pole_vs_non_euler_mutant(self):
        try:
            import mpmath
        except ImportError:
            self.skipTest("mpmath research extra not installed")
        r=compare_signed_weil_tent(F(1),J=4,dps=35,fake6=1)
        self.assertTrue(r["genuine_source"])
        self.assertTrue(r["fake6_source_is_not_genuine"])
        self.assertNotIn(6,r["original_prime_support"])
        self.assertTrue(r["pole_Gamma_terms_retained"])
        self.assertEqual(r["half_density"],F(1,2))
        self.assertFalse(r["numeric_sign_proven_by_rigorous_interval"])
        self.assertFalse(r["full_distributional_identification_proved_here"])
        self.assertFalse(r["Weil_PSD_proved"])
        self.assertFalse(r["RH_proved"])

    def test_analytic_probe_domain_checks(self):
        for kw in ({"a":F(1,2)}, {"fake6":0}, {"J":0}, {"dps":20}):
            with self.assertRaises(ValueError):
                compare_signed_weil_tent(**kw)


if __name__=="__main__":
    unittest.main()
