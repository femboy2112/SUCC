"""Exact source-typed and hostile tests for Tate-Mellin SUCC×prime-FUCC."""
import unittest
from fractions import Fraction as F
from math import factorial

from observational_succ.tate_mellin_prime_transport import (
    TateMellinSourceError,exp_taylor_lower,primes_upto,
    dirac_probability_band_certificate,prime_euler_certificate,
    completed_mellin_band_certificate,finite_prime_coefficients,
    mutant_source_discriminator,prime_escape_certificate,
    archimedean_parity_and_pole_firewall,
    finite_completed_characteristic,completed_characteristic_oracle,
)


class ExactRealPlaceTransport(unittest.TestCase):
    def test_baseline_taylor_exact_integer(self):
        self.assertEqual(exp_taylor_lower(F(1),3), F(8,3))
        self.assertGreater(exp_taylor_lower(F(4),16), F(50))
        self.assertLess(exp_taylor_lower(F(4),16), F(55))

    def test_exact_rational_dirac_envelope(self):
        c=dirac_probability_band_certificate(0,F(1,120),-840,840,F(2))
        self.assertLess(c['uniform_normalized_gamma_error_upper'],F(1,10))
        self.assertGreater(c['lower_normalization_relative_to_n_factorial'],F(9,10))
        self.assertEqual(c['source_event_count'],1681)
        self.assertEqual(c['sigma'],2)
        self.assertFalse(c['numerically_evaluated_source_weights_certified'])

    def test_moving_anchor_moments(self):
        for n in (0,1,2,3):
            c=dirac_probability_band_certificate(n,F(1,300),-2400,2400,F(2))
            self.assertGreater(c['lower_normalization_relative_to_n_factorial'],0)
            self.assertLess(c['uniform_normalized_gamma_error_upper'],F(1,4))

    def test_dirac_missing_left_right_rejected(self):
        for l,r,step in ((0,80,F(1,40)),(-80,0,F(1,40)),
                          (-40,40,F(1,40)),(-100,100,F(1))):
            with self.assertRaises(TateMellinSourceError):
                dirac_probability_band_certificate(2,step,l,r,2)

    def test_dirac_bad_source_inputs_rejected(self):
        for step in (0,-1,F(-1,12),True,0.01):
            with self.assertRaises(TateMellinSourceError):
                dirac_probability_band_certificate(0,step,-10,10,1)
        with self.assertRaises(TateMellinSourceError):
            dirac_probability_band_certificate(0,F(1,10),-30,30,F(-1))

    def test_bands_nested(self):
        small=dirac_probability_band_certificate(0,F(1,120),-840,840,F(1))
        large=dirac_probability_band_certificate(0,F(1,120),-840,840,F(5))
        self.assertLess(small['uniform_normalized_gamma_error_upper'],
                        large['uniform_normalized_gamma_error_upper'])


