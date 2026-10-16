"""Hostile finite controls and a separate policy-tree enumeration oracle."""
from dataclasses import replace
from functools import lru_cache
from itertools import combinations, product
import unittest

from observational_succ.collective_policy import (
    Action, CollectiveModel, CollectivePolicyError, Cost, JointState, Outcome,
    Policy, SearchLimit, Source, capacity_parity_model, cross_enabled_model,
    miniport_model, replay_policy, restrict_observers, solve_collective_policy,
)


LADDER_BUDGET = Cost(8, 4, 4, 1, 1, 9)


def tiny(rows, *, targets=("0", "1"), initial=((0, 0), (1, 1)), states=None):
    if states is None:
        states = tuple(JointState(str(i), ("ready",)) for i in range(len(rows[0])))
    return CollectiveModel("declared-test", "original-bit", ("E",),
                           tuple(Source(f"s{i}", t) for i, t in enumerate(targets)),
                           states, initial,
                           tuple(Action(chr(97 + i), "E", "probe", Cost(1, 1, observation_bits=max(0, len({o.public for row in r for o in row}) - 1).bit_length(), certificate=1), r)
                                 for i, r in enumerate(rows)))


@lru_cache(None)
def raw_trees(depth, actions):
    """Enumerate all public binary-outcome policies, including early stops.

    Unreachable branches are harmless total-function completions. This oracle
    never calls the planner, belief helpers, replay, or a reachability DP.
    """
    trees = ["0", "1"]
    if depth:
        subtrees = raw_trees(depth - 1, actions)
        trees.extend((a, left, right) for a in range(actions)
                     for left in subtrees for right in subtrees)
    return tuple(trees)


def raw_tree_wins(model, budget, tree):
    def walk(source, current, node, remaining):
        if type(node) is str:
            return (node == model.sources[source].target and
                    all(x >= y for x, y in zip(remaining, model.leaf_cost.vector)))
        action = model.actions[node[0]]
        rest = tuple(x - y for x, y in zip(remaining, action.cost.vector))
        if min(rest) < 0 or not action.rows[current]:
            return False
        # All raw supports, including two poststates with the same public bit.
        return all(walk(source, o.after, node[1 + int(o.public)], rest)
                   for o in action.rows[current])
    return all(walk(s, c, tree, budget.vector) for s, c in model.initial)


def exhaustive_controls():
    atoms = tuple(Outcome(str(y), c) for y in range(2) for c in range(2))
    deterministic_rows = ((),) + tuple((o,) for o in atoms)
    support_rows = tuple(tuple(atoms[i] for i in range(4) if mask & (1 << i)) for mask in range(16))
    counts = {"deterministic_two_action_models": 0, "nondeterministic_one_action_models": 0,
              "budget_comparisons": 0, "winning_comparisons": 0, "replayed_winners": 0}
    for family, rows, action_count in (
        ("deterministic_two_action_models", deterministic_rows, 2),
        ("nondeterministic_one_action_models", support_rows, 1),
    ):
        for flat in product(rows, repeat=2 * action_count):
            tables = tuple(tuple(flat[2 * i:2 * i + 2]) for i in range(action_count))
            for target in product(("0", "1"), repeat=2):
                model = tiny(tables, targets=target)
                counts[family] += 1
                for depth in range(3):
                    budget = Cost(depth, depth, observation_bits=2 * depth, certificate=depth + 1)
                    expected = any(raw_tree_wins(model, budget, tree)
                                   for tree in raw_trees(depth, action_count))
                    result = solve_collective_policy(model, budget)
                    if result.winning != expected:
                        raise AssertionError((family, flat, target, depth, expected, result))
                    counts["budget_comparisons"] += 1
                    counts["winning_comparisons"] += int(expected)
                    if result.winning:
                        replay_policy(model, budget, result.policy)
                        counts["replayed_winners"] += 1
    return counts


