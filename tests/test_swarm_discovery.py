from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from random import Random
import unittest

from observational_succ.swarm_discovery import (TableSource, Probe, DiscoveryError,
    discover_quotient, verify_quotient, shortest_separators, action_algebra, factor_map,
    target_factors, invariant_under_label_change)
from observational_succ.swarm_lawful_history import (LawfulSource, Instrument, Event,
    HistoryError, replay_fiber, extend_fiber, restrict_fiber, certifies_original,
    quotient_source, legal_histories, synchronized_original_support)
from observational_succ.swarm_resource_geometry import (GeometryError, debt_stages,
    finite_completion_possible, dovetail_round_bound, anchored_graph_matrix,
    graph_evidence_update, solve_exact, clock_gluing)


class DiscoveryTests(unittest.TestCase):
    def test_complete_generated_systems_against_independent_moore_oracle(self):
        rng = Random(20261013)
        for n in range(1, 7):
            for trial in range(8):
                source = TableSource(f"generated-{n}-{trial}",
                    tuple((a, tuple(rng.randrange(n) for _ in range(n))) for a in ("a", "b")),
                    (tuple(rng.randrange(2) for _ in range(n)),))
                q = discover_quotient(source)
                self.assertTrue(verify_quotient(source, q))
                # Exhaust every word through the maximum shortest-pair path bound.
                for pair, probe in shortest_separators(source).items():
                    values = probe.values(source)
                    self.assertNotEqual(values[pair[0]], values[pair[1]])

    def test_shortest_separator_not_only_some_separator(self):
        source = TableSource("delayed", (("a", (1, 2, 3, 3)),), ((0, 0, 0, 1),))
        self.assertEqual(shortest_separators(source)[0, 1], Probe(("a", "a"), 0))
        for length in range(2):
            self.assertEqual(Probe(("a",)*length, 0).values(source)[0:2], (0, 0))

    def test_hidden_copies_target_does_not_factor(self):
        source = TableSource("copies", (("a", (1, 0, 3, 2)),), ((0, 1, 0, 1),))
        q = discover_quotient(source)
        self.assertEqual(q.labels, (0, 1, 0, 1))
        self.assertEqual(target_factors(q.labels, (0, 0, 1, 1)), (False, (0, 2)))
        self.assertTrue(target_factors(q.labels, (0, 1, 0, 1))[0])

    def test_opaque_relabeling_is_conjugacy(self):
        source = TableSource("copies", (("a", (1, 0, 3, 2)),), ((0, 1, 0, 1),))
        permutation = (2, 0, 3, 1)
        changed = invariant_under_label_change(source, permutation)
        original, new = discover_quotient(source), discover_quotient(changed)
        for i, j in product(range(4), repeat=2):
            self.assertEqual(original.labels[i] == original.labels[j],
                             new.labels[permutation[i]] == new.labels[permutation[j]])

    def test_changed_instrument_menu_invalidates_old_certificate(self):
        source = TableSource("copies", (("a", (1, 0, 3, 2)),), ((0, 1, 0, 1),))
        q = discover_quotient(source)
        changed = replace(source, actions=source.actions + (("new", (2, 1, 0, 3)),))
        with self.assertRaises(DiscoveryError):
            verify_quotient(changed, q)

    def test_grammar_mutation_must_have_real_factor_map(self):
        self.assertEqual(factor_map((0, 1, 2, 3), (0, 0, 1, 1)), (0, 0, 1, 1))
        with self.assertRaises(DiscoveryError):
            factor_map((0, 0, 1, 1), (0, 1, 0, 1))

    def test_unlicensed_word_and_forged_quotient_rejected(self):
        source = TableSource("two", (("a", (1, 0)),), ((0, 1),))
        q = discover_quotient(source)
        with self.assertRaises(DiscoveryError):
            Probe(("reset",), 0).values(source)
        with self.assertRaises(DiscoveryError):
            verify_quotient(source, replace(q, actions=(("a", (0, 1)),)))

    def test_budget_exhaustion_is_open_not_group_certificate(self):
        source = TableSource("cyclic", (("a", (1, 2, 0)),), ((0, 1, 2),))
        with self.assertRaisesRegex(DiscoveryError, "OPEN"):
            action_algebra(discover_quotient(source), cap=2)

    def test_noninvertible_action_not_called_group(self):
        source = TableSource("erase", (("a", (0, 0)),), ((0, 1),))
        self.assertFalse(action_algebra(discover_quotient(source))["group"])

    def test_predeclared_holdouts_and_null_different_family(self):
        from scripts.swarm_f_probe import discovery_receipt
        r = discovery_receipt()
        self.assertEqual([x["minimal_states"] for x in r["family_holdouts"]], [4, 25])
        self.assertEqual([x["generator_product_order"] for x in r["family_holdouts"]], [4, 5])
        self.assertFalse(r["out_of_family"]["action_profile"]["central_commutator"])


