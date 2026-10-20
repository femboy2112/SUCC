"""Tests for observational_succ.goldbach_circle (Rigidity Forge Part VII, section 7).

Exact-arithmetic receipts for the additive Fourier identity (GC-01), the
F^2 vs |F|^2 firewall, the prime-support / contamination split, and the
Hardy-Littlewood singular series (GC-02).  Binary Goldbach is OPEN; no Goldbach
claim is tested, only classical identities and the singular-series object.
"""
import unittest
from fractions import Fraction

import sympy as sp

from observational_succ.arithmetic_interactions import goldbach_representation_R_Lambda
from observational_succ.goldbach_circle import (
    GoldbachCircleError,
    R_Lambda_from_dft,
    R_Lambda_from_fourier_poly,
    arc_decomposition_summary,
    difference_diagonal,
    farey_major_arcs,
    fourier_identity_check,
    goldbach_main_term_enclosure,
    major_arc_benchmark,
    odd_prime_transport_factor,
    singular_series_enclosure,
    singular_series_local_factor,
    singular_series_transport_enclosure,
    singular_series_truncated,
    singular_series_via_transport,
    support_split,
    twin_prime_constant_enclosure,
)


class TestFourierIdentityExact(unittest.TestCase):
    """GC-01: R_Lambda(N) = [z^N] F(z)^2, exact, three agreeing routes."""

    def test_poly_route_matches_direct(self):
        for N in range(4, 30):
            poly = R_Lambda_from_fourier_poly(N)
            direct = goldbach_representation_R_Lambda(N)
            self.assertEqual(sp.simplify(sp.sympify(poly) - direct), 0,
                             f"poly Fourier identity failed at N={N}")

    def test_dft_route_matches_direct_small(self):
        # exact roots-of-unity route (slow, symbolic): small N only
        for N in (4, 5, 6, 8, 10):
            dft = R_Lambda_from_dft(N)
            direct = goldbach_representation_R_Lambda(N)
            self.assertEqual(sp.simplify(dft - direct), 0,
                             f"DFT Fourier identity failed at N={N}")

    def test_known_small_values(self):
        # N=6: a+b=6 -> (2,4)no, (3,3)yes, (4,2)no, (2,4)... Lambda nonzero at primes/powers
        # pairs: (2,4):log2*0? 4=2^2 so Lambda(4)=log2 -> log2*log2 ; (3,3):log3^2 ; (4,2):log2^2
        # total = 2 log2^2 + log3^2
        val = sp.simplify(sp.sympify(R_Lambda_from_fourier_poly(6)))
        self.assertEqual(val, sp.simplify(2 * sp.log(2) ** 2 + sp.log(3) ** 2))

    def test_identity_check_bundle(self):
        res = fourier_identity_check(12, with_dft=False)
        self.assertTrue(res["poly_matches"])
        self.assertTrue(res["difference_is_zero"])


class TestFourierFirewall(unittest.TestCase):
    """F^2 (sum) vs |F|^2 (difference): the difference diagonal is identically 0."""

    def test_difference_diagonal_zero(self):
        for N in range(4, 30):
            self.assertEqual(sp.simplify(difference_diagonal(N)), 0,
                             f"difference diagonal nonzero at N={N}")


class TestSupportSplit(unittest.TestCase):
    """Exact split into genuine prime-pair mass and prime-power contamination."""

    def test_decomposition_exact(self):
        for N in range(4, 60):
            s = support_split(N)
            self.assertTrue(s.decomposition_exact, f"split not exact at N={N}")

    def test_contamination_identified(self):
        # N=8: pairs (3,5),(5,3) pure prime; (2,6)no(6 not pp); (4,4) 4=2^2 contamination;
        #      (6,2)no; so contamination includes (4,4).
        s = support_split(8)
        self.assertIn((4, 4), s.contamination_terms)
        self.assertEqual(s.n_true_prime_pairs, 2)   # (3,5) and (5,3)

    def test_total_equals_R_Lambda(self):
        for N in (10, 16, 24, 30):
            s = support_split(N)
            self.assertEqual(sp.simplify(sp.sympify(s.total)
                             - goldbach_representation_R_Lambda(N)), 0)


