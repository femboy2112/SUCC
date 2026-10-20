"""Exact tests for observational_succ.abc_triple_moment (Moonshot D).

Every assertion is integer/Fraction-exact.  No float is used as a certificate:
bracket containment is checked with exact rational arithmetic (``lo**den <=
base**num <= hi**den``), and all constants/ratios are compared as Fractions.
"""
import unittest
from collections import Counter
from fractions import Fraction
from math import gcd

from observational_succ import abc_triple_moment as m
from observational_succ.abc_clock_families import ABCClockError, ris


class IntegerRootTests(unittest.TestCase):
    def test_floor_root_exact_cases(self):
        self.assertEqual(m.integer_root(1000, 3), 10)   # 10^3 = 1000
        self.assertEqual(m.integer_root(999, 3), 9)
        self.assertEqual(m.integer_root(1024, 10), 2)   # 2^10 = 1024
        self.assertEqual(m.integer_root(1023, 10), 1)
        self.assertEqual(m.integer_root(0, 5), 0)
        self.assertEqual(m.integer_root(1, 7), 1)

    def test_floor_root_property_random_ish(self):
        for n in (2, 7, 50, 81, 10 ** 6, 2 ** 40 + 5):
            for k in (2, 3, 5, 7):
                r = m.integer_root(n, k)
                self.assertLessEqual(r ** k, n)
                self.assertGreater((r + 1) ** k, n)

    def test_integer_root_guards(self):
        with self.assertRaises(ABCClockError):
            m.integer_root(-1, 2)
        with self.assertRaises(ABCClockError):
            m.integer_root(10, 0)


class PowerEnclosureTests(unittest.TestCase):
    def test_bracket_contains_true_value_exactly(self):
        # Exact (no float): lo**den <= base**num <= hi**den.
        for base, num, den in [(32, 2, 5), (7, 3, 4), (2, 1, 5), (1000, 7, 3)]:
            lo, hi = m.power_enclosure(base, num, den, 10 ** 6)
            self.assertLessEqual(lo ** den, Fraction(base) ** num)
            self.assertLessEqual(Fraction(base) ** num, hi ** den)
            self.assertEqual(hi - lo, Fraction(1, 10 ** 6))

    def test_integer_exponent_is_exact(self):
        lo, hi = m.power_enclosure(13, 2, 1, 10 ** 3)
        self.assertEqual(lo, Fraction(169))          # exact 13^2, point bracket
        self.assertEqual(hi, Fraction(169))

    def test_returns_fractions_not_floats(self):
        lo, hi = m.power_enclosure(5, 2, 3, 10 ** 4)
        self.assertIsInstance(lo, Fraction)
        self.assertIsInstance(hi, Fraction)


class TripleRisAndGuardsTests(unittest.TestCase):
    def test_two_routes_agree(self):
        for a, b in [(1, 1), (1, 2), (5, 27), (169, 343), (1, 511), (4, 121)]:
            c = a + b
            if gcd(a, b) != 1:
                continue
            self.assertEqual(m.triple_ris(a, b, c), m.ris_product_direct(a, b, c))
            self.assertEqual(m.triple_ris(a, b, c), ris(a) * ris(b) * ris(c))

    def test_known_values(self):
        # (169,343,512): ris=13*49*256=163072.
        self.assertEqual(m.triple_ris(169, 343, 512), 13 * 49 * 256)
        # (1,8,9): ris(1)*ris(8)*ris(9)=1*4*3=12.
        self.assertEqual(m.triple_ris(1, 8, 9), 12)

    def test_gcd_and_sum_guards(self):
        with self.assertRaises(ABCClockError):   # gcd(2,4)=2
            m.triple_ris(2, 4, 6)
        with self.assertRaises(ABCClockError):   # a+b != c
            m.triple_ris(1, 2, 4)
        with self.assertRaises(ABCClockError):   # nonpositive
            m.triple_ris(0, 1, 1)


