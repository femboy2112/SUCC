#!/usr/bin/env python3
"""Reproduce exact source/triangle receipts; optional phase diagnostics are numeric.

No finite output proves pi normality. The exact budget is a representation
bound and the original zero-seeded phases remain present in both sums.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import recursive_carrier_triangle as r
from observational_succ import oily_macaroni_transfer as inherited
from observational_succ.succ_internal_matrix_walk import authentic_r


def json_value(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: json_value(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_value(v) for v in value]
    return value


def run_exact():
    counts = Counter()
    def check(group, predicate):
        if not predicate:
            raise AssertionError(group)
        counts[group] += 1

    parameters = (F(1, 17), F(23, 11), F(1001, 7), F(289), F(481), F(769))
    for a in parameters:
        for shift in (F(0), F(1, 13), F(7, 5), F(8), F(19)):
            check('atomic_laplace', r.atomic_laplace(a, shift) == r.tilt_normalizer(a, shift))
        for order in range(1, 13):
            low, high = r.cumulant_bounds(a, order)
            check('cumulant_squeeze', low < r.source_cumulant(a, order) < high)
        for order in range(1, 7):
            steps = tuple((F(1, 13), F(7, 5), F(8), F(19))[k % 4] for k in range(order))
            interaction = r.interaction_ratio(a, steps)
            check('all_order_interaction', interaction > 1 if order % 2 == 0 else interaction < 1)
    for n in (1, 2, 3, 37, 61, 97, 1001):
        check('native_source', r.source_factorization(8*n-7) == authentic_r(n))
    for a, b in product(parameters, repeat=2):
        low, high = r.overlap_square_bounds(a, b)
        h2 = r.overlap_square(a, b)
        check('overlap_squeeze', low <= h2 <= high)
        check('rational_deficit', (1-r.overlap_deficit_bound(a, b))**2 <= h2)

    comparisons = []
    for n in (27, 343, 512, 1000, 4096, 10**6):
        old = inherited.multiscale_hilbert_transport_budget(n)
        new = r.cubic_transport_budget(n)
        check('cubic_simple_bound', new['absolute_mean_error_upper'] <= new['simple_upper'])
        old_count = (n-old['first_retained']+old['block_length'])//old['block_length']
        comparisons.append({
            'N': n, 'old_anchor_count': old_count, 'new_anchor_count': new['blocks'],
            'old_discarded': old['discarded'], 'new_discarded': 0,
            'old_exact_bound': old['absolute_mean_error_upper'],
            'new_exact_endpoint_bound': new['absolute_mean_error_upper'],
            'new_simple_exact_bound': new['simple_upper'],
            'old_bound_decimal_display': float(old['absolute_mean_error_upper']),
            'new_bound_decimal_display': float(new['absolute_mean_error_upper']),
            'bound_type': 'representation error; not a signed sum bound',
        })

    for n in (1, 2, 7, 8, 9, 26, 27, 28, 343, 344, 999, 1000, 1001, 4096, 4097):
        budget = r.cubic_transport_budget(n)
        check('cube_boundary', budget['last_block_index']**3 <= n-1 < budget['blocks']**3)
        check('endpoint_budget', budget['absolute_mean_error_upper'] <= budget['simple_upper'])

    phase_lift_checks = 0
    history = r.authentic_history(97)
    for n in range(1, 97):
        for h in (-3, -1, 0, 1, 7):
            # Exponents of Psi_(n+1)(h) and e(h*r_(n+1))*Psi_n(16h).
            check('selected_phase_carrier_exponent', h*history[n+1] == 16*h*history[n]+h*authentic_r(n+1))
            phase_lift_checks += 1
        # Squared source amplitude multiplier is exp(-8x)/Z_n.
        check('selected_phase_carrier_normalizer', r.tilt_normalizer(8*n-7, 8)
              == authentic_r(n+1)/authentic_r(n))

    law = r.exponential_left
    for length in range(1, 8):
        total = signed = F()
        for word_tuple in product('LR', repeat=length):
            word = ''.join(word_tuple)
            p = r.word_probability(word, law)
            total += p
            signed += (1 if word[-1] == 'L' else -1)*p
        check('nonflat_ensemble_zero', total == 1 and signed == 0)
    check('coherent_atom_lower_bound', r.all_left_atom_lower_bound(3) == F(1, 5))

    return json_value({
        'schema': 'succ.recursive-carrier-triangle.production-probe.v1',
        'status': 'passed', 'baseline_commit': 'ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc',
        'python': platform.python_version(), 'checks': dict(sorted(counts.items())),
        'exact_check_total': sum(counts.values()),
        'finite_grid': {'source_parameters': parameters, 'max_cumulant_order': 12,
                        'max_interaction_order': 6, 'selected_phase_horizon': 97,
                        'selected_phase_exponent_checks': phase_lift_checks},
        'authentic_clock_pair_ratio': r.interaction_ratio(1, (8, 8)),
        'authentic_clock_cubic_ratio': r.interaction_ratio(1, (8, 8, 8)),
        'transport_comparisons': comparisons,
        'control': {'nonflat_diamond': r.diamond_ratio(1, 0, law),
                    'all_left_infinite_atom_paper_lower_bound': F(1, 5),
                    'coherent_phase_average_for_z_equal_one': 1},
        'scope': {'finite_exact_instrument_checks': True,
                  'analytic_proofs': 'separate paper dossiers',
                  'signed_cancellation_proved': False, 'pi_normality_proved': False,
                  'path_to_positive_density_feedback_derived': False,
                  'independent_atoms_are_arithmetic_phase_independence': False},
    })


def numeric_selected_phase_diagnostics():
    import mpmath as mp
    rows = []
    with mp.workdps(80):
        convert = lambda q: mp.mpf(q.numerator)/q.denominator
        history = r.authentic_history(512)
        for n in (127, 343, 512):
            for h in (1, 3, 7):
                original = weighted = mp.mpc(0)
                coherent_weighted = mp.mpf(0)
                for k in range(1, n+1):
                    j = r.integer_cuberoot(k-1)
                    start = 1+j**3
                    affinity = mp.sqrt(convert(r.overlap_square(8*k-7, 8*start-7)))
                    phase = mp.exp(2j*mp.pi*convert((h*history[k]) % 1))
                    original += phase
                    weighted += phase*affinity
                    coherent_weighted += affinity
                bound = r.cubic_transport_budget(n)['absolute_mean_error_upper']
                discrepancy = abs(original-weighted)/n
                if discrepancy > convert(bound):
                    raise AssertionError('observed discrepancy exceeds proved analytic ceiling')
                rows.append({'N': n, 'h': h, 'original_mean_magnitude': mp.nstr(abs(original)/n, 24),
                             'weighted_mean_magnitude': mp.nstr(abs(weighted)/n, 24),
                             'observed_transport_discrepancy': mp.nstr(discrepancy, 24),
                             'proved_exact_endpoint_budget': str(bound),
                             'coherent_control_original_mean': '1',
                             'coherent_control_weighted_mean': mp.nstr(coherent_weighted/n, 24)})
    return {'status': 'OBSERVED_NUMERICAL', 'precision_decimal_digits': 80, 'rows': rows,
            'certified_phase_intervals': False,
            'scope': 'finite diagnostics; only the separately proved transport budget is rigorous'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--numerical', action='store_true')
    args = parser.parse_args()
    result = run_exact()
    if args.numerical:
        result['numerical_diagnostics'] = numeric_selected_phase_diagnostics()
    else:
        result['numerical_diagnostics'] = {'executed': False}
    rendered = json.dumps(result, sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding='utf-8')
    print(rendered, end='')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
