"""Hostile independent controls; no universal theorem inferred from a census."""

from fractions import Fraction as F
import unittest

from scripts.duck_hostile_referee import (
    bbp_four_terms, bbp_rational, bbp_tail_interval, c2_c3_nontrivial_common_factors,
    clock_stationarity_residuals, cyclic_factor_maps, delayed_probe,
    fake_alternating_derivative, fake_closed_orbit, fake_forcing, forced_orbit,
    intervals_meet_mod_one, machin_interval, receipt, thue_morse_prefix,
    sharp_bbp_polynomial_gap,
)


class DuckHostileRefereeTests(unittest.TestCase):
    def test_exact_domain_rejects_type_confusion(self):
        for value in [True, 1.0, F(1), 0, -1]:
            with self.assertRaises(ValueError):
                bbp_rational(value)
        for value in [True, 1.5, F(2), -1]:
            with self.assertRaises(ValueError):
                bbp_tail_interval(value, 3)

    def test_independent_rational_identity_and_bound(self):
        for n in [1, 2, 3, 17, 113, 10**30]:
            r = bbp_rational(n)
            self.assertEqual(r, bbp_four_terms(n))
            self.assertGreater(r, 0)
            self.assertLessEqual(r, F(8, n*n))
        self.assertEqual(bbp_rational(1), F(47, 15))
        # The denominator mutation -206n -> -205n is rejected already at n=1.
        self.assertNotEqual(bbp_four_terms(1), F(47, 16))

    def test_independent_machin_source_rejects_off_by_one(self):
        low, high = machin_interval(60)
        for n in range(1, 9):
            x = forced_orbit(n)
            a, b = bbp_tail_interval(n, 12)
            self.assertTrue(intervals_meet_mod_one((x+a, x+b), (16**(n-1)*low, 16**(n-1)*high)))
            self.assertFalse(intervals_meet_mod_one((x+a, x+b), (16**n*low, 16**n*high)))

    def test_optimal_global_coefficient_and_pole_classes(self):
        for n in [1, 2, 3, 100, 10**30]:
            lhs, rhs = sharp_bbp_polynomial_gap(n)
            self.assertEqual(lhs, rhs)
            self.assertGreaterEqual(lhs, 0)
            self.assertLessEqual(bbp_rational(n), F(47, 15*n*n))
        self.assertEqual(sharp_bbp_polynomial_gap(1), (0, 0))
        poles = [F(1, 4), F(1, 2), F(3, 8), F(7, 8)]
        for i, a in enumerate(poles):
            for b in poles[i+1:]:
                self.assertNotEqual((a-b).denominator, 1)

    def test_smooth_positive_rational_impostor(self):
        for n in range(129):
            self.assertEqual(forced_orbit(n, fake_forcing), fake_closed_orbit(n))
            if n >= 2:
                self.assertEqual(fake_closed_orbit(n), 1-F(1, 64*(n+1)**2))
        for n in range(1, 25):
            self.assertLessEqual(fake_forcing(n), F(8, n*n))
            for order in range(9):
                self.assertGreater(fake_alternating_derivative(n, order), 0)

    def test_erased_cycles_have_no_nontrivial_common_onto_factor(self):
        self.assertEqual(c2_c3_nontrivial_common_factors(), [])
        self.assertEqual(len(cyclic_factor_maps(2, (1, 0))), 2)
        self.assertEqual(len(cyclic_factor_maps(3, (1, 2, 0))), 3)
        self.assertEqual(len(cyclic_factor_maps(2, (0,))), 1)

    def test_no_fixed_probe_budget_without_separation_theorem(self):
        for budget in range(25):
            row = delayed_probe(budget)
            self.assertTrue(row["all_budget_words_agree"])
            self.assertTrue(row["next_word_distinguishes"])

    def test_thue_morse_missing_words(self):
        prefix = thue_morse_prefix(16384)
        self.assertTrue(all(prefix[2*k] != prefix[2*k+1] for k in range(len(prefix)//2)))
        triples = {prefix[k:k+3] for k in range(len(prefix)-2)}
        self.assertNotIn((0, 0, 0), triples)
        self.assertNotIn((1, 1, 1), triples)
        self.assertNotIn(2, prefix)  # Also a missing digit when read in base 16.

    def test_clock_boundary_and_nonminimal_attractor_controls(self):
        self.assertNotEqual(clock_stationarity_residuals((F(1), F(0))), (F(0), F(0)))
        self.assertNotEqual(clock_stationarity_residuals((F(0), F(1))), (F(0), F(0)))
        self.assertEqual(clock_stationarity_residuals((F(0),)*8), (F(0),)*8)
        # A finite covering attractor may contain unused points and need not be a cycle.
        covering_set = {F(0), F(1, 3)}
        self.assertIn(F(0), covering_set)
        self.assertNotIn(F(2, 3), covering_set)

    def test_receipt_runs_all_controls(self):
        result = receipt()
        self.assertEqual(result["status"], "EXACT_FINITE_CHECK")
        self.assertEqual(result["pi_normality"], "OPEN")


if __name__ == "__main__":
    unittest.main()
