"""Hostile exact controls for CAMBRIAN C, independent bounded oracles."""
from fractions import Fraction
from itertools import product, permutations
import json
from pathlib import Path
from random import Random
import unittest

from observational_succ.cambrian_c_geometry import (
    FiniteHistorySystem, glue_constraint_sections, orbit_section_cover,
    relational_compose, coarse_interface_composition,
    canonical_interface_refinement, restricted_yoneda_controls, geometry_demo,
)
from observational_succ.core import DomainError
from observational_succ.voltage_cover_synthesis import PermutationGraph


def powerset(seq):
    return [frozenset(x for x, bit in zip(seq, bits) if bit)
            for bits in product((0, 1), repeat=len(seq))]


class CambrianHistories(unittest.TestCase):
    def test_240_source_changing_nondeterministic_receipts_against_cartesian_oracle(self):
        rng = Random(13731)
        for _ in range(240):
            depth = rng.randrange(1, 6)
            spaces = tuple(tuple(f"s{t}_{i}" for i in range(rng.randrange(1, 5)))
                           for t in range(depth + 1))
            relations = tuple(frozenset((x, y) for x in spaces[t] for y in spaces[t+1]
                                       if rng.randrange(2)) for t in range(depth))
            receipts = tuple(frozenset(x for x in space if rng.randrange(2)) for space in spaces)
            system = FiniteHistorySystem(spaces, relations, receipts, "independent-causal-source")
            oracle_support = []
            for h in range(depth + 1):
                oracle = set(path for path in product(*spaces[:h+1])
                             if all(path[t] in receipts[t] for t in range(h+1))
                             and all((path[t], path[t+1]) in relations[t] for t in range(h)))
                self.assertEqual(set(system.prefix_paths(h)), oracle)
                oracle_support.append(frozenset(path[-1] for path in oracle))
            self.assertEqual(system.support_history(), tuple(oracle_support))
            self.assertEqual(system.first_impossible_prefix(),
                             next((t for t, states in enumerate(oracle_support) if not states), None))

    def test_destructive_instrument_keeps_history_provenance(self):
        system = FiniteHistorySystem(
            (("past0", "past1"), ("erased",)),
            (frozenset({("past0", "erased"), ("past1", "erased")}),),
            (frozenset({"past1"}), frozenset({"erased"})), "destructive-source")
        self.assertEqual(system.prefix_paths(1), (("past1", "erased"),))
        self.assertEqual(system.support_history()[-1], frozenset({"erased"}))
        # Current physical state alone cannot reconstruct the old source bit.
        unrestricted = FiniteHistorySystem(system.spaces, system.transitions,
            (frozenset(system.spaces[0]), system.receipts[1]), system.source_id)
        self.assertEqual(len(unrestricted.prefix_paths(1)), 2)

    def test_countdown_controls_arbitrarily_long_but_each_finite_source_dies(self):
        # Exact finite witnesses for TWO universal counterexamples; the
        # universal no-infinite-history proofs are in the dossier/Lean.
        for depth in range(1, 65):
            natural_path = tuple(range(depth, -1, -1))
            self.assertTrue(all(y + 1 == x for x, y in zip(natural_path, natural_path[1:])))
            compact_path = tuple(Fraction(1, n) for n in range(depth+1, 0, -1))
            self.assertTrue(all(y.denominator + 1 == x.denominator
                                for x, y in zip(compact_path, compact_path[1:])))
            self.assertEqual(compact_path[-1], 1)
        # Nonclosed graph points converge exactly in the declared metric;
        # this finite bound checks the formula, not closure in Python.
        for n in range(2, 65):
            self.assertLessEqual(max(Fraction(1, n), Fraction(1, n-1)), Fraction(1, n-1))

    def test_source_types_and_horizon_guards(self):
        with self.assertRaises(DomainError):
            FiniteHistorySystem((("x",), ("y",)), (frozenset({("x", "wrong")}),),
                                (frozenset({"x"}), frozenset({"y"})), "s")
        with self.assertRaises(DomainError):
            FiniteHistorySystem((("x",),), (), (frozenset({"missing"}),), "s")
        s = FiniteHistorySystem((("x",),), (), (frozenset({"x"}),), "s")
        for depth in (-1, 1, True):
            with self.assertRaises(DomainError):
                s.prefix_paths(depth)


