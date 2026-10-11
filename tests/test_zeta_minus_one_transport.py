"""Exact source-aware regression tests for zeta(-1) global Euler transport.

All arithmetic probes use Fraction; the functional equation, Basel result,
and Bernoulli special-value theorem are stated imported classical facts.
"""
from fractions import Fraction as Q
from math import pi
import unittest

from observational_succ.zeta_minus_one_transport import (
    EulerTransportError, primes_upto, prime_jet_gap,
    local_prime_factor_minus_one, local_factor_at_two,
    naive_cutoff_at_minus_one, convergent_cutoff_at_two,
    certified_euler_cutoff, positive_side_mutation_controls,
    eta_abel_value, eta_abel_deficit, negative_odd_zeta_from_bernoulli,
    zeta_minus_one_transport_demo,
    shift_dilation_address_defect, shift_dilation_operator_identity,
)


class ZetaLocalGlobalTransportTests(unittest.TestCase):
    def test_local_negative_one_factor_is_inverse_prime_jet_gap(self):
        for p in primes_upto(199):
            self.assertEqual(local_prime_factor_minus_one(p), -Q(1,p-1))
            for k in (0,1,2,3):
                self.assertEqual(prime_jet_gap(p,k),(p-1)*p**k)
        with self.assertRaises(EulerTransportError):
            local_prime_factor_minus_one(6)
        with self.assertRaises(EulerTransportError):
            prime_jet_gap(6,0)

    def test_succ_fucc_exact_ax_plus_b_semigroup_relation(self):
        for p in (2,3,5,7,11,13,19):
            for n in (1,2,5,11,57):
                self.assertEqual(shift_dilation_address_defect(p,n),1-p)
                self.assertTrue(shift_dilation_operator_identity(p,n))
                for a in (0,1,2,3,10):
                    self.assertEqual(shift_dilation_address_defect(p,n,a),
                                     a*(1-p))
                    self.assertTrue(shift_dilation_operator_identity(p,n,a))
                    # Operator ket equality V_p S^a |n> = S^(p*a) V_p |n>.
                    self.assertEqual(p*(n+a),p*n+p*a)
        self.assertEqual(shift_dilation_address_defect(5,3),-4)

    def test_composite_affine_defect_does_not_make_a_fake_prime_place(self):
        self.assertEqual(shift_dilation_address_defect(6,3),-5)
        self.assertTrue(shift_dilation_operator_identity(6,3))
        with self.assertRaises(EulerTransportError):
            local_prime_factor_minus_one(6)
        with self.assertRaises(EulerTransportError):
            prime_jet_gap(6)
        with self.assertRaises(EulerTransportError):
            shift_dilation_address_defect(1,3)
        with self.assertRaises(EulerTransportError):
            shift_dilation_address_defect(5,0)
        with self.assertRaises(EulerTransportError):
            shift_dilation_address_defect(5,1,-1)
        # A coordinate integer difference is not [S,V]|n>=scalar*|n>.
        # The two different destination basis states remain orthogonal.
        self.assertNotEqual(5*3+1,5*(3+1))

    def test_local_prime_cutoffs_have_sign_and_zero_magnitude_behavior(self):
        values={2:Q(-1),3:Q(1,2),5:Q(-1,8),
                7:Q(1,48),11:Q(-1,480),13:Q(1,5760)}
        for cutoff,answer in values.items():
            self.assertEqual(naive_cutoff_at_minus_one(cutoff),answer)
        magnitude=Q(1)
        for p in primes_upto(199):
            following=abs(naive_cutoff_at_minus_one(p))
            self.assertLessEqual(following,magnitude)
            magnitude=following
        self.assertLess(magnitude,Q(1,10**40))
        # Euclid gives infinitely many p>=3, each factor has norm <=1/2.
        # The mathematical infinite-limit conclusion is NOT from the
        # finite numeric cutoff alone.

    def test_convergent_positive_prime_cutoffs_are_exact_rational(self):
        expected={2:Q(4,3),3:Q(3,2),
                  5:Q(25,16),7:Q(1225,768)}
        previous=Q(1)
        for cutoff in (2,3,5,7,11,13,17,23,31,47):
            P=convergent_cutoff_at_two(cutoff)
            self.assertGreater(P,previous)
            previous=P
            self.assertGreater(local_factor_at_two(primes_upto(cutoff)[-1]),1)
            if cutoff in expected:
                self.assertEqual(P,expected[cutoff])

    def test_exact_integer_tail_telescopes_and_bounds_missing_prime_tail(self):
        for X in (2,3,5,7,10,20):
            for M in (X+1,X+4,X+25):
                integer_tail=Q(1)
                for n in range(X+1,M+1):
                    integer_tail*=Q(n*n,n*n-1)
                self.assertEqual(integer_tail,Q(M*(X+1),X*(M+1)))
                self.assertLessEqual(integer_tail,Q(X+1,X))
                missing_prime_tail=Q(1)
                for p in primes_upto(M):
                    if p>X:
                        missing_prime_tail*=local_factor_at_two(p)
                self.assertLessEqual(missing_prime_tail,integer_tail)
        # Taking M to infinity is an elementary algebraic limit theorem.

    def test_cutoff_certificate_has_rigorous_normalized_arch_tail_bound(self):
        for X in (2,3,5,7,11,29,47,101):
            c=certified_euler_cutoff(X)
            self.assertEqual(c.cutoff,X)
            self.assertEqual(c.zeta_two_lower,c.convergent_positive_product)
            self.assertEqual(c.zeta_two_upper,c.zeta_two_lower*Q(X+1,X))
            self.assertEqual(c.absolute_minus_one_error_leq_coefficient,
                             Q(1,12*X))
            self.assertLess(c.zeta_two_lower,c.zeta_two_upper)
            # float is a sanity check, NOT the source of the rigorous proof.
            estimate=c.transported_minus_one_estimate()
            self.assertGreater(estimate,-1/12-1e-12)
            self.assertLessEqual(estimate+1/12,1/(12*X)+1e-12)

    def test_abel_renormalized_alternating_path_has_exact_error_formula(self):
        for r in (Q(0),Q(1,2),Q(9,10),Q(99,100),Q(999,1000)):
            self.assertEqual(eta_abel_value(r)+eta_abel_deficit(r),Q(1,4))
            self.assertEqual(eta_abel_deficit(r),(1-r)**2/(4*(1+r)**2))
        self.assertEqual(Q(1,4)/(1-4),Q(-1,12))
        self.assertLess(eta_abel_deficit(Q(99,100)),eta_abel_deficit(Q(9,10)))
        with self.assertRaises(EulerTransportError):
            eta_abel_value(Q(1))
        with self.assertRaises(EulerTransportError):
            eta_abel_value(-Q(1,2))
        with self.assertRaises(EulerTransportError):
            eta_abel_value(0.5)

    def test_negative_odd_family_and_classical_completed_symmetry(self):
        known={1:Q(-1,12),2:Q(1,120),3:-Q(1,252),
               4:Q(1,240),5:-Q(1,132),6:Q(691,32760)}
        for m,value in known.items():
            self.assertEqual(negative_odd_zeta_from_bernoulli(m),value)
        with self.assertRaises(EulerTransportError):
            negative_odd_zeta_from_bernoulli(0)
        # Completed zeta at s=-1,2: both equal pi/6.
        self.assertAlmostEqual(-2*pi*float(known[1]),pi/6)

    def test_prime_two_deletion_does_not_preserve_unmodified_gamma_factor(self):
        r=positive_side_mutation_controls()
        self.assertEqual(r["base_zeta_minus_one"],"-1/12")
        self.assertEqual(r["two_deletion_analytic_value"],"1/12")
        self.assertEqual(r["two_deletion_bad_reused_zeta_reflection"],"-1/16")
        self.assertTrue(r["prime_two_deletion_invalidates_unmodified_functional_equation"])
        self.assertTrue(r["fake_six_is_not_a_prime_euler_factor"])
        self.assertNotEqual(convergent_cutoff_at_two(11),
                            convergent_cutoff_at_two(11)*Q(36,35))

    def test_source_prime_validation_refuses_fake_composite_and_boolean(self):
        self.assertEqual(primes_upto(11),(2,3,5,7,11))
        self.assertNotIn(6,primes_upto(11))
        with self.assertRaises(EulerTransportError):
            primes_upto(1)
        with self.assertRaises(EulerTransportError):
            primes_upto(True)
        with self.assertRaises(EulerTransportError):
            local_factor_at_two(6)
        with self.assertRaises(EulerTransportError):
            prime_jet_gap(2,-1)

    def test_global_analytic_continuation_does_not_commute_with_local_product(self):
        self.assertNotEqual(naive_cutoff_at_minus_one(101),Q(-1,12))
        self.assertEqual(negative_odd_zeta_from_bernoulli(1),Q(-1,12))
        # Rigorous contradiction follows from product-to-zero theorem,
        # whereas completed zeta at -1 has the nonzero Bernoulli value.

    def test_receipt_retains_no_rh_zero_reading_or_physical_claims(self):
        r=zeta_minus_one_transport_demo()
        self.assertEqual(r["status"],"ZETA_MINUS_ONE_GLOBAL_EULER_ARCHIMEDEAN_TRANSPORT")
        self.assertEqual(r["local_prime_minus_one_factor"],"-1/(p-1)")
        self.assertEqual(r["prime_jet_first_return_gap"],"p-1")
        self.assertEqual(r["shift_dilation_one_step_address_defect"],"1-p")
        self.assertEqual(r["ax_b_operator_semigroup_relation"],"V_p S = S^p V_p")
        self.assertTrue(r["same_shift_dilation_defect_rule_for_composite_six"])
        self.assertTrue(r["nonprime_affine_defect_does_not_authorize_euler_prime_factor"])
        self.assertFalse(r["operator_commutator_claimed_scalar"])
        self.assertFalse(r["cuntz_ax_b_finite_arch_completion_proved_here"])
        self.assertEqual(r["global_zeta_minus_one_value"],"-1/12")
        self.assertEqual(r["abel_eta_negative_one"],"1/4")
        self.assertEqual(r["eta_to_zeta_factor_at_minus_one"],"-3")
        self.assertEqual(r["negative_odd_s_minus_three"],"1/120")
        self.assertTrue(r["local_factor_partial_products_tend_to_zero"])
        self.assertFalse(r["local_continuation_and_global_product_commute"])
        self.assertTrue(r["analytic_continuation_and_functional_equation_are_imported_theorems"])
        self.assertFalse(r["source_specific_euler_gamma_completed_weil_RH_bridge_proved"])
        self.assertFalse(r["nontrivial_zeta_zeros_used_as_inputs"])
        self.assertFalse(r["RH_claimed"])


if __name__=="__main__":
    unittest.main()
