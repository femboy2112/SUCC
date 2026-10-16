#!/usr/bin/env python3
"""Serial exact compact/Galerkin lane replay, including only its focused tests."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import io
import json
import os
from pathlib import Path
import platform
import shlex
import subprocess
import sys
from time import monotonic
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import compact_galerkin as C

OWN_PATHS = (
    'observational_succ/compact_galerkin.py',
    'tests/test_compact_galerkin.py',
    'scripts/compact_galerkin_probe.py',
    'research/2026-10-16/COMPACT_SOURCE_GALERKIN.md',
)


def git(*args):
    result = subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True)
    return {'returncode': result.returncode, 'stdout': result.stdout.strip(),
            'stderr': result.stderr.strip()}


def own_hashes():
    return {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in OWN_PATHS}


def encode(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    start = monotonic()
    source = C.source_snapshot()
    before = own_hashes()
    old = json.loads((ROOT/'research/2026-10-15/proof_teeth_receipts/'
                     'schur-declared-environment.json').read_text())
    for p, digest in source['sha256'].items():
        inherited = old['source']['sha256'].get(p, old['own_code_sha256'].get(p))
        if digest != inherited:
            raise RuntimeError('inherited source/receipt hash mismatch: '+p)
    receipt = {
        'schema': 'COMPACT_SOURCE_GALERKIN_ROUND_II_V1',
        'time_utc': datetime.now(timezone.utc).isoformat(),
        'command': shlex.join([sys.executable, *sys.argv]),
        'cwd': str(Path.cwd()), 'python': platform.python_version(),
        'environment': {key: os.environ.get(key) for key in (
            'OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'PYTHONDONTWRITEBYTECODE')},
        'git_head': git('rev-parse', 'HEAD'),
        'git_branch': git('branch', '--show-current'),
        'origin_source_blob': git('rev-parse',
            'dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc:observational_succ/source_weil_hierarchy.py'),
        'source': source, 'matches_inherited_source_receipt': True,
        'own_sha256': before,
        'proof_authority': 'PAPER_PROVED; exact executions support only their stated finite/enclosure scope',
        'formal_kernel_proofs_run_by_this_lane': [],
        'compact_source_bounds': [C.source_legendre_bound(n, 64) for n in (4, 20, 100, 1000)],
        'noncompact_control': C.diagonal_compression_control(100, 0),
        'compact_control': C.diagonal_compression_control(100, 2),
        'zero_shift_discontinuity': [C.zero_shift_discontinuity(n) for n in (4, 16, 64)],
        'fixed_source_graph_blocks': [C.graph_failure_block(j) for j in (1, 4, 8)],
        'fixed_source_graph_stages': [C.graph_failure_stage(j, complete)
                                     for j in (1, 4, 8) for complete in (False, True)],
        'clamped_range_gap': [C.clamped_polynomial_control((0, 0, c, -2*c, c))
                              for c in (F(), F(1, 24), -F(1, 5))],
        'conditional_Gamma_matrix_bound': C.gamma_residual_gram_upper(
            ((1, 0), (0, 2)), ((1, 0), (0, 3)), 64, F(1, 10)),
        'original_four_low_S0_sign': 'OPEN', 'RH_PROVED': False,
        'full_suite_run': False, 'git_writes_performed_by_lane': False,
    }
    output = io.StringIO()
    suite = unittest.defaultTestLoader.discover(str(ROOT/'tests'), pattern='test_compact_galerkin.py')
    result = unittest.TextTestRunner(stream=output, verbosity=2).run(suite)
    receipt['focused_tests'] = {'run': result.testsRun, 'failures': len(result.failures),
                                'errors': len(result.errors), 'skipped': len(result.skipped),
                                'successful': result.wasSuccessful(), 'output': output.getvalue()}
    receipt['source_bytes_unchanged'] = source == C.source_snapshot()
    receipt['own_bytes_unchanged'] = before == own_hashes()
    receipt['elapsed_seconds'] = monotonic()-start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, default=encode, indent=2)+'\n')
    print(output.getvalue(), end='')
    print('receipt:', args.output)
    print('source stable:', receipt['source_bytes_unchanged'],
          'own files stable:', receipt['own_bytes_unchanged'])
    print('Original S0: OPEN. RH PROVED: NO.')
    return int(not (result.wasSuccessful() and receipt['source_bytes_unchanged']
                   and receipt['own_bytes_unchanged']))


if __name__ == '__main__':
    raise SystemExit(main())
