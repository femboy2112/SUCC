#!/usr/bin/env python3
"""Independent bounded audits and exact policy-transport controls for SWM-X05.

The binary garbling oracle uses a closed formula, and the policy oracle enumerates
complete report trees and replays original states without normalized beliefs.
Finite probes support, but do not prove, the general paper theorem in X05.md.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.swarm_probability import (  # only audit subjects
    Experiment, SearchBudgetError, StochasticHistory, StochasticInstrument,
    find_garbling, optimal_zero_error_cost,
)


def binary_formula(p, q, r, s):
    """Independent EG=F feasibility: p,q and r,s are first-report probabilities."""
    if p == q:
        return r == s
    difference = (r-s)/(p-q)
    v = r-p*difference
    u = v+difference
    return 0 <= u <= 1 and 0 <= v <= 1


def audit_garbling():
    grid = tuple(Q(n, 4) for n in range(5))
    count = feasible = 0
    for p, q, r, s in product(grid, repeat=4):
        more = Experiment('X05', ((p, 1-p), (q, 1-q)))
        less = Experiment('X05', ((r, 1-r), (s, 1-s)))
        expected = binary_formula(p, q, r, s)
        answer = find_garbling(more, less)
        assert (answer is not None) == expected, (p, q, r, s)
        if answer is not None:
            # Do not reuse the subject's garbling_verifies routine.
            assert all(v >= 0 for row in answer for v in row)
            assert all(sum(row) == 1 for row in answer)
            assert all(sum(more.rows[o][a]*answer[a][b] for a in range(2))
                       == less.rows[o][b] for o, b in product(range(2), repeat=2))
        count += 1
        feasible += expected
    e = Experiment('X05', ((Q(1, 2), Q(1, 2)),))
    try:
        find_garbling(e, e, max_bases=1)
    except SearchBudgetError:
        pass
    else:
        raise AssertionError('Budget exhaustion was confused with a verdict')
    return {'binary_pairs': count, 'feasible': feasible, 'budget_fails_closed': True}


def trees(depth, actions):
    """Every binary-report deterministic tree, including early target guesses."""
    result = [(None, 0), (None, 1)]
    if depth:
        smaller = trees(depth-1, actions)
        result.extend((a, left, right) for a in range(actions)
                      for left in smaller for right in smaller)
    return result


def replay_tree(tree, current, original, rows, costs):
    """Unnormalized original-path enumeration; return (error probability, cost)."""
    if tree[0] is None:
        return Q(int(tree[1] != original)), Q(0)
    a = tree[0]
    bad, cost = Q(0), Q(costs[a])
    for report, after, probability in rows[a][current]:
        child_bad, child_cost = replay_tree(tree[report+1], after, original, rows, costs)
        bad += probability*child_bad
        cost += probability*child_cost
    return bad, cost


def brute_policy(rows, costs, prior, depth):
    best = None
    for tree in trees(depth, len(rows)):
        bad = cost = Q(0)
        for original, weight in enumerate(prior):
            b, c = replay_tree(tree, original, original, rows, costs)
            bad += weight*b
            cost += weight*c
        if bad == 0 and (best is None or cost < best):
            best = cost
    return best


def audit_policies():
    # All 16 deterministic two-state, binary-report, source-changing actions.
    actions = tuple(tuple(((r, y, Q(1)),) for r, y in rows)
                    for rows in product(tuple(product(range(2), repeat=2)), repeat=2))
    priors = ((Q(1, 2), Q(1, 2)), (Q(1, 3), Q(2, 3)))
    checks = 0
    for first, second in product(actions, repeat=2):
        rows = (first, second)
        instruments = tuple(StochasticInstrument(str(a), 'X05', 'x', 'x', 2,
                                                 row, Q(a+1))
                            for a, row in enumerate(rows))
        for prior in priors:
            root = StochasticHistory.original('X05', 'x', prior)
            for depth in range(3):
                expected = brute_policy(rows, (1, 2), prior, depth)
                actual = optimal_zero_error_cost(root, instruments, (0, 1), depth).cost
                assert actual == expected, (rows, prior, depth, actual, expected)
                checks += 1
    # Full-support noise plus a costly certain read tests genuinely stochastic paths.
    noise = (((0, 0, Q(3, 4)), (1, 0, Q(1, 4))),
             ((0, 1, Q(1, 4)), (1, 1, Q(3, 4))))
    certain = (((0, 0, Q(1)),), ((1, 1, Q(1)),))
    for rows in ((noise, certain), (noise, noise)):
        instruments = tuple(StochasticInstrument(str(a), 'X05', 'x', 'x', 2,
                                                 row, Q(a+1))
                            for a, row in enumerate(rows))
        for prior in priors:
            root = StochasticHistory.original('X05', 'x', prior)
            for depth in range(3):
                expected = brute_policy(rows, (1, 2), prior, depth)
                actual = optimal_zero_error_cost(root, instruments, (0, 1), depth).cost
                assert actual == expected
                checks += 1
    return {'deterministic_action_pairs': 256, 'policy_comparisons': checks,
            'complete_depth2_trees_per_model': len(trees(2, 2))}


def simulation_square(actual, virtual, transport, garblings, actual_enabled,
                      virtual_enabled, actual_cost, virtual_cost):
    """Check the sufficient one-way theorem's finite contract, not necessity.

    Instruments are sparse normalized rows (report,next,weight). The simulator
    G sees only actual report; T is a proof-level carrier kernel, never an oracle.
    Input fixtures are exact normalized kernels with finite integer labels.
    """
    nx, ny = len(transport), len(transport[0])
    for a in range(len(actual)):
        if actual_cost[a] > virtual_cost[a]:
            return False
        for x in range(nx):
            if any(transport[x][y] and y not in virtual_enabled[a] for y in range(ny)):
                continue
            if x not in actual_enabled[a]:
                return False
            for beta in range(len(garblings[a][0])):
                for end in range(ny):
                    lhs = sum(weight*garblings[a][alpha][beta]*transport[z][end]
                              for alpha, z, weight in actual[a][x])
                    rhs = sum(transport[x][y]*weight
                              for y in range(ny)
                              for report, z, weight in virtual[a][y]
                              if report == beta and z == end)
                    if lhs != rhs:
                        return False
    return True


def push(joint, transport):
    return tuple(tuple(sum(row[x]*transport[x][y] for x in range(len(row)))
                       for y in range(len(transport[0]))) for row in joint)


def branch(joint, instrument, report, garbling=None):
    after_count = max(z for row in instrument for _, z, _ in row)+1
    result = [[Q(0)]*after_count for _ in joint]
    for original, row in enumerate(joint):
        for x, weight in enumerate(row):
            for alpha, z, probability in instrument[x]:
                g = garbling[alpha][report] if garbling is not None else Q(alpha == report)
                result[original][z] += weight*probability*g
    return tuple(tuple(row) for row in result)


def transport_fixture():
    # Actual x is a visible bit. Virtual y=(visible bit, independent hidden bit).
    # T is genuinely stochastic. Virtual hidden bit is refreshed by every action.
    transport = ((Q(1, 2), Q(1, 2), Q(0), Q(0)),
                 (Q(0), Q(0), Q(1, 2), Q(1, 2)))
    actual = tuple(tuple(((x, x ^ a, Q(1)),) for x in range(2)) for a in range(2))
    g = (((Q(3, 4), Q(1, 4)), (Q(1, 4), Q(3, 4))),
         ((Q(1), Q(0)), (Q(0), Q(1))))
    virtual = tuple(tuple(tuple((beta, 2*((y//2) ^ a)+hidden, g[a][y//2][beta]/2)
                                for beta, hidden in product(range(2), repeat=2)
                                if g[a][y//2][beta])
                          for y in range(4)) for a in range(2))
    return actual, virtual, transport, g


def audit_transport():
    actual, virtual, transport, g = transport_fixture()
    full_x = (frozenset(range(2)),)*2
    full_y = (frozenset(range(4)),)*2
    assert simulation_square(actual, virtual, transport, g, full_x, full_y, (1, 2), (2, 2))
    initial = ((Q(1, 3), Q(0)), (Q(0), Q(2, 3)))
    pending = [((), initial, push(initial, transport))]
    checked = 0
    while pending:
        history, jx, jy = pending.pop()
        assert push(jx, transport) == jy
        assert tuple(map(sum, jx)) == tuple(map(sum, jy))
        checked += 1
        if len(history) == 4:
            continue
        a = 0 if not history else history[-1]  # genuinely report-dependent choice
        for beta in range(2):
            cx, cy = branch(jx, actual[a], beta, g[a]), branch(jy, virtual[a], beta)
            if sum(map(sum, cx)):
                pending.append((history+(beta,), cx, cy))
    # Three independently missing hypotheses fail their actual contract.
    assert not simulation_square(actual, virtual, transport, g,
                                 (frozenset({0}), full_x[1]), full_y, (1, 2), (2, 2))
    assert not simulation_square(actual, virtual, transport, g, full_x, full_y, (3, 2), (2, 2))
    bad_virtual = list(virtual)
    bad_virtual[0] = tuple(((0, 0, Q(1)),) for _ in range(4))
    assert not simulation_square(actual, tuple(bad_virtual), transport, g,
                                 full_x, full_y, (1, 2), (2, 2))
    return {'positive_history_nodes_depth4': checked, 'stochastic_transport': True,
            'availability_cost_backaction_mutations_rejected': 3}


def audit_minimal_counterexample():
    # Both first steps emit the sole constant report 0; one preserves and one erases.
    preserve = (((0, 0, Q(1)),), ((0, 1, Q(1)),))
    erase = (((0, 0, Q(1)),), ((0, 0, Q(1)),))
    read = (((0, 0, Q(1)),), ((1, 1, Q(1)),))
    prior = ((Q(1, 2), Q(0)), (Q(0), Q(1, 2)))
    good, bad = branch(prior, preserve, 0), branch(prior, erase, 0)
    assert tuple(map(sum, good)) == tuple(map(sum, bad)) == (Q(1, 2), Q(1, 2))
    good_read, bad_read = branch(good, read, 0), branch(bad, read, 0)
    assert tuple(map(sum, good_read)) == (Q(1, 2), Q(0))
    assert tuple(map(sum, bad_read)) == (Q(1, 2), Q(1, 2))
    return {'original_states': 2, 'first_report_alphabet': 1,
            'good_continuation_cost': 1, 'erased_continuation': 'impossible at every horizon'}


def receipt():
    root = Path(__file__).resolve().parents[1]
    return {'assignment': 'X05', 'base_commit': '508f16881a4b145dffa13d0d3d336d1abcbda98c',
            'status': 'PROVED LOCAL (paper theorem); exact finite audit controls',
            'garbling': audit_garbling(), 'policies': audit_policies(),
            'transport': audit_transport(), 'minimal_counterexample': audit_minimal_counterexample(),
            'audited_module_sha256': hashlib.sha256((root/'observational_succ/swarm_probability.py').read_bytes()).hexdigest()}


if __name__ == '__main__':
    print(json.dumps(receipt(), indent=2))
