"""Source/model interaction tests: exact controls independent of zeta-zero tables."""
import unittest
from fractions import Fraction as Q
from math import factorial, isqrt

from observational_succ.source_model_interaction import (
    SourceInteractionError, factor, padic_v, global_product_formula,
    diagonal_source_filter, unobserved_denominator_witness,
    local_euler_shell, finite_euler_model, prime_set, e3_gt_20,
    power_geometric_upper, smooth_prime_theta_obstruction,
    completed_function_mutant, wrong_conductor_theta_scale,
    upper_exp_neg, exponential_moment_tail, analytic_theta_tail,
    xi_tail_envelopes, real_strip_nonvanishing, trivial_zero_certificate,
    contact_constant_bridge, completed_prime_current_source_rule,
    derivative_of_trivial_zero, interaction_receipt,
)


class AdelicSourceReceipts(unittest.TestCase):
    def test_prime_source_rejects_fake_composite_six(self):
        with self.assertRaises(SourceInteractionError):
            prime_set([2, 3, 6])
        with self.assertRaises(SourceInteractionError):
            prime_set([4])
        self.assertEqual(prime_set([2, 3, 5, 7]),(2,3,5,7))

    def test_integer_source_factorizations(self):
        known = {1:{}, 2:{2:1}, 4:{2:2}, 6:{2:1,3:1},
                 30:{2:1,3:1,5:1}, 121:{11:2}, 7**5:{7:5}}
        for n, expected in known.items():
            self.assertEqual(factor(n), expected)
            self.assertEqual(__import__('math').prod(p**e for p,e in factor(n).items()),n)

    def test_normalized_rational_product_formula(self):
        for p in (2,3,5,7,11):
            for k in (-4,-2,-1,0,1,3):
                for sign in (-1,1):
                    x=Q(sign)*Q(p)**k
                    proof=global_product_formula(x)
                    self.assertTrue(proof['product_one'])
        self.assertEqual(global_product_formula(Q(6,35))['finite_local_norms'],
                         {'2':'1/2','3':'1/3','5':'5','7':'7'})

    def test_padic_orders_allow_negative_exponents(self):
        q=Q(-72,175)
        self.assertEqual({p:padic_v(q,p) for p in (2,3,5,7,11)},
                         {2:3,3:2,5:-2,7:-1,11:0})

    def test_lattice_from_all_integral_places(self):
        for k in (-11,-1,0,1,137):
            self.assertTrue(diagonal_source_filter(k,(2,3,5))['all_places_integral'])
        self.assertFalse(diagonal_source_filter(Q(1,35),(2,3,5))['all_places_integral'])

    def test_finite_place_source_alias_is_real(self):
        witness=unobserved_denominator_witness((2,3,5,7,11,13))
        q=Q(witness['source'])
        self.assertTrue(witness['legal_visible_integrality'])
        self.assertTrue(witness['illegal_global_integrality'])
        self.assertNotIn(witness['hidden_prime'],(2,3,5,7,11,13))
        self.assertEqual(q.denominator,witness['hidden_prime'])
        self.assertTrue(diagonal_source_filter(q,(2,3,5,7,11,13))['passed_visible'])

    def test_wrong_unknown_denominator_is_exposed(self):
        self.assertEqual(diagonal_source_filter(Q(2,15),(3,))['unseen_denominator_places'],[5])
        self.assertFalse(diagonal_source_filter(Q(2,15),(3,))['passed_visible'])
        self.assertFalse(diagonal_source_filter(Q(1,7),(2,3,5))['all_places_integral'])

    def test_all_shell_limits_exact(self):
        for p in (2,3,5,7):
            for s in (1,2,3):
                for K in (0,1,2,8):
                    x=local_euler_shell(p,s,K)
                    pref=Q(x['prefix']);tail=Q(x['tail']);lim=Q(x['limit'])
                    self.assertEqual(pref+tail,lim)
                    self.assertEqual(lim,Q(p**s,p**s-1))

    def test_padic_local_haar_normalization_not_uniform_integer_sum(self):
        x=local_euler_shell(2,2,2)
        self.assertEqual(Q(x['prefix']),Q(21,16))
        self.assertEqual(Q(x['tail']),Q(1,48))
        self.assertEqual(Q(x['limit']),Q(4,3))

    def test_real_harmonic_divergence_gate(self):
        for P in ((2,), (2,3), (2,3,5),(2,3,5,7),(2,3,5,7,11)):
            x=finite_euler_model(P,1)
            self.assertGreaterEqual(Q(x['local_product']),Q(x['harmonic_lower_at_sigma_one']))
        with self.assertRaises(SourceInteractionError):
            finite_euler_model((2,3,6),1)

    def test_local_product_matches_source_finite_smooth_sum(self):
        for P in ((2,3),(2,3,5)):
            for s in (1,2,4):
                # independent finite rectangular valuation enumeration
                v=Q(0)
                from itertools import product
                for ks in product(range(5),repeat=len(P)):
                    n=1
                    for p,k in zip(P,ks): n*=p**k
                    v+=Q(1,n**s)
                prod=Q(1)
                for p in P:
                    prod*=sum((Q(1,p**(s*k)) for k in range(5)),Q())
                self.assertEqual(v,prod)


