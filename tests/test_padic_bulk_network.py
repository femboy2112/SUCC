"""Exact independent checks of lattice geometry and arithmetic boundary maps."""
import itertools
import unittest
from fractions import Fraction as F

from observational_succ.padic_bulk_network import (
    ArithmeticBoundaryChart, BTVertex, PadicGeometryError, boundary_visual_distance,
    bruhat_tits_ball, bt_sphere, crt_glue, prime_dilation_embedding,
    projective_vertex, residue_measurement_weights, tree_distance,
    projective_contact_depth, reconstruct_boundary_clusters,
)
from observational_succ.finite_fourier_carrier import CyclotomicElement, exact_dft, exact_idft


class BruhatTitsLatticeTests(unittest.TestCase):
    def test_primitive_orbits_and_lattice_index_independently(self):
        for p, r in ((2, 1), (2, 3), (3, 2), (5, 1)):
            q = p ** r
            sphere = bt_sphere(p, r)
            normalized = set()
            for x, y in itertools.product(range(q), repeat=2):
                if x % p or y % p:
                    v = projective_vertex(p, r, x, y)
                    normalized.add(v)
                    for unit in range(q):
                        if unit % p:
                            self.assertEqual(v, projective_vertex(p, r, unit*x, unit*y))
            self.assertEqual(normalized, set(sphere))
            self.assertEqual(len(sphere), (p + 1) * p ** (r - 1))
            for v in sphere:
                (a, c), (b, d) = v.lattice_basis
                self.assertEqual(abs(a*d-b*c), q)
                # Exactly q of q^2 residue vectors belong to the lattice.
                self.assertEqual(sum(v.contains_integral(x, y) for x, y in itertools.product(range(q), repeat=2)), q)

    def test_true_neighbors_have_index_p_and_degree(self):
        for p, radius in ((2, 4), (3, 3), (5, 2)):
            ball = bruhat_tits_ball(p, radius)
            self.assertEqual(len(ball.edges), len(ball.vertices)-1)
            for v in ball.vertices:
                self.assertEqual(len(ball.neighbors(v)), 1 if v.depth == radius else p+1)
            for parent, child in ball.edges:
                self.assertEqual(child.parent(), parent)
                self.assertIn(child, parent.children())
                for x, y in child.lattice_basis:
                    self.assertTrue(parent.contains_integral(x, y))
                self.assertEqual(child.depth, parent.depth+1)
            # Independent BFS reaches each vertex once; no decorative edges.
            seen = {ball.vertices[0]}
            stack = [ball.vertices[0]]
            while stack:
                node = stack.pop()
                for neighbor in ball.neighbors(node):
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            self.assertEqual(seen, set(ball.vertices))

    def test_radius_zero_has_no_false_regular_degree_claim(self):
        ball = bruhat_tits_ball(2, 0)
        self.assertEqual(len(ball.vertices), 1)
        self.assertEqual(ball.edges, ())
        self.assertEqual(ball.neighbors(ball.vertices[0]), ())

    def test_tree_distance_and_cylinder_ultrametric(self):
        for p, r in ((2, 3), (3, 2)):
            sphere = bt_sphere(p, r)
            for x, y, z in itertools.product(sphere, repeat=3):
                self.assertLessEqual(boundary_visual_distance(x, z), max(boundary_visual_distance(x, y), boundary_visual_distance(y, z)))
                self.assertLessEqual(tree_distance(x, z), tree_distance(x, y) + tree_distance(y, z))
            a = BTVertex(p, r, "affine", 0)
            b = BTVertex(p, r, "affine", p)
            self.assertEqual(boundary_visual_distance(a, b), F(1, p))
            self.assertEqual(tree_distance(a, b), 2*(r-1))

    def test_gl2_action_is_natural_and_isometric(self):
        matrices = (((1, 1), (0, 1)), ((0, 1), (1, 0)), ((1, 0), (1, 1)))
        for p in (2, 3, 5):
            sphere = bt_sphere(p, 2)
            for matrix in matrices:
                images = tuple(v.gl2_action(matrix) for v in sphere)
                self.assertEqual(set(images), set(sphere))
                for v in sphere:
                    self.assertEqual(v.gl2_action(matrix).parent(), v.parent().gl2_action(matrix))
                for a, b in itertools.product(sphere, repeat=2):
                    self.assertEqual(tree_distance(a, b), tree_distance(a.gl2_action(matrix), b.gl2_action(matrix)))

    def test_reconstruct_entire_ball_from_boundary_determinants(self):
        for p, radius in ((2, 4), (3, 3), (5, 2)):
            leaves = bt_sphere(p, radius)
            levels = reconstruct_boundary_clusters(p, radius)
            for depth, clusters in enumerate(levels):
                actual = {frozenset(j for j, v in enumerate(leaves) if v.reduce(depth) == parent)
                          for parent in bt_sphere(p, depth)}
                self.assertEqual(set(clusters), actual)
            for a, b in itertools.product(leaves, repeat=2):
                self.assertEqual(tree_distance(a, b), 2*(radius-projective_contact_depth(a, b)))

    def test_mutated_places_and_nonunit_actions_are_rejected(self):
        for p in (1, 4, 6, True):
            with self.assertRaises(PadicGeometryError):
                bruhat_tits_ball(p, 1)
        with self.assertRaises(PadicGeometryError):
            projective_vertex(3, 2, 3, 6)
        with self.assertRaises(PadicGeometryError):
            BTVertex(2, 1, "affine", 0).gl2_action(((2, 0), (0, 1)))


