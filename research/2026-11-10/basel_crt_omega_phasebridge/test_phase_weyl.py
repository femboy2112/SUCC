#!/usr/bin/env python3
"""Exact/focused controls for SUCC Basel × Ω frame-averaged Weyl bridge.

Stdlib only. No source/seed contract mutation. No asymptotic claims.
"""
import cmath
import math
import unittest
from fractions import Fraction


def original_R(j):
    if j < 0:
        raise ValueError(j)
    return (Fraction(4, 8*j + 1) - Fraction(2, 8*j + 4)
            - Fraction(1, 8*j + 5) - Fraction(1, 8*j + 6))


def prefix_pi_over_16(L):
    return sum((original_R(j) / 16**(j+1) for j in range(L)), Fraction(0))


def cayley_omega_C_pair(n):
    """Return exact C[n,n+1] in the *bulk* of the intrinsic p=2/3 graph.

    The matrix on six entries is independently constructed by tiny rational
    projection multiplication in the test. For n<6 this helper is invalid.
    """
    if n < 6:
        raise ValueError('bulk starts at 6')
    if n % 6 == 1:
        return Fraction(1, 6)
    if n % 6 == 3:
        return Fraction(-1, 6)
    return Fraction(0)


def frame_mass(n):
    if n < 11:
        raise ValueError('all 6 translated bulk windows must be available')
    return sum((18 * cayley_omega_C_pair(n-t)**2 for t in range(6)), Fraction(0))


def orbit_completed_common_horizon(n, seed, L):
    return 16**n * (seed + prefix_pi_over_16(L))


def original_bbp_recurrence_prefix(n):
    # Source-first U0=0, U_{j+1}=16 U_j+R(j).
    u = Fraction(0)
    for j in range(n):
        u = 16*u + original_R(j)
    return u


def gram_6():
    """Independent chronological matrices with exact Fractions (no sympy)."""
    def projection(p):
        a = [[Fraction(0) for _ in range(6)] for _ in range(6)]
        for first in range(0, 6, p):
            for i in range(first, first+p):
                for j in range(first, first+p):
                    a[i][j] = Fraction(1, p)
        return a
    p2, p3 = projection(2), projection(3)
    return [[sum(p2[i][k]*p3[k][j]-p3[i][k]*p2[k][j] for k in range(6))
             for j in range(6)] for i in range(6)]


def round_phase(q):
    # The modulo-1 reduction is exact, so floats only affect the final smoke check.
    q = q - math.floor(q)
    return cmath.exp(2j*math.pi*float(q))


class PhaseBridgeTests(unittest.TestCase):
    def test_exact_six_cell_nearest_neighbor_edges(self):
        c = gram_6()
        self.assertTrue(all(c[i][j] == -c[j][i] for i in range(6) for j in range(6)))
        self.assertEqual([c[i][i+1] for i in range(5)],
                         [Fraction(0), Fraction(1, 6), Fraction(0), Fraction(-1, 6), Fraction(0)])
        for n in range(6, 80):
            self.assertEqual(cayley_omega_C_pair(n), c[n%6][(n+1)%6]
                             if n%6 < 5 else Fraction(0))

    def test_six_translates_are_exact_partition_of_unity(self):
        for n in range(11, 400):
            self.assertEqual(frame_mass(n), 1)
            self.assertEqual(sum(bool(cayley_omega_C_pair(n-t)) for t in range(6)), 2)

    def test_genuine_bbp_poles_and_causal_weld(self):
        self.assertGreater(original_R(0), 0)
        self.assertGreater(original_R(20), 0)
        for n in range(0, 11):
            L = 15
            u = original_bbp_recurrence_prefix(n)
            # T_n^(L) is only the unresolved common-horizon tail.
            tail = sum((original_R(j) * Fraction(1, 16**(j-n+1))
                        for j in range(n, L)), Fraction(0))
            self.assertEqual(u+tail, 16**n * prefix_pi_over_16(L))

    def test_exact_real_lift_phase_and_weyl_identity(self):
        # Symbolic phase exponents; no floating point / no inference from digits.
        L = 28
        P = prefix_pi_over_16(L)
        for s in (Fraction(0), Fraction(3, 17), -P):
            for h in (1, 8, 24, -8):
                for n in range(11, 24):
                    y = orbit_completed_common_horizon(n, s, L)
                    y_next = orbit_completed_common_horizon(n+1, s, L)
                    self.assertEqual(Fraction(h, 15)*(y_next-y), h*y)
                    self.assertEqual(frame_mass(n)*h*y, h*y)

    def test_seed_and_wrong_seed_controls(self):
        L = 28
        P = prefix_pi_over_16(L)
        for n in range(11, 20):
            self.assertEqual(orbit_completed_common_horizon(n, -P, L), 0)
        self.assertNotEqual(orbit_completed_common_horizon(11, 0, L), 0)
        self.assertNotEqual(orbit_completed_common_horizon(11, Fraction(3,17), L), 0)

    def test_real_winding_cannot_be_dropped_before_rational_twist(self):
        # y_n=1/2, y_(n+1)=8 exactly satisfies y_(n+1)=16y_n.
        y, y1 = Fraction(1,2), Fraction(8)
        self.assertEqual(Fraction(1,15)*(y1-y), y)
        reduced_difference = Fraction(1,15)*((y1%1)-(y%1))
        self.assertEqual(reduced_difference, Fraction(-1,30))
        self.assertNotEqual((y-reduced_difference)%1, 0)

    def test_numerical_phase_sum_smoke_and_periodic_controls(self):
        L, A, h = 30, 12, 8
        p = prefix_pi_over_16(L)
        for s in (Fraction(0), Fraction(1, 29), -p):
            source = sum((round_phase(h*orbit_completed_common_horizon(n,s,L))
                         for n in range(A,2*A)), 0j) / A
            graph = sum((18 * cayley_omega_C_pair(n-t)**2 *
                         round_phase(Fraction(h,15) * (
                             orbit_completed_common_horizon(n+1,s,L)-
                             orbit_completed_common_horizon(n,s,L)))
                         for n in range(A,2*A) for t in range(6)), 0j) / A
            self.assertLess(abs(source - graph), 1e-13)
            if s == -p:
                self.assertLess(abs(graph - 1), 1e-13)

    def test_basel_weights_and_exact_height_compensation(self):
        A = 15
        w = [Fraction(1,n*n) for n in range(A,2*A)]
        Z_A = sum(w)
        self.assertGreater(Z_A,0)
        self.assertEqual(sum(w), Z_A)
        for n, wn in zip(range(A,2*A),w):
            # This identity compensates Gibbs n^-2 by a retained height n^2.
            self.assertEqual(wn*n*n, 1)
            self.assertEqual(18*sum(cayley_omega_C_pair(n-t)**2 for t in range(6)),1)

    def test_strict_source_tail_certificate_is_rational(self):
        # From R(j)=int x^(8j)(1-x)M(x) dx, 0<M(x)<15 for x<1.
        for L in (1,3,8,15):
            rhs = Fraction(1,16**L*(8*L+1)*(8*L+2))
            known_segment = sum((original_R(j)/16**(j+1)
                                 for j in range(L,L+36)), Fraction(0))
            self.assertGreater(known_segment, 0)
            self.assertLess(known_segment, rhs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
