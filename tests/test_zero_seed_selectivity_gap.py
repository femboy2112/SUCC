"""Exact tests for the zero-seed selectivity gap (Front F crux)."""
import unittest
from fractions import Fraction as Q

from observational_succ import zero_seed_selectivity_gap as zsg


class ZeroSeedSelectivityTests(unittest.TestCase):
    def test_shadow_gap_positive(self):
        # The shadow is NOT the zero orbit: the gap is strictly positive.
        for A in (10, 50, 100):
            gap = zsg.shadow_gap_bound(A, 1217)
            self.assertGreater(gap, 0)

    def test_shadow_digit_gap_below_one_sixteenth(self):
        # The scaled completed-digit gap stays < 1/16, so all digits vanish.
        for A in (10, 50, 100):
            dgap = zsg.completed_digit_gap(A, 1217)
            self.assertLess(dgap, Q(1, 16), A)

    def test_gap_is_astronomically_small(self):
        # The gap decays faster than any power of A (exponentially in A).
        g10 = zsg.shadow_gap_bound(10, 1217)
        g20 = zsg.shadow_gap_bound(20, 1217)
        self.assertLess(g20, g10 / 1000)

    def test_universal_diophantine_necessity_is_withdrawn(self):
        s = zsg.separation_requires_irrationality_measure()
        self.assertIn('WITHDRAWN', s)
        self.assertIn('not required', s)

    def test_seed_difference_is_exact_without_pi(self):
        from observational_succ.duck_bbp import forcing
        for seed in (Q(1, 5), Q(-19, 113), Q(1, 16)):
            original, shadow = Q(), seed
            for n in range(20):
                self.assertEqual(shadow-original, zsg.exact_seed_separation(n, seed))
                original = 16*original+forcing(n+1)
                shadow = 16*shadow+forcing(n+1)

    def test_circle_alias_does_not_erase_source_seed(self):
        self.assertEqual(zsg.exact_seed_separation(1, Q(1, 16)) % 1, 0)
        self.assertNotEqual(zsg.exact_seed_separation(0, Q(1, 16)), 0)


if __name__ == '__main__':
    unittest.main()