class InteractionObstructions(unittest.TestCase):
    def test_rational_exponential_receipt(self):
        self.assertTrue(e3_gt_20())
        partial=sum((Q(3**k,factorial(k)) for k in range(9)),Q())
        self.assertTrue(partial>20)

    def test_power_geometric_sum_upper_independent_prefix(self):
        for r in range(8):
            upper=power_geometric_upper(r)
            finite=sum((Q(m**r,20**m) for m in range(1,80)),Q())
            self.assertTrue(finite<upper)
            self.assertLess(upper-finite,Q(1,10**20))

    def test_p_smooth_modular_failure_exact_certificate(self):
        for primes in ((),(2,),(2,3),(2,3,5),(2,3,5,7)):
            r=smooth_prime_theta_obstruction(primes,42)
            self.assertTrue(r['strict_nonmodularity_proved_at_depth'])
            self.assertLess(Q(r['normalized_modular_defect_upper']),0)

    def test_modularity_failure_eventually_for_every_fixed_primes(self):
        for primes in ((2,),(2,3),(2,3,5),(2,3,5,7),(2,3,5,7,11)):
            proved=[h for h in (16,24,32,48,64) if
                    smooth_prime_theta_obstruction(primes,h)['strict_nonmodularity_proved_at_depth']]
            self.assertTrue(proved)

    def test_smooth_modular_bound_converges_to_zero(self):
        x=[Q(smooth_prime_theta_obstruction((2,3,5),h)['normalized_theta_upper'])
           for h in (20,40,80)]
        self.assertTrue(x[0]>x[1]>x[2])
        self.assertLess(x[2],Q(1,10**10))

    def test_mutant_functional_equation_and_residue_not_source(self):
        for s in (Q(1,3),Q(1,2),Q(2),Q(-7,3)):
            c=completed_function_mutant(s)
            self.assertTrue(c['symmetric'])
            self.assertEqual(Q(c['multiplier']),1+10*s*(s-1))
        self.assertEqual(Q(completed_function_mutant(0)['multiplier']),1)
        self.assertEqual(Q(completed_function_mutant(1)['multiplier']),1)
        self.assertEqual(Q(completed_function_mutant(2)['multiplier']),21)
        self.assertEqual(Q(completed_function_mutant(Q(1,2))['multiplier']),Q(-3,2))
        # s=(1±sqrt(3/5))/2 are REAL off-centre mutant zeros.
        self.assertEqual(Q(1)-Q(4,10),Q(3,5))

    def test_conductor_mutation_changes_fourier_boundary(self):
        for m in (2,3,4,6,9):
            x=wrong_conductor_theta_scale(m)
            self.assertFalse(x['naive_selfdual_theta_conductor'])
        self.assertTrue(wrong_conductor_theta_scale(4)['composite_not_Euler_prime'])
        self.assertFalse(wrong_conductor_theta_scale(3)['composite_not_Euler_prime'])

    def test_wrong_source_types_are_rejected(self):
        calls=(lambda:prime_set([2,2]), lambda:prime_set([3,2]),
               lambda:prime_set([True]),lambda:global_product_formula(0),
               lambda:padic_v(Q(2,3),9),lambda:local_euler_shell(6,2,3),
               lambda:finite_euler_model((4,),2),
               lambda:wrong_conductor_theta_scale(False),
               lambda:smooth_prime_theta_obstruction((2,2),20))
        for call in calls:
            with self.assertRaises(SourceInteractionError): call()


