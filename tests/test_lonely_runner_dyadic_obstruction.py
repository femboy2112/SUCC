from fractions import Fraction as F
import unittest

from observational_succ.lonely_runner_uniform import (
    AffineRunner, check_local_uniform, poliakova_rule,
)
from scripts.lonely_runner_dyadic_probe import (
    endpoint_capacity, fixed_support_capacity_maximum, sharp_rule,
)


class DyadicEndpointTests(unittest.TestCase):
    def test_sharp_construction_all_cells_including_composite_odd_parts(self):
        for d in (1, 3, 5, 9, 15, 45):
            rule = sharp_rule(d)
            self.assertTrue(check_local_uniform(rule)["local_uniform"])
            self.assertEqual(len(rule.added), 2 * len(rule.removed))
            self.assertEqual([endpoint_capacity(rule.affected, v) for v in rule.added],
                             [F(1, 2), F(1, 2)])

    def test_smallest_level_uses_both_parities(self):
        # k=0 at q=2 and even units at q=2d are essential, not discarded.
        for d in (1, 3, 5, 15):
            q = 2 * d
            for alpha in (F(0), F(1, 2)):
                self.assertEqual(endpoint_capacity((q,), AffineRunner(d, alpha, F(0))),
                                 F(1, 2))

    def test_nonzero_even_phase_resonates_at_one_larger_level(self):
        for d in (1, 3, 15):
            affected = tuple(d * 2**a for a in range(1, 6))
            half = AffineRunner(2*d, F(1, 2), F(0))
            quarter = AffineRunner(2*d, F(1, 4), F(0))
            self.assertEqual(endpoint_capacity(affected, half), F(1))
            self.assertEqual(endpoint_capacity(affected, quarter), F(1, 2))
            for q in affected:
                if q != 4*d:
                    self.assertEqual(endpoint_capacity((q,), half), F(0))
                if q != 8*d:
                    self.assertEqual(endpoint_capacity((q,), quarter), F(0))

    def test_signed_power_endpoint_collisions_are_closed_and_sharp(self):
        affected = (2, 4, 8, 16)
        for beta in (F(0), F(-1), F(1), F(-3), F(3)):
            self.assertEqual(endpoint_capacity(affected, AffineRunner(8, F(0), beta)),
                             F(1))
        for beta in (F(-300), F(300)):
            self.assertEqual(endpoint_capacity(affected, AffineRunner(8, F(0), beta)),
                             F(0))

    def test_complete_phase_maxima_on_fixed_sparse_supports(self):
        for d in (1, 3, 5):
            for levels in ((1, 2, 3), (1, 3, 5), (2, 4)):
                affected = tuple(d * 2**a for a in levels)
                for velocity in affected + (1, 3, 5, 3*d, 9*d):
                    maximum, witness = fixed_support_capacity_maximum(affected, velocity)
                    expected = F(1) if velocity % 2 == 0 else F(1, 2)
                    self.assertLessEqual(maximum, expected, (affected, witness))

    def test_two_odd_parts_are_an_actual_countermodel(self):
        published = poliakova_rule()
        self.assertTrue(check_local_uniform(published)["local_uniform"])
        self.assertGreater(published.gain, 0)
        self.assertLess(len(published.added), 2 * len(published.removed))
        v12 = next(v for v in published.rephased if v.velocity == 12)
        self.assertEqual(endpoint_capacity(published.affected, v12), F(3, 2))

    def test_parity_and_odd_addition_hypotheses_are_necessary(self):
        # A wrong gcd(k,q) filter would retain only k=1 and miss k=0 at q=2.
        runner = AffineRunner(1, F(1, 2), F(0))
        self.assertEqual((F(runner.velocity, 2) + runner.alpha).denominator, 1)
        self.assertNotEqual(runner.alpha.denominator, 1)
        self.assertEqual(endpoint_capacity((2,), runner), F(1, 2))
        # Even additions are illegal in the source convention. If allowed,
        # this one runner would cover every q=4 tangent cell, with capacity 1.
        illegal_even_addition = AffineRunner(2, F(1, 2), F(0))
        self.assertEqual(endpoint_capacity((4,), illegal_even_addition), F(1))

    def test_domain_controls(self):
        for d in (0, 2, -1, True, 1.0):
            with self.assertRaises(ValueError):
                sharp_rule(d)
        for affected in ((), (1,), (2, 2), (2, 3), (True,)):
            with self.assertRaises(ValueError):
                endpoint_capacity(affected, AffineRunner(1, F(0), F(0)))


if __name__ == "__main__":
    unittest.main()
