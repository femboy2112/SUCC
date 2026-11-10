from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import sys
import unittest

spec = importlib.util.spec_from_file_location('round2_chronology_leakage_test',
                                            Path(__file__).with_name('leakage_oracle.py'))
o = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = o
spec.loader.exec_module(o)


class LeakageTests(unittest.TestCase):
    def test_exact_conditional_variance(self):
        points = [Q(1, 64), Q(3, 64), Q(3, 16)]
        cells = o.partition(points, 1)
        self.assertEqual(cells, {0: [0, 1], 3: [2]})
        self.assertEqual(o.rational_residual_variance(points, cells), Q(1, 6144))

    def test_singleton_phase_identity(self):
        values = [o.iv.phase(1, 17), o.iv.phase(16, 17)]
        energy = o.unit_phase_cell_energy(values, {0: [0], 15: [1]})
        self.assertEqual(energy, o.iv.ONE)

    def test_invalid_carrier(self):
        for points in ([], [0.5], [Q(-1, 3)], [Q(1)]):
            with self.assertRaises(ValueError):
                o.partition(points, 1)
        with self.assertRaises(ValueError):
            o.partition([Q(0)], 0)


if __name__ == '__main__':
    unittest.main()