class AuthenticPrimeSource(unittest.TestCase):
    def test_prime_jet_labels_source_authentic(self):
        self.assertEqual(primes_upto(20),(2,3,5,7,11,13,17,19))
        self.assertNotIn(6,primes_upto(97))
        c=prime_euler_certificate(47,5,2)
        self.assertEqual(c['prime_labels'][0],2)
        self.assertNotIn(6,c['prime_labels'])
        self.assertEqual(c['omitted_prime_tail_upper'],F(2,47))
        self.assertGreater(c['uniform_euler_characteristic_error_upper'],0)

    def test_prime_tail_decreases_in_cutoff(self):
        c1=prime_euler_certificate(11,2,2)
        c2=prime_euler_certificate(47,2,2)
        self.assertLess(c2['omitted_prime_tail_upper'],c1['omitted_prime_tail_upper'])
        self.assertGreater(c2['finite_prime_power_truncation_upper'],
                           c1['finite_prime_power_truncation_upper'])
        finer=prime_euler_certificate(47,6,2)
        self.assertLess(finer['uniform_euler_characteristic_error_upper'],
                        c2['uniform_euler_characteristic_error_upper'])

    def test_arithmetic_dirichlet_coefficients_unit(self):
        true=finite_prime_coefficients(5,2)
        self.assertTrue(true['authentic_prime_labels'])
        self.assertEqual(true['coefficients'][2*3*5],1)
        self.assertEqual(true['coefficients'][2**2 * 3**2],1)
        self.assertTrue(all(v==1 for v in true['coefficients'].values()))

    def test_fake_six_and_wrong_alpha_exact_mutation(self):
        diag=mutant_source_discriminator(3,2)
        self.assertEqual(diag['fake_six_first_difference'],6)
        self.assertEqual(diag['fake_six_true_coefficient_at_6'],1)
        self.assertEqual(diag['fake_six_mutant_coefficient_at_6'],2)
        self.assertEqual(diag['changed_two_first_difference'],2)
        self.assertEqual(diag['changed_two_mutant_coefficient_at_2'],F(3,2))
        self.assertTrue(diag['fake_sources_still_positive'])
        self.assertTrue(diag['positivity_does_not_authenticate_Euler'])

    def test_prime_euler_rejects_unjustified_sources(self):
        for sigma in (1,0,-1,True,2.0):
            with self.assertRaises(TateMellinSourceError):
                prime_euler_certificate(47,2,sigma)
        for cutoff in (0,1,3.4,True):
            with self.assertRaises(TateMellinSourceError):
                prime_euler_certificate(cutoff,2,2)
        with self.assertRaises(TateMellinSourceError):
            finite_prime_coefficients(3,2,fake_six=1)

    def test_escaped_positive_euler_source(self):
        prev=None
        for P in (11,31,97,251):
            c=prime_escape_certificate(P,5)
            self.assertTrue(0<c['all_sigma_in_open_0_to_1_untruncated_mass_upper']<=1)
            self.assertTrue(0<c['all_sigma_in_open_0_to_1_finite_geometric_mass_upper']<=1)
            if prev:
                self.assertLess(c['all_sigma_in_open_0_to_1_untruncated_mass_upper'],
                                prev['all_sigma_in_open_0_to_1_untruncated_mass_upper'])
                self.assertLess(c['all_sigma_in_open_0_to_1_finite_geometric_mass_upper'],
                                prev['all_sigma_in_open_0_to_1_finite_geometric_mass_upper'])
            prev=c
        self.assertFalse(prev['weak_limit_probability_on_finite_log_carrier'])

    def test_escape_threshold_bounds(self):
        a=prime_escape_certificate(47,3)
        b=prime_escape_certificate(47,11)
        self.assertLess(a['all_sigma_in_open_0_to_1_untruncated_mass_upper'],
                        b['all_sigma_in_open_0_to_1_untruncated_mass_upper'])


class CompletedPositiveSourceInterface(unittest.TestCase):
    @staticmethod
    def params():
        return dict(n=0,mesh=F(1,120),left=-840,right=840,
                    height=F(2),prime_cutoff=97,
                    prime_power_cutoff=5,beta_cutoff=500)

    def test_certified_composite_bounds_are_rational(self):
        c=completed_mellin_band_certificate(**self.params())
        keys=('dirac_gamma_error','beta_gamma_error','euler_prime_error',
              'dirac_vs_beta_uniform_error_upper',
              'completed_dirac_error_upper','completed_beta_error_upper')
        self.assertTrue(all(isinstance(c[k],F) for k in keys))
        self.assertLess(c['completed_dirac_error_upper'],F(1,8))
        self.assertLess(c['completed_beta_error_upper'],F(1,15))
        self.assertFalse(c['signed_Weil_sign_identified'])
        self.assertFalse(c['RH_proved'])

    def test_triangle_bounds_for_genuine_sources(self):
        c=completed_mellin_band_certificate(**self.params())
        self.assertEqual(c['completed_dirac_error_upper'],
                         c['dirac_gamma_error']+c['euler_prime_error'])
        self.assertEqual(c['completed_beta_error_upper'],
                         c['beta_gamma_error']+c['euler_prime_error'])
        self.assertEqual(c['dirac_vs_beta_uniform_error_upper'],
                         c['dirac_gamma_error']+c['beta_gamma_error'])

    def test_completed_pole_and_parity_guard(self):
        c=archimedean_parity_and_pole_firewall(2)
        self.assertEqual(c['even_pi_scaled_second_moment'],3)
        self.assertEqual(c['odd_pi_scaled_second_moment'],F(7,2))
        self.assertEqual(c['wrong_2pi_scaled_second_moment'],F(3,2))
        self.assertEqual(c['xi_scalar_pole_removal_at_sigma2_t1_modulus_squared'],10)
        self.assertFalse(c['xi_scalar_is_itself_positive_characteristic'])
        self.assertEqual(c['therefore_completed_xi_is_not_positive_characteristic'],
                         'NOT_ESTABLISHED')

    def test_numerical_convergence_holdouts_not_certified_as_interval(self):
        import mpmath as mp
        p=self.params()
        c=completed_mellin_band_certificate(**p)
        with mp.workdps(65):
            for t in (mp.mpf('0'),mp.mpf('0.4'),mp.mpf('1.375')):
                target=completed_characteristic_oracle(0,t)
                b=finite_completed_characteristic(0,t,chart='beta',
                         cutoff=500,prime_cutoff=97,max_exponent=5)
                d=finite_completed_characteristic(0,t,chart='dirac',
                         mesh=F(1,120),left=-840,right=840,
                         prime_cutoff=97,max_exponent=5)
                assert_bound=lambda q: mp.mpf(q.numerator)/q.denominator
                self.assertLessEqual(abs(b-target),
                                     assert_bound(c['completed_beta_error_upper']))
                self.assertLessEqual(abs(d-target),
                                     assert_bound(c['completed_dirac_error_upper']))
                self.assertLessEqual(abs(b-d),
                                     assert_bound(c['dirac_vs_beta_uniform_error_upper']))
                self.assertLessEqual(abs(b),mp.mpf('1.0000000000001'))
                self.assertLessEqual(abs(d),mp.mpf('1.0000000000001'))

    def test_zero_frequency_strict_normalization(self):
        for chart in ('beta','dirac'):
            z=finite_completed_characteristic(1,0,chart=chart,
                  cutoff=30,mesh=F(1,30),left=-100,right=110,
                  prime_cutoff=13,max_exponent=2)
            self.assertLess(abs(z-1),1e-45)

    def test_wrong_chart_refused(self):
        with self.assertRaises(TateMellinSourceError):
            finite_completed_characteristic(0,1,chart='phase_gauge')

    def test_parameter_mutation_does_not_prove_RH(self):
        fake=finite_prime_coefficients(3,2,fake_six=True)
        wrong=finite_prime_coefficients(3,2,wrong_two=True)
        self.assertTrue(fake['positive_coefficients'])
        self.assertTrue(wrong['positive_coefficients'])
        self.assertFalse(fake['authentic_prime_labels'])
        self.assertFalse(wrong['authentic_prime_labels'])
        self.assertTrue(archimedean_parity_and_pole_firewall(0)
                        ['signed_completed_Weil_not_constructed'])


