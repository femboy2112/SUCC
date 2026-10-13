#!/usr/bin/env python3
"""Independent X12 finite controls. General statements have written proofs.

No F-cohort replay, quotient, or algebra helper is used as the oracle. The F
implementation is imported only as the system under test in two audit routines.
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def independent_replay(initial, actions, history):
    answer = {}
    for original, prepared in enumerate(initial):
        current = prepared
        for name, report in history:
            after, outcome, enabled, _cost = actions[name]
            if not enabled[current] or outcome[current] != report:
                break
            current = after[current]
        else:
            answer[original] = current
    return answer


def audit_f48():
    from observational_succ.swarm_lawful_history import (
        Event, HistoryError, Instrument, LawfulSource, quotient_source, replay_fiber)

    words = [word for length in range(4)
             for word in product((("a", 0), ("a", 1)), repeat=length)]
    checked, accepted, rejected = 0, 0, 0
    for after, report, enabled in product(product(range(2), repeat=2),
                                         product(range(2), repeat=2),
                                         product((False, True), repeat=2)):
        actions = {"a": (after, report, enabled, (0, 0))}
        source = LawfulSource("X12-exhaustive", (0, 1),
                              (Instrument("a", after, report, enabled),))
        for labels in ((0, 1), (0, 0)):
            # Check the universal squares directly, without the implementation.
            valid = all(labels[i] != labels[j] or
                        (enabled[i] == enabled[j] and report[i] == report[j]
                         and labels[after[i]] == labels[after[j]])
                        for i in range(2) for j in range(2))
            try:
                coarse = quotient_source(source, labels)
            except HistoryError:
                assert not valid
                rejected += 1
                continue
            assert valid
            accepted += 1
            for history in words:
                expected = independent_replay((0, 1), actions, history)
                actual = dict(replay_fiber(source, tuple(Event(*e) for e in history)).configurations)
                descended = dict(replay_fiber(coarse, tuple(Event(*e) for e in history)).configurations)
                assert actual == expected
                assert descended == {o: labels[c] for o, c in expected.items()}
                checked += 1
    return {"two_state_one_instrument_sources": 64,
            "accepted_quotients": accepted, "rejected_quotients": rejected,
            "history_comparisons_including_impossible_histories": checked}


def independent_group(generators):
    identity = tuple(range(len(generators[0])))
    elements, queue = {identity}, deque([identity])
    # Ordinary functional composition g o f; explicit and independent code.
    def multiply(g, f):
        return tuple(g[f[x]] for x in range(len(f)))
    while queue:
        element = queue.popleft()
        for generator in generators:
            candidate = multiply(generator, element)
            if candidate not in elements:
                elements.add(candidate)
                queue.append(candidate)
    assert all(set(g) == set(identity) for g in elements)
    center = {g for g in elements if all(multiply(g, h) == multiply(h, g)
                                        for h in generators)}
    a, b = generators
    inverse_a = tuple(a.index(x) for x in identity)
    inverse_b = tuple(b.index(x) for x in identity)
    commutator = multiply(inverse_b, multiply(inverse_a, multiply(b, a)))
    return len(elements), len(center), commutator in center


def audit_f43():
    from observational_succ.swarm_discovery import TableSource, discover_quotient

    records = []
    for p, coupling in ((2, 1), (5, 1), (2, 0), (5, 0)):
        # Own lexicographic producer, unrelated to cohort's shuffled producer.
        states = tuple(product(range(p), repeat=3))
        index = {s: i for i, s in enumerate(states)}
        a = tuple(index[((x + 1) % p, y, (z + coupling*y) % p)] for x, y, z in states)
        b = tuple(index[(x, (y + 1) % p, z)] for x, y, z in states)
        source = TableSource(f"X12-H-{p}-{coupling}", (("a", a), ("b", b)),
                             (tuple(z for _, _, z in states),))
        learned = discover_quotient(source)
        # Closed-form independent oracle: z and z-after-a recover y for lambda=1.
        expected = tuple((y, z) if coupling else (z,) for _, y, z in states)
        assert all((learned.labels[i] == learned.labels[j]) == (expected[i] == expected[j])
                   for i in range(len(states)) for j in range(len(states)))
        carriers = tuple(product(range(p), repeat=2)) if coupling else tuple((z,) for z in range(p))
        lookup = {s: i for i, s in enumerate(carriers)}
        if coupling:
            g_a = tuple(lookup[(y, (z + y) % p)] for y, z in carriers)
            g_b = tuple(lookup[((y + 1) % p, z)] for y, z in carriers)
        else:
            g_a = g_b = tuple(range(p))
        size, center, central = independent_group((g_a, g_b))
        assert size == (p**3 if coupling else 1)
        assert center == (p if coupling else 1)
        records.append({"p": p, "coupling": coupling, "minimal_states": learned.count,
                        "group_size": size, "center_size": center,
                        "central_commutator": central})
    rotate, reflect = tuple((x + 1) % 5 for x in range(5)), tuple(-x % 5 for x in range(5))
    source = TableSource("X12-D5", (("a", rotate), ("b", reflect)),
                         ((1, 0, 0, 0, 0),))
    assert discover_quotient(source).count == 5
    assert independent_group((rotate, reflect)) == (10, 1, False)
    return {"family_controls": records, "dihedral": [10, 1, False],
            "complete_tables_and_group_predicates_supplied": True,
            "unbiased_external_holdout_claim": False}


def local_quotient_node(configurations, history):
    # Current state is 4*visible + two hidden bits. After a nonempty lawful event its
    # visible bit is recoverable from the history, so one point suffices locally.
    return {c: c // 4 if not history else 0 for c in set(configurations.values())}


def dynamic_bridge():
    initial = tuple(range(8))
    actions = {
        "flip": (tuple(c ^ 4 for c in initial), tuple(c // 4 for c in initial), (True,)*8, tuple(1 + c // 4 for c in initial)),
        "erase": (tuple(c % 4 for c in initial), ("done",)*8, (True,)*8, (2,)*8),
        "one": (initial, ("ok",)*8, tuple(c >= 4 for c in initial), (3,)*8),
    }
    source_nodes = {(): dict(enumerate(initial))}
    coarse_nodes = {(): {o: c // 4 for o, c in enumerate(initial)}}
    edge_checks = local_square_checks = robust_action_checks = 0
    for length in range(5):
        for history in tuple(h for h in source_nodes if len(h) == length):
            original = source_nodes[history]
            coarse = coarse_nodes[history]
            q = local_quotient_node(original, history)
            assert coarse == {o: q[c] for o, c in original.items()}
            for action, (after, report, enabled, cost) in actions.items():
                # Descend from representatives; verify every member, including guards/cost.
                representatives = {q[c]: c for c in original.values()}
                descent = {d: (enabled[c], report[c], cost[c]) for d, c in representatives.items()}
                for c in original.values():
                    assert descent[q[c]] == (enabled[c], report[c], cost[c])
                assert all(enabled[c] for c in original.values()) == all(descent[d][0] for d in coarse.values())
                robust_action_checks += 1
                if length == 4:
                    continue
                for outcome in set(report[c] for c in original.values() if enabled[c]):
                    child = history + ((action, outcome),)
                    direct = independent_replay(initial, actions, child)
                    q_child = local_quotient_node(direct, child)
                    transition = {}
                    for c in original.values():
                        if enabled[c] and report[c] == outcome:
                            value = q_child[after[c]]
                            if q[c] in transition:
                                assert transition[q[c]] == value
                            transition[q[c]] = value
                            local_square_checks += 1
                    evolved = {o: transition[d] for o, d in coarse.items()
                               if descent[d][0] and descent[d][1] == outcome}
                    assert evolved == {o: q_child[c] for o, c in direct.items()}
                    source_nodes[child], coarse_nodes[child] = direct, evolved
                    edge_checks += 1
    # Two genuinely noninjective representation maps: discard one hidden bit,
    # then the other. After a report, the second map also discards the visible
    # bit known from history. The intermediate carrier still keeps a hidden bit.
    composition_checks = 0
    for h, original in source_nodes.items():
        first = {c: c // 2 for c in set(original.values())}
        second = {d: d // 2 if not h else 0 for d in set(first.values())}
        direct_composite = {o: second[first[c]] for o, c in original.items()}
        assert direct_composite == coarse_nodes[h]
        assert len(first) > len(set(first.values()))
        for action, (after, report, enabled, cost) in actions.items():
            for left in original.values():
                for right in original.values():
                    if first[left] == first[right]:
                        assert enabled[left] == enabled[right]
                        assert report[left] == report[right]
                        assert cost[left] == cost[right]
                        assert after[left] // 2 == after[right] // 2
        composition_checks += 1
    # Original-target support is retained despite one-point current representations.
    revealed = source_nodes[(("flip", 1),)]
    assert set(revealed) == {4, 5, 6, 7}
    assert {o // 4 for o in revealed} == {1}
    assert {o % 2 for o in revealed} == {0, 1}
    erased = source_nodes[(("erase", "done"),)]
    assert set(erased) == set(range(8))
    assert len(set(coarse_nodes[(("erase", "done"),)].values())) == 1
    # Known policy flip then stop for original visible bit; exact branch costs agree.
    for o, c in enumerate(initial):
        assert actions["flip"][3][c] == (1 if coarse_nodes[()][o] == 0 else 2)
    return {"lawful_nodes_through_depth_4": len(source_nodes), "edges": edge_checks,
            "pointwise_cross_stage_squares": local_square_checks,
            "robust_availability_comparisons": robust_action_checks,
            "composite_representation_comparisons": composition_checks,
            "visible_target_support_after_flip_1": sorted(revealed),
            "hidden_target_remains_ambiguous": True,
            "erase_support_retained": sorted(erased)}


def boundary_controls():
    # Two individually valid static quotients for an identity, constant-report source.
    old, new, identity = (0, 0), (0, 1), (0, 1)
    assert all(old[identity[c]] == old[c] for c in range(2))
    assert all(new[identity[c]] == new[c] for c in range(2))
    possible_cross_maps = [(v,) for v in range(2)]
    assert not any(all(candidate[old[c]] == new[identity[c]] for c in range(2))
                   for candidate in possible_cross_maps)
    # Same fibers, same current map, changed target: certifying T0 does not certify T1.
    support = {0, 1}
    old_target, new_target = (0, 0), (0, 1)
    assert len({old_target[o] for o in support}) == 1
    assert len({new_target[o] for o in support}) == 2
    # A target factors through a compressed original index iff it is constant on its fibers.
    original_compression = (0, 0)
    assert any(original_compression[i] == original_compression[j] and new_target[i] != new_target[j]
               for i in support for j in support)
    # Report preservation alone says nothing about guards or numerical costs.
    guard, original_cost, coarse_cost = (False, True), (Fraction(1), Fraction(2)), Fraction(1)
    assert len(set(guard)) == 2 and any(c != coarse_cost for c in original_cost)
    return {"static_quotients_without_cross_stage_square": "REFUTED",
            "preservation_under_unannounced_target_change": "REFUTED",
            "original_index_compression_without_target_factor": "REFUTED",
            "report_only_policy_and_cost_preservation": "REFUTED",
            "source_dependent_schedule_as_free_observation": "NOT_AUTHORIZED_BY_THE_MODEL"}


def main():
    result = {
        "schema": "succ-swm-x12-v1",
        "base_commit": "216651461e182c2a9ded1796c34485e2e34a29e3",
        "status": "PROVED_LOCAL_WRITTEN; FINITE_CONTROLS_EXECUTED",
        "f48_independent_audit": audit_f48(),
        "f43_independent_audit": audit_f43(),
        "history_indexed_bridge": dynamic_bridge(),
        "boundaries": boundary_controls(),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "kernel_checked": False,
        "human_psychology_claim": False,
        "academic_novelty_verified": False,
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
