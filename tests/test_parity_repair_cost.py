"""Exact hostile tests for minimum-cost F_2 parity-repair (Max-2-LIN/MaxCut).

All arithmetic is exact (int / Fraction); every optimum is checked against an
independent, non-gauge-fixed exhaustive oracle.  No floats, no randomness.
"""
import json
import subprocess
import sys
import unittest
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

from observational_succ.meta_choice_descent import solve_parity_descent
from observational_succ.parity_repair_cost import (
    RepairContractError,
    all_flip_targets,
    bipartite_max_cut,
    connected_graph_certificates,
    forest_repair_cost,
    frustration_index,
    greedy_sequential_repair,
    illegal_source_law_alteration,
    is_balanced,
    is_bipartite,
    is_forest,
    ising_couplings,
    ising_energy,
    ising_ground_state_bruteforce,
    ising_ground_state_energy,
    lawful_model_repair,
    max_cut,
    min_repair_cost,
    probe_reveal_obstruction,
    repair_cost,
    repair_graph,
    signed_signs,
    single_flip_local_certificate,
    spins_of_assignment,
    to_transport_graph,
    total_weight,
    unit_weights,
    verify_maxcut_identity,
)

ROOT = Path(__file__).resolve().parents[1]
CERT_PATH = ROOT / "research" / "2026-10-19" / "PARITY_REPAIR_CERTIFICATES.json"


def brute_min_cost(graph, t, w):
    """Independent oracle: full 2**n enumeration, NO gauge fixing."""
    best = None
    for bits in product((0, 1), repeat=graph.n_vertices):
        x = dict(zip(graph.vertices, bits))
        c = repair_cost(graph, t, w, x)
        best = c if best is None else min(best, c)
    return best


def brute_max_cut(graph):
    """Independent oracle: full 2**n enumeration of the cut, NO gauge fixing."""
    best = -1
    for bits in product((0, 1), repeat=graph.n_vertices):
        x = dict(zip(graph.vertices, bits))
        best = max(best, sum(1 for (u, v) in graph.edges if x[u] != x[v]))
    return best


