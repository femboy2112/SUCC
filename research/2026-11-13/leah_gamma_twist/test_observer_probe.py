"""Frozen controls declared in OBSERVER_BRIDGE.md before their execution."""

from fractions import Fraction
from itertools import product
import unittest

import observer_probe as p


class ObserverProbeTests(unittest.TestCase):
    def test_word_compiler_against_sequential_interpreter(self):
        letters = ((1, 1), (3, 1), (2, -1))
        for length in range(5):
            for word in product(letters, repeat=length):
                for seed in (Fraction(0), Fraction(1, 3), Fraction(-2, 7)):
                    self.assertEqual(p.compile_word(word).apply(seed), p.iterate_word(word, seed))

    def test_inverse_order_is_material(self):
        word = ((2, 1), (5, 1))
        correct = p.compile_word(word+p.inverse_word(word))
        wrong = p.compile_word(word+((2, -1), (5, -1)))
        self.assertEqual((correct.net_scale, correct.offset), (0, 0))
        self.assertEqual(wrong.offset, Fraction(15, 256)*(p.source(2)-p.source(5)))
        self.assertNotEqual(wrong.offset, 0)

    def test_sorting_mutant_and_source_sign_are_rejected(self):
        forward = ((2, 1), (5, 1))
        reverse = tuple(reversed(forward))
        actual = p.compile_word(forward).offset-p.compile_word(reverse).offset
        self.assertEqual(actual, p.swap_defect(2, 5))
        self.assertNotEqual(actual, 0)
        self.assertNotEqual(actual, -p.swap_defect(2, 5))
        self.assertNotEqual(actual, 16*(p.source(2)-p.source(5)))
        self.assertEqual(p.compile_word(tuple(sorted(forward))), p.compile_word(tuple(sorted(reverse))))

    def test_equal_scale_seed_blind_but_not_absolute(self):
        first, second = p.compile_word(((1, 1), (2, 1))), p.compile_word(((2, 1), (1, 1)))
        for seed in (Fraction(0), Fraction(2, 9), Fraction(-5, 11)):
            self.assertEqual(first.apply(seed)-second.apply(seed), first.offset-second.offset)
        self.assertNotEqual(first.apply(0), first.apply(Fraction(1, 15)))

    def test_compensation_precedes_relative_arithmetic_phase(self):
        first, second = p.compile_word(((2, 1),)), p.compile_word(((5, 1), (3, 1)))
        seed = Fraction(2, 7)
        raw = first.apply(seed)-second.apply(seed)
        compensated = raw-(first.offset-second.offset)
        self.assertEqual(compensated, (first.slope-second.slope)*seed)
        self.assertNotEqual(p.phase(raw), p.phase(compensated))

    def test_present_seed_pin_checks_data_not_metadata(self):
        for n in (0, 1, 4, 9):
            for seed in (Fraction(0), Fraction(1, 3), Fraction(-2, 7)):
                self.assertEqual(p.seed_pin(n, p.state_at(n, seed)), seed)
            wrong = p.state_at(n, Fraction(1, 3))
            self.assertNotEqual(p.seed_pin(n, wrong), 0)

    def test_complete_fifteen_torsion_and_absolute_separator(self):
        for base in (Fraction(0), Fraction(1, 7), Fraction(2, 9)):
            for j in range(15):
                shifted = base+Fraction(j, 15)
                for first, second in product(range(5), repeat=2):
                    q = p.relative_frequency(1, first, second)
                    self.assertEqual(q % 15, 0)
                    self.assertEqual(p.phase(q*base), p.phase(q*shifted))
            self.assertEqual(len({p.phase(base+Fraction(j, 15)) for j in range(15)}), 15)
        self.assertEqual(p.relative_frequency(1, 1, 0), 15)
        self.assertNotEqual(p.phase(Fraction(15, 16)), 0)

    def test_higher_arity_neutrality_retains_gauge(self):
        patterns = (((0, 1, 2), (1, -2, 1)), ((0, 1, 2, 3), (1, -1, 2, -2)),
                    ((0, 1, 2, 3, 4), (1, 1, 1, 1, -4)))
        for clocks, charges in patterns:
            for j in range(15):
                self.assertEqual(p.neutral_phase(Fraction(j, 15), clocks, charges), 0)
        with self.assertRaises(ValueError):
            p.neutral_phase(Fraction(1, 15), (0, 1, 2), (1, 1, 1))

    def test_wrong_seed_pair_retains_literal_tail(self):
        for n in (0, 1, 3, 8):
            for j in range(15):
                xi = Fraction(j, 15)
                actual = p.state_at(n, p.LinearX(-1, xi))
                tail = p.symbolic_tail(n)
                self.assertEqual(actual+tail, p.LinearX(0, 16**n*xi))
                self.assertNotEqual(actual, actual+tail)
                self.assertEqual(p.seed_pin(n, actual), p.LinearX(-1, xi))
                self.assertEqual(p.phase(16**n*xi), xi)

    def test_bidirectional_present_clock_transport(self):
        words = ((), ((5, 1),), ((5, -1),), ((7, -1), (2, -1)),
                 ((2, 1), (5, 1), (2, -1), (5, -1)))
        for n in (2, 4):
            for word in words:
                final_clock = n+p.compile_word(word).net_scale
                result = p.completed_word(Fraction(2, 15), n, word)
                self.assertEqual(result, p.LinearX(0, 16**final_clock*Fraction(2, 15)))
        with self.assertRaises(ValueError):
            p.completed_word(Fraction(1, 15), 0, ((1, -1),))

    def test_four_poles_against_expanded_moment_and_beta_bounds(self):
        for n in (1, 2, 5, 17, 64):
            for order in range(6):
                direct = p.finite_difference(n, order)
                self.assertEqual(direct, p.moment_difference(n, order))
                lower, upper = p.difference_bounds(n, order)
                self.assertTrue(0 < lower <= direct <= upper)

    def test_difference_word_cost_and_exact_translation(self):
        for n in (1, 5, 17):
            for order in range(1, 6):
                word = p.difference_word(n, order)
                action = p.compile_word(word)
                self.assertEqual(len(word), 2**order)
                self.assertEqual(action.net_scale, 0)
                self.assertEqual(action.offset, p.finite_difference(n, order)/16)

    def test_tail_budget_is_frequency_dependent(self):
        self.assertEqual(p.relative_tail_budget(4, -15), p.relative_tail_budget(4, 15))
        self.assertEqual(p.relative_tail_budget(4, 30), 2*p.relative_tail_budget(4, 15))
        self.assertEqual(p.relative_tail_budget(4, 0), 0)

    def test_invalid_indices_types_and_frequency_contracts(self):
        for bad in (True, 1.0, "1"):
            with self.assertRaises(TypeError):
                p.source(bad)
            with self.assertRaises(TypeError):
                p.finite_difference(1, bad)
        for bad in (0, -1):
            with self.assertRaises(ValueError):
                p.source(bad)
        with self.assertRaises(ValueError):
            p.compile_word(((1, 0),))
        with self.assertRaises(ValueError):
            p.relative_frequency(1, -1, 0)
        with self.assertRaises(TypeError):
            p.neutral_phase(Fraction(1, 15), (0, 1), (True, -1))


if __name__ == "__main__":
    unittest.main()
