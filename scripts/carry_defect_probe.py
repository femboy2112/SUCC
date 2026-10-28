#!/usr/bin/env python3
"""Deterministic finite replay; no computed onset or normality authority."""
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
import argparse
import hashlib
import json
from pathlib import Path

from observational_succ.carry_defect_energy import (
    all_center_certificate, authentic_window, authenticate_window, green_energy,
    green_kernel,
)
from observational_succ.mixed_lag_coercivity import (
    authentic_mixed_window, conditional_mixed_lag_budget,
    diophantine_exponent_margin, finite_tail_holdout, scale_requirement,
    verify_authentic_mixed_window,
)
from observational_succ.periodic_template_coercivity import (
    authentic_forcing_parameters, conditional_periodic_budget,
    periodic_integer_solution, periodic_branch_parameters,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT/'research/2026-10-27/carry_defect_validation/exact_receipt.json'
SOURCES = (
    'observational_succ/succ_internal_matrix_walk.py',
    'observational_succ/integer_bbp_carrier.py',
    'observational_succ/bbp_resonant_lags.py',
    'observational_succ/global_branch_coercivity.py',
    'observational_succ/periodic_template_coercivity.py',
    'observational_succ/mixed_lag_coercivity.py',
    'observational_succ/carry_defect_energy.py',
)


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return encode(asdict(value))
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def payload():
    source_hashes = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                     for name in SOURCES}
    periodic = []
    for period, frequency in ((1, 1), (3, -17), (11, 257)):
        m = 4096*period
        conditions = authentic_forcing_parameters(m, period, frequency)
        periodic.append({'scale': m, 'frequency': frequency,
                         'conditions': conditions})
    completed = periodic_branch_parameters(7*4096-1, 1, Q())
    lag_records = []
    for p, h, lags in ((1, 1, (1,)*12), (7, -17, (7, 13, 29)),
                       (3, 257, (1, 2, 3, 9))):
        m = scale_requirement(p, sum(lags), h)
        values = authentic_mixed_window(7, 3, lags)
        verify_authentic_mixed_window(values, 7, 3, lags)
        budget = conditional_mixed_lag_budget(8**10, p, sum(lags), h, 4)
        lag_records.append({'period': p, 'frequency': h, 'lags': lags,
                            'source_window': values,
                            'exponent_margin': diophantine_exponent_margin(m, p, lags, h),
                            'scale': m, 'tail': finite_tail_holdout(17, lags, 9),
                            'conditional_budget': budget,
                            'conditional_modulus_upper': budget.modulus_sum_upper,
                            'onset_certified': budget.numerical_onset_certified})
    carry_records = []
    for start, t, h in ((17, 9, 1), (31, 12, -3), (101, 7, 11)):
        states, forcing = authentic_window(start, t)
        authenticate_window(states, forcing, start)
        certificate = all_center_certificate(states, forcing, h)
        carry_records.append({'start': start, 'transitions': t, 'frequency': h,
                              'minimum_nonmodal': certificate.minimum_nonmodal_count,
                              'minimum_pairs': certificate.minimum_unequal_pairs,
                              'modal_loss_lower': certificate.modal_loss_lower,
                              'pair_loss_lower': certificate.pair_loss_lower,
                              'quadratic_loss_lower': certificate.quadratic_loss_lower,
                              'cut_count': len(certificate.cuts)})
    green = green_energy((Q(1, 7), Q(-2, 9), Q(1, 13), Q(-1, 11)))
    homogeneous = green_energy(tuple(Q(16**j, 16**6) for j in range(5)))
    return encode({
        'parent': '848bad224fef455a9f87ed19e947c936d309c965',
        'source': 'original four signed BBP poles; U_0=0; unwrapped lifts',
        'source_sha256': source_hashes,
        'authority': {'normality_proved': False, 'superlogarithmic_loss_proved': False,
                      'numerical_onset_certified': False,
                      'analytic_theorems': 'PAPER-PROVED with CLASSICAL input',
                      'this_receipt': 'EXACT FINITE only'},
        'periodic_source_holdouts': periodic,
        'completed_zero_forcing_parameters': completed,
        'periodic_integer_fixedpoint': periodic_integer_solution((-2, 7, -11)),
        'conditional_periodic_budget': conditional_periodic_budget(8**10, 7, 257, 4),
        'mixed_lag_holdouts': lag_records,
        'carry_holdouts': carry_records,
        'green_kernel_3': green_kernel(3),
        'signed_green': green,
        'homogeneous_boundary_control': homogeneous,
    })


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--verify', action='store_true')
    parser.add_argument('--path', type=Path, default=DEFAULT)
    args = parser.parse_args()
    expected = payload()
    rendered = json.dumps(expected, indent=2, sort_keys=True)+'\n'
    if args.write:
        args.path.parent.mkdir(parents=True, exist_ok=True)
        args.path.write_text(rendered)
        print('EXACT FINITE receipt written; no numerical onset or normality claim')
    else:
        observed = json.loads(args.path.read_text())
        if observed.get('authority') != expected['authority']:
            raise SystemExit('REJECTED: proof-authority claims differ')
        if observed.get('source_sha256') != expected['source_sha256']:
            raise SystemExit('REJECTED: source hashes differ')
        if observed != expected or args.path.read_text() != rendered:
            raise SystemExit('REJECTED: exact receipt differs')
        print('EXACT FINITE receipt replayed byte-for-byte; arithmetic onset remains unknown')


if __name__ == '__main__':
    main()
