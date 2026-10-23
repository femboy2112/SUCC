"""Small exact controls for the restricted continuum identifiability theorem."""
import unittest
from fractions import Fraction as Q
from observational_succ.reality_pin_continuum import (
    ContinuumError, exp_interval, invert_ratio_interval, known_capacity_pin,
    line_invariants, line_response_interval, ratio_interval, sqrt_interval,
)


class ContinuumLineTests(unittest.TestCase):
    def test_taylor_oracle_has_independent_rational_exponential_sandwich(self):
        # e=sum 1/n!: first 7 terms exceed 2.718; elementary geometric
        # tail after n=6 proves e<2.719, independently of the implementation.
        lo, hi = exp_interval(1, Q(1, 10**10))
        self.assertGreater(lo, Q(2718, 1000))
        self.assertLess(hi, Q(2719, 1000))
        self.assertLessEqual(hi-lo, Q(1, 10**10))
        self.assertEqual(exp_interval(0, Q(1, 100)), (1, 1))

    def test_certified_coth_ratio_and_monotonicity(self):
        lo, hi = ratio_interval(1, Q(1, 10**9))
        self.assertGreater(lo, Q(1313035, 10**6))
        self.assertLess(hi, Q(1313036, 10**6))
        self.assertLessEqual(hi-lo, Q(1, 10**9))
        self.assertEqual(ratio_interval(0), (1, 1))
        points = (Q(1, 10), Q(1, 2), Q(1), Q(2), Q(3))
        bands = [ratio_interval(x) for x in points]
        self.assertTrue(all(x[1] < y[0] for x, y in zip(bands, bands[1:])))

    def test_inverse_certificate_brackets_declared_rational_ratio(self):
        lo, hi = invert_ratio_interval(Q(3, 2), Q(1, 100000))
        self.assertLessEqual(hi-lo, Q(1, 100000))
        self.assertLess(ratio_interval(lo, Q(1, 10**10))[1], Q(3, 2))
        self.assertGreater(ratio_interval(hi, Q(1, 10**10))[0], Q(3, 2))

    def test_known_capacity_dc_and_dynamic_pin_recovers_source_band(self):
        # Exact source a=2,c=3,L=4; s=1/24 gives z=1.
        ratio = ratio_interval(1, Q(1, 10**8))
        pin = known_capacity_pin(Q(1, 2), 3, Q(1, 24), ratio, Q(1, 10**6))
        self.assertLess(pin['length'][0], 4)
        self.assertGreater(pin['length'][1], 4)
        self.assertLess(pin['conductivity'][0], 2)
        self.assertGreater(pin['conductivity'][1], 2)
        self.assertFalse(pin['physical_measurement_authenticated'])
        # Independent held-out Laplace scale s=1/6 gives z=2.
        holdout = line_response_interval(2, 3, 4, Q(1, 6), Q(1, 10**8))
        self.assertGreater(holdout[0], Q(1037314, 10**6))
        self.assertLess(holdout[1], Q(1037315, 10**6))

    def test_unknown_capacity_scale_fiber_is_exact_for_entire_response(self):
        original = line_invariants(2, 3, 4)
        for scale in (Q(1, 3), Q(2), Q(7, 2)):
            self.assertEqual(line_invariants(2*scale, 3/scale, 4*scale), original)
            for s in (0, Q(1, 24), Q(1, 6)):
                self.assertEqual(line_response_interval(2*scale, 3/scale, 4*scale, s),
                                 line_response_interval(2, 3, 4, s))

    def test_incorrect_capacity_prior_changes_inferred_physical_length(self):
        ratio = ratio_interval(1, Q(1, 10**8))
        wrong = known_capacity_pin(Q(1, 2), 6, Q(1, 24), ratio, Q(1, 10**6))
        self.assertLess(wrong['length'][0], 2)
        self.assertGreater(wrong['length'][1], 2)
        self.assertLess(wrong['length'][1], 3)
        self.assertEqual(line_invariants(1, 6, 2), line_invariants(2, 3, 4))

    def test_dc_only_is_insufficient_even_with_known_capacity(self):
        self.assertEqual(line_response_interval(2, 3, 4, 0),
                         line_response_interval(3, 3, 6, 0))
        first = line_response_interval(2, 3, 4, Q(1, 24))
        second = line_response_interval(3, 3, 6, Q(1, 24))
        self.assertLess(first[1], second[0])

    def test_invalid_input_and_exhausted_precision_budget_are_refused(self):
        for f in (lambda: ratio_interval(-1), lambda: invert_ratio_interval(1),
                  lambda: line_invariants(1, 0, 1), lambda: exp_interval(1.0, Q(1, 10)),
                  lambda: exp_interval(100, Q(1, 1000), max_terms=3),
                  lambda: known_capacity_pin(1, 1, 0, (2, 3))):
            with self.assertRaises(ContinuumError):
                f()
        lo, hi = sqrt_interval(2, Q(1, 10000))
        self.assertLessEqual(lo*lo, 2)
        self.assertGreaterEqual(hi*hi, 2)


if __name__ == '__main__':
    unittest.main()
