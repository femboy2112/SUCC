"""Unit cases for the exact chronology checker, separate from theorem proofs."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import unittest

spec = importlib.util.spec_from_file_location('round2_chronology_oracle', Path(__file__).with_name('oracle.py'))
o = importlib.util.module_from_spec(spec)
spec.loader.exec_module(o)


class ChronologyTests(unittest.TestCase):
    def test_literal_first_source(self):
        self.assertEqual(o.source_history(1), [Q(0), Q(47, 15)])

    def test_source_contract_rejects_float(self):
        with self.assertRaises(ValueError):
            o.source_history(3, 0.0)
        with self.assertRaises(ValueError):
            o.principal(1.0, 17)

    def test_prime_preconditions(self):
        for p in (2, 9, 25, 19, True):
            with self.assertRaises(ValueError):
                o.order(p)
        self.assertEqual(o.order(17), 2)

    def test_resonance_classification(self):
        self.assertEqual(o.classify((-16, 1), (0, 1), 17), 'integer_resonance')
        self.assertEqual(o.classify((17,), (0,), 17), 'modular_alias')
        self.assertEqual(o.classify((1,), (0,), 17), 'nonresonance')
        with self.assertRaises(ValueError):
            o.effective_frequency((1,), (0, 1))
        with self.assertRaises(ValueError):
            o.effective_frequency((1,), (-1,))

    def test_base16_word(self):
        # 1/17 = .0f0f... in hexadecimal, the other clock state is16/17.
        self.assertEqual(o.word_by_orbit(1, 17, 4), 0x0f0f)
        self.assertEqual(o.word_by_orbit(16, 17, 4), 0xf0f0)
        with self.assertRaises(ValueError):
            o.word_by_orbit(17, 17, 2)

    def test_support_horizon(self):
        counts = {0x0f0f: 1, 0xf0f0: 1}
        self.assertEqual(o.total_variation(counts, 2, 16**4), 1-Q(2, 16**4))
        with self.assertRaises(ValueError):
            o.total_variation(counts, 3, 16**4)

    def test_carry_initial_floor_required(self):
        zero = o.source_history(8)
        shifted = o.source_history(8, Q(3))
        self.assertEqual(o.carry_data(zero)[1], o.carry_data(shifted)[1])
        self.assertNotEqual(o.carry_data(zero)[0][0], o.carry_data(shifted)[0][0])

    def test_carry_radius_endpoint(self):
        zero = o.source_history(8)
        sigma = o.carry_radius(zero)
        self.assertEqual(o.carry_data(zero), o.carry_data(o.source_history(8, sigma/2)))
        self.assertNotEqual(o.carry_data(zero), o.carry_data(o.source_history(8, sigma)))


if __name__ == '__main__':
    unittest.main()
