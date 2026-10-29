"""Exact boundary, coding and hostile-source regressions; no asymptotic lift."""
from fractions import Fraction as F
from itertools import product
import unittest

from observational_succ import inertial_information_boundary as b
from observational_succ.succ_internal_matrix_walk import authentic_r as native_r


class CodingTests(unittest.TestCase):
    def test_exact_declared_sign_and_framing(self):
        expected = {0: "0", 1: "101", -1: "111", -16: "11000010000"}
        for number, code in expected.items():
            self.assertEqual(b.signed_integer_encode(number), code)
            self.assertEqual(b.signed_integer_decode(code), number)

    def test_signed_roundtrips_and_lengths(self):
        numbers = set(range(-257, 258)) | {sign*2**k for sign in (-1, 1) for k in range(17)}
        for number in numbers:
            code = b.signed_integer_encode(number)
            self.assertEqual(b.signed_integer_decode(code), number)
            self.assertEqual(len(code), b.signed_integer_code_length(number))
        self.assertTrue(b.is_prefix_free(b.signed_integer_encode(n) for n in numbers))

    def test_kraft_by_independent_word_sum_and_full_shells(self):
        for magnitude in (0, 1, 2, 7, 16, 31, 257):
            direct = sum((F(1, 2**len(b.signed_integer_encode(n)))
                          for n in range(-magnitude, magnitude+1)), F())
            self.assertEqual(direct, b.integer_kraft_partial(magnitude))
            self.assertLess(direct, 1)
        for level in range(17):
            self.assertEqual(b.integer_kraft_partial(2**(level+1)-1),
                             1-F(1, 2**(level+2)))

    def test_countercoding_changes_the_fixed_numeral_ranking(self):
        def swapped(number):
            return b.signed_integer_encode({0: -1, -1: 0}.get(number, number))
        self.assertTrue(b.is_prefix_free(swapped(n) for n in range(-257, 258)))
        self.assertLess(len(swapped(-1)), len(swapped(0)))
        self.assertLess(b.signed_integer_code_length(0), b.signed_integer_code_length(-1))

    def test_empty_codeword_requires_single_symbol(self):
        self.assertTrue(b.is_prefix_free([""]))
        self.assertFalse(b.is_prefix_free(["", "1"]))
        self.assertFalse(b.is_prefix_free(["0", "01"]))
        self.assertFalse(b.is_prefix_free(["0", "0"]))

    def test_decoder_rejects_truncation_trailing_and_nonbinary(self):
        for bad in ("", "1", "10", "11", "100", "110", "00", "0101", "1010", "11x", None):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                b.signed_integer_decode(bad)


class PointedPreparationTests(unittest.TestCase):
    def test_empty_and_free_words_keep_actual_zero(self):
        for length in range(7):
            for letters in product("RN", repeat=length):
                result = b.evaluate_preparation(letters)
                self.assertEqual(result["seed"], 0)
                self.assertEqual(result["cost"], 0)

    def test_negative_one_and_negative_sixteen_each_cost_one(self):
        one, sixteen = b.evaluate_preparation("-"), b.evaluate_preparation("-R")
        self.assertEqual((one["seed"], one["cost"]), (-1, 1))
        self.assertEqual((sixteen["seed"], sixteen["cost"]), (-16, 1))
        self.assertNotEqual(b.signed_integer_code_length(-1), b.signed_integer_code_length(-16))

    def test_positive_cost_is_required_but_not_sufficient_for_displacement(self):
        self.assertEqual(b.evaluate_preparation("+-")["seed"], 0)
        self.assertEqual(b.evaluate_preparation("+-")["cost"], 2)
        for length in range(5):
            for word in product("RN+-", repeat=length):
                result = b.evaluate_preparation(word)
                if result["seed"]:
                    self.assertGreaterEqual(result["cost"], result["positive_cost_gap"])

    def test_wrong_free_generators_are_rejected(self):
        for multiplier, offset in ((1, -1), (16, 1), (-1, -1)):
            with self.assertRaises(ValueError):
                b.AffinePreparation(multiplier, offset, 0)

    def test_rational_cost_gap_and_cross_base_are_declared_resources(self):
        operations = {"a": b.AffinePreparation(1, 2, F(1, 7)),
                      "r": b.AffinePreparation(3, 0, 0)}
        self.assertEqual(b.evaluate_preparation("ar", operations)["seed"], 6)
        self.assertEqual(b.evaluate_preparation("ar", operations)["positive_cost_gap"], F(1, 7))
        for radix in (2, 3, 10, 16, 27):
            self.assertEqual(b.evaluate_preparation("-R", base=radix)["seed"], -radix)


