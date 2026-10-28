"""Independent exact holdouts for the mixed-lag signed-loss instruments.

These tests certify finite arithmetic and source authentication. They do not
instantiate the paper theorem's unspecified universal Diophantine onset.
"""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.mixed_lag_coercivity import (
    authentic_mixed_window, conditional_mixed_lag_budget,
    diophantine_exponent_margin, finite_tail_holdout, lag_multiplier,
    scale_requirement, tail_transport_upper, verify_authentic_mixed_window,
)


def independent_source(n):
    """Collapsed rational identity, independent of the four-pole adapter."""
    j = n - 1
    return Q(120*j*j + 151*j + 47,
             (2*j+1)*(4*j+3)*(8*j+1)*(8*j+5))


def independent_state(n, source=independent_source):
    return sum((16**(n-k)*source(k) for k in range(1, n+1)), Q())


def subset_coefficients(lags):
    """Subset expansion, not the production polynomial multiplication."""
    result = {}
    for chosen in product((0, 1), repeat=len(lags)):
        index = sum(lag for lag, bit in zip(lags, chosen) if bit)
        sign = (-1)**(len(lags)-sum(chosen))
        result[index] = result.get(index, 0) + sign
    return result


def literal_difference(function, start, lags):
    """Apply successive forward differences to the actual value list."""
    values = [function(start+j) for j in range(sum(lags)+1)]
    for lag in lags:
        values = [values[j+lag]-values[j]
                  for j in range(len(values)-lag)]
    return values[0]


def independent_positive_moment(start, lags):
    return (-1)**len(lags)*literal_difference(
        lambda n: independent_source(n+1), start, lags)


def independent_tail_interval(start, lags, terms):
    moments = [independent_positive_moment(start+j, lags)
               for j in range(terms+1)]
    lower = sum((moments[j]/16**(j+1) for j in range(terms)), Q())
    return lower, lower + moments[-1]/(15*16**terms)


