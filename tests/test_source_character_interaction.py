"""Exact finite χ4 model/source/parity and signed analytic envelope regressions."""
import unittest
from fractions import Fraction as Q
from observational_succ.source_character_interaction import (
    character_four, gauss_sum_four, local_chi4_euler,
    chi4_pair_cancellation, signed_theta_tail, chi4_analytic_source_rules,
    character_receipt,
)
from observational_succ.source_model_interaction import SourceInteractionError


class CharacterAllPlaceTests(unittest.TestCase):
    def test_actual_chi4_source_signs(self):
        self.assertEqual([character_four(n) for n in range(17)],
                         [0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0])

    def test_character_completely_multiplicative_on_integer_controls(self):
        for a in range(-30,31):
            for b in range(-30,31):
                self.assertEqual(character_four(a*b),character_four(a)*character_four(b))

    def test_parity_requires_odd_theta_weight(self):
        for n in range(1,40):
            x=chi4_pair_cancellation(n)
            self.assertEqual(x['unweighted_pair_sum'],0)
            self.assertEqual(x['odd_weighted_pair_sum'],2*n*character_four(n))
        self.assertTrue(chi4_pair_cancellation(1)['unweighted_global_signed_theta_identically_zero'])

    def test_gauss_sum_source_root_one_exact(self):
        x=gauss_sum_four()
        self.assertEqual((x['gauss_sum_real'],x['gauss_sum_imag']),(0,2))
        self.assertEqual(x['normalized_root_number'],'1')
        self.assertEqual(x['parity'],'odd')

    def test_true_odd_prime_local_character_factor(self):
        for p in (3,5,7,11,13,17):
            for s in (1,2,3):
                x=local_chi4_euler(p,s,4)
                self.assertEqual(Q(x['partial'])+Q(x['tail']),Q(x['full']))
                self.assertEqual(Q(x['full']),Q(p**s,p**s-character_four(p)))
        self.assertEqual(Q(local_chi4_euler(2,2,4)['full']),1)

    def test_sign_oscillation_must_not_be_sold_as_positive_mass(self):
        a=local_chi4_euler(3,1,4)
        self.assertTrue(a['signed_tail_not_a_positive_measure'])
        b=local_chi4_euler(5,1,4)
        self.assertFalse(b['signed_tail_not_a_positive_measure'])

    def test_local_euler_odd_parity_negative_control(self):
        with self.assertRaises(SourceInteractionError):
            local_chi4_euler(6,2,3)
        with self.assertRaises(SourceInteractionError):
            local_chi4_euler(9,2,3)

    def test_character_tail_shrinks_with_modes_and_integration_horizon(self):
        for r in range(3):
            a=Q(signed_theta_tail(-2,3,2,6,r)['rational_upper'])
            b=Q(signed_theta_tail(-2,3,4,18,r)['rational_upper'])
            self.assertTrue(0<b<a)

    def test_uniform_vertical_strip_has_odd_source_power(self):
        x=signed_theta_tail(-4,5,4,14)
        self.assertEqual(x['power_envelope'],2)
        self.assertTrue(x['uniform_all_imaginary_ordinates'])
        self.assertFalse(x['not_a_finite_interval_quadrature_certificate'] is False)

    def test_global_dirichlet_beta_symmetry_requires_parity_and_conductor(self):
        x=chi4_analytic_source_rules()
        self.assertIn('Gamma((s+1)/2)',x['one_real_place_gamma'])
        self.assertIn('t^(-3/2)',x['theta_modular'])
        self.assertEqual(x['beta_at_zero'],'1/2')
        self.assertTrue(x['negative_odd_trivial_zeros_simple'])
        self.assertFalse(x['GRH_proved'])

    def test_prime_sphere_catalan_bridge_exact_symbolic(self):
        x=chi4_analytic_source_rules()
        self.assertEqual(x['first_trivial_zero_derivative'], 'beta_prime(-1)=2*beta(2)/pi')
        self.assertIn('4*beta(2)',x['bridge_to_PR68_chiral_diagonal'])

    def test_source_receipt_deterministic_and_nonRH(self):
        self.assertEqual(character_receipt(),character_receipt())
        self.assertFalse(character_receipt()['original_zeta_RH_proved'])
        self.assertFalse(character_receipt()['generalized_RH_proved'])


if __name__=='__main__':
    unittest.main()
