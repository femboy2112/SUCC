#!/usr/bin/env python3
"""Real signed-source Swarm D probe; numerical outputs never certify RH/sign."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import platform
import shlex
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import four_low_schur_proof_teeth as T


def encode(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)


def git(*args):
    p = subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True)
    return {'returncode': p.returncode, 'stdout': p.stdout.strip(), 'stderr': p.stderr.strip()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'research/2026-10-15/four_low_schur_proof_teeth_receipts/probe.json')
    parser.add_argument('--rank', type=int, default=20)
    parser.add_argument('--fit-nodes', type=int, default=24)
    parser.add_argument('--holdout-nodes', type=int, default=48)
    args = parser.parse_args()
    import numpy as np
    import mpmath as mp
    import scipy
    start = monotonic()
    before = T.source_snapshot()
    receipt = {'schema': 'SWARM_D_FOUR_LOW_SCHUR_PROOF_TEETH_V1',
               'time_utc': datetime.now(timezone.utc).isoformat(),
               'command': shlex.join([sys.executable, *sys.argv]),
               'cwd': str(Path.cwd()), 'python': platform.python_version(),
               'versions': {'numpy': np.__version__, 'mpmath': mp.__version__, 'scipy': scipy.__version__},
               'git_head': git('rev-parse', 'HEAD'), 'git_branch': git('branch', '--show-current'),
               'git_status_before': git('status', '--short'),
               'PR85_origin_blob': git('rev-parse', 'dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc:observational_succ/source_weil_hierarchy.py'),
               'source': before, 'source_sign': 'OPEN', 'RH_PROVED': False}
    print('Recomputing inherited exact source bounds', flush=True)
    receipt['certified_scalar_improvement'] = T.certified_scalar_improvement()
    print('Computing complete signed source matrix and independent quadrature', flush=True)
    full = T.numerical_full_source_matrix(args.rank, 60)
    fresh = T.numerical_full_source_matrix(min(args.rank, 12), 80)
    size = min(args.rank, 12)
    with mp.workdps(90):
        diff = max(abs(mp.mpf(full['matrix_decimal'][i][j])-mp.mpf(fresh['matrix_decimal'][i][j]))
                   for i in range(size) for j in range(size))
        receipt['precision_crosscheck'] = {'digits': [60, 80], 'rank': size,
                                         'maximum_difference': mp.nstr(diff, 20),
                                         'independent_source': False, 'rigorous_bound': False}
    receipt['full_source_numeric'] = full
    fit = T.numerical_derivative_grid(args.rank, args.fit_nodes)
    holdout = T.numerical_derivative_grid(args.rank, args.holdout_nodes)
    receipt['derivative_quadrature'] = {
        label: {'nodes_per_panel': d['nodes_per_panel'], 'x': d['x'].tolist(),
                'weights': d['weights'].tolist(), 'derivatives': d['derivatives'].tolist(),
                'estimated_inner_errors': d['estimated_inner_errors'], 'rigorous_error_bound': False}
        for label, d in (('fit', fit), ('holdout', holdout))}
    receipt['trials'] = []
    for rank in [n for n in (4, 6, 8, 12, 20) if n <= args.rank]:
        for method in ('galerkin', 'quotient_least_squares'):
            a = T.numerical_trial(full, fit, rank, method)
            frozen = np.asarray(a['U']).reshape(rank-4, 4)
            b = T.numerical_trial(full, holdout, rank, method, frozen_U=frozen)
            receipt['trials'].append({'fit': a, 'holdout_frozen_trial': b})
            print(rank, method, 'upper min', min(b['upper_eigenvalues']),
                  'quotient lower min', min(b['quotient_lower_eigenvalues']), flush=True)
    receipt['finite_Gamma_stages'] = []
    for J in (16, 32, 64):
        stage = T.source_low_intervals(8, J)
        norms = np.sqrt(2*np.arange(1, 9)+1)
        g = np.array([[float(z.mid()) for z in row] for row in stage['matrix']])
        g = norms[:, None]*g*norms[None, :]
        u = np.linalg.solve(g[4:, 4:], g[4:, :4])
        receipt['finite_Gamma_stages'].append({
            'J': J, 'intervals': [[(z.lo, z.hi) for z in row] for row in stage['matrix']],
            'positive_tail_operator_upper': stage['positive_tail_operator_upper'],
            'midpoint_schur_eigenvalues_NUMERICAL': np.linalg.eigvalsh(g[:4, :4]-g[:4, 4:]@u).tolist(),
            'full_source_sign_certified': False})
    print('Certifying source-specific zero-trial obstructions', flush=True)
    obstructions = []
    for i, j in ((1, 5), (2, 6), (3, 5), (4, 6)):
        v, q = [0]*6, [0]*6
        v[i-1], q[j-1] = 1, 1
        obstructions.append(T.certified_trial_obstruction(v, q))
    receipt['certified_zero_trial_obstructions'] = obstructions
    # Freeze an actual rank-8 Galerkin column as rational coefficients.
    # q is chosen from a disjoint higher mode; selection is not a proof.
    # The subsequent outward source calculation is the certificate, if strict.
    galerkin = next(t['fit'] for t in receipt['trials']
                   if t['fit']['rank'] == 8 and t['fit']['trial'] == 'galerkin')
    U = np.array(galerkin['U'])
    selected = []
    for low, high in ((2, 10), (4, 10), (1, 9), (3, 9)):
        v, q = [F()]*10, [F()]*10
        v[low-1] = F(1)
        for j in range(4, 8):
            # e_low=sqrt(2low+1) P_low, so divide response by its normalization.
            val = -U[j-4, low-1]*np.sqrt((2*j+3)/(2*low+1))
            v[j] = F(round(float(val)*10**9), 10**9)
        q[high-1] = F(1)
        selected.append(T.certified_trial_obstruction(v, q))
    receipt['certified_frozen_Galerkin_trial_obstructions'] = selected
    receipt['source_specific_controls'] = T.source_specific_controls(full)
    receipt['source_bytes_unchanged_during_probe'] = before == T.source_snapshot()
    if not receipt['source_bytes_unchanged_during_probe']:
        raise RuntimeError('source drift during source-matched experiment')
    receipt['elapsed_seconds'] = monotonic()-start
    receipt['own_code_sha256'] = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in (
        'observational_succ/four_low_schur_proof_teeth.py',
        'scripts/four_low_schur_proof_teeth_probe.py')}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, default=encode, indent=2)+'\n')
    print('receipt', args.output, 'seconds', receipt['elapsed_seconds'], 'RH_PROVED: NO', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
