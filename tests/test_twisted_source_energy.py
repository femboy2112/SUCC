"""Exact identities, independent controls and a certified authentic source."""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.twisted_source_energy import (
    exact_energy_identity, phase_boxes, energy_intervals,
    green_energy_budget, source_energy_report,
)
from observational_succ.pi_source_genesis import (
    ComplexBox, character_interval, machin_pi_interval,
)


class TwistedSourceEnergyTests(unittest.TestCase):
    def test_exact_signed_zero_extension_and_bound(self):
        alphabet = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for z in product(alphabet, repeat=4):
            for width in (1, 2, 3, 4):
                row = exact_energy_identity(z, width)
                self.assertEqual(row["lag_side"], row["block_side"])
                self.assertLessEqual(row["mean_squared"], row["mean_squared_upper"])

    def test_nonunit_gaussian_inputs_are_also_valid(self):
        row = exact_energy_identity(((Q(2, 3), Q(-1, 7)), (3, -2), (0, 0)), 3)
        self.assertEqual(row["lag_side"], row["block_side"])
        self.assertLessEqual(row["mean_squared"], row["mean_squared_upper"])

    def test_constant_energy_includes_endpoints(self):
        for n in (2, 3, 7, 12):
            for width in range(1, n+1):
                row = exact_energy_identity(((1, 0),)*n, width)
                self.assertEqual(row["energy"], 1-Q(width*width-1, 3*n*width))
                self.assertEqual(row["mean_squared"], 1)

    def test_absolute_correlations_destroy_signed_saving(self):
        row = exact_energy_identity(((1, 0), (-1, 0))*4, 4)
        signed = row["lag_side"]
        unsigned = 4*8+2*sum((4-d)*abs(row["correlations"][d-1][0])
                              for d in range(1, 4))
        self.assertLess(signed, unsigned)
        self.assertEqual(row["mean_squared"], 0)

    def test_interval_control_on_exact_fourth_roots(self):
        phases = (Q(), Q(1, 4), Q(1, 2), Q(3, 4))*2
        boxes = phase_boxes(phases)
        result = energy_intervals(boxes, (1, 2, 4, 8))
        exact = ((1, 0), (0, 1), (-1, 0), (0, -1))*2
        self.assertLessEqual(result["direct_mean_squared_low"], 0)
        self.assertLess(result["direct_mean_squared_high"], Q(1, 10**20))
        for row in result["rows"]:
            truth = exact_energy_identity(exact, row["width"])["energy"]
            self.assertLessEqual(row["energy_low"], truth)
            self.assertGreaterEqual(row["energy_high"], truth)
            self.assertLess(row["energy_high"]-row["energy_low"], Q(1, 10**14))

    def test_bbp_source_certificate_and_source_tail(self):
        report = source_energy_report(41, 1, (2, 4, 8))
        self.assertEqual(report["length"], 15)
        self.assertGreater(report["direct_mean_squared_low"], Q(1, 50))
        self.assertLess(report["direct_mean_squared_high"], 1)
        for row in report["rows"]:
            self.assertLessEqual(report["direct_mean_squared_low"],
                                 row["mean_squared_upper"])
            self.assertLessEqual(row["energy_low"], row["energy_high"])
        self.assertEqual(green_energy_budget(6, 15, 0), 0)
        self.assertEqual(green_energy_budget(6, 15, -2),
                         2*green_energy_budget(6, 15, 1))
        self.assertLess(green_energy_budget(6, 15, 1), Q(88, 7*49*50))

    def test_strict_inputs_and_bad_scales(self):
        for bad in (True, 1.0, "1"):
            with self.assertRaises(ValueError):
                phase_boxes((0, Q(1, 2)), bad)
            with self.assertRaises(ValueError):
                exact_energy_identity(((1, 0),), bad)
        with self.assertRaises(ValueError):
            phase_boxes((0.1,))
        with self.assertRaises(ValueError):
            exact_energy_identity((), 1)
        with self.assertRaises(ValueError):
            exact_energy_identity(((1, 0),), 2)
        with self.assertRaises(ValueError):
            green_energy_budget(0, 2)
        with self.assertRaises(ValueError):
            energy_intervals((ComplexBox(1.0, 1.0, 0, 0),), (1,))

    def test_independent_machin_shadow_within_green_budget(self):
        # Build the true pi shadow independently of the rational recurrence.
        start, length = 6, 15
        low, high = machin_pi_interval(2*(start+length)+40)
        boxes = tuple(character_interval(16**(n-1)*low, 16**(n-1)*high,
                                          order=16, bits=90).outward(90)
                      for n in range(start, start+length))
        shadow = energy_intervals(boxes, (2, 4, 8))
        source = source_energy_report(41, 1, (2, 4, 8))
        budget = green_energy_budget(start, length)
        for x, y in zip(shadow["rows"], source["rows"]):
            # The whole independently enclosed difference lies in the budget.
            self.assertLess(x["energy_high"]-y["energy_low"], budget)
            self.assertLess(y["energy_high"]-x["energy_low"], budget)


if __name__ == "__main__":
    unittest.main()
