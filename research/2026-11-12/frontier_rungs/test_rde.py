#!/usr/bin/env python3
"""Unit tests for RESTRICTED_EXPONENT.md (RDT-01 ... RDT-08).

Only proved statements are asserted.  Everything is exact except real sizes, which are
evaluated with mpmath at a precision far above the scale of the quantities compared.
Nothing here tests, or could test, an asymptotic claim, and nothing bears on normality.
"""
from __future__ import annotations

import random
import sys
import unittest
from fractions import Fraction as F
from math import log, sqrt
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import rde_core as rc  # noqa: E402

mp.mp.dps = 700
PI, LOG2 = mp.pi, mp.log(2)


def mpf(x: F):
    return mp.mpf(x.numerator) / x.denominator


class TransferenceLemma(unittest.TestCase):
    """RDT-01: the inequality holds for EVERY form and EVERY m (theorem-grade)."""

    def test_random_forms_never_violate_the_lemma(self):
        rng = random.Random(20261112)
        consts = [PI, LOG2, mp.sqrt(2), mp.e, 1 / PI]
        checks = 0
        for _ in range(600):
            xi = rng.choice(consts)
            b = rng.choice([2, 3, 6, 10, 16])
            g = rng.choice([1, 1, 3, 15])
            den = rng.choice([1, 3, 7, 45, 2 ** rng.randint(0, 9), 5 * 2 ** rng.randint(0, 6)])
            scale = rng.choice([1, 2 ** rng.randint(0, 12), 3 ** rng.randint(0, 6), 6 ** rng.randint(0, 5)])
            A = F(rng.randint(1, 4000) * scale, rng.choice([1, 2, 4, 9]))
            # choose B so that the form is small (otherwise the lemma is silent)
            B = F(int(mp.nint(mpf(A) * xi * den * 10 ** 6)), den * 10 ** 6)
            if B == 0:
                continue
            I = abs(mpf(A) * xi - mpf(B))
            for m in range(0, 14):
                r = rc.transfer(A, B, I, b, m, g=g)
                self.assertEqual(r["H"].denominator, 1)                 # H is an integer
                if r["bound"] is None:
                    continue
                truth = rc.dist_to_int(g * mp.mpf(b) ** m * xi)
                self.assertGreaterEqual(truth, r["bound"] * (1 - mp.mpf(10) ** -200))
                checks += 1
        self.assertGreater(checks, 1500)

    def test_gain_is_exactly_the_S_adic_imbalance(self):
        # RDT-02(b): restricted H and Q equal the gcd-normalised ones divided by the imbalance.
        A, B = F(2 ** 9 * 35), F(1234567, 3 * 11)
        I = abs(mpf(A) * PI - mpf(B))
        rr = rc.transfer(A, B, I, 2, 40)
        ru = rc.transfer(A, B, I, 2, 40, mode="unrestricted")
        self.assertEqual(ru["H"] / rr["H"], 2 ** 9)
        self.assertAlmostEqual(float(ru["Q"] / rr["Q"]), 2.0 ** 9, places=6)

    def test_no_rescue_inequality(self):
        # RDT-02(c):  b^m Q_m >= E|I| / (E B)_S  for every m.
        rng = random.Random(7)
        for _ in range(200):
            b = rng.choice([2, 6, 16])
            primes = rc.prime_factors(b)
            A = F(rng.randint(1, 10 ** 6) * b ** rng.randint(0, 8), rng.randint(1, 50))
            B = F(rng.randint(1, 10 ** 6), rng.randint(1, 50) * b ** rng.randint(0, 5))
            I = mp.mpf(rng.random()) + mp.mpf("1e-9")
            E = rc.minimal_E(A, B, primes)
            floor_ = mpf(E) * I / mpf(rc.s_part(E * B, primes))
            for m in range(0, 30, 3):
                r = rc.transfer(A, B, I, b, m)
                self.assertGreaterEqual(r["bmQ"], floor_ * (1 - mp.mpf(10) ** -100))

    def test_mutation_overclaimed_unit_is_rejected(self):
        # xi_6 = sum 6^(-k!): at k = 2, m = 4 the true distance is about 1/9 and the lemma
        # is sharp; enlarging u by one factor b (the "mutant") claims about 2/9 and fails.
        xi = sum(mp.mpf(6) ** -mp.factorial(k) for k in range(1, 7))
        A, B = F(6 ** 2), F(6 + 1)
        I = mpf(A) * xi - mpf(B)
        good = rc.transfer(A, B, I, 2, 4)
        bad = rc.transfer(A, B, I, 2, 4, mode="mutant")
        truth = rc.dist_to_int(16 * xi)
        self.assertGreaterEqual(truth, good["bound"])
        self.assertLess(float(truth / good["bound"]), 1.01)              # sharp to 1%
        self.assertLess(truth, bad["bound"])                             # mutant rejected