class MixedLagCoercivityTests(unittest.TestCase):
    def test_multiplier_matches_independent_subset_expansion(self):
        for lags in ((1,), (1, 1, 2), (2, 5), (1,)*8, (4, 7, 11)):
            coefficients = subset_coefficients(lags)
            expected = sum(c*16**j for j, c in coefficients.items())
            self.assertEqual(lag_multiplier(lags), expected)
            self.assertGreater(expected, 0)
            self.assertLess(expected, 16**sum(lags))

    def test_unwrapped_zero_source_replayed_by_closed_sum(self):
        start, length, lags = 3, 7, (1, 2, 4)
        values = authentic_mixed_window(start, length, lags)
        expected = tuple(literal_difference(independent_state, n, lags)
                         for n in range(start, start+length))
        self.assertEqual(values, expected)
        self.assertTrue(all(type(x) is Q for x in values))
        verify_authentic_mixed_window(values, start, length, lags)

    def test_integer_lift_mutation_rejected_despite_equal_circle_phase(self):
        values = authentic_mixed_window(4, 3, (2, 3))
        mutant = (values[0]+1,) + values[1:]
        self.assertEqual(mutant[0] % 1, values[0] % 1)
        with self.assertRaises(ValueError):
            verify_authentic_mixed_window(mutant, 4, 3, (2, 3))

    def test_same_forcing_changed_seed_rejected(self):
        start, length, lags, seed = 2, 5, (1, 3), Q(1, 17)
        values = authentic_mixed_window(start, length, lags)
        altered = tuple(literal_difference(
            lambda n: independent_state(n)+16**n*seed, n, lags)
            for n in range(start, start+length))
        for index, (actual, changed) in enumerate(zip(values, altered)):
            self.assertEqual(changed-actual,
                             seed*16**(start+index)*lag_multiplier(lags))
        with self.assertRaises(ValueError):
            verify_authentic_mixed_window(altered, start, length, lags)

    def test_missing_signed_pole_and_zero_forcing_rejected(self):
        start, length, lags = 3, 4, (1, 2)
        def mutant_source(n):
            return independent_source(n) + Q(1, 8*n-3)
        mutant = tuple(literal_difference(
            lambda k: independent_state(k, mutant_source), n, lags)
            for n in range(start, start+length))
        for candidate in (mutant, (Q(),)*length):
            with self.assertRaises(ValueError):
                verify_authentic_mixed_window(candidate, start, length, lags)

    def test_frequency_log_boundaries_and_sign(self):
        for exponent in (1, 3, 11):
            for h, ceiling in ((16**exponent-1, exponent),
                               (16**exponent, exponent),
                               (16**exponent+1, exponent+1)):
                expected = 60*(1000+ceiling)
                self.assertEqual(scale_requirement(1, 1000, h), expected)
                self.assertEqual(scale_requirement(1, 1000, -h), expected)
                self.assertEqual(tail_transport_upper(71, -h),
                                 tail_transport_upper(71, h))

    def test_joint_diophantine_margin_at_schedule_endpoint(self):
        for period, lags, h in ((1, (1,), 1), (7, (2, 3), -17),
                                (1, (1000,), 16**17+1)):
            scale = scale_requirement(period, sum(lags), h)
            margin = diophantine_exponent_margin(scale, period, lags, h)
            self.assertGreaterEqual(2*margin, scale)
            self.assertLess(abs(h)*lag_multiplier(lags),
                            16**((scale-margin-15*period)//15))
            with self.assertRaises(ValueError):
                diophantine_exponent_margin(scale-1, period, lags, h)

    def test_geometric_block_schedule_has_exact_boundary(self):
        for horizon, blocks in ((8**5-1, 0), (8**5, 1),
                                (8**6-1, 1), (8**6, 2)):
            budget = conditional_mixed_lag_budget(horizon, 1, 1, -1, 4)
            self.assertEqual(budget.first_exponent, 4)
            self.assertEqual(budget.first_scale, 4096)
            self.assertEqual(budget.eligible_blocks, blocks)
            self.assertEqual(budget.transport_debt,
                             Q(11, 112*4096) if blocks else Q())
            expected = Q(horizon)-Q(blocks, 14)+budget.transport_debt
            self.assertEqual(budget.modulus_sum_upper, expected)
            self.assertFalse(budget.numerical_onset_certified)

    def test_high_order_tail_with_independent_infinite_remainder(self):
        cases = ((1, (1,)*12), (17, (1,)*8),
                 (31, (7, 13, 29)), (7, (1, 2, 3, 9)))
        for start, lags in cases:
            short = finite_tail_holdout(start, lags, 3)
            long = finite_tail_holdout(start, lags, 9)
            for terms, record in ((3, short), (9, long)):
                low, high = independent_tail_interval(start, lags, terms)
                self.assertEqual((record['lower'], record['upper']),
                                 (low, high))
                self.assertGreater(low, 0)
                self.assertLess(low, high)
                self.assertLess(high, Q(1, 64*start**2))
                self.assertTrue(record['infinite_remainder_included'])
                self.assertTrue(record['finite_interval_inside_bound'])
            self.assertLess(short['lower'], long['lower'])
            self.assertLess(long['upper'], short['upper'])

    def test_mixed_tail_is_less_than_authentic_undifferenced_tail(self):
        for start, lags in ((1, (1,)), (7, (1,)*10), (31, (3, 17))):
            mixed = finite_tail_holdout(start, lags, 9)
            original_lower = sum((independent_source(start+j)/16**j
                                  for j in range(1, 10)), Q())
            self.assertLess(mixed['upper'], original_lower)

    def test_transport_pays_entire_future_not_just_sampled_terms(self):
        start, end, h, lags = 11, 23, -7, (1, 1, 5, 9)
        finite_debt = Q(44*abs(h), 7)*sum(
            (independent_tail_interval(n, lags, 6)[1]
             for n in range(start+1, end+1)), Q())
        future_debt = tail_transport_upper(end, h)
        self.assertLess(finite_debt+future_debt,
                        tail_transport_upper(start, h))
        self.assertGreater(future_debt, 0)

    def test_uncompleted_comparison_loses_exponential_counterterm(self):
        start, lags = 3, (7, 13)
        value = authentic_mixed_window(start, 1, lags)[0]
        multiplier = lag_multiplier(lags)
        wrong_comparison = value-multiplier*independent_state(start)
        self.assertGreater(abs(wrong_comparison), 16**sum(lags)//10000)
        holdout = finite_tail_holdout(start, lags, 9)
        self.assertLess(holdout['upper'], Q(1, 64*start**2))
        # P(E)U-AU=A*T-P(E)T. The discarded term is exactly A*T.
        base_low = sum((independent_source(start+j)/16**j
                        for j in range(1, 10)), Q())
        base_high = base_low+independent_source(start+10)/(15*16**9)
        self.assertLess(multiplier*base_low-holdout['upper'],
                        wrong_comparison)
        self.assertLess(wrong_comparison,
                        multiplier*base_high-holdout['lower'])

    def test_conditional_budget_never_claims_computed_arithmetic_onset(self):
        budget = conditional_mixed_lag_budget(8**9, 1, 1, 1, 4)
        self.assertFalse(budget.numerical_onset_certified)
        self.assertEqual(budget.threshold_exponent, 4)
        with self.assertRaises(ValueError):
            conditional_mixed_lag_budget(8**9, 1, 1, 1, 3)

    def test_domains_and_finite_replay_limits(self):
        for lags in ((), [1], (0,), (-1,), (True,)):
            with self.assertRaises(ValueError):
                lag_multiplier(lags)
        for h in (0, True, Q(1)):
            with self.assertRaises(ValueError):
                tail_transport_upper(1, h)
        with self.assertRaises(ValueError):
            authentic_mixed_window(1999, 1, (1,))
        with self.assertRaises(ValueError):
            finite_tail_holdout(1999, (1,), 1)


if __name__ == '__main__':
    unittest.main()
