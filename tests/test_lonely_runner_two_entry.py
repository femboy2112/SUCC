from dataclasses import replace
from fractions import Fraction as F
from math import lcm
import unittest

from observational_succ.lonely_runner_two_entry import (
    all_retained, centre_divisibility, circle_distance, effective_bounds,
    general_effective_bounds, general_single_insert_hole, occupancy_upper_bound,
    periodic_occupancy, retained, safe_radius, single_insert_hole,
    uncovered_intervals,
)


class TwoEntryTests(unittest.TestCase):
    def test_general_single_insert_holes_and_source_endpoint_spacing(self):
        for n in range(5, 13):
            for r1 in range(1, n - 1):
                for r2 in range(r1 + 1, n):
                    for w in (n, n + 1, 2 * n, 3 * n + 1):
                        witness = general_single_insert_hole(n, r1, r2, w)
                        self.assertTrue(witness.verify(), (n, r1, r2, w))
                        gaps = uncovered_intervals(n, all_retained(n, r1, r2) + (w,))
                        self.assertTrue(all(b - a >= F(1, n * w * (n - 1)) for a, b in gaps))
                    base_gaps = uncovered_intervals(n, all_retained(n, r1, r2))
                    self.assertTrue(base_gaps)
                    self.assertTrue(all(b - a >= F(1, n * (n - 1)**2) for a, b in base_gaps))

    def test_general_bound_includes_sporadic_middle_range(self):
        self.assertEqual(uncovered_intervals(8, (1, 4, 5, 6, 7, 11, 13)), ())
        self.assertEqual(uncovered_intervals(5, (2, 4, 6, 8)), ())
        nonprimitive = general_effective_bounds(5, 1, 3)
        self.assertLess(6, nonprimitive["first_strict_bound"])
        self.assertLessEqual(8, nonprimitive["second_multiplier"] * 6)
        bounds = general_effective_bounds(8, 2, 3)
        self.assertLess(11, bounds["first_strict_bound"])
        self.assertLessEqual(13, bounds["second_multiplier"] * 11)
        for n in range(5, 250):
            bounds = general_effective_bounds(n, 1, n - 1)
            self.assertLess(bounds["first_strict_bound"], 8 * n**2)
            self.assertLessEqual(bounds["first_strict_bound"], bounds["uniform_first_strict_bound"])
            self.assertLess(bounds["w1_max"], bounds["first_strict_bound"])
            self.assertGreaterEqual(bounds["w1_max"] + 1, bounds["first_strict_bound"])
            self.assertLess(bounds["w2_max"], 4 * n**3)
            expected = F(56) if n == 5 else F(60) if n == 6 else F((n-2)**2*(n-1), n-4)
            self.assertEqual(bounds["uniform_first_strict_bound"], expected)

    def test_general_hole_sporadic_one_entry_collision_controls(self):
        # One of the two supplemented sets is classically tight; the other
        # deletion still forces a strict hole in the smaller actual set.
        for n, w in ((5, 7), (6, 9)):
            for r in range(1, n):
                if r != 2:
                    a, b = sorted((2, r))
                    self.assertTrue(general_single_insert_hole(n, a, b, w).verify())

    def test_single_insert_hole_all_three_branches(self):
        branches = set()
        for n in range(5, 22):
            for r1 in range((n - 1) // 2 + 1, n - 1):
                for r2 in range(r1 + 1, n):
                    for w in list(range(n, 2 * n)) + [lcm(r1, r2), 2 * lcm(r1, r2)]:
                        witness = single_insert_hole(n, r1, r2, w)
                        self.assertTrue(witness.verify(), (n, r1, r2, w, witness))
                        branches.add(witness.strategy)
        self.assertEqual(len(branches), 3)

    def test_common_multiple_at_large_exact_scale(self):
        witness = single_insert_hole(74, 70, 72, lcm(70, 72) * 10**40)
        self.assertTrue(witness.verify())
        self.assertGreater(witness.margin, F(1, 74))
        self.assertFalse(replace(witness, time=F(1, 70)).verify())

    def test_periodic_discrepancy_and_sharp_constant(self):
        for n in range(5, 13):
            for v in range(1, 12):
                for a, b in ((F(-7, 13), F(8, 11)), (F(1, 17), F(1, 5)),
                             (F(0), F(3)), (F(1, 4), F(1, 4))):
                    self.assertLessEqual(periodic_occupancy(n, v, a, b),
                                         occupancy_upper_bound(n, v, b - a))
                a, b = F(-1, n * v), F(1, n * v)
                occupancy = periodic_occupancy(n, v, a, b)
                self.assertEqual(occupancy, b - a)
                self.assertEqual(occupancy, occupancy_upper_bound(n, v, b - a))
                self.assertGreater(occupancy, 2 * (b - a) / n)  # boundary-free mutant

    def test_all_gap_components_have_quantized_width(self):
        for n in range(5, 13):
            for r1 in range((n - 1) // 2 + 1, n - 1):
                for r2 in range(r1 + 1, n):
                    for w in (n, 2 * n + 1, lcm(r1, r2)):
                        gaps = uncovered_intervals(n, retained(n, r1, r2) + (w,))
                        self.assertTrue(gaps)
                        self.assertTrue(all(b - a >= F(1, n * w * (n - 1)) for a, b in gaps))
                        t = single_insert_hole(n, r1, r2, w).time
                        self.assertTrue(any(a < t < b for a, b in gaps))

    def test_known_infinite_family_members_obey_bounds_and_cover(self):
        for n in (74, 284):
            r1, r2 = n - 4, n - 2
            w1, w2 = 2 * r1, 2 * r2
            speeds = retained(n, r1, r2) + (w1, w2)
            self.assertEqual(uncovered_intervals(n, speeds), ())
            self.assertTrue(centre_divisibility(n, r1, r2, w1, w2))
            bounds = effective_bounds(n, r1, r2)
            self.assertLess(w1, bounds["first_strict_bound"])
            self.assertLessEqual(w2, bounds["second_multiplier"] * w1)

    def test_integer_bounds_and_cubic_corollary(self):
        for n in range(5, 120):
            for r1 in range((n - 1) // 2 + 1, n - 1):
                bounds = effective_bounds(n, r1, r1 + 1)
                bound = bounds["first_strict_bound"]
                self.assertLess(bounds["w1_max"], bound)
                self.assertGreaterEqual(bounds["w1_max"] + 1, bound)
                self.assertLess(bound, 2 * n**2)
                self.assertLess(bounds["w2_max"], 4 * n**3)

    def test_safe_interval_at_both_centres(self):
        for n, r1, r2 in ((5, 3, 4), (8, 5, 7), (74, 70, 72)):
            for r in (r1, r2):
                for sign in (-1, 1):
                    t = F(1, r) + sign * safe_radius(n, r) * F(999, 1000)
                    self.assertGreater(min(circle_distance(v * t) for v in retained(n, r1, r2)), F(1, n))

    def test_source_and_domain_controls(self):
        # The known middle-range sporadic example has neither replacement even.
        self.assertEqual(uncovered_intervals(8, (1, 4, 5, 6, 7, 11, 13)), ())
        with self.assertRaises(ValueError):
            centre_divisibility(8, 2, 3, 11, 13)
        for args in ((4, 2, 3), (8, 3, 7), (8, 5, 5), (8, 5, 8)):
            with self.assertRaises(ValueError):
                effective_bounds(*args)
        with self.assertRaises(TypeError):
            effective_bounds(True, 3, 4)
        with self.assertRaises(TypeError):
            periodic_occupancy(5, 2, 0.0, F(1))
        with self.assertRaises(ValueError):
            uncovered_intervals(5, (1, 2, 3), max_intervals=2)


if __name__ == "__main__":
    unittest.main()
