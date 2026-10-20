"""Tests for observational_succ.abc_decomposition (Rigidity Forge Part VII, section 6).

Exact-arithmetic receipts for the prime-power layer anatomy (ABC-DEC-01), the
uniform per-layer convergence threshold / Cauchy-Schwarz ceiling (ABC-DEC-02),
and the machinery-boundary ledger (ABC-DEC-03).  A finite census is evidence,
never a proof of a uniform bound (AGENTS.md item 8).
"""
import unittest
from fractions import Fraction
from math import gcd

from observational_succ.abc_clock_families import prime_factors, radical, ris
from observational_succ.abc_decomposition import (
    bblt_anatomy,
    cauchy_schwarz_ceiling,
    census_anchor_S1,
    exponent_layers,
    inner_correlation_enclosure,
    layer_anatomy,
    layer_euler_product_converges,
    layer_mean_leading_exponent,
    local_ris_mean_factor_enclosure,
    machinery_boundary,
    max_exponent,
    ris_power_layer_factorization,
    uniform_layer_threshold,
)
from observational_succ.abc_triple_moment import integer_moment


class TestLayerAnatomyExact(unittest.TestCase):
    """ABC-DEC-01: n = prod m_j^j, rad = prod m_j, ris = prod m_j^{j-1}, exact."""

    def test_identity_holds_on_range(self):
        for n in range(1, 3000):
            cert = layer_anatomy(n)
            self.assertTrue(cert.identity_holds, f"anatomy identity failed at n={n}")
            self.assertEqual(cert.n_reconstructed, n)
            self.assertEqual(cert.radical_reconstructed, radical(n))
            self.assertEqual(cert.ris_reconstructed, ris(n))
            self.assertTrue(cert.pairwise_coprime)

    def test_layers_match_factorization(self):
        # e.g. 360 = 2^3 * 3^2 * 5  -> m_1=5, m_2=3, m_3=2
        self.assertEqual(exponent_layers(360), {3: 2, 2: 3, 1: 5})
        self.assertEqual(max_exponent(360), 3)
        self.assertEqual(exponent_layers(1), {})
        self.assertEqual(max_exponent(1), 0)

    def test_ris_power_factorization_product(self):
        # ris(n)^t = prod_{j>=2} m_j^{t(j-1)}; check the integer exponent t=1 case
        for n in (1, 2, 4, 8, 12, 72, 360, 1800, 2**5 * 3**3 * 7):
            layers = ris_power_layer_factorization(n, 1)
            prod = 1
            for _j, m, _e in layers:
                # t=1 so exponent is (j-1); rebuild m^(j-1)
                prod *= m ** _e.numerator  # _e = 1*(j-1) is integer Fraction
            self.assertEqual(prod, ris(n), f"ris factorization failed at n={n}")

    def test_bblt_tail_exact_when_bounded(self):
        # n0 = 1 exactly iff max exponent <= d (the eps0=0 case of BBLT Lemma 2.2)
        for n in range(1, 500):
            for d in (1, 2, 3, 6):
                res = bblt_anatomy(n, d)
                self.assertTrue(res["exact_when_bounded"])
                self.assertEqual(res["n0"] == 1, max_exponent(n) <= d)


class TestCensusAnchor(unittest.TestCase):
    """Reproduce the documented anchor S_1(24) = 557 two independent ways."""

    def test_anchor_557(self):
        res = census_anchor_S1(24)
        self.assertEqual(res["route_a_integer_moment"], 557)
        self.assertEqual(res["route_b_layer_product"], 557)
        self.assertTrue(res["agree"])

    def test_anchor_matches_module(self):
        self.assertEqual(census_anchor_S1(24)["route_a_integer_moment"],
                         integer_moment(24, 1, ordered=True))


