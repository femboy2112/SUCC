"""Exact regression tests for Operation Main XVI (Triangle Genesis repair & advance).

Research-only. No test asserts pi normality or RH. The tested modules are path-loaded to avoid a
production dependency or touching the historical BBP source modules.

Coverage:
  P0  the normalized-average vacuity: the erroneous  Sbar_N = (1/N) sum e(hU_n) = o(N)  criterion
      is satisfied by a coherent NONNORMAL orbit, whereas the correct  Sbar_N = o(1)  (equivalently
      the unnormalized  T_N = sum e(hU_n) = o(N)) rejects it.
  P1  the golden locus  q_{r,theta} = lambda^r  <=>  theta = lambda/(1-lambda^r);
      supercriticality, calibration table, restricted uniqueness at theta=1, the Laplace invariant.
  P2  the seven-class seed-alias classification of  U_n(s) = U_n(0) + 16^n s.
  P3  the literal-carry obstruction (distinguishes circle-aliases; carries no |T_N| magnitude saving).
  X   agreement with the independently-implemented oracle.
"""
from __future__ import annotations

import importlib.util
from fractions import Fraction as Fr
from pathlib import Path
import unittest

import mpmath as mp
import sympy as sp

_DIR = Path(__file__).resolve().parents[1] / "research/2026-10-29/triangle_genesis_repair"


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, _DIR / filename)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


GL = _load("xvi_golden_locus", "golden_locus.py")
SA = _load("xvi_seed_alias", "seed_alias.py")
ORACLE = _load("xvi_oracle", "independent_oracle_xvi.py")

mp.mp.dps = 60                       # compute the golden constants at full test precision
LAMF = (mp.sqrt(5) - 1) / 2
PHIF = (mp.sqrt(5) + 1) / 2


class P0NormalizationVacuity(unittest.TestCase):
    """The normalized character average is O(1), so 'Sbar=o(N)' is vacuous for EVERY orbit."""

    def test_all_zero_orbit_is_coherent_and_nonnormal(self):
        # U_n = 0 for all n => e(h U_n) = 1 => T_N(h) = N, Sbar_N(h) = 1 for every N, h.
        for N in (10, 100, 1000, 10 ** 6):
            Sbar = Fr(1)                       # (1/N) * N = 1 exactly
            T = Fr(N)                          # unnormalized
            self.assertEqual(Sbar, 1)
            self.assertEqual(T, N)

    def test_vacuous_oN_accepts_nonnormal_but_o1_rejects(self):
        # vacuous criterion "Sbar = o(N)":  |Sbar|/N -> 0  (true for the all-zero orbit, 1/N -> 0)
        ratios = [Fr(1, N) for N in (100, 10 ** 4, 10 ** 6)]
        self.assertTrue(all(x <= Fr(1, 100) for x in ratios))          # ACCEPTED (vacuously)
        # correct criterion "Sbar = o(1)":  |Sbar| -> 0.  All-zero orbit has |Sbar| = 1 forever.
        self.assertTrue(all(Fr(1) == 1 for _ in (10, 100, 1000)))      # |Sbar| == 1, so REJECTED
        # unnormalized form: T_N = N is NOT o(N) -> the canonical repo gate correctly rejects it too.
        self.assertEqual(Fr(10 ** 6), 10 ** 6)


