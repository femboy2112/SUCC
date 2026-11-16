"""Calibrated exact controls for present-cut transport and retained branches."""
from fractions import Fraction as F
import unittest

from twin_transport import (CenteredReturn, LinearChain, LinearMap, Space,
                            flag_branch, fresh_flags, inner, sparse_inner,
                            sparse_state)


class TwinTransportTests(unittest.TestCase):
    def test_cut_pairing_survives_rectangular_and_singular_maps(self):
        a, b, c = Space("a", 2), Space("b", 3), Space("c", 1)
        chain = LinearChain((a, b, c), (
            LinearMap(a, b, ((1, 2), (0, 0), (-1, 3))),
            LinearMap(b, c, ((2, 5, -1),))))
        profile = chain.cuts((2, -1), (3,))
        self.assertEqual(profile.pairings, (F(15),) * 3)
        self.assertEqual(profile.local_defects, (0, 0))
        self.assertGreater(len(set(profile.squared_state_gaps)), 1)

    def test_zero_length_path_and_named_types(self):
        a = Space("left", 2)
        chain = LinearChain((a,), ())
        self.assertEqual(chain.cuts((1, 0), (0, 1)).pairings, (0,))
        other = Space("other-frame", 2)
        with self.assertRaises(ValueError):
            LinearMap.identity(a).after(LinearMap.identity(other))
        with self.assertRaises(ValueError):
            LinearChain((a, other), (LinearMap.identity(a),))

    def test_unitary_matching_boundaries_agree_at_current_cut(self):
        spaces = tuple(Space(str(i), 2) for i in range(4))
        entries = (((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5))),
                   ((1, 0), (0, -1)), ((0, 1), (-1, 0)))
        chain = LinearChain(spaces, tuple(LinearMap(spaces[i], spaces[i+1], m)
                                         for i, m in enumerate(entries)))
        self.assertTrue(all(a.is_unitary() for a in chain.arrows))
        left = (F(5, 13), F(12, 13))
        right = chain.total().apply(left)
        profile = chain.cuts(left, right)
        self.assertEqual(profile.squared_state_gaps, (0,) * 4)
        shifted = (right[0] + 2, right[1] - 1)
        self.assertEqual(chain.cuts(left, shifted).squared_state_gaps, (5,) * 4)

    def test_endpoint_mismatch_is_not_repaired_by_meeting(self):
        a = Space("meeting", 2)
        chain = LinearChain((a, a), (LinearMap.identity(a),))
        profile = chain.cuts((1, 0), (0, 1))
        self.assertEqual(profile.pairings, (0, 0))
        self.assertEqual(profile.squared_state_gaps, (2, 2))

    def test_adjoint_is_not_inverse_for_a_projection(self):
        a = Space("a", 2)
        projection = LinearMap(a, a, ((1, 0), (0, 0)))
        self.assertFalse(projection.is_unitary())
        profile = LinearChain((a, a), (projection,)).cuts((1, 1), (1, 0))
        self.assertEqual(profile.squared_state_gaps, (1, 0))
        self.assertEqual(profile.pairings, (1, 1))

    def test_isometry_without_surjectivity_can_hide_boundary_residual(self):
        a, b = Space("one", 1), Space("two", 2)
        embedding = LinearMap(a, b, ((1,), (0,)))
        self.assertFalse(embedding.is_unitary())
        profile = LinearChain((a, b), (embedding,)).cuts((1,), (1, 1))
        self.assertEqual(profile.squared_state_gaps, (0, 1))

    def test_relative_sign_mutation_is_missed_on_root(self):
        a = Space("phase-calibrated", 2)
        normal = LinearChain((a, a), (LinearMap.identity(a),))
        mutant = LinearChain((a, a), (LinearMap(a, a, ((1, 0), (0, -1))),))
        self.assertEqual(normal.cuts((1, 0), (1, 0),
                         reverse_chain=mutant).local_defects, (0,))
        exposed = normal.cuts((0, 1), (0, 1), reverse_chain=mutant)
        self.assertEqual(exposed.pairings, (-1, 1))
        self.assertEqual(exposed.local_defects, (2,))

    def test_rejection_information_survives_extension(self):
        t = CenteredReturn(3, 2)
        self.assertEqual(t.apply({1: 1}), {})
        self.assertEqual(t.unitary(({1: 1}, {})), ({}, {1: F(1)}))
        self.assertEqual(t.unitary(t.unitary(({1: 1}, {})), adjoint=True),
                         ({1: F(1)}, {}))

    def test_block_inverse_on_both_channels_and_sparse_superpositions(self):
        for q, r in ((3, 2), (7, 3), (17, 5), (29, 11), (71, 29)):
            t = CenteredReturn(q, r)
            original = ({0: F(3, 5), q: F(4, 5), 997: F(-2, 7)},
                        {0: F(1, 13), r: F(-5, 11), 1009: F(7, 17)})
            output = t.unitary(original)
            self.assertEqual(t.unitary(output, adjoint=True), original)
            self.assertEqual(t.unitary(t.unitary(original, adjoint=True)), original)
            norm = lambda z: sum(sparse_inner(x, x) for x in z)
            self.assertEqual(norm(output), norm(original))

    def test_reusing_one_block_unitary_does_not_dilate_powers(self):
        t = CenteredReturn(3, 2)
        source = {1: F(1)}
        self.assertEqual(t.apply(t.apply(source)), {})
        self.assertEqual(t.unitary(t.unitary((source, {})))[0], source)

    def test_fresh_flags_keep_all_accept_product_and_total_norm(self):
        returns = (CenteredReturn(3, 2), CenteredReturn(5, 3),
                   CenteredReturn(7, 4), CenteredReturn(17, 5))
        source = {0: F(1, 3), 1: F(-2, 5), 105: F(7, 11), 1785: F(13, 17)}
        flags = fresh_flags(returns, source)
        direct = sparse_state(source)
        for t in returns:
            direct = t.apply(direct)
        self.assertEqual(flag_branch(flags, (0,) * len(returns)), direct)
        self.assertEqual(sum(x*x for x in flags.values()), sparse_inner(source, source))
        self.assertEqual(fresh_flags((), source), {((), k): v for k, v in source.items()})

    def test_common_root_does_not_determine_return_map(self):
        left, right = CenteredReturn(5, 1), CenteredReturn(5, 2)
        self.assertEqual(left.apply({0: 1}), right.apply({0: 1}))
        self.assertEqual(left.apply({5: 1}), {1: F(1)})
        self.assertEqual(right.apply({5: 1}), {2: F(1)})

    def test_invalid_numeric_and_operator_contracts_are_rejected(self):
        for q, r in ((1, 1), (4, 2), (2, 3)):
            with self.assertRaises(ValueError):
                CenteredReturn(q, r)
        with self.assertRaises(TypeError):
            sparse_state({0: 0.5})
        with self.assertRaises(TypeError):
            CenteredReturn(True, 1)
        with self.assertRaises(ValueError):
            sparse_state({-1: 1})
        with self.assertRaises(ValueError):
            LinearMap(Space("x", 2), Space("y", 1), ((1,),))
        with self.assertRaises(TypeError):
            CenteredReturn(3, 2).apply({}, adjoint=1)


if __name__ == "__main__":
    unittest.main()
