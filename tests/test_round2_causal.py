import dataclasses
from fractions import Fraction as Q
import itertools
import random
import unittest

from observational_succ.round2_causal import (
    Blocker, CausalError, Certificate, Edge, Loss, Policy, Report, Source,
    compare_interfaces, guard_source, output_split_combined, post, safe_menu,
    simulation, split_combined, stochastic_contract, synthesize, verify_certificate,
)
from observational_succ.no_ghost import (
    Event, FiniteContract, Step, solve_nonnegative, verify_dual, verify_primal,
)
from observational_succ.no_ghost_policy import (
    compile_public_policy, replay_public_policy, verify_policy_solution, verify_policy_obstruction,
)


def brute_trees(actions, reports, depth):
    """Full Cartesian enumeration of public decision trees, without beliefs."""
    if depth == 0:
        return (None,)
    children = brute_trees(actions, reports, depth - 1)
    return tuple((a, dict(zip(reports, choices))) for a in actions
                 for choices in itertools.product(children, repeat=len(reports)))


def direct_safe(model, state, tree):
    """Private-path recursion with one fixed total public tree."""
    if tree is None:
        return True
    a, children = tree
    row = model.transitions.get((state, a))
    if not row:
        return False
    return all(direct_safe(model, edge.target,
                           children[(edge.outcome, edge.cost, model.observation[edge.target])])
               for edge in row)


def brute_exists(model, initial, horizon, reports):
    return any(all(direct_safe(model, s, tree) for s in initial)
               for tree in brute_trees(model.actions, reports, horizon))


