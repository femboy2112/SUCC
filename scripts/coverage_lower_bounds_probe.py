#!/usr/bin/env python3
"""Exact, finite source-relative ObsSUCC coverage certificates (JSON receipt)."""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.coverage_lower_bounds import (
    uniform_frame, gaussian_frame, lattice_snake, block_coverage_audit,
    translation_audit, batch_coverage_lower_bound,
)


def show(f):
    return str(f)


def main():
    grid = lattice_snake(65)
    factors = ((1, 2), (1, -2), (2, 3), (2, -3))
    gauss = []
    for f in factors:
        frame = gaussian_frame(grid, f, '65x65 unit-step snake (NOT a prime walk)')
        report = frame.bound(F(1, 4))
        gauss.append({'factor': list(f), 'norm': f[0]**2+f[1]**2,
                      'chi2': show(frame.chi2),
                      'coverage_lower': show(report['lower_mass']),
                      'actual_coverage': show(report['good_mass']),
                      'undercovered': report['exception_count']})
    bad = uniform_frame('same source', 'one missing',
              (F(0), F(1, 4), F(1, 4), F(1, 4), F(1, 4)))
    good = uniform_frame('same source', 'full', (F(1, 5),) * 5)
    batch = batch_coverage_lower_bound((good,) * 99 + (bad,), F(1, 2), F(1, 5))
    collapse = translation_audit(tuple((x, (-x) % 5, F(1, 5)) for x in range(5)),
                                 5, 'controlled correlated-update countermodel')
    short = gaussian_frame(tuple((i, 0) for i in range(4)), (2, 3),
                           'four-point unit-step segment')
    blocks = []
    for n in (1, 2, 4, 16):
        r = block_coverage_audit(5, n)
        blocks.append({'blocks': n, 'steps': 4 * n,
                       'guaranteed_tau': show(r['tau']),
                       'minimum_probability': show(min(r['law'])),
                       'chi2': show(r['frame'].chi2)})
    output = {
        'status': 'exact finite certificate, classical theorem with SUCC source contracts',
        'rational_probabilities_only': True,
        'formal_lean_proof': False,
        'gaussian_moat_all_D_from_succ': False,
        'source_authentication': 'DECLARED, not physically attested',
        'sharp_reference_coverage': {'threshold': '1/2',
                 'formula': 'good_pi_mass >= (1-tau)^2/(chi2+(1-tau)^2)',
                 'missing_residue_example_chi2': show(bad.chi2),
                 'missing_residue_example_bound': show(bad.bound(F(1, 2))['lower_mass'])},
        'gaussian_full_grid_control': {'step_squared': 1,
                 'all_points_distinct': len(set(grid)) == len(grid),
                 'samples': len(grid), 'all_signed_coordinates': gauss,
                 'contains_nonprime_points': True},
        'gaussian_short_window_negative': {
            'norm': 13, 'samples': 4,
            'exact_collision_index': show(short.chi2),
            'uncovered_residues': short.bound(F(1, 4))['exception_count']},
        'batch_joint_collision': {k: show(v) for k, v in batch.items()},
        'source_dependent_update_control': {
            'initial_chi2': show(collapse['source'].chi2),
            'terminal_chi2': show(collapse['terminal'].chi2),
            'conditional_budget': show(collapse['conditional_energy']),
            'independent': collapse['independent_update']},
        'independent_succ_coverage_amplification': blocks,
    }
    assert output['gaussian_full_grid_control']['samples'] == 4225
    assert all(c['chi2'] == '0' for c in gauss)
    assert batch['coordinate_fraction_lower'] == F(24,25)
    assert collapse['terminal'].chi2 == 4
    print(json.dumps(output, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