class LiouvilleExample(unittest.TestCase):
    """RDT-02 example: xi_6 = sum 6^(-k!) has mu = infinity and v_2 <= log 3 / log 6."""

    def test_window_bounds(self):
        xi = sum(mp.mpf(6) ** -mp.factorial(k) for k in range(1, 7))
        for k in (2, 3, 4):
            kf = int(mp.factorial(k))
            A = F(6 ** kf)
            B = sum(F(6 ** (kf - int(mp.factorial(j)))) for j in range(1, k + 1))
            self.assertEqual(B % 6, 1)
            I = mpf(A) * xi - mpf(B)
            self.assertTrue(mp.mpf(6) ** (kf - int(mp.factorial(k + 1))) < I
                            < 2 * mp.mpf(6) ** (kf - int(mp.factorial(k + 1))))
            Mk = int(mp.floor(mp.factorial(k + 1) * mp.log(6, 2) - kf * mp.log(3, 2) - 2))
            for m in range(kf, min(Mk, 220) + 1):
                r = rc.transfer(A, B, I, 2, m)
                self.assertFalse(r["vanishing_possible"])
                self.assertEqual(r["H"], 3 ** kf)
                self.assertGreaterEqual(r["bound"], 1 / (2 * mp.mpf(3) ** kf))
                self.assertGreaterEqual(rc.dist_to_int(mp.mpf(2) ** m * xi),
                                        r["bound"] * (1 - mp.mpf(10) ** -200))


