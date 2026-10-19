"""Independent finite oracles, hostile controls, and certificate mutations."""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
import random
import unittest

from observational_succ.lawful_history_gluing import (
    CutCertificate, GluingError, PathCertificate, PrivateState, SourceGraph,
    UniformCertificate, audit_projection, lift_or_cut, locally_compatible,
    obstruction_bound, path_from_flow, verify_cut, verify_path, verify_uniform,
    verify_unit_flow,
)


def path_oracle(model, source, reports, actions):
    """Cartesian-product oracle, deliberately not forward support recursion."""
    fibers = [tuple(x for x in model.states if x.source == source and x.report == y)
              for y in reports]
    return tuple(path for path in product(*fibers)
                 if path[0] in model.initial
                 and all((path[i], action, path[i + 1]) in model.edges
                         for i, action in enumerate(actions)))


def broken_interface():
    p, u, v, q = (PrivateState("original", name, report)
                  for name, report in (("p", "P"), ("u", "M"), ("v", "M"), ("q", "Q")))
    return SourceGraph((p, u, v, q), frozenset((p,)),
                       frozenset(((p, "a", u), (v, "b", q))))


class LawfulHistoryGluing(unittest.TestCase):
    def test_pairwise_reports_glue_but_private_interfaces_do_not(self):
        model = broken_interface()
        self.assertTrue(locally_compatible(model, "original", ("P", "M", "Q"), ("a", "b")))
        cut = lift_or_cut(model, "original", ("P", "M", "Q"), ("a", "b"))
        self.assertIsInstance(cut, CutCertificate)
        self.assertTrue(verify_cut(model, cut))
        self.assertEqual(tuple(len(layer) for layer in cut.layers), (1, 1, 0))
        self.assertEqual(path_oracle(model, "original", cut.reports, cut.actions), ())
        # Independent 0/1 Farkas dual for head-minus-tail incidence A:
        # potential^T A >= 0, potential^T b = -1.
        source, sink = ("super", "source"), ("super", "sink")
        potential = {source: 1, sink: 0}
        for t, report in enumerate(cut.reports):
            for x in model.states:
                if x.source == cut.source and x.report == report:
                    potential[t, x] = int(x in cut.layers[t])
        network = [(source, (0, x)) for x in model.initial if x.report == cut.reports[0]]
        network += [((t, x), (t + 1, z)) for t, action in enumerate(cut.actions)
                    for x, a, z in model.edges if a == action and x.report == cut.reports[t]
                    and z.report == cut.reports[t + 1]]
        network += [((len(cut.actions), x), sink) for x in model.states if x.report == cut.reports[-1]]
        self.assertTrue(all(potential[head] - potential[tail] >= 0 for tail, head in network))
        self.assertEqual(potential[sink] - potential[source], -1)
        audit = audit_projection(model, "original")
        self.assertEqual(audit.status, "SPURIOUS_PATH")
        self.assertEqual(len(audit.certificate.actions), 2)
        self.assertTrue(verify_cut(model, audit.certificate))

    def test_full_private_interface_restores_glue_and_cut_mutation_fails(self):
        model = broken_interface()
        p, u, v, q = model.states
        cut = lift_or_cut(model, "original", ("P", "M", "Q"), ("a", "b"))
        repaired = replace(model, edges=model.edges | {(u, "b", q)})
        self.assertFalse(verify_cut(repaired, cut))
        path = lift_or_cut(repaired, "original", cut.reports, cut.actions)
        self.assertTrue(verify_path(repaired, path))
        self.assertFalse(verify_path(model, path))
        self.assertFalse(verify_cut(model, replace(cut, layers=(frozenset(),) * 3)))
        self.assertFalse(verify_path(repaired, replace(path, states=(p, v, q))))

    def test_uniform_trace_lifting_is_weaker_than_every_representative_back_condition(self):
        good, dead = PrivateState("s", "good", "y"), PrivateState("s", "dead", "y")
        model = SourceGraph((good, dead), frozenset((good, dead)), frozenset(((good, "a", good),)))
        audit = audit_projection(model, "s")
        self.assertEqual(audit.status, "ALL_PROJECTED_PATHS_LIFT")
        self.assertEqual(audit.explored, 2)
        self.assertTrue(verify_uniform(model, audit.certificate))
        self.assertFalse(any(x == dead for x, _, _ in model.edges))
        bad = UniformCertificate("s", frozenset((("y", frozenset((good, dead))),)))
        self.assertFalse(verify_uniform(model, bad))
        self.assertFalse(verify_uniform(model, UniformCertificate("s", frozenset())))
        self.assertEqual(audit_projection(model, "s", max_configurations=1).status, "UNRESOLVED")

    def test_no_fixed_local_window_detects_all_obstructions(self):
        # Each k-step constant-report window lifts, but k+1 steps do not.
        for k in (1, 2, 5, 11):
            states = tuple(PrivateState("s", str(i), "same") for i in range(k + 1))
            model = SourceGraph(states, frozenset((states[0],)),
                                frozenset((states[i], "tick", states[i + 1]) for i in range(k)))
            self.assertTrue(verify_path(model, lift_or_cut(model, "s", ("same",) * (k + 1), ("tick",) * k)))
            audit = audit_projection(model, "s")
            self.assertEqual(len(audit.certificate.actions), k + 1)
            self.assertTrue(verify_cut(model, audit.certificate))
            self.assertLessEqual(k + 1, obstruction_bound(model, "s"))

    def test_all_paths_lift_without_a_safe_public_first_action(self):
        zero = PrivateState("s", "zero", "unknown")
        one = PrivateState("s", "one", "unknown")
        end = PrivateState("s", "end", "done")
        model = SourceGraph((zero, one, end), frozenset((zero, one)),
                            frozenset(((zero, "a0", end), (one, "a1", end))))
        audit = audit_projection(model, "s")
        self.assertTrue(verify_uniform(model, audit.certificate))
        self.assertTrue(all(path_oracle(model, "s", ("unknown", "done"), (a,)) for a in ("a0", "a1")))
        safe_actions = [a for a in ("a0", "a1")
                        if all(any(x == initial and action == a for x, action, _ in model.edges)
                               for initial in model.initial)]
        self.assertEqual(safe_actions, [])

    def test_every_word_has_lift_but_no_online_successor_resolver_exists(self):
        p, u, v = (PrivateState("s", name, "y") for name in ("p", "u", "v"))
        edges = {(p, a, z) for a in ("a", "b") for z in (u, v)}
        edges |= {(u, "a", z) for z in (u, v)}
        edges |= {(v, "b", z) for z in (u, v)}
        model = SourceGraph((p, u, v), frozenset((p,)), frozenset(edges))
        audit = audit_projection(model, "s")
        self.assertEqual(audit.status, "ALL_PROJECTED_PATHS_LIFT")
        self.assertTrue(verify_uniform(model, audit.certificate))
        self.assertEqual(audit.certificate.configurations,
                         frozenset((("y", frozenset((p,))), ("y", frozenset((u, v))))))
        for n in range(6):
            for word in product(("a", "b"), repeat=n):
                self.assertTrue(path_oracle(model, "s", ("y",) * (n + 1), word))
        # Even an omniscient resolver knows only the requests so far. After
        # the first request a, every available chosen successor has a hostile
        # next request. The initial private state is fixed, not ambiguous.
        first_choices = {z for x, action, z in model.edges if x == p and action == "a"}
        self.assertEqual(first_choices, {u, v})
        for chosen in first_choices:
            hostile = [a for a in ("a", "b") if not any(x == chosen and action == a
                                                         for x, action, _ in model.edges)]
            self.assertEqual(len(hostile), 1)

    def test_fractional_private_flow_has_an_integral_path(self):
        p, u, v, q = broken_interface().states
        model = SourceGraph((p, u, v, q), frozenset((p,)),
                            frozenset(((p, "a", u), (p, "a", v), (u, "b", q), (v, "b", q))))
        nodes = ({p: 1}, {u: Q(1, 2), v: Q(1, 2)}, {q: 1})
        edges = ({(p, u): Q(1, 2), (p, v): Q(1, 2)},
                 {(u, q): Q(1, 2), (v, q): Q(1, 2)})
        args = (model, "original", ("P", "M", "Q"), ("a", "b"))
        self.assertTrue(verify_unit_flow(*args, nodes, edges))
        self.assertTrue(verify_path(model, path_from_flow(*args, nodes, edges)))
        self.assertFalse(verify_unit_flow(*args, ({p: 1.0},) + nodes[1:], edges))
        self.assertFalse(verify_unit_flow(*args, ({p: True},) + nodes[1:], edges))

    def test_projected_unit_flow_is_not_private_conservation(self):
        model = broken_interface()
        p, u, v, q = model.states
        nodes = ({p: 1}, {u: 1}, {q: 1})
        edges = ({(p, u): 1}, {(v, q): 1})
        self.assertFalse(verify_unit_flow(model, "original", ("P", "M", "Q"), ("a", "b"), nodes, edges))
        with self.assertRaises(GluingError):
            path_from_flow(model, "original", ("P", "M", "Q"), ("a", "b"), nodes, edges)

    def test_odd_cycle_fractional_certificate_and_integral_obstruction(self):
        pairs = ((0, 1), (1, 2), (2, 0))
        fractional = (Q(1, 2),) * 3
        self.assertTrue(all(fractional[i] + fractional[j] == 1 for i, j in pairs))
        binary = tuple(product((0, 1), repeat=3))
        self.assertFalse(any(all(x[i] + x[j] == 1 for i, j in pairs) for x in binary))
        # Exact local *distributions* also pass all separator equalities.
        local = {(0, 1): Q(1, 2), (1, 0): Q(1, 2)}
        self.assertEqual(sum(local.values()), 1)
        for coordinate in (0, 1):
            self.assertEqual(sum(p for bits, p in local.items() if bits[coordinate] == 0), Q(1, 2))
        # A global nonnegative law must obey E[number of unequal pairs] <= 2.
        self.assertEqual(max(sum(x[i] != x[j] for i, j in pairs) for x in binary), 2)
        self.assertEqual(sum(sum(p for (a, b), p in local.items() if a != b) for _ in pairs), 3)

    def test_source_switch_rejected_and_sources_audited_separately(self):
        a, b = PrivateState("A", "x", "y"), PrivateState("B", "x", "y")
        with self.assertRaises(GluingError):
            SourceGraph((a, b), frozenset((a,)), frozenset(((a, "switch", b),)))
        model = SourceGraph((a, b), frozenset((a, b)), frozenset(((b, "tick", b),)))
        self.assertFalse(locally_compatible(model, "A", ("y", "y"), ("tick",)))
        self.assertTrue(verify_cut(model, lift_or_cut(model, "A", ("y", "y"), ("tick",))))
        self.assertTrue(verify_path(model, lift_or_cut(model, "B", ("y", "y"), ("tick",))))
        with self.assertRaises(GluingError):
            audit_projection(model, "unknown")

    def test_zero_steps_empty_initial_and_malformed_certificates(self):
        x = PrivateState("s", "x", "r")
        model = SourceGraph((x,), frozenset((x,)), frozenset())
        self.assertTrue(verify_path(model, lift_or_cut(model, "s", ("r",), ())))
        no_initial = replace(model, initial=frozenset())
        self.assertTrue(verify_cut(no_initial, lift_or_cut(no_initial, "s", ("r",), ())))
        audit = audit_projection(no_initial, "s")
        self.assertTrue(verify_uniform(no_initial, audit.certificate))  # Vacuous language.
        self.assertFalse(verify_path(model, PathCertificate("s", ("r",), (), ())))
        self.assertFalse(verify_cut(model, CutCertificate("s", ("r",), (), ())))
        self.assertFalse(verify_uniform(model, UniformCertificate("s", frozenset((("r", frozenset()),)))))
        with self.assertRaises(GluingError):
            audit_projection(model, "s", max_configurations=True)

    def test_exhaustive_two_state_uniform_audit_against_cartesian_oracle(self):
        cases = 0
        for reports in product(("0", "1"), repeat=2):
            states = tuple(PrivateState("s", str(i), reports[i]) for i in range(2))
            possible_edges = tuple((x, "a", z) for x in states for z in states)
            for mask in range(16):
                edges = frozenset(e for i, e in enumerate(possible_edges) if mask & (1 << i))
                for initial_mask in (1, 2, 3):
                    model = SourceGraph(states, frozenset(x for i, x in enumerate(states) if initial_mask & (1 << i)), edges)
                    bound = obstruction_bound(model, "s")
                    bad_lengths = []
                    for n in range(bound + 1):
                        for word in product(sorted(set(reports)), repeat=n + 1):
                            actions = ("a",) * n
                            expected = path_oracle(model, "s", word, actions)
                            cert = lift_or_cut(model, "s", word, actions)
                            self.assertEqual(isinstance(cert, PathCertificate), bool(expected))
                            self.assertTrue(verify_path(model, cert) if expected else verify_cut(model, cert))
                            if locally_compatible(model, "s", word, actions) and not expected:
                                bad_lengths.append(n)
                    audit = audit_projection(model, "s")
                    self.assertEqual(audit.status == "SPURIOUS_PATH", bool(bad_lengths))
                    if bad_lengths:
                        self.assertEqual(len(audit.certificate.actions), min(bad_lengths))
                    else:
                        self.assertTrue(verify_uniform(model, audit.certificate))
                    cases += 1
        self.assertEqual(cases, 192)

    def test_fresh_seeded_four_state_two_action_holdout(self):
        rng = random.Random(2026101807)
        for _ in range(40):
            states = tuple(PrivateState("held-out", str(i), str(rng.randrange(2))) for i in range(4))
            edges = frozenset((x, a, z) for x in states for a in ("a", "b") for z in states if rng.randrange(5) == 0)
            model = SourceGraph(states, frozenset(states[:2]), edges)
            for _ in range(25):
                n = rng.randrange(6)
                reports = tuple(str(rng.randrange(2)) for _ in range(n + 1))
                actions = tuple(rng.choice(("a", "b")) for _ in range(n))
                expected = path_oracle(model, "held-out", reports, actions)
                cert = lift_or_cut(model, "held-out", reports, actions)
                self.assertEqual(isinstance(cert, PathCertificate), bool(expected))
                self.assertTrue(verify_path(model, cert) if expected else verify_cut(model, cert))
            audit = audit_projection(model, "held-out")
            if audit.status == "SPURIOUS_PATH":
                self.assertTrue(verify_cut(model, audit.certificate))
                self.assertLessEqual(len(audit.certificate.actions), obstruction_bound(model, "held-out"))
            else:
                self.assertTrue(verify_uniform(model, audit.certificate))


if __name__ == "__main__":
    unittest.main()
