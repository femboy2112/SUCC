from __future__ import annotations
import math
from fractions import Fraction
from unittest import TestCase, main
from carrier_probe import (
    generalized_binom, pascal_delta, pascal_polarization, vandermonde_signed, first_hex_digit, stirling2,
    hasse_difference_at_negative, zeta_negative_pascal, zeta_negative_stirling,
    zeta_negative_bernoulli, fibonacci_tiling_count, fibonacci,
    gamma_moment_from_pascal, primes_upto, mangoldt_terms, arch_prime_partial,
    arch_prime_tail_bound, bbp_r, bbp_r_grouped, bbp_u, bbp_tail_interval,
    bbp_digit_word, bbp_conjugacy_residual, theta_trunc, theta_tail_bound)

class CarrierExactTests(TestCase):
    def test_signed_pascal_integral(self):
        for n in range(-13,15):
            for k in range(0,12):
                self.assertEqual(generalized_binom(n,k), math.prod(n-j for j in range(k))//math.factorial(k))
    def test_pascal_difference_intertwining(self):
        for n in range(-15,30):
            for k in range(1,13):
                self.assertEqual(pascal_delta(k,n),generalized_binom(n,k-1))
    def test_pascal_level_zero(self):
        for n in range(-9,10):
            self.assertEqual(pascal_delta(0,n),0)
    def test_multiplication_polarization_all_signs(self):
        for a in range(-15,16):
            for b in range(-15,16):
                self.assertEqual(pascal_polarization(a,b),a*b)
    def test_signed_vandermonde_all_grades(self):
        for a in range(-7,9):
            for b in range(-7,9):
                for k in range(0,8):
                    self.assertEqual(vandermonde_signed(a,b,k), generalized_binom(a+b,k))
    def test_observer_one_digit_not_closed(self):
        a=Fraction(0)
        b=Fraction(1,256)
        self.assertEqual(first_hex_digit(a),first_hex_digit(b))
        self.assertNotEqual(first_hex_digit(16*a),first_hex_digit(16*b))
    def test_map_not_multiplicative(self):
        self.assertNotEqual(5*(5-1),5*5) # J(x^2)=x(x-1), J(x)^2=x^2
    def test_hasse_stirling_exact_differences(self):
        for m in range(0,13):
            for n in range(0,m+4):
                self.assertEqual(hasse_difference_at_negative(m,n),
                                 (-1)**n*math.factorial(n)*stirling2(m+1,n+1))
    def test_zeta_negative_three_independent_forms(self):
        for m in range(0,19):
            self.assertEqual(zeta_negative_pascal(m),zeta_negative_stirling(m))
            self.assertEqual(zeta_negative_pascal(m),zeta_negative_bernoulli(m))
    def test_zeta_minus_one(self):
        self.assertEqual(zeta_negative_pascal(1),Fraction(-1,12))
    def test_negative_even_zeta_zeros(self):
        for m in range(2,17,2):
            self.assertEqual(zeta_negative_pascal(m),0)
    def test_fibonacci_via_pascal(self):
        for n in range(0,100):
            self.assertEqual(fibonacci_tiling_count(n),fibonacci(n+1))
    def test_gamma_rank_moments(self):
        for r in range(1,12):
            for k in range(0,13):
                self.assertEqual(gamma_moment_from_pascal(r,k),math.prod(r+j for j in range(k)))
    def test_pisot_not_universal(self):
        self.assertLess(abs((1-math.sqrt(5))/2),1)
        self.assertGreater(abs((1-math.sqrt(13))/2),1)
    def test_fib_radix_239_obstruction(self):
        self.assertEqual(16*16-16-1,239)
    def test_mangoldt_primepowers(self):
        self.assertEqual(mangoldt_terms(25),[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13),(16,2),(17,17),(19,19),(23,23),(25,5)])
    def test_log_divisor_prime_decomposition(self):
        pairs=dict(mangoldt_terms(150))
        for n in range(1,151):
            lhs=sum(math.log(p) for d,p in pairs.items() if n%d==0)
            self.assertAlmostEqual(lhs,math.log(n),places=12)
    def test_prime_tail_bound_decreases(self):
        self.assertGreater(arch_prime_partial(2000),0.5)
        self.assertLess(arch_prime_tail_bound(20000),0.0006)
    def test_bbp_r_two_exact_schemes(self):
        for n in range(1,201):
            self.assertEqual(bbp_r(n),bbp_r_grouped(n))
            self.assertGreater(bbp_r(n),0)
    def test_bbp_first_state(self):
        self.assertEqual(bbp_u(1),Fraction(47,15))
    def test_bbp_tail_bounds_nest(self):
        for n in (0,1,2,4,12,70):
            for R in (2,3,5,10):
                a,b=bbp_tail_interval(n,R)
                c,d=bbp_tail_interval(n,R+1)
                self.assertLess(a,c)
                self.assertLess(d,b)
    def test_bbp_finite_conjugacy(self):
        for n in range(0,25):
            for R in (1,3,7):
                self.assertEqual(bbp_conjugacy_residual(n,R),0)
    def test_bbp_hex_prefix_without_pi_digits(self):
        self.assertEqual(bbp_digit_word(1,8,R=27),'243F6A88')
    def test_theta_poisson_truncation(self):
        for t in (0.25,0.37,1.0,2.7,4.0):
            M=12
            residual=abs(theta_trunc(t,M)-t**(-0.5)*theta_trunc(1/t,M))
            bound=theta_tail_bound(t,M)+t**(-0.5)*theta_tail_bound(1/t,M)
            self.assertLess(residual, max(2e-14,bound+2e-14))

if __name__=='__main__':
    main()
