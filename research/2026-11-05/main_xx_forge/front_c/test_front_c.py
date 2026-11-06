"""Focused tests for Front C (< 60 s).  Run:
    PYTHONPATH=<checkout> python -m unittest research/2026-11-05/main_xx_forge/front_c/test_front_c.py
mpmath precision is only ever changed inside local mp.workdps(...) blocks.
"""
import json
import math
import os
import sys
import unittest
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import front_c_probe as P  # noqa: E402


def _lcg(seed):
    while True:
        seed = (1103515245 * seed + 12345) % (1 << 31)
        yield seed / float(1 << 31)


class Shared:
    N = 2 * 512 + 80
    X, C, _ = P.exact_orbit(P.ORIG_TAPS, N)
    Tk = P.tail_fixed(P.ORIG_TAPS, N)


class TestInstrument(unittest.TestCase):
    def test_lcm_recurrence_matches_fraction(self):
        U = P.fraction_orbit(P.ORIG_TAPS, 200)
        for n in range(201):
            fl = U[n].numerator // U[n].denominator
            self.assertEqual(Shared.X[n], ((U[n] - fl) * P.ONE).__floor__())
            if n:
                fl0 = U[n - 1].numerator // U[n - 1].denominator
                self.assertEqual(Shared.C[n], fl - 16 * fl0)

    def test_tail_CC01_bounds(self):
        for n in range(1, 400):
            d = F(P.ONE, 64 * n * n) - Shared.Tk[n]
            self.assertTrue(-2 < d < F(P.ONE, 64 * n ** 3) + 2)

    def test_source_hex_digits_are_pi(self):
        # carries of the zero-seeded source give hex digits of pi/16 = 0.3243f6a8885a308d...
        fu = 0
        for n in range(1, 17):
            fu = 16 * fu + Shared.C[n]
        self.assertEqual(format(fu, "x"), "3243f6a8885a308d")


