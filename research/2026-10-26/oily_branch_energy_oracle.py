#!/usr/bin/env python3
"""Independent exact finite branch-energy oracle; no asymptotic claim.

The literal four-pole source is independently reconstructed for this research
receipt. Production remains in observational_succ. This standalone oracle
certifies an all-centers lower bound for the deficit N-|sum exp(2*pi*i*h*X_n)|.
It never evaluates complex characters and never estimates their infinite limit.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RECEIPT = HERE / 'OILY_BRANCH_ENERGY_RECEIPT.json'


def floor(value):
    return value.numerator // value.denominator


def circle(value):
    return value-floor(value)


def rational_json(value):
    value = Q(value)
    return str(value.numerator) if value.denominator == 1 else f'{value.numerator}/{value.denominator}'


def literal_forcing(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def source_history(end, initial=Q()):
    state = Q(initial)
    states, forcing = [], []
    for n in range(1, end+1):
        r = literal_forcing(n)
        state = 16*state+r
        states.append(state)
        forcing.append(r)
    return tuple(states), tuple(forcing)


def history_hash(states, forcing, initial):
    text = json.dumps({'initial': rational_json(initial),
                       'states': [rational_json(x) for x in states],
                       'forcing': [rational_json(x) for x in forcing]},
                      sort_keys=True, separators=(',', ':'))
    return sha256(text.encode()).hexdigest()


def validate_history(states, forcing, initial):
    if len(states) < 3 or len(states) != len(forcing):
        raise ValueError('at least three states and matching forcing required')
    previous = Q(initial)
    for state, r in zip(states, forcing):
        if state != 16*previous+r:
            raise ValueError('literal lifted recurrence failed')
        previous = state


def phase_cell(states, forcing, h, theta):
    """Slow independent direct cell evaluation, used as an oracle for the sweep."""
    k = tuple(floor(h*x-theta+Q(1, 2)) for x in states)
    q = tuple(h*x-theta-lift for x, lift in zip(states, k))
    b = tuple(k[n+2]-17*k[n+1]+16*k[n] for n in range(len(k)-2))
    d = tuple(h*(forcing[n+2]-forcing[n+1]) for n in range(len(k)-2))
    a = tuple(dd-bb for dd, bb in zip(d, b))
    direct = tuple(q[n+2]-17*q[n+1]+16*q[n] for n in range(len(k)-2))
    if a != direct or not all(-Q(1, 2) <= x < Q(1, 2) for x in q):
        raise AssertionError('source-to-lift second difference failed')
    exact = sum((x*x for x in a), Q())
    floor_energy = sum((max(Q(), abs(bb)-abs(dd))**2
                        for bb, dd in zip(b, d)), Q())
    if exact > 1156*sum((x*x for x in q), Q()):
        raise AssertionError('finite convolution norm failed')
    return exact, floor_energy, a


def minimum_energy(states, forcing, h=1, verify_each_cell=False):
    """Exact minimum over all circle centers using grouped rational lift jumps.

    At most N breakpoints. A simultaneous group is updated together: sequential
    updates inside a tied group would create unrealizable branch patterns.
    Each state changes at most three second differences, so after sorting the
    sweep takes O(N) exact arithmetic updates (bit complexity is not constant).
    """
    if type(h) is not int or h == 0:
        raise ValueError('nonzero integer h required')
    count = len(states)
    groups = defaultdict(list)
    for j, x in enumerate(states):
        groups[circle(h*x+Q(1, 2))].append(j)
    breakpoints = sorted(groups)
    initial_exact, initial_floor, initial_a = phase_cell(states, forcing, h, Q())
    d = tuple(h*(forcing[n+2]-forcing[n+1]) for n in range(count-2))
    a = list(initial_a)
    energy, integer_energy = initial_exact, initial_floor
    best, best_floor = energy, integer_energy
    best_theta, best_floor_theta = Q(), Q()
    patterns = [(Q(), energy, integer_energy)]
    for i, beta in enumerate(breakpoints):
        updates = defaultdict(int)
        for j in groups[beta]:
            for n, coefficient in ((j, 16), (j-1, -17), (j-2, 1)):
                if 0 <= n < count-2:
                    updates[n] += coefficient
        for n, delta in updates.items():
            previous = a[n]
            old_b = d[n]-previous
            current = previous+delta
            new_b = d[n]-current
            if old_b.denominator != 1 or new_b.denominator != 1:
                raise AssertionError('branch ceased to be integer')
            energy += current*current-previous*previous
            integer_energy += (max(Q(), abs(new_b)-abs(d[n]))**2
                               -max(Q(), abs(old_b)-abs(d[n]))**2)
            a[n] = current
        next_beta = breakpoints[i+1] if i+1 < len(breakpoints) else Q(1)
        theta = (beta+next_beta)/2
        if verify_each_cell:
            slow_energy, slow_floor, slow_a = phase_cell(states, forcing, h, theta)
            if (energy, integer_energy, tuple(a)) != (slow_energy, slow_floor, slow_a):
                raise AssertionError('grouped sweep differs from direct cell oracle')
        patterns.append((theta, energy, integer_energy))
        if energy < best:
            best, best_theta = energy, theta
        if integer_energy < best_floor:
            best_floor, best_floor_theta = integer_energy, theta
    if tuple(a) != initial_a or energy != initial_exact or integer_energy != initial_floor:
        raise AssertionError('full-circle branch energy failed to return')
    # Check the minimizers directly even when the full slow replay is disabled.
    if phase_cell(states, forcing, h, best_theta)[0] != best:
        raise AssertionError('minimum exact energy witness failed')
    if phase_cell(states, forcing, h, best_floor_theta)[1] != best_floor:
        raise AssertionError('minimum integer floor witness failed')
    if best_floor > best:
        raise AssertionError('integer floor exceeded the exact energy')
    patterns_text = json.dumps([[rational_json(v) for v in row] for row in patterns],
                               separators=(',', ':'))
    return {
        'distinct_breakpoints': len(breakpoints),
        'evaluated_patterns_including_cyclic_duplicate': len(patterns),
        'minimum_energy': best,
        'minimum_integer_floor_energy': best_floor,
        'minimizing_center': best_theta,
        'integer_floor_minimizing_center': best_floor_theta,
        'deficit_lower': Q(2, 289)*best,
        'normalized_deficit_lower': Q(2, 289)*best/count,
        'pattern_energy_sha256': sha256(patterns_text.encode()).hexdigest(),
    }


def certificate(end, h=1, changed_seed=False):
    native, forcing = source_history(end)
    initial = -native[-1]/16**end if changed_seed else Q()
    states, forcing = source_history(end, initial)
    validate_history(states, forcing, initial)
    result = minimum_energy(states, forcing, h, verify_each_cell=end <= 32)
    return {
        'N': end,
        'frequency': h,
        'source': 'unchanged literal four poles',
        'selector': 'rational terminal-zero changed seed' if changed_seed else 'authentic U0=0',
        'authentic_zero_selector': initial == 0,
        'history_sha256': history_hash(states, forcing, initial),
        **{k: rational_json(v) if isinstance(v, Q) else v for k, v in result.items()},
    }


def self_checks():
    # Fresh, nongeometric source sizes and signed frequencies, with every cell
    # independently evaluated. This is not fitted to the displayed receipt grid.
    for end, h in ((7, -2), (13, 5), (19, -3), (29, 7), (31, 16)):
        states, forcing = source_history(end)
        validate_history(states, forcing, 0)
        minimum_energy(states, forcing, h, verify_each_cell=True)
    # Fixed phases: all breakpoints coincide. Treating tied jumps as separate
    # cells would manufacture fake positive energies between impossible states.
    zeros = (Q(),)*9
    fixed = minimum_energy(zeros, zeros, verify_each_cell=True)
    assert fixed['minimum_energy'] == 0 and fixed['distinct_breakpoints'] == 1
    assert fixed['evaluated_patterns_including_cyclic_duplicate'] == 2
    # Generic positive control. This is deliberately not the BBP forcing.
    alternating = tuple(Q(n % 2, 2) for n in range(1, 17))
    forcing = tuple(x-16*(alternating[j-1] if j else Q())
                    for j, x in enumerate(alternating))
    validate_history(alternating, forcing, 0)
    positive = minimum_energy(alternating, forcing, verify_each_cell=True)
    assert positive['minimum_energy'] == Q(289, 4)*(len(alternating)-2)
    assert positive['deficit_lower'] == Q(len(alternating)-2, 2)
    # Exact same forcing / different finite selector: its energy does not grow.
    for end in (11, 23, 47):
        selected, forcing = source_history(end)
        initial = -selected[-1]/16**end
        changed, forcing = source_history(end, initial)
        validate_history(changed, forcing, initial)
        control = minimum_energy(changed, forcing, verify_each_cell=True)
        no_branch = sum(((forcing[n+2]-forcing[n+1])**2
                         for n in range(end-2)), Q())
        assert control['minimum_energy'] == no_branch
    # Explicit false recurrence mutation must be rejected.
    states, forcing = source_history(9)
    mutant = list(states)
    mutant[4] += Q(1, 997)
    try:
        validate_history(tuple(mutant), forcing, 0)
    except ValueError:
        pass
    else:
        raise AssertionError('source mutation escaped validation')
    return {
        'direct_cell_holdouts': [[7, -2], [13, 5], [19, -3], [29, 7], [31, 16]],
        'fixed_phase_tied_breakpoint_control': 'passed',
        'alternating_phase_positive_control': 'passed',
        'same_forcing_changed_seed_controls': [11, 23, 47],
        'mutated_source_recurrence': 'rejected',
        'full_circle_energy_return': 'passed',
    }


def build_receipt():
    checks = self_checks()
    return {
        'schema': 'oily-branch-energy-v1',
        'authority': 'exact finite source-authenticated deficit lower bound; no asymptotic energy lower bound',
        'bound': 'N - abs(S_N(h)) >= (2/289) min_theta sum_n (h*Delta_r_n - B_n(theta))^2',
        'source_engine': 'independent literal four-pole Fraction recurrence',
        'complex_character_evaluation': 'none',
        'oracle_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks': checks,
        'certificates': [certificate(end, h, control)
                         for end in (16, 32, 64, 128)
                         for h in (1, -3)
                         for control in (False, True)],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    receipt = build_receipt()
    encoded = json.dumps(receipt, indent=2, sort_keys=True)+'\n'
    if args.write:
        RECEIPT.write_text(encoded)
        print(f'WROTE {RECEIPT.name}: {len(receipt["certificates"])} exact certificates')
    elif args.verify:
        if RECEIPT.read_text() != encoded:
            raise SystemExit('RECEIPT_MISMATCH')
        print(f'VERIFIED {RECEIPT.name}: {len(receipt["certificates"])} exact certificates')
    else:
        for row in receipt['certificates']:
            ratio = Q(row['normalized_deficit_lower'])
            print(row['N'], row['frequency'], row['authentic_zero_selector'],
                  f'{float(ratio):.8f} (display-only decimal of exact rational bound)')


if __name__ == '__main__':
    main()
