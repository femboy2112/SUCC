from fractions import Fraction as F
from itertools import combinations
import unittest

from observational_succ.lonely_runner_census import (
    complete_census, gap_velocity_cap, residual_gaps, single_band_winding,
)
from observational_succ.lonely_runner_two_entry import (
    all_retained, general_effective_bounds, uncovered_intervals,
)
from observational_succ.lonely_runner_verify import verify_cover


class CompleteCensusTests(unittest.TestCase):
    def test_all_n8_residual_gaps_match_separate_fraction_sweep(self):
        count = 0
        for r1, r2 in combinations(range(1, 8), 2):
            source = all_retained(8, r1, r2)
            for w1 in range(8, general_effective_bounds(8, r1, r2)["w1_max"] + 1):
                actual = residual_gaps(8, source + (w1,))
                self.assertEqual(actual, uncovered_intervals(8, source + (w1,)))
                self.assertTrue(actual)
                count += 1
        self.assertEqual(count, 531)

    def test_every_n8_gap_candidate_matches_full_source_union(self):
        tested = 0
        for r1, r2 in combinations(range(1, 8), 2):
            source = all_retained(8, r1, r2)
            for w1 in range(8, general_effective_bounds(8, r1, r2)["w1_max"] + 1):
                gaps = residual_gaps(8, source + (w1,))
                for w2 in range(w1 + 1, gap_velocity_cap(8, gaps) + 1):
                    covers = all(single_band_winding(8, w2, a, b) is not None for a, b in gaps)
                    self.assertEqual(covers, not uncovered_intervals(8, source + (w1, w2)))
                    tested += 1
        self.assertEqual(tested, 119)

    def test_closed_endpoints_and_sub_float_perturbation(self):
        left, right = F(7, 104), F(9, 104)
        self.assertEqual(single_band_winding(8, 13, left, right), 1)
        # A strict-inequality mutant loses the tight endpoint case. A float
        # mutant cannot distinguish this extension beyond a closed band.
        self.assertIsNone(single_band_winding(8, 13, left, right + F(1, 10**40)))
        self.assertEqual(float(right), float(right + F(1, 10**40)))

    def test_width_bound_uses_floor_and_accepts_equality(self):
        self.assertEqual(gap_velocity_cap(8, [(F(0), F(1, 31))]), 7)
        self.assertEqual(gap_velocity_cap(8, [(F(0), F(1, 32))]), 8)
        self.assertIsNone(single_band_winding(8, 8, F(0), F(1, 31)))
        # With the band centered at k=1, full equality is attainable.
        self.assertEqual(single_band_winding(8, 8, F(7, 64), F(9, 64)), 1)

    def test_omitting_a_residual_component_manufactures_a_false_cover(self):
        source = (1, 4, 5, 6, 7, 8)
        gaps = residual_gaps(8, source)
        self.assertIsNotNone(single_band_winding(8, 10, *gaps[0]))
        self.assertFalse(all(single_band_winding(8, 10, a, b) is not None for a, b in gaps))
        self.assertTrue(uncovered_intervals(8, source + (10,)))

    def test_n8_complete_domain_counts_and_independent_survivor(self):
        receipt, certificates = complete_census(8)
        self.assertTrue(receipt["complete"])
        self.assertEqual(receipt["deletion_pair_count"], 21)
        self.assertEqual(receipt["proved_finite_domain_candidate_count"], 158145)
        self.assertEqual(receipt["width_rejected_count"] + receipt["gap_tested_count"], 158145)
        self.assertEqual(receipt["gap_rejected_count"], 118)
        self.assertEqual(len(certificates), 1)
        survivor = receipt["survivors"][0]
        self.assertEqual((survivor["removed"], survivor["inserted"]), ([2, 3], [11, 13]))
        self.assertEqual(survivor["exact_maxmin"]["gamma"], [1, 8])
        self.assertTrue(verify_cover(certificates[survivor["certificate"]], require_counterexample=False)["accepted"])

    def test_nonprimitive_source_and_empty_classifications(self):
        receipt, certificates = complete_census(5)
        self.assertEqual(receipt["survivor_count"], 1)
        survivor = receipt["survivors"][0]
        self.assertEqual(survivor["velocities"], [2, 4, 6, 8])
        self.assertEqual(survivor["exact_maxmin"]["gamma"], [1, 5])
        self.assertEqual(certificates[survivor["certificate"]]["velocity_gcd"], 2)
        for n in (6, 7, 9):
            receipt, certificates = complete_census(n)
            self.assertTrue(receipt["complete"])
            self.assertEqual(receipt["survivor_count"], 0)
            self.assertEqual(certificates, {})

    def test_explicit_budget_failure_cannot_return_complete(self):
        with self.assertRaisesRegex(ValueError, "exceeding budget"):
            complete_census(8, max_domain_candidates=158144)
        with self.assertRaisesRegex(ValueError, "enumeration budget"):
            residual_gaps(8, (1, 4, 5, 6, 7, 11), max_intervals=2)

    def test_source_and_exact_input_rejections(self):
        for value in (True, 8.0):
            with self.assertRaises(TypeError):
                complete_census(value)
        with self.assertRaises(ValueError):
            complete_census(4)
        with self.assertRaises(ValueError):
            residual_gaps(8, (1, 1))
        with self.assertRaises(TypeError):
            single_band_winding(8, 13, 0.1, F(1, 4))
        with self.assertRaises(ValueError):
            gap_velocity_cap(8, [])


if __name__ == "__main__":
    unittest.main()
