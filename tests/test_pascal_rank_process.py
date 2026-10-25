"""Exact controls for all one-window Pascal laws without normality."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
import unittest

from observational_succ.pascal_rank_process import (
    WORDS, binomial_rank_law, block_law, block_segment_law, character,
    enumerate_window_law, four_word_formula, symbol_table, window_rank_law,
)


class PascalRankProcessTests(unittest.TestCase):
    def test_block_is_positive_normalized_exactly(self):
        for t in (Q(-1, 2), Q(-1, 4), 0, Q(1, 4), Q(1, 3), Q(1, 2)):
            law = block_law(t)
            self.assertEqual(sum(law.values()), 1)
            self.assertGreaterEqual(min(law.values()), 0)
        self.assertEqual(set(block_law().values()), {Q(1, 32), Q(1, 16), Q(3, 32)})

    def test_all_proper_contiguous_block_segments_uniform(self):
        for t in (Q(-1, 2), Q(1, 4), Q(1, 3)):
            for start in range(5):
                for length in range(5 - start):
                    if length == 4:
                        continue
                    expected = {w: Q(1, 2**length) for w in product((0, 1), repeat=length)}
                    self.assertEqual(block_segment_law(start, length, t), expected)

    def test_full_block_rank_is_binomial_with_nonuniform_words(self):
        for t in (Q(-1, 2), Q(1, 4), Q(1, 3)):
            rank = defaultdict(Q)
            for word, mass in block_law(t).items():
                rank[sum(word)] += mass
            self.assertEqual(dict(rank), binomial_rank_law(4))
            self.assertNotEqual(len(set(block_law(t).values())), 1)

    def test_exact_four_word_witness(self):
        law = enumerate_window_law(4)
        self.assertEqual(law, four_word_formula())
        self.assertEqual(law[(0, 0, 1, 0)], Q(9, 128))
        self.assertEqual(law[(0, 1, 0, 0)], Q(7, 128))
        self.assertEqual(law[(0, 0, 0, 0)], Q(1, 16))

    def test_signed_positional_characters_survive_alignment_average(self):
        for t in (Q(-1, 2), Q(1, 4), Q(1, 3)):
            law = enumerate_window_law(4, t)
            self.assertEqual(sum(p * character(w, (0, 1, 3)) for w, p in law.items()), t / 4)
            self.assertEqual(sum(p * character(w, (0, 2, 3)) for w, p in law.items()), -t / 4)

    def test_contiguous_one_two_three_word_laws_are_uniform(self):
        for length in (1, 2, 3):
            self.assertEqual(set(enumerate_window_law(length).values()), {Q(1, 2**length)})

    def test_direct_whole_block_enumeration_matches_rank_convolution(self):
        for length in range(11):
            rank = defaultdict(Q)
            for word, mass in enumerate_window_law(length).items():
                rank[sum(word)] += mass
            self.assertEqual(dict(rank), window_rank_law(length))

    def test_all_alignments_match_independent_binomial_reference(self):
        for length in range(33):
            for offset in range(4):
                self.assertEqual(window_rank_law(length, alignment=offset), binomial_rank_law(length))

    def test_held_out_parameter_and_long_windows(self):
        for t in (Q(-1, 2), Q(1, 3)):
            for length in (0, 1, 7, 11, 19, 33, 64):
                self.assertEqual(window_rank_law(length, t), binomial_rank_law(length))
            self.assertEqual(enumerate_window_law(4, t), four_word_formula(t))

    def test_shift_marginal_consistency(self):
        for length in range(1, 8):
            longer = enumerate_window_law(length + 1)
            left, right = defaultdict(Q), defaultdict(Q)
            for w, p in longer.items():
                left[w[:-1]] += p
                right[w[1:]] += p
            self.assertEqual(dict(left), enumerate_window_law(length))
            self.assertEqual(dict(right), enumerate_window_law(length))

    def test_pairwise_independence_does_not_remove_triple_interaction(self):
        law = enumerate_window_law(8)
        for i, j in combinations(range(8), 2):
            pair = defaultdict(Q)
            for w, p in law.items():
                pair[(w[i], w[j])] += p
            self.assertEqual(dict(pair), {(0, 0): Q(1, 4), (0, 1): Q(1, 4),
                                          (1, 0): Q(1, 4), (1, 1): Q(1, 4)})

    def test_uniform_mutation_removes_the_detected_defect(self):
        uniform = enumerate_window_law(4, 0)
        self.assertEqual(set(uniform.values()), {Q(1, 16)})
        self.assertNotEqual(uniform, enumerate_window_law(4))
        self.assertEqual(window_rank_law(17, 0), window_rank_law(17))

    def test_alphabet_map_has_exact_required_multiplicities(self):
        table = symbol_table()
        self.assertEqual(len(table), 32)
        counts = Counter(table)
        self.assertEqual({w: Q(counts[w], 32) for w in WORDS}, block_law())

    def test_invalid_domains_and_explicit_enumeration_budget(self):
        for t in (0.25, Q(3, 4), True):
            with self.assertRaises(ValueError):
                block_law(t)
        for length in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                window_rank_law(length)
        with self.assertRaises(ValueError):
            block_segment_law(3, 2)
        with self.assertRaises(ValueError):
            enumerate_window_law(100)
        with self.assertRaises(ValueError):
            enumerate_window_law(1, alignment=4)
        with self.assertRaises(ValueError):
            character((0, 1), (1, 1))


if __name__ == "__main__":
    unittest.main()
