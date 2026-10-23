"""Exact independent contractions and hostile controls for arithmetic codes."""
import itertools
import unittest
from fractions import Fraction as F

from observational_succ.holographic_reconstruction import (
    ArithmeticTreeCode, arithmetic_code, copy_refinement, logical_filter_gram,
    minimum_tree_cut, nonstar_pair_control, pair_decoder,
)
from observational_succ.padic_bulk_network import bruhat_tits_ball, bt_sphere


IDENTITY = tuple(tuple(F(i == j) for j in range(3)) for i in range(3))


class TestHolographicReconstruction(unittest.TestCase):
    def test_genuine_trivalent_geometry_and_refinement(self):
        for radius in (1, 2, 3):
            code = ArithmeticTreeCode(radius=radius)
            boundary = code.geometric_boundary()
            ball = bruhat_tits_ball(2, radius)
            self.assertEqual(set(boundary), set(ball.boundary))
            self.assertEqual(len(boundary), code.sites)
            if radius == 1:
                self.assertEqual(boundary, bt_sphere(2, 1))
            else:
                previous = ArithmeticTreeCode(radius=radius - 1).geometric_boundary()
                self.assertEqual(tuple(v.parent() for v in boundary), tuple(v for v in previous for _ in range(2)))

    def test_uniform_and_arithmetic_encodings_are_isometric(self):
        for radius in (1, 2, 3):
            for amplitudes in ((F(1),) * 3, (F(1), F(1, 2), F(1, 4)), (F(0), F(2), F(-3))):
                code = ArithmeticTreeCode(amplitudes, radius)
                self.assertEqual(code.gram(), IDENTITY)

    def test_orthogonality_independent_full_column_contraction(self):
        code = arithmetic_code(2, 1)
        rows = list(itertools.product(range(3), repeat=3))
        # Dense numerator matrix is independently specified without column().
        matrix = [[F(1, 2**r) if word == (r, (r+k) % 3, (r+2*k) % 3) else F(0)
                   for k in range(3)] for word in rows for r in [word[0]]]
        for a, b in itertools.product(range(3), repeat=2):
            self.assertEqual(sum(row[a] * row[b] for row in matrix), F(a == b) * F(21, 16))

    def test_all_pair_decoders_are_bijections(self):
        for pair in itertools.combinations(range(3), 2):
            outputs = {pair_decoder(pair, x, y) for x, y in itertools.product(range(3), repeat=2)}
            self.assertEqual(outputs, set(itertools.product(range(3), repeat=2)))
            e = next(iter(set(range(3)) - set(pair)))
            for k, r in itertools.product(range(3), repeat=2):
                x, y = ((r+i*k) % 3 for i in pair)
                self.assertEqual(pair_decoder(pair, x, y), (k, (r+e*k) % 3))

    def test_all_uniform_matrix_unit_intertwiners_including_heldout_pairs(self):
        code = ArithmeticTreeCode()
        for pair in ((0, 1), (0, 2), (1, 2)):
            for a, b, k in itertools.product(range(3), repeat=3):
                self.assertEqual(code.intertwining_defect(a, b, k, pair), {})

    def test_boundary_representation_is_adjoint_preserving(self):
        code = ArithmeticTreeCode()
        words = tuple(itertools.product(range(3), repeat=3))
        for a, b in itertools.product(range(3), repeat=2):
            for x in words:
                image = code.boundary_matrix_unit(x, a, b, (0, 2))
                for y in words:
                    self.assertEqual(image.get(y, 0), code.boundary_matrix_unit(y, b, a, (0, 2)).get(x, 0))

    def test_uniform_singletons_hide_every_complex_logical_state(self):
        code = ArithmeticTreeCode()
        expected = {((r,), (r,)): F(1, 3) for r in range(3)}
        for site, k, l in itertools.product(range(3), repeat=3):
            self.assertEqual(code.reduce_matrix_unit(k, l, (site,)), expected if k == l else {})

    def test_knill_laflamme_and_failed_singleton_recovery(self):
        code = ArithmeticTreeCode()
        for erased in itertools.combinations(range(3), 1):
            self.assertTrue(code.corrects_erasure(erased))
        for erased in itertools.combinations(range(3), 2):
            self.assertFalse(code.corrects_erasure(erased))
        with self.assertRaises(ValueError):
            code.reconstructing_pair((0,))

    def test_arithmetic_weights_and_privileged_recovery(self):
        code = arithmetic_code(2, 1)
        self.assertEqual(code.weights, (F(16, 21), F(4, 21), F(1, 21)))
        self.assertTrue(code.corrects_erasure((0,)))
        self.assertFalse(code.corrects_erasure((1,)))
        self.assertFalse(code.corrects_erasure((2,)))
        for a, b, k in itertools.product(range(3), repeat=3):
            self.assertEqual(code.intertwining_defect(a, b, k, (1, 2)), {})
        with self.assertRaises(ValueError):
            code.reconstructing_pair((0, 1))

    def test_weighted_erasure_leak_has_exact_trace_distance(self):
        code = arithmetic_code(2, 1)
        first = code.reduce_matrix_unit(0, 0, (1,))
        second = code.reduce_matrix_unit(1, 1, (1,))
        distance = sum(abs(first.get(key, 0) - second.get(key, 0)) for key in first.keys() | second.keys()) / 2
        self.assertEqual(distance, F(5, 7))

    def test_malformed_and_composite_sources_rejected(self):
        for p in (0, 1, 4, 6, 9, True):
            with self.assertRaises(ValueError):
                arithmetic_code(p, 1)
        with self.assertRaises(ValueError):
            ArithmeticTreeCode((F(0), F(0), F(0)))
        with self.assertRaises(ValueError):
            ArithmeticTreeCode((1.0, F(1), F(1)))
        with self.assertRaises(ValueError):
            ArithmeticTreeCode().reduce_matrix_unit(0, 0, (0, 0))

    def test_logical_weight_filter_is_not_internal_weight_deformation(self):
        f = (F(1), F(1, 2), F(1, 4))
        self.assertNotEqual(logical_filter_gram(f), IDENTITY)
        self.assertEqual(ArithmeticTreeCode(f).gram(), IDENTITY)

    def test_source_preserving_refinement_square(self):
        for code in (ArithmeticTreeCode(), arithmetic_code(3, 2)):
            for radius in (1, 2, 3):
                current = ArithmeticTreeCode(code.amplitudes, radius)
                for k in range(3):
                    self.assertEqual(copy_refinement(current.column(k)), current.refined().column(k))

    def test_all_radius_two_regions_against_analytic_access_prediction(self):
        # These 64 regions were not used to choose the root tensor.
        for amplitudes in ((F(1),) * 3, (F(1), F(1, 2), F(1, 4))):
            code = ArithmeticTreeCode(amplitudes, radius=2)
            for mask in range(1 << code.sites):
                keep = tuple(i for i in range(code.sites) if mask & (1 << i))
                erased = tuple(i for i in range(code.sites) if i not in keep)
                full = code.full_branches(keep)
                predicted = len(full) >= 2 if len(set(amplitudes)) == 1 else 1 in full and 2 in full
                self.assertEqual(code.corrects_erasure(erased), predicted, (amplitudes, keep))
                if predicted:
                    for a, b, k in itertools.product(range(3), repeat=3):
                        self.assertEqual(code.intertwining_defect(a, b, k, keep), {})

    def test_fresh_radius_three_boundary_regions(self):
        code = arithmetic_code(5, 1, radius=3)
        self.assertTrue(code.corrects_erasure(tuple(range(4))))
        self.assertFalse(code.corrects_erasure((0, 4)))
        self.assertEqual(code.intertwining_defect(2, 0, 0, tuple(range(4, 12))), {})

    def test_geometry_cut_oracle_independently_enumerated(self):
        radius = 2
        code = ArithmeticTreeCode(radius=radius)
        ball = bruhat_tits_ball(2, radius)
        boundary = code.geometric_boundary()
        interior = [v for v in ball.vertices if v not in ball.boundary]
        for mask in range(1 << code.sites):
            keep = tuple(i for i in range(code.sites) if mask & (1 << i))
            boundary_colors = {v: int(i in keep) for i, v in enumerate(boundary)}
            optimum = len(ball.edges)
            for colors in itertools.product((0, 1), repeat=len(interior)):
                label = dict(boundary_colors, **{})
                label.update(dict(zip(interior, colors)))
                optimum = min(optimum, sum(label[a] != label[b] for a, b in ball.edges))
            self.assertEqual(minimum_tree_cut(radius, keep), optimum)

    def test_refinement_breaks_unconditional_min_cut_equality(self):
        code = ArithmeticTreeCode(radius=2)
        keep = (0, 2)  # one leaf in each of two different top-level branches
        reduced = code.reduce_matrix_unit(0, 0, keep)
        self.assertEqual(reduced, {((r, r), (r, r)): F(1, 3) for r in range(3)})
        self.assertEqual(minimum_tree_cut(2, keep), 2)
        # Exact spectrum is (1/3,1/3,1/3): entropy log3, bound 2 log3.

    def test_nonmaximal_bond_entropy_and_filter_countercontrol(self):
        code = arithmetic_code(2, 1)
        reduced = code.reduce_matrix_unit(0, 0, (0,))
        self.assertEqual(tuple(reduced[((r,), (r,))] for r in range(3)), code.weights)
        self.assertEqual(minimum_tree_cut(1, (0,)), 1)
        # Local contraction changes Schmidt probabilities (4/5,1/5) -> (1/2,1/2).
        input_weights = (F(4, 5), F(1, 5))
        filtered = (input_weights[0] * F(1, 4), input_weights[1])
        self.assertEqual(sum(filtered), F(2, 5))
        self.assertEqual(tuple(x / sum(filtered) for x in filtered), (F(1, 2), F(1, 2)))

    def test_bare_intertwining_can_pass_while_adjoint_transport_and_qec_fail(self):
        code = arithmetic_code(2, 1)
        for a, b, k in itertools.product(range(3), repeat=3):
            result = {}
            for word, value in code.column(k).items():
                for image, coefficient in nonstar_pair_control(code, (0, 1), word, a, b).items():
                    result[image] = result.get(image, 0) + value * coefficient
            self.assertEqual(result, code.column(a) if k == b else {})
        forward = nonstar_pair_control(code, (0, 1), (0, 0, 0), 1, 0)
        backward = nonstar_pair_control(code, (0, 1), (1, 2, 0), 0, 1)
        self.assertEqual(forward, {(1, 2, 0): F(1, 2)})
        self.assertEqual(backward, {(0, 0, 0): F(2)})
        self.assertNotEqual(forward[(1, 2, 0)], backward[(0, 0, 0)])
        self.assertFalse(code.corrects_erasure((2,)))

    def test_geometric_root_isotropy_detects_arithmetic_direction_choice(self):
        uniform = ArithmeticTreeCode()
        weighted = arithmetic_code(2, 1)
        directions = bt_sphere(2, 1)
        geometric_permutations = set()
        for a, b, c, d in itertools.product((0, 1), repeat=4):
            if (a * d - b * c) % 2:
                matrix = ((a, b), (c, d))
                geometric_permutations.add(tuple(directions.index(v.gl2_action(matrix)) for v in directions))
        self.assertEqual(geometric_permutations, set(itertools.permutations(range(3))))
        preserved = []
        for permutation in itertools.permutations(range(3)):
            self.assertTrue(all(not uniform.root_permutation_defect(permutation, k) for k in range(3)))
            if all(not weighted.root_permutation_defect(permutation, k) for k in range(3)):
                preserved.append(permutation)
        self.assertEqual(preserved, [(0, 1, 2), (0, 2, 1)])


if __name__ == "__main__":
    unittest.main()