class HistoryTests(unittest.TestCase):
    def setUp(self):
        self.source = LawfulSource("once", (0, 1), (
            Instrument("read", (0, 1), (0, 1), (True, True)),
            Instrument("erase", (0, 0), ("done", "done"), (True, True))))

    def test_destructive_convergence_does_not_identify_original(self):
        f = replay_fiber(self.source, (Event("erase", "done"), Event("read", 0)))
        self.assertEqual(f.configurations, ((0, 0), (1, 0)))
        self.assertEqual(certifies_original(self.source, f, (0, 1)).status, "AMBIGUOUS")

    def test_original_support_survives_later_erasure(self):
        f = replay_fiber(self.source, (Event("read", 1), Event("erase", "done")))
        self.assertEqual(f.configurations, ((1, 0),))
        self.assertEqual(certifies_original(self.source, f, (0, 1)).value, 1)

    def test_empty_fiber_not_empirical_ex_falso(self):
        f = replay_fiber(self.source, (Event("read", 8),))
        self.assertFalse(f.originals)
        self.assertEqual(certifies_original(self.source, f, (0, 1)).status, "INCONSISTENT")

    def test_null_semantic_value_not_confused_with_unknown(self):
        f = replay_fiber(self.source, (Event("read", 1),))
        result = certifies_original(self.source, f, (None, None))
        self.assertEqual(result.status, "CERTIFIED_MODEL_RELATIVE")
        self.assertIsNone(result.value)

    def test_extension_and_restriction_composition(self):
        for f in legal_histories(self.source, 4):
            for j in range(len(f.history)+1):
                earlier = replay_fiber(self.source, f.history[:j])
                self.assertEqual(restrict_fiber(self.source, f, j),
                    tuple((o, dict(earlier.configurations)[o]) for o in sorted(f.originals)))
                for i in range(j+1):
                    oldest = dict(replay_fiber(self.source, f.history[:i]).configurations)
                    via_j = tuple((o, oldest[o]) for o, _ in restrict_fiber(self.source, f, j))
                    self.assertEqual(via_j, restrict_fiber(self.source, f, i))

    def test_forged_prefix_and_reset_rejected(self):
        f = replay_fiber(self.source, ())
        with self.assertRaises(HistoryError):
            extend_fiber(self.source, replace(f, configurations=((0, 0),)), Event("read", 0))
        with self.assertRaises(HistoryError):
            extend_fiber(self.source, f, Event("reset", "done"))

    def test_availability_is_part_of_the_quotient_type(self):
        source = LawfulSource("different-access", (0, 1), (
            Instrument("read", (0, 1), (0, 0), (True, False)),))
        with self.assertRaises(HistoryError):
            quotient_source(source, (0, 0))

    def test_shared_original_overlap_does_not_glue_actual_branches(self):
        from scripts.swarm_f_probe import destructive_source
        source = destructive_source()
        a = replay_fiber(source, (Event("a", 1),))
        b = replay_fiber(source, (Event("b", 1),))
        self.assertEqual(a.originals & b.originals, {3})
        self.assertFalse(replay_fiber(source, (Event("a", 1), Event("b", 1))).originals)
        self.assertFalse(replay_fiber(source, (Event("b", 1), Event("a", 1))).originals)

    def test_current_quotient_preserves_all_tested_history_supports(self):
        source = LawfulSource("duplicate-current", (0, 1, 2, 3), (
            Instrument("flip", (1, 0, 3, 2), (0, 1, 0, 1), (True,)*4),
            Instrument("erase", (0, 0, 2, 2), (0, 0, 0, 0), (True,)*4)))
        q = quotient_source(source, (0, 1, 0, 1))
        for f in legal_histories(source, 4):
            self.assertTrue(synchronized_original_support(source, q, (0, 1, 0, 1), f.history))

    def test_generated_safe_duplicate_quotients(self):
        rng = Random(4148)
        for n in range(1, 6):
            for trial in range(5):
                instruments = []
                for name in ("a", "b"):
                    after = tuple(rng.randrange(n) for _ in range(n))
                    outcome = tuple(rng.randrange(2) for _ in range(n))
                    enabled = tuple(bool(rng.randrange(2)) for _ in range(n))
                    instruments.append(Instrument(name, tuple(after[i % n]+(i//n)*n for i in range(2*n)),
                        outcome*2, enabled*2))
                source = LawfulSource(f"generated-{n}-{trial}", tuple(range(2*n)), tuple(instruments))
                labels = tuple(range(n))*2
                q = quotient_source(source, labels)
                for f in legal_histories(source, 3):
                    self.assertTrue(synchronized_original_support(source, q, labels, f.history))


class ResourceAndClockTests(unittest.TestCase):
    def test_sharp_resource_threshold_and_zero_limit_not_finite_completion(self):
        r = F(1, 2)
        self.assertEqual(debt_stages(2, 1, 1, r, 12), tuple(F(2, 2**n) for n in range(13)))
        self.assertFalse(finite_completion_possible(2, 1, 1, r))
        self.assertTrue(finite_completion_possible(F(3, 2), 1, 1, r))
        self.assertEqual(debt_stages(F(3, 2), 1, 1, r, 2)[2], 0)
        self.assertFalse(finite_completion_possible(3, 1, 1, r))

    def test_same_or_faster_service_growth_completes(self):
        for r in (2, 3):
            values = debt_stages(5, 2, 1, r, 20)
            self.assertTrue(finite_completion_possible(5, 2, 1, r))
            self.assertTrue(any(x <= 0 for x in values))

    def test_dovetail_bound_explicit_scheduler(self):
        for k, steps in product(range(1, 7), repeat=2):
            last, work = dovetail_round_bound(k, steps)
            self.assertEqual(last-k+1, steps)
            self.assertEqual(sum(range(1, last+1)), work)

    def test_anchored_graph_update_matches_independent_normal_equations(self):
        matrix = anchored_graph_matrix(3, ((0, 1, 1), (0, 2, 1)), (1, 1, 1))
        baseline = (F(1, 3), F(2, 3), F(4, 3))
        for node in range(3):
            update = graph_evidence_update(matrix, baseline, node, F(3, 2), 2)
            modified = [list(row) for row in matrix]
            modified[node][node] += 2
            rhs = [sum(a*x for a, x in zip(row, baseline)) for row in matrix]
            rhs[node] += 3
            self.assertEqual(update, solve_exact(modified, rhs))

    def test_integration_degree_does_not_determine_resistance(self):
        # Raising the leaf's anchoring reverses susceptibility despite same degree.
        edges = ((0, 1, 1), (0, 2, 1))
        weak = anchored_graph_matrix(3, edges, (1, 1, 1))
        strong = anchored_graph_matrix(3, edges, (1, 100, 1))
        leaf_weak = graph_evidence_update(weak, (0, 0, 0), 1, 1, 1)[1]
        leaf_strong = graph_evidence_update(strong, (0, 0, 0), 1, 1, 1)[1]
        self.assertGreater(leaf_weak, leaf_strong)

    def test_unanchored_component_not_positive_definite(self):
        with self.assertRaises(GeometryError):
            anchored_graph_matrix(2, ((0, 1, 1),), (0, 0))

    def test_cycle_holonomy_positive_negative_and_gauge(self):
        edges = ((0, 1, 1), (1, 2, 1), (2, 0, 1))
        self.assertEqual(clock_gluing(3, 3, edges)["phases"], (0, 1, 2))
        bad = clock_gluing(3, 3, ((0, 1, 1), (1, 2, 1), (2, 0, 2)))
        self.assertIsNone(bad["phases"])
        self.assertNotEqual(bad["residual"], 0)
        self.assertEqual(bad["cycle"][0], bad["cycle"][-1])

    def test_exhaustive_three_clock_triangle(self):
        for lags in product(range(4), repeat=3):
            edges = ((0, 1, lags[0]), (1, 2, lags[1]), (2, 0, lags[2]))
            result = clock_gluing(3, 4, edges)
            brute = [p for p in product(range(4), repeat=3) if
                     all((p[v]-p[u]-lag) % 4 == 0 for u, v, lag in edges)]
            self.assertEqual(result["phases"] is not None, bool(brute))

    def test_synchronized_clocks_do_not_certify_shared_semantics(self):
        phases = clock_gluing(2, 4, ((0, 1, 0),))["phases"]
        self.assertEqual(phases, (0, 0))
        semantic_targets = (False, True)
        self.assertNotEqual(*semantic_targets)


if __name__ == "__main__":
    unittest.main()
