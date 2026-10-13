#!/usr/bin/env python3
"""Exact finite controls for A08; None denotes +infinity, never a float."""
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from observational_succ.adaptive_proof_policy import adaptive_policy_demo
from observational_succ.noncommuting_proof_transport import FiniteCarrier, Instrument
from observational_succ.proof_backaction_debt import SupportCarrier
from observational_succ.resource_probe import ValuationWord


def plus(a, b):
    return None if a is None or b is None else a + b


def le(a, b):
    return b is None or (a is not None and a <= b)


def shortest(n, edges):
    d = [[Q(0) if i == j else None for j in range(n)] for i in range(n)]
    for i, j, c in edges:
        assert isinstance(c, Q) and c >= 0
        if le(c, d[i][j]):
            d[i][j] = c
    for k, i, j in product(range(n), repeat=3):
        c = plus(d[i][k], d[k][j])
        if le(c, d[i][j]):
            d[i][j] = c
    # A distinct exhaustive simple-path implementation checks this tiny graph.
    def visit(i, j, seen):
        candidates = [Q(0)] if i == j else []
        for a, b, c in edges:
            if a == i and b not in seen:
                suffix = visit(b, j, seen | {b})
                if suffix is not None:
                    candidates.append(c + suffix)
        return min(candidates) if candidates else None
    assert all(d[i][j] == visit(i, j, {i}) for i, j in product(range(n), repeat=2))
    assert all(d[i][i] == 0 for i in range(n))
    assert all(le(d[i][k], plus(d[i][j], d[j][k]))
               for i, j, k in product(range(n), repeat=3))
    return d


def collapsed(d):
    fibers = ((0,), (1, 2), (3,))
    return [[min((d[i][j] for i in a for j in b if d[i][j] is not None),
                 default=None) for b in fibers] for a in fibers]


def main():
    # Complete states: X, Y-spent, Y-fresh, Z. Output 0 conveys no hidden state.
    field = FiniteCarrier(4, (
        Instrument("USE", (0,)*4, (1, 1, 2, 3), (True, False, False, False)),
        Instrument("RESET", (0,)*4, (0, 2, 2, 3), (False, True, False, False)),
        Instrument("FINISH", (0,)*4, (0, 1, 3, 3), (False, False, True, False)),
    ), "A08-declared-one-token-model", "resource-state-v1")
    assert field.run(0, ("USE", "RESET", "FINISH")).terminal_state == 3
    native_edges = [(i, a.transitions[i], Q(1)) for a in field.actions
                    for i in range(field.count) if a.enabled[i]]
    assert set(native_edges) == {(0, 1, Q(1)), (1, 2, Q(1)), (2, 3, Q(1))}
    rows = []
    for reset in (None, Q(0), Q(1, 2), Q(1), Q(3)):
        edges = [(0, 1, Q(1)), (2, 3, Q(1))]
        if reset is not None:
            edges.append((1, 2, reset))
        d = shortest(4, edges)
        e = shortest(4, [(i, j, c/2) for i, j, c in edges])
        assert all(le(e[i][j], d[i][j]) for i, j in product(range(4), repeat=2))
        delta = collapsed(d)
        violation = not le(delta[0][2], plus(delta[0][1], delta[1][2]))
        assert violation == (reset != Q(0))
        rows.append({"reset_cost": reset, "collapsed_XY": delta[0][1],
                     "collapsed_YZ": delta[1][2], "collapsed_XZ": delta[0][2],
                     "triangle_failure": violation, "full_triangle": True,
                     "identity_word_map_half_cost_contracts": True})
    word = ValuationWord.from_integer
    separation = [word(a).min_separating_prime_power(word(b))[2]
                  for a, b in ((8, 16), (8, 3), (3, 16))]
    assert separation == [16, 2, 2] and separation[0] > sum(separation[1:])
    carrier = SupportCarrier((0,)*32)
    debt = [carrier.debt]
    for _ in range(3):
        carrier, event = carrier.probe()
        debt.append(carrier.debt)
        assert debt[-1] == debt[-2] - 1 + event.births
    assert debt == [1, 1, 2, 4]
    policy = adaptive_policy_demo()
    assert not policy["destructive_original_parity_winning"]
    assert policy["nondestructive_worst_case"] == 2
    result = {"status": "TESTED MODEL", "arithmetic": "Fraction plus symbolic infinity",
              "reset_controls": rows, "full_triangle_triples": 320,
              "contracting_pairs": 80, "native_separation_nonmetric": separation,
              "native_support_debt": debt, "native_policy": policy,
              "universal_theorem_proved_by_finite_probe": False}
    print(json.dumps(result, default=lambda x: str(x), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
