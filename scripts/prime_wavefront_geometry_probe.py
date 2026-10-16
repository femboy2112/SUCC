#!/usr/bin/env python3
"""Serial wavefront evidence probe. No writes unless --output PATH is given."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha1, sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import time

# Also prevent imported modules from writing bytecode when invoked without -B.
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ import prime_wavefront_geometry as W
from observational_succ import suzuki_legendre_source as L
from observational_succ import source_weil_hierarchy as S

PIN = '0cc8510b71d178fc79e8d410a86d8b6014cf9178'
BASE = '24d0f18a103fb2add32ee817fdfefb4ff401ed27'
FILES = (
    'observational_succ/source_weil_hierarchy.py',
    'observational_succ/suzuki_legendre_source.py',
    'observational_succ/suzuki_moment_schur.py',
    'provenance/IMPORT_MANIFEST.json',
    'observational_succ/prime_wavefront_geometry.py',
    'tests/test_prime_wavefront_geometry.py',
    'scripts/prime_wavefront_geometry_probe.py',
    'research/2026-10-16/PRIME_WAVEFRONT_HILBERT_SCHMIDT.md',
)
TEST_MODULES = (
    'tests.test_prime_wavefront_geometry',
    'tests.test_hilbert_prime_hinge_integrals',
    'tests.test_hilbert_prime_wavefront',
    'tests.test_suzuki_legendre_source',
    'tests.test_suzuki_prime_boundary',
)


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(type(value).__name__)


def file_pins():
    pins = {}
    for relative in FILES:
        data = (ROOT/relative).read_bytes()
        pins[relative] = {'sha256': sha256(data).hexdigest(),
                          'git_blob': sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
    return pins


def command(args, timeout=120):
    start = time.monotonic()
    completed = subprocess.run(args, cwd=ROOT, capture_output=True, text=True,
                               timeout=timeout, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1',
                                                     'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'})
    return {'argv': args, 'exit_code': completed.returncode,
            'stdout': completed.stdout, 'stderr': completed.stderr,
            'elapsed_seconds': round(time.monotonic()-start, 6)}


def evidence():
    a = Q(1, 2)
    hinges = (W.Hinge(Q(1, 4), -1), W.Hinge(Q(2, 3), Q(3, 2)))
    columns = tuple(L.legendre_polynomial(i, a) for i in (1, 2, 3, 4))
    before = W.derivative_response(a, (0, 1), (W.Hinge(Q(2, 3)),), output_modes=(1, 2))
    after = W.derivative_response(a, (0, 1), (W.Hinge(Q(2, 3)),), derivative_modes=(1, 2))
    difference = before.add(after, -1)
    controls = []
    mutants = (
        ('fake6_outside_window', {'tape': S.AUTHENTIC_TAPE+((6, 6),)}),
        ('missing2', {'tape': S.AUTHENTIC_TAPE[1:]}),
        ('duplicate2', {'tape': S.AUTHENTIC_TAPE+((2, 2),)}),
        ('wrong_half_density', {'half_density': Q(2, 3)}),
        ('wrong_clock', {'clock_scale': Q(1, 2)}),
    )
    for name, kwargs in mutants:
        try:
            W.source_prime_geometry(a, **kwargs)
        except (W.WavefrontGeometryError, S.WeilHierarchyError) as exc:
            controls.append({'name': name, 'rejected': True, 'reason': str(exc),
                             'authority': 'exact source contract, not spectral fitting'})
        else:
            controls.append({'name': name, 'rejected': False})
    contraction = W.source_first_prime_projection_bound()
    contraction['squared_ratio_strictly_below_one_fifth'] = (
        5*contraction['D_Q_G2_Q_HS_squared_upper'] < contraction['D_G2_HS_squared_interval'].lo)
    distribution = W.zero_extension_second_derivative(W.clipped_hinge(Q(3, 2), W.Hinge(Q(2, 3), 2)))
    return {
        'rational_geometry': {
            'authority': 'EXACT_COMPUTATION; isolated signed rational hinges',
            'radius': a, 'hinges': hinges, 'basis_modes': (1, 2, 3, 4),
            'basis': 'unnormalized P_n(x/a), real rational form coordinates',
            'matrix': W.hinge_matrix(a, columns, columns, hinges),
            'raw_derivative_gram': W.derivative_gram(a, columns, hinges),
            'output_projected_derivative_gram': W.derivative_gram(a, columns, hinges, output_modes=(1, 2)),
            'quotient_derivative_gram': W.derivative_gram(a, columns, hinges, derivative_modes=(0, 1, 2, 3)),
        },
        'projection_order_counterexample': {
            'radius': a, 'threshold': Q(2, 3), 'input_polynomial': (0, 1), 'removed_modes': (1, 2),
            'D_Q_T_p_minus_Q_D_T_p_L2_squared': difference.inner(difference),
            'refuted': 'derivative commutes with output projection',
        },
        'hinge_input_tail_amplification_control': W.projection_hs_audit(a, (W.Hinge(0),), (0, 1, 2, 3, 4)),
        'true_prime_geometry': W.source_prime_geometry(a),
        'true_prime_matrix_modes_1_to_4': W.source_prime_matrix(a, (1, 2, 3, 4), (1, 2, 3, 4)),
        'true_prime_only_projection_contraction': contraction,
        'window_boundary_distribution': {
            'window': Q(3, 2), 'hinge': W.Hinge(Q(2, 3), 2),
            'second_derivative': distribution,
            'total_second_derivative_mass': distribution.pair_polynomial((1,)),
            'boundary_free_mass_mutant': Q(4),
        },
        'negative_source_controls': controls,
        'source_nonidentification': {
            'fake6_locally_invisible_at_this_radius': S.log_iv(6).lo > 2*a,
            'interpretation': 'Local kernel agreement cannot authenticate the global Euler tape.',
        },
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Explicit JSON destination; absent means stdout only')
    parser.add_argument('--skip-tests', action='store_true', help='Run evidence only; receipt marks tests NOT_RUN')
    args = parser.parse_args(argv)
    started = datetime.now(timezone.utc).isoformat()
    start = time.monotonic()
    before = file_pins()
    if before['observational_succ/source_weil_hierarchy.py']['git_blob'] != PIN:
        raise RuntimeError('frozen source blob mismatch')
    head = command(['git', 'rev-parse', 'HEAD'])
    ancestry = command(['git', 'merge-base', '--is-ancestor', BASE, 'HEAD'])
    result = evidence()
    tests = None if args.skip_tests else command([sys.executable, '-B', '-m', 'unittest', *TEST_MODULES, '-v'])
    after = file_pins()
    checks = {
        'frozen_source_blob_matches': after['observational_succ/source_weil_hierarchy.py']['git_blob'] == PIN,
        'all_inputs_unchanged_during_probe': before == after,
        'requested_base_is_ancestor': ancestry['exit_code'] == 0,
        'all_negative_source_controls_rejected': all(r['rejected'] for r in result['negative_source_controls']),
        'projection_commutation_refuted': result['projection_order_counterexample']['D_Q_T_p_minus_Q_D_T_p_L2_squared'] > 0,
        'true_prime_only_contraction_bound': result['true_prime_only_projection_contraction']['squared_ratio_strictly_below_one_fifth'],
        'finite_window_total_distribution_mass_zero': result['window_boundary_distribution']['total_second_derivative_mass'] == 0,
        'focused_tests_passed': tests is not None and tests['exit_code'] == 0,
    }
    passed = all(v for k, v in checks.items() if k != 'focused_tests_passed') and (tests is None or tests['exit_code'] == 0)
    receipt = {
        'schema_version': 'arithmetic-resonance.wavefront.v1',
        'status': ('PASS' if tests is not None else 'EVIDENCE_PASS_TESTS_NOT_RUN') if passed else 'FAIL',
        'source_pins': {'required_source_blob': PIN, 'requested_base': BASE,
                        'live_head': head['stdout'].strip(), 'before': before, 'after': after},
        'evidence': result, 'checks': checks,
        'claim_status': {
            'general_hinge_and_distribution_identities': 'CONDITIONAL_PAPER_PROOF; stated analytic hypotheses',
            'rational_matrix_gram_and_boundary_instances': 'EXACT_COMPUTATION',
            'prime_only_source_bounds': 'EXACT_OUTWARD_RATIONAL_ENCLOSURE plus stated paper perturbation bound',
            'full_source_four_low_sign': 'OPEN', 'RH': 'NOT_PROVED',
        },
        'independence': 'Triangle, rational interpolatory and SymPy integrals use distinct calculation paths; same worker and shared mathematical source. No blind-agent independence claimed.',
        'nonclaims': ['no zero-coordinate inputs', 'no manufactured positivity',
                      'no full Gamma/contact/pole derivative Gram', 'no universal output-projection contraction',
                      'no new source range-closure theorem', 'no Lean proof or hosted CI claim'],
        'execution': {'started_at_utc': started, 'python': sys.version, 'cwd': str(ROOT),
                      'argv': sys.argv, 'elapsed_seconds': round(time.monotonic()-start, 6),
                      'serial': True, 'test_command': tests, 'base_ancestry_check': ancestry},
    }
    encoded = json.dumps(receipt, default=encode, indent=2, sort_keys=True)+'\n'
    if args.output is None:
        sys.stdout.write(encoded)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
        print(json.dumps({'status': receipt['status'], 'output': str(args.output),
                          'sha256': sha256(encoded.encode()).hexdigest(), 'checks': checks}, sort_keys=True))
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
