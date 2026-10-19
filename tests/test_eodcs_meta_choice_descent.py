"""Hostile finite tests for SUCC meta-choice/descent: exact model, no physics."""
import unittest
from dataclasses import replace
from itertools import combinations, product

from observational_succ.meta_choice_descent import (
    DescentContractError, FiniteTransportGraph, LoopObstruction,
    ParityEdge, brute_force_sections, local_edge_witnesses,
    solve_parity_descent, triangle, verify_loop, verify_section,
)


def graph(vertices, edges, source="original-s", basis="GF2"):
    return FiniteTransportGraph(source, basis, tuple(vertices), tuple(
        ParityEdge(u, v, p, source, basis) for u, v, p in edges
    ))


class TestMetaChoiceDescent(unittest.TestCase):
    def test_odd_triangle_local_choices_exist_but_no_global_section(self):
        carrier = triangle((1, 1, 1))
        self.assertTrue(all(local_edge_witnesses(e) for e in carrier.edges))
        self.assertEqual(len(brute_force_sections(carrier)), 0)
        result = solve_parity_descent(carrier)
        self.assertFalse(result.section_exists)
        self.assertEqual(result.number_of_sections, 0)
        self.assertTrue(verify_loop(carrier, result.obstruction))
        self.assertIsNone(result.rooted_potential)
        self.assertFalse(result.physical_source_authenticated)
        self.assertFalse(result.general_sheaf_descent_proved)
        self.assertFalse(result.RH_proved)

    def test_even_triangle_has_exactly_two_global_assignments(self):
        carrier = triangle((1, 1, 0))
        result = solve_parity_descent(carrier)
        self.assertTrue(result.section_exists)
        self.assertIsNone(result.obstruction)
        self.assertEqual(result.number_of_sections, 2)
        self.assertEqual(len(brute_force_sections(carrier)), 2)
        self.assertTrue(verify_section(carrier, dict(result.rooted_potential)))

    def test_all_eight_parity_triangles_match_independent_oracle(self):
        for triple in product((0, 1), repeat=3):
            with self.subTest(triple=triple):
                carrier = triangle(triple)
                actual = solve_parity_descent(carrier)
                oracle = brute_force_sections(carrier)
                expected = not bool(triple[0] ^ triple[1] ^ triple[2])
                self.assertEqual(actual.section_exists, expected)
                self.assertEqual(actual.number_of_sections, len(oracle))
                if expected:
                    self.assertTrue(verify_section(
                        carrier, dict(actual.rooted_potential)))
                else:
                    self.assertTrue(verify_loop(carrier, actual.obstruction))

    def test_all_729_simple_labeled_graphs_on_four_vertices(self):
        vertices = ("a", "b", "c", "d")
        pairs = tuple(combinations(vertices, 2))
        # 3^6=729 graphs: each undirected pair absent, parity 0 or parity 1.
        # Independent oracle enumerates all 2^4=16 vertex assignments.
        for specification in product((0, 1, 2), repeat=len(pairs)):
            edges = [
                (u, v, value - 1) for (u, v), value in zip(pairs, specification)
                if value
            ]
            carrier = graph(vertices, edges)
            actual = solve_parity_descent(carrier)
            oracle = brute_force_sections(carrier)
            self.assertEqual(actual.section_exists, bool(oracle))
            self.assertEqual(actual.number_of_sections, len(oracle))
            if actual.section_exists:
                self.assertEqual(len(oracle), 1 << actual.number_of_components)
                self.assertTrue(verify_section(
                    carrier, dict(actual.rooted_potential)))
            else:
                self.assertIsNone(actual.rooted_potential)
                self.assertTrue(verify_loop(carrier, actual.obstruction))

    def test_disconnected_and_empty_domains(self):
        four = graph(("a", "b", "c", "d"), [("a", "b", 1)])
        self.assertEqual(solve_parity_descent(four).number_of_sections, 8)
        self.assertEqual(len(brute_force_sections(four)), 8)
        empty = graph((), [])
        self.assertEqual(solve_parity_descent(empty).number_of_sections, 1)
        self.assertEqual(brute_force_sections(empty), ((),))

    def test_parallel_conflict_and_self_loop_are_detected(self):
        conflict = graph(("a", "b"), [("a", "b", 0), ("a", "b", 1)])
        result = solve_parity_descent(conflict)
        self.assertTrue(verify_loop(conflict, result.obstruction))
        self.assertEqual(result.number_of_sections, 0)
        self.assertTrue(all(local_edge_witnesses(e) for e in conflict.edges))
        loop = graph(("x",), [("x", "x", 1)])
        result = solve_parity_descent(loop)
        self.assertTrue(verify_loop(loop, result.obstruction))
        self.assertEqual(local_edge_witnesses(loop.edges[0]), ())

    def test_witness_mutations_are_rejected(self):
        carrier = triangle((1, 1, 1))
        witness = solve_parity_descent(carrier).obstruction
        self.assertTrue(verify_loop(carrier, witness))
        self.assertFalse(verify_loop(carrier, replace(witness, parity=0)))
        self.assertFalse(verify_loop(carrier, replace(
            witness, edge_indices=(99,) + witness.edge_indices[1:])))
        self.assertFalse(verify_loop(carrier, replace(
            witness, vertices=witness.vertices[:-1])))
        self.assertFalse(verify_loop(carrier, LoopObstruction((), (), 1)))

    def test_cross_source_and_basis_relabeling_is_forbidden(self):
        with self.assertRaises(DescentContractError):
            FiniteTransportGraph("s", "basis", ("a", "b"),
                (ParityEdge("a", "b", 1, "other-source", "basis"),))
        with self.assertRaises(DescentContractError):
            FiniteTransportGraph("s", "basis", ("a", "b"),
                (ParityEdge("a", "b", 1, "s", "shifted-basis"),))
        with self.assertRaises(DescentContractError):
            graph(("a", "b"), [("a", "not-there", 1)])
        with self.assertRaises(DescentContractError):
            graph(("a", "a"), [])
        with self.assertRaises(DescentContractError):
            graph(("a", "b"), [("a", "b", True)])
        with self.assertRaises(DescentContractError):
            graph(("a", "b"), [("a", "b", 2)])

    def test_spoofed_original_identity_is_not_a_physical_certificate(self):
        for source in ("authentic", "attacker-supplied-same-string"):
            result = solve_parity_descent(triangle((0, 0, 0), source_id=source))
            self.assertFalse(result.physical_source_authenticated)
            self.assertFalse(result.general_sheaf_descent_proved)

    def test_exact_probe_receipt_and_independent_count(self):
        # Exercise the actual command-line entrypoint, not a duplicated
        # in-test receipt object. Its published counts are fixed by the
        # independent subgraph/coboundary enumeration in the manuscript.
        import json
        import subprocess
        import sys
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        run = subprocess.run(
            [sys.executable, "scripts/meta_choice_descent_probe.py"],
            cwd=root, capture_output=True, text=True, check=True,
        )
        report = json.loads(run.stdout)
        self.assertEqual(report["all_four_vertex_simple_labeled_graphs"], 729)
        self.assertEqual(report["flat_graphs"], 393)
        self.assertEqual(report["obstructed_graphs"], 336)
        self.assertEqual(report["odd_triangle_global_sections"], 0)
        self.assertEqual(report["even_triangle_global_sections"], 2)
        self.assertTrue(report["odd_triangle_obstruction_verified"])
        self.assertTrue(report["independent_exhaustive_oracle_agrees"])
        self.assertFalse(report["source_provenance_authenticated"])
        self.assertFalse(report["full_sheaf_or_topos_semantics_formalized"])
        self.assertFalse(report["LEM_proved"])
        self.assertFalse(report["RH_proved"])

    def test_uniform_oracle_budget_restriction(self):
        big = graph(tuple("v" + str(i) for i in range(17)), [])
        self.assertEqual(solve_parity_descent(big).number_of_sections, 1 << 17)
        with self.assertRaises(DescentContractError):
            brute_force_sections(big)


if __name__ == "__main__":
    unittest.main()
