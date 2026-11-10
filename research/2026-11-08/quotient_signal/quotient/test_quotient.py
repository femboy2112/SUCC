"""Focused exact tests for the learned quotient, independent of BBP numerics."""
from fractions import Fraction as F
import unittest

from oracle import (Z, control_receipts, mean, norm2, project, quotient, run,
                    unit, verify_case)


class QuotientTests(unittest.TestCase):
    def test_rational_unit_circle(self):
        for numerator in range(-30, 31):
            self.assertEqual(unit(F(numerator, 11)).abs2(), 1)

    def test_weighted_projection(self):
        self.assertEqual(project([Z(1), Z(3), Z(7)], [0, 0, 1], [1, 2, 1]),
                         [Z(F(7, 3)), Z(F(7, 3)), Z(7)])

    def test_sharp_operator_constant(self):
        a, one, labels, weights = [Z(1), Z(0, 1)], [Z(1)]*2, [0, 0], [1, 1]
        residual = [x-y for x, y in zip(one, quotient(one, a, labels, weights))]
        self.assertEqual(norm2(residual, weights), 1-mean(a, weights).abs2())
        self.assertEqual(norm2(residual, weights), F(1, 2))

    def test_all_exact_identities(self):
        result = run()
        self.assertEqual(result["cases"], 28)
        self.assertGreater(result["exact_checks"], 3000)

    def test_exact_hostile_controls(self):
        result = control_receipts()
        self.assertEqual(result["signed_refinement_increments"],
                         [["1/3", "0"], ["-1/3", "0"]])
        self.assertTrue(result["zero_mean_error_unit_reconstruction_error"])

    def test_nonunit_phase_rejected(self):
        with self.assertRaises(ValueError):
            quotient([Z(1)], [Z(2)], [0], [1])

    def test_weight_and_dimension_guards(self):
        with self.assertRaises(ValueError):
            project([Z(1)], [0], [0])
        with self.assertRaises(ValueError):
            project([Z(1)], [0, 1], [1])
        with self.assertRaises(ValueError):
            quotient([Z(1)], [], [0], [1])


if __name__ == "__main__":
    unittest.main()
