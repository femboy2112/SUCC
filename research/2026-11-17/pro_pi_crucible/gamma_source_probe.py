"""Exact probes for a source-changing, zero-seeded shell countermodel.

This does not test or claim an asymptotic failure of R0 for original BBP.
Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import factorial
import unittest


POLES = ((0, 4), (3, -2), (4, -1), (5, -1))


def r(n):
    return F(4, 8*n-7) - F(2, 8*n-4) - F(1, 8*n-3) - F(1, 8*n-2)


def forcing_integral(n):
    # Independent monomial integration of t^(8n-8) Q(t).
    return sum((F(c, 8*n-7+j) for j, c in POLES), F())


def h(n, M):
    return r(n+M) - r(n+M+1)


def g(n, M):
    return 16*h(n, M) - h(n+1, M)


def kernel_integral_g(n, M):
    # (16-t^8)(1-t^8) = 16-17t^8+t^16.
    return sum((F(c*d, 8*(n+M)-7+j+k)
                for j, c in POLES
                for k, d in ((0, 16), (8, -17), (16, 1))), F())


def states(source, N):
    out = [F()]
    for n in range(1, N+1):
        out.append(16*out[-1] + source(n))
    return out


def ceil_fraction(v):
    return -(-v.numerator // v.denominator)


def clone(B, M):
    U = states(r, 2*B)
    P = U[-1]/16**(2*B)
    q = F(ceil_fraction(16**B*P), 16**B)
    delta = q-P
    eps = delta/h(1, M)
    source = lambda n: r(n) + eps*g(n, M)
    V = states(source, 2*B)
    a = eps*h(2*B+1, M)
    return U, V, q, delta, eps, a


def circle_distance(v):
    z = v - v.numerator//v.denominator
    return min(z, 1-z)


def wall_count(C, B):
    digits = [(C//16**k) % 16 for k in range(B)]
    D = sum(a not in (0, 15) for a in digits)
    J = sum({a, b} == {0, 15} for a, b in zip(digits, digits[1:]))
    return D, J


def leakage(z):
    return F(162, 289)*max(F(), circle_distance(z)-F(1, 18))**2


class PositiveSourceShellClone(unittest.TestCase):
    def test_original_and_perturbation_integrals(self):
        for M in (1, 2, 8):
            for n in range(1, 25):
                self.assertEqual(r(n), forcing_integral(n))
                self.assertEqual(g(n, M), kernel_integral_g(n, M))
                self.assertGreater(h(n, M), 0)
                self.assertGreater(g(n, M), g(n+1, M))

    def test_coboundary_total_and_tail_are_exact(self):
        for M in (1, 2, 8):
            for N in (1, 2, 7, 16, 31):
                partial = sum((g(n, M)/16**n for n in range(1, N+1)), F())
                self.assertEqual(partial, h(1, M)-h(N+1, M)/16**N)

    def test_zero_seed_full_history_and_terminal_block(self):
        for M in (1, 2, 8):
            for B in (1, 2, 4, 8, 16, 32, 64):
                U, V, q, delta, eps, a = clone(B, M)
                self.assertEqual(V[0], 0)
                self.assertGreaterEqual(delta, 0)
                self.assertLess(delta, F(1, 16**B))
                for n in range(0, 2*B+1):
                    self.assertEqual(V[n]-U[n], eps*(16**n*h(1, M)-h(n+1, M)))
                self.assertEqual(V[-1], 16**(2*B)*q-a)
                self.assertGreaterEqual(a, 0)
                self.assertLess(a, F(1, 16**B))
                C = V[-1].numerator//V[-1].denominator
                self.assertEqual(wall_count(C, B), (0, 0))
                self.assertEqual(C % 16**B, 16**B-1 if delta else 0)

    def test_exact_norm_and_zero_borwein_anchor(self):
        for B in (1, 2, 4, 8, 16, 32, 64):
            _, V, _, _, _, a = clone(B, 1)
            R = sum((circle_distance(V[-1]/16**k)**2 for k in range(1, B+1)), F())/B
            self.assertEqual(R, a*a*(1-F(1, 256**B))/(255*B))
            self.assertLess(R, F(1, 16**(2*B)*255*B))
            J = sum((leakage(V[-1]/16**k) for k in range(1, B+1)), F())/B
            self.assertEqual(J, 0)

    def test_sweep_is_far_from_haar(self):
        mean = F(256, 7803)
        for B in (1, 2, 4, 8, 16, 32):
            _, V, _, _, _, a = clone(B, 1)
            sweep = sum((leakage(V[-1]/16**k-F(1, 2)) for k in range(1, B+1)), F())/B
            lower = F(608, 7803)-F(144, 289)*a*(1-F(1,16**B))/(15*B)
            self.assertGreaterEqual(sweep-mean, lower)
            self.assertGreater(lower, F(3, 40))

    def test_all_four_weighted_pole_residues_preserved(self):
        for M in (1, 2, 8):
            _, _, _, _, eps, _ = clone(8, M)
            for R in (F(1, 2), F(-1, 4), F(-1, 8), F(-1, 8)):
                added = {M: 16*eps*R, M+1: -17*eps*R, M+2: eps*R}
                self.assertEqual(sum((16**j*c for j, c in added.items()), F()), 0)
                self.assertEqual(R+sum((16**j*c for j,c in added.items()), F()), R)

    def test_mellin_residue_changes_only_at_two_depths(self):
        for M in (1, 2, 8):
            # Weighted chronological completion of perturbation's pole stencil.
            for j in range(0, M+7):
                coefficient = sum((F(d, 16**(j-shift+1))
                                   for shift, d in ((M,16),(M+1,-17),(M+2,1))
                                   if j >= shift), F())
                self.assertEqual(coefficient, 1 if j == M else -1 if j == M+1 else 0)

    def test_uniform_relative_kernel_bound(self):
        # Finite calibration of universal product proof 0 <= A_M(t) <= 16.
        for M in (1, 2, 8):
            for j in range(65):
                t = F(j, 64)
                A = t**(8*M)*(16-t**8)*(1-t**8)
                self.assertGreaterEqual(A, 0)
                self.assertLessEqual(A, 16)

    def test_mutated_coboundary_is_rejected(self):
        M, N = 2, 11
        bad_partial = sum(((15*h(n,M)-h(n+1,M))/16**n for n in range(1,N+1)), F())
        self.assertNotEqual(bad_partial, h(1,M)-h(N+1,M)/16**N)
        # Mutating 16 to 15 breaks each invariant, as well as telescoping.
        self.assertNotEqual(15*16**M-16*16**(M+1)+16**(M+2), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
