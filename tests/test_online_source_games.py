"""Distinct strategy-enumeration oracle, raw-interface checks, hostile mutants."""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
import random
import unittest

from observational_succ.lawful_history_gluing import (
    PrivateState, SourceGraph, audit_projection, verify_uniform,
)
from observational_succ.online_source_games import (
    ControlContract, GameBudgetExceeded, GameError, Move, OneStepInterface,
    Probe, SafetyGame, belief_game, minimal_conflicts, minimum_probe_repair,
    private_resolver_game, solve_safety, verify_safety,
)


def strategy_enumeration_oracle(game):
    """No fixed-point elimination: enumerate strategies, then reachable graphs."""
    keys = [(x, r) for x in range(len(game.requests)) for r in sorted(game.requests[x])]
    options = [tuple(sorted(m.response for m in game.moves if m.position == x and m.request == r)) or (None,)
               for x, r in keys]
    rows = {(m.position, m.request, m.response): m.successors for m in game.moves}
    winners = set()
    for values in product(*options):
        strategy = dict(zip(keys, values))
        for start in range(len(game.requests)):
            pending, reached, safe = [start], set(), True
            while pending and safe:
                x = pending.pop()
                if x in reached:
                    continue
                reached.add(x)
                for r in game.requests[x]:
                    outcomes = rows.get((x, r, strategy[x, r]))
                    if outcomes is None:
                        safe = False
                        break
                    pending.extend(outcomes - reached)
            if safe:
                winners.add(start)
    return frozenset(winners)


def prophetic_graph():
    p, u, v = (PrivateState("origin", name, "y") for name in ("p", "u", "v"))
    edges = {(p, a, z) for a in ("a", "b") for z in (u, v)}
    edges |= {(u, "a", z) for z in (u, v)} | {(v, "b", z) for z in (u, v)}
    return SourceGraph((p, u, v), frozenset((p,)), frozenset(edges))


def raw_public_tree_oracle(contract, observation, initial, horizon):
    """Explicit finite public-strategy tree over complete private path records.

    No belief-game compiler, arena fixed point, or certificate checker is used.
    A safety failure has depth at most the complete belief-arena cardinality.
    """
    signals = dict(zip(contract.model.states, observation))

    def survives(paths, depth):
        if depth == 0:
            return True
        report = paths[0][-1].report
        requests = [(a, y) for before, a, y in contract.abstract_edges if before == report]
        for action, target in requests:
            successful_command = False
            for command in contract.commands:
                extended = []
                legal = True
                for path in paths:
                    outcomes = [z for x, a, c, z in contract.implementations
                                if x == path[-1] and a == action and c == command]
                    if not outcomes or any(z.report != target for z in outcomes):
                        legal = False
                        break
                    extended.extend(path + (z,) for z in outcomes)
                if not legal:
                    continue
                observations = {signals[path[-1]] for path in extended}
                if all(survives(tuple(path for path in extended if signals[path[-1]] == signal), depth - 1)
                       for signal in observations):
                    successful_command = True
                    break
            if not successful_command:
                return False
        return True

    return survives(tuple((x,) for x in initial), horizon)


