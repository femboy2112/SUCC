"""Independent exact walk, Gram, resolvent and zero-forcing inverse controls."""
import itertools
import unittest
from fractions import Fraction as Q

from observational_succ.reality_pin_geometry import (
    GeometryError, GraphPassport, block_hankel, boundary_moments,
    boundary_response, coordinate_boundary, first_return_extension,
    identity, multiply, rank, reconstruct_zero_forcing, transpose,
    zero_forcing_schedule,
)


def walk_entry(a, start, end, length):
    # Exponential literal enumeration, independent of the matrix-power oracle.
    if length == 0:
        return Q(start == end)
    value = Q()
    for middle in itertools.product(range(len(a)), repeat=length-1):
        path = (start,) + middle + (end,)
        weight = Q(1)
        for u, v in zip(path, path[1:]):
            weight *= a[u][v]
        value += weight
    return value


def extend(a, c, d):
    return (tuple(tuple(row) + tuple(c[i]) for i, row in enumerate(a))
            + tuple(tuple(row) + tuple(d[i]) for i, row in enumerate(transpose(c))))


def grounded_matrix(size, edges):
    a = [[Q() for _ in range(size)] for _ in range(size)]
    for u, v, sign in edges:
        g = Q(2 + u + v, 1 + v)
        a[u][v] = a[v][u] = sign * g
    for u in range(size):
        a[u][u] = 2 + u + sum(abs(x) for x in a[u])
    return tuple(tuple(row) for row in a)


