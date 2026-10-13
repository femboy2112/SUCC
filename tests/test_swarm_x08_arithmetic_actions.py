"""Mutation and independent-oracle checks for the X08 bridge."""
from fractions import Fraction
from pathlib import Path
import json
import unittest

from observational_succ.swarm_x08_arithmetic_actions import (
    cyclic_word_kernel, direct_log, fixed_point_repair, least_report_period,
    pair_covariance, stable, valuation_report, x08_receipt,
)


class ArithmeticActionBridgeTests(unittest.TestCase):
    def test_nontrivial_residue_quotient_retains_noncommutation(self):
        report = tuple(x % 3 for x in range(12))
        self.assertEqual(least_report_period(report), 3)
        self.assertEqual(cyclic_word_kernel(report), report)
        self.assertNotEqual(2*(0+1) % 3, (2*0+1) % 3)
        self.assertEqual(fixed_point_repair(report, (tuple((x+1) % 12 for x in range(12)),
                                                    tuple(2*x % 12 for x in range(12)))), report)

    def test_valuation_dilation_pass_successor_fail_and_repair(self):
        report = valuation_report(3, 1)
        self.assertEqual(report, (1, 0, 0))
        self.assertTrue(stable(report, (0, 0, 0)))
        self.assertFalse(stable(report, (1, 2, 0)))
        self.assertEqual(fixed_point_repair(report, ((1, 2, 0),)), (0, 1, 2))

    def test_nonlinear_mutation_breaks_successor_absorption(self):
        report, shift, mutation = (0, 1, 0, 1), (1, 2, 3, 0), (0, 0, 1, 0)
        self.assertEqual(fixed_point_repair(report, (shift,)), report)
        self.assertEqual(fixed_point_repair(report, (shift, mutation)), (0, 1, 2, 3))

    def test_phase_mutation_is_detected_before_covariance(self):
        original, mutant = (0, 1, 1, 1, 1, 1, 1), (0, 1, 1, 1, 1, 1, -1)
        self.assertEqual(direct_log(original)[6], 0)
        self.assertEqual(direct_log(mutant)[6], -2)
        weights = tuple(Fraction(1, n) for n in range(1, 7))
        features = ((0, 0), (1, 0), (0, 1), (2, 0), (0, 0), (1, 1))
        matrix = pair_covariance(weights, features)
        self.assertGreater(matrix[0][0]*matrix[1][1]-matrix[0][1]**2, 0)

    def test_invalid_contracts_rejected(self):
        with self.assertRaises(ValueError):
            valuation_report(6, 2)
        with self.assertRaises(ValueError):
            stable((0, 1), (1,))
        with self.assertRaises(ValueError):
            direct_log((0, 0, 1))
        with self.assertRaises(ValueError):
            pair_covariance((Fraction(-1), Fraction(2)), ((0,), (1,)))

    def test_saved_receipt_replays_independent_oracles(self):
        path = Path(__file__).resolve().parents[1] / "research/2026-10-13/SWARM_ATLAS/X08_RECEIPT.json"
        self.assertEqual(x08_receipt(), json.loads(path.read_text()))


if __name__ == "__main__":
    unittest.main()
