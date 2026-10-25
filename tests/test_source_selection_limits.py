"""Exact controls for source selection, averaging limits and normalization."""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.pi_source_genesis import machin_pi_interval
from observational_succ.source_selection_limits import (
    RationalInterval, bbp_selection_budget, bbp_selector_interval,
    cylinder_interval, cylinder_mixture_report, interval_haar_tv,
    interval_observable_mean, interval_time_average,
    orbit_observable_enclosure, orbit_observable_mean, parabola_range,
    periodic_parabola, signed_product_variation,
)


class SelectionMemoryTests(unittest.TestCase):
    def test_canonical_cylinders_and_boundary_points(self):
        self.assertEqual(cylinder_interval(2, 3, Q(5, 8)),
                         RationalInterval(Q(5, 8), Q(3, 4)))
        self.assertEqual(cylinder_interval(3, 0, Q(-1, 7)),
                         RationalInterval(0, 1))
        self.assertEqual(cylinder_interval(5, 2, 1),
                         RationalInterval(0, Q(1, 25)))

    def test_periodic_primitive_against_hand_integrals(self):
        whole = RationalInterval(0, 1)
        for base in (2, 3, 5, 16):
            for time in (0, 1, 4):
                self.assertEqual(interval_observable_mean(whole, base, time), Q(1, 6))
        self.assertEqual(interval_observable_mean(RationalInterval(0, Q(1, 2)), 2, 0), Q(1, 6))
        self.assertEqual(interval_observable_mean(RationalInterval(Q(-1, 4), Q(1, 4)), 2, 0), Q(5, 48))

    def test_exact_density_tv_against_independent_piecewise_count(self):
        for interval in (RationalInterval(Q(1, 7), Q(5, 7)),
                         RationalInterval(Q(-1, 3), Q(7, 3)),
                         RationalInterval(0, Q(1, 8))):
            for base, time in product((2, 3, 5), (0, 1, 2)):
                a, b = base**time*interval.left, base**time*interval.right
                cuts = sorted({Q(), Q(1), a % 1, b % 1})
                l1 = Q()
                for lo, hi in zip(cuts, cuts[1:]):
                    mid = (lo+hi)/2
                    count = sum(a <= mid+k < b for k in range(a//1-1, b//1+2))
                    l1 += (hi-lo)*abs(Q(count)/(b-a)-1)
                self.assertEqual(interval_haar_tv(interval, base, time), l1/2)

    def test_every_cylinder_becomes_haar_at_exact_memory_depth(self):
        for base, depth, x in product((2, 3, 16), range(5), (Q(), Q(1, 7), Q(9, 11))):
            interval = cylinder_interval(base, depth, x)
            self.assertEqual(interval_haar_tv(interval, base, depth), 0)
            if depth:
                self.assertEqual(interval_haar_tv(interval, base, depth-1), 1-Q(1, base))

    def test_mixture_identity_on_prescribed_and_held_out_carriers(self):
        for base, depth, horizon, x in product((2, 3, 16, 5), range(5), (1, 3, 8), (Q(), Q(1, 7), Q(4, 13))):
            r = cylinder_mixture_report(base, depth, x, horizon)
            self.assertLessEqual(r['absolute_error'], r['wasserstein_budget'])
            self.assertLessEqual(r['wasserstein_budget'], Q(1, 2*horizon*(base-1)))

    def test_wrong_limit_promotion_fails_on_constant_selected_source(self):
        selected = orbit_observable_mean(0, 16, 64)
        shallow = cylinder_mixture_report(16, 2, 0, 64)
        deep = cylinder_mixture_report(16, 64, 0, 64)
        self.assertEqual(selected, 0)
        self.assertGreater(shallow['interval_mean'], Q(3, 20))
        self.assertLess(deep['interval_mean'], Q(1, 100))
        self.assertGreater(abs(shallow['interval_mean']-selected), shallow['wasserstein_budget'])

    def test_triangular_mixture_retains_periodic_source_weight(self):
        r = cylinder_mixture_report(16, 32, Q(1, 5), 64)
        self.assertEqual(r['selected_fraction'], Q(1, 2))
        self.assertEqual(r['mixture_mean'], Q(1, 2)*Q(4, 25)+Q(1, 12))
        self.assertLessEqual(r['absolute_error'], r['wasserstein_budget'])

    def test_concentration_cost_is_inverse_selected_mass(self):
        for base, depth in product((2, 3, 16), range(7)):
            r = cylinder_mixture_report(base, depth, Q(2, 7), 3)
            self.assertEqual(r['selection_mass']*r['normalized_density_l2_squared'], 1)

    def test_signed_consistency_does_not_bound_total_variation(self):
        weights = (Q(2), Q(-1))
        for depth in range(7):
            masses = []
            for word in product(range(2), repeat=depth):
                value = Q(1)
                for digit in word:
                    value *= weights[digit]
                masses.append(value)
            self.assertEqual(sum(masses, Q()), 1)
            self.assertEqual(sum(map(abs, masses), Q()), 3**depth)
            self.assertEqual(signed_product_variation(weights, depth), 3**depth)
        self.assertEqual(signed_product_variation((Q(1, 3), Q(2, 3)), 100), 1)

    def test_domains_reject_inexact_or_malformed_inputs(self):
        for args in ((1, 2, 0), (2, -1, 0), (2, True, 0), (2, 2, 0.5)):
            with self.assertRaises(ValueError): cylinder_interval(*args)
        for a, b in ((0, 0), (1, 0), (0.0, 1)):
            with self.assertRaises(ValueError): RationalInterval(a, b)
        with self.assertRaises(ValueError): signed_product_variation((2, 1), 3)
        for malformed in (None, {1: 2}, (x for x in (1,))):
            with self.assertRaises(ValueError): signed_product_variation(malformed, 3)
        with self.assertRaises(ValueError): interval_time_average(RationalInterval(0, 1), 2, 0)


class AuthenticBBPSelectionTests(unittest.TestCase):
    def test_first_interval_against_independent_four_pole_value(self):
        self.assertEqual(bbp_selector_interval(0), RationalInterval(0, Q(1, 2)))
        self.assertEqual(bbp_selector_interval(1).left, Q(47, 240))
        self.assertEqual(bbp_selector_interval(1).length, Q(1, 1440))

    def test_source_enclosures_are_strictly_nested_and_contain_machin(self):
        lo, hi = machin_pi_interval(80)
        for depth in (0, 1, 2, 7, 17, 29, 47):
            first, second = bbp_selector_interval(depth), bbp_selector_interval(depth+1)
            self.assertLess(first.left, second.left)
            self.assertLess(second.right, first.right)
            self.assertLess(first.left, lo/16)
            self.assertLess(hi/16, first.right)

    def test_effective_depth_and_uniform_mixture_budget(self):
        for depth, horizon in product((0, 1, 2, 7, 17, 29), (1, 5, 17, 40)):
            r = bbp_selection_budget(depth, horizon)
            k = r['effective_depth']
            interval = r['interval']
            self.assertGreaterEqual(16**k*interval.length, 1)
            self.assertLess(16**(k-1)*interval.length, 1)
            self.assertLessEqual(r['exact_late_tv_budget'], r['geometric_late_budget'])
            self.assertLessEqual(r['total_budget'], r['uniform_budget'])
            self.assertEqual(r['normalized_density_l2_squared'], 16**depth*(8*depth+1)*(8*depth+2))

    def test_source_mixture_against_independent_machin_orbit_enclosure(self):
        lo, hi = machin_pi_interval(80)
        alpha = RationalInterval(lo/16, hi/16)
        for depth, horizon in ((0, 12), (1, 24), (7, 7), (7, 30), (17, 32), (29, 40)):
            r = bbp_selection_budget(depth, horizon)
            length = r['selected_steps']
            a, b = orbit_observable_enclosure(alpha, 16, length)
            weight = r['selected_fraction']
            mixture_lo = weight*a+(1-weight)/6
            mixture_hi = weight*b+(1-weight)/6
            self.assertLessEqual(mixture_lo-r['total_budget'], r['interval_mean'])
            self.assertLessEqual(r['interval_mean'], mixture_hi+r['total_budget'])

    def test_periodic_range_includes_wrap_and_stationary_extrema(self):
        self.assertEqual(parabola_range(RationalInterval(Q(-1, 10), Q(1, 10))), (0, Q(9, 100)))
        self.assertEqual(parabola_range(RationalInterval(Q(2, 5), Q(3, 5))), (Q(6, 25), Q(1, 4)))
        self.assertEqual(parabola_range(RationalInterval(-1, 2)), (0, Q(1, 4)))
        self.assertEqual(periodic_parabola(Q(6, 5)), Q(4, 25))

    def test_invalid_source_depth_and_horizon_fail_closed(self):
        for depth in (-1, True, Q(1), 1.0):
            with self.assertRaises(ValueError): bbp_selector_interval(depth)
        with self.assertRaises(ValueError): bbp_selection_budget(2, 0)


if __name__ == '__main__':
    unittest.main()
