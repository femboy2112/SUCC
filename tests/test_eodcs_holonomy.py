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
            # Independent BFS-based monodromy return phases at the root.
            returns = {level for vertex, level in g.lifted_reachable()
                       if vertex == v[0]}
            self.assertEqual(hol, returns)
            c = g.cover_report()
            self.assertEqual(c["connected_lift_vertices"], len(v)*len(hol))
            self.assertTrue(c["scalar_on_cover_verified"])
            self.assertEqual(c["minimal_cover_vertices"], len(v)*len(hol))
            self.assertEqual(c["minimal_cover_arcs"], len(edges)*len(hol))


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

    def test_nonabelian_S3_kernel_cover_six_sheets_from_three_fiber_values(self):
        p, q = (1, 0, 2), (0, 2, 1)
        g = PermutationGraph(("root",),
                             (("root", "root", p), ("root", "root", q)), 3)
        group = g.holonomy_group()
        self.assertEqual(len(group), 6)
        self.assertEqual(len(g.root_fixed_points()), 0)
        vertices, arcs = g.minimal_connected_trivializing_cover()
        self.assertEqual(len(vertices), 6)
        self.assertEqual(len(arcs), 12)
        # The lifted cover transports are simultaneously trivializable for
        # ALL root fiber values; the base has no parallel global section.
        for (u, h), (v, h2), perm in arcs:
            self.assertEqual(u, "root")
            self.assertEqual(v, "root")
            self.assertTrue(all(perm[h[i]] == h2[i] for i in range(3)))

    def test_nontrivial_holonomy_and_base_section_do_not_trivialize_cover(self):
        g = PermutationGraph(("root",),
                             (("root", "root", (1, 0, 2)),), 3)
        self.assertEqual(g.root_fixed_points(), (2,))
        self.assertEqual(len(g.holonomy_group()), 2)
        vertices, arcs = g.minimal_connected_trivializing_cover()
        self.assertEqual(len(vertices), 2)
        self.assertEqual(len(arcs), 2)

    def test_flat_connection_has_degree_one_even_with_many_fiber_values(self):
        g = PermutationGraph(("x", "y"),
                             (("x", "y", (1, 2, 0)),), 3)
        self.assertEqual(len(g.holonomy_group()), 1)
        vertices, arcs = g.minimal_connected_trivializing_cover()
        self.assertEqual(len(vertices), 2)
        self.assertEqual(len(arcs), 1)
        self.assertEqual(len(g.root_fixed_points()), 3)

    def test_120_seeded_nonabelian_minimal_covers_against_raw_path_BFS(self):
        rng = Random(20261013)
        perms = tuple(permutations(range(3)))
        for _ in range(120):
            n = rng.choice((1, 2, 3, 4))
            v = tuple(str(i) for i in range(n))
            edges = [(v[i], v[i+1], rng.choice(perms)) for i in range(n-1)]
            edges += [(rng.choice(v), rng.choice(v), rng.choice(perms))
                      for _ in range(rng.randrange(1, 5))]
            graph = PermutationGraph(v, tuple(edges), 3)
            # Independent oracle does not use holonomy_generators or the
            # library's permutation-composition helper: directly enumerate
            # path walks and their raw root-to-vertex permutations.
            adj = {x: [] for x in v}
            for u, w, p in edges:
                adj[u].append((w, p))
                inv = tuple(p.index(j) for j in range(3))
                adj[w].append((u, inv))
            start = (v[0], (0, 1, 2))
            reachable = {start}
            todo = [start]
            for at, path in todo:
                for w, p in adj[at]:
                    nxt = (w, tuple(p[path[i]] for i in range(3)))
                    if nxt not in reachable:
                        reachable.add(nxt)
                        todo.append(nxt)
            root_h = {p for at, p in reachable if at == v[0]}
            group = set(graph.holonomy_group())
            self.assertEqual(group, root_h)
            cover_vertices, cover_arcs = graph.minimal_connected_trivializing_cover()
            self.assertEqual(len(cover_vertices), n * len(root_h))
            self.assertEqual(len(cover_arcs), len(edges) * len(root_h))

    def test_cover_sections_descend_exactly_at_holonomy_fixed_points(self):
        # Base has one section, while a two-sheet cover has three;
        # only the fixed root value 2 yields a deck-invariant section.
        nonfree = PermutationGraph(("root",),
                                   (("root", "root", (1, 0, 2)),), 3)
        report = nonfree.section_descent_report()
        self.assertEqual(report["cover_parallel_sections"], 3)
        self.assertEqual(report["base_parallel_sections"], 1)
        self.assertEqual(report["root_elements_admitting_descent"], [2])
        self.assertFalse(report["all_cover_sections_descend"])

        # Noncommuting S3 holonomy forces a six-sheet kernel cover.
        # Each of three fiber-root values lifts to a cover section, but
        # none is deck-invariant and none descends to the original graph.
        s3 = PermutationGraph(("root",),
                              (("root", "root", (1, 0, 2)),
                               ("root", "root", (0, 2, 1))), 3)
        report = s3.section_descent_report()
        self.assertEqual(report["holonomy_group_order"], 6)
        self.assertEqual(report["cover_parallel_sections"], 3)
        self.assertEqual(report["base_parallel_sections"], 0)
        self.assertEqual(report["root_elements_admitting_descent"], [])

    def test_cover_section_mutant_invalid_root_rejected(self):
        graph = PermutationGraph(("v",), (("v", "v", (1, 0, 2)),), 3)
        for bad in (-1, 3, 1.0, "0"):
            with self.assertRaises(GeneticsError):
                graph.cover_parallel_section(bad)

    def test_random_nonabelian_descent_versus_assignment_oracle(self):
        rng = Random(879)
        perms = tuple(permutations(range(3)))
        for _ in range(60):
            n = rng.choice((1, 2, 3))
            v = tuple(str(i) for i in range(n))
            edges = [(v[i], v[i+1], rng.choice(perms))
                     for i in range(n-1)]
            edges += [(rng.choice(v), rng.choice(v), rng.choice(perms))
                      for _ in range(rng.randrange(3))]
            graph = PermutationGraph(v, tuple(edges), 3)
            report = graph.section_descent_report()
            # Brute force global base assignments never uses group closure.
            self.assertEqual(report["base_parallel_sections"],
                             graph.independent_assignment_count())
            self.assertEqual(report["cover_parallel_sections"], 3)

    def test_mutated_source_epoch_rejected_for_permutation_transport(self):
        with self.assertRaises(GeneticsError):
            PermutationGraph(("root",), (), 3, epoch=-1)
        with self.assertRaises(GeneticsError):
            PermutationGraph(("root",), (), 3, basis="")

    def test_generated_receipt_retains_nonflat_and_nonfree_cases(self):
        d = language_birth_demo()
        self.assertTrue(d["nonfree_nontrivial_holonomy"])
        self.assertEqual(d["nonfree_parallel_sections"], 1)
        self.assertEqual(d["independent_nonfree_section_count"], 1)
        self.assertEqual(d["incompatible_fixed_sets_section_count"], 0)
        self.assertEqual(d["nonfree_trivializing_cover_degree"], 2)
        self.assertEqual(d["nonabelian_S3_cover_degree"], 6)
        self.assertEqual(d["nonabelian_S3_cover_vertices"], 6)
        self.assertEqual(d["nonabelian_S3_cover_edges"], 12)
        self.assertEqual(d["nonabelian_S3_base_sections"], 0)
        self.assertEqual(d["nonfree_cover_descent"]["base_parallel_sections"], 1)
        self.assertEqual(d["nonabelian_cover_descent"]["base_parallel_sections"], 0)
        self.assertEqual(d["nonabelian_cover_descent"]["cover_parallel_sections"], 3)
        self.assertFalse(d["physical_gauge_field_claimed"])


if __name__ == "__main__":
    unittest.main()
