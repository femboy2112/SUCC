"""Exact controls for graph/matrix semantics and existing SUCC source adapters."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
import unittest

from observational_succ.collective_spectral import Gaussian as C, SpectralError
from observational_succ.quantum_records import (
    INITIAL_PLUS, INITIAL_ZERO, measure_x, measure_z,
)
from observational_succ.source_lambda import LambdaError
from observational_succ.ym_graph_semantics import (
    Edge, GraphSemanticsError, LayeredGraph, Matrix, born_probabilities,
    channel_action, compile_record_instrument, compile_source_lambda,
    kraus_graph, linearize_function, pure_density, reversible_oracle,
    squared_norm, truncated_successor,
)


def basis(size, index):
    return tuple(C(int(k == index)) for k in range(size))


def raw_multiply(left, right):
    """Independent entry contraction using Python complex pairs of Fractions."""
    def mul(a, b):
        return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
    rows = []
    for i in range(len(left)):
        row = []
        for j in range(len(right[0])):
            terms = [mul(left[i][k], right[k][j]) for k in range(len(right))]
            row.append(C(sum(x[0] for x in terms), sum(x[1] for x in terms)))
        rows.append(tuple(row))
    return Matrix(tuple(rows))


def pairs(matrix):
    return tuple(tuple((x.real, x.imag) for x in row) for row in matrix.entries)


class FiniteGraphSemanticsTests(unittest.TestCase):
    def test_parallel_path_interference_matches_explicit_enumeration(self):
        graph = LayeredGraph((1, 2, 1), (
            Edge(0, 0, 0, C(0, 1)), Edge(0, 0, 1, Q(2, 3)),
            Edge(1, 0, 0, C(0, 1)), Edge(1, 1, 0, Q(3, 2)),
        ))
        self.assertEqual(graph.path_sum(0, 0), C())
        self.assertEqual(graph.matrix(), Matrix(((0,),)))
        # Replace only one path phase: the cancelled amplitude becomes two.
        mutant = LayeredGraph(graph.dimensions, graph.edges[:-2]+(
            Edge(1, 0, 0, C(0, -1)), Edge(1, 1, 0, Q(3, 2))))
        self.assertEqual(mutant.path_sum(0, 0), C(2))
        self.assertNotEqual(graph.matrix(), mutant.matrix())

    def test_general_matrix_representation_and_nontrivial_paths(self):
        first = Matrix(((C(1, 2), Q(2, 7)), (C(0, -1), 3), (Q(-1, 5), C(2, -1))))
        second = Matrix(((1, C(0, 1), Q(1, 3)), (C(2, 1), 0, -1)))
        a, b = LayeredGraph.from_matrix(first), LayeredGraph.from_matrix(second)
        graph = a.then(b)
        expected = raw_multiply(pairs(second), pairs(first))
        self.assertEqual(graph.matrix(), expected)
        for i, j in product(range(2), repeat=2):
            self.assertEqual(graph.path_sum(j, i), expected.entries[i][j])
        self.assertEqual(LayeredGraph.from_matrix(first).matrix(), first)

    def test_composition_tensor_dagger_and_identity_laws(self):
        a = LayeredGraph.from_matrix(Matrix(((C(1, 1), 2), (3, C(0, -1)))))
        b = LayeredGraph.from_matrix(Matrix(((Q(2, 5), 1), (C(0, 1), Q(-3, 7)))))
        c = LayeredGraph.from_matrix(Matrix(((1, 0), (1, 1))))
        ident = LayeredGraph((2,), ())
        self.assertTrue(ident.then(a).equivalent(a))
        self.assertTrue(a.then(ident).equivalent(a))
        self.assertTrue(a.then(b).then(c).equivalent(a.then(b.then(c))))
        self.assertEqual(a.then(b).dagger().matrix(), b.dagger().then(a.dagger()).matrix())
        self.assertEqual(a.dagger().dagger().matrix(), a.matrix())
        self.assertEqual(a.tensor(b).dagger().matrix(), a.dagger().tensor(b.dagger()).matrix())
        self.assertEqual(a.then(b).tensor(c.then(a)).matrix(),
                         a.tensor(c).then(b.tensor(a)).matrix())
        self.assertEqual(LayeredGraph((2, 3), ()).matrix(), Matrix.zero(3, 2))

    def test_presentation_quotient_preserves_amplitude_not_path_count(self):
        direct = LayeredGraph((1, 1), (Edge(0, 0, 0, 1),))
        split = LayeredGraph((1, 1), (Edge(0, 0, 0, Q(1, 3)), Edge(0, 0, 0, Q(2, 3))))
        duplicated = LayeredGraph((1, 1), (Edge(0, 0, 0, 1), Edge(0, 0, 0, 1)))
        self.assertTrue(direct.equivalent(split))
        self.assertNotEqual(direct.edges, split.edges)
        self.assertFalse(direct.equivalent(duplicated))
        self.assertEqual(duplicated.matrix().entries[0][0], C(2))

    def test_exact_unitary_interference_and_recorded_branch_mutation(self):
        a, b = Q(3, 5), Q(4, 5)
        mixer = Matrix(((a, b), (b, -a)))
        state = (a, b)
        self.assertTrue(mixer.is_unitary())
        self.assertEqual(born_probabilities(mixer.apply(state)), (Q(1), Q(0)))
        rho = pure_density(state)
        z_kraus = tuple(Matrix(k) for _, k in measure_z().outcomes)
        dephased = channel_action(z_kraus, rho)
        incoherent = mixer @ dephased @ mixer.dagger()
        self.assertEqual(tuple(incoherent.entries[i][i].real for i in range(2)),
                         (Q(337, 625), Q(288, 625)))
        # A global phase preserves density; a relative sign changes interference.
        self.assertEqual(pure_density((-a, -b)), rho)
        self.assertEqual(born_probabilities(mixer.apply((a, -b))),
                         (Q(49, 625), Q(576, 625)))

    def test_complex_unitary_and_restricted_coefficient_scope(self):
        gate = Matrix(((Q(3, 5), C(0, Q(4, 5))),
                       (C(0, Q(4, 5)), Q(3, 5))))
        self.assertTrue(gate.is_unitary())
        self.assertEqual(born_probabilities(gate.apply((1, 0))), (Q(9, 25), Q(16, 25)))
        # H tensor H has rational entries even though H itself needs sqrt(2).
        walsh4 = Matrix(tuple(tuple(Q((-1)**((i & j).bit_count()), 2)
                                    for j in range(4)) for i in range(4)))
        self.assertTrue(walsh4.is_unitary())
        for bad in (0.5, 1j, True):
            with self.assertRaises(SpectralError):
                Matrix(((bad,),))

    def test_nonunitary_projection_never_gets_silent_normalization(self):
        projection = Matrix(((1, 0), (0, 0)))
        self.assertFalse(projection.is_isometry())
        self.assertEqual(squared_norm(projection.apply((Q(3, 5), Q(4, 5)))), Q(9, 25))
        with self.assertRaises(GraphSemanticsError):
            born_probabilities(projection.apply((Q(3, 5), Q(4, 5))))
        with self.assertRaises(GraphSemanticsError):
            kraus_graph((projection,))
        with self.assertRaises(GraphSemanticsError):
            channel_action((projection,), pure_density((1, 0)))
        self.assertEqual(pure_density((1, 1)), Matrix(INITIAL_PLUS))

    def test_kernel_loss_is_not_a_reversible_representation_change(self):
        erase = linearize_function((0, 0), 1).matrix()
        self.assertEqual(erase.apply((1, -1)), (C(),))
        self.assertFalse(erase.is_isometry())
        self.assertEqual(squared_norm(erase.apply((Q(3, 5), Q(4, 5)))), Q(49, 25))
        with self.assertRaises(GraphSemanticsError):
            born_probabilities(erase.apply((Q(3, 5), Q(4, 5))))

    def test_actual_source_lambda_successor_and_prime_maps(self):
        for modulus in range(2, 10):
            successor = compile_source_lambda(modulus, "succ").matrix()
            self.assertTrue(successor.is_unitary())
            for prime in (2, 3, 5, 7):
                multiplication = compile_source_lambda(modulus, "prime_mul", prime).matrix()
                self.assertEqual(multiplication.is_unitary(), gcd(prime, modulus) == 1)
                power = Matrix.identity(modulus)
                for _ in range(prime):
                    power = successor @ power
                self.assertEqual(multiplication @ successor, power @ multiplication)
                for value in range(modulus):
                    self.assertEqual(multiplication.apply(basis(modulus, value)),
                                     basis(modulus, prime*value % modulus))
        with self.assertRaises(LambdaError):
            compile_source_lambda(7, "prime_mul", 6)
        with self.assertRaises(GraphSemanticsError):
            compile_source_lambda(7, "succ", 3)

    def test_reversible_oracle_retains_source_even_for_many_to_one_map(self):
        table = (0, 0, 1)
        oracle = reversible_oracle(table, 2).matrix()
        self.assertTrue(oracle.is_unitary())
        for x, y in product(range(3), range(2)):
            self.assertEqual(oracle.apply(basis(6, 2*x+y)),
                             basis(6, 2*x+(y+table[x]) % 2))
        self.assertNotEqual(oracle.apply(basis(6, 0)), oracle.apply(basis(6, 2)))
        self.assertEqual(linearize_function(table, 2).matrix().apply((1, -1, 0)), (C(), C()))

    def test_truncated_successor_has_explicit_boundary_defects(self):
        n = 5
        s = truncated_successor(n).matrix()
        self.assertFalse(s.is_isometry())
        self.assertEqual(s.apply(basis(n, n-1)), (C(),)*n)
        self.assertEqual(s.dagger() @ s, Matrix(tuple(tuple(
            int(i == j and i < n-1) for j in range(n)) for i in range(n))))
        self.assertEqual(s @ s.dagger(), Matrix(tuple(tuple(
            int(i == j and i > 0) for j in range(n)) for i in range(n))))
        self.assertTrue(compile_source_lambda(n, "succ").matrix().is_unitary())

    def test_existing_record_instruments_compile_with_same_probabilities(self):
        rational_pure = tuple(tuple(x.real for x in row)
                              for row in pure_density((Q(3, 5), Q(4, 5))).entries)
        for instrument, raw in product((measure_x(), measure_z()),
                                       (INITIAL_ZERO, INITIAL_PLUS, rational_pure)):
            graph = compile_record_instrument(instrument)
            v, rho = graph.matrix(), Matrix(raw)
            self.assertTrue(v.is_isometry())
            joint = v @ rho @ v.dagger()
            expected = instrument.probabilities(raw)
            weights = tuple(sum((joint.entries[2*o+i][2*o+i].real
                                 for i in range(2)), Q()) for o in range(2))
            self.assertEqual(dict(zip((name for name, _ in instrument.outcomes), weights)), expected)
            partial_trace = Matrix(tuple(tuple(sum((joint.entries[2*o+i][2*o+j]
                                                   for o in range(2)), C())
                                              for j in range(2)) for i in range(2)))
            kraus = tuple(Matrix(k) for _, k in instrument.outcomes)
            self.assertEqual(partial_trace, channel_action(kraus, rho))
        with self.assertRaises(GraphSemanticsError):
            compile_record_instrument("X")

    def test_boundaries_and_coefficients_are_validated(self):
        bad_graphs = (
            ((), ()), ((0,), ()), ((True, 2), ()),
            ((2, 2), (Edge(1, 0, 0),)),
            ((2, 2), (Edge(0, 2, 0),)),
            ((2,), (Edge(0, 0, 0),)),
        )
        for dimensions, edges in bad_graphs:
            with self.assertRaises(GraphSemanticsError):
                LayeredGraph(dimensions, edges)
        with self.assertRaises(GraphSemanticsError):
            Matrix(((1,), (1, 2)))
        with self.assertRaises(GraphSemanticsError):
            LayeredGraph((2,), ()).then(LayeredGraph((3,), ()))
        with self.assertRaises(GraphSemanticsError):
            linearize_function((0, True), 2)
        with self.assertRaises(GraphSemanticsError):
            pure_density((0, 0))


if __name__ == "__main__":
    unittest.main()