class TiltedLegendreLog2(unittest.TestCase):
    """RDT-05: every ingredient of the proof, on instances."""

    TRIPLES = [(1, 1, 1), (2, 4, 3), (4, 6, 5), (1, 2, 1), (2, 3, 2), (6, 8, 7), (3, 5, 4)]

    def test_form_integrality_valuations_savings_sizes(self):
        for (a, b, c) in self.TRIPLES:
            r = rc.log2_rates(a, b, c)
            for n in (1, 2, 3, 5):
                A, B = rc.log2_form(a, b, c, n)
                self.assertEqual(A.denominator, 1)
                I = mpf(A) * LOG2 - mpf(B)
                self.assertTrue(0 < I <= mp.e ** (-r["alpha"] * n) * LOG2)          # step 5
                self.assertLessEqual(abs(mpf(A)), mp.e ** (r["logR"] * n) * (1 + mp.mpf(10) ** -30))
                self.assertGreaterEqual(rc.vp(A, 2), (b - c) * n)                   # step 2
                Nst = max(a + b - c, c) * n
                self.assertGreaterEqual(rc.vp(B, 2), -log(Nst, 2) - 1e-9)
                D = rc.log2_Delta(a, b, c, n)                                       # step 3
                self.assertEqual(rc.odd_part((D * B).denominator), 1)
                for p in rc.log2_saved_primes(a, b, c, n):
                    self.assertEqual(A % p, 0)

    def test_saved_primes_exist_and_mutation(self):
        # a prime outside the saving set must NOT be removable in general
        a, b, c, n = 4, 6, 5, 12
        saved = rc.log2_saved_primes(a, b, c, n)
        self.assertEqual(saved, [23, 31])
        A, B = rc.log2_form(a, b, c, n)
        D = rc.log2_Delta(a, b, c, n)
        self.assertEqual(rc.odd_part((D * B).denominator), 1)
        self.assertNotEqual(rc.odd_part((F(D, 29) * B).denominator), 1)      # 29 is needed

    def test_rates_and_exponents(self):
        res, unr = rc.log2_exponent(1, 1, 1)
        self.assertAlmostEqual(res, 3.6221008, places=6)                    # classical, no tilt
        self.assertAlmostEqual(unr, res, places=12)
        # savings formula reproduces the Rukhadze-Hata value mu - 1 = 2.8914 for (6,8,7)
        res, unr = rc.log2_exponent_with_saving(6, 8, 7, J=400)
        self.assertAlmostEqual(unr, 2.8914, delta=3e-3)
        # the stated theorem: weights (4,6,5), rational saving s_60
        s60 = rc.log2_saving(4, 6, 5, 60)
        self.assertEqual(rc.log2_saving_segments(4, 6, 5),
                         [(F(1, 6), F(1, 5)), (F(1, 3), F(2, 5)), (F(1, 2), F(3, 5)), (F(3, 4), F(4, 5))])
        self.assertGreater(s60, F(1153, 1000))
        res, _ = rc.log2_exponent_with_saving(4, 6, 5, J=60)
        self.assertLess(res, 2.4104)
        self.assertGreater(res, 2.4076)
        r = rc.log2_rates(4, 6, 5)
        self.assertGreater(r["alpha"], r["Nstar"] - float(s60))              # classical criterion
        # headline weights (2,4,3): s_60 exact rational, exponent below 2.3814
        self.assertEqual(rc.log2_saving_segments(2, 4, 3), [(F(1, 4), F(1, 3)), (F(1, 2), F(2, 3))])
        self.assertGreater(rc.log2_saving(2, 4, 3, 60), F(7365, 10000))
        res, unr = rc.log2_exponent_with_saving(2, 4, 3, J=60)
        self.assertLess(res, 2.3814)
        self.assertGreater(res, 2.3766)
        self.assertGreater(unr, 3.38)                                        # same forms, unrestricted

    def test_symmetries_give_proportional_forms(self):
        pairs = [((7, 7, 8), (8, 6, 7)), ((7, 7, 8), (7, 7, 6)), ((7, 7, 8), (6, 8, 7)),
                 ((2, 4, 3), (3, 3, 2)), ((2, 4, 3), (4, 2, 3)), ((4, 6, 5), (5, 5, 4))]
        for t1, t2 in pairs:
            for n in (1, 2, 3):
                A1, B1 = rc.log2_form(*t1, n)
                A2, B2 = rc.log2_form(*t2, n)
                self.assertEqual(A1 * B2, A2 * B1)

    def test_certified_bounds_at_finite_n(self):
        a, b, c = 4, 6, 5
        for n in (1, 2, 3, 5, 8):
            A, B = rc.log2_form(a, b, c, n)
            I = mpf(A) * LOG2 - mpf(B)
            D = rc.log2_Delta(a, b, c, n)
            tau = (b - c) * n
            lam = int(log(5 * n, 2))
            H = F(D) * abs(A) / 2 ** tau
            self.assertEqual(H.denominator, 1)
            Q = mp.mpf(D) * I / 2 ** tau
            for m in range(tau + lam, tau + lam + 300):
                bq = mp.mpf(2) ** m * Q
                if bq >= 1:
                    break
                # E = Delta_n, u = 2^tau is admissible for m >= tau + lam (RDT-05, step 6)
                self.assertEqual((F(2) ** m * D * B / 2 ** tau).denominator, 1)
                self.assertGreaterEqual(rc.dist_to_int(mp.mpf(2) ** m * LOG2), min(bq, 1 - bq) / mpf(H))


class DalzellAndSeries(unittest.TestCase):
    def test_dalzell_coefficient_is_a_power_of_two(self):
        for (a, b) in ((1, 1), (2, 3), (1, 2)):
            for n in (1, 2, 3):
                A, B = rc.dalzell_form(a, b, n)
                self.assertEqual(A, F((-4) ** (b * n), 4))
                I = mpf(A) * PI + mpf(B)
                self.assertTrue(0 < I < mp.mpf(1) / 4 ** (4 * min(a, b) * n))
        A, B = rc.dalzell_form(1, 1, 1)
        self.assertEqual((A, B), (F(-1), F(22, 7)))

    def test_dalzell_weight_optimum(self):
        top = 4 * log(1 + sqrt(2))
        self.assertLess(top, 4)
        grid = max(rc.dalzell_criterion_value(i / 2000) for i in range(1, 2000))
        self.assertLessEqual(grid, top + 1e-12)
        self.assertAlmostEqual(rc.dalzell_criterion_value(sqrt(2) - 1), top, places=12)

    def test_series_self_certification_table(self):
        # criterion of RDT-04(a): s log 2 > d
        table = {"BBP four-pole": (4, 8), "Bellard": (10, 10), "log 2 = sum 1/(n 2^n)": (1, 1),
                 "log(16/15) = sum 1/(n 16^n)": (4, 1)}
        self.assertFalse(table["BBP four-pole"][0] * log(2) > table["BBP four-pole"][1])
        self.assertFalse(table["Bellard"][0] * log(2) > table["Bellard"][1])
        self.assertFalse(table["log 2 = sum 1/(n 2^n)"][0] * log(2) > 1)
        self.assertTrue(table["log(16/15) = sum 1/(n 16^n)"][0] * log(2) > 1)


