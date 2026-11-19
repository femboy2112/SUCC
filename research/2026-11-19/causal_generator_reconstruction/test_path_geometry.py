"""Exact rational controls for the causal phase/Jacobian reconstruction claims."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from observational_succ.collective_spectral import Gaussian as C
from observational_succ.ym_graph_semantics import Matrix
from path_geometry import (CausalPhaseNetwork, PhaseEdge, jacobian_graph,
                           transported_jacobians)


def diamond(extra_loop=False):
    edges = (PhaseEdge(0, 1, Q(1, 7)), PhaseEdge(0, 2, Q(2, 9)),
             PhaseEdge(1, 3, Q(3, 11)), PhaseEdge(2, 3, Q(4, 13)))
    if extra_loop:
        edges += (PhaseEdge(3, 3, Q(5, 17)),)
    return CausalPhaseNetwork(4, 0, edges, (0, 1, 2))


class PathGeometryTests(unittest.TestCase):
    def test_forward_diamond_holonomy_needs_no_backward_execution(self):
        graph = diamond()
        left = graph.path_phase((0, 2))
        right = graph.path_phase((1, 3))
        self.assertEqual(left[0], right[0])
        self.assertEqual(graph.chord_holonomies()[3], (right[1] - left[1]) % 1)
        self.assertEqual(len(graph.chords), len(graph.edges) - graph.vertex_count + 1)
        self.assertEqual(graph.comparison_cost(), 4)
        with self.assertRaises(ValueError):
            graph.path_phase((2,), start=3)  # Cannot walk 1->3 backward.

    def test_every_gauge_has_the_same_tree_normal_form(self):
        graph = diamond(extra_loop=True)
        canonical = graph.from_holonomies(graph.chord_holonomies())
        for offsets in product((Q(0), Q(1, 3), Q(5, 7)), repeat=4):
            changed = graph.gauge(offsets)
            self.assertEqual(changed.chord_holonomies(), graph.chord_holonomies())
            self.assertEqual(changed.gauge(tuple(-t for t in changed.tree_phases())), canonical)

    def test_reconstruction_preserves_sampled_long_declared_walks(self):
        graph = diamond(extra_loop=True)
        normal = graph.from_holonomies(graph.chord_holonomies())
        tau = graph.tree_phases()
        for length in range(40):
            for prefix in ((0, 2), (1, 3)):
                path = prefix + (4,) * length
                target, raw = graph.path_phase(path)
                self.assertEqual(normal.path_phase(path), (target, (raw - tau[target]) % 1))

    def test_missing_chord_and_unreachable_tree_are_rejected(self):
        graph = diamond(extra_loop=True)
        with self.assertRaises(ValueError):
            graph.from_holonomies({3: graph.chord_holonomies()[3]})
        with self.assertRaises(ValueError):
            CausalPhaseNetwork(3, 0, (PhaseEdge(1, 2, 0), PhaseEdge(2, 1, 0)), (0, 1))
        with self.assertRaises(ValueError):
            CausalPhaseNetwork(2, 0, (PhaseEdge(1, 0, 0),), (0,))

    def test_unqueried_chord_mutation_changes_a_legal_future_response(self):
        graph = diamond(extra_loop=True)
        changed = CausalPhaseNetwork(4, 0, graph.edges[:-1] +
                                     (PhaseEdge(3, 3, Q(6, 17)),), graph.tree_edges)
        self.assertEqual(graph.path_phase((0, 2)), changed.path_phase((0, 2)))
        self.assertEqual(graph.chord_holonomies()[3], changed.chord_holonomies()[3])
        self.assertNotEqual(graph.path_phase((0, 2, 4)), changed.path_phase((0, 2, 4)))

    def test_noncommuting_jacobians_and_endpoint_frames(self):
        js = (Matrix(((2, 1), (0, 1))), Matrix(((1, 0), (3, 2))),
              Matrix(((1, -1), (2, 1))))
        frames = (Matrix(((1, 1), (0, 1))), Matrix(((2, 0), (0, 1))),
                  Matrix(((1, 0), (1, 1))), Matrix(((1, 2), (0, 1))))
        invs = (Matrix(((1, -1), (0, 1))), Matrix(((Q(1, 2), 0), (0, 1))),
                Matrix(((1, 0), (-1, 1))), Matrix(((1, -2), (0, 1))))
        ks = transported_jacobians(js, frames, invs)
        original, moved = jacobian_graph(js), jacobian_graph(ks)
        self.assertEqual(moved.matrix(), frames[-1] @ original.matrix() @ invs[0])
        self.assertNotEqual(moved.matrix(), original.matrix())
        for i, j in product(range(2), repeat=2):
            self.assertEqual(original.path_sum(j, i), original.matrix().entries[i][j])
            self.assertEqual(moved.path_sum(j, i), moved.matrix().entries[i][j])
        # Boundary vector/covector transport recovers the same scalar response.
        b, c = Matrix(((1,), (2,))), Matrix(((3, -1),))
        self.assertEqual(c @ original.matrix() @ b,
                         (c @ invs[-1]) @ moved.matrix() @ (frames[0] @ b))
        with self.assertRaises(ValueError):
            transported_jacobians(js, frames, invs[:-1] + (Matrix.identity(2),))

    def test_one_jet_does_not_determine_a_nonlinear_map(self):
        f, g = lambda x: x, lambda x: x + x*x
        df, dg = lambda x: 1, lambda x: 1 + 2*x
        self.assertEqual(f(0), g(0))
        self.assertEqual(df(0), dg(0))
        self.assertNotEqual(f(1), g(1))

    def test_intensities_do_not_determine_coherent_sum(self):
        plus_paths, minus_paths = (C(1), C(1)), (C(1), C(-1))
        intensity = lambda z: z.real*z.real + z.imag*z.imag
        self.assertEqual(tuple(map(intensity, plus_paths)), tuple(map(intensity, minus_paths)))
        self.assertEqual(sum(plus_paths, C()), C(2))
        self.assertEqual(sum(minus_paths, C()), C(0))

    def test_equal_closed_walk_traces_do_not_determine_anchored_response(self):
        lam = Q(1, 3)
        a = Matrix(((lam, 0), (0, lam)))
        b = Matrix(((lam, 1), (0, lam)))
        ap = bp = Matrix.identity(2)
        for n in range(12):
            self.assertEqual(ap.trace(), bp.trace())
            if n:
                self.assertEqual(ap.entries[0][1], C())
                self.assertEqual(bp.entries[0][1], C(n * lam**(n - 1)))
            ap, bp = a @ ap, b @ bp

    def test_hidden_mode_matches_every_sampled_boundary_response(self):
        # The proof is diagonal multiplication; this checks its exact finite implementation.
        a = Matrix(((Q(1, 2), 0), (0, Q(1, 3))))
        ap = Matrix.identity(2)
        for n in range(20):
            self.assertEqual(ap.entries[0][0], C(Q(1, 2)**n))
            self.assertEqual(ap.trace(), C(Q(1, 2)**n + Q(1, 3)**n))
            ap = a @ ap

    def test_fibonacci_trace_exponential_matches_reciprocal_determinant(self):
        a, power = Matrix(((1, 1), (1, 0))), Matrix.identity(2)
        traces = [Q(2)]
        for n in range(1, 17):
            power = a @ power
            self.assertEqual(power.trace().imag, 0)
            traces.append(power.trace().real)
        zeta = [Q(1)]
        for n in range(1, 17):
            zeta.append(sum(traces[k] * zeta[n-k] for k in range(1, n+1)) / n)
        fib = [1, 1]
        for _ in range(15):
            fib.append(fib[-1] + fib[-2])
        self.assertEqual(zeta, fib)

    def test_resolvent_conditioning_cost_is_necessary(self):
        for n in (4, 11, 37, 101):
            eps = Q(1, n)
            a, b = 1-eps, 1-2*eps
            self.assertEqual(abs(a-b), eps)
            self.assertEqual(abs(1/(1-a)-1/(1-b)), Q(n, 2))
            # The exact resolvent identity, not a numerical tolerance.
            self.assertEqual(1/(1-a)-1/(1-b), (a-b)/((1-a)*(1-b)))


if __name__ == "__main__":
    unittest.main()