TRIANGLE = repair_graph(("A", "B", "C"), [("A", "B"), ("B", "C"), ("C", "A")])
SQUARE = repair_graph(("a", "b", "c", "d"),
                      [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")])
K4_MINUS_EDGE = repair_graph(
    ("p", "q", "r", "s"),
    [("p", "q"), ("p", "r"), ("q", "r"), ("q", "s"), ("r", "s")])
PATH = repair_graph(("a", "b", "c"), [("a", "b"), ("b", "c")])


class TestParityRepairCost(unittest.TestCase):

    # 1 -----------------------------------------------------------------
    def test_all_flip_identity_triangle(self):
        identity = verify_maxcut_identity(TRIANGLE)
        self.assertEqual(identity.num_edges, 3)
        self.assertEqual(identity.max_cut, 2)
        self.assertEqual(identity.repair_cost_star, 1)
        self.assertTrue(identity.holds)
        self.assertEqual(identity.repair_cost_star,
                         identity.num_edges - identity.max_cut)

    # 2 -----------------------------------------------------------------
    def test_all_flip_identity_every_connected_graph_up_to_five(self):
        certs = connected_graph_certificates(5)
        self.assertEqual(len(certs), 31)
        self.assertEqual(Counter(c["n_vertices"] for c in certs),
                         Counter({1: 1, 2: 1, 3: 2, 4: 6, 5: 21}))
        for cert in certs:
            n = cert["n_vertices"]
            vertices = tuple(f"v{i}" for i in range(n))
            graph = repair_graph(
                vertices, [(f"v{u}", f"v{v}") for (u, v) in cert["edges"]],
                source_id="certificate-family")
            identity = verify_maxcut_identity(graph)
            self.assertEqual(identity.repair_cost_star, cert["repair_cost_star"])
            self.assertEqual(identity.max_cut, cert["max_cut"])
            # cross-check against the independent non-gauge-fixed oracle
            self.assertEqual(
                identity.repair_cost_star,
                brute_min_cost(graph, all_flip_targets(graph),
                               unit_weights(graph)))
            self.assertEqual(identity.max_cut, brute_max_cut(graph))
            self.assertEqual(identity.repair_cost_star,
                             identity.num_edges - identity.max_cut)

    # 3 -----------------------------------------------------------------
    def test_repair_cost_exact_single_assignment(self):
        # odd triangle, all targets 1, x all 0: every edge x_u(+)x_v=0 != 1.
        self.assertEqual(
            repair_cost(TRIANGLE, (1, 1, 1), (1, 1, 1),
                        {"A": 0, "B": 0, "C": 0}), 3)
        # x=(0,1,1): AB (0^1=1) and CA (1^0=1) satisfied, only BC (1^1=0!=1)
        # frustrated, so exactly the weight of edge BC is paid.
        self.assertEqual(
            repair_cost(TRIANGLE, (1, 1, 1), (2, 5, 7),
                        {"A": 0, "B": 1, "C": 1}), 5)

    # 4 -----------------------------------------------------------------
    def test_min_repair_matches_independent_bruteforce(self):
        for graph in (TRIANGLE, SQUARE, K4_MINUS_EDGE, PATH):
            for t in product((0, 1), repeat=graph.n_edges):
                w = unit_weights(graph)
                result = min_repair_cost(graph, t, w)
                self.assertEqual(result.cost, brute_min_cost(graph, t, w))
                # returned assignment really attains the reported cost
                self.assertEqual(
                    repair_cost(graph, t, w, result.as_dict()), result.cost)
            self.assertEqual(max_cut(graph).value, brute_max_cut(graph))

    # 5 -----------------------------------------------------------------
    def test_frustration_index_and_balance_match_188(self):
        for graph in (TRIANGLE, SQUARE, PATH):
            for t in product((0, 1), repeat=graph.n_edges):
                w = unit_weights(graph)
                self.assertEqual(frustration_index(graph, t, w),
                                 min_repair_cost(graph, t, w).cost)
                section = solve_parity_descent(
                    to_transport_graph(graph, t)).section_exists
                # balanced <=> C_*==0 <=> a global F_2 section exists (#188)
                self.assertEqual(is_balanced(graph, t, w), section)
                self.assertEqual(frustration_index(graph, t, w) == 0, section)
        self.assertEqual(signed_signs((0, 1, 1)), (1, -1, -1))

    # 6 -----------------------------------------------------------------
    def test_ising_pointwise_and_ground_state_mapping(self):
        t = (1, 0, 1)
        w = (Fraction(1, 2), Fraction(3, 2), 2)
        couplings = ising_couplings(t, w)
        W = total_weight(w)
        for bits in product((0, 1), repeat=TRIANGLE.n_vertices):
            x = dict(zip(TRIANGLE.vertices, bits))
            spins = spins_of_assignment(x)
            self.assertEqual(ising_energy(TRIANGLE, couplings, spins),
                             2 * repair_cost(TRIANGLE, t, w, x) - W)
        ground = ising_ground_state_bruteforce(TRIANGLE, couplings)
        self.assertEqual(ground.energy, ising_ground_state_energy(TRIANGLE, t, w))
        self.assertEqual(ground.energy,
                         2 * min_repair_cost(TRIANGLE, t, w).cost - W)

    # 7 -----------------------------------------------------------------
    def test_forest_repair_is_zero_and_matches_exhaustive(self):
        tree = repair_graph(("a", "b", "c", "d"),
                            [("a", "b"), ("b", "c"), ("b", "d")])
        self.assertTrue(is_forest(tree))
        for t in product((0, 1), repeat=tree.n_edges):
            w = unit_weights(tree)
            poly = forest_repair_cost(tree, t, w)
            self.assertEqual(poly.cost, 0)
            self.assertEqual(poly.cost, brute_min_cost(tree, t, w))
            self.assertEqual(repair_cost(tree, t, w, poly.as_dict()), 0)
        self.assertFalse(is_forest(TRIANGLE))
        with self.assertRaises(RepairContractError):
            forest_repair_cost(TRIANGLE, (1, 1, 1), (1, 1, 1))

    # 8 -----------------------------------------------------------------
    def test_bipartite_maxcut_poly_matches_exhaustive(self):
        self.assertTrue(is_bipartite(SQUARE))
        poly = bipartite_max_cut(SQUARE)
        self.assertEqual(poly.value, SQUARE.n_edges)
        self.assertEqual(poly.value, max_cut(SQUARE).value)
        self.assertEqual(poly.value, brute_max_cut(SQUARE))
        # odd cycle is not bipartite; the poly shortcut must refuse it
        self.assertFalse(is_bipartite(TRIANGLE))
        with self.assertRaises(RepairContractError):
            bipartite_max_cut(TRIANGLE)

    # 9 -----------------------------------------------------------------
    def test_greedy_sequential_strictly_suboptimal(self):
        t = all_flip_targets(K4_MINUS_EDGE)
        w = unit_weights(K4_MINUS_EDGE)
        greedy = greedy_sequential_repair(K4_MINUS_EDGE, t, w)
        exact = min_repair_cost(K4_MINUS_EDGE, t, w)
        self.assertEqual(greedy.cost, 2)
        self.assertEqual(exact.cost, 1)
        self.assertGreater(greedy.cost, exact.cost)
        # greedy's own assignment really does cost what it claims
        self.assertEqual(repair_cost(K4_MINUS_EDGE, t, w, greedy.as_dict()),
                         greedy.cost)

    # 10 ----------------------------------------------------------------
    def test_single_flip_local_optimum_certificate_c4(self):
        t = all_flip_targets(SQUARE)
        w = unit_weights(SQUARE)
        bad = {"a": 0, "b": 0, "c": 1, "d": 1}
        cert = single_flip_local_certificate(SQUARE, t, w, bad)
        self.assertEqual(cert.local_cost, 2)
        self.assertEqual(cert.global_cost, 0)
        self.assertTrue(cert.is_strict_local_optimum)
        self.assertTrue(cert.strictly_suboptimal)
        # every single-vertex flip stays at cost 2 (no local improvement)
        self.assertTrue(all(c == 2 for _, c in cert.neighbor_costs))
        # the true optimum (alternating 2-coloring) really achieves 0
        self.assertEqual(
            repair_cost(SQUARE, t, w, {"a": 0, "b": 1, "c": 0, "d": 1}), 0)

    # 11 ----------------------------------------------------------------
    def test_certificate_replay_bit_for_bit(self):
        expected = json.dumps(connected_graph_certificates(5),
                              indent=2, sort_keys=True) + "\n"
        self.assertTrue(CERT_PATH.exists())
        self.assertEqual(CERT_PATH.read_text(), expected)
        # a second independent regeneration is byte-identical (determinism)
        self.assertEqual(
            json.dumps(connected_graph_certificates(5), indent=2,
                       sort_keys=True) + "\n",
            expected)

    # 12 ----------------------------------------------------------------
    def test_probe_vs_repair_vs_illegal_source_law(self):
        odd = (1, 1, 1)
        w = unit_weights(TRIANGLE)

        # (a) observational probe: reveals the obstruction, repairs nothing.
        probe = probe_reveal_obstruction(TRIANGLE, odd)
        self.assertEqual(probe.repair_cost_paid, 0)
        self.assertFalse(probe.source_targets_altered)
        self.assertTrue(probe.reveals_obstruction)
        self.assertFalse(probe.makes_globally_representable)
        self.assertIsNotNone(probe.obstruction)

        # (b) lawful model repair: keep source laws, pay the residual C_* > 0.
        lawful = lawful_model_repair(TRIANGLE, odd, w)
        self.assertEqual(lawful.cost, 1)
        self.assertFalse(lawful.source_targets_altered)
        self.assertTrue(lawful.lawful_succ_repair)

        # (c) illegal source-law alteration: zero apparent cost, but it
        #     rewrote the source target vector -> NOT a lawful SUCC repair.
        illegal = illegal_source_law_alteration(TRIANGLE, odd, (0,))
        self.assertEqual(illegal.apparent_repair_cost, 0)
        self.assertTrue(illegal.source_targets_altered)
        self.assertFalse(illegal.lawful_succ_repair)
        self.assertNotEqual(illegal.altered_targets, illegal.original_targets)
        # the "cheap" cost is a lie: under the TRUE source law the cost is 1.
        self.assertEqual(min_repair_cost(TRIANGLE, odd, w).cost, 1)

    # 13 ----------------------------------------------------------------
    def test_firewall_flags_and_contract_guards(self):
        result = min_repair_cost(TRIANGLE, (1, 1, 1), (1, 1, 1))
        self.assertFalse(result.RH_proved)
        self.assertFalse(result.physical_source_authenticated)
        # malformed targets / weights / assignments are rejected
        with self.assertRaises(RepairContractError):
            repair_cost(TRIANGLE, (1, 1), (1, 1, 1), {"A": 0, "B": 0, "C": 0})
        with self.assertRaises(RepairContractError):
            repair_cost(TRIANGLE, (1, 1, 2), (1, 1, 1), {"A": 0, "B": 0, "C": 0})
        with self.assertRaises(RepairContractError):
            repair_cost(TRIANGLE, (1, 1, 1), (1, 1, -1), {"A": 0, "B": 0, "C": 0})
        with self.assertRaises(RepairContractError):  # bool weight is forbidden
            repair_cost(TRIANGLE, (1, 1, 1), (True, 1, 1),
                        {"A": 0, "B": 0, "C": 0})
        with self.assertRaises(RepairContractError):  # incomplete assignment
            repair_cost(TRIANGLE, (1, 1, 1), (1, 1, 1), {"A": 0, "B": 0})
        with self.assertRaises(RepairContractError):  # duplicate vertices
            repair_graph(("a", "a"), [])

    # 14 ----------------------------------------------------------------
    def test_fraction_weights_exact_and_gauge_invariance(self):
        w = (Fraction(1, 3), Fraction(1, 4), Fraction(5, 6))
        t = (1, 1, 1)
        result = min_repair_cost(TRIANGLE, t, w)
        self.assertEqual(result.cost, brute_min_cost(TRIANGLE, t, w))
        self.assertIsInstance(result.cost, Fraction)
        # cheapest single frustrated edge on the odd triangle is the 1/4 edge
        self.assertEqual(result.cost, Fraction(1, 4))
        # cost is invariant under the global complement x -> x (+) 1
        x = result.as_dict()
        flipped = {v: b ^ 1 for v, b in x.items()}
        self.assertEqual(repair_cost(TRIANGLE, t, w, x),
                         repair_cost(TRIANGLE, t, w, flipped))

    # 15 ----------------------------------------------------------------
    def test_probe_receipt_subprocess(self):
        run = subprocess.run(
            [sys.executable, "scripts/parity_repair_cost_probe.py"],
            cwd=ROOT, capture_output=True, text=True, check=True)
        report = json.loads(run.stdout)
        self.assertEqual(report["connected_graph_family_size"], 31)
        self.assertTrue(report["all_maxcut_identities_hold"])
        self.assertTrue(
            report["sample_all_flip_unit_identity"]["C_star_equals_E_minus_MaxCut"])
        self.assertTrue(report["greedy_strictly_suboptimal"])
        self.assertTrue(report["c4_is_strict_local_optimum"])
        self.assertTrue(report["c4_strictly_suboptimal"])
        self.assertTrue(report["ising_mapping_agrees"])
        self.assertFalse(report["illegal_alteration_is_lawful_succ_repair"])
        self.assertTrue(report["illegal_alteration_alters_source"])
        self.assertFalse(report["NP_hardness_is_noncomputability"])
        self.assertFalse(report["RH_proved"])
        self.assertFalse(report["LEM_proved"])


if __name__ == "__main__":
    unittest.main()