class TestC1(unittest.TestCase):
    A = 256

    def setUp(self):
        A = self.A
        self.idx = range(A, 2 * A)
        self.xT = [Shared.X[n] for n in self.idx]
        self.xC = [(P.ONE - Shared.Tk[n]) & P.MASK for n in self.idx]

    def test_partial_summation_and_exact_duality(self):
        for h in (1, 3):
            terms, _, smax = P.weyl_stats(self.xT, h)
            g = _lcg(7 + h)
            for _ in range(20):
                a = [next(g) * 2 - 1 for _ in self.idx]
                st = P.mixed_stats(a, terms, smax)
                self.assertTrue(st["bv_holds"])
            # the unit V-ball is the hull of initial step weights: equality is attained
            S, best, Lbest = 0j, 0.0, 0
            for L, t in enumerate(terms, start=1):
                S += t
                if abs(S) > best:
                    best, Lbest = abs(S), L
            step = [1.0 if i < Lbest else 0.0 for i in range(self.A)]
            V = abs(step[-1]) + sum(abs(step[i + 1] - step[i]) for i in range(self.A - 1))
            self.assertEqual(V, 1.0)
            self.assertAlmostEqual(abs(sum(s * t for s, t in zip(step, terms))), smax, places=9)

    def test_carry_identity_and_coherent_carries(self):
        X, Tk, C = Shared.X, Shared.Tk, Shared.C
        for n in self.idx:
            e0 = X[n] + Tk[n] >= P.ONE
            e1 = X[n + 1] + Tk[n + 1] >= P.ONE
            d = ((X[n] + Tk[n]) & P.MASK) >> (P.K - 4)
            self.assertEqual(C[n + 1], d + 16 * e0 - e1)
        for i, n in enumerate(self.idx):
            r1 = P.r_orig(n + 1)
            self.assertEqual((16 * self.xC[i] + (r1.numerator << P.K) // r1.denominator) >> P.K, 15)

    def test_frontB_CB1_interval_form(self):
        X = Shared.X
        for n in self.idx:
            Sk = P.r_orig(n + 1)
            Sd = 16 * P.r_orig(n + 1) + P.r_orig(n + 2)
            Sm = P.r_orig(n + 2)
            self.assertLess(Sd, 1)
            theta = (X[n] << 8) & P.MASK
            dl = 16 * Sk
            dl -= dl.numerator // dl.denominator
            b_def = theta + (dl.numerator << P.K) // dl.denominator >= P.ONE
            y = X[n + 2]
            b_int = (Sm.numerator << P.K) // Sm.denominator <= y < (Sd.numerator << P.K) // Sd.denominator
            self.assertEqual(b_def, b_int)

    def test_coherent_collapse_and_rotation(self):
        TA = [Shared.Tk[n] / P.ONE for n in self.idx]
        a = [math.log(8 * n - 7) if len(P.factor(8 * n - 7, P.sieve_spf(16 * self.A))) == 1 else 0.0
             for n in self.idx]
        for h in (1, 3):
            tC, _, _ = P.weyl_stats(self.xC, h)
            M = sum(x * y for x, y in zip(a, tC)) / self.A
            R = sum(a) / self.A
            bound = 2 * math.pi * h * sum(abs(x) * t for x, t in zip(a, TA)) / self.A
            self.assertLessEqual(abs(M - R), bound + 1e-12)
            tT, _, _ = P.weyl_stats(self.xT, h)
            xR = [(v + P.ONE // 5) & P.MASK for v in self.xT]
            tR, _, _ = P.weyl_stats(xR, h)
            rot = complex(math.cos(2 * math.pi * h / 5), math.sin(2 * math.pi * h / 5))
            self.assertLess(abs(sum(x * y for x, y in zip(a, tR)) - rot * sum(x * y for x, y in zip(a, tT))), 1e-8)


class TestC2(unittest.TestCase):
    def test_group_law_and_dims(self):
        basis = [tuple(F(int(i == j)) for i in range(8)) for j in range(8)]
        for a in (1, 3, 5, 7):
            for b in (1, 3, 5, 7):
                for e in basis:
                    self.assertEqual(P.S_op(a, P.S_op(b, e)), P.S_op((a * b) % 8, e))
        dims = {ch: len(P.isotypic_basis(ch)) for ch in P.CHARS}
        self.assertEqual(dims, {"1": 4, "chi_-4": 2, "chi_8": 1, "chi_-8": 1})

    def test_period_kernel_is_radial_line_and_misses_chi_minus4(self):
        ker = P.nullspace(P.period_matrix_rows(), 8)
        self.assertEqual(len(ker), 1)
        v = ker[0]
        scale = v[0] / 8
        self.assertEqual(tuple(x / scale for x in v), tuple(map(F, (8, -8, -4, -8, -2, -2, 1, 0))))
        self.assertEqual(P.rank_of(ker + [P.RAD_TAPS]), 1)
        self.assertEqual(P.span_intersection(P.isotypic_basis("chi_-4"), ker), [])
        for a in (3, 5, 7):
            self.assertEqual(P.rank_of(ker + [P.S_op(a, ker[0])]), 1)

    def test_baker_identities_numeric_local_precision(self):
        import mpmath
        before = mpmath.mp.dps
        out = P.baker_numeric_check()
        self.assertEqual(mpmath.mp.dps, before)
        self.assertLess(out["max_log_identity_error"], 1e-40)
        self.assertAlmostEqual(out["orig"]["I_over_pi"], 1.0, places=12)
        self.assertAlmostEqual(out["sharp"]["I_over_pi"], 2.0, places=12)
        self.assertLess(abs(out["radial"]["I_direct"]), 1e-40)

    def test_chi_minus4_periods_are_pi_and_arctan_half(self):
        import mpmath
        before = mpmath.mp.dps
        e1, e2 = P.isotypic_basis("chi_-4")
        with mpmath.workdps(40):
            p1 = mpmath.mpf(P.period_numeric(e1, 40))
            p2 = mpmath.mpf(P.period_numeric(e2, 40))
            self.assertLess(abs(p1 - (mpmath.pi / 8 - mpmath.atan(0.5) / 4)), 1e-14)
            self.assertLess(abs(p2 - mpmath.atan(0.5) / 2), 1e-14)
        self.assertEqual(mpmath.mp.dps, before)

    def test_shadow_seed_blindness_and_visibility(self):
        Uo = P.fraction_orbit(P.ORIG_TAPS, 2 * 43 + 1)
        Um = P.fraction_orbit(P.MUT_TAPS, 2 * 43 + 1)
        for k, primes in ((1, (11, 13, 17, 19, 23, 29, 31, 37, 41, 43)), (2, (17, 19, 23, 29, 31, 37, 41, 43))):
            for p in primes:
                if p <= 8 * k:
                    continue
                a = p % 8
                rhs = P.fraction_orbit(P.S_op(a, P.ORIG_TAPS), k)[k]
                rhs = (rhs.numerator * pow(rhs.denominator, -1, p)) % p
                lhs = P.residue_pU(Uo[k * p], p)
                self.assertEqual(lhs, rhs)
                self.assertEqual(P.residue_pU(Uo[k * p] + F(16) ** (k * p) / 5, p), lhs)
                rm = P.fraction_orbit(P.S_op(a, P.MUT_TAPS), k)[k]
                self.assertEqual(P.residue_pU(Um[k * p], p), (rm.numerator * pow(rm.denominator, -1, p)) % p)
                self.assertEqual((P.residue_pU(-Uo[k * p], p) + lhs) % p, 0)
        self.assertNotEqual(P.residue_pU(Uo[13] + F(16) ** 13 / 13, 13), P.residue_pU(Uo[13], 13))

    def test_reflection_conjugates_weyl(self):
        neg = tuple(-x for x in P.ORIG_TAPS)
        Xn, _, _ = P.exact_orbit(neg, 400)
        for n in range(200, 400):
            self.assertEqual((Xn[n] + Shared.X[n]) % P.ONE in (0, P.ONE - 1), True)
        self.assertEqual(P.proj("chi_-4", neg), tuple(-x for x in P.proj("chi_-4", P.ORIG_TAPS)))


class TestC3(unittest.TestCase):
    A = 256

    def _orbits(self):
        A = self.A
        idx = range(A, 2 * A)
        zT = [(Shared.X[n] + Shared.Tk[n]) & P.MASK for n in idx]
        digs = P.base15_digits_sqrt2(2 * A + 70)
        cur = 0
        for kk in range(1, 65):
            cur = (cur << 4) | digs[A + kk - 1]
        z15 = []
        for n in idx:
            z15.append(cur)
            cur = ((cur << 4) & P.MASK) | digs[n + 64]
        fu = 0
        for n in range(1, 62):
            fu = 16 * fu + Shared.C[n]
        k61 = fu + (1 if Shared.X[61] + Shared.Tk[61] >= P.ONE else 0)
        M61 = 16 ** 61 - 1
        cur = (k61 * pow(16, A, M61)) % M61
        zPS = []
        for n in idx:
            zPS.append((cur << P.K) // M61)
            cur = (cur * 16) % M61
        return {"TRUE": zT, "COH": [0] * A, "FIFTEEN": z15, "PER_SHORT": zPS}, digs

    def test_single_scale_lemma(self):
        orbs, _ = self._orbits()
        A = self.A
        for name, pts in orbs.items():
            for delta in (A ** -0.5, 4.0 / A):
                B = (P.pair_counts(pts, [P.W_of(2 * delta) + 8])[0] + A) / A ** 2
                for h in (1, 3):
                    J = int(math.floor(math.log(1.0 / (4 * delta * h), 16))) + 1
                    _, c, _ = P.weyl_stats(pts, h)
                    bound = (math.pi / 2) * math.sqrt(max(B / (2 * delta) - 1, 0) / (2 * J)) + 2 * (J - 1) / A
                    self.assertLessEqual(abs(c), bound + 1e-12, name)

    def test_microscopic_exclusion_is_shared_by_nonnormal_fifteen(self):
        orbs, digs = self._orbits()
        A = self.A
        self.assertNotIn(15, digs)
        W = [P.W_of(A ** -2.5), P.W_of(A ** -3.0)]
        self.assertEqual(P.pair_counts(orbs["FIFTEEN"], W), [0, 0])
        self.assertEqual(P.pair_counts(orbs["TRUE"], W), [0, 0])
        xC = [(P.ONE - Shared.Tk[n]) & P.MASK for n in range(A, 2 * A)]
        self.assertEqual(P.pair_counts(xC, [P.W_of(1.0 / (64 * A * A))])[0], A * (A - 1))
        self.assertGreaterEqual(P.pair_counts(orbs["PER_SHORT"], [0])[0], A * A // 61 - A)

    def test_coherent_gap_bound_and_GPB2_occupancy(self):
        A = self.A
        for n in range(A, 2 * A):
            self.assertGreater(Shared.Tk[n] - Shared.Tk[n + 1] + 4, P.ONE / (128 * n ** 3))
        xC = [(P.ONE - Shared.Tk[n]) & P.MASK for n in range(A, 2 * A)]
        w = A ** -2.0 * math.log(A) ** -4
        self.assertLessEqual(P.max_occupancy(xC, P.W_of(w)), 1 + 1024 * w * A ** 3)


class TestReceipt(unittest.TestCase):
    def test_receipt_flags_and_exact_values(self):
        path = os.path.join(HERE, "FINITE_RECEIPT.json")
        with open(path) as fh:
            rec = json.load(fh)
        fl = rec["preregistered_flags"]
        failed = sorted(k for k, v in fl.items() if not v)
        self.assertEqual(failed, ["P-C3-2_fifteen_c1_band"])   # recorded failure, not refit
        self.assertEqual(rec["C2"]["ker_I_dim"], 1)
        self.assertEqual(rec["C2"]["ker_I_basis"], [["8", "-8", "-4", "-8", "-2", "-2", "1", "0"]])
        sh = rec["C2"]["frobenius_shadow"]
        self.assertEqual(sh["orig_pass"], sh["eligible_pk"])
        self.assertEqual(sh["rot_shadow_equals_true"], sh["eligible_pk"])
        self.assertTrue(rec["no_pi_digits_input"])
        for A in rec["C3"]:
            self.assertEqual(rec["C3"][A]["z:FIFTEEN:pairs"]["A^-2.5"], 0)
            self.assertEqual(rec["C3"][A]["fifteen_digitF_count_in_window"], 0)


if __name__ == "__main__":
    unittest.main()
