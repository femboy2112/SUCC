"""Independent Warshall/subset oracles and selected-source hostile controls."""
import unittest
from fractions import Fraction
from itertools import product

from observational_succ.ancestral_observer import (
    AncestralAudit, GhostPath, audit_ancestral_observer,
)
from observational_succ.future_safe_quotient import (
    Edge, ForgettingError, Machine, State, audit_representation,
)


def model(n, relation):
    # One action per destination realizes every finite relation in the existing
    # partial deterministic Machine; endpoint audit then forgets that action.
    names = tuple(str(i) for i in range(n))
    return Machine(
        tuple(State(s, "declared-source", "") for s in names), names,
        tuple(Edge(str(i), str(j), str(j), Fraction(0)) for i, j in relation),
    )


def closure(n, edges):
    matrix = [[i == j or (i, j) in edges for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] |= matrix[i][k] and matrix[k][j]
    return matrix


def partitions(n):
    for labels in product(range(n), repeat=n):
        if labels[0] == 0 and all(labels[i] <= 1 + max(labels[:i])
                                  for i in range(1, n)):
            yield labels


class TestAncestralObserver(unittest.TestCase):
    def test_all_relations_and_partitions_through_three_states(self):
        cases = 0
        for n in range(1, 4):
            pairs = tuple(product(range(n), repeat=2))
            for bits in product((False, True), repeat=len(pairs)):
                edges = {edge for edge, present in zip(pairs, bits) if present}
                m = model(n, sorted(edges))
                reach = closure(n, edges)
                for q in partitions(n):
                    labels = tuple(str(v) for v in q)
                    k = max(q) + 1
                    quotient = {(q[i], q[j]) for i, j in edges}
                    qreach = closure(k, quotient)
                    exact = True
                    for start in range(n):
                        result = audit_ancestral_observer(m, labels, str(start))
                        expected_states = {i for i in range(n) if reach[start][i]}
                        expected_reports = {q[i] for i in expected_states}
                        expected_abstract = {j for j in range(k) if qreach[q[start]][j]}
                        self.assertEqual(set(result.reachable_states),
                                         {str(i) for i in expected_states})
                        self.assertEqual(set(result.reachable_reports),
                                         {str(i) for i in expected_reports})
                        self.assertEqual(set(result.quotient_reports),
                                         {str(i) for i in expected_abstract})
                        self.assertEqual(result.endpoint_exact,
                                         expected_reports == expected_abstract)
                        saturated_reach_closed = all(q[i] not in expected_reports
                                                     or q[j] in expected_reports
                                                     for i, j in edges)
                        self.assertEqual(result.endpoint_exact, saturated_reach_closed)
                        exact &= result.endpoint_exact
                        if not result.endpoint_exact:
                            self.check_witness(m, labels, result)
                    # Independent power-set formulation of the theorem. No BFS.
                    saturations_closed = True
                    for flags in product((False, True), repeat=n):
                        if all(not flags[i] or flags[j] for i, j in edges):
                            reports = {q[i] for i in range(n) if flags[i]}
                            if any(q[i] in reports and q[j] not in reports
                                   for i, j in edges):
                                saturations_closed = False
                    self.assertEqual(exact, saturations_closed)
                    cases += 1
        self.assertEqual(cases, 2594)

    def check_witness(self, m, labels, result):
        w = result.obstruction
        self.assertIsNotNone(w)
        q = {s.name: labels[i] for i, s in enumerate(m.states)}
        reached = set(w.reachable_states)
        reached_reports = {q[s] for s in reached}
        self.assertIn(result.start, reached)
        self.assertTrue(all(e.start not in reached or e.target in reached
                            for e in m.edges))
        self.assertEqual(w.reports[0], q[result.start])
        self.assertIn(w.reports[-1], result.ghost_reports)
        self.assertNotIn(w.reports[-1], reached_reports)
        self.assertEqual(len(w.reports), len(w.source_edges) + 1)
        for i, edge in enumerate(w.source_edges):
            self.assertIn(edge, m.edges)
            self.assertEqual((q[edge.start], q[edge.target]), w.reports[i:i+2])
        self.assertIn(w.boundary, w.source_edges)
        self.assertIn(w.reachable_representative, reached)
        self.assertEqual(q[w.reachable_representative], q[w.boundary.start])
        self.assertIn(q[w.boundary.start], reached_reports)
        self.assertNotIn(q[w.boundary.target], reached_reports)

    def test_same_observation_different_selected_source(self):
        m = model(3, ((1, 2),))
        labels = ("A", "A", "B")
        bad = audit_ancestral_observer(m, labels, "0")
        good = audit_ancestral_observer(m, labels, "1")
        self.assertFalse(bad.endpoint_exact)
        self.assertTrue(good.endpoint_exact)
        self.assertEqual(bad.obstruction.reports, ("A", "B"))
        self.assertEqual(bad.reachable_states, ("0",))
        self.assertEqual(bad.obstruction.reachable_representative, "0")

    def test_unpointed_closure_commutation_does_not_authenticate_selected_root(self):
        edges = {(1, 2)}
        q = (0, 0, 1)
        reach = closure(3, edges)
        image_of_closure = {(q[i], q[j]) for i, j in product(range(3), repeat=2)
                            if reach[i][j]}
        abstract = closure(2, {(q[i], q[j]) for i, j in edges})
        closure_of_image = {(i, j) for i, j in product(range(2), repeat=2)
                            if abstract[i][j]}
        self.assertEqual(image_of_closure, closure_of_image)
        self.assertFalse(audit_ancestral_observer(model(3, edges),
                                                ("A", "A", "B"), "0").endpoint_exact)

    def test_independent_checker_rejects_forged_path_returning_to_real_endpoint(self):
        m = model(3, ((1, 2), (2, 1)))
        witness = GhostPath(("A", "B", "A"), m.edges, ("0",), m.edges[0], "0")
        forged = AncestralAudit("0", ("0",), ("A",), ("A", "B"), ("A",), witness)
        # Every abstract edge and the escaping saturation boundary are real.
        # The claimed endpoint A is nevertheless realized by the zero-step path.
        with self.assertRaises(AssertionError):
            self.check_witness(m, ("A", "A", "B"), forged)

    def test_endpoint_exactness_does_not_preserve_one_step_or_traces(self):
        m = model(3, ((0, 1), (1, 2)))
        labels = ("A", "A", "B")
        self.assertTrue(all(audit_ancestral_observer(m, labels, s.name).endpoint_exact
                            for s in m.states))
        stronger = audit_representation(m, labels)
        self.assertFalse(stronger["autonomous"])
        self.assertFalse(stronger["future_safe"])
        self.assertFalse(any(e.start == "0" and labels[int(e.target)] == "B"
                             for e in m.edges))

    def test_shortest_multi_step_ghost_and_unconnected_edge_representatives(self):
        m = model(5, ((0, 1), (2, 3), (3, 4)))
        labels = ("A", "B", "B", "C", "D")
        result = audit_ancestral_observer(m, labels, "0")
        self.assertEqual(result.ghost_reports, ("C", "D"))
        self.assertEqual(result.obstruction.reports, ("A", "B", "C"))
        left, right = result.obstruction.source_edges
        self.assertNotEqual(left.target, right.start)
        self.check_witness(m, labels, result)

    def test_zero_step_at_isolated_source_and_identity_observer(self):
        m = model(2, ())
        self.assertEqual(audit_ancestral_observer(m, ("A", "A"), "0").reachable_states,
                         ("0",))
        for edges in ((), ((0, 1),), ((0, 1), (1, 0))):
            m = model(2, edges)
            for s in m.states:
                self.assertTrue(audit_ancestral_observer(m, ("0", "1"), s.name).endpoint_exact)

    def test_endpoint_test_cannot_authenticate_sources_or_costs(self):
        m = Machine((State("x", "source-X", ""), State("y", "source-Y", "")),
                    ("step",), (Edge("x", "step", "x", Fraction(1)),
                                Edge("y", "step", "y", Fraction(2))))
        self.assertTrue(audit_ancestral_observer(m, ("same", "same"), "x").endpoint_exact)
        self.assertFalse(audit_representation(m, ("same", "same"))["future_safe"])

    def test_malformed_models_labels_and_selected_start_are_rejected(self):
        m = model(1, ())
        for labels in ([], ["x"], (), ("x", "y"), (1,)):
            with self.assertRaises(ForgettingError):
                audit_ancestral_observer(m, labels, "0")
        for start in ("missing", 0, False):
            with self.assertRaises(ForgettingError):
                audit_ancestral_observer(m, ("x",), start)
        with self.assertRaises(ForgettingError):
            audit_ancestral_observer(None, (), "0")


if __name__ == "__main__":
    unittest.main()
