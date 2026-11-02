"""Exhaustive cross-check tests for the π-normality arithmetic core.

Each primitive is verified against an INDEPENDENT representation, following the
repo's dual-certification discipline. stdlib only (Fraction, unittest). No
floating point in the arithmetic; the BBP identity is checked via high-precision
decimal comparison of exact rationals.

Run: python -m unittest research/2026-11-02/pi_normality_spine/test_arithmetic_core.py
"""
import unittest
from fractions import Fraction
from decimal import Decimal, getcontext

from arithmetic_core import (
    r, r_as_fm, U, U_direct, T, T_upper_bound,
    birth_index, primary_coeff, a_pj, kappa, W_pj, order16, Q_mN,
)

getcontext().prec = 120
PI = Decimal("3.14159265358979323846264338327950288419716939937510"
             "58209749445923078164062862089986280348253421170679"
             "82148086513282306647093844609550582231725359408128")


def dec(f: Fraction) -> Decimal:
    return Decimal(f.numerator) / Decimal(f.denominator)


class TestForcing(unittest.TestCase):
    def test_fm_decomposition(self):
        for n in range(1, 300):
            self.assertEqual(r(n), r_as_fm(n))

    def test_positivity_and_monotone(self):
        for n in range(1, 400):
            self.assertGreater(r(n), 0)
        for n in range(1, 200):
            self.assertGreater(r(n), r(n + 1))

    def test_asymptotic(self):
        # r(n) = 15/(64 n^2) + O(n^-3); check n^2 r(n) -> 15/64 from above
        for n in (1000, 5000):
            self.assertAlmostEqual(float(n*n * r(n)), 15/64, delta=0.02)


class TestOrbit(unittest.TestCase):
    def test_recurrence_equals_direct(self):
        for n in range(1, 60):
            self.assertEqual(U(n), U_direct(n))

    def test_recurrence_step(self):
        for n in range(1, 60):
            self.assertEqual(U(n + 1), 16 * U(n) + r(n + 1))

    def test_bbp_identity(self):
        # U_n + T_n = 16^{n-1} pi  (exact; residual = truncated pi)
        for n in (1, 2, 3, 5, 10, 20, 40):
            lhs = dec(U(n)) + dec(T(n))
            rhs = Decimal(16 ** (n - 1)) * PI
            self.assertLess(abs(lhs - rhs), Decimal("1e-40"))

    def test_tail_bound(self):
        for n in range(1, 120):
            self.assertGreater(T(n), 0)
            self.assertLess(T(n), T_upper_bound(n))

    def test_denominator_growth(self):
        # den(U_n) grows: den(U_10) > den(U_5) > den(U_1)
        self.assertGreater(U(5).denominator, U(1).denominator)
        self.assertGreater(U(10).denominator, U(5).denominator)


class TestPrimeCofiber(unittest.TestCase):
    def test_birth_and_coeff(self):
        self.assertEqual(birth_index(13), 2)   # 5 mod 8
        self.assertEqual(birth_index(17), 3)   # 1 mod 8
        self.assertEqual(primary_coeff(13), -1)
        self.assertEqual(primary_coeff(17), 4)

    def test_cofiber_p_integral(self):
        for p in (13, 29, 37, 53, 61, 101, 149, 197):
            if p % 8 != 5:
                continue
            b = birth_index(p)
            for j in range(b, (p + 1) // 2):
                self.assertNotEqual(W_pj(p, j).denominator % p, 0)

    def test_primary_residue_consistency(self):
        # a_{p,j} = c_p 16^{j-b_p} mod p; verify via recurrence a_{p,j+1} = 16 a_{p,j} mod p
        for p in (13, 17, 29, 37):
            b = birth_index(p)
            for j in range(b, b + 20):
                self.assertEqual(a_pj(p, j + 1), (16 * a_pj(p, j)) % p)

    def test_carry_range(self):
        for p in (13, 17, 29, 37, 53):
            b = birth_index(p)
            for j in range(b, b + 30):
                self.assertIn(kappa(p, j), range(16))

    def test_carry_recurrence(self):
        # W_{p,j+1} = 16 W_{p,j} + r(j+1) + kappa_{p,j}   (PCN-01)
        for p in (13, 29, 37, 53):
            if p % 8 != 5:
                continue
            b = birth_index(p)
            for j in range(b, b + 8):
                lhs = W_pj(p, j + 1)
                rhs = 16 * W_pj(p, j) + r(j + 1) + kappa(p, j)
                self.assertEqual(lhs, rhs)

    def test_midy_complementarity(self):
        # p=1 mod 8 with even L: a_{p,j+M} = p - a_{p,j}, kappa_j + kappa_{j+M} = 15
        p = 97  # L = 12, M = 6
        M = 6
        b = birth_index(p)
        for j in range(b, b + 6):
            self.assertEqual(a_pj(p, j + M), p - a_pj(p, j))
            self.assertEqual(kappa(p, j) + kappa(p, j + M), 15)


class TestOrder(unittest.TestCase):
    def test_order_divides_p_minus_1(self):
        for p in (13, 17, 29, 37, 53, 61, 97, 101, 109, 257):
            self.assertEqual((p - 1) % order16(p), 0)

    def test_order_5mod8_odd(self):
        # p=5 mod 8: ord_p(16) odd (PCN-16)
        for p in (13, 29, 37, 53, 61, 101, 109, 149):
            if p % 8 == 5:
                self.assertEqual(order16(p) % 2, 1)


class TestCollisionEnergy(unittest.TestCase):
    def test_debruijn(self):
        # order-2 de Bruijn cycle (16-ary) has Q_1 = Q_2 = 1
        # build a 16-ary order-2 de Bruijn via the FKM algorithm
        def debruijn(k, n):
            a = [0] * (k * n + 1)
            seq = []
            def db(t, p):
                if t > n:
                    if n % p == 0:
                        seq.extend(a[1:p+1])
                else:
                    a[t] = a[t-p]; db(t+1, p)
                    for j in range(a[t-p]+1, k):
                        a[t] = j; db(t+1, t)
            db(1, 1)
            return seq
        cyc = debruijn(16, 2)
        # words length 1 and 2
        w1 = cyc[:256]
        w2 = [cyc[i]*16 + cyc[(i+1) % 256] for i in range(256)]
        self.assertEqual(Q_mN(w1, 1), 1)
        self.assertEqual(Q_mN(w2, 2), 1)

    def test_all_zero_saturates(self):
        w = [0]*64
        self.assertEqual(Q_mN(w, 2), 16**2)

    def test_sampling_floor(self):
        # Q_{m,N} >= 16^m / N
        w = [i % 16 for i in range(100)]
        for m in (1, 2, 3):
            self.assertGreaterEqual(Q_mN(w[:100], m), Fraction(16**m, 100))


if __name__ == "__main__":
    unittest.main(verbosity=2)