class TestUniformLayerThreshold(unittest.TestCase):
    """ABC-DEC-02: every layer j>=2 has convergence threshold theta<1."""

    def test_leading_exponents(self):
        # layer-j leading exponent is (j-1)theta - j
        self.assertEqual(layer_mean_leading_exponent(2, Fraction(2, 5)),
                         Fraction(2, 5) - 2)              # theta - 2
        self.assertEqual(layer_mean_leading_exponent(3, Fraction(1, 2)),
                         2 * Fraction(1, 2) - 3)          # 2theta - 3

    def test_threshold_is_one_for_every_layer(self):
        thr = uniform_layer_threshold(20)
        self.assertEqual(thr["threshold"], Fraction(1))
        self.assertTrue(thr["uniform"])
        for j in range(2, 21):
            self.assertEqual(thr["per_layer"][j], Fraction(1))

    def test_convergence_boundary(self):
        # converges for theta<1, diverges at theta>=1, every layer j>=2
        for j in range(2, 10):
            self.assertTrue(layer_euler_product_converges(j, Fraction(9, 10)))
            self.assertFalse(layer_euler_product_converges(j, Fraction(1)))
            self.assertFalse(layer_euler_product_converges(j, Fraction(11, 10)))

    def test_cauchy_schwarz_ceiling(self):
        c = cauchy_schwarz_ceiling()
        self.assertEqual(c["ceiling_t"], Fraction(1, 2))
        self.assertFalse(c["bounded_exponent_helps"])


class TestLocalMeanEnclosure(unittest.TestCase):
    """E_p(theta) certified bracket; sanity against hand values."""

    def test_bracket_contains_and_narrow(self):
        # E_2(1/2) = (1/2)(1 + 2^{-1/2}/(2^{1/2}-1)).  2^{1/2} ~ 1.41421356
        lo, hi = local_ris_mean_factor_enclosure(2, Fraction(1, 2), precision=10 ** 12)
        self.assertLess(lo, hi)
        self.assertLess(hi - lo, Fraction(1, 10 ** 6))
        # independent float reference
        import math
        s = math.sqrt(2)
        ref = 0.5 * (1 + (1 / s) / (s - 1))
        self.assertLessEqual(float(lo), ref)
        self.assertGreaterEqual(float(hi), ref)

    def test_rejects_theta_ge_one(self):
        with self.assertRaises(Exception):
            local_ris_mean_factor_enclosure(3, Fraction(1))


class TestAdditiveCorrelation(unittest.TestCase):
    """ABC-DEC-03: exact inner correlation enclosure; honest census behaviour."""

    def test_integer_t_is_exact(self):
        # for integer t the enclosure collapses (lo == hi) and equals the direct sum
        for c in range(2, 40):
            lo, hi = inner_correlation_enclosure(c, 1)
            self.assertEqual(lo, hi)
            direct = sum(ris(a) * ris(c - a) for a in range(1, c) if gcd(a, c - a) == 1)
            self.assertEqual(lo, direct)

    def test_rational_t_bracket_valid(self):
        # the certified bracket must sandwich a high-precision float evaluation
        c, t = 30, Fraction(2, 5)
        lo, hi = inner_correlation_enclosure(c, t, precision=10 ** 9)
        ref = sum((ris(a) * ris(c - a)) ** (2 / 5) for a in range(1, c) if gcd(a, c - a) == 1)
        self.assertLessEqual(float(lo), ref + 1e-6)
        self.assertGreaterEqual(float(hi), ref - 1e-6)
        self.assertLess(hi - lo, Fraction(c))   # width < #terms * grid

    def test_machinery_boundary_ledger(self):
        m = machinery_boundary()
        self.assertFalse(m["beats_half_rigorously"])
        self.assertEqual(m["heuristic_true_threshold"], Fraction(1))
        self.assertEqual(m["abc_status"], "OPEN")
        self.assertIn("BBLT", m["needs_machinery_not_in_SUCC"])


if __name__ == "__main__":
    unittest.main()
