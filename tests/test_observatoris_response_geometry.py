"""Exact tests for response geometry: positivity, balance, gauge and cone bounds.

Exhaustive enumerations are over fully declared small tables.  They can
falsify the stated theorems; they are not their proofs (see CAUSAL_GEOMETRY.md).
"""
from fractions import Fraction
from itertools import product
import random
import unittest

from observational_succ.observatoris_response_geometry import (
    SIGNED_DIAMOND,
    ResponseGeometryError,
    absolute,
    cancellations,
    detection_lower_bound,
    diagonal_similarity,
    edges,
    effect_time,
    gauge_invariant_dimension,
    is_nonnegative,
    matrix,
    powers,
    quotient_pattern,
    relevance,
    rescale,
    simple_cycle_products,
    structural_distance,
    switching_function,
    triangle_violations,
    walk_exists,
    warning_margin,
)


def all_matrices(n, values):
    for flat in product(values, repeat=n * n):
        yield matrix(tuple(flat[i * n:(i + 1) * n] for i in range(n)))


def random_matrix(rng, n, values, density):
    return matrix(tuple(tuple(rng.choice(values) if rng.random() < density else 0
                              for _ in range(n)) for _ in range(n)))


class SupportAndPositivity(unittest.TestCase):
    def test_response_support_is_always_inside_structural_walks(self):
        # RG-1 soundness, exhaustively for all 3x3 tables over {-1, 0, 1}.
        count = 0
        for a in all_matrices(3, (-1, 0, 1)):
            walks = walk_exists(a, 4)
            for tau, p in enumerate(powers(a, 4)):
                for x in range(3):
                    for y in range(3):
                        if p[y][x] != 0:
                            self.assertTrue(walks[tau][y][x])
            count += 1
        self.assertEqual(count, 3 ** 9)

    def test_nonnegative_tables_never_cancel(self):
        # RG-1 completeness for A >= 0: all 3x3 tables over {0, 1, 2}.
        for a in all_matrices(3, (0, 1, 2)):
            self.assertEqual(cancellations(a, 4), ())

    def test_effect_time_equals_structural_distance_when_nonnegative(self):
        rng = random.Random(20261114)
        for _ in range(300):
            a = random_matrix(rng, 5, (1, 2, Fraction(1, 3)), 0.3)
            dist = structural_distance(a)
            for x in range(5):
                for y in range(5):
                    self.assertEqual(effect_time(a, x, y), dist[x][y])

    def test_signed_effect_time_is_never_early(self):
        rng = random.Random(7)
        late = 0
        for _ in range(400):
            a = random_matrix(rng, 4, (1, -1), 0.5)
            dist = structural_distance(a)
            for x in range(4):
                for y in range(4):
                    t = effect_time(a, x, y)
                    if dist[x][y] is None:
                        self.assertIsNone(t)
                    elif t is not None:
                        self.assertGreaterEqual(t, dist[x][y])
                        late += t > dist[x][y]
                    else:
                        late += 1
        self.assertGreater(late, 0)  # the inequality is strict somewhere

    def test_effect_time_none_is_an_all_lag_statement(self):
        # Cayley-Hamilton horizon: zero on lags 0..n-1 forces zero on 0..3n.
        rng = random.Random(11)
        for _ in range(300):
            a = random_matrix(rng, 4, (1, -1, 2), 0.5)
            far = powers(a, 12)
            for x in range(4):
                for y in range(4):
                    if effect_time(a, x, y) is None:
                        self.assertTrue(all(p[y][x] == 0 for p in far))

    def test_dimension_horizon_is_sharp(self):
        # A length-(n-1) chain first responds at lag n-1: n-1 zeros prove nothing.
        n = 5
        chain = matrix(tuple(tuple(int(v == u + 1) for u in range(n)) for v in range(n)))
        self.assertEqual(effect_time(chain, 0, n - 1), n - 1)
        self.assertTrue(all(p[n - 1][0] == 0 for p in powers(chain, n - 2)))


