"""Authentic zeta first-window source HIGH range and conditional residual cost."""
import unittest
from fractions import Fraction as F
from observational_succ import one_object_source_residual as s

class AuthenticSourceResidualTests(unittest.TestCase):
    def test_source_pinned_original_first_window_and_proven_range(self):
        data=s.authenticated_first_window_gate()
        self.assertEqual(data["radius"],F(1,2))
        self.assertEqual(data["low_legendre_modes"],30)
        self.assertEqual(data["reflection_parity_blocks"],(15,15))
        self.assertEqual(data["kappa"],F(369,10000))
        self.assertEqual(data["high_gap_relative_to"],
                         "Q_K_Neumann_Q_NOT_IDENTITY")
        self.assertTrue(data["zero_shift_cross_resolvent_finite"])
        self.assertFalse(data["finite_candidate_galerkin_residual_derived"])
        self.assertFalse(data["low_signed_schur_positivity_proved"])
        self.assertFalse(data["global_Connes_adelic_trace_identified"])
        self.assertFalse(data["rh_proved"])

    def test_true_source_gamma_remainder_and_spectrum_firewall(self):
        for J in (1,3,10,64,128):
            c=s.genuine_gamma_residual_tail(J)
            tau=F(1,4*J+1)+F(4,(4*J+1)**2)
            self.assertEqual(c["gamma_cross_H1_error_bound"],963*tau)
            self.assertTrue(c["gamma_source_is_original"])
            self.assertFalse(c["derivative_Gram_from_full_original_G_source_verified"])

    def test_conditional_residual_mathematics_has_explicit_normalization(self):
        T=((F(1),F()),(F(),F(2)))
        Y=((F(1),F()),(F(),F(1)),(F(1,3),F(2,3)))
        data=s.conditional_original_residual_gram(T,Y,J=12,eta=F(1))
        delta=data["H1_gamma_tail_gain"]
        Iplus=((F(1)+F(1)+F(1,9),F(2,9)),
               (F(2,9),F(1)+F(1)+F(4,9)))
        want=tuple(tuple(2*T[i][j]+2*delta**2*Iplus[i][j]
                         for j in range(2)) for i in range(2))
        self.assertEqual(data["conditional_residual_derivative_Gram_upper"],want)
        self.assertTrue(data["requires_independent_original_finiteJ_derivative_Gram_authentication"])
        self.assertTrue(data["requires_independent_original_low_high_response_basis_authentication"])
        self.assertFalse(data["actual_T_J_verified"])
        self.assertFalse(data["actual_Y_verified"])
        self.assertFalse(data["authentic_signed_low_A_minus_short_R0_positive_proved"])
        self.assertFalse(data["all_radii_RH_proved"])

    def test_advanced_positive_gamma_tail_shrinks_without_claiming_sign(self):
        T=((F(1),),)
        Y=((F(),),(F(),))
        low=s.conditional_original_residual_gram(T,Y,2,F(1))
        high=s.conditional_original_residual_gram(T,Y,16,F(1))
        self.assertGreater(low["H1_gamma_tail_gain"],high["H1_gamma_tail_gain"])
        self.assertGreater(low["conditional_residual_derivative_Gram_upper"][0][0],
                           high["conditional_residual_derivative_Gram_upper"][0][0])
        self.assertFalse(high["authentic_signed_low_A_minus_short_R0_positive_proved"])


    def test_original_gamma_ladder_outpaces_any_finite_response_cost(self):
        for M in (F(),F(1,10),F(1),F(10),F(1000)):
            for eps in (F(20),F(1),F(1,10)):
                x=s.adaptive_gamma_response_schedule(M,eps)
                self.assertGreaterEqual(x["sufficient_finite_original_gamma_modes"],1)
                self.assertLess(x["joint_response_gamma_error_upper"],eps)
                self.assertTrue(x["strictly_below_target"])
                self.assertFalse(x["actual_gamma_stage_built"])
                self.assertFalse(x["original_high_response_norm_source_authenticated"])
                self.assertFalse(x["true_residual_derivative_Gram_sign_evaluated"])

    def test_gamma_zeno_schedule_refuses_unbounded_or_fake_cost(self):
        for fn in (
            lambda:s.adaptive_gamma_response_schedule(-1,1),
            lambda:s.adaptive_gamma_response_schedule(0,0),
            lambda:s.adaptive_gamma_response_schedule(0.5,F(1)),
            lambda:s.adaptive_gamma_response_schedule(F(1),1e-100),
            lambda:s.adaptive_gamma_response_schedule(F(100000000),F(1,1000000)),
        ):
            with self.assertRaises(s.ResidualSourceError):fn()

    def test_conditional_source_gram_type_and_math_validity(self):
        for fn in (
            lambda:s.conditional_original_residual_gram(((F(-1),),),
                           ((F(1),),),2,F(1)),
            lambda:s.conditional_original_residual_gram(((F(1),),),
                           ((F(1),),),0,F(1)),
            lambda:s.conditional_original_residual_gram(((F(1),),),
                           ((F(1),),),2,F(0)),
            lambda:s.conditional_original_residual_gram(((F(1),),),
                           ((F(1),),),2,0.1),
            lambda:s.conditional_original_residual_gram(((F(1),),),
                           ((F(1),F(1)),),2,F(1)),
        ):
            with self.assertRaises((s.ResidualSourceError,)):fn()

if __name__=="__main__":
    unittest.main()