if __name__=='__main__':
    unittest.main()

from observational_succ.tate_mellin_prime_transport import (
    finite_prime_jet_cumulants,compact_weil_prime_jet_source,
)

class PrimeJetsAtTheBoundary(unittest.TestCase):
    def test_exact_von_mangoldt_jet_cumulants(self):
        c=finite_prime_jet_cumulants(7,2,4)
        self.assertEqual(tuple(x['prime'] for x in c['rows']),(2,3,5,7))
        p2=c['rows'][0]
        self.assertEqual(p2['coefficient_of_log_prime'],F(1,3))
        self.assertEqual(p2['coefficient_of_log_prime_squared_in_variance'],F(4,9))
        self.assertEqual(p2['finite_prime_power_weights'][:2],(F(1,4),F(1,16)))
        self.assertEqual(p2['truncated_log_prime_tail'],F(1,4**5)*F(4,3))

    def test_genuine_half_density_compact_support(self):
        c=compact_weil_prime_jet_source(36)
        lookup={x['n']:x for x in c['prime_power_impulses']}
        self.assertEqual(lookup[4]['half_density_weight'],'log(2)/sqrt(4)')
        self.assertEqual(lookup[8]['exponent'],3)
        self.assertEqual(lookup[9]['prime'],3)
        self.assertEqual(lookup[25]['half_density_weight'],'log(5)/sqrt(25)')
        self.assertNotIn(6,lookup)
        self.assertFalse(c['full_signed_Weil_form_obtained'])

    def test_source_thresholds_extend_only_with_authentic_prime_sieve(self):
        with self.assertRaises(TateMellinSourceError):
            compact_weil_prime_jet_source(4000)
        with self.assertRaises(TateMellinSourceError):
            compact_weil_prime_jet_source(1)
        with self.assertRaises(TateMellinSourceError):
            finite_prime_jet_cumulants(11,1,4)

from observational_succ.tate_mellin_prime_transport import (
    finite_hyperbolic_succ_fucc_certificate,natural_succ_dirichlet_band_certificate,
    euler_vs_succ_carrier_certificate,natural_succ_characteristic,
    finite_euler_characteristic,
)