class ArithmeticBoundaryTests(unittest.TestCase):
    def test_chart_refinement_and_dual_frequency_lift(self):
        for p in (2, 3, 5):
            coarse = ArithmeticBoundaryChart(p, 1, "source-A", 7)
            fine = ArithmeticBoundaryChart(p, 3, "source-A", 7)
            for n in range(-9, 30):
                for k in range(p):
                    result = coarse.refinement_receipt(fine, n, k)
                    self.assertTrue(result["geometric_reduction"])
                    self.assertEqual(coarse.character(k).phase(n), F(k*n, p) % 1)
                    self.assertEqual(fine.character(k*p*p).phase(n), coarse.character(k).phase(n))
            with self.assertRaises(PadicGeometryError):
                coarse.refinement_receipt(ArithmeticBoundaryChart(p, 3, "source-B", 7), 1, 1)
            with self.assertRaises(PadicGeometryError):
                coarse.refinement_receipt(ArithmeticBoundaryChart(p, 3, "source-A", 8), 1, 1)

    def test_correct_phase_matches_existing_cyclotomic_fourier(self):
        chart = ArithmeticBoundaryChart(3, 1)
        root = chart.character(1).character_root(1)
        expected = CyclotomicElement.root(3, 1)
        reversed_orientation = CyclotomicElement.root(3, -1)
        self.assertEqual(root, expected)
        self.assertNotEqual(root, reversed_orientation)
        data = (0, 1, -1)
        spectrum = exact_dft(data)
        self.assertEqual(exact_idft(spectrum), tuple(CyclotomicElement.scalar(3, v) for v in data))
        self.assertEqual(spectrum[1], expected + reversed_orientation.scale(-1))

    def test_prime_embedding_isometry_and_typed_braid(self):
        for p, r in ((2, 1), (2, 4), (3, 2), (5, 1)):
            indices = prime_dilation_embedding(p, r)
            q = p**r
            self.assertEqual(len(set(indices)), q)
            for a in range(q):
                self.assertEqual(indices[(a+1) % q], (indices[a]+p) % (p*q))
                self.assertNotEqual(indices[(a+1) % q], (indices[a]+1) % (p*q))
            # The same-size residue map is noninjective: no unitary FUCC there.
            self.assertLess(len({(p*a) % q for a in range(q)}), q)

    def test_integer_orbit_reaches_only_affine_boundary_chart(self):
        chart = ArithmeticBoundaryChart(2, 3)
        reached = {chart.observe_integer(n) for n in range(16)}
        self.assertEqual(len(reached), 8)
        self.assertEqual(len(bt_sphere(2, 3)), 12)
        self.assertTrue(all(v.chart == "affine" for v in reached))

    def test_local_boundary_forgets_other_prime_range_projection(self):
        for p, q in ((2, 3), (3, 2), (5, 7)):
            for r in (1, 2, 4):
                chart = ArithmeticBoundaryChart(p, r)
                left, right = q, q + p**r
                self.assertEqual(chart.observe_integer(left), chart.observe_integer(right))
                self.assertEqual(left % q, 0)
                self.assertNotEqual(right % q, 0)

    def test_local_prime_compression_and_all_character_expectations(self):
        for p in (2, 3):
            q = p*p
            chart = ArithmeticBoundaryChart(p, 2)
            # Any residue function gives a bounded diagonal operator j_p(f).
            values = tuple(F(a*a-a+1) for a in range(q))
            for n in range(1, 4*q):
                self.assertEqual(values[(p*n) % q], values[chart.observe_integer(p*n).value])
                # rho_p f is defined on the next chart; its support is pZ_p.
                compressed = values[(n//p) % q] if n % p == 0 else F(0)
                fine_label = n % (p*q)
                source_value = values[fine_label//p] if fine_label % p == 0 else F(0)
                self.assertEqual(compressed, source_value)
            weights = {n: F(1, 9) for n in range(1, 10)}
            measured = residue_measurement_weights(weights, q)
            for k in range(q):
                source_sum = CyclotomicElement.scalar(q, 0)
                boundary_sum = CyclotomicElement.scalar(q, 0)
                for n, w in weights.items():
                    source_sum = source_sum + chart.character(k).character_root(n).scale(w)
                for a, w in enumerate(measured):
                    boundary_sum = boundary_sum + CyclotomicElement.root(q, k*a).scale(w)
                self.assertEqual(source_sum, boundary_sum)

    def test_coherent_residue_quotient_is_unbounded(self):
        # M orthogonal basis vectors in one residue class, each amplitude one:
        # input norm^2 M, coherent output norm^2 M^2. Ratio has no uniform bound.
        for q in (2, 3, 5):
            for count in (1, 2, 11, 37):
                source = tuple(1 + q*j for j in range(count))
                outputs = [0] * q
                for n in source:
                    outputs[n % q] += 1
                self.assertEqual(sum(v*v for v in outputs), count*count)
                self.assertEqual(F(sum(v*v for v in outputs), len(source)), count)

    def test_legal_residue_measurement_and_incompatible_global_charts(self):
        self.assertEqual(residue_measurement_weights({1:F(1,2), 3:F(1,2)}, 2), (0, 1))
        self.assertEqual(residue_measurement_weights({1:F(1,2), 2:F(1,2)}, 2), (F(1,2), F(1,2)))
        charts = (ArithmeticBoundaryChart(2, 3, "x", 4), ArithmeticBoundaryChart(3, 2, "x", 4), ArithmeticBoundaryChart(5, 1, "x", 4))
        for n in range(-23, 24):
            residues = tuple(n % c.modulus for c in charts)
            x, modulus = crt_glue(charts, residues)
            self.assertEqual(modulus, 360)
            self.assertEqual(x, n % 360)
            self.assertEqual(tuple(x % c.modulus for c in charts), residues)
            self.assertNotEqual(x, x+modulus)  # Archimedean ambiguity persists.
        with self.assertRaises(PadicGeometryError):
            crt_glue((charts[0], ArithmeticBoundaryChart(3, 1, "y", 4)), (1, 1))
        # Two individually legal nested reports may violate descent.
        coarse, fine = ArithmeticBoundaryChart(2, 1), ArithmeticBoundaryChart(2, 2)
        self.assertNotEqual(coarse.observe_integer(0), fine.observe_integer(1).reduce(1))
        with self.assertRaises(PadicGeometryError):
            crt_glue((coarse, fine), (0, 1))


if __name__ == "__main__":
    unittest.main()
