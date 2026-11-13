"""Cross-module tests: native SUCC graph, Wilson ray, Haar and record channel."""

from fractions import Fraction as Q
import unittest

from observational_succ.quantum_records import measure_z
from observational_succ.ym_graph_semantics import (
    LayeredGraph, Matrix, channel_action, pure_density, truncated_successor,
)
from observational_succ.ym_haar_bridge import (
    WeightedHaarPacket, haar_analyze, haar_coefficient_weights, haar_synthesize,
)
from observational_succ.ym_succ_character import (
    graph_return_moment, wilson_graph_expectation, wilson_graph_vector,
)


def jacobi(size):
    s = truncated_successor(size).matrix()
    return (s + s.dagger()).scaled(Q(1, 2))


def diagonal(entries):
    return Matrix(tuple(tuple(x if i == j else 0 for j in range(len(entries)))
                        for i, x in enumerate(entries)))


class TestQuantumBridgeIntegration(unittest.TestCase):
    def test_compiled_successor_graph_reproduces_haar_walks(self):
        for size in range(1, 7):
            step = LayeredGraph.from_matrix(jacobi(size))
            graph = LayeredGraph((size,), ())
            for power in range(10):
                expected = graph_return_moment(power, size - 1)
                self.assertEqual(graph.path_sum(0, 0).real, expected)
                self.assertEqual(graph.matrix().entries[0][0].real, expected)
                graph = graph.then(step)

    def test_wilson_expectation_survives_complete_haar_representation(self):
        size, degree, beta = 8, 4, Q(3, 2)
        v = wilson_graph_vector(beta, degree, size - 1)
        j = jacobi(size)
        observable = Matrix.identity(size) + (j @ j).scaled(-2)
        columns = [haar_analyze(tuple(int(i == k) for i in range(size)),
                                (1,) * size).coefficients for k in range(size)]
        transform = Matrix(tuple(tuple(columns[k][i] for k in range(size))
                                 for i in range(size)))
        inverse_columns = [haar_synthesize(WeightedHaarPacket((Q(1),) * size,
                            tuple(Q(i == k) for i in range(size))))
                           for k in range(size)]
        inverse = Matrix(tuple(tuple(inverse_columns[k][i] for k in range(size))
                               for i in range(size)))
        metric = diagonal(haar_coefficient_weights((1,) * size))
        self.assertEqual(inverse @ transform, Matrix.identity(size))
        self.assertEqual(transform.dagger() @ metric @ transform, Matrix.identity(size))
        # Rational Haar coordinates are unitary in their retained weighted metric.
        self.assertFalse(transform.is_unitary())
        changed_observable = transform @ observable @ inverse
        column = Matrix(tuple((x,) for x in v))
        changed_column = transform @ column
        norm = sum(x * x for x in v)
        result = (changed_column.dagger() @ metric @ changed_observable
                  @ changed_column).entries[0][0].real / norm
        expected = wilson_graph_expectation(beta, degree, (1, 0, -2), size - 1)
        self.assertEqual(result, expected)
        self.assertEqual((observable @ pure_density(v)).trace().real, expected)

    def test_existing_measurement_record_changes_the_wilson_state_if_discarded(self):
        ray = wilson_graph_vector(1, 1, 1)
        rho = pure_density(ray)
        trace_observable = jacobi(2)
        self.assertEqual((trace_observable @ rho).trace().real, Q(4, 17))
        instrument = measure_z()
        dephased = channel_action(tuple(Matrix(k) for _, k in instrument.outcomes), rho)
        self.assertEqual((trace_observable @ dephased).trace().real, 0)
        self.assertEqual(dephased.trace().real, 1)
        self.assertNotEqual(dephased, rho)


if __name__ == '__main__':
    unittest.main()
