"""Independent exact finite controls for the carrier-first arithmetic operator."""
import unittest
from itertools import product
from math import isqrt

from carrier_probe import (
    additive_triples_left, additive_triples_right,
    alternate_empty_mask, convolution, multiplicative_triples_left,
    multiplicative_triples_right, pair_matrix, plus, scope_report, sieve,
    times, trial_prime, two_color_goldbach,
)


class CarrierFirstTests(unittest.TestCase):
    def test_two_prime_oracles_agree(self):
        p = sieve(512)
        for i in range(513):
            self.assertEqual(p[i], trial_prime(i), i)

    def test_primitive_factorization_zero_is_exactly_prime(self):
        for n in range(2, 513):
            self.assertEqual(len(times(n)) == 0, trial_prime(n), n)

    def test_both_reduced_coproducts_coassociative(self):
        for n in range(2, 85):
            self.assertEqual(sorted(additive_triples_left(n)), sorted(additive_triples_right(n)), n)
            self.assertEqual(sorted(multiplicative_triples_left(n)), sorted(multiplicative_triples_right(n)), n)

    def test_prime_pair_adjoint_composition(self):
        p = sieve(256)
        # Independent coefficient calculation from pair convolution.
        all_counts = convolution(p)
        for n in range(4, 257):
            self.assertEqual(two_color_goldbach(n, p), all_counts[n], n)
            self.assertEqual(all_counts[n], sum(1 for a in range(2, n - 1)
                if trial_prime(a) and trial_prime(n-a)), n)

    def test_prime_pair_matrix_is_outer_product(self):
        p = sieve(32)
        v = tuple(int(p[i]) for i in range(2, 33))
        a = pair_matrix(v)
        self.assertEqual(len(a), len(v))
        self.assertEqual(tuple(a[i][i] for i in range(len(v))), v)
        for i in range(len(v)):
            for j in range(len(v)):
                self.assertEqual(a[i][j], v[i] * v[j])

    def test_mask_matrix_class_exact_information_count(self):
        m = 8
        mats = {pair_matrix(bits) for bits in product((0, 1), repeat=m)}
        self.assertEqual(len(mats), 2 ** m)

    def test_black_box_midpoint_pairs_disjoint(self):
        for n in range(2, 64):
            pairs = [{n-d, n+d} for d in range(n-1)]
            self.assertEqual(len(pairs), n-1)
            for i, p in enumerate(pairs):
                for q in pairs[i+1:]:
                    self.assertTrue(p.isdisjoint(q))
            z, s = alternate_empty_mask(n, n-2)
            self.assertEqual(sum(z[a]*z[b] for a,b in plus(2*n)), 0)
            self.assertEqual(sum(s[a]*s[b] for a,b in plus(2*n)), 2 if n>2 else 1)

    def test_counterfeit_source_blocks_all_0_mod_4(self):
        p = sieve(256)
        fake = [False] * 257
        for k in range(2, 257):
            fake[k] = p[k] and k % 4 == 1
        for n in range(4, 257, 4):
            self.assertEqual(two_color_goldbach(n, fake), 0, n)
        self.assertGreater(two_color_goldbach(10, fake), 0)

    def test_midpoint_chart_can_raise_matrix_rank(self):
        # The endpoint interaction matrix has rank 1, but midpoint/displacement
        # reindexing is NOT a tensor product of coordinate changes.
        p = sieve(16)
        chart = [[int(p[n-d] and p[n+d]) for d in (0, 1)] for n in (5, 6)]
        self.assertEqual(chart, [[1, 0], [0, 1]])
        self.assertEqual(chart[0][0] * chart[1][1] - chart[0][1] * chart[1][0], 1)

    def test_sum_projection_schmidt_rank_equals_ordered_goldbach_count(self):
        # After projecting the separable prime pair state onto a sum fiber N,
        # each surviving a has a unique orthogonal counterpart b=N-a.
        p = sieve(64)
        for n in range(4, 65):
            supported_a = [a for a, b in plus(n) if p[a] and p[b]]
            self.assertEqual(len(supported_a), two_color_goldbach(n, p))
            self.assertEqual(len(set(supported_a)), len(supported_a))
            self.assertEqual(len({n-a for a in supported_a}), len(supported_a))
        self.assertEqual(two_color_goldbach(20, p), 4)

    def test_scope_report(self):
        d = scope_report()
        self.assertEqual(d["ordered_goldbach_count"]["20"], 4)
        self.assertEqual(d["ordered_goldbach_count"]["22"], 5)
        self.assertEqual(d["one_mod_four_prime_subsource"]["100"], 0)

if __name__ == '__main__':
    unittest.main()