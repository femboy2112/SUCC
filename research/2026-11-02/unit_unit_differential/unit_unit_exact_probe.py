#!/usr/bin/env python3
"""Exact original-BBP and coherent-shadow unit–unit SUCC differential probes.

Source and seed are fixed. All assertions use Python Fraction/integer arithmetic.
Finite tests calibrate but do not prove the PNT-AP all-n assertions in PROOFS.md.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, isqrt
import unittest


@lru_cache(None)
def source(n: int) -> Q:
    assert n >= 1
    return (Q(4, 8*n - 7) - Q(2, 8*n - 4)
            - Q(1, 8*n - 3) - Q(1, 8*n - 2))


@lru_cache(None)
def source_combined(n: int) -> Q:
    a = 8*n-7
    return Q(15*a*a + 121*a + 240, a*(a+3)*(a+4)*(a+5))


@lru_cache(None)
def original(n: int) -> Q:
    return Q(0) if n == 0 else 16*original(n-1) + source(n)


@lru_cache(None)
def finite_tail(n: int) -> Q:
    assert n >= 0
    return sum((source(n+j)/16**j for j in range(1, n+2)), Q(0))


@lru_cache(None)
def shadow(n: int) -> Q:
    return 16**n*Q(47, 240) - finite_tail(n)


def delta(f, n: int, order: int) -> Q:
    return sum(((-1)**(order-j) * comb(order,j) * f(n+j)
                for j in range(order+1)), Q(0))


def eta(n: int, order: int) -> Q:
    return (-1)**order * delta(finite_tail, n, order)


def prime(p: int) -> bool:
    return p >= 2 and all(p % t for t in range(2, isqrt(p)+1))


def born(p: int):
    assert p % 4 == 1 and p > 5
    return ((p+7)//8, 4) if p%8 == 1 else ((p+3)//8, -1)


def p_principal(fr: Q, p: int):
    """p*fr mod p when v_p(fr)=-1; otherwise return None."""
    if fr.denominator % p or fr.denominator % (p*p) == 0:
        return None
    return fr.numerator * pow(fr.denominator//p, -1, p) % p


def renormalize(f, n: int, iterations: int = 1) -> Q:
    assert iterations >= 0 and n >= 0
    power = 2**iterations
    return f(power*(n+1)-1)/16**((n+1)*(power-1))


def changed_source(n: int) -> Q:
    return (source(n) - source(2*n)/16**n
            - source(2*n+1)/16**(n+1))


class UnitUnitDifferential(unittest.TestCase):
    def test_exact_four_pole_source(self):
        for n in range(1, 181):
            self.assertEqual(source(n), source_combined(n))
        self.assertEqual(source(1), Q(47, 15))
        self.assertEqual(original(0), 0)
        self.assertEqual(shadow(0), 0)

    def test_newton_pascal_and_homogeneous_evaluation(self):
        for n in (1, 2, 5, 9, 15, 25):
            for d in range(1, 9):
                left = delta(original, n, d)
                right = 15**d * original(n)
                right += sum(15**(d-1-j) * delta(source, n+1, j)
                             for j in range(d))
                self.assertEqual(left, right)
                self.assertEqual(delta(shadow, n, d) +
                                 delta(finite_tail, n, d),
                                 15**d*16**n*Q(47, 240))
                self.assertEqual((15**d*16**n*Q(47, 240)).denominator, 1)

    def test_true_higher_unit_difference_prime_witness(self):
        checks=0
        for n in (12, 19, 27, 39, 53, 70):
            for d in sorted({1, 2, 3, n//5, n//2, (3*n)//4}):
                x=delta(original,n,d)
                for p in range(2*(n+d)+1,8*n):
                    if p%4!=1 or not prime(p): continue
                    j,c=born(p)
                    self.assertEqual(p_principal(x,p),
                                     c*pow(16,n-j,p)*pow(15,d,p)%p)
                    checks+=1
        self.assertGreater(checks,300)

    def test_shadow_higher_unit_difference_prime_witness(self):
        checks=0
        for n in (14, 20, 29, 41, 57, 72):
            for d in sorted({1, 2, 3, n//5, n//3, n//2}):
                x=delta(shadow,n,d)
                for p in range(8*(n+d+1)+1,16*n):
                    if p%4!=1 or not prime(p):continue
                    j,c=born(p)
                    self.assertEqual(p_principal(x,p),
                                     -c*pow(16,n-j,p)*pow(15,d,p)%p)
                    checks+=1
        self.assertGreater(checks,150)

    def test_positive_two_axis_pascal_lattice(self):
        for n in range(0, 24):
            for d in range(0, 22):
                self.assertGreater(eta(n,d), 0)
                self.assertEqual(eta(n,d), eta(n+1,d)+eta(n,d+1))
                self.assertLessEqual(eta(n,d+1), eta(n,d))
        for n in range(1, 80):
            self.assertLess(finite_tail(n), Q(1,(8*n+1)**2))

    def test_coherent_high_order_circle_phase_bound(self):
        for n in range(1, 35):
            for d in (1, 2, 3, 5, 8, 12, 24):
                diff=delta(shadow,n,d)
                homogeneous=15**d * 16**n * Q(47,240)
                self.assertEqual((homogeneous).denominator, 1)
                self.assertLessEqual(abs(diff-homogeneous),finite_tail(n))
                self.assertLess(abs(diff-homogeneous),Q(1,(8*n+1)**2))

    def test_nested_dyadic_blocks_are_exact(self):
        for n in range(0, 4):
            for depth in range(1, 6):
                got=sum((renormalize(finite_tail,n,j)
                         for j in range(depth)),Q(0))
                final=2**depth*(n+1)-1
                direct=sum((source(t)/16**(t-n)
                            for t in range(n+1,final+1)), Q(0))
                self.assertEqual(got,direct)
                # Exact block endpoints, not a limit of numerics.
                for j in range(depth):
                    low=2**j*(n+1)
                    high=2**(j+1)*(n+1)-1
                    blk=sum((source(t)/16**(t-n)
                             for t in range(low,high+1)),Q(0))
                    self.assertEqual(renormalize(finite_tail,n,j),blk)

    def test_unit_differential_renormalization_commutator(self):
        for n in range(0, 30):
            left=(renormalize(finite_tail,n+1)
                  -renormalize(finite_tail,n)
                  -renormalize(lambda j: finite_tail(j+1)-finite_tail(j),n))
            right= -changed_source(2*n+3)/16**(n+2)
            self.assertEqual(left,right)
            self.assertLess(right,0)

    def test_covariant_source_differential_erases_seed(self):
        for n in range(0, 40):
            self.assertEqual(original(n+1)-16*original(n),source(n+1))
            self.assertEqual(shadow(n+1)-16*shadow(n),changed_source(n+1))
            self.assertGreater(changed_source(n+1),0)

    def test_positive_shadow_moment_stirling_control(self):
        for n in (0, 1, 2, 3, 5, 8):
            for d in (0, 1, 2, 3, 5, 9, 16, 28):
                self.assertGreater(eta(n,d),0)
                self.assertLessEqual(eta(n,d), finite_tail(n))

if __name__ == "__main__":
    unittest.main(verbosity=2)