class CausalBoundaryTests(unittest.TestCase):
    def test_recurrence_against_direct_green_sum(self):
        forcing = (F(2, 3), F(-7, 5), F(0), F(11, 13), F(1, 19))
        for radix, seed in product((2, 3, 10, 16, 27), (F(-16), F(), F(1, 256), F(-7, 40))):
            history = b.recurrence_history(forcing, seed, base=radix)
            for n, value in enumerate(history):
                expected = radix**n*seed+sum((radix**(n-k)*forcing[k-1]
                                              for k in range(1, n+1)), F())
                self.assertEqual(value, expected)

    def test_finite_time_charge_reconstruction_and_scaling(self):
        forcing = tuple(native_r(n) for n in range(1, 98))
        for seed in (F(-16), F(-1), F(), F(1, 16), F(-7, 40)):
            history = b.recurrence_history(forcing, seed)
            scaled = b.scaled_history(history)
            for n in (0, 1, 2, 5, 37, 61, 97):
                self.assertEqual(b.homogeneous_charge(forcing[:n], history[n], n), seed)
                if n:
                    self.assertEqual(scaled[n]-scaled[n-1], forcing[n-1]/16**n)

    def test_future_change_leaves_retarded_prefix_unchanged(self):
        for length in (0, 2, 5, 37, 61, 97):
            prefix = tuple(native_r(n) for n in range(1, length+1))
            first, second = prefix+(F(1, 7),), prefix+(F(8, 7),)
            self.assertEqual(b.recurrence_history(first)[:length+1],
                             b.recurrence_history(second)[:length+1])
            self.assertEqual(b.finite_advanced_seed(second)-b.finite_advanced_seed(first),
                             -F(1, 16**(length+1)))

    def test_finite_advanced_boundary_minimizes_terminal_displacement(self):
        forcing = (F(1), F(2, 7), F(-1, 11))
        seed = b.finite_advanced_seed(forcing)
        self.assertEqual(b.recurrence_history(forcing, seed)[-1], 0)
        self.assertNotEqual(seed, 0)
        self.assertEqual(b.finite_advanced_seed([1]), F(-1, 16))
        self.assertNotEqual(b.recurrence_history([1])[-1], 0)

    def test_inertia_alone_does_not_select_the_seed(self):
        for seed in (F(-16), F(), F(1, 3)):
            history = b.recurrence_history([0]*5, seed)
            self.assertEqual(b.scaled_history(history), (seed,)*6)

    def test_static_translation_changes_source_moving_translation_does_not(self):
        forcing, shift = (F(1, 3), F(2, 7), F(3, 11)), F(5, 13)
        original = b.recurrence_history(forcing, F(2, 5))
        static = tuple(x-shift for x in original)
        self.assertEqual(static, b.recurrence_history(
            [r+15*shift for r in forcing], F(2, 5)-shift))
        moving = tuple(x-16**n*shift for n, x in enumerate(original))
        self.assertEqual(moving, b.recurrence_history(forcing, F(2, 5)-shift))


class PhaseObservationTests(unittest.TestCase):
    def test_integer_seed_offsets_are_phase_invisible_at_all_tested_times(self):
        for radix, h, offset, time in product((2, 3, 10, 16, 27), (-7, 1, 5),
                                             (-16, -1, 0, 1), (0, 1, 2, 5, 97)):
            self.assertEqual(b.seed_phase_residue(offset, time, frequency=h, base=radix), 0)
            self.assertEqual(b.eventual_phase_equivalence_start(offset, frequency=h, base=radix), 0)

    def test_exact_eventual_thresholds_and_impossibility(self):
        cases = ((F(1, 16), 16, 1, 1), (F(1, 256), 16, 1, 2),
                 (F(1, 256), 2, 1, 8), (F(1, 3), 16, 1, None),
                 (F(1, 3), 3, 1, 1), (F(1, 3), 16, -3, 0),
                 (F(-7, 40), 10, 1, 3), (F(-7, 40), 16, 1, None),
                 (F(1, 81), 27, 1, 2))
        for offset, radix, h, expected in cases:
            self.assertEqual(b.eventual_phase_equivalence_start(offset, frequency=h, base=radix), expected)
            if expected is not None:
                self.assertEqual(b.seed_phase_residue(offset, expected, frequency=h, base=radix), 0)
                if expected:
                    self.assertNotEqual(b.seed_phase_residue(offset, expected-1, frequency=h, base=radix), 0)

    def test_phase_difference_from_independent_same_source_histories(self):
        seeds = (F(-16), F(-1), F(), F(1), F(1, 16), F(1, 256), F(1, 3), F(-7, 40))
        forcing = (F(2, 3), F(-5, 7), F(11, 13), F(17, 19), F(23, 29))
        for radix, seed, h in product((2, 3, 10, 16, 27), seeds, (-7, 1, 5)):
            actual = b.recurrence_history(forcing, seed, base=radix)
            reference = b.recurrence_history(forcing, base=radix)
            for start in (0, 1, 2, 5):
                difference = h*(actual[start]-reference[start])
                self.assertEqual(difference % 1,
                                 b.seed_phase_residue(seed, start, frequency=h, base=radix))
                self.assertEqual(difference.denominator == 1,
                                 b.phase_equivalent_from(seed, start, frequency=h, base=radix))


