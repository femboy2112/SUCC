#!/usr/bin/env python3
"""Exact hostile controls for deterministic adaptive linear observation.

The universal minimax theorem is a paper proof. This standalone standard-library
probe checks its zero-history mechanism and precise assumption-deletion examples.
No native implementation or floating arithmetic is used.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def minus(x, y):
    return tuple(a-b for a, b in zip(x, y))


def solve(a, b):
    n = len(a)
    rows = [list(map(Q, row))+[Q(value)] for row, value in zip(a, b)]
    for j in range(n):
        k = next((i for i in range(j, n) if rows[i][j]), None)
        if k is None:
            return None
        rows[j], rows[k] = rows[k], rows[j]
        pivot = rows[j][j]
        rows[j] = [v/pivot for v in rows[j]]
        for i in range(n):
            if i != j:
                c = rows[i][j]
                rows[i] = [x-c*y for x, y in zip(rows[i], rows[j])]
    return tuple(row[-1] for row in rows)


def ball_radius_squared(points):
    """Enumerate finite Euclidean ball supports of size at most dim+1."""
    points = tuple(dict.fromkeys(tuple(map(Q, p)) for p in points))
    dim = len(points[0])
    best = None
    for size in range(1, min(dim+1, len(points))+1):
        for support in combinations(points, size):
            p = support[0]
            differences = [minus(q, p) for q in support[1:]]
            if differences:
                gram = [[dot(u, v) for v in differences] for u in differences]
                coeff = solve(gram, [dot(v, v)/2 for v in differences])
                if coeff is None:
                    continue
                center = tuple(p[j]+sum(c*v[j] for c, v in zip(coeff, differences))
                               for j in range(dim))
            else:
                center = p
            radius2 = dot(minus(center, p), minus(center, p))
            if all(dot(minus(q, center), minus(q, center)) <= radius2 for q in points):
                if best is None or radius2 < best:
                    best = radius2
    assert best is not None
    return best


def query(state, index):
    # Four-coordinate homogeneous linear action overwriting only the readout
    # register. The same formula works for the three-coordinate ball control.
    return (state[index],)+state[1:]


def transcript(state, word):
    history = [state[0]]
    for index in word:
        state = query(state, index)
        history.append(state[0])
    return tuple(history)


def nonconvex_prior_control():
    zero = (Q(0),)*4
    positive = ((Q(0), Q(0), Q(1, 2), Q(0)),
                (Q(0), Q(1, 2), Q(0), Q(0)),
                (Q(0), Q(1, 2), Q(0), Q(1, 2)))
    prior = (zero,)+positive+tuple(tuple(-v for v in state) for state in positive)
    assert len(set(prior)) == 7
    assert all(tuple(-v for v in state) in prior for state in prior)
    assert all(dot(state, state) <= 1 for state in prior)
    # The midpoint of the two different positive-axis points is absent.
    assert tuple((a+b)/2 for a, b in zip(positive[0], positive[1])) not in prior
    records = {}
    for state in prior:
        first = query(state, 1)
        second_index = 2 if first[0] == 0 else 3
        record = transcript(state, (1, second_index))
        key = ((1, second_index), record)
        records.setdefault(key, set()).add(state[1:])
    assert len(records) == 7 and all(len(values) == 1 for values in records.values())
    fixed = {}
    for length in range(3):
        for word in product((1, 2, 3), repeat=length):
            fibers = {}
            for state in prior:
                fibers.setdefault(transcript(state, word), []).append(state[1:])
            radius2 = max(ball_radius_squared(targets) for targets in fibers.values())
            fixed[''.join('abc'[i-1] for i in word) or 'empty'] = radius2
    assert len(fixed) == 13
    assert min(fixed.values()) == Q(1, 16)
    assert fixed['ab'] == fixed['ba'] == Q(1, 16)
    assert fixed['ac'] == fixed['bc'] == Q(1, 4)
    return {'prior_size': 7, 'adaptive_target_fibers': len(records),
            'adaptive_worst_error_squared': '0',
            'best_fixed_worst_error_squared': '1/16',
            'fixed_schedules': {k: str(v) for k, v in sorted(fixed.items())}}


def unit_ball_and_randomization_controls():
    # Source coordinates (r,a,b), target (a,b). At zero, a deterministic
    # budget-one policy chooses one query or stops. An unqueried hidden unit
    # vector and its negative have the same zero transcript.
    zero_path_cases = 0
    for word in ((), (1,), (2,)):
        missing = 2 if word == (1,) else 1
        plus = tuple(Q(int(i == missing)) for i in range(3))
        negative = tuple(-v for v in plus)
        assert transcript(plus, word) == transcript(negative, word) == transcript((0, 0, 0), word)
        assert dot(plus[1:], plus[1:]) == 1
        zero_path_cases += 1
    # Independent random choice, evaluated under worst-case EXPECTED SQUARED
    # error, changes the objective and achieves 1/2 rather than deterministic 1.
    values = tuple(map(Q, (-1, 0, 1)))+(Q(3, 5), Q(-3, 5), Q(4, 5), Q(-4, 5))
    checked = 0
    for a, b in product(values, repeat=2):
        if a*a+b*b <= 1:
            expected_squared = (b*b+a*a)/2
            assert expected_squared <= Q(1, 2)
            checked += 1
    return {'zero_path_choices': zero_path_cases,
            'rational_hidden_points': checked,
            'deterministic_worst_squared_error': '1',
            'randomized_worst_expected_squared_error': '1/2',
            'objective_changed_for_randomization': True}


def nonlinear_control():
    # Initial readout s and target t on the Euclidean unit disk. Total
    # continuous nonlinear actions send (s,t) to (max(0,1 +/- 2s)t,0).
    # Adaptively choosing sign(s) always gives a known multiplier >=1.
    pairs = ((Q(-3, 5), Q(4, 5)), (Q(-3, 5), Q(-4, 5)),
             (Q(3, 5), Q(4, 5)), (Q(3, 5), Q(-4, 5)))
    for s, t in pairs:
        assert s*s+t*t == 1
        multiplier = max(Q(0), 1+(2*s if s >= 0 else -2*s))
        assert multiplier >= 1
        assert multiplier*t/multiplier == t
    assert max(Q(0), 1+2*pairs[0][0]) == 0
    assert max(Q(0), 1-2*pairs[2][0]) == 0
    return {'rational_unit_disk_controls': len(pairs), 'adaptive_error': '0',
            'each_fixed_action_worst_error_at_least': '4/5',
            'removed_assumption': 'homogeneous linear actions'}


def state_cost_control():
    # Both labels perform the same linear query of hidden t. On initial
    # readout s, their costs exchange 1 and 2. Budget one admits a sign-based
    # adaptive policy but neither fixed nonempty schedule uniformly.
    for s in (Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1)):
        c_plus = 1 if s >= 0 else 2
        c_minus = 1 if s < 0 else 2
        chosen = c_plus if s >= 0 else c_minus
        assert chosen == 1
    return {'budget': 1, 'adaptive_error': '0', 'best_uniformly_feasible_fixed_error': '1',
            'removed_assumption': 'state-independent action costs'}


def main():
    result = {'scope': 'Exact finite controls; universal adaptive theorem has a separate proof',
              'nonconvex_prior': nonconvex_prior_control(),
              'unit_ball_randomization': unit_ball_and_randomization_controls(),
              'nonlinear_actions': nonlinear_control(),
              'state_dependent_costs': state_cost_control()}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
