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

    def test_authentic_boundary_moment_loewner_formula(self):
        # The new source-attested moment correction is an *additional* 
        # rigorous lower, NEVER a mathematical maximum of unrelated matrices.
        for out in (self.zero,self.nonzero):
            low=mat(out['source_dual_U_lower_bracket'])
            boost=mat(out['source_dual_boundary_moment_lower'])
            actual=mat(out['source_dual_boundary_lower_bracket'])
            for i in range(4):
                for j in range(4):
                    self.assertEqual(actual[i][j],low[i][j]+50*boost[i][j])
                    self.assertEqual(actual[i][j],actual[j][i])
            self.assertTrue(out['source_dual_U_has_authenticated_moments'])
            self.assertFalse(out['RH_proved'])

    def test_true_source_moment_interval_geometry(self):
        # Two rows 4-column exact intervals, no source oracle supplied by caller.
        out=self.nonzero
        mids=mat(out['source_dual_boundary_rows_mid'])
        err=mat(out['source_dual_boundary_rows_error'])
        self.assertEqual(len(mids),2)
        self.assertEqual(len(mids[0]),4)
        self.assertTrue(all(x>=0 for row in err for x in row))
        # Original G parity: first P1 row odd input only, P2 row even only.
        for i in (1,3):self.assertEqual(mids[0][i],0)
        for i in (0,2):self.assertEqual(mids[1][i],0)

    def test_no_projected_derivative_shortcut(self):
        self.assertTrue(self.nonzero['source_dual_U_uses_unprojected_derivative_pairing'])
        self.assertTrue(self.nonzero['source_dual_U_has_authenticated_moments'])
        self.assertIn('TWO endpoint-vanishing', 
                      self.nonzero['source_dual_U_authenticated_moment_scope'])

    def test_complete_four_moment_and_parity_kappa_brackets(self):
        for out in (self.zero, self.nonzero):
            E_mid = mat(out['source_full_four_moment_E_mid'])
            E_err = mat(out['source_full_four_moment_E_error'])
            self.assertEqual(len(E_mid), 4)
            self.assertEqual(len(E_mid[0]), 4)
            # Parity structure of E_{j,i} = int t^j h_i'(t) dt:
            for j in range(4):
                for i in range(4):
                    if (j - i) % 2:
                        self.assertEqual(E_mid[j][i], F(0))
                        self.assertEqual(E_err[j][i], F(0))
                    else:
                        self.assertGreater(E_err[j][i], F(0))
            low = mat(out['source_dual_U_lower_bracket'])
            full_mom = mat(out['source_full_four_moment_lower'])
            four_br = mat(out['source_dual_four_moment_lower_bracket'])
            for i in range(4):
                for j in range(4):
                    self.assertEqual(four_br[i][j], low[i][j] + 50 * full_mom[i][j])
            self.assertEqual(out['parity_kappa_lower']['odd'], '63/500')
            self.assertEqual(out['parity_kappa_lower']['even'], '153/500')
            pk_eig = out['source_dual_parity_kappa_min_eig_lower_by_parity']
            lo_eig = out['lower_bracket_min_eig_lower_by_parity']
            self.assertGreater(F(pk_eig['odd']), F(lo_eig['odd']))
            self.assertGreater(F(pk_eig['even']), F(lo_eig['even']))

    def test_certified_derivative_energy_trial_b1_b3(self):
        from observational_succ.certified_four_schur_trial import CertifiedDerivativeEnergyTrial
        res = CertifiedDerivativeEnergyTrial(U=(), J_deriv=3, grid=8, J_galerkin=3, rank=6)
        self.assertEqual(res['verdict'], 'AMBIGUOUS')
        self.assertFalse(res['RH_proved'])
        ibp_tails = tuple(F(x) for x in res['gamma_tail_ibp_O_J_minus_3_2'])
        yng_tails = tuple(F(x) for x in res['gamma_tail_young_O_J_minus_1'])
        for i in range(4):
            self.assertGreater(ibp_tails[i], F(0))
            self.assertGreater(yng_tails[i], F(0))
        pk_eig = res['certified_Hprime_parity_kappa_min_eig_lower_by_parity']
        k50_eig = res['certified_Hprime_kappa50_min_eig_lower_by_parity']
        self.assertGreater(F(pk_eig['odd']), F(k50_eig['odd']))
        self.assertGreater(F(pk_eig['even']), F(k50_eig['even']))

    def test_30_to_4_middle_block_obstruction(self):
        from observational_succ.four_thirty_schur_transport import (
            source_30mode_middle_block_obstruction_certificate,
        )
        obs = source_30mode_middle_block_obstruction_certificate(J=4)
        self.assertTrue(obs['middle_block_5_to_30_strictly_negative_definite'])
        self.assertFalse(obs['monotone_nested_short_hypothesis_satisfied'])
        self.assertEqual(obs['universal_middle_loewner_upper_factor_moment30'], -F(26191, 14760))
        self.assertEqual(obs['universal_middle_loewner_upper_factor_fourier30'], -F(187, 200))
        self.assertFalse(obs['RH_proved'])


if __name__=='__main__':unittest.main()