class CensusTests(unittest.TestCase):
    def test_spectrum_small_by_hand(self):
        # Ordered primitive triples, c=2..6:
        #  c=2:(1,1) ris=1
        #  c=3:(1,2),(2,1) ris=1,1
        #  c=4:(1,3),(3,1) ris=1,1
        #  c=5:(1,4),(2,3),(3,2),(4,1) ris: ris(4)=2 -> 2,1,1,2
        #  c=6:(1,5),(5,1) ris=1,1
        # => {1:7, 2:4}
        self.assertEqual(m.ris_spectrum(6), Counter({1: 7, 2: 4}))

    def test_spectrum_matches_independent_bruteforce(self):
        X = 40
        brute = Counter()
        for c in range(2, X + 1):
            for a in range(1, c):
                b = c - a
                if gcd(a, b) == 1:
                    brute[ris(a) * ris(b) * ris(c)] += 1
        self.assertEqual(m.ris_spectrum(X), brute)

    def test_counts_and_integer_moments(self):
        X = 30
        spec = m.ris_spectrum(X)
        self.assertEqual(m.triple_count(X), sum(spec.values()))
        self.assertEqual(m.integer_moment(X, 0), m.triple_count(X))
        # S_1 = sum of ris(abc) over triples, exact int.
        brute1 = sum(ris(a) * ris(b) * ris(c) for a, b, c in m.primitive_triples(X))
        self.assertEqual(m.integer_moment(X, 1), brute1)
        self.assertIsInstance(m.integer_moment(X, 1), int)

    def test_ordered_vs_unordered_relation(self):
        # Only (1,1,2) lies on the diagonal, so ordered = 2*unordered - 1.
        for X in (5, 10, 25, 50):
            o = m.triple_count(X, ordered=True)
            u = m.triple_count(X, ordered=False)
            self.assertEqual(o, 2 * u - 1)


class EnclosureTests(unittest.TestCase):
    def test_integer_t_enclosure_is_exact_anchor(self):
        X = 25
        lo, hi = m.S_t_enclosure(X, Fraction(1))   # den=1 -> exact
        self.assertEqual(lo, hi)
        self.assertEqual(lo, Fraction(m.integer_moment(X, 1)))

    def test_t_two_fifths_bracket_is_valid_and_tight(self):
        X = 60
        lo, hi = m.S_t_enclosure(X, Fraction(2, 5))
        self.assertLess(lo, hi)
        self.assertIsInstance(lo, Fraction)
        self.assertIsInstance(hi, Fraction)
        # width <= (#triples)/precision; here precision default 1e9.
        self.assertLessEqual(hi - lo, Fraction(m.triple_count(X), 10 ** 9))

    def test_enclosures_at_two_precisions_overlap(self):
        X = 40
        lo1, hi1 = m.S_t_enclosure(X, Fraction(2, 5), precision=10 ** 3)
        lo2, hi2 = m.S_t_enclosure(X, Fraction(2, 5), precision=10 ** 7)
        # Both brackets contain the true value, hence overlap.
        self.assertLessEqual(lo1, hi2)
        self.assertLessEqual(lo2, hi1)


class RatioGrowthTests(unittest.TestCase):
    def test_ratio_bounded_on_computed_range(self):
        # Empirical boundedness: S_{2/5}(X)/X^2 stays well under 1 on the range.
        for X in (10, 20, 40, 80, 160):
            lo, hi = m.ratio_enclosure(X, Fraction(2, 5))
            self.assertGreater(lo, 0)
            self.assertLess(hi, Fraction(9, 10))

    def test_growth_table_shape_and_increase(self):
        rows = m.growth_table(Fraction(2, 5), (20, 40, 80, 160))
        self.assertEqual([r["X"] for r in rows], [20, 40, 80, 160])
        # On this range the ratio lower bound is (slowly) nondecreasing.
        los = [r["ratio_lo"] for r in rows]
        self.assertEqual(los, sorted(los))


