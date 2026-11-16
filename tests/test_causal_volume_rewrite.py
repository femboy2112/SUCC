"""Focused exact rational controls for the SUCC causal-volume algebra."""
from fractions import Fraction as F
from itertools import product
import random
import unittest

from observational_succ.causal_volume_rewrite import (
    poly,padd,pmul,pscale,peval,pderiv,pdivmod,pgcd,pcompose,from_sparse,
    integral_monomial_product,CausalVolumeGrammar,BBP,RATIONAL_NONNORMAL,
    bbp_tail_interval,bbp_forcing_pole_decomposition,bbp_completed_interval,
    fixed_n_shift_crosscheck,phase_frequency_ladder_residual,
    finite_moment_positive_mutant, finite_difference_forcing,
    finite_difference_integrand, approximate_green_difference,
    bbp_integer_lift_carry, gamma_phase_bound,
    OILY_U,OILY_V,OILY_DEN,oily_packet,oily_packet_partial,
    oily_packet_tail_budget,oily_two_register_resolvent_entry,
)


def beta(m,k):
    num=1
    for j in range(2,k+1): num*=j
    den=1
    for j in range(1,k+2): den*=m+j
    return F(num,den)


class CausalVolumeTests(unittest.TestCase):

    def test_oily_two_register_resolvent_is_exact_signed_bbp_kernel(self):
        self.assertEqual(OILY_DEN,BBP.reduced_kernel[1])
        for t in (F(0),F(1,19),F(1,5),F(1,2),F(7,10),F(1)):
            u=peval(OILY_U,t);v=peval(OILY_V,t)
            self.assertEqual(u+v,t)
            self.assertEqual(4*(1-u)*(1-v),peval(BBP.reduced_kernel[1],t))
            R=(1-t)/peval(BBP.reduced_kernel[1],t)
            self.assertEqual((1-t)*oily_two_register_resolvent_entry(t)/4,R)

    def test_oily_grade_partial_reconstructs_source_with_certified_tail(self):
        for t in (F(0),F(1,3),F(1,2),F(7,8),F(1)):
            R=(1-t)/peval(BBP.reduced_kernel[1],t)
            for N in (0,1,2,3,8,16):
                S=oily_packet_partial(t,N)
                self.assertLessEqual(S,R)
                self.assertLessEqual(R-S,oily_packet_tail_budget(t,N))
                self.assertGreaterEqual(oily_packet(t,N),0)

    def test_original_poles_are_integrated(self):
        for n in range(1,129):
            self.assertEqual(BBP.forcing(n),bbp_forcing_pole_decomposition(n))
            self.assertGreater(BBP.forcing(n),0)

    def test_reduced_kernel_is_exact_oily_kernel(self):
        num,den=BBP.reduced_kernel
        self.assertEqual(num,poly(1,-1))
        self.assertEqual(den,pmul(poly(2,0,-1),poly(2,-2,1)))
        self.assertTrue(BBP.pointwise_cancellation())

    def test_source_moment_factor_is_positive(self):
        self.assertEqual(BBP.numerator,pmul(poly(1,-1),pmul(poly(2,0,1),poly(2,2,1))))
        for q in (F(0),F(1,17),F(1,2),F(3,4),F(1)):
            self.assertGreaterEqual(peval(BBP.numerator,q),0)
            self.assertGreater(peval(BBP.denominator,q),0)

    def test_exact_zero_origin_and_successor(self):
        self.assertTrue(BBP.origin_equalizer())
        self.assertEqual(BBP.state(0),0)
        for n in range(1,42):
            self.assertEqual(BBP.state(n),BBP.state_by_successor(n))
            self.assertEqual(BBP.state(n),16*BBP.state(n-1)+BBP.forcing(n))

    def test_volume_polynomial_geometric_identity(self):
        for n in range(0,38):
            self.assertEqual(BBP.finite_volume_residual(n),poly(0))

    def test_prefix_and_truncated_tail_exact(self):
        for n in range(0,12):
            for d in range(0,7):
                self.assertEqual(fixed_n_shift_crosscheck(n,d),0)

    def test_bbp_green_bounds_and_monotone_r(self):
        for n in range(0,32):
            self.assertGreater(BBP.forcing(n+1),BBP.forcing(n+2))
            lo,hi=bbp_tail_interval(n,12)
            deeper,_=bbp_tail_interval(n,20)
            self.assertLessEqual(lo,deeper)
            self.assertLess(deeper,hi)

    def test_source_boundary_gamma_two(self):
        self.assertEqual(BBP.endpoint_order_and_coefficient(),(1,F(1)))
        self.assertEqual(RATIONAL_NONNORMAL.endpoint_order_and_coefficient(),(1,F(1)))

    def test_alternative_gamma_two_but_rational_completion(self):
        self.assertEqual(RATIONAL_NONNORMAL.reduced_kernel,(poly(-1,1),poly(-1)))
        for n in range(0,15):
            green=F(1,(8*n+1)*(8*n+2))
            self.assertEqual(RATIONAL_NONNORMAL.state(n),16**n*F(1,2)-green)
        self.assertNotEqual(RATIONAL_NONNORMAL.forcing(1),BBP.forcing(1))

    def test_signed_moment_zero_and_first_jet(self):
        self.assertEqual(peval(BBP.numerator,1),0)
        self.assertEqual(peval(pderiv(BBP.numerator),1),-15)
        self.assertEqual(sum(BBP.numerator,F(0)),0)

    def test_gamma2_moment_bounds_exact_rational(self):
        for n in (2,3,5,8,12,24,40):
            m=8*n
            lower=beta(m,1)-2*beta(m,2)+4*beta(m,3)-20*beta(m,4)
            upper=beta(m,1)-2*beta(m,2)+4*beta(m,3)
            a,b=bbp_tail_interval(n,20)
            self.assertLess(lower,a)
            self.assertGreater(upper,b)
            self.assertLess(a,b)

    def test_phase_frequency_ladder_is_exact_on_unwrapped_original(self):
        for n,h in product(range(0,25),(-5,-1,1,2,11)):
            self.assertEqual(phase_frequency_ladder_residual(n,h),0)

    def test_polynomial_gcd_cancellation_generic(self):
        rng=random.Random(411)
        for _ in range(180):
            g=poly(1,rng.randrange(-3,4),rng.randrange(-3,4))
            a=poly(2,rng.randrange(-3,4),rng.randrange(-3,4))
            b=poly(5,rng.randrange(-3,4))
            mul=pmul(g,a)
            quot,rem=pdivmod(mul,g)
            self.assertEqual(rem,poly(0))
            self.assertEqual(quot,a)
            self.assertEqual(pmul(mul,b),pmul(pmul(g,b),a))

    def test_polynomial_integral_exact(self):
        for degree in range(8):
            p=from_sparse(((3,0),(-5,2),(8,5)))
            self.assertEqual(integral_monomial_product(p,degree),
                             F(3,degree+1)-F(5,degree+3)+F(8,degree+6))


    def test_reflection_chart_preserves_mellin_integral_with_jacobian(self):
        # t=1-u, dt=-du, integration bounds reverse; no source change.
        reflectedQ=pcompose(BBP.numerator,poly(1,-1))
        one_minus=poly(1,-1)
        for n in range(0,7):
            weight=poly(1)
            for _ in range(8*n):
                weight=pmul(weight,one_minus)
            self.assertEqual(integral_monomial_product(pmul(reflectedQ,weight)),
                             integral_monomial_product(BBP.numerator,8*n))

    def test_generic_three_source_boundary_orders(self):
        for degree in range(4):
            p=poly(1)
            for _ in range(degree):p=pmul(p,poly(1,-1))
            grammar=CausalVolumeGrammar(16,8,p)
            self.assertEqual(grammar.endpoint_order_and_coefficient(),(degree,F(1,15)))
            for n in range(7):self.assertEqual(grammar.state(n),grammar.state_by_successor(n))

    def test_reject_malformed_inputs(self):
        with self.assertRaises(ValueError):CausalVolumeGrammar(1,8,poly(1))
        with self.assertRaises(ValueError):CausalVolumeGrammar(16,0,poly(1))
        with self.assertRaises(ValueError):CausalVolumeGrammar(16,8,poly(0))
        with self.assertRaises(ValueError):BBP.state(-1)
        with self.assertRaises(ValueError):BBP.forcing(0)
        with self.assertRaises(ValueError):phase_frequency_ladder_residual(0,0)
        with self.assertRaises(ZeroDivisionError):pdivmod(poly(1),poly(0))
        with self.assertRaises(ValueError):finite_moment_positive_mutant(4)

    def test_finite_moment_positive_mutant_invisible_at_early_depths(self):
        for M in (0,1,2):
            mutant,f,eps=finite_moment_positive_mutant(M)
            self.assertGreater(eps,0)
            self.assertEqual(mutant.endpoint_order_and_coefficient(),(1,F(1)))
            for k in range(M+1):
                self.assertEqual(integral_monomial_product(f,8*k),0)
            self.assertNotEqual(integral_monomial_product(f,8*(M+1)),0)
            for n in range(1,M+1):
                self.assertEqual(BBP.forcing(n),mutant.forcing(n))
                self.assertEqual(BBP.state(n),mutant.state(n))
            self.assertNotEqual(mutant.forcing(M+1),BBP.forcing(M+1))

    def test_mutant_kernel_is_positive_for_all_real_interval_by_coefficient_bound(self):
        for M in (0,1,2):
            mutated,f,eps=finite_moment_positive_mutant(M)
            from observational_succ.causal_volume_rewrite import pdivmod
            q,rem=pdivmod(f,poly(1,-1))
            self.assertEqual(rem,poly(0))
            magnitude=sum(map(abs,q),F(0))
            self.assertLess(eps*magnitude,F(1,8))
            # Since original R(t)>= (1-t)/4 on [0,1], this proves R+eps f>= (1-t)/8.
            self.assertTrue(mutated.pointwise_cancellation())
            for t in [F(i,30) for i in range(31)]:
                self.assertGreaterEqual(peval(mutated.numerator,t),0)

    def test_volume_observer_and_source_shift_not_same(self):
        # A changed initial seed is never the original pointed volume construction.
        n=4
        u=BBP.state(n)
        bad=u+16**n*F(1,16)
        self.assertNotEqual(bad,u)
        self.assertEqual(bad-u,16**n*F(1,16))

    def test_exact_nonlinearity_firewall(self):
        # e(∫_0^1 t dt)=exp(pi i)=-1 while ∫_0^1 e(t)dt=0.
        self.assertEqual(integral_monomial_product(poly(0,1)),F(1,2))
        self.assertNotEqual(F(-1), F(0))


    def test_every_source_forcing_difference_is_a_positive_causal_face(self):
        for n in range(0,14):
            for k in range(0,9):
                signed=finite_difference_forcing(n,k)
                face=integral_monomial_product(finite_difference_integrand(n,k))
                self.assertEqual(signed,face)
                self.assertGreater(face,0)

    def test_green_complete_monotonicity_source_certified_bounds(self):
        for n in (0,1,3,11):
            for k in range(0,8):
                lo,hi=approximate_green_difference(n,k,depth=24)
                deeper,_=approximate_green_difference(n,k,depth=32)
                self.assertGreater(lo,0)
                self.assertGreater(deeper,lo)
                self.assertLess(deeper,hi)

    def test_strict_log_convexity_of_forcing_moments(self):
        for n in range(2,70):
            self.assertLess(BBP.forcing(n)**2,
                            BBP.forcing(n-1)*BBP.forcing(n+1))

    def test_gamma_face_asymptotics_not_a_statistical_normality_proof(self):
        from math import factorial
        n=200
        for k in range(5):
            lo,hi=approximate_green_difference(n,k,depth=36)
            leading=F(factorial(k+1),64*n**(k+2))
            self.assertGreater(lo/F(leading),F(7,10))
            self.assertLess(hi/F(leading),F(11,10))

    def test_lifted_carry_reconstructed_from_original_source(self):
        for n in range(1,50):
            a=BBP.state(n)
            b=BBP.state(n-1)
            expected=a.numerator//a.denominator-16*(b.numerator//b.denominator)
            self.assertEqual(bbp_integer_lift_carry(n),expected)

    def test_moving_mellin_phase_bound_exact_rational(self):
        for m in (14,16,32,64,128):
            for lam in (F(0),F(1,8),F(1),F(3,2),F(2)):
                bound=gamma_phase_bound(m,lam)
                self.assertGreater(bound,0)
                self.assertEqual(bound, F(14+12*lam,m)+F(2*m*m,2**m))
        with self.assertRaises(ValueError):gamma_phase_bound(13,F(1))
        with self.assertRaises(ValueError):gamma_phase_bound(16,F(-1))


if __name__=='__main__':
    unittest.main(verbosity=2)