class SourceControlsTests(unittest.TestCase):
    def test_authentic_four_pole_source_and_zero_boundary(self):
        history = b.authentic_source_history(97)
        self.assertEqual(history[0], 0)
        self.assertEqual(history[1], F(47, 15))
        for n in (1, 2, 37, 61, 97):
            direct = F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)
            self.assertEqual(history[n]-16*history[n-1], direct)
            self.assertEqual(direct, native_r(n))
            shifted = F(4, 8*n-6)-F(2, 8*n-3)-F(1, 8*n-2)-F(1, 8*n-1)
            self.assertNotEqual(direct, shifted)
            self.assertNotEqual(direct, direct+F(1, 8*n-7))

    def test_coherent_family_closed_form_against_recurrence(self):
        for shift in (F(), F(1), F(2), F(7, 5), F(19)):
            forcing = tuple(b.coherent_source_r(n, shift) for n in range(1, 98))
            closed = b.coherent_source_history(97, shift)
            self.assertEqual(closed, b.recurrence_history(forcing))
            self.assertEqual(closed[0], 0)
            self.assertTrue(all(r > 0 for r in forcing))
            for n in (37, 61, 97):
                a = F(8*n-7)
                direct = 16/(a+shift)**2-1/(a+shift+8)**2
                self.assertEqual(direct, forcing[n-1])
                self.assertNotEqual(direct, native_r(n))

    def test_coherent_limit_mode_has_exact_small_tail_representative(self):
        for shift in (F(), F(1), F(2), F(7, 5), F(19)):
            h = b.coherent_source_limit_mode(shift)
            for n in (1, 37, 61, 97):
                state = b.coherent_source_history(n, shift)[-1]
                tail = F(1)/(8*n+shift+1)**2
                self.assertEqual((h*(state+tail)).denominator, 1)
                self.assertGreater(tail, 0)
            self.assertGreater(h, 0)


class DomainValidationTests(unittest.TestCase):
    def test_exact_input_rejections(self):
        cases = (
            lambda: b.signed_integer_encode(True), lambda: b.signed_integer_encode(1.0),
            lambda: b.signed_integer_code_length(F(1)), lambda: b.integer_kraft_partial(-1),
            lambda: b.is_prefix_free(["2"]), lambda: b.AffinePreparation(1, 0, -1),
            lambda: b.AffinePreparation(1, 0, 0.0), lambda: b.evaluate_preparation("X"),
            lambda: b.evaluate_preparation("", {"x": (1, 0, 0)}),
            lambda: b.recurrence_history([1.0]), lambda: b.recurrence_history([], base=1),
            lambda: b.recurrence_history([], base=True), lambda: b.scaled_history([]),
            lambda: b.homogeneous_charge([], 0, 1), lambda: b.homogeneous_charge([], 0, -1),
            lambda: b.finite_advanced_seed([F(1)], base=F(16)),
            lambda: b.seed_phase_residue(F(1, 3), -1),
            lambda: b.seed_phase_residue(F(1, 3), 1, frequency=0),
            lambda: b.eventual_phase_equivalence_start(0.5),
            lambda: b.phase_equivalent_from(0, -1), lambda: b.coherent_laplace(0),
            lambda: b.coherent_laplace(1, -1), lambda: b.coherent_source_r(0),
            lambda: b.coherent_source_history(-1), lambda: b.coherent_source_limit_mode(1.0),
            lambda: b.authentic_source_history(True),
        )
        for case in cases:
            with self.subTest(case=case), self.assertRaises(ValueError):
                case()


if __name__ == "__main__":
    unittest.main()
