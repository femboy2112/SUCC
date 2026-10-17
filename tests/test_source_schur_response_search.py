"""Source-chosen finite high responses are inputs, not positivity certificates."""
import unittest
from fractions import Fraction as F
from observational_succ.source_schur_response_search import (
    SourceResponseSearchError,original_source_rational_response,
    source_response_analytic_trial,
)


class GenuineTrialOptimizer(unittest.TestCase):
    def test_original_source_candidate_parity_rational_and_no_sign_promotion(self):
        c=original_source_rational_response(rank=6,J=64,denominator=10000)
        self.assertTrue(c["original_source_verified"])
        self.assertFalse(c["U_has_original_S4_sign_certificate"])
        self.assertFalse(c["RH_proved"])
        self.assertTrue(any(x for row in c["U"] for x in row))
        for i,row in enumerate(c["U"]):
            for j,x in enumerate(row):
                self.assertEqual((x*10000).denominator,1)
                if (i+4-j)%2:self.assertEqual(x,0)

    def test_invalid_optimizer_source_contract_rejects(self):
        for bad in (True,4,9):
            with self.assertRaises(SourceResponseSearchError):
                original_source_rational_response(rank=bad)
        with self.assertRaises(SourceResponseSearchError):
            original_source_rational_response(rank=6,J=2)

    def test_true_source_recertification_remains_scoped(self):
        report=source_response_analytic_trial(rank=6,J_source=64,J_deriv=2)
        self.assertTrue(report["genuine_S4_source_audited"])
        self.assertIn(report["genuine_first_window_verdict"],
                      ("AMBIGUOUS","POSITIVE_CERTIFIED"))
        self.assertFalse(report["RH_proved"])


if __name__=="__main__":unittest.main()