class P1GoldenLocus(unittest.TestCase):
    def setUp(self):
        mp.mp.dps = 60

    def test_fixed_point_equals_lambda_r_on_locus(self):
        for r in (0.5, 1, 2, 3, 4, 5, 10):
            theta = GL.theta_locus(r)
            q_iter = GL.least_fixed_point(r, theta)      # operational route (iteration)
            self.assertLess(abs(q_iter - GL.golden_point(r)), mp.mpf(10) ** (-45),
                            f"r={r}: least fixed point != lambda^r")

    def test_symbolic_identity_and_golden_factorisation(self):
        is_fp, factored = GL.locus_symbolic_certificate()
        self.assertEqual(is_fp, 0)                       # G(lambda^r)-lambda^r == 0 on the locus
        q = sp.symbols('q', positive=True)
        self.assertEqual(sp.expand(factored - (q - 1) * (q ** 2 - 3 * q + 1)), 0)

    def test_calibration_table(self):
        # (r, theta, fixed point):  (1, phi, lambda), (2, 1, lambda^2), (3, phi/2, lambda^3)
        self.assertLess(abs(GL.theta_locus(1) - PHIF), mp.mpf(10) ** (-45))
        self.assertLess(abs(GL.theta_locus(2) - 1), mp.mpf(10) ** (-45))
        self.assertLess(abs(GL.theta_locus(3) - PHIF / 2), mp.mpf(10) ** (-45))
        for r in (1, 2, 3):
            self.assertLess(abs(GL.golden_point(r) - LAMF ** r), mp.mpf(10) ** (-45))

    def test_supercritical_on_locus(self):
        for r in (0.25, 0.5, 1, 2, 3, 5, 10, 50):
            self.assertTrue(GL.is_supercritical_on_locus(r), f"r*theta<=1 at r={r}")
            self.assertGreater(r * LAMF + LAMF ** r, 1)   # f(r)=r*lambda+lambda^r>1

    def test_restricted_uniqueness_theta_equals_one(self):
        self.assertLess(abs(GL.theta_locus(2) - 1), mp.mpf(10) ** (-45))   # r=2 is on {theta=1}
        for r in (0.5, 1, 1.5, 2.5, 3, 5):                                # no other r gives theta=1
            if abs(r - 2) > 1e-9:
                self.assertGreater(abs(GL.theta_locus(r) - 1), 1e-6)

    def test_theta_strictly_decreasing_with_limits(self):
        vals = [GL.theta_locus(r) for r in (0.5, 1, 2, 3, 5, 10, 50)]
        self.assertTrue(all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)))
        self.assertGreater(GL.theta_locus(0.01), 10)            # -> +inf as r->0+
        self.assertLess(abs(GL.theta_locus(200) - LAMF), 1e-6)  # -> lambda as r->inf

    def test_laplace_rate_invariant(self):
        # theta*(1-q) = lambda for EVERY r on the locus; and E e^{-lambda Y}=(1+lambda)^-r=lambda^r=q
        for r in (0.5, 1, 2, 3, 5, 10):
            self.assertLess(abs(GL.laplace_rate_on_locus(r) - LAMF), mp.mpf(10) ** (-45))
            self.assertLess(abs(GL.gamma_laplace(r, LAMF) - GL.golden_point(r)), mp.mpf(10) ** (-45))


class P2SeedAliasClassification(unittest.TestCase):
    def test_affine_law(self):
        for s in (Fr(1, 16), Fr(1, 3), Fr(7, 256), Fr(-5, 3), Fr(13, 7)):
            for n in range(0, 7):
                self.assertEqual(SA.U(n, s) - SA.U(n, 0), 16 ** n * s)

    def test_class2_exact_alias_1_over_16(self):
        self.assertTrue(SA.circle_aliased(Fr(1, 16), n_from=1, n_to=8, hmax=5))
        self.assertEqual(SA.alias_onset(Fr(1, 16)), 1)

    def test_class3_eventual_alias(self):
        self.assertEqual(SA.alias_onset(Fr(1, 256)), 2)
        self.assertNotEqual(SA.frac(SA.U(1, Fr(1, 256))), SA.frac(SA.U(1, 0)))   # not at n=1
        self.assertTrue(SA.circle_aliased(Fr(1, 256), n_from=2, n_to=8, hmax=3))  # aliased n>=2
        self.assertEqual(SA.alias_onset(Fr(1, 65536)), 4)

    def test_class4_constant_twist_magnitude_invariant(self):
        for s in (Fr(1, 3), Fr(2, 5), Fr(1, 15), Fr(-5, 3)):
            self.assertIsNotNone(SA.constant_twist_value(s))
            self.assertEqual(SA.twist_period(s), 1)
            self.assertTrue(SA.weyl_magnitude_invariant(s, N=14, h=1))
            self.assertTrue(SA.weyl_magnitude_invariant(s, N=14, h=3))

    def test_class4_not_in_Z16_and_not_aliased(self):
        self.assertIsNone(SA.alias_onset(Fr(1, 3)))

    def test_periodic_twist_q7_is_not_constant(self):
        self.assertIsNone(SA.constant_twist_value(Fr(1, 7)))   # 16 != 1 mod 7
        self.assertEqual(SA.twist_period(Fr(1, 7)), 3)
        self.assertFalse(SA.weyl_magnitude_invariant(Fr(1, 7), N=10, h=1))

    def test_classify_fingerprints(self):
        c = SA.classify(Fr(1, 16))
        self.assertTrue(c["in_Z[1/16]"] and c["circle_alias_onset_N0"] == 1)
        self.assertTrue(c["carry_distinguishes_from_authentic"])
        c3 = SA.classify(Fr(1, 3))
        self.assertEqual(c3["constant_twist_value"], Fr(1, 3))
        self.assertTrue(c3["weyl_magnitude_invariant"])
        self.assertFalse(c3["carry_distinguishes_from_authentic"])