class PartialTheoremTests(unittest.TestCase):
    def test_constant_is_fraction_and_finite_for_two_fifths(self):
        C = m.S_t_constant_upper(Fraction(2, 5))
        self.assertIsInstance(C, Fraction)
        self.assertGreater(C, 1)

    def test_theorem_bound_dominates_data(self):
        # The proved inequality S_t(X) <= C_t * X^2 holds on the exact census.
        C = m.S_t_constant_upper(Fraction(2, 5))
        for X in (20, 60, 120, 200):
            lo, hi = m.S_t_enclosure(X, Fraction(2, 5))
            self.assertLessEqual(hi, C * X * X)

    def test_constant_upper_exceeds_independent_partial_lower(self):
        # Independent LOWER bound on the true M(theta) from the first two Euler
        # factors; the rigorous upper bound must exceed it.
        for theta in (Fraction(2, 5), Fraction(4, 5)):
            num, den = theta.numerator, theta.denominator
            lower = Fraction(1)
            for p in (2, 3, 5):
                lo_pt, _ = m.power_enclosure(p, num, den, 10 ** 6)        # <= p^theta
                _, hi_p1mt = m.power_enclosure(p, den - num, den, 10 ** 6)  # >= p^{1-theta}
                # a_p >= (p^theta-1) / (p^2 (1 - 1/hi))   (a true lower bound)
                a_low = (lo_pt - 1) / ((p * p) * (1 - 1 / hi_p1mt))
                lower *= (1 + a_low)
            self.assertGreaterEqual(m.ris_moment_constant_upper(theta), lower)

    def test_method_wall_at_one_half(self):
        # The Cauchy-Schwarz route needs 2t<1; it must refuse t>=1/2.
        with self.assertRaises(ABCClockError):
            m.S_t_constant_upper(Fraction(1, 2))
        with self.assertRaises(ABCClockError):
            m.S_t_constant_upper(Fraction(3, 5))


class HostileFamilyTests(unittest.TestCase):
    def test_power_tower_exact_values(self):
        fam = {r["k"]: r for r in m.power_tower_family(64, base=2)}
        # (1, 7, 8): ris(7)=1, ris(8)=4 -> 4
        self.assertEqual(fam[3]["c"], 8)
        self.assertEqual(fam[3]["ris_abc"], 1 * 1 * 4)
        # (1, 63, 64): 63=3^2*7 -> ris=3; 64=2^6 -> ris=32; product 96
        self.assertEqual(fam[6]["c"], 64)
        self.assertEqual(fam[6]["ris_abc"], 1 * 3 * 32)
        # Each row is a valid primitive triple with the claimed ris.
        for r in fam.values():
            self.assertEqual(r["a"] + r["b"], r["c"])
            self.assertEqual(gcd(r["a"], r["b"]), 1)
            self.assertEqual(r["ris_abc"], ris(r["a"]) * ris(r["b"]) * ris(r["c"]))

    def test_pointwise_moment_is_unbounded_but_family_is_subquadratic(self):
        # Pointwise maximum ris grows with X (no uniform termwise bound) ...
        max_small, arg_small = m.pointwise_max_ris(100)
        max_big, arg_big = m.pointwise_max_ris(600)
        self.assertGreater(max_big, max_small)
        a, b, c = arg_big
        self.assertEqual(a + b, c)
        self.assertEqual(gcd(a, b), 1)
        self.assertEqual(ris(a) * ris(b) * ris(c), max_big)
        # ... yet the tower family's total ris^{2/5} contribution is o(X^2):
        # contribution / X^2 shrinks as X grows.
        _, hi_s = m.power_tower_contribution_enclosure(1024, Fraction(2, 5))
        _, hi_b = m.power_tower_contribution_enclosure(4096, Fraction(2, 5))
        r_s = hi_s / (1024 ** 2)
        r_b = hi_b / (4096 ** 2)
        self.assertLess(r_b, r_s)
        self.assertLess(r_b, Fraction(1, 1000))


class NoFloatDisciplineTests(unittest.TestCase):
    def test_outputs_are_exact_types(self):
        self.assertTrue(all(isinstance(k, int) and isinstance(v, int)
                            for k, v in m.ris_spectrum(20).items()))
        lo, hi = m.S_t_enclosure(20, Fraction(2, 5))
        self.assertIsInstance(lo, Fraction)
        self.assertIsInstance(hi, Fraction)
        self.assertIsInstance(m.S_t_constant_upper(Fraction(2, 5)), Fraction)
        self.assertIsInstance(m.integer_moment(20, 2), int)


if __name__ == "__main__":
    unittest.main()
