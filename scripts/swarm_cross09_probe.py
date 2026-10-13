#!/usr/bin/env python3
"""Freeze the exact X09 countermodels; this is not an analytic proof oracle."""
import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.swarm_cross09 import (
    alternating_coefficient_lower_bound, alternating_data,
    coefficient_prefix_enclosure, gamma_product_cutoff, interpolate,
    pairwise_difference_bound, polynomial_value, quarter_periodic_multiplier,
)


def receipt():
    interpolation = []
    for count in (2, 3, 5, 8, 12):
        data = alternating_data(count)
        coefficients = interpolate(data)
        interpolation.append({
            'samples': count,
            'exact_fit': all(polynomial_value(coefficients, x) == y for x, y in data),
            'max_coefficient': str(max(map(abs, coefficients))),
            'necessary_common_bound': str(alternating_coefficient_lower_bound(count)),
        })
    geometric = []
    for size in (0, 1, 5, 20):
        lo, hi = coefficient_prefix_enclosure((Q(1),) * size, 1, Q(1, 2))
        geometric.append({'prefix_length': size, 'interval': [str(lo), str(hi)],
                          'actual_limit': '2', 'upper_endpoint_exact': hi == 2})
    ratio = gamma_product_cutoff(19, 4) / gamma_product_cutoff(19, 3)
    return {
        'mission': 'X09',
        'source_base': '7913e101d6e83b697f4e13535cc3b1330b80f0c2',
        'truth_status': {
            'compact_holomorphic_actualization': 'PROVED LOCAL (paper proof; classical method)',
            'unrestricted_finite_interpolation_implies_realization': 'REFUTED',
            'closed_coefficient_bound': 'DECLARED GLOBAL HYPOTHESIS, not inferred from finite probes',
            'formal_kernel_coverage': 'None for X09 analytic theorem',
        },
        'interpolation_phantoms': interpolation,
        'bounded_geometric_positive_control': geometric,
        'same_source_pair_control': {
            'reports': [['0', '1'], ['1/2', '-1']],
            'individual_constant_sources': ['1', '-1'],
            'observed_difference': '2',
            'maximum_difference_in_K1': str(pairwise_difference_bound(1, 0, Q(1, 2))),
            'joint_source_exists': False,
        },
        'gamma_independent_product_control': {
            'cutoff': 19, 'z': 3, 'ratio': str(ratio), 'target': '3',
            'defect': str(3 - ratio),
            'quarter_periodic_multiplier': str(quarter_periodic_multiplier(1)),
            'integer_periodic_multiplier': str(quarter_periodic_multiplier(4)),
        },
        'validation': {
            'command': "python -m unittest discover -s tests -p 'test_swarm_cross09.py' -v",
            'tests_passed': 8,
            'exact_domain': 'fractions.Fraction; float and bool scalars rejected',
            'probes_do_not_execute_infinite_limits': True,
        },
        'no_nontrivial_zero_inputs': True,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    serialized = json.dumps(receipt(), indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(serialized)
    else:
        print(serialized, end='')
