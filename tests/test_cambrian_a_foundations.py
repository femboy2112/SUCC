"""Independent finite predicate/conditional-law oracles for cluster A."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.causal_nerode_succ import SourceChart, SourceTransportError
from observational_succ.eodcs_relational_choice import RelationalIntervention
from observational_succ.noncommuting_proof_transport import Instrument, FiniteCarrier
from observational_succ.cambrian_a_foundations import (
    and_source, bayesian_base_change, forward_evidence, multiobserver_information,
    pointwise_minimal_supports, powerset, relational_base_change,
    retained_claims, toolkit_pair_verdict, public_history_square,
)


def source(rows, old_reports, new_reports, exhaustive=True):
    before = SourceChart("cambrian-original-v1", 0, "declared-basis",
                         tuple(f"x{i}" for i in range(len(rows))), tuple(old_reports))
    after = SourceChart("cambrian-original-v1", 1, "declared-basis",
                        tuple(f"y{i}" for i in range(len(new_reports))), tuple(new_reports))
    return RelationalIntervention("declared-intervention", before, after,
                                  tuple(tuple(after.states[j] for j in row) for row in rows),
                                  exhaustive)


def factors(report, truth):
    # Pair predicate, deliberately unlike the production dictionary decoder.
    return all(report[i] != report[j] or truth[i] == truth[j]
               for i in range(len(report)) for j in range(len(report)))


def law_oracle(s, joint):
    """Normalize every nonnull U,B event and compare all target predicates."""
    ys = s.after.states
    for selected in powerset(s.before.image()):
        for b in s.after.image():
            event = [(i, j) for i, x in enumerate(s.before.states)
                     for j, y in enumerate(ys)
                     if s.before.report(x) in selected and s.after.report(y) == b]
            whole = [(i, j) for i in range(len(s.before.states))
                     for j, y in enumerate(ys) if s.after.report(y) == b]
            mass = sum((joint[i][j] for i, j in event), Q())
            base = sum((joint[i][j] for i, j in whole), Q())
            if mass == 0:
                continue
            for good in powerset(ys):
                left = sum((joint[i][j] for i, j in event if ys[j] in good), Q()) / mass
                right = sum((joint[i][j] for i, j in whole if ys[j] in good), Q()) / base
                if left != right:
                    return False
    return True


class RelationalLiftingTests(unittest.TestCase):
    def test_complete_three_state_relations_two_binary_report_tables(self):
        choices = tuple(row for row in powerset(range(3)) if row)
        cases = 0
        for rows in product(choices, repeat=3):
            for q in product(("a", "b"), repeat=3):
                for p in product(("c", "d"), repeat=3):
                    s = source(rows, q, p)
                    cert = relational_base_change(s)
                    # Source-lift iff ALL report predicates have exact preimage.
                    source_exact = True
                    for good in powerset(s.after.image()):
                        actual = {x for x in s.before.states
                                  if any(s.after.report(y) in good for y in s.possible_states(x))}
                        abstract_reports = {s.before.report(x) for x in actual}
                        completed = {x for x in s.before.states
                                     if s.before.report(x) in abstract_reports}
                        source_exact &= actual == completed
                        # Dual universal precondition tests, independently quantified.
                        universal = {x for x in s.before.states
                                     if all(s.after.report(y) in good for y in s.possible_states(x))}
                        abstract_all = {a for a in s.before.image()
                                        if all(s.after.report(y) in good
                                               for x in s.before.states if s.before.report(x) == a
                                               for y in s.possible_states(x))}
                        if cert.source_lift:
                            self.assertEqual(universal, {x for x in s.before.states
                                                        if s.before.report(x) in abstract_all})
                    target_exact = True
                    for selected in powerset(s.before.image()):
                        audit = forward_evidence(s, selected)
                        target_exact &= audit["equal"]
                    self.assertEqual(source_exact, cert.source_lift)
                    self.assertEqual(target_exact, cert.target_lift)
                    cases += 1
        self.assertEqual(cases, 21952)

    def test_directional_gates_are_independent(self):
        # Old source fully observed; post-report collapses y0,y1.
        target_bad = source(((0,), (1,)), ("a", "b"), ("c", "c"))
        a = relational_base_change(target_bad)
        self.assertTrue(a.source_lift)
        self.assertFalse(a.target_lift)
        self.assertEqual(a.target_defect, ("a", "y1"))
        self.assertEqual(forward_evidence(target_bad, ("a",))["actual_states"], ("y0",))
        # Old report collapses x0,x1; post-source is fully observed.
        source_bad = source(((0,), (1,)), ("a", "a"), ("c", "d"))
        b = relational_base_change(source_bad)
        self.assertFalse(b.source_lift)
        self.assertTrue(b.target_lift)
        both_good = source(((0,), (1,)), ("a", "a"), ("c", "c"))
        self.assertTrue(relational_base_change(both_good).both_exact)
        # Full relation saturation is sufficient but NOT necessary.
        self.assertEqual(sum(map(len, both_good.successors)), 2)

    def test_incomplete_source_and_untyped_evidence_rejected(self):
        s = source(((0,),), ("a",), ("b",), False)
        with self.assertRaises(SourceTransportError):
            relational_base_change(s)
        with self.assertRaises(SourceTransportError):
            forward_evidence(s, ("a",))
        with self.assertRaises(SourceTransportError):
            forward_evidence(source(((0,),), ("a",), ("b",)), ("forged",))


class ConditionalLawTests(unittest.TestCase):
    def test_support_lifts_do_not_identify_conditional_weights(self):
        s = source(((0, 1), (0, 1)), ("a", "b"), ("c", "c"))
        self.assertTrue(relational_base_change(s).both_exact)
        positive = ((Q(1, 4), Q(1, 4)), (Q(1, 4), Q(1, 4)))
        mutation = ((Q(1, 8), Q(3, 8)), (Q(3, 8), Q(1, 8)))
        self.assertTrue(bayesian_base_change(s, positive).exact_for_all_old_evidence_and_post_predicates)
        result = bayesian_base_change(s, mutation)
        self.assertFalse(result.exact_for_all_old_evidence_and_post_predicates)
        self.assertEqual(result.defect[-2:], (Q(1, 8), Q(1, 4)))
        self.assertFalse(law_oracle(s, mutation))

    def test_all_denominator_eight_joint_tables_against_normalized_oracle(self):
        cases = 0
        for a, b, c in product(range(9), repeat=3):
            d = 8 - a - b - c
            if d < 0 or a + b == 0 or c + d == 0:
                continue
            joint = ((Q(a, 8), Q(b, 8)), (Q(c, 8), Q(d, 8)))
            rows = tuple(tuple(j for j, w in enumerate(row) if w) for row in joint)
            for q in product(("a", "b"), repeat=2):
                for p in product(("c", "d"), repeat=2):
                    s = source(rows, q, p)
                    cert = bayesian_base_change(s, joint)
                    self.assertEqual(cert.exact_for_all_old_evidence_and_post_predicates,
                                     law_oracle(s, joint))
                    cases += 1
        self.assertEqual(cases, 2352)

    def test_null_reports_not_normalized_and_bad_weights_rejected(self):
        s = source(((0,), (0,)), ("a", "b"), ("c", "d"))
        joint = ((Q(1, 2), Q()), (Q(1, 2), Q()))
        cert = bayesian_base_change(s, joint)
        self.assertEqual(cert.null_post_reports, ("d",))
        self.assertTrue(cert.exact_for_all_old_evidence_and_post_predicates)
        for forged in (((0.5, 0.0), (0.5, 0.0)),
                       ((Q(1, 4), Q(1, 4)), (Q(1, 2), Q()))):
            with self.assertRaises(SourceTransportError):
                bayesian_base_change(s, forged)


class HistoryAndSupportTests(unittest.TestCase):
    def test_source_typed_history_square_and_epistemic_fibers(self):
        reset = Instrument("reset", (0, 1), (0, 0), (True, True))
        read = Instrument("read", (0, 1), (0, 1), (True, True))
        field = FiniteCarrier(2, (reset, read), "history-original-v1", "basis-v1")
        result = public_history_square(field, (("reset", "read"),))
        self.assertTrue(result["truncation_square_commutes"])
        rows = result["execution_rows"]
        self.assertEqual(tuple(row["audit_current_state"] for row in rows), (0, 0))
        self.assertNotEqual(rows[0]["long_report"], rows[1]["long_report"])
        self.assertEqual(tuple(roots for _, roots in result["public_source_fibers"]),
                         ((0,), (1,)))
        # If the destructive outcome was not exposed, root stays epistemically aliased.
        silent_reset = Instrument("reset", (0, 0), (0, 0), (True, True))
        silent = FiniteCarrier(2, (silent_reset, read), "history-original-v1", "basis-v1")
        dark = public_history_square(silent, (("reset", "read"),))
        self.assertEqual(dark["public_source_fibers"][0][1], (0, 1))

    def test_retention_iff_all_old_measurable_boolean_facts_survive(self):
        cases = 0
        for old, kept in product(product(range(2), repeat=4), repeat=2):
            truth_maps = tuple(product((0, 1), repeat=len(set(old))))
            labels = tuple(sorted(set(old)))
            actual = True
            for truth_map in truth_maps:
                lookup = dict(zip(labels, truth_map))
                truth = tuple(lookup[x] for x in old)
                actual &= factors(kept, truth)
            self.assertEqual(actual, retained_claims(old, kept))
            cases += 1
        self.assertEqual(cases, 256)

    def test_reset_loses_current_but_retained_history_keeps_original_fact(self):
        old = (0, 1)
        current_after_reset = (0, 0)
        kept_history = tuple(zip(old, current_after_reset))
        self.assertFalse(retained_claims(old, current_after_reset))
        self.assertTrue(retained_claims(old, kept_history))
        self.assertFalse(retained_claims(old, ("semantic-zero", "semantic-zero")))

    def test_AND_pointwise_support_sharp_for_positive_and_negative_results(self):
        for n in range(1, 7):
            field = and_source(n)
            positive = pointwise_minimal_supports(field, (1 << n) - 1, "AND")
            self.assertEqual(positive, (tuple(field.probes),))
            for state in field.states[:-1]:
                actual = pointwise_minimal_supports(field, state, "AND")
                self.assertEqual(set(actual), {(f"bit{i}",) for i in range(n)
                                               if not (state >> i) & 1})


class ToolkitAndManyObserverTests(unittest.TestCase):
    def test_pairwise_separators_do_not_supply_one_uniform_destructive_policy(self):
        # States encode (a,b). Each read exposes its bit and erases the other.
        a = Instrument("A", (0, 0, 1, 1), (0, 0, 2, 2), (True,) * 4)
        b = Instrument("B", (0, 1, 0, 1), (0, 1, 0, 1), (True,) * 4)
        field = FiniteCarrier(4, (a, b), "destructive-two-bit", "bits")
        target = tuple((s >> 1) ^ (s & 1) for s in range(4))
        for x in range(4):
            for y in range(x + 1, 4):
                if target[x] != target[y]:
                    self.assertIsNotNone(toolkit_pair_verdict(field, x, y)["separator"])
        # Every possible first action has a same-receipt, same-poststate,
        # opposite-target rival. Therefore no future adaptive policy can repair it.
        for action in field.actions:
            self.assertTrue(any(action.outputs[x] == action.outputs[y]
                                and action.transitions[x] == action.transitions[y]
                                and target[x] != target[y]
                                for x in range(4) for y in range(x + 1, 4)))

    def test_pair_darkness_and_extension_lamp(self):
        blind = Instrument("tick", (0, 0), (0, 1), (True, True))
        base = FiniteCarrier(2, (blind,), "same-source", "same-basis")
        result = toolkit_pair_verdict(base, 0, 1)
        self.assertTrue(result["toolkit_relative_dark"])
        self.assertIn((0, 1), result["closed_equivalence_witness"])
        lamp = Instrument("read", (0, 1), (0, 1), (True, True))
        extended = FiniteCarrier(2, (blind, lamp), "same-source", "same-basis")
        self.assertEqual(toolkit_pair_verdict(extended, 0, 1)["separator"], ("read",))

    def test_toolkit_delayed_path_and_forgotten_basis(self):
        # read alone aliases 0,1; advance then read distinguishes them.
        tick = Instrument("tick", (0, 0, 0), (0, 2, 2), (True,) * 3)
        read = Instrument("read", (0, 0, 1), (0, 1, 2), (True,) * 3)
        field = FiniteCarrier(3, (tick, read), "three-state", "basis-v1")
        self.assertEqual(toolkit_pair_verdict(field, 0, 1)["separator"], ("tick", "read"))
        # A lossy semantic map can still collapse an available physical separator.
        self.assertFalse(retained_claims((0, 1), (0, 0)))

    def test_three_incomplete_observers_fuse_to_complete_source(self):
        rows = tuple(tuple((s >> i) & 1 for s in range(8)) for i in range(3))
        result = multiobserver_information(rows)
        self.assertEqual(result["common_classes"], 1)
        self.assertEqual(result["fused_classes"], 8)
        self.assertTrue(result["all_source_states_reconstructed"])
        self.assertTrue(all(len(set(row)) == 2 for row in rows))

    def test_three_observer_common_factor_by_independent_boolean_algebra(self):
        cases = 0
        for rows in product(tuple(product(range(2), repeat=4)), repeat=3):
            result = multiobserver_information(rows)
            common = result["common_factor"]
            for truth in product(range(2), repeat=4):
                all_local = all(factors(row, truth) for row in rows)
                self.assertEqual(all_local, factors(common, truth))
            cases += 1
        self.assertEqual(cases, 4096)

    def test_pairwise_independence_not_joint_independence_or_source_realizability(self):
        states = (0, 3, 5, 6)  # even parity, uniform mass
        rows = tuple(tuple((s >> i) & 1 for s in states) for i in range(3))
        for i in range(3):
            for j in range(i + 1, 3):
                self.assertEqual(set(zip(rows[i], rows[j])), set(product(range(2), repeat=2)))
        self.assertNotIn((1, 1, 1), set(zip(*rows)))
        self.assertEqual(multiobserver_information(rows)["fused_classes"], 4)
        # General k-observer bad fusion instance: any k-1 all-one coordinates extend
        # to the even-parity source for odd k, but the all-one full record does not.
        for k in (3, 5, 7):
            original = [s for s in range(1 << k) if s.bit_count() % 2 == 0]
            self.assertNotIn((1 << k) - 1, original)
            for omitted in range(k):
                mask = ((1 << k) - 1) ^ (1 << omitted)
                self.assertIn(mask, original)


if __name__ == "__main__":
    unittest.main()
