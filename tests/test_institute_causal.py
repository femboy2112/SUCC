"""Exact adversarial checks; finite enumeration is not universal proof."""
import dataclasses
import itertools
import unittest
from fractions import Fraction as Q

from observational_succ.institute_causal import (
    CausalError, HistoryCertificate, ReportStep, SourceSystem, Step,
    audit_public_transcript, audit_quotient, backward_exclusion_oracle,
    distinguishing_word, forward_history_oracle, refine_quotient,
    source_run, splice_counterexample, verify_history_certificate,
)


def machine(transitions, observations=None):
    return SourceSystem("two-state-source", "label-cost-state", ("0", "1"), ("a",),
                        {"0": "root", "1": "root"},
                        observations or {"0": "same", "1": "same"}, transitions)


def observed(model, state, word):
    """Independent explicit report replay, including failed action position."""
    answer = [model.observation[state]]
    for action in word:
        edge = model.transitions.get((state, action))
        if edge is None:
            return tuple(answer + [("unavailable", action)])
        state = edge.target
        answer.append((edge.outcome, edge.cost, model.observation[state]))
    return tuple(answer)


def brute_paths(model, initial, transcript):
    """Independent full Cartesian path enumeration, deliberately no DP."""
    valid = []
    for path in itertools.product(model.states, repeat=len(transcript) + 1):
        if path[0] not in initial:
            continue
        legal = True
        for i, report in enumerate(transcript):
            edge = model.transitions.get((path[i], report.action))
            if (edge is None or edge.target != path[i + 1] or edge.cost != report.cost or
                    edge.outcome != report.outcome or
                    model.observation[path[i + 1]] != report.observation):
                legal = False
                break
        if legal:
            valid.append(path)
    return valid