class SignedDiamond(unittest.TestCase):
    def test_every_edge_is_live_but_the_composite_never_responds(self):
        a = SIGNED_DIAMOND
        self.assertEqual(set(edges(a)), {(0, 1), (0, 2), (1, 3), (2, 3)})
        self.assertEqual(structural_distance(a)[0][3], 2)
        self.assertIsNone(effect_time(a, 0, 3))
        self.assertEqual(cancellations(a, 6), ((2, 0, 3),))
        self.assertIsNone(switching_function(a))

    def test_triangle_inequality_fails_for_the_signed_diamond(self):
        self.assertIn((0, 1, 3), triangle_violations(SIGNED_DIAMOND, 1, 1))

    def test_intervening_on_one_branch_restores_the_response(self):
        # Holding branch y' fixed deletes its incoming edge: do(z_{y'} = c).
        cut = matrix((
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 1, -1, 0),
        ))
        self.assertEqual(effect_time(cut, 0, 3), 2)

    def test_three_nodes_cannot_hide_a_dependency_at_every_lag(self):
        # Minimality (proved in CAUSAL_GEOMETRY.md for all real weights): no
        # 3-node sign table has a structurally reachable pair whose response
        # vanishes at all lags.
        for a in all_matrices(3, (-1, 0, 1)):
            dist = structural_distance(a)
            for x in range(3):
                for y in range(3):
                    if dist[x][y] is not None:
                        self.assertIsNotNone(effect_time(a, x, y))

    def test_single_lag_cancellation_needs_only_two_nodes(self):
        a = matrix(((1, 0), (1, -1)))
        self.assertEqual(cancellations(a, 2), ((2, 0, 1),))
        self.assertEqual(effect_time(a, 0, 1), 1)


class Balance(unittest.TestCase):
    def test_balanced_tables_have_absolute_powers_and_no_cancellation(self):
        # RG-4 exhaustively over all 3x3 sign patterns.
        balanced = unbalanced = 0
        for a in all_matrices(3, (-1, 0, 1)):
            s = switching_function(a)
            if s is None:
                unbalanced += 1
                continue
            balanced += 1
            switched = matrix(tuple(tuple(s[v] * a[v][u] * s[u] for u in range(3))
                                    for v in range(3)))
            self.assertTrue(is_nonnegative(switched))
            self.assertEqual(cancellations(a, 4), ())
            for p, q in zip(powers(a, 4), powers(absolute(a), 4)):
                self.assertEqual(absolute(p), q)
        self.assertGreater(balanced, 0)
        self.assertGreater(unbalanced, 0)

    def test_balanced_tables_obey_the_multiplicative_triangle_inequality(self):
        rng = random.Random(3)
        for _ in range(200):
            a = random_matrix(rng, 4, (1, -1, 2, Fraction(-1, 2)), 0.5)
            if switching_function(a) is not None:
                self.assertEqual(triangle_violations(a, 2, 2, Fraction(1, 2)), ())

    def test_cancellation_implies_imbalance_with_generic_magnitudes(self):
        rng = random.Random(5)
        seen = 0
        for _ in range(500):
            a = random_matrix(rng, 4, (1, -1, 2, -3, Fraction(1, 2)), 0.6)
            if cancellations(a, 5):
                seen += 1
                self.assertIsNone(switching_function(a))
        self.assertGreater(seen, 0)

    def test_imbalance_does_not_imply_cancellation(self):
        # A directed 3-cycle with one negative edge is unbalanced, but there is
        # at most one walk of each length between two nodes: nothing cancels.
        a = matrix(((0, 0, -1), (1, 0, 0), (0, 1, 0)))
        self.assertIsNone(switching_function(a))
        self.assertEqual(cancellations(a, 9), ())

    def test_negative_self_loop_is_unbalanced(self):
        self.assertIsNone(switching_function(matrix(((-1,),))))
        self.assertEqual(switching_function(matrix(((1,),))), (1,))