class BoundaryGeometryTests(unittest.TestCase):
    def test_multiport_moments_match_literal_walk_enumeration(self):
        a = ((4, -1, 0), (-1, 5, -2), (0, -2, 6))
        boundary = (0, 2)
        moments = boundary_moments(a, coordinate_boundary(3, boundary), 4)
        for k in range(5):
            for i, u in enumerate(boundary):
                for j, v in enumerate(boundary):
                    self.assertEqual(moments[k][i][j], walk_entry(a, u, v, k))

    def test_block_hankel_equals_direct_krylov_gram(self):
        a = ((4, -1, 0, 0), (-1, 5, -2, 0), (0, -2, 6, -1), (0, 0, -1, 4))
        b = coordinate_boundary(4, (0, 3))
        h = block_hankel(boundary_moments(a, b, 4), 3)
        ab, aab = multiply(a, b), multiply(a, multiply(a, b))
        k = tuple(b[i] + ab[i] + aab[i] for i in range(4))
        self.assertEqual(h, multiply(transpose(k), k))
        self.assertEqual(rank(h), 4)
        self.assertEqual(rank(block_hankel(boundary_moments(a, b, 0), 1)), 2)

    def test_star_single_port_is_dark_but_leaf_multiport_complete(self):
        a = ((3, -1, -1), (-1, 2, 0), (-1, 0, 2))
        for boundary, expected in (((0,), 2), ((1, 2), 3)):
            m = boundary_moments(a, coordinate_boundary(3, boundary), 4)
            self.assertEqual(rank(block_hankel(m, 3)), expected)

    def test_first_return_general_block_extension(self):
        a = ((4, -2, 0), (-2, 6, -3), (0, -3, 5))
        b = coordinate_boundary(3, (0,))
        c = ((0, 0), (0, 0), (Q(2, 3), Q(5, 7)))
        order, jump = first_return_extension(a, b, c)
        self.assertEqual(order, 6)
        self.assertEqual(jump, ((36*(Q(4, 9)+Q(25, 49)),),))
        old = boundary_moments(a, b, order)
        for d in (((7, 1), (1, 8)), ((17, -3), (-3, 21))):
            full = extend(a, c, d)
            new = boundary_moments(full, coordinate_boundary(5, (0,)), order)
            self.assertEqual(new[:order], old[:order])
            self.assertEqual(new[order][0][0]-old[order][0][0], jump[0][0])

    def test_multiport_first_return_jump_is_a_matrix_gram(self):
        a = ((3, 1), (1, 4))
        b = identity(2)
        c = ((1, 2), (3, 4))
        order, jump = first_return_extension(a, b, c)
        self.assertEqual(order, 2)
        self.assertEqual(jump, ((5, 11), (11, 25)))
        full = extend(a, c, ((12, 0), (0, 13)))
        delta = boundary_moments(full, coordinate_boundary(4, (0, 1)), 2)[2]
        old = boundary_moments(a, b, 2)[2]
        self.assertEqual(tuple(tuple(delta[i][j]-old[i][j] for j in range(2))
                               for i in range(2)), jump)

    def test_signed_paths_cancel_and_delay_beyond_graph_distance(self):
        a = ((4, -1, -1), (-1, 2, 0), (-1, 0, 3))
        b = coordinate_boundary(3, (0,))
        c = ((0,), (1,), (-1,))
        order, jump = first_return_extension(a, b, c)
        self.assertEqual((order, jump), (6, ((Q(1),),)))
        full = extend(a, c, ((9,),))
        old = boundary_moments(a, b, 6)
        new = boundary_moments(full, coordinate_boundary(4, (0,)), 6)
        self.assertEqual(old[:6], new[:6])
        self.assertEqual(new[6][0][0]-old[6][0][0], 1)
        # Mutation: replacing one sign removes cancellation; topology unchanged.
        self.assertEqual(first_return_extension(a, b, ((0,), (1,), (1,)))[0], 4)

    def test_connected_extension_can_remain_forever_dark(self):
        a = ((4, -1, -1), (-1, 3, 0), (-1, 0, 3))
        b = coordinate_boundary(3, (0,))
        c = ((0,), (1,), (-1,))
        self.assertIsNone(first_return_extension(a, b, c))
        full = extend(a, c, ((7,),))
        for s in (0, 1, 3, Q(7, 2)):
            self.assertEqual(boundary_response(a, b, s),
                             boundary_response(full, coordinate_boundary(4, (0,)), s))

    def test_disconnected_ghost_extension_is_dark(self):
        self.assertIsNone(first_return_extension(((3,),), ((1,),), ((0, 0),)))

    def test_weak_extra_layer_keeps_exact_rank_without_noise_margin(self):
        for epsilon in (Q(1, 10), Q(1, 1000), Q(1, 1000000)):
            a = ((2, epsilon), (epsilon, 3))
            m = boundary_moments(a, ((1,), (0,)), 2)
            h = block_hankel(m, 2)
            self.assertEqual(rank(h), 2)
            self.assertEqual(h[0][0]*h[1][1]-h[0][1]*h[1][0], epsilon**2)

    def test_boundary_fixed_orthogonal_gauge_preserves_response(self):
        a = ((4, -1, 0), (-1, 4, -1), (0, -1, 4))
        u = ((1, 0, 0), (0, Q(4, 5), Q(-3, 5)), (0, Q(3, 5), Q(4, 5)))
        transformed = multiply(multiply(u, a), transpose(u))
        b = coordinate_boundary(3, (0,))
        self.assertNotEqual(a, transformed)
        self.assertNotEqual(transformed[0][2], 0)
        self.assertEqual(boundary_moments(a, b, 7), boundary_moments(transformed, b, 7))
        for s in (0, 1, 2, 11):
            self.assertEqual(boundary_response(a, b, s), boundary_response(transformed, b, s))

    def test_invalid_inputs_are_refused(self):
        with self.assertRaises(GeometryError):
            boundary_moments(((1, 1), (0, 2)), identity(2), 2)
        with self.assertRaises(GeometryError):
            boundary_moments(((1.0,),), ((1,),), 2)
        with self.assertRaises(GeometryError):
            block_hankel((((1,),),), 2)
        with self.assertRaises(GeometryError):
            coordinate_boundary(2, (0, 0))


