"""Exact positive, negative and mutation controls for observer continuation."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q

from observational_succ.principia_intermedia import (
    ContinuationError, ObserverState, LayeredModel, continuation, verify_witness,
    seam_report, granular_crossing, lattice_zero, transport_section,
)


def state(name, source="source", target="comparison", history=()):
    return ObserverState(name, source, target, history)


def fork_model():
    return LayeredModel(
        ((state("a"),), (state("u"), state("v"), state("dead")), (state("b"),)),
        (frozenset({("a", "u"), ("a", "v"), ("a", "dead")}),
         frozenset({("u", "b"), ("v", "b")})),
        frozenset({"a"}), frozenset({"b"}),
    )


class FiniteContinuationTests(unittest.TestCase):
    def test_two_cones_remove_forward_only_dead_end(self):
        model = fork_model()
        result = continuation(model)
        self.assertEqual(result.forward[1], frozenset({"u", "v", "dead"}))
        self.assertEqual(result.backward[1], frozenset({"u", "v"}))
        self.assertEqual(result.viable[1], frozenset({"u", "v"}))
        self.assertEqual(result.witness, ("a", "u", "b"))
        self.assertIsNone(result.cut_layer)
        self.assertEqual(tuple(s.source for s in verify_witness(model, result.witness)),
                         ("source",) * 3)

    def test_nonempty_local_relations_do_not_imply_extension(self):
        model = LayeredModel(
            ((state("a"),), (state("u"), state("v")), (state("b"),)),
            (frozenset({("a", "u")}), frozenset({("v", "b")})),
            frozenset({"a"}), frozenset({"b"}),
        )
        result = continuation(model)
        self.assertFalse(result.feasible)
        self.assertIsNone(result.witness)
        self.assertEqual(result.forward[1], frozenset({"u"}))
        self.assertEqual(result.backward[1], frozenset({"v"}))
        self.assertTrue(all(not values for values in result.viable))
        self.assertEqual(result.cut_layer, 1)

    def test_pairwise_source_domains_have_no_global_witness(self):
        # {1,2}, {2,3}, {1,3} have pairwise overlaps but empty total intersection.
        layers = tuple(tuple(state(str(c), source=str(c)) for c in sources)
                       for sources in ((1, 2), (2, 3), (1, 3)))
        model = LayeredModel(layers, (frozenset({("2", "2")}), frozenset({("3", "3")})),
                             frozenset({"1", "2"}), frozenset({"1", "3"}))
        self.assertFalse(continuation(model).feasible)
        # A false bridge would silently swap the authenticated source.
        with self.assertRaises(ContinuationError):
            LayeredModel(layers, (frozenset({("2", "3")}), frozenset({("3", "3")})),
                         model.starts, model.ends)

    def test_source_and_normalized_target_mutations_rejected(self):
        for mutated in (state("b", source="other"), state("b", target="other")):
            with self.subTest(mutated=mutated):
                with self.assertRaises(ContinuationError):
                    LayeredModel(((state("a"),), (mutated,)), (frozenset({("a", "b")}),),
                                 frozenset({"a"}), frozenset({"b"}))

    def test_append_only_history_and_erasure_mutations(self):
        first = state("a", history=("seed=0", "carry=7"))
        good = state("b", history=("seed=0", "carry=7", "carry=-2"))
        model = LayeredModel(((first,), (good,)), (frozenset({("a", "b")}),),
                             frozenset({"a"}), frozenset({"b"}))
        self.assertTrue(continuation(model).feasible)
        for history in ((), ("seed=0",), ("seed=0", "carry=8")):
            with self.subTest(history=history), self.assertRaises(ContinuationError):
                replace(model, layers=((first,), (replace(good, history=history),)))

    def test_mutating_input_containers_cannot_rewrite_model(self):
        layers = [[state("a")], [state("b")]]
        edges = [{("a", "b")}]
        starts, ends = {"a"}, {"b"}
        model = LayeredModel(layers, edges, starts, ends)
        layers[1].clear()
        edges[0].clear()
        starts.clear()
        self.assertEqual(continuation(model).witness, ("a", "b"))

    def test_single_layer_and_empty_intermediate_layer(self):
        model = LayeredModel(((state("a"), state("b")),), (), frozenset({"a", "b"}), frozenset({"b"}))
        self.assertEqual(continuation(model).witness, ("b",))
        model = LayeredModel(((state("a"),), (), (state("b"),)), (frozenset(), frozenset()),
                             frozenset({"a"}), frozenset({"b"}))
        self.assertFalse(continuation(model).feasible)

    def test_structural_errors_rejected(self):
        with self.assertRaises(ContinuationError):
            LayeredModel((), (), frozenset(), frozenset())
        with self.assertRaises(ContinuationError):
            LayeredModel(((state("a"), state("a")),), (), frozenset(), frozenset())
        with self.assertRaises(ContinuationError):
            LayeredModel(((state("a"),),), (), frozenset({"missing"}), frozenset())
        with self.assertRaises(ContinuationError):
            replace(fork_model(), edges=(frozenset({("a", "unknown")}), frozenset()))
        with self.assertRaises(ContinuationError):
            state("a", history=["mutable"])

    def test_witness_verifier_rejects_teleports_and_forbidden_vertices(self):
        model = fork_model()
        for witness in (("a", "dead", "b"), ("a", "b"), ("unknown", "u", "b")):
            with self.subTest(witness=witness), self.assertRaises(ContinuationError):
                verify_witness(model, witness)
        with self.assertRaises(ContinuationError):
            verify_witness(model, ("a", "u", "b"), {(1, "u")})


class SeamTests(unittest.TestCase):
    def test_a_single_branch_null_is_avoidable(self):
        report = seam_report(fork_model(), {(1, "u")})
        self.assertTrue(report.feasible)
        self.assertFalse(report.unavoidable)
        self.assertEqual(report.avoiding_witness, ("a", "v", "b"))
        self.assertIsNone(report.avoidance_cut)

    def test_all_paths_seam_cut(self):
        report = seam_report(fork_model(), {(1, "u"), (1, "v")})
        self.assertTrue(report.unavoidable)
        self.assertIsNone(report.avoiding_witness)
        self.assertIsNotNone(report.avoidance_cut)

    def test_disconnected_model_does_not_earn_vacuous_crossing(self):
        model = replace(fork_model(), edges=(frozenset(), frozenset()))
        report = seam_report(model, {(1, "u"), (1, "v")})
        self.assertFalse(report.feasible)
        self.assertFalse(report.unavoidable)

    def test_endpoint_seam_and_empty_seam(self):
        self.assertTrue(seam_report(fork_model(), {(0, "a")}).unavoidable)
        self.assertFalse(seam_report(fork_model(), set()).unavoidable)
        with self.assertRaises(ContinuationError):
            seam_report(fork_model(), {(9, "a")})

    def test_multichannel_seam_does_not_follow_from_separate_roots(self):
        model = LayeredModel(tuple((state(str(i)),) for i in range(4)),
                             tuple(frozenset({(str(i), str(i + 1))}) for i in range(3)),
                             frozenset({"0"}), frozenset({"3"}))
        first_null, second_null = {(1, "1")}, {(2, "2")}
        self.assertTrue(seam_report(model, first_null).unavoidable)
        self.assertTrue(seam_report(model, second_null).unavoidable)
        self.assertFalse(seam_report(model, first_null & second_null).unavoidable)


class ExactScalarCrossingTests(unittest.TestCase):
    def test_sharp_half_jump_bound_and_no_fake_exact_zero(self):
        result = granular_crossing((Q(-1, 2), Q(1, 2)))
        self.assertEqual(result.edge_index, 0)
        self.assertIsNone(result.zero_index)
        self.assertEqual(abs(result.near_value), result.near_bound)
        self.assertEqual(result.near_bound, Q(1, 2))

    def test_reverse_orientation_and_unequal_bracket(self):
        result = granular_crossing((4, Q(1, 3), Q(-2, 3), -2))
        self.assertEqual(result.edge_index, 1)
        self.assertEqual(result.near_value, Q(1, 3))
        self.assertLessEqual(abs(result.near_value), result.near_bound)

    def test_exact_internal_null_and_singleton_null(self):
        result = granular_crossing((-2, -1, 0, 1))
        self.assertEqual(result.zero_index, 2)
        self.assertIsNone(result.edge_index)
        self.assertEqual(granular_crossing((0,)).near_bound, 0)

    def test_understated_jump_and_missing_bracket_rejected(self):
        with self.assertRaises(ContinuationError):
            granular_crossing((-1, 1), max_jump=1)
        with self.assertRaises(ContinuationError):
            granular_crossing((1, 2))
        with self.assertRaises(ContinuationError):
            granular_crossing((), max_jump=0)
        with self.assertRaises(ContinuationError):
            granular_crossing((-1, 1), max_jump=-2)

    def test_inexact_float_and_bool_inputs_rejected(self):
        for values in ((-0.5, 0.5), (-1, True)):
            with self.subTest(values=values), self.assertRaises(ContinuationError):
                granular_crossing(values)
        with self.assertRaises(ContinuationError):
            granular_crossing((-1, 1), max_jump=2.0)

    def test_lattice_null_and_sharp_threshold(self):
        self.assertEqual(lattice_zero((-2, -1, 0, 1), spacing=1), 2)
        self.assertEqual(lattice_zero((Q(-1, 3), 0, Q(1, 3)), spacing=Q(1, 3)), 1)
        with self.assertRaises(ContinuationError):
            lattice_zero((-1, 1), spacing=1)  # jump exactly 2h; no null

    def test_lattice_domain_mutations_rejected(self):
        with self.assertRaises(ContinuationError):
            lattice_zero((Q(-1, 2), 0, Q(1, 2)), spacing=1)
        with self.assertRaises(ContinuationError):
            lattice_zero((-1, 0, 1), spacing=0)
        with self.assertRaises(ContinuationError):
            lattice_zero((-1, 0, 1), spacing=1, max_jump=2)


class FiniteHolonomyTests(unittest.TestCase):
    def test_tree_transport_and_endpoint_anchor(self):
        result = transport_section(("a", "b", "c"),
                                   (("a", "b", (1, 0)), ("b", "c", (1, 0))),
                                   fiber_size=2, anchor_vertex="a", anchor_value=0,
                                   required={"c": 0})
        self.assertTrue(result.coherent)
        self.assertEqual(dict(result.assignment), {"a": 0, "b": 1, "c": 0})
        bad = transport_section(("a", "b"), (("a", "b", (1, 0)),),
                                fiber_size=2, anchor_vertex="a", anchor_value=0,
                                required={"b": 0})
        self.assertFalse(bad.coherent)

    def test_loop_holonomy_can_refute_locally_valid_transport(self):
        result = transport_section(("a", "b", "c"),
                                   (("a", "b", (0, 1)), ("b", "c", (0, 1)), ("c", "a", (1, 0))),
                                   fiber_size=2, anchor_vertex="a", anchor_value=0)
        self.assertFalse(result.coherent)
        self.assertIsNotNone(result.obstruction)

    def test_anchor_fixed_is_weaker_than_identity_holonomy(self):
        for anchor, expected in ((0, True), (1, False), (2, False)):
            with self.subTest(anchor=anchor):
                result = transport_section(("a",), (("a", "a", (0, 2, 1)),),
                                           fiber_size=3, anchor_vertex="a", anchor_value=anchor)
                self.assertEqual(result.coherent, expected)

    def test_nonbijective_and_disconnected_models_rejected(self):
        with self.assertRaises(ContinuationError):
            transport_section(("a", "b"), (("a", "b", (0, 0)),),
                              fiber_size=2, anchor_vertex="a", anchor_value=0)
        with self.assertRaises(ContinuationError):
            transport_section(("a", "b"), (), fiber_size=2, anchor_vertex="a", anchor_value=0)


if __name__ == "__main__":
    unittest.main()