class ChronologicalPolicyTests(unittest.TestCase):
    def test_cross_enabled_sequence_costs_and_public_history(self):
        model = cross_enabled_model()
        result = solve_collective_policy(model, LADDER_BUDGET)
        self.assertTrue(result.winning)
        audit = replay_policy(model, LADDER_BUDGET, result.policy)
        self.assertEqual(audit.worst_cost, LADDER_BUDGET)
        self.assertEqual((audit.policy_nodes, audit.public_leaves, len(audit.leaves)), (10, 2, 2))
        expected = ("p0", "send:p0", "p1", "send:p1", "p2", "send:p2", "p3", "send:p3")
        for leaf in audit.leaves:
            self.assertEqual(tuple(a for a, _ in leaf.history), expected)
            self.assertEqual(result.policy.at(leaf.history).claim, leaf.claim)
            self.assertEqual(leaf.current.resources, (0,))
        self.assertEqual(audit.leaves[0].history[:-1], audit.leaves[1].history[:-1])
        self.assertNotEqual(audit.leaves[0].history[-1], audit.leaves[1].history[-1])

    def test_complete_observer_ablation(self):
        model = cross_enabled_model()
        values = []
        for active in ((), ("A",), ("B",), ("A", "B")):
            values.append(solve_collective_policy(restrict_observers(model, active), LADDER_BUDGET).winning)
        self.assertEqual(values, [False, False, False, True])

    def test_every_separate_ladder_budget_is_necessary(self):
        model = cross_enabled_model()
        for i in range(6):
            values = list(LADDER_BUDGET.vector)
            values[i] -= 1
            with self.subTest(coordinate=i):
                self.assertFalse(solve_collective_policy(model, Cost(*values)).winning)

    def test_no_message_no_private_result(self):
        model = cross_enabled_model()
        # Allow all four probes via their real transitions, but remove last send.
        model = replace(model, actions=tuple(a for a in model.actions if a.name != "send:p3"))
        self.assertFalse(solve_collective_policy(model, LADDER_BUDGET).winning)

    def test_counterfactual_access_is_not_performed_history(self):
        losing = capacity_parity_model(2, 1)
        self.assertFalse(solve_collective_policy(losing, Cost(4, 4, observation_bits=8, certificate=5)).winning)
        winning = capacity_parity_model(2, 2)
        result = solve_collective_policy(winning, Cost(2, 2, observation_bits=4, certificate=3))
        self.assertTrue(result.winning)
        replay_policy(winning, result.budget, result.policy)

    def test_pairwise_available_but_not_joint(self):
        model = capacity_parity_model(3, 2)
        for pair in combinations(range(3), 2):
            for _, c in model.initial:
                for i in pair:
                    row = model.actions[i].rows[c]
                    self.assertEqual(len(row), 1)
                    c = row[0].after
                self.assertTrue(all(not a.rows[c] for a in model.actions))
        self.assertFalse(solve_collective_policy(model, Cost(5, 5, observation_bits=10, certificate=6)).winning)
        full = capacity_parity_model(3, 3)
        result = solve_collective_policy(full, Cost(3, 3, observation_bits=6, certificate=4))
        self.assertTrue(result.winning)
        replay_policy(full, result.budget, result.policy)

    def test_original_source_survives_current_state_erasure(self):
        states = tuple(JointState(c, ("ready",)) for c in ("left", "right", "erased"))
        model = tiny((((Outcome("ack", 2),), (Outcome("ack", 2),), ()),
                      ((), (), (Outcome("0", 2),))), states=states)
        self.assertFalse(solve_collective_policy(model, Cost(3, 3, observation_bits=6, certificate=4)).winning)
        forged = Policy(action="a", branches=(("ack", Policy(claim="0")),))
        with self.assertRaisesRegex(CollectivePolicyError, "ORIGINAL"):
            replay_policy(model, Cost(3, 3, observation_bits=6, certificate=4), forged)

    def test_same_physical_realization_distinct_original_targets(self):
        model = tiny((((Outcome("0", 0),),),), initial=((0, 0), (1, 0)))
        self.assertFalse(solve_collective_policy(model, Cost(2, 2, observation_bits=4, certificate=3)).winning)

    def test_target_winning_does_not_require_source_identification(self):
        model = tiny((((Outcome("0", 0),), (Outcome("0", 1),)),), targets=("same-target", "same-target"))
        model = replace(model, actions=())
        result = solve_collective_policy(model, Cost(certificate=1))
        self.assertTrue(result.winning)
        audit = replay_policy(model, result.budget, result.policy)
        self.assertEqual(result.policy.claim, "same-target")
        self.assertEqual({leaf.original for leaf in audit.leaves}, {"s0", "s1"})
        self.assertEqual(audit.public_leaves, 1)

    def test_uniform_legality_forbids_free_menu_observation(self):
        model = tiny((((Outcome("0", 0),), ()), ((), (Outcome("1", 1),))))
        self.assertFalse(solve_collective_policy(model, Cost(1, 1, observation_bits=2, certificate=2)).winning)
        with self.assertRaisesRegex(CollectivePolicyError, "illegal"):
            replay_policy(model, Cost(1, 1, observation_bits=2, certificate=2), Policy(action="a", branches=(("0", Policy(claim="0")),)))

    def test_hidden_resource_stock_is_part_of_uniform_legality(self):
        states = (JointState("same", ("ready",), (0,)), JointState("same", ("ready",), (1,)))
        model = tiny((((), (Outcome("1", 0),)),), states=states)
        self.assertFalse(solve_collective_policy(model, Cost(2, 2, observation_bits=4, certificate=3)).winning)

    def test_nondeterministic_outcomes_are_and_not_or(self):
        model = tiny((((Outcome("0", 0), Outcome("retry", 0)),
                       (Outcome("1", 1), Outcome("retry", 1))),))
        self.assertFalse(solve_collective_policy(model, Cost(4, 4, observation_bits=8, certificate=5)).winning)
        lucky = Policy(action="a", branches=(("0", Policy(claim="0")), ("1", Policy(claim="1"))))
        with self.assertRaisesRegex(CollectivePolicyError, "outcome branch"):
            replay_policy(model, Cost(4, 4, observation_bits=8, certificate=5), lucky)

    def test_hidden_nondeterministic_poststates_are_not_dropped(self):
        model = tiny((((Outcome("0", 0), Outcome("0", 1)),
                       (Outcome("0", 0), Outcome("0", 1))),
                      ((Outcome("0", 0),), (Outcome("1", 1),))))
        # Action b would solve directly; make a compulsory preparation phase.
        states = tuple(JointState(str(i), ("ready",)) for i in range(4))
        mixed = tiny((((Outcome("0", 2), Outcome("0", 3)),
                       (Outcome("0", 2), Outcome("0", 3)), (), ()),
                      ((), (), (Outcome("0", 2),), (Outcome("1", 3),))), states=states)
        self.assertTrue(solve_collective_policy(model, Cost(1, 1, observation_bits=2, certificate=2)).winning)
        self.assertFalse(solve_collective_policy(mixed, Cost(2, 2, observation_bits=4, certificate=3)).winning)

    def test_public_coin_then_read_recovers_original_after_backaction(self):
        states = tuple(JointState(str(i), ("ready",)) for i in range(4))
        model = tiny((((Outcome("0", 2), Outcome("1", 3)),
                       (Outcome("0", 3), Outcome("1", 2)), (), ()),
                      ((), (), (Outcome("0", 2),), (Outcome("1", 3),))), states=states)
        result = solve_collective_policy(model, Cost(2, 2, observation_bits=4, certificate=3))
        self.assertTrue(result.winning)
        audit = replay_policy(model, result.budget, result.policy)
        self.assertEqual(len(audit.leaves), 4)
        self.assertEqual(audit.public_leaves, 4)

    def test_multiple_initial_realizations_per_source(self):
        states = tuple(JointState(str(i), ("ready",)) for i in range(3))
        model = tiny((((Outcome("0", 0),), (Outcome("1", 1),), (Outcome("1", 2),)),),
                     initial=((0, 0), (0, 2), (1, 1)), states=states)
        self.assertFalse(solve_collective_policy(model, Cost(2, 2, observation_bits=4, certificate=3)).winning)

    def test_leaf_certificate_work_is_not_policy_tree_size(self):
        model = tiny((((Outcome("0", 0),), (Outcome("1", 1),)),))
        good = solve_collective_policy(model, Cost(1, 1, observation_bits=2, certificate=2))
        replay = replay_policy(model, good.budget, good.policy)
        self.assertEqual(replay.worst_cost.certificate, 2)
        self.assertEqual(replay.policy_nodes, 3)
        self.assertFalse(solve_collective_policy(model, Cost(1, 1, observation_bits=2, certificate=1)).winning)

    def test_physical_actions_need_not_equal_decision_depth(self):
        model = tiny((((Outcome("0", 0),), (Outcome("1", 1),)),))
        model = replace(model, actions=(replace(model.actions[0], cost=Cost(1, 3, observation_bits=1, certificate=1)),))
        self.assertFalse(solve_collective_policy(model, Cost(2, 2, observation_bits=4, certificate=3)).winning)
        result = solve_collective_policy(model, Cost(1, 3, observation_bits=1, certificate=2))
        self.assertTrue(result.winning)
        self.assertEqual(replay_policy(model, result.budget, result.policy).worst_cost.actions, 3)

    def test_search_exhaustion_is_unknown_and_replay_exhaustion_is_incomplete(self):
        model = cross_enabled_model()
        with self.assertRaises(SearchLimit):
            solve_collective_policy(model, LADDER_BUDGET, max_nodes=1)
        result = solve_collective_policy(model, LADDER_BUDGET)
        with self.assertRaises(SearchLimit):
            replay_policy(model, LADDER_BUDGET, result.policy, max_prefixes=1)

    def test_replay_rejects_fictional_and_duplicate_outcomes(self):
        model = tiny((((Outcome("0", 0),), (Outcome("1", 1),)),))
        good = solve_collective_policy(model, Cost(1, 1, observation_bits=2, certificate=2)).policy
        for extra in (("fiction", Policy(claim="0")), good.branches[0]):
            with self.assertRaises(CollectivePolicyError):
                replay_policy(model, Cost(1, 1, observation_bits=2, certificate=2), replace(good, branches=good.branches + (extra,)))

    def test_table_contracts_and_cost_types(self):
        with self.assertRaises(CollectivePolicyError):
            Cost(depth=True)
        with self.assertRaises(CollectivePolicyError):
            Cost(observation_bits=-1)
        model = cross_enabled_model()
        with self.assertRaises(CollectivePolicyError):
            replace(model, initial=((0, 0),))
        with self.assertRaises(CollectivePolicyError):
            replace(model.actions[0], cost=Cost(actions=1))
        with self.assertRaises(CollectivePolicyError):
            replace(model, actions=(replace(model.actions[-1], cost=Cost(1, messages=1, certificate=1)),))

    def test_public_readouts_must_pay_observation_alphabet(self):
        model = tiny((((Outcome("0", 0),), (Outcome("1", 1),)),))
        with self.assertRaisesRegex(CollectivePolicyError, "observation alphabet"):
            replace(model, actions=(replace(model.actions[0], cost=Cost(1, 1, certificate=1)),))
        # Communication and observation bits are independent budgets.
        self.assertFalse(solve_collective_policy(model, Cost(1, 1, communication_bits=100, certificate=2)).winning)
        self.assertTrue(solve_collective_policy(model, Cost(1, 1, observation_bits=1, certificate=2)).winning)

    def test_private_readouts_cannot_be_hidden_in_local_state_updates(self):
        model = cross_enabled_model()
        p3 = next(a for a in model.actions if a.name == "p3")
        omitted = replace(p3, rows=tuple(tuple(replace(o, readout=None) for o in row) for row in p3.rows))
        with self.assertRaisesRegex(CollectivePolicyError, "undeclared readout"):
            replace(model, actions=(omitted,))
        with self.assertRaisesRegex(CollectivePolicyError, "observation alphabet"):
            replace(model, actions=(replace(p3, cost=Cost(1, 1, certificate=1)),))

    def test_message_cannot_read_hidden_carrier_or_install_hidden_recipient_state(self):
        states = (JointState("s0", ("same", "empty")), JointState("s1", ("same", "empty")),
                  JointState("s0", ("same", "got0")), JointState("s1", ("same", "got1")))
        def check(public):
            send = Action("send", "A", "message", Cost(1, messages=1, communication_bits=1),
                          ((Outcome(public[0], 2),), (Outcome(public[1], 3),), (), ()), "B")
            return CollectiveModel("s", "t", ("A", "B"), (Source("0", "0"), Source("1", "1")),
                                   states, ((0, 0), (1, 1)), (send,))
        with self.assertRaisesRegex(CollectivePolicyError, "sender local"):
            check(("0", "1"))
        with self.assertRaisesRegex(CollectivePolicyError, "receiver state"):
            check(("same", "same"))

    def test_existing_adaptive_policy_controls(self):
        from observational_succ.adaptive_proof_policy import conditional_source_field, solve_adaptive_claim
        from observational_succ.noncommuting_proof_transport import _bit_field
        for field in (_bit_field(), _bit_field(nondestructive=True), _bit_field(with_joint=True), conditional_source_field()):
            target = ("0", "1", "1", "0")
            old = solve_adaptive_claim(field, (0, 1, 2, 3), target, target_id="original-parity")
            model = tiny(tuple(tuple((Outcome(str(a.outputs[c]), a.transitions[c]),) if a.enabled[c] else ()
                                     for c in range(field.count)) for a in field.actions),
                         targets=target, initial=tuple((i, i) for i in range(field.count)))
            budget = Cost(4, 4, observation_bits=8, certificate=5)
            new = solve_collective_policy(model, budget)
            self.assertEqual(new.winning, old.winning)
            if new.winning:
                replay_policy(model, budget, new.policy)

    def test_verified_miniport_current_parent_execution(self):
        from observational_succ.consensus_lambda import MiniPort
        from observational_succ.miniature_carrier import Carrier, Mini
        from observational_succ.source_lambda import Passport
        source = "policy-mini-table"
        flip = {"0": "1", "1": "0"}
        parent = Carrier(("0", "1"), {"flip": flip}, {"0": "P0", "1": "P1"}, ("0", "1"), source)
        mini = Mini(("0", "1"), {"flip": flip}, {"0": "R0", "1": "R1"}, "0", source)
        port = MiniPort("bit", parent, mini, {"0": "0", "1": "1"}, {"flip": ("flip",)}, {"P0": "R0", "P1": "R1"})
        model, receipt = miniport_model(port, Passport(source, 0), {"0": "T0", "1": "T1"})
        self.assertTrue(receipt["factor"]["certified"])
        self.assertFalse(receipt["physical_authentication"])
        result = solve_collective_policy(model, Cost(1, 1, observation_bits=2, certificate=2))
        audit = replay_policy(model, result.budget, result.policy)
        self.assertEqual([(x.original, x.current.carrier, x.claim) for x in audit.leaves],
                         [("1", "0", "T1"), ("0", "1", "T0")])
        self.assertEqual({x.history[0][1] for x in audit.leaves}, {'["R0"]', '["R1"]'})
        with self.assertRaises(ValueError):
            miniport_model(replace(port, public_map={"P0": "R1", "P1": "R0"}), Passport(source, 0), {"0": "T0", "1": "T1"})

    def test_exhaustive_policy_tree_controls(self):
        counts = exhaustive_controls()
        self.assertEqual(counts["deterministic_two_action_models"], 2500)
        self.assertEqual(counts["nondeterministic_one_action_models"], 1024)
        self.assertEqual(counts["budget_comparisons"], 10572)
        self.assertEqual(counts["winning_comparisons"], counts["replayed_winners"])


if __name__ == "__main__":
    unittest.main()
