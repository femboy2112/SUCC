#!/usr/bin/env python3
"""Exact finite controls for D2. Universal statements have paper proofs."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import prod
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.observatoris_response_geometry import (  # noqa: E402
    matrix, powers, switching_function,
)


def tv(p, q):
    assert len(p) == len(q)
    return sum(abs(x - y) for x, y in zip(p, q)) / Q(2)


def dot(p, q):
    return sum(x * y for x, y in zip(p, q))


def aggregate(p, labels):
    return tuple(sum(p[x] for x in range(len(p)) if labels[x] == y)
                 for y in range(max(labels) + 1))


def push(p, rows):
    return tuple(dot(p, column) for column in zip(*rows))


def dual_certificate(rows, allowed, center, alpha, radius):
    assert sum(center) == 1 and min(center) >= 0
    assert all(i in allowed or not center[i] for i in range(len(center)))
    assert sum(weight for _, _, weight in alpha) == 1
    assert all(weight >= 0 for _, _, weight in alpha)
    upper = max(tv(row, center) for row in rows)
    event_value = sum(weight * sum(rows[x][j] for j in event)
                      for x, event, weight in alpha)
    charge = max(sum(weight for _, event, weight in alpha if j in event)
                 for j in allowed)
    assert upper == event_value - charge == radius


def stochastic_controls():
    rows = ((Q(3, 4), 0, Q(1, 4)), (0, Q(3, 4), Q(1, 4)))
    dual_certificate(rows, {0, 1}, (Q(1, 2), Q(1, 2), 0),
                     ((0, {0, 2}, Q(1, 2)), (1, {1, 2}, Q(1, 2))), Q(1, 2))
    assert max(row[2] for row in rows) == Q(1, 4)
    assert tv(*rows) / 2 == Q(3, 8)
    delta = tuple(tuple(int(i == j) for j in range(3)) for i in range(3))
    dual_certificate(delta, {0, 1, 2}, (Q(1, 3),) * 3,
                     tuple((j, {j}, Q(1, 3)) for j in range(3)), Q(2, 3))
    bernoulli = ((Q(1, 4), Q(3, 4)), (Q(3, 4), Q(1, 4)))
    dual_certificate(bernoulli, {0, 1}, (Q(1, 2), Q(1, 2)),
                     ((0, {1}, Q(1, 2)), (1, {0}, Q(1, 2))), Q(1, 4))
    for perm in permutations(range(3)):
        for row in rows:
            reordered = tuple(row[i] for i in perm)
            center = tuple((Q(1, 2), Q(1, 2), 0)[i] for i in perm)
            assert tv(reordered, center) == Q(1, 2)
    return {"mask_radius": "1/2", "excluded_mass": "1/4",
            "diameter_half": "3/8", "three_point_radius": "2/3",
            "identical_support_bernoulli_radius": "1/4"}


def deterministic_controls():
    count = exact = 0
    witnessed_noncongruence = False
    labels = (0, 0, 1)
    for left, right in product(product(range(3), repeat=3), repeat=2):
        actions = (left, right)
        induced = [tuple(labels[t[x]] for x in (0, 2)) for t in actions]
        descends = all(labels[t[0]] == labels[t[1]] for t in actions)
        congruent = all(labels[t[x]] == b[labels[x]] for t, b in zip(actions, induced)
                        for x in range(3))
        assert congruent == descends
        if congruent:
            for word in product(range(2), repeat=3):
                for x in range(3):
                    sx, sy = x, labels[x]
                    for a in word:
                        sx, sy = actions[a][sx], induced[a][sy]
                    assert labels[sx] == sy
            exact += 1
        else:
            witnessed_noncongruence = True
        count += 1
    assert witnessed_noncongruence
    # Same label marginal and same next-report marginal, opposite joint law.
    diag = (Q(1, 2), 0, 0, Q(1, 2))
    anti = (0, Q(1, 2), Q(1, 2), 0)
    assert aggregate(diag, (0, 0, 1, 1)) == aggregate(anti, (0, 0, 1, 1))
    assert aggregate(diag, (0, 1, 0, 1)) == aggregate(anti, (0, 1, 0, 1))
    assert tv(diag, anti) == 1
    return {"two_action_tables": count, "exact_generator_models": exact,
            "joint_law_tv_despite_equal_marginals": "1"}


def hitting_bracket(rows, labels, target, steps):
    groups = [tuple(i for i, value in enumerate(labels) if value == y)
              for y in range(max(labels) + 1)]
    observed = tuple(aggregate(row, labels) for row in rows)
    lower = upper = tuple(Q(y == target) for y in range(len(groups)))
    true = tuple(Q(y == target) for y in labels)
    for _ in range(steps):
        lower = tuple(Q(1) if y == target else
                      min(dot(observed[x], lower) for x in group)
                      for y, group in enumerate(groups))
        upper = tuple(Q(1) if y == target else
                      max(dot(observed[x], upper) for x in group)
                      for y, group in enumerate(groups))
        true = tuple(Q(1) if labels[x] == target else dot(row, true)
                     for x, row in enumerate(rows))
        assert all(lower[labels[x]] <= p <= upper[labels[x]] for x, p in enumerate(true))
    return lower, true, upper


def hitting_controls():
    labels = (0, 1, 1, 2)
    def table(action):
        return tuple(tuple(Q(y == action[x]) for y in range(4)) for x in range(4))
    case1 = hitting_bracket(table((1, 1, 3, 3)), labels, 2, 2)
    case2 = hitting_bracket(table((1, 3, 1, 3)), labels, 2, 2)
    assert (case1[0][0], case1[1][0], case1[2][0]) == (0, 0, 1)
    assert (case2[0][0], case2[1][0], case2[2][0]) == (0, 1, 1)
    # Each row is an equally weighted pair of possible successors.
    choices = ((0, 1), (1, 2), (0, 3), (2, 3))
    for selections in product(choices, repeat=4):
        rows = tuple(tuple(Q(pair.count(i), 2) for i in range(4))
                     for pair in selections)
        hitting_bracket(rows, labels, 2, 4)
    sharp = 0
    for epsilon in (Q(1, 20), Q(1, 5), Q(1)):
        hazard = epsilon / 2
        model = ((1-hazard, hazard), (Q(0), Q(1)))
        current = (Q(1), Q(0))
        error_bound = Q(0)
        for k in range(1, 13):
            current = push(current, model)
            error_bound = tv(*model) * error_bound + hazard
            assert current[1] == error_bound == 1-(1-hazard)**k
            sharp += 1
    return {"four_state_chains": len(choices) ** 4, "horizon": 4,
            "sharp_endpoint_bounds": sharp,
            "strict_upper": [0, 0, 1], "strict_lower": [0, 1, 1]}


def propagation_controls():
    labels = (0, 0, 1)
    sources = (((0, Q(1, 3), Q(2, 3)), (Q(1, 2), Q(1, 2), 0),
                (Q(1, 4), 0, Q(3, 4))),
               ((Q(1, 3), Q(2, 3), 0), (0, Q(1, 2), Q(1, 2)),
                (Q(2, 5), Q(1, 5), Q(2, 5))))
    coarse = (((Q(1, 2), Q(1, 2)), (Q(1, 4), Q(3, 4))),
              ((Q(3, 4), Q(1, 4)), (Q(1, 3), Q(2, 3))))
    checked = strict = 0
    for word in product(range(2), repeat=4):
        for initial in ((1, 0, 0), (0, 1, 0), (Q(1, 5), Q(2, 5), Q(2, 5))):
            p, v, error_bound = initial, aggregate(initial, labels), Q(0)
            for a in word:
                t, b = sources[a], coarse[a]
                local = sum(px * tv(aggregate(row, labels), b[labels[x]])
                            for x, (px, row) in enumerate(zip(p, t)))
                error_bound = tv(*b) * error_bound + local
                p, v = push(p, t), push(v, b)
                actual = tv(aggregate(p, labels), v)
                assert actual <= error_bound
                strict += actual < error_bound
                checked += 1
    assert strict > 0
    return {"signed_telescoping_comparisons": checked, "strict_bounds": strict}


def cancellation_controls():
    # Every signed complete ordered DAG on four nodes, exact length-two paths.
    edges = tuple(combinations(range(4), 2))
    pos_path = ((0, 1), (1, 3))
    alt_path = ((0, 2), (2, 3))
    zeros = equal_signs = 0
    for signs in product((-1, 1), repeat=len(edges)):
        sign = dict(zip(edges, signs))
        paths = (pos_path, alt_path)
        polar = [prod(sign[e] for e in path) for path in paths]
        def evaluate(magnitudes):
            return sum(prod(sign[e] * magnitudes[e] for e in path) for path in paths)
        def source_response(magnitudes):
            a = matrix([[sign.get((u, v), 0) * magnitudes.get((u, v), 0)
                         for u in range(4)] for v in range(4)])
            return powers(a, 2)[2][3][0]
        if polar[0] == polar[1]:
            for weight in (Q(1), Q(2, 7)):
                magnitudes = dict.fromkeys(edges, weight)
                assert source_response(magnitudes) * polar[0] > 0
            equal_signs += 1
            continue
        plus = paths[polar.index(1)]
        minus = paths[polar.index(-1)]
        starting = {e: Q(1) if e in plus else Q(1, 5) for e in edges}
        ending = {e: Q(1) if e in minus else Q(1, 5) for e in edges}
        assert evaluate(starting) > 0 > evaluate(ending)
        for e in edges:
            old = starting[e]
            left = evaluate(starting)
            starting[e] = ending[e]
            right = evaluate(starting)
            if left * right <= 0:
                if left:
                    starting[e] = old + (ending[e] - old) * left / (left - right)
                else:
                    starting[e] = old
                break
        assert min(starting.values()) > 0
        assert evaluate(starting) == source_response(starting) == 0
        zeros += 1
    for a, b, c in product((Q(1, 3), Q(1), Q(7, 5)), repeat=3):
        source = matrix(((a, 0), (c, -b)))
        assert powers(source, 3)[3][1][0] == c * ((a-b)**2+a*b) > 0
    source = matrix(((0, 0, 0), (1, 0, 0), (-1, 0, 0)))
    assert switching_function(source) is not None
    assert aggregate(tuple(row[0] for row in source), (0, 1, 1)) == (0, 0)
    return {"dag_sign_patterns": 2**len(edges), "rational_zeros": zeros,
            "sign_definite_patterns": equal_signs, "cyclic_positive_controls": 27,
            "balanced_source_aggregate_response": "0"}


if __name__ == "__main__":
    print(json.dumps({"D2_1": deterministic_controls(), "D2_2": stochastic_controls(),
                      "D2_3_hitting": hitting_controls(),
                      "D2_3_transport": propagation_controls(),
                      "D2_4_5": cancellation_controls()},
                     indent=2, sort_keys=True))
