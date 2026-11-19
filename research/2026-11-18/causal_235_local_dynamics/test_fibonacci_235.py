import unittest
from fractions import Fraction
from fibonacci_235 import (A, B, M, S2, S4, S6, T, J, L, W, P, H,
                           identity, multiply, subtract, power, determinant,
                           symmetric_power_2, fibonacci, valuation,
                           matrix_valuation, monomials, source_norms,
                           forward_null, delayed_null)


def order_by_enumeration(a, modulus, cap):
    # Independent repeated multiplication; no prescribed order is assumed.
    value = identity(len(a))
    for n in range(1, cap+1):
        value = tuple(tuple(x % modulus for x in row)
                      for row in multiply(value, a))
        if value == identity(len(a)):
            return n
    raise AssertionError("enumeration cap was insufficient")


class Fibonacci235Tests(unittest.TestCase):
    def test_forward_lifts_and_integral_split(self):
        for x in range(-3, 4):
            for y in range(-3, 4):
                for degree in (2, 4):
                    self.assertEqual(multiply(symmetric_power_2(A, degree),
                                              monomials(x, y, degree)),
                                     monomials(x+y, x, degree))
        self.assertEqual(multiply(S6, J), multiply(J, S4))
        self.assertEqual(multiply(P, J), identity(5))
        self.assertEqual(multiply(J, P), subtract(identity(6), multiply(W, L)))
        self.assertEqual(multiply(S6, W), W)
        self.assertEqual(multiply(L, W), ((1,),))
        self.assertEqual(multiply(P, S6), multiply(S4, P))
        self.assertEqual(multiply(L, S6), L)

    def test_characteristic_and_trace_bridge(self):
        # Cayley-Hamilton without a symbolic/eigenvalue library.
        coefficients = (-1, 55, -385, 385, -55, 1)
        zero = [[0]*5 for _ in range(5)]
        for k, c in enumerate(coefficients):
            a = power(T, k)
            for i in range(5):
                for j in range(5):
                    zero[i][j] += c*a[i][j]
        self.assertEqual(zero, [[0]*5 for _ in range(5)])
        self.assertEqual(sum(T[i][i] for i in range(5)), fibonacci(10))
        self.assertEqual(determinant(T), 1)
        self.assertEqual(source_norms(1, 0), (55, 55))

    def test_prime_power_orders_independent_enumeration(self):
        for a in range(1, 9):
            expected = 3*2**max(a-3, 0)
            self.assertEqual(order_by_enumeration(T, 2**a, expected), expected)
        for b in range(1, 6):
            expected = 2*3**(b-1)
            self.assertEqual(order_by_enumeration(T, 3**b, expected), expected)
        for c in range(1, 4):
            expected = 5**c
            self.assertEqual(order_by_enumeration(T, 5**c, expected), expected)
        # A one-entry perturbation defeats the proposed base cycles.
        mutation = [list(row) for row in T]
        mutation[0][0] += 1
        self.assertNotEqual(power(mutation, 3, 2), identity(5))

    def test_local_near_returns_and_persistent_five_phase(self):
        for m in range(1, 5):
            n = 6**m
            difference = subtract(power(T, n), identity(5))
            self.assertEqual(matrix_valuation(difference, 2), m+3)
            self.assertEqual(matrix_valuation(difference, 3), m+1)
            self.assertEqual(power(T, n, 5), power(T, 1, 5))
            self.assertNotEqual(power(T, n, 5), identity(5))
            self.assertNotEqual(difference, tuple(tuple(0 for _ in range(5))
                                                  for _ in range(5)))

    def test_common_clock_fiber_product(self):
        from math import gcd, lcm
        for a in range(4, 7):
            for b in range(2, 5):
                u, v = 3*2**(a-3), 2*3**(b-1)
                self.assertEqual(gcd(u, v), 6)
                observed = {(n % u, n % v) for n in range(lcm(u, v))}
                compatible = {(i, j) for i in range(u) for j in range(v)
                              if (i-j) % 6 == 0}
                self.assertEqual(observed, compatible)
                self.assertEqual(6*len(observed), u*v)
                self.assertNotIn((0, 1), observed)

    def test_stride_norms_and_pentagon_collapse(self):
        for d in range(1, 20):
            for k in range(4):
                nf, n5 = source_norms(d, k)
                self.assertEqual(nf, 55*(-5*fibonacci(4*d)**2)**k)
                if d % 5:
                    self.assertEqual(n5, 55*5**k)
                    self.assertEqual(nf/n5, (-fibonacci(4*d)**2)**k)
                else:
                    self.assertEqual(n5, 55 if k == 0 else 0)

    def test_fibonacci_local_valuation_formula(self):
        for d in range(1, 251):
            f = fibonacci(4*d)
            self.assertEqual(valuation(f, 3), 1+valuation(d, 3))
            expected = 0 if d % 3 else valuation(d, 2)+4
            self.assertEqual(valuation(f, 2), expected)
        for m in range(1, 5):
            f = fibonacci(4*6**m)
            self.assertEqual(valuation(f*f, 2), 2*(m+4))
            self.assertEqual(valuation(f*f, 3), 2*(m+1))

    def test_mask_mutation_is_only_base_specific(self):
        mask = H[:-1]+(H[-1]+1,)
        f0, p0 = source_norms(1, 0, mask)
        self.assertNotEqual(f0, p0)
        for d in (1, 2, 3, 6):
            for k in (1, 2, 3):
                f, p = source_norms(d, k, mask)
                self.assertEqual(Fraction(f*p0, p*f0),
                                 (-fibonacci(4*d)**2)**k)

    def test_observation_latency(self):
        for n in range(1, 7):
            for d in (1, 2, 3, 6, 10):
                for k in range(5):
                    self.assertEqual(forward_null(n, d, k),
                                     delayed_null(n+d*k, d, k))
        with self.assertRaises(ValueError):
            delayed_null(5, 2, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
