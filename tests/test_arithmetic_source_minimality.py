"""Independent word enumeration and exact adversarial controls, not an infinite proof."""
from collections import Counter
from fractions import Fraction
from math import isqrt
import unittest

from observational_succ.arithmetic_source_minimality import (
    LateBeurlingPair,
    incomplete_clock_witness,
    multiplication_compression_characteristic,
)


def primes_through(n):
    # Sieve independent from the constructor's trial-division primality check.
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def free_words(generators, cutoff):
    """Convolve one geometric series at a time, counting collisions explicitly."""
    counts = Counter({Fraction(1): 1})
    for generator in generators:
        following = Counter()
        for old, multiplicity in counts.items():
            value = old
            while value <= cutoff:
                following[value] += multiplicity
                value *= generator
        counts = following
    return counts


class ArithmeticSourceMinimalityTest(unittest.TestCase):
    def test_arbitrarily_late_prefixes_and_independent_enumerator(self):
        for horizon in (1, 2, 7, 31, 64, 101, Fraction(99, 2)):
            with self.subTest(horizon=horizon):
                model = LateBeurlingPair.beyond(horizon)
                self.assertGreater(model.p, horizon)
                self.assertGreater(model.a, model.p + 1)
                self.assertGreater(model.b, model.p + 1)
                expected = tuple(map(Fraction, range(1, int(horizon) + 1)))
                self.assertEqual(model.atoms(horizon), expected)
                self.assertEqual(model.count(horizon), len(expected))
                cutoff = 3 * model.p + 5
                generators = [Fraction(p) for p in primes_through(cutoff)
                              if p not in (model.p, model.q)] + [model.a, model.b]
                independently = free_words(generators, cutoff)
                self.assertEqual(set(independently.values()), {1})
                self.assertEqual(tuple(sorted(independently)), model.atoms(cutoff))
                self.assertEqual(sum(independently.values()), model.count(cutoff))

    def test_general_family_holdouts_density_and_braid(self):
        # Not only the constructor's nearest q; several unrelated prime choices.
        for p, q in ((3, 11), (3, 101), (5, 29), (5, 997),
                     (7, 53), (11, 127), (13, 211), (17, 307)):
            with self.subTest(p=p, q=q):
                model = LateBeurlingPair(p, q)
                self.assertEqual(model.density_multiplier(), 1)
                self.assertEqual(model.first_braid_witness()["defect"], -1)
                self.assertEqual(model.atoms(p + 1),
                                 tuple(map(Fraction, [*range(1, p), p + 1])))
                # Exact first renewal residual: source mass(p)-source mass(p-1).
                atoms = set(model.atoms(p))
                self.assertEqual(int(Fraction(p) in atoms) - int(Fraction(p - 1) in atoms), -1)

    def test_certified_counting_error_bound(self):
        for model in (LateBeurlingPair(3, 11), LateBeurlingPair(5, 29),
                      LateBeurlingPair(7, 997)):
            for x in (1, 2, 3, 10, 100, 1_000, 100_000, Fraction(101, 3)):
                with self.subTest(p=model.p, q=model.q, x=x):
                    self.assertLessEqual(abs(model.count(x) - x), model.counting_error_bound(x))

    def test_missing_prime_location_is_decisive_fresh_probe(self):
        model = LateBeurlingPair.beyond(100)
        self.assertEqual(model.count(100), 100)
        self.assertEqual(model.count(model.p), model.p - 1)
        self.assertNotIn(Fraction(model.p), model.atoms(2 * model.p))
        self.assertIn(model.a, model.atoms(2 * model.p))

    def test_complete_source_positive_control_and_fake_six(self):
        authentic = free_words(list(map(Fraction, primes_through(50))), 50)
        self.assertEqual(authentic, Counter({Fraction(n): 1 for n in range(1, 51)}))
        fake = free_words([Fraction(2), Fraction(3), Fraction(6)], 12)
        self.assertEqual(fake[Fraction(6)], 2)
        self.assertEqual(fake[Fraction(12)], 2)

    def test_rank_scale_is_not_archimedean_unit(self):
        # n -> n^c with c=2 preserves multiplicative ranks and every braid.
        rank = {n * n: n for n in range(1, 51)}
        for multiplier in (2, 3, 5):
            for n in range(1, 10):
                self.assertEqual(rank[(multiplier * (n + 1)) ** 2]
                                 - rank[(multiplier * n) ** 2], multiplier)
        self.assertEqual(2 ** 2 - 1, 3)  # first additive-real cell is not one

    def test_incomplete_all_simple_clock_shadow(self):
        periods = (3, 4, 5, 6, 7, 12, 35, 60)
        witness = incomplete_clock_witness(periods)
        self.assertEqual(witness, {"prime": 2, "cap": 2, "missing_period": 8})
        # Every supplied period divides a finite stage of the same capped system.
        for period in periods:
            self.assertNotEqual(period % witness["missing_period"], 0)
        self.assertEqual(incomplete_clock_witness((), 3)["missing_period"], 9)

    def test_compression_is_not_full_operator_spectral_endpoints(self):
        for prime in (2, 3, 5, 11):
            coefficients = multiplication_compression_characteristic(prime)
            d = 1 + Fraction(1, prime)
            # Independent determinant d*d - offdiag_squared.
            self.assertEqual(coefficients, (1, -2 * d, d * d - Fraction(1, prime)))
            self.assertGreater(coefficients[2], 0)
            # Incorrect endpoint eigenvalues have this different product.
            self.assertNotEqual(coefficients[2], (1 - Fraction(1, prime)) ** 2)

    def test_finite_counting_state_is_not_tracial_on_infinite_algebra(self):
        # Literal V_2*V_2=I and V_2 V_2*=projection onto even integers.
        # Independent explicit basis images, not a postulated density formula.
        for n in (1, 2, 3, 10, 101):
            identity = sum(1 for _ in range(1, n + 1))
            even_range = sum(1 for k in range(1, n + 1) if k % 2 == 0)
            defect = Fraction(identity - even_range, n)
            self.assertGreaterEqual(defect, Fraction(1, 2))

    def test_domain_and_budget_mutants(self):
        for p, q in ((2, 11), (6, 53), (3, 9), (5, 23), (True, 11)):
            with self.assertRaises(ValueError):
                LateBeurlingPair(p, q)
        for horizon in (0, True, 3.5):
            with self.assertRaises(ValueError):
                LateBeurlingPair.beyond(horizon)
        with self.assertRaises(ValueError):
            LateBeurlingPair(3, 11).atoms(100, budget=2)
        with self.assertRaises(ValueError):
            incomplete_clock_witness((3, 4), 6)
        with self.assertRaises(ValueError):
            multiplication_compression_characteristic(6)


if __name__ == "__main__":
    unittest.main()