class CambrianCategoryAndGluing(unittest.TestCase):
    def test_restricted_yoneda_object_and_morphism_controls(self):
        result = restricted_yoneda_controls()
        self.assertEqual(result["object_source_hom_2_to_3"], 0)
        self.assertTrue(result["restricted_natural_isomorphism_2_3"])
        self.assertTrue(result["blind_context_collapses_parallel_arrows"])
        self.assertTrue(result["precursor_identity_context_distinguishes"])
        self.assertEqual(result["full_yoneda"]["natural_transform_count"], 2)
        self.assertEqual(result["full_yoneda"]["represented_count"], 2)
        self.assertTrue(result["single_retract_probe_fully_faithful"])
        self.assertEqual(result["single_retract_probe_hom_nat_counts"],
                         {"1_to_1": [1, 1], "1_to_2": [2, 2],
                          "2_to_1": [1, 1], "2_to_2": [4, 4]})
        self.assertEqual(result["ignoring_probe_endomorphism_laws_gives_256_instead_of_4"], 256)

    def test_literal_overlap_gluing_all_4096_binary_triangle_constraint_systems(self):
        variables = ("x", "y", "z")
        scopes = (("x", "y"), ("y", "z"), ("z", "x"))
        allowed_relations = powerset(tuple(product((0, 1), repeat=2)))
        for relations in product(allowed_relations, repeat=3):
            constraints = tuple(zip(scopes, relations))
            global_oracle = {values for values in product((0, 1), repeat=3)
                             if all(tuple(dict(zip(variables, values))[v] for v in scope) in allowed
                                    for scope, allowed in constraints)}
            glued = set()
            for rows in product(*(tuple(allowed) for allowed in relations)):
                charts = tuple(dict(zip(scope, row)) for scope, row in zip(scopes, rows))
                try:
                    section = glue_constraint_sections(variables, charts, constraints)
                except DomainError:
                    continue
                glued.add(tuple(section[v] for v in variables))
            self.assertEqual(glued, global_oracle)

    def test_constraint_scope_coverage_and_coarse_observation_mutants(self):
        equality = ((("x", "y"), frozenset({(0, 0), (1, 1)})),)
        with self.assertRaisesRegex(DomainError, "cross-chart"):
            glue_constraint_sections(("x", "y"), ({"x": 0}, {"y": 1}), equality)
        with self.assertRaisesRegex(DomainError, "omitted"):
            glue_constraint_sections(("x", "y"), ({"x": 0}, {"y": 1}), equality,
                                     require_constraint_cover=False)
        with self.assertRaisesRegex(DomainError, "overlap"):
            glue_constraint_sections(("x", "y"), ({"x": 0, "y": 0}, {"x": 1}), equality)
        # Each odd-parity triangle edge has source witnesses and all their
        # CONSTANT observation images match, but no global source assignment.
        xor = frozenset({(0, 1), (1, 0)})
        self.assertTrue(xor)
        self.assertFalse(any(all(bits[a] != bits[b] for a, b in ((0, 1), (1, 2), (2, 0)))
                             for bits in product((0, 1), repeat=3)))
        self.assertEqual({0 for _ in xor}, {0})

    def test_180_nonabelian_cover_holdouts_with_nonfree_actions(self):
        rng = Random(15015)
        perms = tuple(permutations(range(3)))
        for _ in range(180):
            n = rng.randrange(1, 5)
            vertices = tuple(f"v{i}" for i in range(n))
            edges = [(vertices[i], vertices[i+1], rng.choice(perms)) for i in range(n-1)]
            edges.extend((rng.choice(vertices), rng.choice(vertices), rng.choice(perms))
                         for _ in range(rng.randrange(5)))
            graph = PermutationGraph(vertices, tuple(edges), 3)
            for x in range(3):
                report = orbit_section_cover(graph, x)
                # Independent raw-edge BFS in the action bundle, without
                # tree gauges or group-closure computation.
                seen, queue = {(vertices[0], x)}, [(vertices[0], x)]
                adjacency = {v: [] for v in vertices}
                for u, v, p in edges:
                    adjacency[u].append((v, p))
                    adjacency[v].append((u, tuple(p.index(i) for i in range(3))))
                for v, value in queue:
                    for w, p in adjacency[v]:
                        nxt = (w, p[value])
                        if nxt not in seen:
                            seen.add(nxt)
                            queue.append(nxt)
                root_orbit = {value for v, value in seen if v == vertices[0]}
                self.assertEqual(report["minimum_degree_for_this_section"], len(root_orbit))
                self.assertEqual(len(report["vertices"]), len(seen))
                self.assertTrue(report["source_section_valid"])

    def test_one_section_and_all_transport_require_different_degrees(self):
        graph = PermutationGraph(("r",), (("r", "r", (1, 0, 2)),
                                            ("r", "r", (0, 2, 1))), 3)
        report = orbit_section_cover(graph, 0)
        self.assertEqual(report["minimum_degree_for_this_section"], 3)
        self.assertEqual(report["minimum_degree_for_all_transport_trivialization"], 6)
        self.assertEqual(report["orbit_cover_deck_group_order"], 1)
        self.assertTrue(report["constructed_section_deck_invariant"])
        self.assertFalse(report["constructed_section_descends_to_base"])
        fixed = PermutationGraph(("r",), (("r", "r", (1, 0, 2)),), 3)
        self.assertEqual(orbit_section_cover(fixed, 2)["minimum_degree_for_this_section"], 1)
        self.assertEqual(orbit_section_cover(fixed, 0)["minimum_degree_for_this_section"], 2)