class GaussianFamilies(unittest.TestCase):
    FAMS = [(2, 2, 0, 3), (1, 1, 0, 1), (1, 0, 0, 1), (1, 0, 2, 1), (2, 1, 2, 3), (1, 2, 0, 3), (3, 2, 0, 4)]

    def test_two_adic_shadow_lemma(self):
        # RDT-06(a): v_2(B_n) >= (2a - c/2) n - log_2(D n + 1) - 1/2
        for (a, mid, two, c) in self.FAMS:
            N = rc.gauss_poly(a, mid, two)
            D = len(N) - 1
            for n in (1, 2, 4, 6, 9, 12):
                A, B = rc.gauss_form(N, c, n)
                J = mpf(A) * PI / 2 + mpf(B)
                self.assertLess(abs(J), mp.mpf(4) ** n)                   # the form is the integral
                if B != 0:
                    self.assertGreaterEqual(rc.vp(B, 2), (2 * a - c / 2) * n - log(D * n + 1, 2) - 0.5)
                if A != 0 and c <= 2 * a:
                    self.assertGreaterEqual(rc.vp(A, 2), a * n - (c * n) // 2)

    def test_gaussian_saved_primes(self):
        # RDT-06(d): primes with 3*(2n mod p) < (3n mod p) divide A_n and drop out of B_n
        self.assertGreater(rc.gauss_saving(2, 2, 0, 3, 60), F(642, 1000))
        N = rc.gauss_poly(2, 2, 0)
        for n in (6, 10, 14, 18, 25):
            A, B = rc.gauss_form(N, 3, n)
            D = rc.odd_part(rc.lcm_upto(3 * n))
            for p in rc.gauss_saved_primes(2, 2, 0, 3, n):
                self.assertEqual(A % p, 0)
                D //= p
            self.assertEqual(rc.odd_part((D * B).denominator), 1)

    def test_lemma_on_pi_and_reciprocal_pi(self):
        N = rc.gauss_poly(2, 2, 0)
        for n in (4, 8, 12):
            A, B = rc.gauss_form(N, 3, n)
            J = abs(mpf(A) * PI / 2 + mpf(B))
            usable = 0
            for m in range(1, 160):
                r1 = rc.transfer(B, -A / 2, J / PI, 2, m)                 # form in 1/pi
                if r1["bound"] is not None:
                    usable += 1
                    self.assertGreaterEqual(rc.dist_to_int(mp.mpf(2) ** m / PI), r1["bound"])
                r2 = rc.transfer(A / 2, -B, J, 2, m)                      # form in pi
                if r2["bound"] is not None:
                    self.assertGreaterEqual(rc.dist_to_int(mp.mpf(2) ** m * PI), r2["bound"])
            self.assertGreater(usable, 5)


class RivoalImport(unittest.TestCase):
    def test_formula_reproduces_published_table(self):
        for (a, b, ref) in [(1, 2, 4.622103), (1, 3, 3.528776), (1, 4, 3.004521), (1, 12, 1.999208),
                            (1, 13, 1.963420), (-1, 2, 3.547470), (-1, 8, 2.211331), (1, 256, 1.407106),
                            (2, 61, 1.998995), (1, 31, 1.691777)]:
            self.assertAlmostEqual(rc.rivoal_Lambda(a, b)[0], ref, delta=3e-6)

    def test_lambda_at_sixteen(self):
        lam, kappa = rc.rivoal_Lambda(1, 16)
        self.assertAlmostEqual(lam, 1.881272, delta=2e-6)
        self.assertLess(lam, 2)
        self.assertGreater(rc.rivoal_Lambda(3, 128)[0], 2)               # log(125/128): not below 2
        self.assertGreater(rc.rivoal_Lambda(13, 256)[0], 2)              # log(243/256): not below 2

    def test_single_pole_source_is_log_16_over_15(self):
        # ZSC-06 convention: L(A) = sum_j A_j sum_{k>=0} 16^(-k-1)/(8k+j); A = 8 e_8
        s = sum(F(8, 16 ** (k + 1) * (8 * k + 8)) for k in range(120))
        self.assertAlmostEqual(float(mpf(s) - mp.log(mp.mpf(16) / 15)), 0.0, delta=1e-100)

    def test_pade_forms_and_multiplier(self):
        x = F(1, 16)
        xi = mp.log(mp.mpf(15) / 16)
        for (p, q) in [(3, 1), (11, 2), (22, 4), (33, 6)]:
            Bv, Av = rc.pade_log_form(p, q, x)
            self.assertEqual((Bv * 16 ** q).denominator, 1)
            self.assertEqual((Av * rc.lcm_upto(p) * 16 ** p).denominator, 1)
            R = mpf(Bv) * xi - mpf(Av)
            R2 = rc.pade_log_remainder_series(p, q, x)
            self.assertLess(abs(R - R2), abs(R2) * mp.mpf(10) ** -30)
            for g in (1, 15, 2, 4, 8):
                hits = 0
                for m in range(0, 80):
                    r = rc.transfer(Bv, Av, abs(R), 16, m, g=g)
                    if r["bound"] is None:
                        continue
                    hits += 1
                    self.assertGreaterEqual(rc.dist_to_int(g * mp.mpf(16) ** m * xi), r["bound"])
                self.assertGreater(hits, 2)


class ContinuedFractionDictionary(unittest.TestCase):
    def test_locality_both_directions_exact(self):
        rng = random.Random(3)
        for _ in range(4000):
            L = rng.randint(1, 6)
            j = rng.randint(0, 15)
            # a point whose first L digits are j, then arbitrary
            tail = F(rng.randrange(16 ** 4), 16 ** 4)
            y = sum(F(j, 16 ** i) for i in range(1, L + 1)) + tail / 16 ** L
            if y >= 1:
                continue
            d15 = abs(15 * y - round(15 * y))
            self.assertLessEqual(d15, F(max(j, 15 - j), 16 ** L))
            # converse: ||15 y|| < 16^(-L) forces L equal leading digits
            z = F(rng.randrange(1, 15 * 16 ** 7), 15 * 16 ** 7)
            dz = abs(15 * z - round(15 * z))
            Lz = 0
            while dz < F(1, 16 ** (Lz + 1)) and Lz < 6:
                Lz += 1
            digs = []
            w = z
            for _i in range(Lz):
                w *= 16
                digs.append(int(w))
                w -= int(w)
            self.assertLessEqual(len(set(digs)), 1)

    def test_two_convergent_decomposition(self):
        x = PI / 16
        a, conv = rc.cf_convergents(x, 60)
        self.assertEqual(a[:6], [0, 5, 10, 1, 3, 8])
        rng = random.Random(11)
        tested = dujella_violations = 0
        for _ in range(4000):
            q = rng.randint(1, 10 ** rng.randint(1, 9))
            for p in {int(mp.floor(q * x)), int(mp.ceil(q * x))}:
                if p < 0:
                    continue
                cq = q * abs(q * x - p)                    # |x - p/q| = cq / q^2
                if cq > 20:
                    continue
                m, r, s, t = rc.two_convergent_decomposition(p, q, x, a, conv)
                tested += 1
                # PROVED LOCAL (RDT-03(c)): min(r, t) * s < 2c(1 + 1/a_{m+2}) <= 4c
                self.assertLess(min(r, t) * s, 2 * cq * (1 + mp.mpf(1) / a[m + 2]))
                dujella_violations += int(min(r, t) * s >= 2 * cq)     # the imported sharper form
        self.assertGreater(tested, 1000)
        self.assertEqual(dujella_violations, 0)

    def test_legendre_regime(self):
        # a restricted approximation with q*||q x|| < 1/2 is a convergent (classical), and the
        # partial-quotient inequality of RDT-03(b) holds on the true convergents of pi/16
        x = PI / 16
        a, conv = rc.cf_convergents(x, 40)
        for k in range(1, 30):
            pk, qk = conv[k + 1]
            err = abs(qk * x - pk)
            self.assertLess(mp.mpf(1) / ((a[k + 1] + 2) * qk), err)
            self.assertLess(err, mp.mpf(1) / (a[k + 1] * qk))

    def test_L2_window_on_pi(self):
        # observational: no shell [B, 2B), 1 <= B <= 1500, of the hex expansion of pi/16 is change-free;
        # equivalently 15*16^B*||15*16^B x|| > 15/16 there (RDT-03(a)).  Not an asymptotic statement.
        mp.mp.dps = 4000
        try:
            d = rc.hex_digits(mp.pi / 16, 3050)
        finally:
            mp.mp.dps = 700
        longest = run = 1
        for i in range(1, len(d)):
            run = run + 1 if d[i] == d[i - 1] else 1
            longest = max(longest, run)
        self.assertLessEqual(longest, 5)


if __name__ == "__main__":
    unittest.main()
