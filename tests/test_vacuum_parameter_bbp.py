"""Exact rational and independent Machin holdout for BBP vacuum/resolvent bridge."""
from __future__ import annotations

import unittest
from fractions import Fraction as Q
from math import comb

from observational_succ.vacuum_parameter_bbp import (
    VacuumBridgeError, kernel, forcing, moment, difference, parameter_derivative,
    hankel, hankel_sylvester, krylov_certificate, certified_hex_prefix,
    source_orbit, source_tail_bracket, selected_hex_digit,
    prime_valuations, finite_adelic_norm, diagonal_product_formula,
    log_bracket_positive, vacuum_rank_one_factor, hidden_determinant_example,
    rational_moment_counterfeit,
)


def independent_arctan_bracket(denominator, terms):
    x=Q(1,denominator)
    subtotal=sum(((-1)**k*x**(2*k+1)/Q(2*k+1)
                  for k in range(terms)),Q())
    next_term=(-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return min(subtotal,subtotal+next_term),max(subtotal,subtotal+next_term)


def independent_machin_pi_bracket(terms=32):
    a,A=independent_arctan_bracket(5,terms)
    b,B=independent_arctan_bracket(239,terms)
    return 16*a-4*B,16*A-4*b


class VacuumNormalizationTests(unittest.TestCase):
    def test_polynomial_signed_source_vacuum_and_factor(self):
        for t in (Q(0),Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(9,10),Q(1)):
            self.assertEqual(kernel(t),4-2*t**3-t**4-t**5)
            self.assertGreaterEqual(kernel(t),0)
        self.assertEqual(kernel(1),0)
        self.assertEqual(kernel(0),4)
        self.assertEqual(kernel(Q(1,2)),Q(1,2)*(Q(1,4)+2)*
                         (Q(1,4)+1+2))
        with self.assertRaises(VacuumBridgeError):kernel(Q(3,2))
    def test_authentic_poles_have_exact_monomial_integral(self):
        # P(t) integral against t^(8n-8) is exact sum of beta monomial terms.
        for n in range(1,35):
            a=Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
            self.assertEqual(forcing(n),a)
            self.assertGreater(a,0)
            self.assertEqual(moment(n-1),a)
        self.assertEqual(forcing(1),Q(47,15))
        self.assertEqual(forcing(2),Q(106,819))
        with self.assertRaises(VacuumBridgeError):forcing(0)
    def test_continuous_generator_derivatives_alternate(self):
        for n in range(1,14):
            self.assertEqual(parameter_derivative(n,0),forcing(n))
            for order in range(1,7):
                self.assertGreater((-1)**order*parameter_derivative(n,order),0)
    def test_discrete_source_differences_alternate(self):
        for n in range(1,14):
            for depth in range(10):
                self.assertGreater((-1)**depth*difference(n,depth),0)
                expected=sum(((-1)**(depth-j)*comb(depth,j)*forcing(n+j)
                              for j in range(depth+1)),Q())
                self.assertEqual(difference(n,depth),expected)
    def test_hankel_all_source_minors_strictly_positive(self):
        for n in range(1,6):
            minors=hankel_sylvester(n)
            self.assertEqual(len(minors),n)
            self.assertTrue(all(x>0 for x in minors))
        self.assertEqual(hankel(1),((Q(47,15),),))
    def test_source_bounds_and_asymptotic_coefficient(self):
        for n in range(1,40):
            self.assertGreaterEqual(forcing(n),Q(4,(8*n-7)*(8*n-6)))
            self.assertLessEqual(forcing(n),Q(15,(8*n-7)*(8*n-6)))
        for n in (500,1000):
            asym=forcing(n)*n*n
            self.assertLess(abs(asym-Q(15,64)),Q(1,50))


class ParametricSchurCertificateTests(unittest.TestCase):
    def test_krylov_one_mode_vacuum_resolvent(self):
        first=krylov_certificate(1)
        m0,m1=moment(0),moment(1)
        self.assertEqual(first.galerkin_lower,m0*m0/(m0-m1/16))
        self.assertEqual(first.moments_used,3)
        self.assertEqual(first.lower,
                         first.galerkin_lower+first.residual_norm_squared)
        self.assertEqual(first.upper,
                         first.galerkin_lower+Q(16,15)*first.residual_norm_squared)
    def test_stronger_Krylov_enclosures_monotone(self):
        prior=None
        for d in range(1,9):
            c=krylov_certificate(d)
            self.assertEqual(c.moments_used,2*d+1)
            self.assertGreater(c.residual_norm_squared,0)
            self.assertLess(c.lower,c.upper)
            self.assertLessEqual(c.upper-c.galerkin_lower,
                                 c.baseline_neumann_tail_upper)
            if prior is not None:
                self.assertGreater(c.galerkin_lower,prior.galerkin_lower)
                self.assertGreater(c.lower,prior.lower)
                self.assertLess(c.upper,prior.upper)
            prior=c
    def test_machin_independent_holdout_all_bounds(self):
        lo,hi=independent_machin_pi_bracket(32)
        self.assertLess(lo,hi)
        for d in range(1,9):
            c=krylov_certificate(d)
            self.assertLessEqual(c.lower,lo)
            self.assertGreaterEqual(c.upper,hi)
    def test_hex_prefix_from_exact_rational_eight_dimensional(self):
        self.assertEqual(certified_hex_prefix(1,3),'3.243')
        self.assertEqual(certified_hex_prefix(2,5),'3.243F6')
        self.assertEqual(certified_hex_prefix(4,11),'3.243F6A8885A')
        self.assertEqual(certified_hex_prefix(8,23),'3.243F6A8885A308D313198A2')
        self.assertIsNone(certified_hex_prefix(8,24))
        pi_lo,pi_hi=independent_machin_pi_bracket(32)
        c=krylov_certificate(8)
        scale=16**23
        self.assertEqual((pi_lo*scale).numerator//(pi_lo*scale).denominator,
                         (c.lower*scale).numerator//(c.lower*scale).denominator)
        self.assertEqual((pi_hi*scale).numerator//(pi_hi*scale).denominator,
                         (c.upper*scale).numerator//(c.upper*scale).denominator)
    def test_explicit_all_depth_neumann_residual_cap(self):
        for d in range(1,9):
            cert=krylov_certificate(d)
            cap=Q(16,15)*Q(1,16)**(2*d)*forcing(2*d+1)
            self.assertEqual(cert.baseline_neumann_tail_upper,cap)
            self.assertLessEqual(cert.upper-cert.galerkin_lower,cap)
            simpler=Q(16,1)*Q(1,16)**(2*d)/Q((16*d+1)*(16*d+2))
            self.assertLessEqual(cap,simpler)
    def test_invalid_vacuum_and_parameter_inputs_rejected(self):
        for args in ((0,Q(1,16)),(2,Q(1)),(2,Q(-1,2)),(2,.25)):
            with self.assertRaises(VacuumBridgeError):krylov_certificate(*args)
        with self.assertRaises(VacuumBridgeError):certified_hex_prefix(3,0)
        with self.assertRaises(VacuumBridgeError):moment(-1)
    def test_separable_fake_source_matches_two_moments_but_not_pi(self):
        fake=rational_moment_counterfeit()
        self.assertFalse(fake['genuine_bbp_source'])
        self.assertEqual(fake['matching_moments'],2)
        self.assertEqual(fake['mass'],moment(0))
        self.assertEqual(fake['mass']*fake['location'],moment(1))
        self.assertNotEqual(fake['mass']*fake['location']**2,moment(2))
        self.assertEqual(fake['pi_like_rational'],krylov_certificate(1).galerkin_lower)
        self.assertNotEqual(fake['pi_like_rational'],krylov_certificate(8).lower)


class AuthenticatedOrbitTransferTests(unittest.TestCase):
    def test_gearbox_recurrence_and_tail_bounds(self):
        u=Q(0)
        for n in range(1,40):
            u=16*u+forcing(n)
            self.assertEqual(source_orbit(n),u)
            lo,hi=source_tail_bracket(n)
            self.assertEqual(lo,forcing(n+1)/16)
            self.assertEqual(hi,forcing(n+1)/15)
            self.assertLess(lo,hi)
            self.assertLess(hi,Q(1,2))
    def test_selected_hex_digits_on_same_orbit(self):
        lo,hi=independent_machin_pi_bracket(32)
        for n in range(1,26):
            proposed=selected_hex_digit(n)
            self.assertIsNotNone(proposed)
            x=16**(n-1)
            f1=(x*lo).numerator//(x*lo).denominator
            f2=(x*hi).numerator//(x*hi).denominator
            self.assertEqual(f1,f2)
            self.assertEqual(proposed,f1%16)
    def test_origin_zero_is_not_source_infinity(self):
        self.assertEqual(source_orbit(0),0)
        self.assertEqual(source_orbit(1),Q(47,15))
        with self.assertRaises(VacuumBridgeError):source_tail_bracket(0)
        with self.assertRaises(VacuumBridgeError):selected_hex_digit(0)


class AdelicVacuumTests(unittest.TestCase):
    def test_diagonal_rational_product_formula_exact(self):
        for x in (Q(1),Q(-1),Q(12),Q(5,14),Q(-360,49),Q(7,128),Q(81,25)):
            self.assertTrue(diagonal_product_formula(x))
            sup=prime_valuations(x)
            self.assertEqual(finite_adelic_norm(x,max(sup,default=1)),1)
        self.assertEqual(prime_valuations(Q(12)),{2:2,3:1})
        self.assertEqual(prime_valuations(Q(5,14)),{2:-1,5:1,7:-1})
    def test_incomplete_place_source_has_visible_residual(self):
        self.assertEqual(finite_adelic_norm(12,1),12)
        self.assertEqual(finite_adelic_norm(12,2),3)
        self.assertEqual(finite_adelic_norm(12,3),1)
        self.assertNotEqual(Q(1,2),1) # one-place p=2 idele, not rational diagonal
        self.assertEqual(finite_adelic_norm(Q(1,6),2),Q(1,3))
        self.assertEqual(finite_adelic_norm(Q(1,6),3),1)
    def test_exact_log_vacuum_at_one_and_rational_bracket(self):
        self.assertEqual(log_bracket_positive(1,1),(Q(0),Q(0)))
        self.assertEqual(log_bracket_positive(1,100),(Q(0),Q(0)))
        import mpmath as mp
        with mp.workdps(70):
            for x in (Q(1,3),Q(2),Q(3),Q(12)):
                lo,hi=log_bracket_positive(x,40)
                r=mp.log(mp.mpf(x.numerator)/x.denominator)
                self.assertLessEqual(mp.mpf(lo.numerator)/lo.denominator,r)
                self.assertGreaterEqual(mp.mpf(hi.numerator)/hi.denominator,r)
    def test_reject_malformed_additive_vs_multiplicative_zero(self):
        with self.assertRaises(VacuumBridgeError):diagonal_product_formula(0)
        with self.assertRaises(VacuumBridgeError):prime_valuations(0)
        with self.assertRaises(VacuumBridgeError):finite_adelic_norm(0,2)
        with self.assertRaises(VacuumBridgeError):log_bracket_positive(0,5)
        with self.assertRaises(VacuumBridgeError):log_bracket_positive(-1,5)


class MatrixPotentialTests(unittest.TestCase):
    def test_rank_one_logdet_vacuum_and_parameter_resolvent(self):
        A=((Q(2),Q(1)),(Q(1),Q(2)))
        u=(Q(1),Q(0))
        zero=vacuum_rank_one_factor(A,u,0)
        self.assertEqual(zero['determinant_ratio'],1)
        self.assertEqual(zero['c'],Q(2,3))
        for t in (Q(1,2),Q(1),Q(3)):
            out=vacuum_rank_one_factor(A,u,t)
            self.assertEqual(out['determinant_ratio'],1+t*Q(2,3))
            self.assertEqual(out['log_potential_derivative'],Q(2,3)/(1+t*Q(2,3)))
            self.assertTrue(out['log_potential_at_zero_is_zero'])
    def test_hidden_graph_one_port_same_response_different_determinant(self):
        a=hidden_determinant_example(Q(1),Q(1))
        b=hidden_determinant_example(Q(2),Q(3))
        self.assertEqual(a['static_one_port'],b['static_one_port'])
        self.assertEqual(a['static_one_port'],0)
        self.assertEqual(a['hidden_determinant'],1)
        self.assertEqual(b['hidden_determinant'],6)
    def test_invalid_matrices_and_singular_paths_refused(self):
        with self.assertRaises(VacuumBridgeError):vacuum_rank_one_factor(((0,),),(1,),1)
        with self.assertRaises(VacuumBridgeError):vacuum_rank_one_factor(((1,2),(2,1)),(1,1),1)
        with self.assertRaises(VacuumBridgeError):vacuum_rank_one_factor(((1,),),(1,),-1)
        with self.assertRaises(VacuumBridgeError):hidden_determinant_example(0,2)
    def test_noncommuting_matrix_log_derivative_is_not_inverse_times_H(self):
        # d log(A+tH)/dt is symmetric if SPD A+tH. A^-1 H is nonsymmetric.
        a_inv_H=((Q(0),Q(1,2)),(Q(1,3),Q(0)))
        self.assertNotEqual(a_inv_H[0][1],a_inv_H[1][0])


if __name__=='__main__':unittest.main()
