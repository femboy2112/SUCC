"""Independent brute-force and adversarial monodromy/cover oracles."""
import unittest
from random import Random
from itertools import permutations

from observational_succ.relational_model_genetics import GeneticsError
from observational_succ.voltage_cover_synthesis import (
    VoltageGraph, PermutationGraph, compose_permutations, language_birth_demo,
)


class TestVoltageCover(unittest.TestCase):
    def test_parity_triangle_inconsistent_base_and_consistent_double_cover(self):
        g = VoltageGraph(("x", "y", "z"),
                         (("x", "y", 1), ("y", "z", 1), ("x", "z", 1)), 2)
        r = g.cover_report()
        self.assertFalse(r["global_base_potential"])
        self.assertEqual(g.brute_force_potentials(), 0)
        self.assertEqual(r["holonomy_image"], [0, 1])
        self.assertEqual(r["minimal_connected_trivializing_cover_degree"], 2)
        self.assertEqual(r["connected_lift_vertices"], 6)
        self.assertEqual(r["canonical_cover_components"], 1)
        self.assertTrue(r["scalar_on_cover_verified"])
        self.assertFalse(r["scalar_on_base_claimed_after_repair"])

    def test_unobstructed_graph_requires_no_new_sheets(self):
        g = VoltageGraph(("x", "y", "z"),
                         (("x", "y", 1), ("y", "z", 2), ("x", "z", 3)), 5)
        r = g.cover_report()
        self.assertTrue(r["global_base_potential"])
        self.assertEqual(g.brute_force_potentials(), 5)
        self.assertEqual(r["minimal_connected_trivializing_cover_degree"], 1)
        self.assertEqual(r["canonical_cover_components"], 5)
        self.assertEqual(r["connected_lift_vertices"], 3)

    def test_nontrivial_proper_subgroup_gives_three_sheet_cover(self):
        g = VoltageGraph(("root",), (("root", "root", 2),), 6)
        self.assertEqual(g.holonomy_subgroup(), (0, 2, 4))
        self.assertEqual(g.cover_report()["minimal_connected_trivializing_cover_degree"], 3)
        self.assertEqual(g.cover_report()["canonical_cover_components"], 2)
        self.assertFalse(g.global_potential_exists())

    def test_parallel_edge_inconsistency_not_erased(self):
        g = VoltageGraph(("x", "y"),
                         (("x", "y", 1), ("x", "y", 2)), 3)
        self.assertEqual(g.brute_force_potentials(), 0)
        self.assertEqual(len(g.holonomy_subgroup()), 3)

    def test_loop_zero_is_not_falsely_obstructive(self):
        g = VoltageGraph(("root",), (("root", "root", 0),), 4)
        self.assertTrue(g.global_potential_exists())
        self.assertEqual(g.brute_force_potentials(), 4)

    def test_negative_source_controls(self):
        with self.assertRaises(GeneticsError):
            VoltageGraph(("x",), (("x", "ghost", 1),), 2)
        with self.assertRaises(GeneticsError):
            VoltageGraph(("x",), (("x", "x", 1),), 1)
        with self.assertRaises(GeneticsError):
            VoltageGraph(("x", "y"), (("x", "y", 1),), 3, epoch=-1)
        with self.assertRaises(GeneticsError):
            VoltageGraph(("x", "y"), (), 2).tree_potentials()

    def test_200_random_graphs_against_independent_assignment_oracle(self):
        rng = Random(82023)
        for _ in range(200):
            m = rng.choice((2, 3, 4))
            n = rng.choice((2, 3, 4))
            v = tuple(str(i) for i in range(n))
            edges = [(v[i], v[i+1], rng.randrange(m)) for i in range(n-1)]
            for j in range(rng.randrange(1, 6)):
                edges.append((rng.choice(v), rng.choice(v), rng.randrange(m)))
            g = VoltageGraph(v, tuple(edges), m)
            brute = g.brute_force_potentials()
            self.assertEqual(brute > 0, g.global_potential_exists())
            self.assertEqual(brute, m if g.global_potential_exists() else 0)
            hol = set(g.holonomy_subgroup())
            self.assertEqual(hol, {k for k in range(m) if
                                  k % (m // len(hol)) == 0} if len(hol) == 1 else hol)
            c = g.cover_report()
            self.assertEqual(c["connected_lift_vertices"], len(v)*len(hol))
            self.assertTrue(c["scalar_on_cover_verified"])


class TestPermutationFixedPoint(unittest.TestCase):
    def test_nontrivial_loop_can_have_one_section(self):
        graph = PermutationGraph(("root",),
                                 (("root", "root", (1, 0, 2)),), 3)
        self.assertTrue(graph.nontrivial_holonomy())
        self.assertEqual(graph.root_fixed_points(), (2,))
        self.assertEqual(graph.independent_assignment_count(), 1)

    def test_nontrivial_loops_with_disjoint_fixed_sets_have_no_section(self):
        graph = PermutationGraph(("root",),
                                 (("root", "root", (1, 0, 2)),
                                  ("root", "root", (0, 2, 1))), 3)
        self.assertTrue(graph.nontrivial_holonomy())
        self.assertEqual(graph.root_fixed_points(), ())
        self.assertEqual(graph.independent_assignment_count(), 0)

    def test_nonabelian_order_is_not_interchangeable(self):
        p, q = (1, 0, 2), (0, 2, 1)
        self.assertEqual(compose_permutations(p, q), (2, 0, 1))
        self.assertEqual(compose_permutations(q, p), (1, 2, 0))
        self.assertNotEqual(compose_permutations(p, q), compose_permutations(q, p))

    def test_zero_edge_connections_admit_all_fiber_values(self):
        g = PermutationGraph(("x", "y"), (("x", "y", (0, 1, 2)),), 3)
        self.assertFalse(g.nontrivial_holonomy())
        self.assertEqual(g.root_fixed_points(), (0, 1, 2))
        self.assertEqual(g.independent_assignment_count(), 3)

    def test_180_random_nonabelian_action_graphs_independent_oracle(self):
        rng = Random(944)
        perms = tuple(permutations(range(3)))
        for _ in range(180):
            n = rng.choice((1, 2, 3, 4))
            v = tuple(str(i) for i in range(n))
            edges = [(v[i], v[i+1], rng.choice(perms)) for i in range(n-1)]
            for j in range(rng.randrange(4)):
                edges.append((rng.choice(v), rng.choice(v), rng.choice(perms)))
            g = PermutationGraph(v, tuple(edges), 3)
            self.assertEqual(len(g.root_fixed_points()),
                             g.independent_assignment_count())

    def test_invalid_permutations_rejected(self):
        with self.assertRaises(GeneticsError):
            PermutationGraph(("v",), (("v", "v", (0, 0, 1)),), 3)
        with self.assertRaises(GeneticsError):
            PermutationGraph(("v",), (("v", "v", (1, 0)),), 3)
        with self.assertRaises(GeneticsError):
            PermutationGraph(("v", "w"), (), 2).tree_transports()

    def test_generated_receipt_retains_nonflat_and_nonfree_cases(self):
        d = language_birth_demo()
        self.assertTrue(d["nonfree_nontrivial_holonomy"])
        self.assertEqual(d["nonfree_parallel_sections"], 1)
        self.assertEqual(d["independent_nonfree_section_count"], 1)
        self.assertEqual(d["incompatible_fixed_sets_section_count"], 0)
        self.assertFalse(d["physical_gauge_field_claimed"])


if __name__ == "__main__":
    unittest.main()
