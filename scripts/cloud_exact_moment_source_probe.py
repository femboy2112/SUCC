#!/usr/bin/env python3
"""Held-out exact Gram-inverse gain on the pinned original signed source."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import cloud_exact_moment_inverse as E
from observational_succ import full_prime_resolvent as F
from observational_succ import original_continuum_residual as R


def grid_lower(a, denominator=10**18):
    return tuple(tuple(Q((x.numerator*denominator)//x.denominator, denominator)
                       -(Q(2, denominator) if i == j else 0)
                       for j, x in enumerate(row)) for i, row in enumerate(a))


def upper_scalar(x, denominator=10**24):
    return Q(-((-x.numerator*denominator)//x.denominator), denominator)


def lower_scalar(x, denominator=10**24):
    return Q((x.numerator*denominator)//x.denominator, denominator)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--J', type=int, default=10)
    parser.add_argument('--M', type=int, default=96)
    parser.add_argument('--cells', type=int, default=32)
    parser.add_argument('--source-holdout-output')
    args = parser.parse_args()
    start = time.monotonic()
    print('Recomputing complete signed-source baseline and all-high budget.', flush=True)
    baseline = F.source_schur_improvement(J=args.J, M=args.M)
    parameters = R.source_parameters()
    sectors = {}
    for name, data in baseline['sectors'].items():
        print('Certifying exact finite-moment inverse: '+name, flush=True)
        indices, parity = ((1, 3), 'even') if name == 'odd_derivative' else ((2, 4), 'odd')
        projected = []
        for index, coefficient in zip(indices, data['fitted_high_coefficients']):
            h = R.high_boundary_match(index, Q(coefficient))['h']
            packet = R.exact_piecewise_primitive_action(h, args.J, args.M, 18, parameters)
            projected.append(F.project_pieces(packet['pieces']))
        result = E.exact_moment_constraint_saving(projected, parameters['b'],
                    parameters['db'], data['kappa'], parity, cells=args.cells)
        if not all(result[p+'_weight_excess_psd'] for p in ('exact', 'quadrature')):
            raise ArithmeticError('source parameters do not support claimed additive gain')
        factor = 1+baseline['eta']
        prior = result['previous_certificate']
        prior_lower = grid_lower(E.matrix_add(data['new_lower'],
                    tuple(tuple(factor*x for x in row) for row in prior['constraint_saving_lower'])))
        details = {}
        for prefix in ('exact', 'quadrature'):
            gain = grid_lower(tuple(tuple(factor*x for x in row)
                    for row in result[prefix+'_additional_saving_lower']))
            new = E.matrix_add(prior_lower, gain)
            details[prefix] = {'additional_gain_lower': gain,
                'gain_positive_definite': E.matrix_pd(gain),
                'new_schur_lower': new, 'new_schur_lower_psd': E.matrix_psd(new),
                'negative_definite_lower_only': E.matrix_pd(tuple(tuple(-x for x in row) for row in new)),
                'weight_excess': result[prefix+'_weight_excess'],
                'weight_excess_positive_definite': E.matrix_pd(result[prefix+'_weight_excess']),
                'additional_error_penalty_upper': upper_scalar(result[prefix+'_additional_error_penalty'])}
        gram = result['gram_certificate']
        # B_b <= (kappa+2w)I implies M_b >= G/(kappa+2w).
        # This bounds the COMPLETE two-moment saving from above, independent
        # of how accurately its inverse is computed. Keep the old ambient
        # estimate and action-error budget fixed when interpreting this cap.
        moment_abs_upper = tuple(tuple(upper_scalar(abs(x)) for x in row)
            for row in prior['nominal_inverse_moments'])
        moment_error_upper = tuple(tuple(upper_scalar(x) for x in row)
            for row in prior['moment_error_bounds'])
        ambient_diagonal_upper = tuple(upper_scalar(data['new_lower'][i][i]) for i in range(2))
        maximal_constraint_diagonal = tuple(upper_scalar((data['kappa']+Q(24, 25))*sum(
            ((moment_abs_upper[j][i]+moment_error_upper[j][i])**2/prior['constraint_norms'][j]
              for j in range(2)), Q())) for i in range(2))
        fixed_budget_diagonal_ceiling = tuple(upper_scalar(ambient_diagonal_upper[i]
             + factor*maximal_constraint_diagonal[i]) for i in range(2))
        sectors[name] = {'primitive_parity': parity, 'kappa': data['kappa'],
            'old_diagonal_constraint_schur_lower': prior_lower,
            'gram_upper': gram['gram_upper'],
            'quadrature_gram_upper': gram['quadrature_gram_upper'],
            'quadrature_enclosures_verified': gram['independent_quadrature_enclosures_verified'],
            'quadrature_entry_error_upper': tuple(tuple(upper_scalar(x) for x in row)
                for row in gram['quadrature_errors']),
            'shift_gram_operator_radius_upper': upper_scalar(gram['shift_operator_radius']),
            'inverse_moment_error_upper': moment_error_upper,
            'nominal_inverse_moment_absolute_upper': moment_abs_upper,
            'constraint_norms': prior['constraint_norms'],
            'fixed_ambient_schur_diagonal_upper': ambient_diagonal_upper,
            'fitted_high_coefficients': data['fitted_high_coefficients'],
            'finite_source_error_upper': tuple(upper_scalar(Q(x)) for x in data['unchanged_finite_source_errors']),
            'omitted_Gamma_action_error_upper': tuple(upper_scalar(Q(x)) for x in data['unchanged_Gamma_tail_errors']),
            'complete_constraint_diagonal_upper': tuple(upper_scalar(x) for x in maximal_constraint_diagonal),
            'fixed_ambient_error_budget_diagonal_ceiling': fixed_budget_diagonal_ceiling,
            'constraint_refinement_alone_cannot_close_fixed_budget': any(x < 0 for x in fixed_budget_diagonal_ceiling),
            'theta': result['theta'], **details}
    source_holdout = None
    if args.source_holdout_output:
        print('Independent source matrix/action holdout at J=6, M=72.', flush=True)
        holdout = R.frozen_operator_matrix_holdout(J=6, M=72, P=18)
        holdout['genealogy_correction'] = (
            'Pinned SUCC source introduced at b0cef75f47de29b1326b351df35b9e5423f2ed4f; '
            'not a member of the 72-file IMPORT_MANIFEST. Two implementations share this source.')
        holdout_path = Path(args.source_holdout_output)
        holdout_path.write_text(json.dumps(holdout, default=str, sort_keys=True, indent=2)+'\n')
        source_holdout = {'path': str(holdout_path), 'sha256': sha256(holdout_path.read_bytes()).hexdigest(),
            'J': 6, 'M': 72, 'all_signed_channels_agree_within_rigorous_errors': True}
    paths = ['observational_succ/source_weil_hierarchy.py',
        'observational_succ/original_continuum_residual.py',
        'observational_succ/full_prime_resolvent.py',
        'observational_succ/cloud_operator_transport.py',
        'observational_succ/cloud_exact_moment_inverse.py',
        'scripts/cloud_exact_moment_source_probe.py',
        'tests/test_cloud_exact_moment_inverse.py']
    result = {'program': 'CLOUD_EXACT_MOMENT_GRAM_INVERSE',
        'audit_parent_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'source_blob': F.SOURCE_BLOB, 'source_import_manifest_member': False,
        'source_introduction': 'b0cef75f47de29b1326b351df35b9e5423f2ed4f',
        'J': args.J, 'M': args.M, 'P': 18, 'eta': baseline['eta'],
        'independent_Simpson_cells_per_piece': args.cells,
        'baseline_recomputed': True, 'source_holdout': source_holdout,
        'b_nominal': parameters['b'], 'b_uncertainty_upper': upper_scalar(parameters['db']),
        'all_high_comparison': {p: {'kappa': packet['kappa'],
            'source_margin_lower': lower_scalar(packet['exact_margin']),
            'prime_weight_floor': packet['prime_surplus_weight_floor']}
            for p, packet in baseline['source_high_budget_audit'].items()},
        'sectors': sectors,
        'both_exact_gains_positive_definite': all(s['exact']['gain_positive_definite'] for s in sectors.values()),
        'both_quadrature_gains_positive_definite': all(s['quadrature']['gain_positive_definite'] for s in sectors.values()),
        'first_window_sign_certified': all(s['exact']['new_schur_lower_psd'] for s in sectors.values()),
        'RH_proved': False, 'formal_verification': False,
        'authority': 'paper theorem; exact rational source instance; no metadata or finite-matrix promotion',
        'independence': ('Exact antiderivative versus certified composite Simpson for finite Gram; '
            'separate original-source matrix/action implementations at held-out depth; '
            'source identity, all-high theorem, trials, and action errors remain shared dependencies.'),
        'sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'execution': {'python': sys.version, 'argv': sys.argv, 'elapsed_seconds': time.monotonic()-start}}
    Path(args.output).write_text(json.dumps(result, default=str, sort_keys=True, indent=2)+'\n')
    print(json.dumps({'both_exact_gains_positive_definite': result['both_exact_gains_positive_definite'],
        'both_quadrature_gains_positive_definite': result['both_quadrature_gains_positive_definite'],
        'first_window_sign_certified': result['first_window_sign_certified'],
        'display_only_decimals': {name: {'gain': [[float(x) for x in row] for row in s['exact']['additional_gain_lower']],
            'new_lower': [[float(x) for x in row] for row in s['exact']['new_schur_lower']]}
            for name, s in sectors.items()}}, sort_keys=True))


if __name__ == '__main__':
    main()
