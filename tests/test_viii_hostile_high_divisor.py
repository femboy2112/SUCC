"""Finite controls for the small-divisor theorem and cofactor counterfamily."""
from fractions import Fraction
from itertools import product
from math import gcd, prod
import unittest

from scripts.viii_hostile_high_divisor import (
    factor, finite_carrier_bound_intervals, g_at_one, g_interval, high_incidences,
    integer_root, powerful_divisors, power_interval, pythagorean_unit_cofactor,
)


class HighDivisorRefereeControls(unittest.TestCase):
    def test_small_divisor_slice_contains_unbalanced_deep_power_families(self):
        for r in range(3, 25):
            m = 2**r
            source = (9 * (2 * m + 9), m*m, (m + 9)**2)
            ds = (9, m*m, (m + 9)**2)
            self.assertEqual(source[0] + source[1], source[2])
            self.assertEqual(gcd(source[0], source[1]), 1)
            self.assertGreater(prod(ds), source[2]**2)
            self.assertEqual(min(ds), 9)
            self.assertEqual(factor(ds[1]), {2: 2 * r})

    def test_integer_root_intervals_are_certified(self):
        for n in range(1, 40):
            for exponent in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(5, 6)):
                low, high = power_interval(n, exponent, bits=20)
                self.assertLessEqual(low**exponent.denominator, n**exponent.numerator)
                self.assertGreaterEqual(high**exponent.denominator, n**exponent.numerator)
        self.assertEqual(integer_root(64, 3), 4)
        self.assertEqual(integer_root(63, 3), 3)

    def test_square_convolution_bound_at_and_beyond_two_thirds(self):
        for t in (Fraction(0), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(9, 10)):
            for Y in (4, 16, 64, 128):
                actual, bound = finite_carrier_bound_intervals(Y, t)
                # Certifies the comparison even with adversarial endpoint errors.
                self.assertLessEqual(actual[1], bound[0])

    def test_cofactor_fiber_has_unbounded_parameterized_multiplicity(self):
        sources = []
        for m in range(2, 42, 2):
            source, divisors, cofactors = pythagorean_unit_cofactor(m)
            a, b, c = source
            self.assertEqual(a + b, c)
            self.assertEqual(gcd(a, b), 1)
            self.assertEqual(cofactors, (1, 1, 1))
            self.assertGreater(prod(divisors), c*c)
            self.assertTrue(all(all(k >= 2 for k in factor(d).values()) for d in divisors))
            sources.append(source)
        self.assertEqual(len(set(sources)), 20)
        for M in (10, 20, 40):
            X = (4 * M*M + 1)**2
            common_fiber = [pythagorean_unit_cofactor(m)
                            for m in range(M, 2 * M + 1, 2)]
            self.assertEqual(len(common_fiber), M // 2 + 1)
            for source, ds, us in common_fiber:
                self.assertLessEqual(source[-1], X)
                self.assertGreater(prod(ds), X*X)
                self.assertEqual(us, (1, 1, 1))

    def test_actual_high_divisor_incidence_injects_into_each_relaxed_slot_sum(self):
        # t=1 is deliberately outside the theorem's convergent range. It
        # makes the finite transport weights integers; the injection itself
        # has no t<1 hypothesis and cannot conceal analytic convergence.
        for X in (25, 40, 70, 100):
            all_inc = list(high_incidences(X))
            for B in (4, 9, 16):
                for small_slot in range(3):
                    chosen = [inc for inc in all_inc if inc[1][small_slot] <= B]
                    keys = []
                    exact_weight = 0
                    for source, ds, us in chosen:
                        i, j = [k for k in range(3) if k != small_slot]
                        self.assertLess(us[i] * us[j], ds[small_slot])
                        key = (ds[small_slot], us[i], us[j], ds[i], ds[j])
                        keys.append(key)
                        exact_weight += prod(g_at_one(d) for d in ds)
                    self.assertEqual(len(keys), len(set(keys)))
                    relaxed = 0
                    for small in range(1, B + 1):
                        for v in range(1, small):
                            for w in range(1, (small - 1) // v + 1):
                                relaxed += g_at_one(small) * sum(g_at_one(e) for e in range(1, X // v + 1)) * sum(g_at_one(f) for f in range(1, X // w + 1))
                    self.assertLessEqual(exact_weight, relaxed)
                    for Q in (X*X, Fraction(3 * X*X, 2), 2 * X*X):
                        for source, ds, us in chosen:
                            if prod(ds) > Q:
                                i, j = [k for k in range(3) if k != small_slot]
                                self.assertLess(us[i] * us[j] * Q,
                                                ds[small_slot] * X*X)
                                self.assertGreater(min(ds) * X*X, Q)

    def test_prime_power_depth_invalidates_square_only_weight_majorant(self):
        # At t=1, g_1(2^k)=2^(k-2), exceeding (2^k)^(t/2)
        # once k>4. The theorem uses the cubic-and-deeper remainder h.
        self.assertGreater(g_at_one(2**6), 2**3)
        # Exact t=2/3 witness: g_t(2^8)=16(2^(2/3)-1).
        # g_t(2^8)> (2^8)^(t/2)=4*2^(2/3) iff 2^(2/3)>4/3.
        self.assertGreater(2**2, Fraction(4, 3)**3)
        self.assertGreater(g_interval(2**8, Fraction(2, 3))[0],
                           power_interval(2**8, Fraction(1, 3))[1])


if __name__ == '__main__':
    unittest.main()