class ZeroForcingRigidityTests(unittest.TestCase):
    def test_branched_tree_reconstruction_from_all_leaves(self):
        edges = ((0, 1, -1), (1, 2, -1), (1, 3, -1), (3, 4, -1), (3, 5, -1))
        passport = GraphPassport(6, (0, 2, 4, 5), edges, "synthetic-branched-tree")
        a = grounded_matrix(6, edges)
        m = boundary_moments(a, coordinate_boundary(6, passport.boundary), 5)
        self.assertEqual(len(zero_forcing_schedule(passport)), 2)
        self.assertEqual(reconstruct_zero_forcing(passport, m), a)

    def test_cycle_with_two_adjacent_boundary_vertices_reconstructs(self):
        edges = ((0, 1, -1), (0, 3, -1), (1, 2, -1), (2, 3, -1))
        passport = GraphPassport(4, (0, 1), edges, "synthetic-cycle")
        a = grounded_matrix(4, edges)
        m = boundary_moments(a, coordinate_boundary(4, passport.boundary), 5)
        self.assertEqual(reconstruct_zero_forcing(passport, m), a)

    def test_every_zero_forcing_passport_on_four_labels(self):
        pairs = tuple(itertools.combinations(range(4), 2))
        count = 0
        for mask in range(1 << len(pairs)):
            edges = tuple((u, v, -1) for j, (u, v) in enumerate(pairs) if mask & (1 << j))
            a = grounded_matrix(4, edges)
            for boundary_mask in range(1, 16):
                boundary = tuple(v for v in range(4) if boundary_mask & (1 << v))
                passport = GraphPassport(4, boundary, edges, "exhaustive-four-vertex")
                try:
                    zero_forcing_schedule(passport)
                except GeometryError:
                    continue
                maximum = 2*(4-len(boundary))+1
                m = boundary_moments(a, coordinate_boundary(4, boundary), maximum)
                self.assertEqual(reconstruct_zero_forcing(passport, m), a)
                count += 1
        self.assertEqual(count, 528)

    def test_non_forcing_star_gateway_is_refused(self):
        p = GraphPassport(3, (0,), ((0, 1, -1), (0, 2, -1)), "star")
        with self.assertRaises(GeometryError):
            zero_forcing_schedule(p)

    def test_fixed_sign_is_load_bearing(self):
        a = ((3, -2), (-2, 4))
        flipped = ((3, 2), (2, 4))
        b = coordinate_boundary(2, (0,))
        m = boundary_moments(a, b, 3)
        self.assertEqual(m, boundary_moments(flipped, b, 3))
        negative = GraphPassport(2, (0,), ((0, 1, -1),), "negative-source-chart")
        positive = GraphPassport(2, (0,), ((0, 1, 1),), "positive-source-chart")
        self.assertEqual(reconstruct_zero_forcing(negative, m), a)
        self.assertEqual(reconstruct_zero_forcing(positive, m), flipped)

    def test_short_budget_and_mutated_history_are_refused(self):
        p = GraphPassport(2, (0,), ((0, 1, -1),), "short-budget")
        m = boundary_moments(((3, -2), (-2, 4)), ((1,), (0,)), 5)
        with self.assertRaises(GeometryError):
            reconstruct_zero_forcing(p, m[:3])
        mutant = m[:-1] + (((m[-1][0][0]+1,),),)
        with self.assertRaises(GeometryError):
            reconstruct_zero_forcing(p, mutant)

    def test_wrong_graph_prior_refused_when_visible_entries_contradict(self):
        p = GraphPassport(3, (0, 1, 2), ((0, 1, -1),), "incorrect-topology")
        a = ((3, -1, -1), (-1, 4, 0), (-1, 0, 5))
        with self.assertRaises(GeometryError):
            reconstruct_zero_forcing(p, boundary_moments(a, identity(3), 1))

    def test_unknown_irrational_weight_not_silently_rounded(self):
        p = GraphPassport(2, (0,), ((0, 1, -1),), "rational-domain-only")
        # Real matrix [[3,-sqrt(2)],[-sqrt(2),4]] has these exact rational moments.
        with self.assertRaises(GeometryError):
            reconstruct_zero_forcing(p, (((1,),), ((3,),), ((11,),), ((47,),)))

    def test_invalid_passports_refused(self):
        for edges in (((0, 1, 0),), ((0, 1, -1), (0, 1, -1)), ((1, 0, -1),)):
            with self.assertRaises(GeometryError):
                GraphPassport(2, (0,), edges, "bad-passport")
        with self.assertRaises(GeometryError):
            GraphPassport(2, (0,), ((0, 1, -1),), "")


if __name__ == "__main__":
    unittest.main()