class Gauge(unittest.TestCase):
    def test_unit_change_multiplies_response_by_a_potential_ratio(self):
        rng = random.Random(13)
        for _ in range(100):
            a = random_matrix(rng, 4, (1, 2, Fraction(1, 3)), 0.6)
            d = tuple(Fraction(rng.randint(1, 5), rng.randint(1, 5)) for _ in range(4))
            b = rescale(a, d)
            for p, q in zip(powers(a, 5), powers(b, 5)):
                for x in range(4):
                    for y in range(4):
                        self.assertEqual(q[y][x], d[y] * p[y][x] / d[x])
            ra, rb = relevance(a, 5), relevance(b, 5)
            for x in range(4):
                for y in range(4):
                    # round-trip relevance is unit-free
                    self.assertEqual(ra[x][y] * ra[y][x], rb[x][y] * rb[y][x])

    def test_one_way_closeness_order_is_not_unit_free(self):
        # Sources 0 and 1 both feed target 2; a unit change reverses their order.
        a = matrix(((0, 0, 0), (0, 0, 0), (2, 1, 0)))
        b = rescale(a, (Fraction(4), Fraction(1), Fraction(1)))
        ra, rb = relevance(a, 2), relevance(b, 2)
        self.assertGreater(ra[0][2], ra[1][2])
        self.assertLess(rb[0][2], rb[1][2])

    def test_diagonal_similarity_iff_equal_cycle_products_when_strongly_connected(self):
        rng = random.Random(17)
        agree = differ = 0
        for _ in range(400):
            n = 3
            a = random_matrix(rng, n, (1, 2, 3), 0.7)
            dist = structural_distance(a)
            if any(dist[x][y] is None for x in range(n) for y in range(n)):
                continue
            b = tuple(tuple(v * rng.choice((1, 1, 2)) for v in row) for row in a)
            b = matrix(b)
            same_cycles = simple_cycle_products(a) == simple_cycle_products(b)
            units = diagonal_similarity(a, b)
            self.assertEqual(units is not None, same_cycles)
            if units is not None:
                self.assertEqual(rescale(a, units), b)
                agree += 1
            else:
                differ += 1
        self.assertGreater(agree, 0)
        self.assertGreater(differ, 0)

    def test_cycle_products_do_not_suffice_without_strong_connectivity(self):
        # The acyclic diamond has no directed cycle at all, yet its two parallel
        # paths carry one unit-free ratio.
        a = matrix(((0, 0, 0, 0), (1, 0, 0, 0), (1, 0, 0, 0), (0, 1, 1, 0)))
        b = matrix(((0, 0, 0, 0), (1, 0, 0, 0), (1, 0, 0, 0), (0, 1, 2, 0)))
        self.assertEqual(simple_cycle_products(a), {})
        self.assertEqual(simple_cycle_products(b), {})
        self.assertIsNone(diagonal_similarity(a, b))
        self.assertEqual(gauge_invariant_dimension(a), 1)

    def test_every_positive_forest_weighting_is_a_unit_convention(self):
        # Path 0 -> 1 -> 2 plus branch 1 -> 3: Betti number zero.
        pattern = ((0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0))
        ones = matrix(pattern)
        self.assertEqual(gauge_invariant_dimension(ones), 0)
        rng = random.Random(19)
        for _ in range(50):
            b = matrix(tuple(tuple(v * Fraction(rng.randint(1, 9), rng.randint(1, 9))
                                   for v in row) for row in pattern))
            units = diagonal_similarity(ones, b)
            self.assertIsNotNone(units)
            self.assertEqual(rescale(ones, units), b)

    def test_gauge_dimension_counts_free_ratios(self):
        # Two-cycle plus a self-loop: 3 edges, 2 nodes, 1 component.
        a = matrix(((1, 1), (1, 0)))
        self.assertEqual(gauge_invariant_dimension(a), 2)
        self.assertEqual(set(simple_cycle_products(a)), {(0,), (0, 1)})

    def test_similarity_refuses_pattern_or_sign_changes(self):
        a = matrix(((0, 1), (1, 0)))
        self.assertIsNone(diagonal_similarity(a, matrix(((0, 1), (0, 0)))))
        self.assertIsNone(diagonal_similarity(a, matrix(((0, -1), (1, 0)))))
        with self.assertRaises(ResponseGeometryError):
            rescale(a, (Fraction(1), Fraction(0)))


