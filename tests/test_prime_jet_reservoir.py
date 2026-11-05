"""Exact-source controls for a *mathematical* signed-prime-jet model.

The path operators are the prime terms of Weil's explicit formula. No
physical negative energy, RH, pi normality or full explicit-formula proof
is claimed by running these finite tests.
"""
import cmath
import itertools
import math
import unittest
from fractions import Fraction

import numpy as np


def chi4(n):
    if n % 2 == 0:
        return 0
    return 1 if n % 4 == 1 else -1


def chi2(a):
    return {1: 1, 3: -1, 5: -1, 7: 1}[a % 8]


def source_action(a, w):
    """Authenticated SUCC #499 source monomial S_a on rational 8-taps."""
    ans = []
    for l in range(1, 9):
        j = (a*l) % 8 or 8
        ans.append(chi2(a)**(8-l)*Fraction(2)**((j-l)//2)*w[j-1])
    return tuple(ans)


def original_forcing(n):
    return sum((Fraction(c, 8*(n-1)+j)
                for j, c in [(1, 4), (4, -2), (5, -1), (6, -1)]), Fraction())


def original_collapsed(n):
    return Fraction(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def graph(m):
    A = np.zeros((m, m))
    for j in range(m-1):
        A[j, j+1] = A[j+1, j] = 1.
    return A


def path_levels(m, weight):
    return sorted([-2*weight*math.cos(math.pi*j/(m+1)) for j in range(1, m+1)])


def fiber_sizes(length_ratio):
    """Positive-measure fiber lengths; the endpoint fiber has measure zero."""
    n = math.floor(length_ratio)
    if length_ratio == n:
        return [n] if n >= 1 else [1]
    return [m for m in (n, n+1) if m >= 1]


class TestPrimeJet(unittest.TestCase):
    def test_original_four_pole_exact(self):
        U = Fraction()
        for n in range(1, 40):
            self.assertEqual(original_forcing(n), original_collapsed(n))
            U = 16*U + original_forcing(n)
            self.assertEqual(U.denominator % 2, 1)

    def test_original_prime_character_eigensources(self):
        a = (Fraction(2), Fraction(2), Fraction(1), Fraction(),
             Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 4), Fraction())
        r = (Fraction(2), Fraction(-2), Fraction(-1), Fraction(-2),
             Fraction(-1, 2), Fraction(-1, 2), Fraction(1, 4), Fraction())
        o = (Fraction(4), Fraction(), Fraction(), Fraction(-2),
             Fraction(-1), Fraction(-1), Fraction(), Fraction())
        self.assertEqual(tuple(x+y for x,y in zip(a,r)), o)
        for p in (1,3,5,7):
            sign = chi4(p)
            self.assertEqual(source_action(p,a), tuple(sign*x for x in a))
            self.assertEqual(source_action(p,r), r)

    def test_exact_path_eigenvalue_formula(self):
        for m in range(1, 15):
            w = math.log(3)/math.sqrt(3)
            observed = sorted(np.linalg.eigvalsh(-w*graph(m)))
            np.testing.assert_allclose(observed, path_levels(m,w), atol=2e-14)
            self.assertAlmostEqual(observed[0], -observed[-1], places=12)

    def test_fiber_length_edge_conventions(self):
        self.assertEqual(fiber_sizes(1.), [1])
        self.assertEqual(fiber_sizes(1.2), [1, 2])
        self.assertEqual(fiber_sizes(2.), [2])
        self.assertEqual(fiber_sizes(2.3), [2, 3])
        self.assertEqual(fiber_sizes(4.), [4])
        self.assertEqual(fiber_sizes(4.5), [4, 5])
        w = math.log(2)/math.sqrt(2)
        for ratio in (1.2, 2., 2.3, 4., 4.5):
            m = max(fiber_sizes(ratio))
            predicted = 2*w*math.cos(math.pi/(m+1))
            self.assertAlmostEqual(max(abs(x) for x in path_levels(m,w)), predicted)

    def test_signed_packets_are_indefinite(self):
        for p in (2,3,5,7):
            w = math.log(p)/math.sqrt(p)
            J = -w*graph(2)
            for vector, expected in ((np.array([1.,1.])/math.sqrt(2),-w),
                                     (np.array([1.,-1.])/math.sqrt(2),w)):
                self.assertAlmostEqual(float(vector@J@vector), expected, places=13)
            self.assertAlmostEqual(float(np.trace(J)), 0, places=13)

    def test_prime_power_thresholds(self):
        # Prime-power jets enter the support only for k log(p) < 2L.
        # In particular p² must not be counted as soon as p appears.
        for length in (0.7, 1.1, 1.4, 2.5):
            actual = {(p, k) for p in (2, 3, 5, 7, 11)
                      for k in (1, 2, 3)
                      if k * math.log(p) < length}
            for p in (2, 3, 5, 7, 11):
                for k in (1, 2, 3):
                    w = math.log(p)/p**(k/2)
                    self.assertGreater(w, 0)
                    self.assertEqual((p, k) in actual, p**k < math.exp(length))
        self.assertIn((2, 1), {(p,k) for p in (2,) for k in (1,2)
                              if k*math.log(p) < 0.7})
        self.assertNotIn((2, 2), {(p,k) for p in (2,) for k in (1,2)
                                 if k*math.log(p) < 0.7})

    def test_rational_clock_2_primary_vs_odd(self):
        L = math.log(16)
        self.assertAlmostEqual(math.log(2)/L, 0.25, places=15)
        for p in (3,5,7,11):
            for q in range(1,9):
                self.assertNotEqual(p**q,16**q)
        for a,b,c in itertools.product(range(-2,3),repeat=3):
            if a == b == c == 0:
                continue
            prod = Fraction(2)**(4*a)*Fraction(3)**b*Fraction(5)**c
            self.assertNotEqual(prod, 1)

    def test_continuous_gauge_obstruction(self):
        previous = 9.
        for n in (1,2,10,100,1000,100000):
            delta = math.log((4*n+3)/(4*n+1))
            self.assertLess(delta, previous)
            self.assertEqual(chi4(4*n+3)*chi4(4*n+1), -1)
            self.assertGreater(delta, 0)
            previous = delta
        self.assertLess(previous, 1e-5)

    def test_lift_to_two_sheeted_arithmetic_fiber(self):
        L = math.log(16)
        def apply(p, v, eps):
            return ((v+math.log(p)) % L, eps*chi4(p))
        for p,q in ((3,5),(3,7),(5,11),(7,13)):
            v, eps = 0.317, -1
            after = apply(q,*apply(p,v,eps))
            other = apply(p,*apply(q,v,eps))
            self.assertAlmostEqual(after[0], other[0], places=12)
            self.assertEqual(after[1], other[1])
            self.assertAlmostEqual(after[0], (v+math.log(p*q)) % L, places=12)
            self.assertEqual(after[1], eps*chi4(p*q))

    def test_character_lift_vs_untwisted_local_levels(self):
        for p in (3,5,7,11):
            w=math.log(p)/math.sqrt(p)
            J=-w*graph(4)
            c=chi4(p)
            D=np.diag([c**j for j in range(4)])
            Jtw=D@J@D
            np.testing.assert_allclose(sorted(np.linalg.eigvalsh(J)),
                                       sorted(np.linalg.eigvalsh(Jtw)), atol=1e-14)
            self.assertAlmostEqual(Jtw[0,1],-w*c,places=13)

    def test_independent_packet_overlap_integral(self):
        # Two source-separated TRIANGULAR packets give a literal signed
        # Weil autocorrelation; integrator knows no graph eigenformula.
        import mpmath as mp
        mp.mp.dps = 45
        for p in (2, 3, 5):
            a = mp.log(p)
            eps = mp.mpf('0.04')
            c0 = mp.mpf('0.2')
            c1 = c0 + a
            def bump(x, c):
                return max(mp.mpf(0), 1 - abs(x-c)/eps)
            parts = sorted([mp.mpf(0), c0-eps, c0, c0+eps,
                            c1-eps, c1, c1+eps, c1+a+eps])
            for sign in (+1, -1):
                def f(x):
                    return bump(x, c0) + sign*bump(x, c1)
                overlap = mp.quad(lambda x: f(x)*f(x-a), parts)
                norm = mp.quad(lambda x: f(x)**2, parts)
                w = mp.log(p)/mp.sqrt(p)
                observed = -2*w*overlap/norm
                self.assertLess(abs(observed + sign*w), mp.mpf('1e-35'))

    def test_two_distinct_prime_clock_symbols(self):
        for p in (2,3,5):
            a=math.log(p)
            w=math.log(p)/math.sqrt(p)
            for k in (0., 0.27, 1.22):
                multiplier=-w*(cmath.exp(1j*a*k)+cmath.exp(-1j*a*k))
                self.assertAlmostEqual(multiplier.imag, 0, places=13)
                self.assertAlmostEqual(multiplier.real, -2*w*math.cos(a*k),places=13)


if __name__ == '__main__':
    unittest.main()
