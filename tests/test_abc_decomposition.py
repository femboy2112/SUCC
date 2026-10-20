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
    FailureStatus,
    bblt_anatomy,
    bounded_exponent_local_factor_enclosure,
    bounded_exponent_mean_converges,
    bounded_exponent_threshold,
    bounded_powerful_part_bound,
    bounded_powerful_part_census,
    cauchy_schwarz_ceiling,
    census_anchor_S1,
    coprimality_joint_occupation,
    exponent_layers,
    failure_mode_ledger,
    failure_mode_overclaim_guard,
    inner_correlation_enclosure,
    is_powerful,
    joint_divisibility_count,
    layer_anatomy,
    layer_euler_product_converges,
    layer_mean_leading_exponent,
    local_ris_mean_factor_enclosure,
    machinery_boundary,
    max_exponent,
    powerful_main_constant_truncated_enclosure,
    powerful_main_term_converges,
    powerful_main_term_leading_exponent,
    powerful_numbers_up_to,
    powerful_part,
    qualified_bounded_exponent_statement,
    residue_box_correlation_obstruction,
    ris_power_layer_factorization,
    ris_powerful_majorant_terms,
    squarefree_class_moment,
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
        # Ordinary layer tail is one exactly iff max exponent <= d; no BBLT claim.
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
        self.assertTrue(m["beats_half_rigorously"])
        self.assertFalse(m["diagonal_method_beats_half"])
        self.assertEqual(m["proved_moment_upper_endpoint"], Fraction(2, 3))
        self.assertFalse(m["endpoint_included"])
        self.assertEqual(m["reviewed_theorems"], ("CLOUD-ABC-01", "CLOUD-ABC-05"))
        self.assertIn("REFUTED", m["fourier_necessity_claim_status"])
        self.assertEqual(m["heuristic_true_threshold"], Fraction(1))
        self.assertEqual(m["abc_status"], "OPEN")
        self.assertIn("BBLT", m["needs_machinery_not_in_SUCC"])


class TestQualifiedBoundedExponent(unittest.TestCase):
    """ABC-DEC-02q (Part V Task 1): E=1 squarefree class has NO theta=1 wall
    (ris==1, theta-independent); E>=2 retains the wall via the j=2 layer alone."""

    def test_squarefree_moment_equals_count_theta_independent(self):
        # the moment on {max v_p <= 1} equals the squarefree count for EVERY theta
        for X in (50, 200, 1000):
            res = squarefree_class_moment(X)
            # independent recomputation of squarefree count
            sqfree = sum(1 for n in range(1, X + 1) if max_exponent(n) <= 1)
            self.assertEqual(res["moment_value"], sqfree)
            self.assertTrue(res["moment_equals_count"])
            self.assertTrue(res["theta_independent"])
            self.assertTrue(res["bounded_by_X"])
            self.assertFalse(res["wall_present"])
            # every such n is squarefree with ris == 1
            self.assertTrue(all(ris(n) == 1 for n in range(1, X + 1)
                                if max_exponent(n) <= 1))

    def test_E1_local_factor_is_exact_and_theta_independent(self):
        # E_p^{(1)}(theta) = 1 - 1/p^2 EXACTLY for every theta (lo == hi)
        for p in (2, 3, 5, 7, 11, 13):
            for theta in (Fraction(0), Fraction(3, 7), Fraction(1, 2),
                          Fraction(9, 10), Fraction(1)):
                lo, hi = bounded_exponent_local_factor_enclosure(p, 1, theta)
                self.assertEqual(lo, hi)
                self.assertEqual(lo, 1 - Fraction(1, p * p))

    def test_E2_local_factor_integer_theta_exact(self):
        # E_p^{(2)}(1) = (p-1)/p (1 + 1/p + 1/p) = (p-1)(p+2)/p^2
        for p in (2, 3, 5):
            lo, hi = bounded_exponent_local_factor_enclosure(p, 2, Fraction(1))
            self.assertEqual(lo, hi)
            self.assertEqual(lo, Fraction((p - 1) * (p + 2), p * p))

    def test_E2_local_factor_rational_theta_bracket_narrow(self):
        lo, hi = bounded_exponent_local_factor_enclosure(5, 2, Fraction(1, 2),
                                                         precision=10 ** 12)
        self.assertLess(lo, hi)
        self.assertLess(hi - lo, Fraction(1, 10 ** 6))

    def test_qualified_threshold_E1_none_E2_one(self):
        self.assertIsNone(bounded_exponent_threshold(0))
        self.assertIsNone(bounded_exponent_threshold(1))
        for E in range(2, 8):
            self.assertEqual(bounded_exponent_threshold(E), Fraction(1))

    def test_mean_convergence_qualified(self):
        # E<=1 converges for EVERY theta; E>=2 iff theta<1
        for theta in (Fraction(1, 2), Fraction(1), Fraction(3, 2)):
            self.assertTrue(bounded_exponent_mean_converges(1, theta))
            self.assertTrue(bounded_exponent_mean_converges(0, theta))
        for E in (2, 3, 5):
            self.assertTrue(bounded_exponent_mean_converges(E, Fraction(9, 10)))
            self.assertFalse(bounded_exponent_mean_converges(E, Fraction(1)))
            self.assertFalse(bounded_exponent_mean_converges(E, Fraction(11, 10)))

    def test_statement_ledger_consistent(self):
        st = qualified_bounded_exponent_statement()
        self.assertEqual(st["claim"], "ABC-DEC-02q")
        self.assertFalse(st["E_equals_1"]["wall_at_theta_1"])
        self.assertTrue(st["E_equals_1"]["vacuous_for_abc"])
        self.assertTrue(st["E_ge_2"]["wall_at_theta_1"])
        self.assertEqual(st["E_ge_2"]["threshold"], Fraction(1))

    def test_cauchy_schwarz_ceiling_qualified_keys(self):
        c = cauchy_schwarz_ceiling()
        self.assertEqual(c["ceiling_t"], Fraction(1, 2))
        self.assertFalse(c["bounded_exponent_helps"])            # unchanged
        self.assertFalse(c["bounded_exponent_helps_for_E_ge_2"])  # qualified
        self.assertTrue(c["E1_squarefree_is_vacuous"])


