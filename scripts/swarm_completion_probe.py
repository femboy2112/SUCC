#!/usr/bin/env python3
"""Reproducible exact receipts for finite completion and source-memory debt."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.swarm_completion import (
    PartialEvidence, patch_tail, power_marker_patch, finite_refutation_search,
    verify_refutation, minimum_prefix_generator, marker_gap_bound, MooreSource,
)


def main():
    evidence = PartialEvidence(((0, 1), (3, 0), (100, 1)))
    tails = (patch_tail(evidence, (0,)), patch_tail(evidence, (1,)), power_marker_patch(evidence))
    words = ((0, 0, 0, 1), (0, 1, 0, 1, 0, 1), ('x', 'y', 'x', 'y', 'END'))
    machine = MooreSource((0, 1, 2), ('a',), (0, 0, 1), ((0,), (2,), (2,)))
    states = tuple(range(13))
    trace = lambda s, n: int(n == s*7)
    target = lambda n: 0
    refutation = finite_refutation_search(states, trace, target, range(100))
    receipt = {
        'status': 'EXACT_SWARM_B_COMPLETION_BOUNDARIES',
        'finite_refutation': refutation,
        'retained_witnesses_independently_replayed': verify_refutation(states, trace, target, refutation),
        'bounded_exhaustion_status': finite_refutation_search(states, trace, target, range(80))['status'],
        'scattered_observed_coordinates': [n for n, _ in evidence.entries],
        'all_three_hypothetical_completions_preserve_evidence': all(evidence.agrees(s) for s in tails),
        'hypothetical_completions_at_unobserved_128': [s(128) for s in tails],
        'sharp_prefix_state_counts': [{'word': w, 'states': minimum_prefix_generator(w)['state_count']} for w in words],
        'nonconstant_marker_gap': marker_gap_bound(words[-1], 0, 4),
        'same_report_future_separator': machine.separator(0, 1),
        'minimal_multi_action_class_count': len(machine.behavioral_classes()),
        'scope': {'physical_source_authenticated': False, 'infinite_experiment_performed': False,
                  'bounded_silence_certifies_global_realization': False, 'academic_priority_established': False},
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