class TestSingularSeries(unittest.TestCase):
    """GC-02: exact Hardy-Littlewood singular series object + certified bracket."""

    def test_local_factor_values(self):
        # p|N -> 1 + 1/(p-1); p∤N -> 1 - 1/(p-1)^2
        self.assertEqual(singular_series_local_factor(3, 6), Fraction(1) + Fraction(1, 2))
        self.assertEqual(singular_series_local_factor(5, 6), Fraction(1) - Fraction(1, 16))
        # p=2, N odd -> 0  (local obstruction)
        self.assertEqual(singular_series_local_factor(2, 7), Fraction(0))
        # p=2, N even -> 1 + 1/(2-1) = 2
        self.assertEqual(singular_series_local_factor(2, 8), Fraction(2))

    def test_odd_N_series_zero(self):
        lo, hi = singular_series_enclosure(15, 4000)
        self.assertEqual((lo, hi), (Fraction(0), Fraction(0)))

    def test_even_enclosure_brackets(self):
        # S(N) must lie in [lo, hi] and the bracket must be positive & ordered
        for N in (10, 30, 100, 210):
            lo, hi = singular_series_enclosure(N, 5000)
            self.assertLess(0, lo)
            self.assertLessEqual(lo, hi)
            # width is controlled by the tail bound 1/(P-1)
            self.assertLess(hi - lo, hi * Fraction(1, 5000 - 1) + Fraction(1, 100))

    def test_twin_prime_constant(self):
        lo, hi = twin_prime_constant_enclosure(5000)
        # 2 C_2 ~ 1.3203236
        self.assertLessEqual(float(lo), 1.3203236)
        self.assertGreaterEqual(float(hi), 1.3203236)

    def test_truncation_requires_large_P(self):
        # N=2310=2*3*5*7*11: P must be >= 11 to capture all p|N
        with self.assertRaises(GoldbachCircleError):
            singular_series_truncated(2310, 10)
        # P=11 is fine
        self.assertGreater(singular_series_truncated(2310, 11), 0)

    def test_main_term_is_bracket_times_N(self):
        lo, hi = singular_series_enclosure(30, 5000)
        mlo, mhi = goldbach_main_term_enclosure(30, 5000)
        self.assertEqual(mlo, lo * 30)
        self.assertEqual(mhi, hi * 30)


