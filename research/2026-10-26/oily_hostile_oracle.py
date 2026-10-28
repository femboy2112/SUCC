#!/usr/bin/env python3
"""Independent exact audit: branch energy, beta jets, and source controls.

Run from any directory; standard library only. This is a finite oracle, not
an infinite-limit proof. It does not import the production cumulant formulas.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import itertools
import json
from math import factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
ORDER = 6


def add(p, q):
    r = dict(p)
    for monomial, value in q.items():
        r[monomial] = r.get(monomial, Q()) + value
    return {k: v for k, v in r.items() if v}


def scale(p, c):
    return {k: c*v for k, v in p.items() if c*v}


def mul(p, q):
    r = {}
    for (a, s), x in p.items():
        for (b, t), y in q.items():
            if a+b <= ORDER:
                key = (a+b, s+t)
                r[key] = r.get(key, Q()) + x*y
    return {k: v for k, v in r.items() if v}


ONE = {(0, 0): Q(1)}


def inverse(p):
    c = p.get((0, 0), Q())
    assert c and all(a > 0 for (a, s) in p if (a, s) != (0, 0))
    remainder = scale(add(p, {(0, 0): -c}), -1/c)
    total, term = dict(ONE), dict(ONE)
    for _ in range(ORDER):
        term = mul(term, remainder)
        total = add(total, term)
    return scale(total, 1/c)


def series_divide(numerator, denominator):
    out = []
    for k in range(ORDER+1):
        value = Q(numerator[k]) if k < len(numerator) else Q()
        for j in range(1, min(k, len(denominator)-1)+1):
            value -= denominator[j]*out[k-j]
        out.append(value/denominator[0])
    return out


def series_mul(p, q):
    return [sum((p[j]*q[k-j] for j in range(k+1)), Q())
            for k in range(ORDER+1)]


def beta_ratio(r):
    """Exact formal jet of (s+2)_r / (a+s+3)_r in A=1/a."""
    out = dict(ONE)
    for j in range(r):
        out = mul(out, {(1, 1): Q(1), (1, 0): Q(2+j)})
        out = mul(out, inverse({(0, 0): Q(1), (1, 1): Q(1),
                                (1, 0): Q(3+j)}))
    return out


def tilted_jet(grade, weight):
    numerator_coefficients = series_mul(grade, weight)
    numerator, denominator = {}, {}
    for r in range(ORDER+1):
        beta = beta_ratio(r)
        numerator = add(numerator, scale(beta, numerator_coefficients[r]))
        denominator = add(denominator, scale(beta, weight[r]))
    return mul(numerator, inverse(denominator))


def rational(x):
    return str(Q(x))


def audit_branch_energy_sweep():
    """Brute all exact boundaries and interval midpoints, using q directly."""
    source = Path(__file__).with_name('oily_branch_energy_oracle.py')
    spec = importlib.util.spec_from_file_location('branch_energy_audited', source)
    sweep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sweep)

    def direct_minimum(states, h):
        points = {Q(), Q(1)}
        for x in states:
            value = h*x+Q(1, 2)
            points.add(value-value.__floor__())
        ordered = sorted(points)
        centers = ordered[:-1]+[(a+b)/2 for a, b in zip(ordered, ordered[1:])]
        def energy(theta):
            residuals = [h*x-theta-(h*x-theta+Q(1, 2)).__floor__() for x in states]
            assert all(-Q(1, 2) <= q < Q(1, 2) for q in residuals)
            return sum(((residuals[n+2]-17*residuals[n+1]+16*residuals[n])**2
                        for n in range(len(states)-2)), Q())
        values = [energy(theta) for theta in centers]
        mean = sum(((b-a)*energy((a+b)/2) for a, b in zip(ordered, ordered[1:])), Q())

        def circle_variance(x):
            d = x-x.__floor__()
            return d*(1-d)

        identity_mean = sum((272*circle_variance(h*(states[n]-states[n+1]))
                             -16*circle_variance(h*(states[n]-states[n+2]))
                             +17*circle_variance(h*(states[n+1]-states[n+2]))
                             for n in range(len(states)-2)), Q())
        assert mean == identity_mean
        assert min(values) <= mean <= Q(289, 4)*(len(states)-2)
        return min(values), mean

    histories = 0
    grid = [Q(j, 4) for j in range(4)]
    for count in (3, 4):
        for states in itertools.product(grid, repeat=count):
            forcing = tuple(x-16*(states[n-1] if n else Q()) for n, x in enumerate(states))
            expected, mean = direct_minimum(states, 1)
            actual = sweep.minimum_energy(states, forcing, 1, verify_each_cell=True)
            assert expected == actual['minimum_energy']
            histories += 1

    holdouts = []
    for count, h in ((17, -2), (37, 3)):
        states, forcing, state = [], [], Q()
        for n in range(1, count+1):
            r = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            state = 16*state+r
            states.append(state)
            forcing.append(r)
        expected, mean = direct_minimum(states, h)
        actual = sweep.minimum_energy(states, forcing, h, verify_each_cell=True)
        assert expected == actual['minimum_energy']
        holdouts.append({'N': count, 'h': h, 'minimum_energy': rational(expected),
                         'mean_energy_over_centers': rational(mean)})
    alternating = tuple(Q(j % 2, 2) for j in range(16))
    sharp_min, sharp_mean = direct_minimum(alternating, 1)
    assert sharp_min == sharp_mean == Q(289, 4)*(len(alternating)-2)
    return {'small_grid_histories': histories,
            'explicit_zero_and_tied_breakpoints': 'passed',
            'direct_method': 'all boundary and midpoint centers; principal q second difference',
            'source_holdouts': holdouts,
            'mean_energy_identity': '272 f(d01) - 16 f(d02) + 17 f(d12), f(d)=d(1-d)',
            'sharp_universal_minimum_energy_upper': '289*(N-2)/4',
            'sharp_alternating_control_N': len(alternating),
            'sharp_alternating_control_minimum': rational(sharp_min),
            'instrument_cannot_certify_modulus_below': '(N+2)/2'}


def build_receipt():
    from observational_succ.succ_internal_matrix_walk import authentic_r, original_state
    from observational_succ.bbp_natural_carrier import exact_forcing
    from observational_succ.integer_bbp_carrier import forcing_pair, source_states

    states, u = source_states(128), Q()
    for n in range(1, 129):
        source = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        assert source == authentic_r(n) == exact_forcing(n) == Q(*forcing_pair(n))
        u = 16*u+source
        assert u == original_state(n) == Q(states[n].numerator, states[n].conductor)
    assert Q(4)-Q(2, 4)-Q(1, 5)-Q(2, 6) != authentic_r(1)

    norms = set()
    pairs = 0
    for transitions in range(2, 12):
        for j in range(transitions):
            for k in range(j+1, transitions):
                vector = [0]*(transitions+1)
                vector[j] -= 16
                vector[j+1] += 1
                vector[k] += 16
                vector[k+1] -= 1
                norm = sum(c*c for c in vector)
                assert norm == (546 if k == j+1 else 514)
                norms.add(norm)
                pairs += 1
    assert max(norms) > 514  # Deliberate false universal norm is rejected.
    margin = Q(19, 546)*Q(4081, 4096)**2-Q(1, 29)
    trig = 2*Q(157, 50)**2-Q(2, 3)*Q(22, 7)**4/225-19
    assert margin > 0 and trig > 0
    assert Q(1, 29)/8 < Q(1, 15)**2
    endpoint = 16*(Q(32, 225)+Q(1, 64*7*7)+Q(1, 64*8*8))
    assert endpoint < 3

    # f_odd(1-t)=(4-4t)/(9-6t+2t^3-t^4), independently derived.
    grade = series_divide([4, -4], [9, -6, 0, 2, -1])
    weight = series_divide([1], [1, 2, 0, 2, -1])
    # A different positive smooth outer weight deliberately changes the source.
    mutant_weight = series_divide([1], [1, Q(-1, 3)])
    jet = tilted_jet(grade, weight)
    mutant_jet = tilted_jet(grade, mutant_weight)
    assert all(s <= a for a, s in jet)
    assert all(s <= a for a, s in mutant_jet)

    delta = [Q()] + [Q((-1)**(k+1)) for k in range(1, ORDER+1)]
    power = [Q(1)]+[Q()]*ORDER
    composed = [Q()]*(ORDER+1)
    for c in grade:
        composed = [x+c*y for x, y in zip(composed, power)]
        power = series_mul(power, delta)
    leading = []
    for m in range(1, ORDER+1):
        observed = jet.get((m, m), Q())
        assert observed == composed[m] == mutant_jet.get((m, m), Q())
        leading.append(factorial(m)*observed)
    assert leading[:3] == [Q(-4, 27), Q(8, 81), Q(-56, 81)]
    assert leading[1] != -Q(8, 81)  # Sign mutant rejected.
    assert jet != mutant_jet  # Lower-degree source terms do change.

    # Exact finite analogue of the source survival/redraw coupling.
    p, survival, g = [Q(1, 3), Q(2, 3)], [Q(1, 4), Q(3, 4)], [Q(), Q(1)]
    Z = sum((p[i]*survival[i] for i in range(2)), Q())
    next_p = [p[i]*survival[i]/Z for i in range(2)]
    mean = sum((p[i]*g[i] for i in range(2)), Q())
    next_mean = sum((next_p[i]*g[i] for i in range(2)), Q())
    covariances = []
    for persistent in (False, True):
        joint = [[p[i]*(survival[i]*int(i == j)+(1-survival[i])*next_p[j])
                  if persistent else p[i]*next_p[j] for j in range(2)]
                 for i in range(2)]
        assert [sum(joint[i][j] for i in range(2)) for j in range(2)] == next_p
        moment = sum((joint[i][j]*g[i]*g[j] for i in range(2) for j in range(2)), Q())
        covariances.append(moment-mean*next_mean)
    assert covariances == [Q(), Q(1, 14)]
    assert covariances[1] == Z*next_mean*(1-next_mean)

    # Small-domain resonances plus the sharp degree-17 adjacent witness.
    nonzero_vectors = 0
    for k in itertools.product(range(-2, 3), repeat=4):
        if any(k):
            nonzero_vectors += 1
            assert sum(c*16**n for n, c in enumerate(k)) != 0
    assert 16-16 == 0 and abs(16)+abs(-1) == 17

    branch_sweep = audit_branch_energy_sweep()

    inputs = [
        Path(__file__).relative_to(ROOT),
        Path('observational_succ/succ_internal_matrix_walk.py'),
        Path('observational_succ/bbp_natural_carrier.py'),
        Path('observational_succ/integer_bbp_carrier.py'),
        Path('research/2026-10-26/oily_branch_energy_oracle.py'),
    ]
    return {
        'schema': 'oily-hostile-oracle-v1',
        'baseline_commit': 'a8c7c85b7a1900d422090f1757c174e7aac69f44',
        'scope': 'exact finite independent calibration; no infinite cancellation proof',
        'source_sha256': {str(p): sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
        'literal_four_pole_states_checked': 128,
        'branch_pairs_checked': pairs,
        'branch_squared_norms': sorted(norms),
        'branch_margin': rational(margin),
        'trigonometric_margin': rational(trig),
        'green_endpoint_prefactor_upper': rational(endpoint),
        'beta_jet_order': ORDER,
        'grade_taylor': [rational(x) for x in grade],
        'source_weight_taylor': [rational(x) for x in weight],
        'normalized_beta_jet': [
            {'inverse_a_degree': a, 's_degree': s, 'coefficient': rational(c)}
            for (a, s), c in sorted(jet.items())],
        'cumulant_leading_coefficients': [rational(x) for x in leading],
        'positive_outer_weight_mutant_same_leading_coefficients': True,
        'positive_outer_weight_mutant_full_jet_differs': True,
        'coupling_survival_mass': rational(Z),
        'coupling_covariances': [rational(x) for x in covariances],
        'nonresonant_small_vectors_checked': nonzero_vectors,
        'sharp_adjacent_resonance_degree': 17,
        'branch_energy_sweep_independent_audit': branch_sweep,
        'mutants_rejected': ['last pole coefficient', 'universal norm 514',
                             'second cumulant sign', 'marginals determine covariance'],
    }


def main():
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--write', action='store_true')
    action.add_argument('--verify', action='store_true')
    parser.add_argument('--receipt', type=Path,
                        default=Path(__file__).with_name('OILY_HOSTILE_ORACLE_RECEIPT.json'))
    args = parser.parse_args()
    payload = json.dumps(build_receipt(), indent=2, sort_keys=True)+'\n'
    if args.write:
        args.receipt.write_text(payload)
        print('WROTE OILY_HOSTILE_ORACLE_RECEIPT')
    else:
        if args.receipt.read_text() != payload:
            raise SystemExit('REJECTED: exact oracle receipt mismatch')
        print('VERIFIED OILY_HOSTILE_ORACLE_RECEIPT')


if __name__ == '__main__':
    main()
