"""Exact real-place brackets, source mutations, and labelled diagnostics."""
import unittest
from fractions import Fraction as F
from observational_succ.diagonal_adele_zeta import DiagonalSourceError
from observational_succ.adelic_theta_completion import (
    atan_reciprocal_bracket,pi_machin_bracket,gamma_factor_at_even,
    completed_s2_interval,deleted_euler_factor_asymmetry,
    theta_poisson_diagnostic,lambda_theta_diagnostic,
)

class ArchimedeanCompletion(unittest.TestCase):
    def test_alternating_arctan_bounds(self):
        for terms in range(1,9):
            l,u=atan_reciprocal_bracket(5,terms)
            self.assertLess(l,u)
            self.assertGreater(l,F(0))

    def test_rational_pi_brackets_shrink(self):
        widths=[]
        for terms in range(2,10):
            lo,hi=pi_machin_bracket(terms)
            self.assertLess(lo,F(22,7))
            self.assertGreater(hi,F(333,106))
            widths.append(hi-lo)
        self.assertTrue(all(x>y for x,y in zip(widths,widths[1:])))

    def test_gaussian_arch_factor_normalization(self):
        self.assertEqual(gamma_factor_at_even(2)['coefficient'],1)
        self.assertEqual(gamma_factor_at_even(2)['pi_power'],-1)
        self.assertEqual(gamma_factor_at_even(6)['coefficient'],2)
        self.assertEqual(gamma_factor_at_even(6)['pi_power'],-3)
        with self.assertRaises(DiagonalSourceError):gamma_factor_at_even(3)

    def test_completed_lambda_2_is_an_interval(self):
        l=completed_s2_interval(13,8)
        self.assertLess(l['lambda_lower'],l['lambda_upper'])
        self.assertFalse(l['continuation_claimed'])
        self.assertFalse(l['RH_claimed'])
        # Classical Basel identity Lambda(2)=pi/6 is used only as holdout;
        # the finite interval is proved without importing Basel or FE.
        self.assertLess(l['lambda_lower'],l['pi_lower']/6)
        self.assertGreater(l['lambda_upper'],l['pi_upper']/6)

    def test_deleting_prime_factor_breaks_symmetric_completion(self):
        r=deleted_euler_factor_asymmetry(2,2)
        self.assertEqual(r['left_mutation'],F(3,4))
        self.assertEqual(r['dual_mutation'],-1)
        self.assertEqual(r['noncommuting_factor'],F(7,4))
        self.assertFalse(r['preserves_unmodified_completion'])
        with self.assertRaises(DiagonalSourceError):
            deleted_euler_factor_asymmetry(6,2)

    def test_theta_precision_diagnostic_properly_labeled(self):
        out=theta_poisson_diagnostic(t='2',terms=12,digits=40)
        self.assertFalse(out['formal_error_interval_provided'])
        self.assertFalse(out['analytic_identity_proved_by_code'])
        self.assertLess(float(out['absolute_truncation_residual']),1e-35)

    def test_completed_lambda_theta_matches_direct_at_examples(self):
        for s in ('2','-1','0.4+2.0j'):
            out=lambda_theta_diagnostic(s,terms=9,digits=48)
            self.assertTrue(out['numeric_diagnostic_not_proof'])
            self.assertLess(float(out['source_match_residual']),1e-35)
            self.assertLess(float(out['symmetry_residual']),1e-35)

    def test_pole_inputs_refused_as_function_values(self):
        for x in ('0','1'):
            with self.assertRaises(DiagonalSourceError):
                lambda_theta_diagnostic(x)

if __name__=='__main__':unittest.main()

class SelfDualNonuniqueArchimedean(unittest.TestCase):
    def test_normalized_r_two_preserves_residues_but_changes_completion(self):
        from observational_succ.adelic_theta_completion import normalized_self_dual_gaussian_pair
        for s in (-1,0,1,2):
            out=normalized_self_dual_gaussian_pair(F(2),s)
            self.assertEqual(out['mellin_relative_to_standard'],out['reflection_partner_relative'])
            self.assertEqual(out['pole_zero_normalization_C0'],1)
            self.assertEqual(out['pole_one_normalization_C1'],1)
            self.assertTrue(out['claimed_Fourier_self_dual'])
        self.assertEqual(normalized_self_dual_gaussian_pair(F(2),2)['mellin_relative_to_standard'],F(3,2))
        self.assertEqual(normalized_self_dual_gaussian_pair(F(2),-1)['mellin_relative_to_standard'],F(3,2))

    def test_standard_gaussian_is_only_r_one_member(self):
        from observational_succ.adelic_theta_completion import normalized_self_dual_gaussian_pair
        self.assertTrue(normalized_self_dual_gaussian_pair(F(1),2)['coincides_with_standard_mellin_at_s'])
        self.assertFalse(normalized_self_dual_gaussian_pair(F(3,2),2)['coincides_with_standard_mellin_at_s'])

    def test_nonpositive_scale_source_mutation_refused(self):
        from observational_succ.adelic_theta_completion import normalized_self_dual_gaussian_pair
        for r in (0,-1,F(-1,2)):
            with self.assertRaises(DiagonalSourceError):
                normalized_self_dual_gaussian_pair(r,2)

class ExplicitOffCriticalMutation(unittest.TestCase):
    def test_offcritical_zeros_from_positive_selfdual_source(self):
        from observational_succ.adelic_theta_completion import offcritical_self_dual_zero_witness
        x=offcritical_self_dual_zero_witness()
        self.assertEqual(x['discriminant'],F(21,25))
        self.assertEqual(x['t_quadratic_constant_first'],(F(1),F(11,5),F(1)))
        self.assertTrue(x['zeros_off_critical_line'])
        self.assertTrue(x['zeros_inside_open_critical_strip'])
        self.assertFalse(x['actual_riemann_zeta_changed'])

    def test_correct_pole_residue_and_source_symmetric_mellin(self):
        from observational_succ.adelic_theta_completion import centered_self_dual_gamma_multiplier
        for s in (-1,0,1,2):
            x=centered_self_dual_gamma_multiplier(F(4),F(11,10),s)
            self.assertEqual(x['C0'],1)
            self.assertEqual(x['C1'],1)
            self.assertEqual(x['relative_to_standard'],x['reflected_relative'])
            self.assertTrue(x['real_source_positive'])
            self.assertTrue(x['same_finite_euler_source'])
        self.assertNotEqual(centered_self_dual_gamma_multiplier(F(4),F(11,10),2)['relative_to_standard'],1)

    def test_negative_source_weight_not_allowed(self):
        from observational_succ.adelic_theta_completion import centered_self_dual_gamma_multiplier
        with self.assertRaises(DiagonalSourceError):
            centered_self_dual_gamma_multiplier(F(4),F(-1),2)