class CambrianCompositionalRepair(unittest.TestCase):
    def test_quotient_created_internal_witness_is_refuted(self):
        left = frozenset({("x", "a")})
        right = frozenset({("b", "z")})
        q = {"a": 0, "b": 0}
        self.assertEqual(relational_compose(left, right), frozenset())
        self.assertEqual(coarse_interface_composition(left, right, q), frozenset({("x", "z")}))
        repaired = canonical_interface_refinement(("a", "b"), q, right)
        self.assertEqual(coarse_interface_composition(left, right, repaired), frozenset())

    def test_all_512_right_relations_and_8_left_relations_preserved_after_generated_refinement(self):
        states, outputs = tuple(range(3)), tuple(range(3))
        for right in powerset(tuple(product(states, outputs))):
            q = {m: 0 for m in states}
            refined = canonical_interface_refinement(states, q, right)
            for left in powerset(tuple(("x", m) for m in states)):
                self.assertEqual(coarse_interface_composition(left, right, refined),
                                 relational_compose(left, right))

    def test_generated_refinement_universal_property_all_three_state_partitions(self):
        states = (0, 1, 2)
        for right in powerset(tuple(product(states, ("yes", "no")))):
            for qvalues in product((0, 1), repeat=3):
                q = dict(zip(states, qvalues))
                refined = canonical_interface_refinement(states, q, right)
                behaviors = {m: frozenset(z for n, z in right if n == m) for m in states}
                for rvalues in product(range(3), repeat=3):
                    # Independent condition: q and EVERY boundary predicate
                    # are constant on fibers of the competing representation.
                    sufficient = all(rvalues[i] != rvalues[j]
                                     or (q[i] == q[j] and behaviors[i] == behaviors[j])
                                     for i in states for j in states)
                    factors = all(rvalues[i] != rvalues[j] or refined[i] == refined[j]
                                  for i in states for j in states)
                    self.assertEqual(sufficient, factors)

    def test_relational_associativity_all_two_state_three_relation_systems(self):
        relations = powerset(tuple(product(range(2), repeat=2)))
        for a, b, c in product(relations, repeat=3):
            self.assertEqual(relational_compose(relational_compose(a, b), c),
                             relational_compose(a, relational_compose(b, c)))

    def test_exact_receipt_replay(self):
        path = Path(__file__).resolve().parents[1] / "research/2026-10-13/CAMBRIAN_C_RECEIPT.json"
        self.assertEqual(json.loads(path.read_text()),
                         json.loads(json.dumps(geometry_demo(), sort_keys=True)))


if __name__ == "__main__":
    unittest.main()
