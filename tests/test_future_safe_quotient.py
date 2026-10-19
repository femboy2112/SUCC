"""Exact controls and independent word-enumeration oracle for safe forgetting."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import combinations, product
from random import Random

from observational_succ.future_safe_quotient import (
    State, Edge, Machine, Separator, QuotientCertificate, ForgettingError,
    trace, distinguishing_word, minimize, verify_certificate,
    audit_representation, budget_lift, certificate_payload,
    minimum_distinguishing_budget,
)


def machine(outputs, rows, actions=("a",), sources=None, tasks=None):
    names = tuple(str(i) for i in range(len(outputs)))
    states = tuple(State(name, sources[i] if sources else "source", str(outputs[i]),
                         tasks[i] if tasks else ()) for i, name in enumerate(names))
    edges = tuple(Edge(names[i], a, names[target], Q(cost))
                  for (i, a), (target, cost) in rows.items())
    return Machine(states, actions, edges)


def oracle_trace(m, start, word):
    """Independent direct interpreter; does not call production trace/maps."""
    records = {s.name: (s.source, s.observation, s.tasks) for s in m.states}
    transitions = {(e.start, e.action): (e.target, e.cost) for e in m.edges}
    out = [records[start]]
    state = start
    for action in word:
        if (state, action) not in transitions:
            out.append(("denied", action))
            return out
        state, price = transitions[state, action]
        out.extend((price, records[state]))
    return out


def words(actions, max_length):
    for n in range(max_length + 1):
        yield from product(actions, repeat=n)


def labels_of(cert):
    return {s: i for i, b in enumerate(cert.blocks) for s in b}


class TestFutureSafeForgetting(unittest.TestCase):
    def assert_oracle(self, m):
        cert = minimize(m)
        self.assertTrue(verify_certificate(m, cert))
        labels = labels_of(cert)
        for x, y in combinations((s.name for s in m.states), 2):
            separating = next((w for w in words(m.actions, len(m.states) - 1)
                               if oracle_trace(m, x, w) != oracle_trace(m, y, w)), None)
            w = distinguishing_word(m, x, y)
            self.assertEqual(labels[x] == labels[y], separating is None)
            self.assertEqual(w is None, separating is None)
            if w is not None:
                self.assertEqual(len(w), len(separating))
                self.assertNotEqual(oracle_trace(m, x, w), oracle_trace(m, y, w))

    def test_all_2744_three_state_unary_models_against_word_oracle(self):
        choices = (None,) + tuple(product(range(3), (0, 1)))
        count = 0
        for outputs in product((0, 1), repeat=3):
            for transitions in product(choices, repeat=3):
                rows = {(i, "a"): e for i, e in enumerate(transitions) if e is not None}
                self.assert_oracle(machine(outputs, rows))
                count += 1
        self.assertEqual(count, 2744)

    def test_fresh_four_state_binary_action_holdouts(self):
        rng = Random(202610184791)
        for _ in range(120):
            rows = {}
            for i, a in product(range(4), ("a", "b")):
                if rng.randrange(4):
                    rows[i, a] = rng.randrange(4), Q(rng.randrange(4), 3)
            self.assert_oracle(machine(tuple(rng.randrange(2) for _ in range(4)),
                                       rows, ("a", "b")))

    def test_positive_negative_null_and_cost_controls(self):
        same = machine((0, 0), {(0, "a"): (0, 0), (1, "a"): (1, 0)})
        self.assertEqual(minimize(same).blocks, (("0", "1"),))
        self.assertIsNone(distinguishing_word(same, "0", "1"))
        cost = machine((0, 0), {(0, "a"): (0, Q(1, 3)),
                                (1, "a"): (1, Q(1, 2))})
        self.assertEqual(distinguishing_word(cost, "0", "1"), ("a",))
        unavailable = machine((0, 0), {(0, "a"): (0, 0)})
        self.assertEqual(distinguishing_word(unavailable, "0", "1"), ("a",))
        output = machine((0, 1), {})
        self.assertEqual(distinguishing_word(output, "0", "1"), ())

    def test_source_is_mandatory_type_and_source_change_is_explicit(self):
        m = machine((0, 0), {(0, "a"): (1, 0)}, sources=("source-A", "source-B"))
        self.assertEqual(distinguishing_word(m, "0", "1"), ())
        self.assertEqual(trace(m, "0", ("a",))[-1][-1][0], "source-B")

    def test_designated_proof_task_result_is_preserved_without_soundness_claim(self):
        m = machine((0, 0), {}, tasks=((('T:proof-check', 'accepted'),),
                                       (('T:proof-check', 'rejected'),)))
        self.assertEqual(distinguishing_word(m, "0", "1"), ())
        self.assertFalse(audit_representation(m, ("same", "same"))["future_safe"])

    def test_history_countermodel_latest_display_is_insufficient(self):
        # States 0 and 1 encode histories 00 and 10. Next output repeats first bit.
        m = machine((0, 0, 0, 1), {(0, "a"): (2, 0), (1, "a"): (3, 0)})
        audit = audit_representation(m, ("display0", "display0", "display0", "display1"))
        self.assertFalse(audit["future_safe"])
        self.assertEqual(audit["future_obstruction"].word, ("a",))

    def test_agreement_only_on_common_lawful_words_is_not_transitive(self):
        # 0=x, 1=y, 2=z, 3=q. No rejection observations are used in this test.
        m = machine((0, 0, 0, 1), {(0, "a"): (0, 0), (2, "a"): (3, 0)})
        transitions = {(e.start, e.action): e.target for e in m.edges}

        def legal(start, word):
            for a in word:
                if (start, a) not in transitions:
                    return False
                start = transitions[start, a]
            return True

        def agrees_on_common_words(x, y):
            return all(oracle_trace(m, x, w) == oracle_trace(m, y, w)
                       for w in words(m.actions, 4) if legal(x, w) and legal(y, w))

        # The finite check is exhaustive for pairs involving y: it has no
        # nonempty lawful word at all. For x,z, the single action is a witness.
        self.assertTrue(agrees_on_common_words("0", "1"))
        self.assertTrue(agrees_on_common_words("1", "2"))
        self.assertFalse(agrees_on_common_words("0", "2"))

    def test_safe_refinement_need_not_update_autonomously(self):
        m = machine((0, 0, 0), {(0, "a"): (0, 0), (1, "a"): (2, 0),
                                (2, "a"): (2, 0)})
        audit = audit_representation(m, ("u", "u", "v"))
        self.assertTrue(audit["future_safe"])
        self.assertFalse(audit["autonomous"])
        self.assertEqual(audit["update_obstruction"], ("successor", "0", "1", "a"))
        self.assertEqual(dict(audit["factor"]), {"u": 0, "v": 0})

    def test_factorization_direction_and_every_three_state_representation(self):
        m = machine((0, 0, 1), {(0, "a"): (0, 0), (1, "a"): (0, 0),
                                (2, "a"): (2, 0)})
        canonical = labels_of(minimize(m))
        for proposed in product(("p", "q", "r"), repeat=3):
            audit = audit_representation(m, proposed)
            expected = all(proposed[i] != proposed[j] or canonical[str(i)] == canonical[str(j)]
                           for i, j in combinations(range(3), 2))
            self.assertEqual(audit["future_safe"], expected)
            if expected:
                f = dict(audit["factor"])
                for i in range(3):
                    self.assertEqual(f[proposed[i]], canonical[str(i)])
            if audit["autonomous"]:
                self.assertTrue(audit["future_safe"])

    def test_fixed_budget_equivalence_is_not_a_same_budget_congruence(self):
        # x->u->0 and y->v->1, every edge costs 1. x,y agree at budget 1,
        # u,v disagree at budget 1, but agree at the correct residual budget 0.
        m = machine((0, 0, 0, 0, 0, 1),
                    {(0, "a"): (2, 1), (1, "a"): (3, 1),
                     (2, "b"): (4, 1), (3, "b"): (5, 1)}, ("a", "b"))
        lifted = budget_lift(m, Q(1))
        self.assertIsNone(distinguishing_word(lifted.machine,
                          lifted.name("0", Q(1)), lifted.name("1", Q(1))))
        self.assertEqual(distinguishing_word(lifted.machine,
                         lifted.name("2", Q(1)), lifted.name("3", Q(1))), ("b",))
        self.assertIsNone(distinguishing_word(lifted.machine,
                          lifted.name("2", Q(0)), lifted.name("3", Q(0))))
        larger = budget_lift(m, Q(2))
        self.assertEqual(distinguishing_word(larger.machine,
                         larger.name("0", Q(2)), larger.name("1", Q(2))), ("a", "b"))

    def test_zero_cost_loops_and_exact_rational_residuals(self):
        m = machine((0,), {(0, "free"): (0, 0), (0, "paid"): (0, Q(1, 3))},
                    ("free", "paid"))
        lifted = budget_lift(m, Q(1))
        self.assertEqual({b for _, _, b in lifted.origins}, {Q(0), Q(1, 3), Q(2, 3), Q(1)})
        self.assertEqual(len(lifted.machine.states), 4)
        self.assertTrue(verify_certificate(lifted.machine, minimize(lifted.machine)))
        self.assertEqual(distinguishing_word(lifted.machine,
                         lifted.name("0", Q(1, 3)), lifted.name("0", Q(2, 3))),
                         ("paid", "paid"))
        with self.assertRaisesRegex(ForgettingError, "UNKNOWN"):
            budget_lift(m, Q(1), max_states=3)

    def test_exact_budget_threshold_selects_cheapest_not_shortest_word(self):
        m = machine((0, 0, 0, 0, 0, 1),
                    {(0, "expensive"): (4, 7), (1, "expensive"): (5, 7),
                     (0, "a"): (2, Q(1, 3)), (1, "a"): (3, Q(1, 3)),
                     (2, "b"): (4, Q(1, 2)), (3, "b"): (5, Q(1, 2))},
                    ("expensive", "a", "b"))
        self.assertEqual(distinguishing_word(m, "0", "1"), ("expensive",))
        threshold = minimum_distinguishing_budget(m, "0", "1")
        self.assertEqual(threshold.budget, Q(5, 6))
        self.assertEqual(threshold.word, ("a", "b"))
        for budget in (Q(0), Q(1, 2), Q(5, 6), Q(1), Q(7)):
            lifted = budget_lift(m, budget)
            distinguishes = distinguishing_word(lifted.machine,
                lifted.name("0", budget), lifted.name("1", budget)) is not None
            self.assertEqual(distinguishes, budget >= threshold.budget)

    def test_cost_threshold_is_cheaper_price_and_zero_threshold_is_attained(self):
        m = machine((0, 0), {(0, "a"): (0, Q(1, 3)), (1, "a"): (1, Q(1, 2))})
        self.assertEqual(minimum_distinguishing_budget(m, "0", "1").budget, Q(1, 3))
        m = machine((0, 0), {(0, "a"): (0, 0)})
        threshold = minimum_distinguishing_budget(m, "0", "1")
        self.assertEqual((threshold.budget, threshold.word), (Q(0), ("a",)))
        m = machine((0, 0), {(0, "a"): (1, 0), (1, "a"): (0, 0)})
        self.assertIsNone(minimum_distinguishing_budget(m, "0", "1"))

    def test_budget_threshold_independent_lift_holdouts(self):
        rng = Random(202610186113)
        for _ in range(70):
            rows = {(i, a): (rng.randrange(3), Q(rng.randrange(4), 2))
                    for i, a in product(range(3), ("a", "b")) if rng.randrange(4)}
            m = machine(tuple(rng.randrange(2) for _ in range(3)), rows, ("a", "b"))
            threshold = minimum_distinguishing_budget(m, "0", "1")
            self.assertEqual(threshold is None, distinguishing_word(m, "0", "1") is None)
            for budget in (Q(0), Q(1, 2), Q(1), Q(2), Q(3)):
                lifted = budget_lift(m, budget)
                self.assertEqual(distinguishing_word(lifted.machine,
                    lifted.name("0", budget), lifted.name("1", budget)) is None,
                    threshold is None or budget < threshold.budget)

    def test_budget_hides_unaffordable_cost_and_no_positive_step_at_zero(self):
        m = machine((0, 0), {(0, "a"): (0, 2), (1, "a"): (1, 3)})
        lifted = budget_lift(m, Q(1))
        self.assertEqual(len(minimize(lifted.machine).blocks), 1)
        self.assertEqual(len(minimize(budget_lift(m, Q(0)).machine).blocks), 1)
        # Residual budgets are stored but not observed: both exhausted states merge.
        self.assertEqual(len(minimize(budget_lift(m, Q(3)).machine).blocks), 3)

    def test_certificate_mutations_fail(self):
        m = machine((0, 0, 1), {(0, "a"): (2, 0), (1, "a"): (2, 0)})
        cert = minimize(m)
        self.assertTrue(verify_certificate(m, cert))
        mutants = [QuotientCertificate((("0", "1", "2"),), ()),
                   QuotientCertificate((("0", "1"),), ()),
                   QuotientCertificate((("0", "1"), ("1", "2")), ()),
                   replace(cert, separators=()),
                   replace(cert, separators=(Separator("0", "2", ("a",)),))]
        for mutant in mutants:
            with self.assertRaises(ForgettingError):
                verify_certificate(m, mutant)
        # Splitting an equivalent pair can be locally sound but not minimal.
        split = QuotientCertificate((("0",), ("1",), ("2",)),
                                    (Separator("0", "1", ()),
                                     Separator("0", "2", ()), Separator("1", "2", ())))
        with self.assertRaises(ForgettingError):
            verify_certificate(m, split)
        cost_mutation = replace(m, edges=(replace(m.edges[0], cost=Q(1)), m.edges[1]))
        with self.assertRaises(ForgettingError):
            verify_certificate(cost_mutation, cert)

    def test_payload_contains_exact_rational_and_declared_interfaces(self):
        m = machine((0, 0), {(0, "a"): (0, Q(2, 3))})
        payload = certificate_payload(m, minimize(m))
        self.assertEqual(payload["edges"][0]["cost"], [2, 3])
        self.assertEqual(payload["certificate"]["separators"][0]["word"], ["a"])

    def test_model_validation_rejects_hidden_nondeterminism_and_float(self):
        s = (State("x", "S", "0"),)
        for edges in ((Edge("x", "a", "x", 0.1),),
                      (Edge("x", "a", "x", Q(-1)),),
                      (Edge("x", "a", "x", Q(1)), Edge("x", "a", "x", Q(2))),
                      (Edge("x", "a", "other", Q(0)),)):
            with self.assertRaises(ForgettingError):
                Machine(s, ("a",), edges)
        with self.assertRaises(ForgettingError):
            Machine((State("x", "S", "0", (("T", "a"),)),
                     State("y", "S", "0", (("U", "a"),))), (), ())
        with self.assertRaises(ForgettingError):
            budget_lift(Machine(s, (), ()), 1.0)
        with self.assertRaises(ForgettingError):
            trace(Machine(s, (), ()), "x", ("unknown",))


if __name__ == "__main__":
    unittest.main()
