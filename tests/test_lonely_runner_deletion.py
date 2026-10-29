"""Adversarial exact checks; bounded sweeps are not the universal proof."""

from dataclasses import replace
from fractions import Fraction
import unittest

from observational_succ.lonely_runner_deletion import (
    circle_distance,
    exact_deletion_value,
    least_coprime_denominator,
    optimal_witness,
    retained_speeds,
    sharp_minimum,
    universal_witness,
    value_at,
)


def envelope_oracle(speeds):
    """Independent exhaustive opposite-slope crossings, including peaks.

    A maximum of the continuous piecewise-linear lower envelope occurs
    where active slopes change from positive to negative.  Its time is
    a/(v+w); v=w includes a single triangular wave's peak.  Reflection
    permits restricting to [0, 1/2].  No deletion formula is used here.
    """
    best = Fraction(0)
    for denominator in {v + w for v in speeds for w in speeds}:
        for numerator in range(denominator // 2 + 1):
            residues = [v * numerator % denominator for v in speeds]
            margin = min(min(j, denominator - j) for j in residues)
            best = max(best, Fraction(margin, denominator))
    return best


class LonelyRunnerDeletionTests(unittest.TestCase):
    def test_user_witness_all_branches(self):
        for n in range(5, 120):
            for r in range(1, n - 1):
                witness = universal_witness(n, r)
                self.assertTrue(witness.verify(), (n, r, witness))
                self.assertGreater(witness.guarantee, Fraction(1, n - 1))

    def test_independent_envelope_oracle(self):
        for n in range(3, 19):
            for r in range(1, n):
                self.assertEqual(
                    exact_deletion_value(n, r),
                    envelope_oracle(retained_speeds(n, r)),
                    (n, r),
                )

    def test_optimal_witness_attains_formula(self):
        for n in range(3, 80):
            for r in range(1, n):
                witness = optimal_witness(n, r)
                self.assertTrue(witness.verify())
                self.assertEqual(value_at(n, r, witness.time), witness.guarantee)

    def test_sharp_minimum_and_all_minimizers(self):
        for n in range(5, 250):
            values = {r: exact_deletion_value(n, r) for r in range(1, n - 1)}
            best = min(values.values())
            self.assertEqual(sharp_minimum(n), (best, tuple(r for r in values if values[r] == best)))

    def test_uniform_equality_has_two_cases(self):
        equalities = [
            (n, r)
            for n in range(5, 100)
            for r in range(1, n - 1)
            if exact_deletion_value(n, r) == Fraction(2, 2 * n - 3)
        ]
        self.assertEqual(equalities, [(5, 2), (6, 2)])

    def test_excluded_last_speed_is_a_countermodel(self):
        for n in range(5, 50):
            self.assertEqual(exact_deletion_value(n, n - 1), Fraction(1, n - 1))
            self.assertLess(exact_deletion_value(n, n - 1), Fraction(2, 2 * n - 3))
            with self.assertRaises(ValueError):
                universal_witness(n, n - 1)

    def test_small_n_assumption_is_necessary(self):
        self.assertEqual(exact_deletion_value(4, 1), Fraction(2, 5))
        self.assertEqual(exact_deletion_value(4, 2), Fraction(1, 2))
        self.assertEqual(exact_deletion_value(3, 1), Fraction(1, 2))
        with self.assertRaises(ValueError):
            universal_witness(4, 1)

    def test_inverse_bound_is_not_always_optimal(self):
        self.assertEqual(least_coprime_denominator(5, 3), 8)
        self.assertEqual(exact_deletion_value(5, 3), Fraction(1, 3))
        self.assertGreater(exact_deletion_value(5, 3), Fraction(2, 8))

    def test_liu_following_remark_counterexample(self):
        # The prose after Thm18 misses this second exception to >=1/|V|.
        speeds = (1, 3, 4, 5)
        self.assertEqual(envelope_oracle(speeds), Fraction(2, 9))
        self.assertLess(Fraction(2, 9), Fraction(1, len(speeds)))

    def test_mutated_witnesses_fail(self):
        witness = universal_witness(5, 2)
        self.assertFalse(replace(witness, time=Fraction(0)).verify())
        self.assertFalse(replace(witness, guarantee=Fraction(1, 3)).verify())
        self.assertFalse(replace(witness, r=1).verify())

    def test_exact_arithmetic_and_validation(self):
        self.assertEqual(circle_distance(Fraction(-17, 7)), Fraction(3, 7))
        self.assertEqual(circle_distance(Fraction(19, 7)), Fraction(2, 7))
        for bad in (True, 5.0, "5"):
            with self.assertRaises(TypeError):
                exact_deletion_value(bad, 2)
        for n, r in ((2, 1), (5, 0), (5, 5)):
            with self.assertRaises(ValueError):
                retained_speeds(n, r)
        with self.assertRaises(TypeError):
            value_at(5, 2, 0.5)


if __name__ == "__main__":
    unittest.main()
