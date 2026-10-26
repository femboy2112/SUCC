"""Tests for observational_succ.ladder_contraction_probe.

Only the forcing-agnostic ladder identity is a certificate (residual == 0 exactly);
lambda_N(h) is OBSERVED and asserted only to compute finitely.  The honest flags must
stay False (the contraction is UNVERIFIED / OPEN).
"""
import unittest
from fractions import Fraction as Q

from observational_succ import ladder_contraction_probe as lp


class LadderContractionProbe(unittest.TestCase):
    def test_identity_residual_exactly_zero(self):
        states = lp.authentic_states(48)
        resid = lp.ladder_identity_residual(states)
        self.assertEqual(len(resid), 47)
        self.assertTrue(all(r == Q(0) for r in resid))  # exact, forcing-agnostic

    def test_lambda_is_finite_observed(self):
        states = lp.authentic_states(64)
        for h in (1, 2, 3):
            lam = lp.ladder_ratio(states, h)
            self.assertIsInstance(lam, float)
            self.assertGreaterEqual(lam, 0.0)

    def test_honest_flags(self):
        self.assertFalse(lp.ladder_contraction_proved)   # UNVERIFIED / OPEN
        self.assertFalse(lp.pi_normality_proved)

    def test_report_states_open(self):
        txt = lp.report(N=32)
        self.assertIn("identity EXACT", txt)
        self.assertIn("UNVERIFIED", txt)
        self.assertIn("OPEN", txt)


if __name__ == "__main__":
    unittest.main()