class HyperbolicCarrierGluing(unittest.TestCase):
    def test_exact_natural_prime_vector_bijection(self):
        for H in (6,12,40,101):
            cert=finite_hyperbolic_succ_fucc_certificate(H,2)
            self.assertEqual(cert['natural_address_count'],H)
            self.assertEqual(cert['unique_valuation_vector_count'],H)
            self.assertEqual(cert['natural_address_6'],((2,1),(3,1)))
            self.assertEqual(cert['SUCC_Dirichlet_partition_exact'],
                             sum((F(1,n*n) for n in range(1,H+1)),F()))
            self.assertEqual(cert['SUCC_Dirichlet_partition_exact'],
                             cert['FUCC_hyperbolic_partition_exact'])

    def test_integer_truncation_error_rational(self):
        c=natural_succ_dirichlet_band_certificate(100,2)
        self.assertEqual(c['omitted_integer_tail_upper'],F(1,100))
        self.assertLess(c['uniform_arithmetic_characteristic_error_upper'],F(1,50))

    def test_two_finite_arithmetic_routes_triangle(self):
        cert=euler_vs_succ_carrier_certificate(200,2,97,5)
        import mpmath as mp
        b=mp.mpf(cert['uniform_zeta_source_discrepancy_upper'].numerator)/\
          cert['uniform_zeta_source_discrepancy_upper'].denominator
        for t in (0,mp.mpf('0.4'),mp.mpf('1.7')):
            succ=natural_succ_characteristic(200,2,t)
            fucc=finite_euler_characteristic(97,5,2,t)
            self.assertLessEqual(abs(succ-fucc),b)
        self.assertFalse(cert['hyperbolic_cutoff_equals_rectangular_cutoff'])

    def test_no_false_finite_box_isomorphism(self):
        # The exact prefix n<=6 excludes 2²3=12; the rectangular box
        # p={2,3}, K>=2 necessarily contains 12.
        h=finite_hyperbolic_succ_fucc_certificate(6,2)
        box=finite_prime_coefficients(3,2)['coefficients']
        self.assertEqual(h['natural_address_count'],6)
        self.assertIn(12,box)
        self.assertNotEqual(len(box),6)

    def test_source_cutoff_out_of_budget_rejected(self):
        with self.assertRaises(TateMellinSourceError):
            finite_hyperbolic_succ_fucc_certificate(1,2)
        with self.assertRaises(TateMellinSourceError):
            natural_succ_dirichlet_band_certificate(50,1)

from observational_succ.tate_mellin_prime_transport import finite_hyperbolic_prime_coupling

class FiniteSourceInducedCoupling(unittest.TestCase):
    def test_finite_S_U_C_C_cutoff_creates_negative_prime_correlation(self):
        c=finite_hyperbolic_prime_coupling(5,2,2,3)
        self.assertEqual(c['joint_active_probability'],0)
        self.assertLess(c['finite_SUCC_coupling_covariance'],0)
        self.assertEqual(c['infinite_genuine_zeta_law_covariance'],0)
        self.assertGreaterEqual(c['absolute_covariance_upper'],
                                abs(c['finite_SUCC_coupling_covariance']))

    def test_even_after_first_joint_event_the_correlation_is_nonzero(self):
        c=finite_hyperbolic_prime_coupling(6,2,2,3)
        self.assertGreater(c['joint_active_probability'],0)
        self.assertLess(c['finite_SUCC_coupling_covariance'],0)
        self.assertEqual(c['finite_SUCC_coupling_covariance'],F(-10800,4118023))

    def test_prime_source_gate_and_limit_independence(self):
        with self.assertRaises(TateMellinSourceError):
            finite_hyperbolic_prime_coupling(30,2,2,6)
        with self.assertRaises(TateMellinSourceError):
            finite_hyperbolic_prime_coupling(30,2,3,3)

from observational_succ.tate_mellin_prime_transport import finite_mellin_gram_transport_certificate

class PositiveMellinGramTransport(unittest.TestCase):
    def test_exact_finite_frequency_operator_norm(self):
        params=CompletedPositiveSourceInterface.params()
        c=completed_mellin_band_certificate(**params)
        x=finite_mellin_gram_transport_certificate(
            (F(0),F(1,2),F(1),F(2)),
            c['completed_dirac_error_upper'],c['height'])
        self.assertEqual(x['dimension'],4)
        self.assertEqual(x['operator_error_upper'],4*c['completed_dirac_error_upper'])
        self.assertTrue(x['finite_source_gram_positive_semidefinite'])
        self.assertFalse(x['completed_signed_Weil_gram_identified'])

    def test_unauthenticated_basis_expansion_refused(self):
        with self.assertRaises(TateMellinSourceError):
            finite_mellin_gram_transport_certificate((F(0),F(5,2)),F(1,20),F(2))
        with self.assertRaises(TateMellinSourceError):
            finite_mellin_gram_transport_certificate((0,1),-1,2)

class SourceResourceBudget(unittest.TestCase):
    def test_rectangular_prime_coefficient_box_oom_gate(self):
        with self.assertRaises(TateMellinSourceError):
            finite_prime_coefficients(97,6)