class ConesAndQuotients(unittest.TestCase):
    def test_quotient_distance_never_exceeds_source_distance(self):
        # Tropical instance of weighted PAP-02, all 4-node patterns with a
        # random labelling each, plus strictness.
        rng = random.Random(23)
        strict = 0
        for _ in range(600):
            a = random_matrix(rng, 4, (1,), 0.3)
            m = rng.randint(1, 4)
            labels = list(range(m)) + [rng.randrange(m) for _ in range(4 - m)]
            rng.shuffle(labels)
            labels = tuple(labels)
            dq = structural_distance(quotient_pattern(a, labels))
            ds = structural_distance(a)
            for x in range(4):
                for y in range(4):
                    if ds[x][y] is not None:
                        self.assertIsNotNone(dq[labels[x]][labels[y]])
                        self.assertLessEqual(dq[labels[x]][labels[y]], ds[x][y])
                    strict += (dq[labels[x]][labels[y]] is not None
                               and (ds[x][y] is None or dq[labels[x]][labels[y]] < ds[x][y])
                               and labels[x] != labels[y])
        self.assertGreater(strict, 0)

    def test_ghost_shortcut_receipt(self):
        # Source chain 0 -> 1 -> 2 -> 3; the observer merges nodes 0 and 2.
        # The source edge 2 -> 3 then reads as a one-step route from the block
        # of node 0 to node 3, which the source needs three steps to realise.
        a = matrix(((0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)))
        labels = (0, 1, 0, 2)
        self.assertEqual(structural_distance(a)[0][3], 3)
        self.assertEqual(structural_distance(quotient_pattern(a, labels))[0][2], 1)

    def test_warning_margin_and_detection_bound(self):
        # cause 0 -> 1 -> 2 (target), and 0 -> 3 -> 4 -> 5 (sensor).
        a = matrix(tuple(tuple(int((u, v) in {(0, 1), (1, 2), (0, 3), (3, 4), (4, 5)})
                               for u in range(6)) for v in range(6)))
        self.assertEqual(detection_lower_bound(a, 0, (5,)), 3)
        self.assertEqual(warning_margin(a, 0, 2, (5,)), -1)   # harm precedes evidence
        self.assertEqual(warning_margin(a, 0, 2, (3,)), 1)    # a nearer sensor warns
        self.assertIsNone(warning_margin(a, 5, 2, (3,)))
        # sharpness on this nonnegative carrier: bounds are attained exactly
        self.assertEqual(effect_time(a, 0, 5), 3)
        self.assertEqual(effect_time(a, 0, 2), 2)

    def test_records_cannot_depend_on_the_cause_before_the_bound(self):
        # Cone lemma, executed: two runs differing only at the cause have equal
        # sensor histories strictly before the structural bound, for signed and
        # unsigned carriers alike.
        rng = random.Random(29)
        for _ in range(300):
            n = 5
            a = random_matrix(rng, n, (1, -1, 2), 0.35)
            cause, sensors = 0, (3, 4)
            bound = detection_lower_bound(a, cause, sensors)
            base = [Fraction(rng.randint(-2, 2)) for _ in range(n)]
            other = list(base)
            other[cause] += 1
            limit = n + 2 if bound is None else bound
            for _ in range(limit):
                self.assertEqual([base[s] for s in sensors], [other[s] for s in sensors])
                base = [sum(a[v][u] * base[u] for u in range(n)) for v in range(n)]
                other = [sum(a[v][u] * other[u] for u in range(n)) for v in range(n)]

    def test_malformed_tables_are_refused(self):
        with self.assertRaises(ResponseGeometryError):
            matrix(((1, 2),))
        with self.assertRaises(ResponseGeometryError):
            quotient_pattern(matrix(((1, 0), (0, 1))), (0, 2))


if __name__ == "__main__":
    unittest.main()
