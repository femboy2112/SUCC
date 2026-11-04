"""Run with python3 -m unittest discover -s <this directory>."""
from fractions import Fraction
import json
from pathlib import Path
import unittest

from europa_probe import negative_values, pair_epoch, prime_bump_intervals, run


class EuropaTests(unittest.TestCase):
    def test_first_missing_negative_integer(self):
        one = negative_values(1)
        self.assertEqual(one["first_defect"], "1260")
        self.assertEqual(one["specialization_at_one"], "109/140")

    def test_nonconstant_seed_phase(self):
        values = pair_epoch()
        self.assertEqual(values["0"], values["1/5"])
        separation = Fraction(values["0"])
        mutant = Fraction(values["1/7"])
        self.assertEqual((mutant-separation) % 1, Fraction(4, 7))
        self.assertNotEqual((separation+mutant) % 1, 0)

    def test_two_signed_euler_atoms(self):
        left, _ = map(Fraction, prime_bump_intervals(3))
        _, right = map(Fraction, prime_bump_intervals(5))
        self.assertGreater(left, Fraction(3, 5))
        self.assertLess(right, Fraction(-7, 10))

    def test_archived_exact_receipt(self):
        receipt = Path(__file__).with_name("receipt.json")
        # Convert integer dictionary keys by JSON roundtrip.
        self.assertEqual(json.loads(json.dumps(run())), json.loads(receipt.read_text()))


if __name__ == "__main__":
    unittest.main()
