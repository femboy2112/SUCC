"""Finite exact calibration of a classical universal theorem; not QFT verification."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import random
import unittest

from observational_succ.collective_spectral import Gaussian as C
from observational_succ.hopf_source_exact import H, ONE, ZERO, I, J, K
from observational_succ.ym_trace_observer import (
    TraceBank, conjugate_tuple, oriented_volume, same_gauge_orbit,
    stereographic_unit, trace_bank, vector_dot, word_trace,
)


# Declared before execution; distinct from the exploratory Q8 corpus.
HOLDOUT_POINTS = (
    (Q(1, 2), Q(-2, 3), Q(3, 5)),
    (Q(-3, 7), Q(5, 13), Q(1, 4)),
    (Q(2, 11), Q(-4, 9), Q(7, 12)),
    (Q(-5, 8), Q(3, 10), Q(-1, 6)),
)
HOLDOUT_GAUGES = (
    (Q(2, 3), Q(1, 7), Q(-3, 5)),
    (Q(-1, 4), Q(5, 9), Q(2, 7)),
    (Q(7, 10), Q(-2, 11), Q(1, 3)),
)


def matrix(q):
    # Independent 2x2 representation of the Hamilton multiplication table.
    return ((C(q.a, q.b), C(q.c, q.d)),
            (C(-q.c, q.d), C(q.a, -q.b)))


def matrix_product(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)), C())
                       for j in range(2)) for i in range(2))


def determinant(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


class TraceObserverTests(unittest.TestCase):
    def setUp(self):
        self.points = tuple(stereographic_unit(t) for t in HOLDOUT_POINTS)
        self.gauges = tuple(stereographic_unit(t) for t in HOLDOUT_GAUGES)

    def test_exact_carrier_and_input_contract(self):
        self.assertTrue(all(q.norm2() == 1 for q in self.points+self.gauges))
        self.assertEqual(stereographic_unit((0, 0, 0)), ONE)
        with self.assertRaises(TypeError): stereographic_unit((0.1, 0, 0))
        with self.assertRaises(TypeError): trace_bank(((1, 0, 0, 0),))
        with self.assertRaises(ValueError): trace_bank((ZERO,))
        with self.assertRaises(ValueError): trace_bank((H(2),))
        with self.assertRaises(ValueError): TraceBank((Q(0),), (Q(0),), ())
        with self.assertRaises(TypeError): TraceBank((0.1,), (), ())

    def test_fresh_common_conjugations(self):
        original = trace_bank(self.points)
        for gauge in self.gauges:
            transformed = conjugate_tuple(self.points, gauge)
            self.assertEqual(trace_bank(transformed), original)
            self.assertTrue(same_gauge_orbit(self.points, transformed))
            self.assertNotEqual(transformed, self.points)

    def test_fresh_gram_and_oriented_volume_reconstruction(self):
        for points in (self.points, *[conjugate_tuple(self.points, g) for g in self.gauges]):
            bank = trace_bank(points)
            expected = tuple(tuple(vector_dot(a, b) for b in points) for a in points)
            self.assertEqual(bank.gram(), expected)
            self.assertEqual(bank.volumes(), tuple(oriented_volume(*t) for t in combinations(points, 3)))

    def test_fresh_signed_words_against_matrix_implementation(self):
        rng = random.Random(4192026)
        for _ in range(64):
            word = tuple(rng.choice((-4, -3, -2, -1, 1, 2, 3, 4))
                         for _ in range(rng.randrange(1, 10)))
            acc = matrix(ONE)
            for letter in word:
                q = self.points[abs(letter)-1]
                acc = matrix_product(acc, matrix(q if letter > 0 else q.conj()))
            actual = (acc[0][0]+acc[1][1])*C(Q(1, 2))
            self.assertEqual(actual, C(word_trace(self.points, word)))
        self.assertEqual(word_trace((), ()), 1)
        for word in ((0,), (5,), (True,)):
            with self.assertRaises(ValueError): word_trace(self.points, word)

    def test_orientation_twins_kill_pair_only_observer(self):
        positive, negative = (I, J, K), (I, J, -K)
        a, b = trace_bank(positive), trace_bank(negative)
        self.assertEqual((a.singles, a.pairs, a.gram()), (b.singles, b.pairs, b.gram()))
        self.assertEqual(a.triples, (Q(-1),))
        self.assertEqual(b.triples, (Q(1),))
        self.assertFalse(same_gauge_orbit(positive, negative))
        self.assertEqual(tuple(x*x for x in a.volumes()), tuple(x*x for x in b.volumes()))

    def test_degenerate_ranks_are_valid_not_unobservable(self):
        for points in ((), (ONE, -ONE), (I, -I, ONE), (I, J, -I, -J)):
            for gauge in self.gauges:
                self.assertTrue(same_gauge_orbit(points, conjugate_tuple(points, gauge)))
        # A reflection of a planar tuple extends to a proper 3D rotation.
        self.assertTrue(same_gauge_orbit((I, J), (I, -J)))
        self.assertEqual(conjugate_tuple((I, J), I), (I, -J))

    def test_independent_gauges_are_a_source_mutation(self):
        self.assertEqual(trace_bank((I, I)).singles, trace_bank((I, J)).singles)
        self.assertFalse(same_gauge_orbit((I, I), (I, J)))

    def test_mean_bank_does_not_determine_a_source_law(self):
        # Same mean of the complete one-holonomy bank, different second moment.
        first = tuple(trace_bank((q,)).singles[0] for q in (ONE, -ONE))
        second = trace_bank((I,)).singles[0]
        self.assertEqual(sum(first)/2, second)
        self.assertNotEqual(sum(x*x for x in first)/2, second*second)

    def test_order_is_observable(self):
        self.assertEqual(word_trace((I, J, K), (1, 2, 3)), -1)
        self.assertEqual(word_trace((I, J, K), (1, 3, 2)), 1)

    def test_q8_exploratory_corpus_reproduced(self):
        q8 = (ONE, -ONE, I, -I, J, -J, K, -K)
        rotations = []
        for perm in permutations(range(3)):
            for signs in product((-1, 1), repeat=3):
                r = tuple(tuple(signs[i]*int(perm[i] == j) for j in range(3)) for i in range(3))
                if determinant(r) == 1:
                    rotations.append(r)
        def rotate(q, r):
            v = (q.b, q.c, q.d)
            return (q.a, *(sum(r[i][j]*v[j] for j in range(3)) for i in range(3)))
        pairs, triples, orbits = {}, {}, set()
        for points in product(q8, repeat=3):
            orbit = min(tuple(rotate(q, r) for q in points) for r in rotations)
            bank = trace_bank(points)
            orbits.add(orbit)
            pairs.setdefault((bank.singles, bank.pairs), set()).add(orbit)
            triples.setdefault(bank, set()).add(orbit)
            self.assertEqual(bank.volumes(), (oriented_volume(*points),))
        self.assertEqual((len(rotations), len(orbits), len(pairs), len(triples)), (24, 50, 49, 50))
        self.assertEqual(sum(len(v) > 1 for v in pairs.values()), 1)
        self.assertTrue(all(len(v) == 1 for v in triples.values()))


if __name__ == "__main__":
    unittest.main()