class OnlineSourceGames(unittest.TestCase):
    def test_offline_lifts_but_ranked_online_loss(self):
        model = prophetic_graph()
        offline = audit_projection(model, "origin")
        self.assertTrue(verify_uniform(model, offline.certificate))
        game, states = private_resolver_game(model, "origin")
        certificate = solve_safety(game)
        self.assertEqual(certificate.winning, frozenset())
        self.assertEqual(certificate.ranks, (2, 1, 1))
        self.assertTrue(verify_safety(game, certificate))
        self.assertEqual(strategy_enumeration_oracle(game), frozenset())
        p = states[0]
        repaired = replace(model, edges=model.edges | {(p, a, p) for a in ("a", "b")})
        fixed, _ = private_resolver_game(repaired, "origin")
        repair_certificate = solve_safety(fixed)
        self.assertEqual(repair_certificate.winning, {0})
        self.assertTrue(verify_safety(fixed, repair_certificate))
        self.assertFalse(verify_safety(fixed, certificate))

    def test_rank_and_strategy_mutations_rejected(self):
        req = ("a", "y")
        game = SafetyGame((frozenset((req,)),) * 3,
                          frozenset((Move(0, req, "go", frozenset((0,))),
                                     Move(1, req, "go", frozenset((2,))))))
        cert = solve_safety(game)
        self.assertEqual(cert.winning, {0})
        self.assertEqual(cert.ranks, (0, 2, 1))
        self.assertTrue(verify_safety(game, cert))
        for mutant in (replace(cert, strategy=()), replace(cert, ranks=(0, 1, 1)),
                       replace(cert, winning=frozenset((0, 1))),
                       replace(cert, counteroutcomes=((1, req, "go", 0),)),
                       replace(cert, spoilers=()),
                       replace(cert, strategy=((False, req, "go"),))):
            self.assertFalse(verify_safety(game, mutant))

    def test_adversarial_outcomes_and_vacuous_terminal_boundary(self):
        req = ("a", "y")
        game = SafetyGame((frozenset((req,)), frozenset((req,)), frozenset()),
                          frozenset((Move(0, req, "risky", frozenset((1, 2))),)))
        cert = solve_safety(game)
        self.assertEqual(cert.winning, {2})
        self.assertEqual(cert.ranks, (2, 1, 0))
        self.assertTrue(verify_safety(game, cert))
        with self.assertRaises(GameError):
            SafetyGame((frozenset((req,)),), frozenset((Move(0, req, "ghost", frozenset()),)))
        with self.assertRaises(GameError):
            SafetyGame((frozenset((req,)),), frozenset((Move(True, req, "bad", frozenset((0,))),)))

    def test_all_256_two_state_two_command_arenas_against_strategy_oracle(self):
        request = ("request", "report")
        outcomes = (frozenset(), frozenset((0,)), frozenset((1,)), frozenset((0, 1)))
        keys = tuple(product(range(2), ("left", "right")))
        count = 0
        for selected in product(outcomes, repeat=4):
            game = SafetyGame((frozenset((request,)),) * 2,
                              frozenset(Move(x, request, c, targets)
                                        for (x, c), targets in zip(keys, selected) if targets))
            cert = solve_safety(game)
            self.assertTrue(verify_safety(game, cert))
            self.assertEqual(cert.winning, strategy_enumeration_oracle(game))
            count += 1
        self.assertEqual(count, 256)

    def test_fresh_three_state_two_request_random_arenas(self):
        rng = random.Random(2026101902)
        requests = ("a", "y"), ("b", "z")
        for _ in range(60):
            moves = []
            for x, r, c in product(range(3), requests, ("c0", "c1")):
                outcomes = frozenset(z for z in range(3) if rng.randrange(4) == 0)
                if outcomes:
                    moves.append(Move(x, r, c, outcomes))
            game = SafetyGame((frozenset(requests),) * 3, frozenset(moves))
            cert = solve_safety(game)
            self.assertTrue(verify_safety(game, cert))
            self.assertEqual(cert.winning, strategy_enumeration_oracle(game))

    def test_public_command_interface_changes_winner_with_same_private_edges(self):
        zero, one = (PrivateState("s", name, "unknown") for name in ("zero", "one"))
        done = PrivateState("s", "done", "done")
        model = SourceGraph((zero, one, done), frozenset((zero, one)),
                            frozenset(((zero, "serve", done), (one, "serve", done))))
        abstract = frozenset((("unknown", "serve", "done"),))
        split = ControlContract(model, abstract, frozenset(("left", "right")),
                                frozenset(((zero, "serve", "left", done), (one, "serve", "right", done))))
        common = ControlContract(model, abstract, frozenset(("serve",)),
                                 frozenset(((zero, "serve", "serve", done), (one, "serve", "serve", done))))
        observation = ("unknown", "unknown", "done")
        for contract, expected in ((split, False), (common, True)):
            game, beliefs = belief_game(contract, observation)
            cert = solve_safety(game)
            self.assertTrue(verify_safety(game, cert))
            self.assertEqual(beliefs.index(frozenset((zero, one))) in cert.winning, expected)
            self.assertEqual(cert.winning, strategy_enumeration_oracle(game))
        # A declared truthful state probe repairs the information obstruction.
        full, beliefs = belief_game(split, ("zero", "one", "done"))
        self.assertEqual(solve_safety(full).winning, frozenset(range(3)))
        # Original identity is not automatically public: these states share it.
        self.assertEqual(zero.source, one.source)

    def test_256_public_command_tables_against_raw_private_path_tree(self):
        states = tuple(PrivateState("s", str(i), "y") for i in range(2))
        outcomes = ((), (states[0],), (states[1],), states)
        for selected in product(outcomes, repeat=4):
            implementations = frozenset((x, "a", command, z)
                                        for (x, command), targets in zip(product(states, ("c0", "c1")), selected)
                                        for z in targets)
            model = SourceGraph(states, frozenset(states),
                                frozenset((x, a, z) for x, a, _, z in implementations))
            contract = ControlContract(model, frozenset((("y", "a", "y"),)),
                                       frozenset(("c0", "c1")), implementations)
            arena, beliefs = belief_game(contract, ("y", "y"))
            cert = solve_safety(arena)
            for i, belief in enumerate(beliefs):
                expected = raw_public_tree_oracle(contract, ("y", "y"), belief, len(beliefs))
                self.assertEqual(i in cert.winning, expected)

    def test_target_report_conditioning_cannot_hide_bad_outcomes(self):
        start = PrivateState("s", "start", "ready")
        good, bad = PrivateState("s", "good", "good"), PrivateState("s", "bad", "bad")
        model = SourceGraph((start, good, bad), frozenset((start,)),
                            frozenset(((start, "a", good), (start, "a", bad))))
        contract = ControlContract(model, frozenset((("ready", "a", "good"),)), frozenset(("coin",)),
                                   frozenset(((start, "a", "coin", good), (start, "a", "coin", bad))))
        game, beliefs = belief_game(contract, ("ready", "good", "bad"))
        self.assertNotIn(beliefs.index(frozenset((start,))), solve_safety(game).winning)
        self.assertEqual(tuple(m for m in game.moves if m.position == beliefs.index(frozenset((start,)))), ())

    def test_structural_online_loss_survives_every_state_probe(self):
        model = prophetic_graph()
        # A public command naming its destination may request only an actual edge.
        commands = frozenset(x.name for x in model.states)
        contract = ControlContract(model, model.projected_edges("origin"), commands,
                                   frozenset((x, a, z.name, z) for x, a, z in model.edges))
        # Full private state observation is already insufficient.
        full, beliefs = belief_game(contract, tuple(x.name for x in model.states))
        self.assertEqual(solve_safety(full).winning, frozenset())
        public, _ = belief_game(contract, ("y", "y", "y"))
        self.assertEqual(solve_safety(public).winning, frozenset())

    def test_belief_memory_strictly_improves_current_report_control(self):
        # The initial signal selects an origin; advance erases that signal.
        p0, p1 = PrivateState("0", "p", "start0"), PrivateState("1", "p", "start1")
        u0, u1 = PrivateState("0", "u", "middle"), PrivateState("1", "u", "middle")
        d0, d1 = PrivateState("0", "d", "done"), PrivateState("1", "d", "done")
        edges = frozenset(((p0, "advance", u0), (p1, "advance", u1),
                           (u0, "finish", d0), (u1, "finish", d1)))
        model = SourceGraph((p0, p1, u0, u1, d0, d1), frozenset((p0, p1)), edges)
        abstract = frozenset((x.report, a, z.report) for x, a, z in edges)
        commands = frozenset(("go", "left", "right"))
        implementations = frozenset(((p0, "advance", "go", u0), (p1, "advance", "go", u1),
                                      (u0, "finish", "left", d0), (u1, "finish", "right", d1)))
        contract = ControlContract(model, abstract, commands, implementations)
        game, beliefs = belief_game(contract, tuple(x.report for x in model.states))
        cert = solve_safety(game)
        for x in (p0, p1, u0, u1):
            self.assertIn(beliefs.index(frozenset((x,))), cert.winning)
        self.assertNotIn(beliefs.index(frozenset((u0, u1))), cert.winning)
        # A controller seeing only the current middle report must pick the
        # same command; retained start history permits different beliefs.
        self.assertFalse(any(all(any(x == u and a == "finish" and c == command
                                     for x, a, c, _ in implementations) for u in (u0, u1))
                             for command in commands))

    def test_higher_order_probe_conflict_and_exact_minimum_cost(self):
        interface = OneStepInterface((frozenset(("a", "b")), frozenset(("b", "c")), frozenset(("a", "c"))))
        self.assertTrue(all(interface.enabled[i] & interface.enabled[j] for i in range(3) for j in range(i)))
        self.assertEqual(minimal_conflicts(interface), (frozenset((0, 1, 2)),))
        probes = (Probe("constant", ("0", "0", "0"), Q(0)),
                  Probe("cheap", ("0", "0", "1"), Q(2, 3)),
                  Probe("expensive", ("0", "1", "1"), Q(3, 2)))
        cost, choices = minimum_probe_repair(interface, probes)
        self.assertEqual(cost, Q(2, 3))
        self.assertEqual(set(choices), {frozenset((1,)), frozenset((0, 1))})
        # Independent raw observation-block command intersection verifies all bundles.
        raw = []
        for bits in product((False, True), repeat=len(probes)):
            selected = tuple(i for i, bit in enumerate(bits) if bit)
            blocks = {}
            for x in range(3):
                blocks.setdefault(tuple(probes[i].outputs[x] for i in selected), []).append(x)
            if all(set.intersection(*(set(interface.enabled[x]) for x in block)) for block in blocks.values()):
                raw.append((sum((probes[i].cost for i in selected), Q()), frozenset(selected)))
        self.assertEqual(cost, min(value for value, _ in raw))
        self.assertEqual(set(choices), {subset for value, subset in raw if value == cost})
        # Two incomparable adequate observations have only a constant common
        # coarsening, which is inadequate. There is no coarsest safe repair.
        first, second = (0, 0, 1), (0, 1, 1)
        def adequate(labels):
            return all(set.intersection(*(set(interface.enabled[i]) for i in range(3) if labels[i] == label))
                       for label in set(labels))
        self.assertTrue(adequate(first) and adequate(second))
        self.assertFalse(adequate((0, 0, 0)))
        common_coarsenings = [labels for labels in product(range(3), repeat=3)
                             if all((first[i] != first[j] and second[i] != second[j]) or labels[i] == labels[j]
                                    for i in range(3) for j in range(3))]
        self.assertTrue(all(len(set(labels)) == 1 for labels in common_coarsenings))

    def test_probe_menu_no_go_and_budget_failures_are_not_losses(self):
        interface = OneStepInterface((frozenset(("a",)), frozenset(("b",))))
        self.assertEqual(minimum_probe_repair(interface, (Probe("blind", ("0", "0"), 0),)), (None, ()))
        structurally_dead = OneStepInterface((frozenset(), frozenset(("a",))))
        self.assertEqual(minimum_probe_repair(structurally_dead, (Probe("perfect", ("0", "1"), 1),)), (None, ()))
        with self.assertRaises(GameBudgetExceeded):
            minimum_probe_repair(interface, (), max_subsets=2)
        model = prophetic_graph()
        contract = ControlContract(model, model.projected_edges("origin"), frozenset(), frozenset())
        with self.assertRaises(GameBudgetExceeded):
            belief_game(contract, ("y", "y", "y"), max_beliefs=6)
        with self.assertRaises(GameError):
            Probe("float", ("x",), 0.1)


if __name__ == "__main__":
    unittest.main()