class TestFailureModeLedger(unittest.TestCase):
    """ABC-FM (Part V Task 2): only (a) diagonal/CS and (b) a particular Euler
    majorant fail; (c) class-wide barrier is REFUTED, (d) theorem failure OPEN."""

    def test_four_modes_statuses(self):
        led = failure_mode_ledger()
        self.assertEqual(len(led), 4)
        by_tag = {m.tag: m for m in led}
        self.assertEqual(by_tag["a"].status, FailureStatus.ESTABLISHED)
        self.assertEqual(by_tag["b"].status, FailureStatus.ESTABLISHED)
        self.assertEqual(by_tag["c"].status, FailureStatus.REFUTED)
        self.assertIn("CLOUD-ABC-01", by_tag["c"].receipt)
        self.assertEqual(by_tag["d"].status, FailureStatus.NOT_ESTABLISHED)
        # every mode carries a receipt pointing at in-repo evidence
        self.assertTrue(all(m.receipt for m in led))

    def test_overclaim_guard(self):
        g = failure_mode_overclaim_guard()
        self.assertEqual(g["established"], ("a", "b"))
        self.assertEqual(g["not_established"], ("d",))
        self.assertEqual(g["refuted"], ("c",))
        self.assertTrue(g["correct"])


class TestResidueBoxCorrelation(unittest.TestCase):
    """ABC-COR-01/02/03 (Part V Task 3): the residue-box additive-correlation
    attempt -- main term reaches t<1, bounded-Q theorem, isolated obstruction."""

    def test_powerful_primitives(self):
        # a^2 b^3 parametrisation matches the brute-force powerful set
        for Q in (50, 500, 3000):
            got = powerful_numbers_up_to(Q)
            brute = tuple(n for n in range(1, Q + 1) if is_powerful(n))
            self.assertEqual(got, brute)
        # ris depends only on the powerful part
        for n in range(1, 2000):
            self.assertEqual(ris(n), ris(powerful_part(n)))
            self.assertTrue(is_powerful(powerful_part(n)))

    def test_ris_powerful_majorant_dominates(self):
        # ABC-COR key inequality: ris(a)^t <= sum_{d|a powerful} ris(d)^t (int t exact)
        for t in (0, 1, 2):
            for a in range(1, 1500):
                lo, hi = ris_powerful_majorant_terms(a, t)
                self.assertEqual(lo, hi)                     # exact for integer t
                self.assertGreaterEqual(lo, Fraction(ris(a) ** t))

    def test_joint_divisibility_matches_bruteforce(self):
        # residue-box encoding of 'd|a and d'|b' equals the direct count
        for (d, dp, X) in ((4, 9, 60), (8, 27, 100), (4, 4, 50), (9, 25, 120)):
            res = joint_divisibility_count(d, dp, X)
            brute = sum(1 for a in range(1, X) for b in range(1, X - a + 1)
                        if a % d == 0 and b % dp == 0)
            self.assertEqual(res["count"], brute)
            # the proved error bound holds around the exact count vs main term
            self.assertLessEqual(abs(res["count"] - res["main_term"]),
                                 res["error_bound"])

    def test_main_term_threshold_beats_half(self):
        # G(t) = sum_{d powerful} ris(d)^t/d converges iff t<1 (past diagonal t<1/2)
        self.assertEqual(powerful_main_term_leading_exponent(Fraction(1, 2)),
                         Fraction(1, 2) - 2)
        for t in (Fraction(0), Fraction(1, 2), Fraction(9, 10), Fraction(99, 100)):
            self.assertTrue(powerful_main_term_converges(t))
        for t in (Fraction(1), Fraction(11, 10)):
            self.assertFalse(powerful_main_term_converges(t))
        # truncated constant is a valid, monotone enclosure
        lo1, hi1 = powerful_main_constant_truncated_enclosure(Fraction(1, 2), 1000)
        lo2, hi2 = powerful_main_constant_truncated_enclosure(Fraction(1, 2), 10000)
        self.assertLessEqual(lo1, hi1)
        self.assertLessEqual(lo1, lo2)                       # monotone in Pmax
        self.assertLessEqual(hi1, hi2 + Fraction(1, 10 ** 6))

    def test_bounded_powerful_part_bound_holds_all_t(self):
        # ABC-COR-02 genuine theorem: J_t^{(Q)}(X) <= bound, EVERY t (here int t)
        for (X, Q, t) in ((60, 8, 1), (80, 16, 1), (100, 9, 1),
                          (60, 8, 2), (50, 25, 1), (60, 4, 3)):
            b = bounded_powerful_part_bound(X, Q, t)
            jq = bounded_powerful_part_census(X, Q, t)
            self.assertLessEqual(jq, b.bound)                # the bound is valid
            self.assertLessEqual(b.G_Q[0], b.G_Q[1])         # valid enclosure
            self.assertEqual(b.bound, b.main_term + b.error_part)
            self.assertGreaterEqual(b.dominance_threshold_X, 0)

    def test_bounded_powerful_threshold_includes_constant_error(self):
        # Q=4,t=0: G=5/4,A=2,B=5. Old threshold26 drops 5B^2=125:
        # at X=26 the main term4225/8 is below the error645. The true least
        # integer satisfying (25/32)X^2>20X+125 is31.
        broken_boundary = bounded_powerful_part_bound(26, 4, 0)
        self.assertEqual(broken_boundary.main_term, Fraction(4225, 8))
        self.assertEqual(broken_boundary.error_part, 645)
        self.assertFalse(broken_boundary.informative)
        self.assertEqual(broken_boundary.dominance_threshold_X, 31)
        for Q, t in ((1, 0), (4, 0), (9, 1), (25, 2), (16, Fraction(3, 5))):
            result = bounded_powerful_part_bound(1, Q, t)
            threshold = result.dominance_threshold_X
            self.assertTrue(bounded_powerful_part_bound(threshold, Q, t).informative)
            self.assertFalse(bounded_powerful_part_bound(threshold - 1, Q, t).informative)

    def test_coprimality_restricts_same_prime_only(self):
        res = coprimality_joint_occupation(2, 120)
        self.assertEqual(res["coprime_same_prime_count"], 0)   # forbidden
        self.assertGreater(res["coprime_different_prime_count"], 0)  # allowed
        self.assertTrue(res["coprimality_kills_same_prime"])
        self.assertTrue(res["coprimality_spares_different_prime"])

    def test_obstruction_ledger_honest(self):
        o = residue_box_correlation_obstruction()
        self.assertEqual(o["claim"], "ABC-COR-03")
        self.assertEqual(o["residue_box_main_term_threshold"], Fraction(1))
        self.assertEqual(o["diagonal_cauchy_schwarz_threshold"], Fraction(1, 2))
        self.assertTrue(o["main_term_beats_half"])
        self.assertFalse(o["rigorous_bound_from_residue_box"])  # error >> X^2
        self.assertFalse(o["residue_box_provides_cancellation"])
        self.assertFalse(o["a_plus_b_eq_c_provides_cancellation"])
        self.assertEqual(o["abc_status"], "OPEN")
        self.assertIn("BBLT", o["missing_estimate_source"])
        self.assertIn("PROVED LOCAL", o["t_half_moment_bound_status"])
        self.assertIn("CLOUD-ABC-01", o["t_half_moment_bound_status"])
        self.assertEqual(o["remaining_open_moment_range"], "2/3<=t<1")
        self.assertIn("REFUTED", o["sign_changing_cancellation_necessary_status"])


if __name__ == "__main__":
    unittest.main()
