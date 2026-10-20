"""Independent exact controls for the classical cloud harmonic bridge."""
from fractions import Fraction as F
from math import gcd, prod
import unittest

import sympy as sp

from observational_succ.cloud_ramanujan_transport import (
    divisor_clock_expansion, divisors, factorization, local_factor,
    mobius, modulus_enclosure, modulus_partial_sum, modulus_tail_bound,
    prime_product, prime_product_enclosure, primes_upto, ramanujan_sum,
    singular_coefficient, totient, unit_pair_density,
)


class CloudRamanujanTests(unittest.TestCase):
    def test_ramanujan_against_cyclotomic_character_reduction(self):
        # A separate route: sum the actual primitive characters in Q[z]/Phi_q.
        # No rounded complex numbers and no divisor-sum oracle in this route.
        z = sp.Symbol("z")
        for q in range(1, 41):
            phi = sp.Poly(sp.cyclotomic_poly(q, z), z, domain=sp.QQ)
            for N in range(-3, q + 3):
                polynomial = sum(z ** ((a * N) % q)
                                 for a in range(q) if gcd(a, q) == 1)
                reduced = sp.rem(sp.Poly(polynomial, z, domain=sp.QQ), phi)
                self.assertEqual(reduced.as_expr(), ramanujan_sum(q, N))

    def test_multiplicativity_and_evenness(self):
        for q in range(1, 22):
            for r in range(1, 22):
                for N in (-13, 0, 1, 6, 30):
                    self.assertEqual(ramanujan_sum(q, N), ramanujan_sum(q, -N))
                    if gcd(q, r) == 1:
                        self.assertEqual(ramanujan_sum(q * r, N),
                                         ramanujan_sum(q, N) * ramanujan_sum(r, N))

    def test_actual_units_against_harmonic_and_crt_routes(self):
        for q in range(1, 81):
            for N in range(-2, q + 2):
                brute = unit_pair_density(q, N)
                self.assertEqual(brute, divisor_clock_expansion(q, N))
                self.assertEqual(brute, prod(local_factor(p, N)
                                            for p, _ in factorization(q)))

    def test_finite_euler_expansion_over_squarefree_divisors(self):
        for P in (2, 3, 5, 7, 11):
            W = prod(primes_upto(P))
            for N in (0, 1, 2, 6, 10, 77, -210):
                self.assertEqual(prime_product(N, P), divisor_clock_expansion(W, N))

    def test_prime_cutoff_is_not_modulus_cutoff(self):
        self.assertEqual(prime_product(2, 3), F(3, 2))
        self.assertEqual(modulus_partial_sum(2, 3), F(7, 4))
        self.assertNotEqual(prime_product(2, 3), modulus_partial_sum(2, 3))

    def test_parity_and_nonconstant_goldbach_factor(self):
        for N in (1, 3, 21, -33):
            self.assertEqual(prime_product(N, 11), 0)
            self.assertEqual(modulus_enclosure(N, 5), (0, 0))
        for p in (3, 5, 7, 11):
            # S(2p)/(2*C2)=(p-1)/(p-2), not 1. Exact finite equality once p seen.
            self.assertEqual(prime_product(2 * p, 13) / prime_product(2, 13),
                             F(p - 1, p - 2))

    def test_unseen_divisor_can_reverse_naive_upper_bound(self):
        # At P=3, N=10: F_P=3/2; a certified lower bound at 101 exceeds it.
        coarse = prime_product(10, 3)
        refined = prime_product_enclosure(10, 101)
        self.assertGreater(refined.lower, coarse)
        repaired = prime_product_enclosure(10, 3)
        self.assertLessEqual(repaired.lower, refined.lower)
        self.assertGreaterEqual(repaired.upper, refined.upper)

    def test_no_residual_factorization_needed(self):
        N = 2 * 1000000007 * 1000000009
        cert = prime_product_enclosure(N, 11)
        self.assertEqual(cert.residual_after_small_primes, N // 2)
        self.assertGreaterEqual(cert.unseen_distinct_prime_count_bound, 2)
        self.assertGreater(cert.lower, 0)
        self.assertLess(cert.lower, cert.upper)

    def test_prime_enclosures_against_fresh_larger_products(self):
        for N in (-2, 6, 10, 14, 22, 2 * 13 * 17, 2 ** 12 * 19 ** 3):
            for P in (2, 3, 4, 5, 11, 29):
                cert = prime_product_enclosure(N, P)
                # A finite holdout, not a proof about the infinite product.
                larger = prime_product(N, 401)
                self.assertLessEqual(cert.lower, larger)
                self.assertGreaterEqual(cert.upper, larger)

    def test_totient_bound_independent_finite_audit(self):
        # The proof supplies the infinite tail; this catches arithmetic mutations.
        C = F(5, 2) * F(17, 12) * F(89, 80) * F(265, 252) * F(10, 7)
        self.assertLess(C, 6)
        for Q in (1, 2, 5, 17, 101):
            finite_tail = sum((F(1, totient(n) ** 2)
                               for n in range(Q + 1, 1001)), F())
            self.assertLessEqual(finite_tail, F(12, Q))

    def test_modulus_absolute_tails_and_independent_enclosure_overlap(self):
        for N in (1, 2, 6, 10, 30, -42, 2 * 101):
            for Q in (1, 3, 17, 61):
                partial_abs_tail = sum((abs(singular_coefficient(q, N))
                                        for q in range(Q + 1, 1001)), F())
                self.assertLessEqual(partial_abs_tail, modulus_tail_bound(N, Q))
            prime_cert = prime_product_enclosure(N, 101)
            lo, hi = modulus_enclosure(N, 401)
            self.assertLessEqual(lo, prime_cert.upper)
            self.assertGreaterEqual(hi, prime_cert.lower)

    def test_zero_is_finite_arithmetic_but_not_infinite_series(self):
        for q in range(1, 40):
            self.assertEqual(ramanujan_sum(q, 0), totient(q))
        for f, args in ((prime_product_enclosure, (0, 3)),
                        (modulus_tail_bound, (0, 3)), (modulus_enclosure, (0, 3))):
            with self.assertRaises(ValueError):
                f(*args)

    def test_inputs_and_squarefree_support(self):
        for q in (4, 8, 9, 12, 18, 25):
            self.assertEqual(singular_coefficient(q, 30), 0)
        for f, args in ((local_factor, (6, 10)), (local_factor, (True, 10)),
                        (ramanujan_sum, (0, 1)), (prime_product_enclosure, (2, 1)),
                        (prime_product_enclosure, (2, F(5, 2))),
                        (prime_product_enclosure, (2, 2.5)),
                        (prime_product_enclosure, (2, True)),
                        (modulus_tail_bound, (2, 0)), (ramanujan_sum, (3, 1.0)),
                        (totient, (0,)), (mobius, (-1,)), (divisors, (0,))):
            with self.assertRaises(ValueError):
                f(*args)


if __name__ == "__main__":
    unittest.main()
