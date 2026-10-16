#!/usr/bin/env python3
"""Serial exact spectral-response replay; --output PATH is always required."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha1, sha256
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
from observational_succ import spectral_response as S

SOURCE_PATH = 'observational_succ/source_weil_hierarchy.py'
SOURCE_BLOB = '0cc8510b71d178fc79e8d410a86d8b6014cf9178'
SOURCE_SHA256 = '183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b'
SOURCE_COMMIT = 'dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc'
OWN_PATHS = (
    'observational_succ/spectral_response.py',
    'tests/test_spectral_response.py',
    'scripts/spectral_response_probe.py',
    'research/2026-10-16/SPECTRAL_RESPONSE_MEASURE.md',
)
READ_PATHS = (
    'AGENTS.md', 'docs/METHOD.md', 'provenance/IMPORT_MANIFEST.json',
    'observational_succ/recursive_operator_gluing.py',
    'observational_succ/observer_schur.py', 'observational_succ/compact_galerkin.py',
    'research/2026-10-16/OBSERVER_SCHUR_ROUND_II.md',
    'research/2026-10-16/OBSERVER_SCHUR_THEOREMS.md',
    'research/2026-10-16/OBSERVER_SCHUR_SOURCE.md',
    'research/2026-10-16/COMPACT_SOURCE_GALERKIN.md',
)


def hashes(paths):
    return {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}


def source_pins():
    data = (ROOT/SOURCE_PATH).read_bytes()
    return {'path': SOURCE_PATH, 'origin_commit': SOURCE_COMMIT,
            'expected_git_blob': SOURCE_BLOB, 'expected_sha256': SOURCE_SHA256,
            'live_git_blob': sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
            'live_sha256': sha256(data).hexdigest()}


def git(*args):
    result = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)
    return {'returncode': result.returncode, 'stdout': result.stdout.strip(),
            'stderr': result.stderr.strip()}


def encode(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)


def finite_evidence():
    model = S.SpectralMeasure.from_diagonal(
        (F(1, 16), F(1, 4), 1), ((F(1, 4), -F(1, 2)), (F(1, 3), F(2, 3)), (-1, 1)))
    aliases = []
    for order in (0, 2, 5):
        for scale in (8, 128, 8192):
            epsilon = F(1, (order+1)*scale)
            base, alternative = S.matched_moment_measures(order, epsilon)
            aliases.append({
                'order': order, 'epsilon': epsilon,
                'base_atoms': base.atoms, 'alternative_atoms': alternative.atoms,
                'base_moments': [base.moment(k) for k in range(order+1)],
                'alternative_moments': [alternative.moment(k) for k in range(order+1)],
                'base_inverse': base.response(), 'alternative_inverse': alternative.response(),
                'base_shifted': base.response(epsilon),
                'alternative_shifted': alternative.response(epsilon),
                'status': 'EXACT_FINITE_COMPUTATION; infinite family proved in SR-06',
            })
    weak = S.SpectralMeasure.from_diagonal((F(1, 4), F(1, 2), 1),
                                          ((F(1, 4),), (F(1, 2),), (1,)))
    return {
        'matrix_measure': {'atoms': model.atoms, 'R0': model.response(),
                           'R_quarter': model.response(F(1, 4)),
                           'shift_gap': model.shift_gap(F(1, 4)),
                           'completion_gap': model.completion_gap(F(1, 4)),
                           'stieltjes_parts': model.stieltjes_tail_parts(F(1, 4)),
                           'inverse_tail': model.inverse_tail(F(1, 4)),
                           'fractional_alpha_one': model.fractional_bounds(1, F(1, 4), F(1, 4))},
        'weak_mass': {'atoms': weak.atoms, 'alpha': 1, 'ceiling': ((2,),),
                      'cutoff': 1, 'inverse_tail': weak.inverse_tail(1),
                      'certified_upper': weak.weak_mass_bound(1, ((2,),), 1)},
        'slow_tail': [dict(S.slow_tail_enclosure(64, F(1, 4**n)),
                           n=n, paper_shift_lower=F(1, 2*n), paper_trial_lower=F(1, 4*n))
                      for n in (1, 4, 16, 32)],
        'moment_aliases': aliases,
        'tiny_perturbations': [S.tiny_coupling_counterexample(n) for n in (4, 16, 64)],
        'rejected_routes': [
            'Square-root range or compactness implies a positive power rate: SR-05 refutes.',
            'Finite exact positive moments give a universal inverse upper bound: SR-06 refutes.',
            'Small operator-norm perturbations control the zero short: SR-07 refutes.',
            'A finite fractional Gram proves the infinite source range: not established.',
            'A sharp irrational constant can be certified by a float: API refuses.',
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    # Avoid accidental overwriting of a source/input while still permitting
    # the principal to choose its own receipt directory.
    output = args.output.resolve()
    if output in {ROOT/p for p in OWN_PATHS+READ_PATHS+(SOURCE_PATH,)}:
        parser.error('--output cannot overwrite an input file')
    start = monotonic()
    before, inherited_before, pins = hashes(OWN_PATHS), hashes(READ_PATHS), source_pins()
    origin = git('rev-parse', SOURCE_COMMIT+':'+SOURCE_PATH)
    pinned = (pins['live_git_blob'] == SOURCE_BLOB and pins['live_sha256'] == SOURCE_SHA256
              and origin['returncode'] == 0 and origin['stdout'] == SOURCE_BLOB)
    receipt = {
        'schema': 'ARITHMETIC_RESONANCE_SPECTRAL_RESPONSE_V1',
        'status': 'RUNNING', 'evidence': {}, 'source_pins': pins,
        'authority': {'paper': 'SR-01..04 conditional; SR-05..07 counterexamples',
                      'computation': 'EXACT_FINITE_RATIONAL_AND_SPECIFIED_SERIES_ENCLOSURES',
                      'experiment': 'NO_FLOAT_EXPERIMENT_USED_AS_CERTIFICATE',
                      'formal_kernel_proof': False, 'genuine_fractional_source_range': 'UNVERIFIED',
                      'original_S0_sign': 'OPEN', 'RH_PROVED': False},
        'execution': {'time_utc': datetime.now(timezone.utc).isoformat(),
                      'command': shlex.join([sys.executable, *sys.argv]),
                      'cwd': str(Path.cwd()), 'python': platform.python_version(),
                      'executable': sys.executable,
                      'git_head': git('rev-parse', 'HEAD'),
                      'git_branch': git('branch', '--show-current'),
                      'git_status_before': git('status', '--short'),
                      'source_origin_check': origin,
                      'environment': {k: os.environ.get(k) for k in (
                          'OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                          'PYTHONDONTWRITEBYTECODE')},
                      'full_suite_run': False, 'full_suite_owner': 'principal',
                      'git_writes_performed': False},
        'own_sha256_before': before, 'read_sha256_before': inherited_before,
    }
    success = False
    if pinned:
        receipt['evidence'] = finite_evidence()
        stream = io.StringIO()
        suite = unittest.defaultTestLoader.discover(str(ROOT/'tests'), pattern='test_spectral_response.py')
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
        receipt['tests'] = {'run': result.testsRun, 'failures': len(result.failures),
                            'errors': len(result.errors), 'skipped': len(result.skipped),
                            'successful': result.wasSuccessful(), 'output': stream.getvalue()}
        print(stream.getvalue(), end='')
        success = result.wasSuccessful() and not result.skipped and result.testsRun > 0
    else:
        receipt['tests'] = {'run': 0, 'successful': False, 'reason': 'SOURCE_PIN_MISMATCH'}
    after, inherited_after = hashes(OWN_PATHS), hashes(READ_PATHS)
    receipt['own_sha256_after'] = after
    receipt['read_sha256_after'] = inherited_after
    receipt['source_pins_after'] = source_pins()
    receipt['preservation'] = {'source_pin_matches': pinned,
                               'own_bytes_unchanged': before == after,
                               'read_bytes_unchanged': inherited_before == inherited_after,
                               'source_bytes_unchanged': pins == receipt['source_pins_after']}
    success = success and all(receipt['preservation'].values())
    receipt['status'] = 'PASS' if success else 'FAIL'
    receipt['execution']['exit_code'] = int(not success)
    receipt['execution']['elapsed_seconds'] = monotonic()-start
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, default=encode, indent=2)+'\n')
    print('status:', receipt['status'], 'receipt:', output)
    print('Genuine fractional range: UNVERIFIED. Original S0: OPEN. RH: NOT PROVED.')
    return int(not success)


if __name__ == '__main__':
    raise SystemExit(main())
