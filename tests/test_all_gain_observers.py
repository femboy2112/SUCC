"""Independent finite controls for all-gain limit and prime certificates."""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations_with_replacement
import unittest

from observational_succ.all_gain_observers import (
    composite_stationarity_budgets, gain_average, gain_limit_haar_bound,
    gain_limit_origin_mass, integer_gain_readout, origin_ball_mass,
    prime_fourier_certificate, prime_stationarity_costs, primes_through,
    rational_gain_limit, rational_gain_remainder_budget, uniform_torsion,
)
from observational_succ.pi_source_collision import bbp_forcing, bbp_states
from observational_succ.source_history_transport import (
    AtomicProbability, circle_w1, empirical_law, multiplication_pushforward,
)


def _tv(first, second):
    a, b = dict(first.atoms), dict(second.atoms)
    return sum((abs(a.get(x, 0)-b.get(x, 0)) for x in a.keys() | b.keys()), Q())/2


class AllGainTests(unittest.TestCase):
    def test_single_rational_period_and_exact_tv_all_remainders(self):
        # Independent literal modular counts, including unreduced inputs.
        for d in (2, 3, 4, 5, 7, 9, 11):
            for a in (1, 2, d-1):
                x = Q(a, d)
                mu = empirical_law((x,))
                period = x.denominator
                limit = rational_gain_limit(mu)
                self.assertEqual(limit, uniform_torsion(period))
                for cutoff in range(1, 2*period+2):
                    counts = Counter((q*x) % 1 for q in range(1, cutoff+1))
                    expected = AtomicProbability(tuple((v, Q(c, cutoff))
                                                       for v, c in counts.items()))
                    actual = gain_average(mu, cutoff)
                    self.assertEqual(actual, expected)
                    budget = rational_gain_remainder_budget(mu, cutoff)
                    self.assertEqual(_tv(actual, limit), budget['tv_upper'])
                    self.assertLessEqual(circle_w1(actual, limit), budget['w1_upper'])

    def test_gain_limit_mass_at_zero_detects_rational_absorption(self):
        mu = empirical_law((0, Q(1, 3), Q(1, 5)))
        limit = rational_gain_limit(mu)
        self.assertEqual(gain_limit_origin_mass(mu), Q(23, 45))
        self.assertEqual(dict(limit.atoms)[Q()], Q(23, 45))
        self.assertGreater(dict(limit.atoms)[Q()], dict(mu.atoms)[Q()])
        # A uniform finite grid is NOT fixed by averaging all integer gains.
        grid = uniform_torsion(5)
        self.assertEqual(gain_limit_origin_mass(grid), Q(9, 25))
        self.assertNotEqual(rational_gain_limit(grid), grid)

    def test_zero_is_fixed_and_must_be_excluded_by_the_hypothesis(self):
        zero = empirical_law((0,))
        for cutoff in (1, 2, 7, 31):
            self.assertEqual(gain_average(zero, cutoff), zero)
        self.assertEqual(rational_gain_limit(zero), zero)
        self.assertEqual(origin_ball_mass(zero, 0), 1)
        self.assertEqual(gain_limit_haar_bound(zero), Q(1, 4))

    def test_gain_limit_discontinuity_control_is_not_false_preservation(self):
        zero = empirical_law((0,))
        for denominator in (5, 8, 17, 64):
            mu = empirical_law((Q(1, denominator),))
            limit = rational_gain_limit(mu)
            self.assertEqual(circle_w1(mu, zero), Q(1, denominator))
            self.assertEqual(limit, uniform_torsion(denominator))
            expected = Q(1, 4) if denominator % 2 == 0 else (
                Q(1, 4)-Q(1, 4*denominator**2))
            self.assertEqual(circle_w1(limit, mu), expected)
        self.assertEqual(rational_gain_limit(zero), zero)

    def test_limit_mixture_budget_is_upper_not_false_equality(self):
        mu = empirical_law((Q(1, 3), Q(2, 3), Q(1, 5)))
        limit = rational_gain_limit(mu)
        strict = False
        for cutoff in range(1, 18):
            actual = gain_average(mu, cutoff)
            budget = rational_gain_remainder_budget(mu, cutoff)
            self.assertLessEqual(_tv(actual, limit), budget['tv_upper'])
            strict |= _tv(actual, limit) < budget['tv_upper']
        self.assertTrue(strict)

    def test_origin_closed_ball_wrap_and_boundary(self):
        mu = empirical_law((0, Q(1, 8), Q(1, 2), Q(7, 8)))
        self.assertEqual(origin_ball_mass(mu, Q(1, 8)), Q(3, 4))
        self.assertEqual(origin_ball_mass(mu, Q(1, 9)), Q(1, 4))
        self.assertEqual(origin_ball_mass(mu, Q(1, 2)), 1)

    def test_composite_budgets_dominate_independent_actual_costs(self):
        cases = tuple(combinations_with_replacement((Q(), Q(1, 3), Q(2, 3)), 2))
        for points in cases:
            mu = empirical_law(points)
            costs = prime_stationarity_costs(mu, 12)
            budgets = composite_stationarity_budgets(costs, 12)
            for n in range(1, 13):
                actual = circle_w1(multiplication_pushforward(mu, n), mu)
                self.assertLessEqual(actual, budgets[n])

    def test_prime_certificate_does_not_drop_unseen_prime(self):
        mu = uniform_torsion(7)
        costs = prime_stationarity_costs(mu, 5)
        self.assertEqual(costs, {2: Q(), 3: Q(), 5: Q()})
        with self.assertRaises(ValueError):
            composite_stationarity_budgets(costs, 7)
        self.assertGreater(circle_w1(multiplication_pushforward(mu, 7), mu), 0)

    def test_prime_fourier_budget_exact_quarter_circle_characters(self):
        # Gaussian-integer root sums give an independent exact Fourier oracle.
        roots = ((1, 0), (0, 1), (-1, 0), (0, -1))
        grid = tuple(Q(j, 4) for j in range(4))
        for points in combinations_with_replacement(grid, 3):
            mu = empirical_law(points)
            for h in (1, 2, -3):
                real = imag = Q()
                for x, mass in mu.atoms:
                    re, im = roots[int(4*x*h) % 4]
                    real += mass*re
                    imag += mass*im
                cert = prime_fourier_certificate(mu, 7, h, Q(1, 8))
                self.assertLessEqual(real*real+imag*imag,
                                     cert['fourier_modulus_upper']**2)

    def test_nontrivial_fourier_budget_on_a_heldout_grid(self):
        # The premise has genuine finite content; the bound need not equal 1.
        mu = uniform_torsion(101)
        cert = prime_fourier_certificate(mu, 31, 3, Q(1, 8))
        self.assertTrue(all(value == 0 for value in cert['prime_costs'].values()))
        self.assertLess(cert['fourier_modulus_upper'], Q(2, 5))

    def test_source_integer_readout_all_gains_and_wrong_forcing(self):
        source = bbp_states(45)
        for n in range(1, 46):
            for gain in (1, 2, 3, 5, 7, 11, 13, 16, 31, 37):
                actual = integer_gain_readout(source[n-1], source[n],
                                              bbp_forcing(n), gain)
                self.assertEqual(actual, gain*source[n-1] % 1)
            with self.assertRaises(ValueError):
                integer_gain_readout(source[n-1], source[n],
                                     bbp_forcing(n)+Q(1, 7), 3)
        # Integer changes to a lift do not change the circle readout.
        self.assertEqual(integer_gain_readout(2, 3, 1, 5), 0)

    def test_exact_atom_budget_prevents_exponential_materialization(self):
        mu = empirical_law((Q(1, 10**15+37),))
        with self.assertRaises(ValueError):
            rational_gain_limit(mu, maximum_generated_atoms=1000)
        self.assertEqual(gain_limit_origin_mass(mu), Q(1, 10**15+37))

    def test_domains_reject_float_boolean_and_invalid_prime_certificates(self):
        mu = empirical_law((0,))
        for bad in (0, -1, True, 1.0):
            with self.assertRaises(ValueError):
                gain_average(mu, bad)
        for bad in (-1, Q(3, 4), .1, True):
            with self.assertRaises(ValueError):
                origin_ball_mass(mu, bad)
        for costs in ({4: Q()}, {2: -1}, {2: .1}, {}, []):
            with self.assertRaises(ValueError):
                composite_stationarity_budgets(costs, 2)
        with self.assertRaises(ValueError):
            prime_fourier_certificate(mu, 2, 0, Q(1, 8))
        with self.assertRaises(ValueError):
            prime_fourier_certificate(mu, 2, 1, 0)
        self.assertEqual(primes_through(13), (2, 3, 5, 7, 11, 13))


if __name__ == '__main__':
    unittest.main()
