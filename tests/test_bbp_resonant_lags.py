"""Independent rational controls for lag-filter state and prime birth debt."""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.bbp_resonant_lags import (
    lag_filter, filter_state_multiplier, source_filter_passport,
    prime_filter_passport, mixed_forcing_moment, mixed_tail_interval,
    mixed_tail_beta_bounds, mixed_tail_simple_upper,
    mixed_character_transport_upper,
)
from observational_succ.bbp_source_memory import tail_interval
from observational_succ.pi_pascal_kernel import tail_pascal_interval


def original_forcing(n):
    # Intentionally a literal independent four-denominator implementation.
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def states(count, initial=Q()):
    out = [initial]
    for n in range(1, count+1):
        out.append(16*out[-1]+original_forcing(n))
    return out


def repeated_difference(values, lags):
    for lag in lags:
        values = [values[j+lag]-values[j] for j in range(len(values)-lag)]
    return values


class ResonantLagTests(unittest.TestCase):
    def test_filter_by_independent_repeated_differences(self):
        for order in (1, 2, 3):
            for lags in product((1, 2, 3), repeat=order):
                data = source_filter_passport(3, lags)
                oracle = repeated_difference(states(3+sum(lags)), lags)[3]
                self.assertEqual(data["filtered_state"], oracle)
                self.assertEqual(sum(c*16**j for j, c in
                                     enumerate(lag_filter(lags))),
                                 filter_state_multiplier(lags))
                self.assertGreater(filter_state_multiplier(lags), 0)

    def test_lags_keep_initial_state_dependency(self):
        for lags in ((1,), (2,), (2, 3), (1, 2, 3)):
            zero = repeated_difference(states(sum(lags)), lags)[0]
            changed = repeated_difference(states(sum(lags), Q(1, 7)), lags)[0]
            self.assertEqual(changed-zero, Q(filter_state_multiplier(lags), 7))
            self.assertNotEqual(changed, zero)

    def test_old_prime_resonance_and_fresh_prime_same_lag(self):
        # ord_17(16)=2. At n=4, the same difference U_6-U_4 kills
        # the old 17-clock but contains newly born 41-clock residue 4.
        old = prime_filter_passport(17, 4, (2,))
        fresh = prime_filter_passport(41, 4, (2,))
        self.assertEqual(old["residue"], 0)
        self.assertEqual(fresh["residue"], 4)
        self.assertTrue(fresh["fresh_last_endpoint"])
        self.assertEqual(old["filtered_phase"], fresh["filtered_phase"])

    def test_fresh_endpoint_survives_every_tested_mixed_order(self):
        for prime in (41, 73, 89, 97, 113, 137, 193, 257):
            n0 = (prime+7)//8
            for lags in ((1,), (2,), (1, 2), (2, 2), (1, 2, 3)):
                if sum(lags) <= n0:
                    row = prime_filter_passport(prime, n0-sum(lags), lags)
                    self.assertEqual(row["residue"], 4)

    def test_all_birth_cut_positions(self):
        for prime in (17, 41, 73):
            n0 = (prime+7)//8
            for lags in ((1,), (2,), (1, 2), (2, 2)):
                for start in range(max(0, n0-sum(lags)-1), n0+2):
                    if start+sum(lags) >= n0+3*((prime-1)//8):
                        continue
                    row = prime_filter_passport(prime, start, lags)
                    if row["last"] < n0:
                        self.assertEqual(row["residue"], 0)
                    if start >= n0:
                        self.assertEqual(row["residue"],
                                         4*pow(16, start-n0, prime)
                                         *filter_state_multiplier(lags) % prime)

    def test_mixed_forcing_is_positive_authentic_signed_difference(self):
        for start in (0, 1, 3, 17, 61):
            for lags in ((1,), (3,), (1, 2), (2, 3), (1, 1, 2)):
                oracle = repeated_difference(
                    [original_forcing(start+j+1)
                     for j in range(sum(lags)+1)], lags)[0]
                moment = mixed_forcing_moment(start, lags)
                self.assertEqual(moment, (-1)**len(lags)*oracle)
                self.assertGreater(moment, 0)
                self.assertLess(mixed_forcing_moment(start+1, lags), moment)

    def test_mixed_tail_contains_independent_completed_source_interval(self):
        for start in (0, 1, 7, 20):
            for lags in ((1,), (2,), (1, 2), (2, 3), (1, 2, 3)):
                direct = repeated_difference(states(start+sum(lags)), lags)[start]
                alpha_lo, alpha_hi = tail_interval(0, start+sum(lags)+14)
                multiplier = filter_state_multiplier(lags)*16**start
                lo, hi = multiplier*alpha_lo-direct, multiplier*alpha_hi-direct
                if len(lags) % 2:
                    lo, hi = -hi, -lo
                mixed_lo, mixed_hi = mixed_tail_interval(start, lags, 7)
                self.assertLess(lo, mixed_hi)
                self.assertLess(mixed_lo, hi)
                beta_lo, beta_hi = mixed_tail_beta_bounds(start, lags)
                self.assertLess(beta_lo, lo)
                self.assertLess(hi, beta_hi)
                self.assertLess(hi, mixed_tail_simple_upper(start, lags))

    def test_unit_lags_recover_existing_pascal_tail(self):
        for start in (0, 2, 11):
            for order in (1, 2, 3, 4):
                self.assertEqual(mixed_tail_interval(start, (1,)*order, 5),
                                 tail_pascal_interval(start, order, 5))

    def test_interval_tightening_and_polynomial_lag_cost(self):
        for lags in ((2,), (1, 3), (2, 3, 4)):
            a, b = mixed_tail_interval(5, lags, 2)
            c, d = mixed_tail_interval(5, lags, 4)
            self.assertTrue(0 < a < c < d < b)
        self.assertLess(mixed_tail_simple_upper(100, (100,)), Q(1, 640000))
        self.assertEqual(mixed_character_transport_upper(1, 10, (2,), 0), 0)
        self.assertEqual(mixed_character_transport_upper(1, 0, (2,), 1), 0)
        self.assertGreater(mixed_character_transport_upper(1, 10, (2,), 1), 0)

    def test_mutated_source_does_not_pass_four_pole_oracle(self):
        # One signed source coefficient is changed from -1 to -2.
        mutated = Q()
        authentic = Q()
        for n in range(1, 7):
            authentic = 16*authentic+original_forcing(n)
            mutated = 16*mutated+original_forcing(n)-Q(1, 8*n-2)
        self.assertNotEqual(authentic, mutated)
        self.assertNotEqual((authentic-mutated) % 1, 0)

    def test_domain_and_boundary_controls(self):
        for bad in ((), (0,), (-1,), (True,), [1]):
            with self.assertRaises(ValueError):
                lag_filter(bad)
        for prime in (3, 5, 9, 25):
            with self.assertRaises(ValueError):
                prime_filter_passport(prime, 0, (1,))
        with self.assertRaises(ValueError):
            prime_filter_passport(17, 8, (1,))
        with self.assertRaises(ValueError):
            mixed_tail_interval(0, (1,), 0)
        with self.assertRaises(ValueError):
            mixed_character_transport_upper(0, 1, (1,), 1.0)


if __name__ == "__main__":
    unittest.main()
