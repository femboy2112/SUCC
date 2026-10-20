"""Exact independent controls for the cloud referee's fixture mathematics."""
from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / "scripts" / "cloud_hostile_holdouts.py"
spec = importlib.util.spec_from_file_location("cloud_hostile_holdouts", path)
holdouts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(holdouts)


class CloudHoldoutControls(unittest.TestCase):
    def test_negative_family_exact_and_pair_invisible(self):
        for n in range(3, 10):
            for denominator in (3, 17, 10**14, 10**400):
                matrix, vector = holdouts.shallow_negative_family(n, denominator)
                self.assertEqual(holdouts.rational_quad(matrix, vector),
                                 Fraction(-n*n, denominator))
                for i in range(n):
                    coordinate = [Fraction(k == i) for k in range(n)]
                    self.assertGreater(holdouts.rational_quad(matrix, coordinate), 0)
                    for j in range(i + 1, n):
                        for sign in (1, -1):
                            pair = coordinate.copy()
                            pair[j] = Fraction(sign)
                            self.assertGreater(holdouts.rational_quad(matrix, pair), 0)

    def test_positive_and_null_mutations(self):
        n = 4
        identity = [[Fraction(i == j) for j in range(n)] for i in range(n)]
        projection = [[Fraction(n if i == j else 0)-1 for j in range(n)] for i in range(n)]
        v = [Fraction(1)] * n
        self.assertEqual(holdouts.rational_quad(identity, v), n)
        self.assertEqual(holdouts.rational_quad(projection, v), 0)

    def test_invalid_fixture_parameters_rejected(self):
        for n, denominator in ((2, 9), (3, 2), (3, 1.5), (True, 9)):
            with self.assertRaises(ValueError):
                holdouts.shallow_negative_family(n, denominator)

    def test_slope_calibration_and_nonprimitive_mutation(self):
        receipt = holdouts.primitive_slope_audit(max_x=15, max_divisor=5)
        self.assertGreater(receipt["cases"], 0)
        self.assertEqual(receipt["primitive_failures"], 0)
        mutation = receipt["nonprimitive_mutation"]
        self.assertGreater(mutation["count"], Fraction(mutation["bound"]))


if __name__ == "__main__":
    unittest.main()
