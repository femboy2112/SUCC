#!/usr/bin/env python3
"""Bounded Round II exact source obstruction and optional frozen spline trials."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import shlex
import subprocess
import sys
from time import monotonic

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import observer_schur_source as S


def encode(v):
    if isinstance(v, F):
        return str(v)
    raise TypeError(type(v).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--numerical', action='store_true')
    parser.add_argument('--fit-nodes', type=int, default=8)
    parser.add_argument('--holdout-nodes', type=int, default=16)
    parser.add_argument('--gamma-modes', type=int, default=512)
    parser.add_argument('--output', type=Path, default=ROOT/'research/2026-10-16/source-schur-exact.json')
    args = parser.parse_args()
    start = monotonic()
    before = S.source_snapshot()
    def git(*a):
        return subprocess.run(['git', *a], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()
    owned = ('observational_succ/observer_schur_source.py', 'scripts/observer_schur_source_probe.py')
    before_code = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in owned}
    out = {'schema': 'OBSERVER_SCHUR_SOURCE_ROUND_II_V1',
           'time_utc': datetime.now(timezone.utc).isoformat(),
           'command': shlex.join([sys.executable, *sys.argv]), 'cwd': str(ROOT),
           'python': platform.python_version(), 'git_head_at_start': git('rev-parse', 'HEAD'),
           'git_branch': git('branch', '--show-current'), 'source_snapshot': before,
           'owned_code_sha256': before_code,
           'source_sign': 'OPEN', 'RH_PROVED': False, 'kernel_proofs_created_by_this_probe': [],
           'exact_certificates': []}
    for kappa in (S.SHARPER_KAPPA, F(1, 10), F(1, 5)):
        r = S.certify_degree_eight_family(kappa, args.gamma_modes)
        out['exact_certificates'].append(r)
        print('degree-eight ALL coefficients', kappa, r['all_coefficients_criterion_fails'],
              'upper', None if r['criterion_uniform_upper_for_P2'] is None else float(r['criterion_uniform_upper_for_P2']), flush=True)
    out['source_high_kappa_ceiling'] = S.certified_high_kappa_ceiling(args.gamma_modes)
    print('source high kappa ceiling', float(out['source_high_kappa_ceiling']['every_valid_kappa_upper']), flush=True)
    out['certified_upper_short'] = S.certified_polynomial_upper_short(args.gamma_modes)
    print('certified S0 upper eigenvalue caps',
          {p: float(v['operator_eigenvalue_upper']) for p, v in out['certified_upper_short']['parity_operator_upper_caps'].items()}, flush=True)
    if args.numerical:
        import numpy as np
        import scipy
        import mpmath as mp
        from observational_succ.four_low_schur_proof_teeth import numerical_full_source_matrix
        out['versions'] = {'numpy': np.__version__, 'scipy': scipy.__version__, 'mpmath': mp.__version__}
        knots = (F(0), F(1, 16), F(1, 8), F(3, 16), F(193147, 10**6),
                 F(1, 4), F(5, 16), F(3, 8), F(7, 16), F(1, 2))
        basis = S.threshold_response_basis(knots)
        out['rational_trial_knots'] = knots
        out['rational_response_basis'] = basis
        print('building complete-source threshold-spline fit grid', len(basis), flush=True)
        fit = S.numerical_threshold_grid(basis, args.fit_nodes)
        fitted = {m: S.numerical_threshold_trial(basis, fit, m)
                  for m in ('galerkin', 'relative_least_squares', 'relative_optimal')}
        print('evaluating frozen rational trials on separate grid', flush=True)
        holdout = S.numerical_threshold_grid(basis, args.holdout_nodes)
        out['trials'] = []
        for method, t in fitted.items():
            fresh = S.numerical_threshold_trial(basis, holdout, method, t['frozen_rational_U'])
            out['trials'].append({'fit': t, 'frozen_holdout': fresh})
            print(method, 'holdout sectors', fresh['sectors'], flush=True)
        reference = numerical_full_source_matrix(4, 50)
        ref = np.asarray(reference['matrix_decimal'], dtype=float)
        out['independent_low_matrix_representation_check'] = {
            'reference': reference,
            'fit_max_discrepancy': float(np.max(abs(ref-fit['source_matrix'][:4, :4]))),
            'holdout_max_discrepancy': float(np.max(abs(ref-holdout['source_matrix'][:4, :4]))),
            'independent_source': False, 'rigorous_error_bound': False}
        out['grids'] = {name: {'nodes_per_panel': d['nodes_per_panel'], 'panels': d['panels'],
                               'source_matrix': d['source_matrix'].tolist(),
                               'quotient_Gram': d['quotient_gram'].tolist(),
                               'raw_matrix_asymmetry': d['raw_matrix_asymmetry'],
                               'rigorous_continuum_error_bound': False}
                        for name, d in (('fit', fit), ('holdout', holdout))}
        out['source_channel_mutations'] = S.numerical_channel_mutations()
    out['source_bytes_unchanged'] = before == S.source_snapshot()
    out['owned_code_bytes_unchanged'] = before_code == {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in owned}
    out['elapsed_seconds'] = monotonic()-start
    if not out['source_bytes_unchanged'] or not out['owned_code_bytes_unchanged']:
        raise RuntimeError('source or own implementation changed during replay')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, default=encode, indent=2)+'\n')
    if not all(c['all_coefficients_criterion_fails'] for c in out['exact_certificates']):
        print('at least one requested exact certificate unresolved; no original sign claim', flush=True)
        return 1
    print('receipt', args.output, 'elapsed', out['elapsed_seconds'], 'RH_PROVED: NO', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