class InstituteCausalTests(unittest.TestCase):
    def test_source_splice_is_not_a_path(self):
        model, initial, transcript = splice_counterexample()
        # Each public edge exists, and the public overlap agrees.
        self.assertEqual(model.observation["left1"], model.observation["right1"])
        self.assertEqual(source_run(model, "left0", ("a",))[1], "left1")
        self.assertEqual(source_run(model, "right1", ("b",))[1], "right2")
        self.assertEqual(forward_history_oracle(model, initial, transcript).status, "NO_PATH_FOUND")
        cert = backward_exclusion_oracle(model, initial, transcript)
        self.assertEqual(cert.status, "SOURCE_HISTORY_IMPOSSIBLE")
        self.assertTrue(verify_history_certificate(model, initial, transcript, cert))
        fake = HistoryCertificate("SOURCE_HISTORY_EXISTS", model.source_id, model.basis,
                                  path=("left0", "right1", "right2"))
        self.assertFalse(verify_history_certificate(model, initial, transcript, fake))
        q = dict(model.observation)
        self.assertEqual(audit_quotient(model, q).reason, "AVAILABILITY_LOSS")

    def test_supported_does_not_mean_publicly_available(self):
        model = machine({("0", "a"): Step("0", "ok", 1)})
        initial = frozenset(model.states)
        transcript = (ReportStep("a", "ok", 1, "same"),)
        cert = forward_history_oracle(model, initial, transcript)
        self.assertTrue(verify_history_certificate(model, initial, transcript, cert))
        audit = audit_public_transcript(model, initial, transcript)
        self.assertEqual(audit.status, "PUBLIC_ACTION_UNAVAILABLE")
        self.assertEqual(audit.witness_path, ("1",))
        self.assertEqual(audit.at_step, 0)

    def test_future_report_cannot_postselect_an_unsafe_choice(self):
        model = machine({("0", "a"): Step("0", "reveals-zero", 1)})
        audit = audit_public_transcript(model, frozenset(model.states),
                                        (ReportStep("a", "reveals-zero", 1, "same"),))
        self.assertEqual(audit.status, "PUBLIC_ACTION_UNAVAILABLE")

    def test_safe_report_branch_keeps_private_source(self):
        model = SourceSystem("hidden-original", "private-root-public-report", ("0", "1"), ("a",),
                             {"0": "L", "1": "R"}, {"0": "same", "1": "same"},
                             {("0", "a"): Step("0", "ok", 1),
                              ("1", "a"): Step("1", "ok", 1)})
        q = {"0": "merged", "1": "merged"}
        self.assertTrue(audit_quotient(model, q).lawful)
        transcript = (ReportStep("a", "ok", 1, "same"),) * 3
        self.assertEqual(audit_public_transcript(model, frozenset(model.states), transcript).status,
                         "SAFE_POSSIBLE_TRANSCRIPT")
        for s in model.states:
            cert = forward_history_oracle(model, frozenset({s}), transcript)
            self.assertTrue(verify_history_certificate(model, frozenset({s}), transcript, cert))
            self.assertEqual(cert.path, (s,) * 4)

    def test_cost_and_report_mutations_block_quotient(self):
        model = machine({("0", "a"): Step("0", "ok", 1),
                         ("1", "a"): Step("1", "ok", Q(3, 2))})
        self.assertEqual(audit_quotient(model, {"0": "q", "1": "q"}).reason,
                         "LABEL_OR_COST_LOSS")
        changed = dataclasses.replace(model, observation={"0": "x", "1": "y"})
        self.assertEqual(audit_quotient(changed, {"0": "q", "1": "q"}).reason,
                         "CURRENT_REPORT_LOSS")

    def test_empty_transcript_and_empty_source(self):
        model = machine({})
        yes = forward_history_oracle(model, frozenset({"0"}), ())
        self.assertTrue(verify_history_certificate(model, frozenset({"0"}), (), yes))
        no = backward_exclusion_oracle(model, frozenset(), ())
        self.assertTrue(verify_history_certificate(model, frozenset(), (), no))
        self.assertEqual(audit_public_transcript(model, frozenset(), ()).status, "IMPOSSIBLE_PREFIX")

    def test_bad_credentials_and_corrupt_cuts_are_rejected(self):
        model, initial, transcript = splice_counterexample()
        cert = backward_exclusion_oracle(model, initial, transcript)
        for bad in (dataclasses.replace(cert, source_id="other-source"),
                    dataclasses.replace(cert, basis="other-basis"),
                    dataclasses.replace(cert, excluded=(frozenset(model.states),) * 3),
                    dataclasses.replace(cert, excluded=(frozenset(),) * 3),
                    dataclasses.replace(cert, excluded=(initial, frozenset(), frozenset())),
                    dataclasses.replace(cert, path=("left0",)),
                    dataclasses.replace(cert, excluded=(initial, frozenset({"absent"}), frozenset()))):
            self.assertFalse(verify_history_certificate(model, initial, transcript, bad))

    def test_invalid_source_and_inexact_cost_rejected(self):
        for cost in (1.0, True, -1):
            with self.assertRaises(CausalError):
                Step("0", "ok", cost)
        with self.assertRaises(CausalError):
            SourceSystem("s", "b", ("0", "1"), ("a",), {"0": "L", "1": "R"},
                         {"0": "x", "1": "x"}, {("0", "a"): Step("1", "ok", 1)})
        with self.assertRaises(CausalError):
            audit_quotient(machine({}), {"0": "q"})
        with self.assertRaises(CausalError):
            audit_public_transcript(machine({}, {"0": "x", "1": "y"}),
                                    frozenset({"0", "1"}), ())
        with self.assertRaises(CausalError):
            source_run(machine({}), "0", ("not-available-grammar",))

    def test_declared_tables_are_immutable_copies(self):
        transitions = {("0", "a"): Step("0", "ok", 1)}
        model = machine(transitions)
        transitions.clear()
        self.assertEqual(len(model.transitions), 1)
        with self.assertRaises(TypeError):
            model.transitions["0", "a"] = Step("1", "ok", 1)

    def test_finite_primal_dual_against_independent_full_path_oracle(self):
        options = [None] + [Step(target, outcome, 1)
                            for target in ("0", "1") for outcome in ("yes", "no")]
        checked = 0
        for edges in itertools.product(options, repeat=2):
            model = machine({(s, "a"): e for s, e in zip(("0", "1"), edges) if e is not None})
            for initial in (frozenset(), frozenset({"0"}), frozenset({"1"}), frozenset({"0", "1"})):
                for outcomes in itertools.product(("yes", "no"), repeat=3):
                    transcript = tuple(ReportStep("a", o, 1, "same") for o in outcomes)
                    brute = brute_paths(model, initial, transcript)
                    primal = forward_history_oracle(model, initial, transcript)
                    dual = backward_exclusion_oracle(model, initial, transcript)
                    self.assertEqual(primal.status == "SOURCE_HISTORY_EXISTS", bool(brute))
                    self.assertEqual(dual.status == "SOURCE_HISTORY_IMPOSSIBLE", not brute)
                    self.assertTrue(verify_history_certificate(model, initial, transcript,
                                                               primal if brute else dual))
                    if brute:
                        self.assertIn(primal.path, brute)
                    checked += 1
        self.assertEqual(checked, 800)

    def test_complete_refinement_matches_independent_experiment_search(self):
        options = [None] + [Step(target, outcome, cost)
                            for target in ("0", "1") for outcome in ("yes", "no")
                            for cost in (0, Q(3, 2))]
        checked = 0
        for edges in itertools.product(options, repeat=2):
            model = machine({(s, "a"): e for s, e in zip(("0", "1"), edges) if e is not None})
            quotient, failures = refine_quotient(model)
            self.assertTrue(audit_quotient(model, quotient).lawful)
            witness = distinguishing_word(model, "0", "1")
            self.assertEqual(quotient["0"] == quotient["1"], witness is None)
            words = [tuple("a" for _ in range(n)) for n in range(5)]
            separators = [w for w in words if observed(model, "0", w) != observed(model, "1", w)]
            self.assertEqual(witness, separators[0] if separators else None)
            self.assertLessEqual(len(failures), 1)
            checked += 1
        self.assertEqual(checked, 81)

    def test_delayed_separator_and_minimum_repair(self):
        states = ("s0", "s1", "t0", "t1", "end0", "end1")
        model = SourceSystem("delayed", "declared", states, ("a",),
                             {s: "root" for s in states},
                             {s: "different" if s == "end1" else "same" for s in states},
                             {("s0", "a"): Step("s1", "ok", 1),
                              ("s1", "a"): Step("end0", "ok", 1),
                              ("t0", "a"): Step("t1", "ok", 1),
                              ("t1", "a"): Step("end1", "ok", 1)})
        self.assertEqual(distinguishing_word(model, "s0", "t0"), ("a", "a"))
        quotient, failures = refine_quotient(model)
        self.assertNotEqual(quotient["s0"], quotient["t0"])
        self.assertLessEqual(len(failures), len(states) - len(set(model.observation.values())))
        for s, t, word in failures:
            self.assertNotEqual(observed(model, s, word), observed(model, t, word))

    def test_two_action_experiments_and_every_representative_lift(self):
        options = (None, Step("0", "ok", 1), Step("1", "ok", 1))
        keys = tuple(itertools.product(("0", "1"), ("a", "b")))
        words = [w for n in range(5) for w in itertools.product(("a", "b"), repeat=n)]
        checked = 0
        for edges in itertools.product(options, repeat=4):
            model = SourceSystem("two-action", "partial-deterministic", ("0", "1"), ("a", "b"),
                                 {"0": "root", "1": "root"}, {"0": "same", "1": "same"},
                                 {key: edge for key, edge in zip(keys, edges) if edge is not None})
            q, _ = refine_quotient(model)
            witness = distinguishing_word(model, "0", "1")
            separators = [w for w in words if observed(model, "0", w) != observed(model, "1", w)]
            self.assertEqual(witness, separators[0] if separators else None)
            # Build quotient by representatives, then test every original lift.
            representative = {q[s]: s for s in model.states}
            for s in model.states:
                for word in words:
                    labels, current, available = [], q[s], True
                    for action in word:
                        edge = model.transitions.get((representative[current], action))
                        if edge is None:
                            available = False
                            break
                        labels.append((edge.outcome, edge.cost))
                        current = q[edge.target]
                    down = (tuple(labels), current) if available else None
                    source = source_run(model, s, word)
                    projected = None if source is None else (source[0], q[source[1]])
                    self.assertEqual(down, projected)
            checked += 1
        self.assertEqual(checked, 81)


if __name__ == "__main__":
    unittest.main()