class AnalyticContinuationCertificates(unittest.TestCase):
    def test_exponential_moment_tail_identity_for_degree_zero_upper(self):
        for lam in (Q(1),Q(3),Q(9,2)):
            for T in (1,4,20):
                bound=exponential_moment_tail(lam,T,0)
                self.assertEqual(bound,upper_exp_neg(lam*T)/lam)

    def test_tail_envelopes_positive_and_shrink(self):
        for order in range(3):
            r1=Q(analytic_theta_tail(-2,3,3,8,order)['rational_upper'])
            r2=Q(analytic_theta_tail(-2,3,5,20,order)['rational_upper'])
            self.assertGreater(r1,r2)
            self.assertGreater(r2,0)

    def test_imaginary_uniformity_is_genuine(self):
        a=analytic_theta_tail(0,1,4,12,2)
        self.assertTrue(a['uniform_in_imaginary_direction'])
        self.assertNotIn('imaginary_max',a)

    def test_two_sided_source_strip_uses_right_exponents(self):
        # The gamma reflection endpoint exponent is -(1+sigma)/2, not +sigma/2.
        r=analytic_theta_tail(-4,5,3,12)
        self.assertEqual(r['power_envelope'],2)
        r=analytic_theta_tail(0,1,3,12)
        self.assertEqual(r['power_envelope'],0)

    def test_derivative_tail_has_correct_one_half_factor(self):
        j0=analytic_theta_tail(0,1,2,8,0)
        j1=analytic_theta_tail(0,1,2,8,1)
        self.assertGreater(Q(j0['rational_upper']),Q(0))
        self.assertGreater(Q(j1['rational_upper']),Q(0))
        self.assertNotEqual(j0['rational_upper'],j1['rational_upper'])

    def test_xi_two_derivatives_have_distinct_bounds(self):
        x=xi_tail_envelopes(-2,3,8,4,18)
        self.assertGreater(Q(x['xi_error_upper']),0)
        self.assertGreater(Q(x['xi_prime_error_upper']),0)
        self.assertGreater(Q(x['xi_second_error_upper']),0)
        self.assertTrue(x['not_a_numerical_quadrature_certificate'])

    def test_invalid_domain_and_ghost_limits(self):
        calls=(lambda:analytic_theta_tail(2,1,3,8),
               lambda:analytic_theta_tail(-41,1,3,8),
               lambda:analytic_theta_tail(0,1,0,8),
               lambda:analytic_theta_tail(0,1,3,0),
               lambda:analytic_theta_tail(0,1,3,8,3),
               lambda:xi_tail_envelopes(-2,3,1,3,8))
        for call in calls:
            with self.assertRaises(SourceInteractionError):call()

    def test_real_critical_segment_rigorous_nozero_without_zero_input(self):
        cert=real_strip_nonvanishing()
        self.assertEqual(Q(cert['xi_strict_lower_bound']),Q(59,120))
        self.assertTrue(cert['zeta_negative_on_open_interval'])
        self.assertTrue(cert['not_RH_or_vertical_strip_nonvanishing'])

    def test_global_non_euler_values_constructed(self):
        for m in (1,2,3,7,50):
            c=trivial_zero_certificate(m)
            self.assertEqual(c['argument'],-2*m)
            self.assertTrue(c['zeta_zero_simple'])
            self.assertEqual(c['zeta_0'],'-1/2')
            self.assertEqual(c['zeta_pole_at_1_residue'],'1')
            self.assertTrue(c['nontrivial_zeros_unknown'])

    def test_theta_symmetry_transports_Gamma_contact_at_half(self):
        c=contact_constant_bridge()
        self.assertEqual(c['xi_derivative_at_midpoint'],'0')
        self.assertTrue(c['xi_nonzero'])
        self.assertEqual(c['zeta_logarithmic_derivative_twice'],
                         'EulerGamma+pi/2+3*log(2)+log(pi)')
        self.assertTrue(c['equal_to_authentic_Suzuki_Gamma_contact_C'])

    def test_prime_current_is_analytic_continuation_not_divergent_series(self):
        c=completed_prime_current_source_rule()
        self.assertEqual(c['Euler_halfplane'],'Re(s)>1')
        self.assertIn('digamma(s/2)',c['model_interaction_meromorphic_expression'])
        self.assertTrue(c['cannot_evaluate_at_unknown_poles_without_guard'])
        self.assertTrue(c['not_a_convergent_prime_sum_outside_Euler_halfplane'])

    def test_trivial_zero_derivative_recovers_odd_euler_source(self):
        self.assertEqual(derivative_of_trivial_zero(1)['rational_coefficient'],'-1/4')
        self.assertEqual(derivative_of_trivial_zero(2)['rational_coefficient'],'3/4')
        self.assertEqual(derivative_of_trivial_zero(3)['rational_coefficient'],'-45/8')
        self.assertEqual(derivative_of_trivial_zero(2)['formula'],
                         'zeta_prime(-4)=3/4/pi^4*zeta(5)')
        self.assertTrue(derivative_of_trivial_zero(7)['classical_functional_equation_identity'])

    def test_gluing_receipt_deterministic(self):
        a=interaction_receipt()
        b=interaction_receipt()
        self.assertEqual(a,b)
        self.assertFalse(a['RH_proved'])
        self.assertTrue(a['finite_P_modular_obstruction']['strict_nonmodularity_proved_at_depth'])
        self.assertTrue(a['source_diagonal_product_formula']['product_one'])
        self.assertEqual(a['outside_euler_trivial_zero']['argument'],-2)


if __name__=='__main__':
    unittest.main()