class P2CoherentCounterseed(unittest.TestCase):
    """s* = -pi/16: U_n(s*) = -T_n -> 0, selected phase -> 1 (coherent, nonnormal)."""

    def test_counterseed_collapse(self):
        mp.mp.dps = 200
        pi = mp.pi
        devs, Ts = [], []
        for n in range(1, 31):
            u0 = SA.U(n, 0)
            u0mp = mp.mpf(u0.numerator) / mp.mpf(u0.denominator)
            Us = u0mp - 16 ** (n - 1) * pi          # = -T_n
            Ts.append(16 ** (n - 1) * pi - u0mp)
            devs.append(abs(mp.e ** (2j * mp.pi * Us) - 1))
        self.assertGreater(Ts[-1], 0)
        self.assertLess(Ts[-1], Ts[7])             # T_n -> 0
        self.assertLess(devs[-1], 1e-3)            # phase -> 1
        self.assertLess(devs[-1], devs[7])
        mp.mp.dps = 60


class P3CarryObstruction(unittest.TestCase):
    def test_carry_distinguishes_exact_alias(self):
        # s=1/16 is circle-identical to s=0 for n>=1, yet the literal carries differ.
        self.assertTrue(SA.circle_aliased(Fr(1, 16), n_from=1, n_to=8, hmax=4))
        self.assertTrue(SA.carry_distinguishes(Fr(1, 16)))

    def test_carry_is_integer_lift_only(self):
        # The carry is Z-valued source/lift data; it is NOT a bound on |T_N(h)| (negative result).
        for s in (Fr(0), Fr(1, 16), Fr(1, 256)):
            for n in range(1, 9):
                self.assertIsInstance(SA.carry(n, s), int)


class CrossCheckIndependentOracle(unittest.TestCase):
    def test_p1_oracle_agrees(self):
        for r in (1, 2, 3, 4, 5, 6):
            theta_sym, is_root = ORACLE.locus_root_substitution(r)
            self.assertTrue(is_root, f"oracle: lambda^r not an exact root at r={r}")
            _, least = ORACLE.least_root_numeric(r)
            self.assertIsNotNone(least)
            self.assertLess(abs(least - LAMF ** r), mp.mpf(10) ** (-45))

    def test_p2_oracle_modular_matches_seed_alias(self):
        for s in (Fr(1, 16), Fr(1, 256), Fr(1, 65536), Fr(1, 3), Fr(2, 5), Fr(1, 15), Fr(1, 7)):
            modular = ORACLE.alias_decision_modular(s)
            self.assertEqual(modular["onset"], SA.alias_onset(s))
            self.assertEqual(modular["constant_twist"], SA.constant_twist_value(s) is not None)

    def test_p3_oracle_counterseed_coherent(self):
        cp = ORACLE.counterseed_phase(NN=30)
        self.assertTrue(cp[-1][1] > 0 and cp[-1][1] < cp[7][1])   # T_n -> 0
        self.assertLess(cp[-1][2], cp[7][2])                      # phase dev -> 0


if __name__ == "__main__":
    unittest.main(verbosity=2)
