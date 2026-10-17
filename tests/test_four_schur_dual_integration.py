"""Source-gated CertifiedTrial dual alternative; test within actual SUCC checkout.

The parent #149 implements original-source gating; this suite checks that the
new rigorous trial-dependent lower bracket has the asserted exact formula and
cannot silently replace a stronger inherited lower bound.
"""
import unittest
from fractions import Fraction as F

from observational_succ.certified_four_schur_trial import (
    CertifiedTrial, ZERO_SHIFT_CAP, _trial_matrix_V, _L2_gram_of_trial,
)


def mat(x):
    return tuple(tuple(F(v) for v in row) for row in x)


class SourceDualIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zero = CertifiedTrial(U=(), J=3, rank=6)
        cls.nonzero = CertifiedTrial(
            U=((F(1,20),0,0,0),(0,F(1,10),0,0)),J=3,rank=6)

    def test_source_active(self):
        for res in (self.zero,self.nonzero):
            self.assertTrue(res['source_dual_U_certified'])
            self.assertFalse(res['RH_proved'])
            self.assertIn(res['verdict'],('AMBIGUOUS','POSITIVE_CERTIFIED','NEGATIVE_CERTIFIED'))

    def test_U0_same_old_lower(self):
        self.assertEqual(mat(self.zero['source_dual_U_lower_bracket']),
                         mat(self.zero['lower_bracket']))

    def test_nonzero_exact_rational_source_dual_formula(self):
        res=self.nonzero
        U=((F(1,20),0,0,0),(0,F(1,10),0,0))
        W=_L2_gram_of_trial(_trial_matrix_V(U,6),6)
        e=F(res['interval_loewner_radius_GJ'])
        E=mat(res['source_trial_energy_midpoint'])
        want=tuple(tuple(E[i][j]-(e if i==j else 0)-ZERO_SHIFT_CAP*W[i][j]
                             for j in range(4)) for i in range(4))
        self.assertEqual(mat(res['source_dual_U_lower_bracket']),want)

    def test_precision_gate_does_not_launder_requested_as_certified(self):
        for p in (F(1),F(1,10**20)):
            res=CertifiedTrial(U=(),J=3,rank=6,precision=p)
            width=F(res['source_trial_energy_width_operator_upper'])
            self.assertEqual(res['requested_precision_met_for_trial_energy'],width<=p)
        tight=CertifiedTrial(U=(),J=3,rank=6,precision=F(1,10**20))
        self.assertFalse(tight['requested_precision_met_for_trial_energy'])
        loose=CertifiedTrial(U=(),J=3,rank=6,precision=F(100))
        self.assertTrue(loose['requested_precision_met_for_trial_energy'])

    def test_bad_precision_rejected(self):
        for p in (F(0),F(-1),0.0001,True):
            self.assertEqual(CertifiedTrial(U=(),J=3,rank=6,precision=p)['verdict'],
                             'INVALID_SOURCE')

    def test_no_projected_derivative_shortcut(self):
        self.assertTrue(self.nonzero['source_dual_U_uses_unprojected_derivative_pairing'])
        self.assertFalse(self.nonzero['source_dual_U_has_authenticated_moments'])

if __name__=='__main__':unittest.main()
