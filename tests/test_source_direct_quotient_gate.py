"""Authenticated source smoke test, executed only in the complete SUCC checkout."""
import unittest
from fractions import Fraction as F
from observational_succ.source_direct_quotient_gate import CertifiedSourceDirectQuotientTrial


class OriginalSourceIntegration(unittest.TestCase):
    def test_original_first_window_tiny_stress(self):
        # Exact-head CI checks the imported original Suzuki/Gamma contract.
        r=CertifiedSourceDirectQuotientTrial(J_deriv=1,grid=4,J_galerkin=64,
                                            rank=5,eta=F(1,4))
        self.assertTrue(r['source_gate_passed'])
        self.assertFalse(r['RH_proved'])
        self.assertIn(r['verdict'],('AMBIGUOUS','POSITIVE_CERTIFIED'))
        self.assertEqual(len(r['quotient_loewner_upper']),4)

    def test_invalid_analytic_parameter_not_upgraded_to_source(self):
        r=CertifiedSourceDirectQuotientTrial(J_deriv=0, grid=4, rank=5)
        self.assertEqual(r['verdict'],'INVALID_SOURCE')
        self.assertFalse(r['RH_proved'])


if __name__=='__main__':
    unittest.main()