class TestSingularSeriesTransport(unittest.TestCase):
    """GC-03: finite singular-series transport lemma (exact identity + certified tail).

    Pins the CORRECTION to the twin-constant docstring: 2*C_2 is the BASE constant,
    distinct from S(2q) = 2*C_2 * (q-1)/(q-2).
    """

    def test_odd_prime_transport_factor_exact(self):
        # q=3,5,7 -> (q-1)/(q-2) = 2, 4/3, 6/5 exactly.
        self.assertEqual(odd_prime_transport_factor(2 * 3), Fraction(2, 1))
        self.assertEqual(odd_prime_transport_factor(2 * 5), Fraction(4, 3))
        self.assertEqual(odd_prime_transport_factor(2 * 7), Fraction(6, 5))
        # Power of 2 -> empty product -> 1.
        self.assertEqual(odd_prime_transport_factor(16), Fraction(1))
        # Insensitive to the exponent: K(6) = K(18) (both odd part supported on {3}).
        self.assertEqual(odd_prime_transport_factor(18), odd_prime_transport_factor(6))
        # Several odd primes multiply: 30 = 2*3*5 -> 2 * 4/3 = 8/3.
        self.assertEqual(odd_prime_transport_factor(30), Fraction(8, 3))

    def test_S_2q_is_base_times_factor_not_base(self):
        # The exact fact the docstring fix encodes: S(2q) = 2*C_2 * (q-1)/(q-2),
        # NOT 2*C_2.  Verified at the truncated level (P large, so exact rational).
        P = 20000
        _lo, two_C2 = twin_prime_constant_enclosure(P)       # two_C2 = 2*T(P)
        for q, factor in ((3, Fraction(2)), (5, Fraction(4, 3)), (7, Fraction(6, 5))):
            N = 2 * q
            S_trunc = singular_series_truncated(N, P)
            self.assertEqual(S_trunc, two_C2 * factor,
                             f"S({N}) should be 2*C_2*{factor}")
            self.assertNotEqual(S_trunc, two_C2,
                                f"S({N}) must NOT equal the base constant 2*C_2")

    def test_transport_identity_matches_truncated_product(self):
        # EXACT identity S_{<=P}(N) = 2*T(P)*K(N) = singular_series_truncated(N,P).
        P = 5000
        for N in (6, 10, 14, 18, 22, 30, 42, 210, 2310):
            self.assertEqual(singular_series_via_transport(N, P),
                             singular_series_truncated(N, P),
                             f"transport identity failed at N={N}")

    def test_transport_enclosure_matches_direct_enclosure(self):
        # Two independent routes to the SAME certified bracket.
        P = 5000
        for N in (10, 30, 100, 210, 2310):
            self.assertEqual(singular_series_transport_enclosure(N, P),
                             singular_series_enclosure(N, P),
                             f"transport enclosure disagrees at N={N}")

    def test_transport_enclosure_brackets_true_series(self):
        # lo <= S_{<=P'}(N) <= hi for a much finer truncation P' (S monotone in tail).
        P, Pfine = 2000, 200000
        for N in (10, 30, 210):
            lo, hi = singular_series_transport_enclosure(N, P)
            s_fine = singular_series_truncated(N, Pfine)
            self.assertLessEqual(lo, s_fine)
            self.assertLessEqual(s_fine, hi)
            self.assertLess(0, lo)

    def test_transport_requires_P_ge_largest_prime_factor(self):
        # N=2*101: P must reach 101 or the enhanced S_101 factor is missing.
        with self.assertRaises(GoldbachCircleError):
            singular_series_via_transport(2 * 101, 50)
        self.assertGreater(singular_series_via_transport(2 * 101, 101), 0)

    def test_odd_N_transport_is_zero(self):
        self.assertEqual(singular_series_via_transport(15, 4000), Fraction(0))
        self.assertEqual(singular_series_transport_enclosure(15, 4000),
                         (Fraction(0), Fraction(0)))


class TestMajorArcBenchmark(unittest.TestCase):
    """Structural Siegel-Walfisz major-arc benchmark: honest labels, no fake certificate."""

    def test_benchmark_labels_and_exact_bracket(self):
        b = major_arc_benchmark(100, P=5000, A=2)
        self.assertEqual(b["binary_goldbach"], "OPEN")
        self.assertFalse(b["rh_used"])
        self.assertIn("INEFFECTIVE", b["imported_constant_status"])
        self.assertIn("OPEN", b["minor_arc_status"])
        # The only certified numeric field is the exact singular-series bracket.
        self.assertEqual(b["singular_series_bracket"],
                         singular_series_enclosure(100, 5000))
        lo, hi = b["singular_series_bracket"]
        self.assertIsInstance(lo, Fraction)
        self.assertLessEqual(lo, hi)

    def test_benchmark_rejects_odd_N(self):
        with self.assertRaises(GoldbachCircleError):
            major_arc_benchmark(101, P=5000)


class TestArcStructure(unittest.TestCase):
    """Major/minor-arc Farey structure exposed (no asymptotics claimed)."""

    def test_farey_counts(self):
        # q=1 gives a=0 (1 arc); q=2 gives a=1; q=3 gives a=1,2; total for Q=3: 1+1+2=4
        arcs = farey_major_arcs(3, 10)
        self.assertEqual(len(arcs), 4)
        # half widths are 1/(qN)
        widths = {(a.q, a.half_width) for a in arcs}
        self.assertIn((2, Fraction(1, 20)), widths)
        self.assertIn((3, Fraction(1, 30)), widths)

    def test_summary_labels_open(self):
        s = arc_decomposition_summary(5, 100)
        self.assertEqual(s["goldbach_claim"], "NONE; binary Goldbach is OPEN")
        self.assertIn("OPEN", s["minor_arc_status"])
        self.assertIn("CLASSICAL", s["major_arc_status"])


if __name__ == "__main__":
    unittest.main()
