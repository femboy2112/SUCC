"""Countermodels for maximal-looking finite novelty and hidden source clocks."""
import unittest
from observational_succ.maximal_novelty_source import (
    NoveltyError, cyclic_blocks, de_bruijn_binary, exact_decoder_possible,
    full_binary_shift_has_cyclic_factor, least_period,
    maximal_window_periodic_witness, program_count_bound,
    rooted_cycle_factor_possible,
)


class MaximalNoveltySourceTests(unittest.TestCase):
    def test_independent_known_order_four(self):
        self.assertEqual("".join(map(str, de_bruijn_binary(4))), "0000100110101111")

    def test_all_cyclic_words_once_but_periodic(self):
        for k in range(1, 9):
            w = maximal_window_periodic_witness(k)
            self.assertEqual(w["distinct_order_k_blocks"], 1 << k)
            self.assertEqual(w["global_source_period"], 1 << k)
            self.assertFalse(w["globally_aperiodic"])
            self.assertFalse(w["Martin_Lof_randomness_certified"])

    def test_separate_brute_force_window_oracle(self):
        from itertools import product
        for k in range(1, 7):
            bits = de_bruijn_binary(k)
            self.assertEqual(set(cyclic_blocks(bits, k)),
                             set(product((0, 1), repeat=k)))
            self.assertEqual(least_period(bits), 1 << k)

    def test_cycle_observer_must_respect_divisibility(self):
        self.assertTrue(rooted_cycle_factor_possible(16, 8))
        self.assertFalse(rooted_cycle_factor_possible(16, 3))
        self.assertFalse(rooted_cycle_factor_possible(4, 5))
        self.assertTrue(rooted_cycle_factor_possible(1, 1))

    def test_full_shift_fixed_point_blocks_all_nontrivial_clocks(self):
        self.assertTrue(full_binary_shift_has_cyclic_factor(1))
        for m in range(2, 32):
            self.assertFalse(full_binary_shift_has_cyclic_factor(m))
        # An orbit can be dense and free even though its closure includes a
        # fixed point; hence universal continuous clocks are NOT guaranteed.

    def test_exact_decoder_requires_no_collisions(self):
        self.assertTrue(exact_decoder_possible((("01", "a"), ("10", "b"))))
        self.assertFalse(exact_decoder_possible((("01", "a"), ("10", "a"))))
        self.assertTrue(exact_decoder_possible((("01", "a"), ("01", "a"))))

    def test_short_program_count_only_not_randomness_oracle(self):
        for n, c in ((8, 2), (10, 5), (5, 5), (1, 0)):
            r = program_count_bound(n, c)
            self.assertLess(r["maximum_strings_describable_below_length_minus_deficiency"],
                            1 << max(n-c, 0))
            self.assertFalse(r["algorithmic_randomness_decided"])
        self.assertEqual(program_count_bound(10, 3)
                         ["maximum_strings_describable_below_length_minus_deficiency"], 127)

    def test_reject_malformed_source_records(self):
        for bad in (0, -1, 2.5, True, 13):
            with self.assertRaises(NoveltyError):
                de_bruijn_binary(bad)
        with self.assertRaises(NoveltyError):
            cyclic_blocks((0, 2), 2)
        with self.assertRaises(NoveltyError):
            program_count_bound(2.5, 1)
        with self.assertRaises(NoveltyError):
            rooted_cycle_factor_possible(0, 3)
        with self.assertRaises(NoveltyError):
            full_binary_shift_has_cyclic_factor(0)


if __name__ == "__main__":
    unittest.main()
