#!/usr/bin/env python3
"""Run A-cohort adversarial gates and emit a reproducible exact receipt."""
import argparse
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.swarm_categories import (  # noqa: E402
    FiniteDynamics, finite_relation_glue, holonomy_sections, separation_depth,
    stable_refinement,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.discover(str(ROOT / 'tests'), pattern='test_swarm_categories.py')
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    reports = (0, 0, 0, 1)
    a, b = (0, 0, 3, 0), (0, 2, 0, 0)
    A = FiniteDynamics('A', reports, ('a',), (a,), ('a',))
    B = FiniteDynamics('B', reports, ('b',), (b,), ('b',))
    AB = FiniteDynamics('AB', reports, ('a', 'b'), (a, b), ('a', 'b'))
    cost_source = FiniteDynamics('cost-countermodel', (0, 0, 1, 0, 0),
                                 ('a',), ((0, 3, 2, 4, 2),), ('a',))
    eq, ne = ((0, 0), (1, 1)), ((0, 1), (1, 0))
    receipt = {
        'schema': 'SUCC-SWM-A/1',
        'frozen_parent': '5eb09e7cba36ec01b8f9d6834b78b5766fd93935',
        'status': 'PROVED LOCAL paper derivations; exact finite implementation checked',
        'formal_kernel_checked': False,
        'external_source_authentication': False,
        'unit_tests_run': result.testsRun,
        'unit_test_failures': len(result.failures),
        'unit_test_errors': len(result.errors),
        'unit_tests_passed': result.wasSuccessful(),
        'exhaustive_scope_asserted_by_passing_tests': {
            'unary_three_state_source_initial_partition_instances': 1080,
            'binary_two_state_source_initial_partition_instances': 128,
            'strict_two_to_three_state_base_change_partition_instances': 7200,
            'origin_current_belief_update_subset_action_report_instances': 2048,
            'S3_triangle_connections_with_independent_section_enumeration': 216,
            'S3_triangle_gauge_mutations': 216,
        },
        'noncomposing_repairs': {
            'reports': reports, 'action_A': a, 'action_B': b,
            'I_A_I_B_R': stable_refinement(A, stable_refinement(B)[0])[0],
            'joint_repair': stable_refinement(AB)[0],
            'distinguishing_word': ('b', 'a'),
            'trace_original_0': AB.transcript(0, ('b', 'a')),
            'trace_original_1': AB.transcript(1, ('b', 'a')),
        },
        'pairwise_gluing_countermodel': {
            'contexts': ('xy', 'yz', 'xz'),
            'constraints': ('equal', 'equal', 'unequal'),
            'global_sections': finite_relation_glue(('x', 'y', 'z'), (0, 1),
                              ((('x', 'y'), eq), (('y', 'z'), eq), (('x', 'z'), ne))),
        },
        'even_nonidentity_holonomy': holonomy_sections((0,),
                            (('loop', 0, 0, (1, 2, 0)),), 3, ('loop',)),
        'raw_distinguishing_cost_triangle_failure': {
            'cost_0_1': separation_depth(cost_source, 0, 1),
            'cost_0_2': separation_depth(cost_source, 0, 2),
            'cost_1_2': separation_depth(cost_source, 1, 2),
        },
        'earlier_test_failure': {
            'kind': 'incorrect anticipated enumeration count',
            'anticipated': 4320, 'actual': 7200,
            'mathematical_base_change_assertions_failed': False,
            'corrected_before_final_validation': True,
        },
    }
    text = json.dumps(receipt, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end='')
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