class Round2CausalTests(unittest.TestCase):
    def test_required_split_example_relations(self):
        A, B = split_combined()
        initial = frozenset({"root"})
        self.assertEqual(compare_interfaces(A, initial, B, initial).status, "EQUIVALENT")
        public = compare_interfaces(A, initial, B, initial, public_safe=True)
        self.assertEqual(public.reason, "PUBLIC_MENU")
        self.assertEqual(tuple(a for a, _ in public.witness), ("a",))
        self.assertIn(("root", "root"), simulation(A, B))
        self.assertNotIn(("root", "root"), simulation(B, A))
        self.assertNotIn(("root", "root"), simulation(A, B, bisimulation=True))
        successor = next(iter(post(A, initial, "a").values()))
        self.assertEqual(successor, frozenset({"s0", "s1"}))
        self.assertEqual(safe_menu(A, successor), ())
        self.assertTrue(post(A, frozenset({"s0"}), "b0"))
        self.assertTrue(post(A, frozenset({"s1"}), "b1"))
        for model, expected in ((A, "NO_PUBLIC_POLICY"), (B, "PUBLIC_POLICY_EXISTS")):
            cert = synthesize(model, initial, 2)
            self.assertEqual(cert.status, expected)
            self.assertTrue(verify_certificate(model, initial, 2, cert))

    def test_existing_farkas_oracle_independently_confirms_split(self):
        A, B = split_combined()
        for model, valid in ((A, False), (B, True)):
            chance = stochastic_contract(model)
            system = compile_public_policy(chance, 2).system
            equations = system.equations((), ())
            solution = solve_nonnegative(*equations)
            if valid:
                self.assertTrue(verify_primal(*equations, solution.primal))
                self.assertTrue(verify_policy_solution(chance, system, solution.primal, (), ()))
            else:
                self.assertTrue(verify_dual(*equations, solution.dual))
                self.assertTrue(verify_policy_obstruction(chance, 2, (), (), solution.dual))
                # Missing hidden row is not a probability-zero success/failure event.
                with self.assertRaises(ValueError):
                    replay_public_policy(chance, 2,
                                         {(): {"a": Q(1)}, (("a", "ok"),): {"b0": Q(1)}})

    def test_trace_and_public_interface_still_do_not_imply_bisimulation(self):
        A, B = output_split_combined()
        initial = frozenset({"root"})
        self.assertEqual(compare_interfaces(A, initial, B, initial).status, "EQUIVALENT")
        self.assertEqual(compare_interfaces(A, initial, B, initial, public_safe=True).status, "EQUIVALENT")
        self.assertNotIn(("root", "root"), simulation(A, B, bisimulation=True))
        for model in (A, B):
            cert = synthesize(model, initial, 4)
            self.assertTrue(verify_certificate(model, initial, 4, cert))
            self.assertEqual(cert.status, "PUBLIC_POLICY_EXISTS")

    def test_guard_family_exact_exponential_interface_bound(self):
        for n in range(1, 7):
            model = guard_source(n)
            menus = set()
            for bits in range(1, 1 << n):
                desired = frozenset(str(j) for j in range(n) if bits & (1 << j))
                belief = frozenset(model.states)
                for state in model.states:
                    if state not in desired:
                        action = "test_" + state
                        self.assertIn(action, safe_menu(model, belief))
                        belief = post(model, belief, action)[Report("miss", Q(1), "hidden")]
                self.assertEqual(belief, desired)
                menu = frozenset(safe_menu(model, belief))
                for j in model.states:
                    self.assertEqual("guard_" + j in menu, j not in desired)
                menus.add(menu)
            self.assertEqual(len(menus), (1 << n) - 1)

    def test_source_bound_certificates_reject_false_source_mutations(self):
        A, B = split_combined()
        initial = frozenset({"root"})
        loss = synthesize(A, initial, 2)
        win = synthesize(B, initial, 2)
        self.assertFalse(verify_certificate(A, initial, 2, win))
        forged = dataclasses.replace(win, source_digest=A.digest())
        self.assertFalse(verify_certificate(A, initial, 2, forged))
        changed = dict(A.transitions)
        changed["s1", "b0"] = (Edge("end", "done"),)
        mutation = dataclasses.replace(A, transitions=changed)
        # Even identical source_id/basis cannot hide changed source bytes.
        self.assertEqual(A.source_id, mutation.source_id)
        self.assertFalse(verify_certificate(mutation, initial, 2, loss))
        self.assertFalse(verify_certificate(dataclasses.replace(A, basis="forged"), initial, 2, loss))
        self.assertFalse(verify_certificate(A, initial, 1, loss))
        self.assertFalse(verify_certificate(A, initial, 2, dataclasses.replace(loss,
                         loss=Loss((Blocker("a", unavailable_state="root"),)))))
        tags = dict(A.original)
        tags["s0"] = "other-source"
        with self.assertRaises(CausalError):
            dataclasses.replace(A, original=tags)

    def test_reject_missing_or_counterfeit_policy_branches(self):
        _, B = split_combined()
        initial = frozenset({"root"})
        win = synthesize(B, initial, 2)
        for policy in (Policy(), Policy("a"), Policy("invented"),
                       Policy("a", win.policy.branches + win.policy.branches)):
            self.assertFalse(verify_certificate(B, initial, 2, dataclasses.replace(win, policy=policy)))
        self.assertFalse(verify_certificate(B, initial, 2, win, max_nodes=0))

    def test_full_nondeterministic_tables_against_cartesian_policy_enumeration(self):
        states, actions = ("0", "1"), ("a", "b")
        positions = tuple(itertools.product(states, actions, states))
        count = 0
        for bits in range(256):
            rows = {}
            for i, (s, a, t) in enumerate(positions):
                if bits & (1 << i):
                    rows.setdefault((s, a), []).append(Edge(t))
            model = Source("enumerated", "all-eight-edges", states, actions,
                           {s: "root" for s in states}, {s: "hidden" for s in states},
                           {key: tuple(row) for key, row in rows.items()})
            for initial in (frozenset({"0"}), frozenset({"1"}), frozenset(states)):
                for depth in range(3):
                    cert = synthesize(model, initial, depth)
                    expected = brute_exists(model, initial, depth, (("ok", Q(1), "hidden"),))
                    self.assertEqual(cert.status == "PUBLIC_POLICY_EXISTS", expected)
                    self.assertTrue(verify_certificate(model, initial, depth, cert))
                    count += 1
        self.assertEqual(count, 2304)

    def test_adaptive_two_report_models_against_full_policy_trees(self):
        rng = random.Random(20261018)
        states, actions = ("0", "1"), ("a", "b")
        report_domain = (("yes", Q(1), "hidden"), ("no", Q(1), "hidden"))
        count = 0
        for _ in range(64):
            rows = {}
            for s, a, target, outcome in itertools.product(states, actions, states, ("yes", "no")):
                if rng.randrange(2):
                    rows.setdefault((s, a), []).append(Edge(target, outcome))
            model = Source("seeded", "two-outcome", states, actions,
                           {s: "root" for s in states}, {s: "hidden" for s in states},
                           {key: tuple(row) for key, row in rows.items()})
            for initial in (frozenset({"0"}), frozenset({"1"}), frozenset(states)):
                cert = synthesize(model, initial, 2)
                self.assertEqual(cert.status == "PUBLIC_POLICY_EXISTS",
                                 brute_exists(model, initial, 2, report_domain))
                self.assertTrue(verify_certificate(model, initial, 2, cert))
                count += 1
        self.assertEqual(count, 192)

    def test_legal_stochastic_laws_need_more_than_support(self):
        laws = []
        for p in (Q(1, 3), Q(2, 3)):
            model = FiniteContract("explicit-coin-" + str(p), "lawful-coin", ("source",),
                                  ("root", "end"), {"root": 0, "end": 1}, (Event("coin"),),
                                  (("source", "root", Q(1)),),
                                  {((), "coin", "source", "root"):
                                   (Step("yes", "end", "Y", p), Step("no", "end", "N", 1 - p))})
            system = compile_public_policy(model, 1).system
            result = solve_nonnegative(*system.equations((), ()))
            self.assertTrue(verify_policy_solution(model, system, result.primal, (), ()))
            law = {atom.public[-1][1]: weight for atom, weight in zip(system.atoms, system.weights(result.primal))}
            laws.append(law)
        self.assertEqual(set(laws[0]), set(laws[1]))
        self.assertNotEqual(laws[0], laws[1])
        self.assertEqual(laws[0]["yes"], Q(1, 3))
        self.assertEqual(laws[1]["yes"], Q(2, 3))

    def test_bounds_types_and_empty_belief(self):
        A, B = split_combined()
        initial = frozenset({"root"})
        self.assertEqual(synthesize(A, initial, 2, max_nodes=0).status, "UNRESOLVED")
        self.assertEqual(compare_interfaces(A, initial, B, initial, max_pairs=0).status, "UNRESOLVED")
        with self.assertRaises(CausalError):
            synthesize(A, frozenset(), 2)
        with self.assertRaises(CausalError):
            Report("ok", 1.0, "middle")
        with self.assertRaises(CausalError):
            Edge("s", cost=True)
        with self.assertRaises(CausalError):
            stochastic_contract(A, {("root", "a"): (Q(0), Q(1))})


if __name__ == "__main__":
    unittest.main()
