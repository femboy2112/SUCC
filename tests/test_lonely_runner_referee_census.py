from fractions import Fraction as F
from itertools import combinations
import unittest

from observational_succ.lonely_runner_referee_census import (
    baseline_first_bound, center_modulus, complete_referee_census, intersect_integer_good_bands,
)
from observational_succ.lonely_runner_census import complete_census, residual_gaps
from observational_succ.lonely_runner_census import gap_velocity_cap, single_band_winding
from observational_succ.lonely_runner_two_entry import general_effective_bounds
from scripts.lonely_runner_referee_fraction import (
    fraction_census, known_controls, source_gaps, subtract_source_bands,
)


class RefereeCensusTests(unittest.TestCase):
    def test_cached_integer_intersection_matches_two_fraction_paths(self):
        for n in (5, 8, 13):
            for r1, r2 in combinations(range(1, n), 2):
                source = tuple(v for v in range(1, n) if v not in (r1, r2))
                baseline = residual_gaps(n, source)
                for w in (n, n+3, 3*n+1):
                    expected = source_gaps(n, source+(w,))
                    self.assertEqual(intersect_integer_good_bands(n, baseline, w), expected)
                    self.assertEqual(subtract_source_bands(n, baseline, w), expected)

    def test_new_complete_replay_matches_original_and_independent(self):
        for n in (5, 8, 10):
            actual, _ = complete_referee_census(n)
            old, _ = complete_census(n, max_domain_candidates=1000000)
            other = fraction_census(n)
            self.assertEqual(actual["proved_domain_count"], old["proved_finite_domain_candidate_count"])
            project = lambda xs: [(x["removed"], x["inserted"]) for x in xs]
            self.assertEqual(project(actual["survivors"]), project(old["survivors"]))
            self.assertEqual(project(actual["survivors"]), project(other["survivors"]))

    def test_center_filter_includes_common_multiple_and_lower_chain(self):
        self.assertEqual(center_modulus(8, (5, 7), (1, 2, 3, 4, 6), 35)[0], 1)
        self.assertEqual(center_modulus(8, (5, 7), (1, 2, 3, 4, 6), 10)[0], 7)
        self.assertEqual(center_modulus(8, (3, 6), (1, 2, 4, 5, 7), 8)[0], 6)

    def test_closed_boundaries_and_pruning_strictness(self):
        self.assertEqual(subtract_source_bands(8, ((F(7, 104), F(9, 104)),), 13), ())
        self.assertNotEqual(subtract_source_bands(8, ((F(7, 104), F(9, 104)+F(1, 10**40)),), 13), ())
        self.assertEqual(baseline_first_bound(8, ((F(0), F(1, 8)),)), F(6))
        with self.assertRaisesRegex(ValueError, "budget"):
            complete_referee_census(8, max_domain_candidates=158144)

    def test_required_known_controls_full_fraction_unions(self):
        controls = known_controls()
        self.assertEqual([x["n"] for x in controls], [5, 8, 74, 284])
        self.assertTrue(all(x["full_fraction_cover"] for x in controls))

    def test_known_large_positives_survive_every_new_pruning_stage(self):
        for n in (74, 284):
            removed = (n-4, n-2)
            w1, w2 = (2*r for r in removed)
            source = tuple(v for v in range(1, n) if v not in removed)
            baseline = residual_gaps(n, source)
            self.assertLess(w1, baseline_first_bound(n, baseline))
            self.assertLessEqual(w1, general_effective_bounds(n, *removed)["w1_max"])
            residual = intersect_integer_good_bands(n, baseline, w1)
            self.assertLessEqual(w2, gap_velocity_cap(n, residual))
            modulus, _ = center_modulus(n, removed, source, w1)
            self.assertEqual(w2 % modulus, 0)
            self.assertTrue(all(single_band_winding(n, w2, a, b) is not None for a, b in residual))


if __name__ == "__main__":
    unittest.main()
