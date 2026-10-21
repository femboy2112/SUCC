"""Independent exact finite controls for Wallis/Kummer/Euler pi transport."""
import unittest
from fractions import Fraction
from math import comb

from observational_succ.pi_prime_carry_transport import (
    central_binomial_by_carries, doubling_carries, wallis_prime_ratio,
    wallis_direct_ratio, wallis_pi_bracket, euler_prime_square_bracket,
    rational_digit_prefix, certified_pi_digit_prefix, wallis_midpoint,
    prime_carry_fourier_transport_error, synchronized_pi_brackets,
    certified_pi_digit_prefix_joint, prime_carry_phase_clock, uniform_fourier_budget,
    dyadic_midpoint_period_floor, long_period_nonmixing_control,
)


def _alternating_arctan_bracket(reciprocal, terms):
    x = Fraction(1, reciprocal)
    partial = sum(((-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
                   for k in range(terms)), Fraction(0))
    next_term = x ** (2 * terms + 1) / (2 * terms + 1)
    return ((partial, partial + next_term) if terms % 2 == 0
            else (partial - next_term, partial))


def _machin_pi_bracket(terms=24):
    a, b = _alternating_arctan_bracket(5, terms)
    c, d = _alternating_arctan_bracket(239, terms)
    return 16 * a - 4 * d, 16 * b - 4 * c


class PiPrimeCarryTransportTests(unittest.TestCase):
    def test_01_kummer_vs_comb_independently(self):
        for n in range(1, 75):
            self.assertEqual(central_binomial_by_carries(n), comb(2 * n, n))

    def test_02_wallis_vs_factorials_independently(self):
        for n in range(1, 75):
            self.assertEqual(wallis_prime_ratio(n), wallis_direct_ratio(n))

    def test_03_carries_detect_prime_power_depth(self):
        sample = next(n for n in range(1, 100) if any(c > 1 for c in doubling_carries(n).values()))
        mutant = 1
        for p in doubling_carries(sample):
            mutant *= p
        self.assertNotEqual(mutant, comb(2 * sample, sample))

    def test_04_wallis_bounds_strict_machin_holdout(self):
        ml, mu = _machin_pi_bracket()
        for n in (1, 2, 3, 5, 10, 32, 64, 256):
            lo, hi = wallis_pi_bracket(n)
            self.assertLess(lo, ml)
            self.assertGreater(hi, mu)
            self.assertEqual(hi - lo, lo / (4 * n + 1))

    def test_05_euler_squared_bounds_strict_machin_holdout(self):
        ml, mu = _machin_pi_bracket()
        for q in (2, 3, 5, 11, 47, 200):
            lo, hi = euler_prime_square_bracket(q)
            self.assertLess(lo, ml * ml)
            self.assertGreater(hi, mu * mu)
            self.assertEqual(hi - lo, lo / q)

    def test_06_prime_routes_intersect_and_contain(self):
        ml, mu = _machin_pi_bracket()
        for n, q in ((1, 2), (3, 7), (10, 20), (100, 200)):
            lo, hi = synchronized_pi_brackets(n, q)
            self.assertLess(lo, ml * ml)
            self.assertGreater(hi, mu * mu)

    def test_07_valid_digit_prefix_from_machin(self):
        ml, mu = _machin_pi_bracket()
        expected = rational_digit_prefix(ml, 10, 2)
        self.assertEqual(expected, rational_digit_prefix(mu, 10, 2))
        self.assertEqual(certified_pi_digit_prefix(5000, 10, 2), expected)
        self.assertIsNone(certified_pi_digit_prefix(1, 10, 2))

    def test_08_exact_digit_long_division(self):
        self.assertEqual(rational_digit_prefix(Fraction(1, 7), 10, 6), (1, 4, 2, 8, 5, 7))
        self.assertEqual(rational_digit_prefix(Fraction(8, 3), 2, 6), (1, 0, 1, 0, 1, 0))
        self.assertEqual(rational_digit_prefix(Fraction(12, 3), 10, 3), (0, 0, 0))

    def test_09_transport_budget_vanishes_for_n_base_pow_N(self):
        for base, N in ((2, 5), (2, 10), (3, 6), (10, 3)):
            bound = prime_carry_fourier_transport_error(base ** N, base, 1, N)
            self.assertLess(bound, Fraction(4, N * (base - 1)))
            self.assertGreater(bound, 0)

    def test_10_phase_clock_exact_succ_transition(self):
        for n, base, h, horizon in ((2, 2, 1, 12), (5, 10, -2, 15), (18, 3, 7, 12)):
            denominator, residues = prime_carry_phase_clock(n, base, h, horizon)
            midpoint = wallis_midpoint(n)
            self.assertEqual(residues, tuple(h * pow(base, j, denominator) * midpoint.numerator % denominator
                                             for j in range(horizon)))
            self.assertTrue(all(v == (base * u) % denominator
                                for u, v in zip(residues, residues[1:])))

    def test_11_joint_square_bracket_exact_digit_certification(self):
        ml, mu = _machin_pi_bracket()
        expected = rational_digit_prefix(ml, 10, 4)
        self.assertEqual(expected, rational_digit_prefix(mu, 10, 4))
        self.assertEqual(certified_pi_digit_prefix_joint(10000, 200, 10, 4), expected)
        self.assertIsNone(certified_pi_digit_prefix_joint(1, 2, 10, 4))

    def test_12_uniform_budget_symbolic_enormous_horizon(self):
        self.assertEqual(uniform_fourier_budget(2, 1, 1000000), Fraction(1, 250000))
        for base, N in ((2, 6), (3, 5), (10, 3)):
            exact = prime_carry_fourier_transport_error(base ** N, base, 1, N)
            self.assertLess(exact, uniform_fourier_budget(base, 1, N))

    def test_13_dyadic_period_does_not_collapse_at_sample_horizon(self):
        from math import gcd
        for level in range(0, 11):
            n = 2 ** level
            midpoint = wallis_midpoint(n)
            den = midpoint.denominator
            q1, q2 = 2 ** (level + 1) + 1, 2 ** (level + 2) + 1
            self.assertEqual(den % (q1 * q2), 0)
            self.assertEqual(gcd(den, 2), 1)
            self.assertEqual(doubling_carries(n)[2], 1)
            bound = dyadic_midpoint_period_floor(level)
            self.assertEqual(pow(2, bound, q1), 1)
            self.assertEqual(pow(2, bound, q2), 1)
            self.assertTrue(all(pow(2, k, q1) != 1 for k in range(1, 2*(level+1))))
            self.assertTrue(all(pow(2, k, q2) != 1 for k in range(1, 2*(level+2))))
            self.assertGreater(bound, level)

    def test_14_long_period_cannot_replace_fourier_cancellation(self):
        for N in (3, 4, 5, 8, 12):
            period, deviation_bound = long_period_nonmixing_control(N)
            self.assertEqual(period, N * N)
            denominator = 2 ** period - 1
            self.assertEqual(pow(2, period, denominator), 1)
            self.assertTrue(all(pow(2, k, denominator) != 1
                                for k in range(1, period)))
            self.assertLess(deviation_bound, Fraction(1, 3))
        self.assertLess(long_period_nonmixing_control(12)[1],
                        long_period_nonmixing_control(8)[1])

    def test_15_frequency_divisible_by_base_is_time_shift(self):
        for n, base, primitive_h, k, N in ((5, 2, 3, 4, 10), (9, 10, 7, 2, 9), (8, 3, 2, 3, 8)):
            den1, shifted = prime_carry_phase_clock(n, base, primitive_h * base ** k, N)
            den2, expanded = prime_carry_phase_clock(n, base, primitive_h, N + k)
            self.assertEqual(den1, den2)
            self.assertEqual(shifted, expanded[k:])

    def test_16_strict_source_and_input_guards(self):
        for n in (0, -1, True, 1.0, Fraction(2, 1)):
            with self.assertRaises(ValueError):
                wallis_pi_bracket(n)
        for base in (1, True, 2.0):
            with self.assertRaises(ValueError):
                prime_carry_fourier_transport_error(2, base, 1, 3)
        with self.assertRaises(ValueError):
            prime_carry_fourier_transport_error(2, 2, True, 3)
        with self.assertRaises(ValueError):
            prime_carry_fourier_transport_error(2, 2, 1, 0)
        with self.assertRaises(ValueError):
            rational_digit_prefix(Fraction(-1, 7), 10, 3)


if __name__ == "__main__":
    unittest.main()
