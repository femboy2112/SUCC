import unittest
from fractions import Fraction as Q

import return_paths as rp


class ReturnPathTests(unittest.TestCase):
    def test_five_common_entry_and_distinct_return_targets(self):
        paths = rp.return_family(5)
        self.assertEqual([path.initial_period for path in paths], [5] * 4)
        self.assertEqual([path.basis(1) for path in paths], [1] * 4)
        self.assertEqual([path.basis(6) for path in paths], [2, 3, 4, 5])
        for label in (2, 3, 4, 5, 7, 8, 9, 10):
            self.assertTrue(all(path.basis(label) is None for path in paths))

    def test_composite_extra_entry_is_an_explicit_falsifier(self):
        self.assertEqual(rp.domain_multiplicities(6), {2: 1, 3: 2, 6: 2})
        self.assertEqual(rp.ReturnPath(6, 3).basis(3), 2)
        self.assertIsNone(rp.ReturnPath(6, 1).basis(3))
        self.assertEqual([rp.family_eigenvalue(6, m) for m in range(1, 8)],
                         [5, 0, 1, 2, 1, 0, 5])
        self.assertEqual(rp.projection_defect(6, 3), Q(4, 25))

    def test_literal_words_and_gcd_normal_forms_agree(self):
        for n in (3, 5, 6, 9, 12, 37, 49):
            for a in range(1, n + 1):
                path = rp.ReturnPath(n, a)
                for label in range(1, 51):
                    self.assertEqual(path.basis(label),
                                     rp.evaluate_word(label, path.word))

    def test_adjoint_and_initial_range_projections(self):
        path = rp.ReturnPath(15, 6)  # q=5, r=2
        for label in range(1, 71):
            image = path.basis(label)
            if image is not None:
                self.assertEqual(path.adjoint_basis(image), label)
            inverse = path.adjoint_basis(label)
            if inverse is not None:
                self.assertEqual(path.basis(inverse), label)
            self.assertEqual(image is not None, (label - 1) % 5 == 0)
            self.assertEqual(inverse is not None, (label - 1) % 2 == 0)

    def test_power_formula_and_non_norm_witness(self):
        for n, a in ((5, 2), (6, 4), (12, 9)):
            path = rp.ReturnPath(n, a)
            for rounds in range(1, 7):
                source = 1 + path.initial_period**rounds
                expected = 1 + path.range_period**rounds
                self.assertEqual(path.power_basis(source, rounds), expected)
                self.assertEqual(rp.norm_squared(path.apply({source: 1}, rounds=rounds)), 1)
                for label in range(1, 71):
                    literal = label
                    for _ in range(rounds):
                        if literal is not None:
                            literal = rp.evaluate_word(literal, path.word)
                    self.assertEqual(path.power_basis(label, rounds), literal)

    def test_finite_state_tail_identity(self):
        state = {1: Q(2, 3), 6: Q(1, 2), 26: Q(-3, 7), 126: Q(5, 11)}
        path = rp.ReturnPath(5, 2)
        for rounds in range(5):
            image = path.apply(state, rounds=rounds)
            image.pop(1, None)
            expected = sum((value**2 for label, value in state.items()
                            if label != 1 and (label - 1) % 5**rounds == 0), Q(0))
            self.assertEqual(rp.norm_squared(image), expected)
        self.assertEqual(path.apply(state, rounds=4), {1: Q(2, 3)})

    def test_identity_channel_is_not_part_of_the_proper_family(self):
        for n in (2, 5, 6):
            identity = rp.ReturnPath(n, n)
            self.assertFalse(identity.proper)
            self.assertEqual(identity.apply({1: 1, 13: Q(2, 5)}), {1: Q(1), 13: Q(2, 5)})
            self.assertEqual(len(rp.return_family(n)), n - 1)
            with self.assertRaises(ValueError):
                rp.coherent_sum(n, {n: 1}, {1: 1})

    def test_root_path_cancellation_and_constructive_interference(self):
        plus, minus = {1: Q(1, 2), 2: Q(1, 2)}, {1: Q(1, 2), 2: Q(-1, 2)}
        self.assertEqual(rp.coherent_sum(5, plus, {1: 1}), {1: Q(1)})
        self.assertEqual(rp.coherent_sum(5, minus, {1: 1}), {})
        self.assertEqual(rp.separate_intensity(5, plus, {1: 1}), Q(1, 2))
        self.assertEqual(rp.separate_intensity(5, minus, {1: 1}), Q(1, 2))

    def test_nonunit_interference_requires_coincident_outputs(self):
        state = {6: 1, 11: 1}
        plus, minus = {1: Q(1, 2), 2: Q(1, 2)}, {1: Q(1, 2), 2: Q(-1, 2)}
        self.assertEqual(rp.coherent_sum(5, plus, state),
                         {2: Q(1, 2), 3: Q(1), 5: Q(1, 2)})
        self.assertEqual(rp.norm_squared(rp.coherent_sum(5, plus, state)), Q(3, 2))
        self.assertEqual(rp.norm_squared(rp.coherent_sum(5, minus, state)), Q(1, 2))
        self.assertEqual(rp.separate_intensity(5, plus, state), 1)
        self.assertEqual(rp.separate_intensity(5, minus, state), 1)
        # On just e6 the two outputs are orthogonal: no interference term.
        self.assertEqual(rp.norm_squared(rp.coherent_sum(5, plus, {6: 1})), Q(1, 2))
        self.assertEqual(rp.norm_squared(rp.coherent_sum(5, minus, {6: 1})), Q(1, 2))

    def test_affine_composition_and_parallel_arrow_distinction(self):
        successor, double = rp.Affine(1, 1), rp.Affine(2, 0)
        self.assertEqual(double.after(successor), rp.Affine(1, 2).after(double))
        self.assertEqual(len(rp.affine_hom(1, 5)), 5)
        self.assertEqual(len(rp.affine_hom(2, 5)), 2)
        self.assertEqual(rp.affine_hom(6, 5), ())
        # Same root vertex trace 1,2,4,5 can use S or V2 at its first edge.
        route_s = successor.after(double).after(successor)
        route_v = successor.after(double).after(double)
        self.assertEqual((route_s(1), route_v(1)), (5, 5))
        self.assertEqual((route_s(2), route_v(2)), (7, 9))
        self.assertNotEqual(route_s, route_v)

    def test_gram_is_sum_of_actual_initial_projections(self):
        state = {m: Q((-1)**m, m) for m in range(1, 41)}
        for n in (2, 5, 6, 9, 13, 15):
            observed = {}
            for path in rp.return_family(n):
                for label, value in path.apply(path.apply(state), adjoint=True).items():
                    observed[label] = observed.get(label, Q(0)) + value
            self.assertEqual(observed, rp.family_observation(n, state))

    def test_boundary_validation_and_offset_mutation(self):
        for args in ((1, 1), (5, 0), (5, 6)):
            with self.assertRaises(ValueError):
                rp.ReturnPath(*args)
        for args in ((True, 1), (5, Q(2))):
            with self.assertRaises(TypeError):
                rp.ReturnPath(*args)
        for bad_state in ({0: 1}, {-1: 1}):
            with self.assertRaises(ValueError):
                rp.sparse_state(bad_state)
        for bad_state in ({1: 0.5}, {1: True}):
            with self.assertRaises(TypeError):
                rp.sparse_state(bad_state)
        with self.assertRaises(ValueError):
            rp.evaluate_word(1, (("D", 2), ("BAD", 1)))
        self.assertEqual(rp.family_eigenvalue(5, 6), 4)
        # The incorrect unpointed gcd(5,6)-1 would be zero.
        self.assertNotEqual(rp.family_eigenvalue(5, 6), 0)


if __name__ == "__main__":
    unittest.main()
