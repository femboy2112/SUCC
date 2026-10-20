#!/usr/bin/env python3
"""Fresh signed-source replay plus a new polynomial-constraint inverse saving."""
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
from observational_succ import original_continuum_residual as R
from observational_succ import full_prime_resolvent as F
from observational_succ.cloud_operator_transport import moment_constraint_saving


def compact_lower(matrix, denominator=10**18):
    """Directed row-radius rounding is a Loewner lower, not entrywise optimism."""
    mid = tuple(tuple(Q((x.numerator*denominator)//x.denominator, denominator)
                      for x in row) for row in matrix)
    return tuple(tuple(mid[i][j]-(sum((abs(matrix[i][k]-mid[i][k])
                                      for k in range(len(mid))), Q()) if i == j else 0)
                       for j in range(len(mid))) for i in range(len(mid)))


def grid_lower(matrix, denominator=10**18):
    """Fully bounded-size matrix: floor entries, pay n/grid on diagonal."""
    size = len(matrix)
    return tuple(tuple(Q((x.numerator*denominator)//x.denominator, denominator)
                       -(Q(size,denominator) if i==j else 0)
                       for j,x in enumerate(row)) for i,row in enumerate(matrix))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--J', type=int, default=8)
    parser.add_argument('--M', type=int, default=80)
    args = parser.parse_args()
    start = time.monotonic()
    baseline = F.source_schur_improvement(J=args.J, M=args.M)
    params = R.source_parameters()  # checks frozen source pin and genuine tape
    sectors = {}
    for name, data in baseline['sectors'].items():
        indices = (1,3) if name == 'odd_derivative' else (2,4)
        primitive_parity = 'even' if name == 'odd_derivative' else 'odd'
        projected = []
        for index, coefficient in zip(indices, data['fitted_high_coefficients']):
            h = R.high_boundary_match(index, Q(coefficient))['h']
            packet = R.exact_piecewise_primitive_action(h, args.J, args.M, 18, params)
            projected.append(F.project_pieces(packet['pieces']))
        saving = moment_constraint_saving(projected, params['b'], params['db'],
                                           data['kappa'], primitive_parity)
        gain_exact = tuple(tuple((1+baseline['eta'])*x for x in row)
                           for row in saving['constraint_saving_lower'])
        gain = grid_lower(gain_exact)
        old = grid_lower(data['new_lower'])
        new = tuple(tuple(old[i][j]+gain[i][j] for j in range(2)) for i in range(2))
        # All sign decisions use exact Fractions on rigorous matrix lowers.
        sectors[name] = {
            'primitive_parity': primitive_parity,
            'old_lower': old, 'new_lower': new, 'additional_gain_lower': gain,
            'gain_positive_definite': F.matrix_pd(gain),
            'new_lower_positive_semidefinite': F.matrix_psd(new),
            'new_lower_negative_definite': F.matrix_pd(tuple(tuple(-x for x in row) for row in new)),
            'moment_shift_error_upper': [[str(Q((x.numerator*10**18)//x.denominator+1,10**18))
                                         for x in row]for row in saving['moment_error_bounds']],
            'constraint_norms': saving['constraint_norms'],
            'theta': saving['theta'], 'kappa': data['kappa'],
            'fitted_high_coefficients': data['fitted_high_coefficients'],
        }
    paths = ['observational_succ/source_weil_hierarchy.py',
             'observational_succ/original_continuum_residual.py',
             'observational_succ/full_prime_resolvent.py',
             'observational_succ/cloud_operator_transport.py',
             'scripts/cloud_operator_source_probe.py']
    result = {
        'program': 'CLOUD_OPERATOR_CONSTRAINED_PRIMITIVE_INVERSE',
        'baseline_main': '0e56e0ae26f3d52a2ea34c0a4288478139fcb634',
        'source_blob': F.SOURCE_BLOB, 'J': args.J, 'M': args.M, 'P': 18,
        'source_code_introduction': 'b0cef75f47de29b1326b351df35b9e5423f2ed4f',
        'source_import_manifest_member': False,
        'baseline_recomputed': True,
        'source_parameters': {k:params[k]for k in ('b','db','w','dw','contact','dc')},
        'sectors': sectors,
        'all_gain_lowers_positive_definite': all(v['gain_positive_definite']for v in sectors.values()),
        'first_window_sign_certified': all(v['new_lower_positive_semidefinite']for v in sectors.values()),
        'RH_proved': False,
        'authority': 'paper theorem with exact rational source instance; no formal kernel proof',
        'source_shared_with_baseline': True,
        'independence': 'new constrained variational proof and separate polynomial pairing implementation; inherited source/trials/errors',
        'sha256': {p:sha256((ROOT/p).read_bytes()).hexdigest()for p in paths},
        'execution': {'python': sys.version, 'elapsed_seconds': time.monotonic()-start,
                      'argv':sys.argv},
    }
    Path(args.output).write_text(json.dumps(result, default=str, sort_keys=True, indent=2)+'\n')
    print(json.dumps({'all_gain_lowers_positive_definite': result['all_gain_lowers_positive_definite'],
                      'first_window_sign_certified': result['first_window_sign_certified'],
                      'sectors': {k:{'gain':[[float(x)for x in row]for row in v['additional_gain_lower']],
                                    'new_lower':[[float(x)for x in row]for row in v['new_lower']]}
                                  for k,v in sectors.items()}},sort_keys=True))


if __name__ == '__main__':
    main()
