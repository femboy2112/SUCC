#!/usr/bin/env python3
"""Replay source-selected branch transport and its exact hostile controls.

Deterministic rational receipt; paper and kernel authority remain distinct.
The verifier regenerates every value and source hash. It fails on altered
normality flags, altered source paths, or altered finite measurements.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from observational_succ.lambda_source_duality import original_history
from observational_succ.selected_branch_analytic import (
    PeriodicGreenSelector, SparsePeriodicGreenSelector, certified_control_table,
)
from observational_succ.selected_branch_arithmetic import (
    authentic_spill_points, spill_count_upper,
)
from observational_succ.selected_branch_operator import authentic_resolution_certificate
from observational_succ.selected_branch_transport import (
    source_branch_records, source_energy_transport_budget, source_signed_certificate, source_tables,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT/'research/2026-10-26/selected_branch_validation/exact_receipt.json'


def outward(value, upper=False, denominator=10**12):
    scaled = value*denominator
    integer = scaled.__ceil__() if upper else scaled.__floor__()
    return str(Q(integer, denominator))


def source_hashes():
    paths = [
        'observational_succ/succ_internal_matrix_walk.py',
        'observational_succ/integer_bbp_carrier.py',
        'observational_succ/bbp_source_memory.py',
        'observational_succ/lambda_source_duality.py',
        'observational_succ/pi_succ_character_intervals.py',
        'observational_succ/selected_branch_analytic.py',
        'observational_succ/selected_branch_arithmetic.py',
        'observational_succ/selected_branch_operator.py',
        'observational_succ/selected_branch_transport.py',
        'scripts/selected_branch_probe.py',
    ]
    return {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}


def certificate():
    cases = []
    for N, M in ((16, 2), (64, 4), (128, 8), (257, 16)):
        states = original_history(N+1)
        before, after, records = source_tables(states, M)
        source_cases = {}
        for h in (1, 4, 8):
            signed = source_signed_certificate(states, M, h)
            source_cases[str(h)] = {
                'normalized_modulus_upper': outward(signed['normalized_modulus_upper'], True),
                'signed_midpoint_rectangle': [outward(x, k % 2 == 1)
                                              for k, x in enumerate(signed['midpoint_rectangle'])],
                'source_transport_error': str(signed['source_transport_error']),
            }
        actual_spills = sum(p.spill > 0 for p in authentic_spill_points(N))
        actual_scaled = sum(p.spill > 0 for p in authentic_spill_points(N, M))
        if records['digit_changes'] != actual_spills or records['bin_changes'] > actual_scaled:
            raise ArithmeticError('independent scaled source count mismatch')
        if before.rational_energy(8) != before.totient_parity_energy():
            raise ArithmeticError('parity endpoint mass identity failed')
        cases.append({
            'N': N, 'M': M, 'authentic_zero_source': True,
            'digit_spills': actual_spills, 'scaled_spills': actual_scaled,
            'changed_future_bins': records['bin_changes'],
            'prior_source_budget': source_energy_transport_budget(N, M),
            'original_chi_squared': str(before.chi_squared()),
            'future_chi_squared': str(after.chi_squared()),
            'original_h4_energy': str(before.rational_energy(4)),
            'future_h4_energy': str(after.rational_energy(4)),
            'original_h8_energy': str(before.rational_energy(8)),
            'future_h8_energy': str(after.rational_energy(8)),
            'endpoint_conditional_totient_energy': str(after.totient_parity_energy()),
            'signed_finite_certificates': source_cases,
        })
    saturation = []
    for N in (7, 19, 31):
        cert = authentic_resolution_certificate(original_history(N))
        if cert.chi_squared != 15:
            raise ArithmeticError('authentic exact-conditioning obstruction failed')
        saturation.append({'N': N, 'M': str(cert.bins), 'conductor': str(cert.conductor),
                           'chi_squared': str(cert.chi_squared),
                           'h4_energy': tuple(map(str, cert.conditional_mode_energy(4).coefficients)),
                           'h8_energy': tuple(map(str, cert.conditional_mode_energy(8).coefficients))})
    controls = []
    for cls in (PeriodicGreenSelector, SparsePeriodicGreenSelector):
        for k in (2, 3):
            control = cls(k)
            N, M = 64, control.conductor
            data = certified_control_table(control, N, M)
            controls.append({'family': cls.__name__, 'q': control.conductor,
                             'period': control.period, 'N': N, 'M': M,
                             'original_forcing': data.source_forcing_preserved,
                             'authentic_zero_anchor': data.authentic_zero_anchor,
                             'certified_chi_squared': str(data.defect.chi_squared),
                             'certified_h8_energy': str(data.defect.exact_parity_energy()),
                             'h8_limiting_character': tuple(map(str, control.periodic_character(8))),
                             'h8_all_N_error_upper': str(control.finite_mode_error_upper(N, 8)),
                             'energy_lower_bounds': tuple(map(str, control.energy_lower_bounds(N, M)))})
    schedules = []
    for exponent in (64, 256, 1024):
        N, M = 1 << exponent, exponent
        schedules.append({'log2_N': exponent, 'M': M,
                          'spill_count_upper': str(spill_count_upper(N)),
                          'comparison': source_energy_transport_budget(N, M)})
    critical = []
    for N in (1, 3, 17, 65):
        points = authentic_spill_points(N, 8*N*N)
        if not all(p.spill > 0 for p in points):
            raise ArithmeticError('quadratic-scale all-spill source theorem failed')
        rec = source_branch_records(original_history(N+1), 8*N*N)
        if rec['bin_changes'] != N:
            raise ArithmeticError('quadratic-scale bin-change source theorem failed')
        critical.append({'N': N, 'scale': 8*N*N,
                         'positive_spills': sum(p.spill > 0 for p in points),
                         'changed_bins': rec['bin_changes'],
                         'last_scaled_forcing': str(8*N*N*points[-1].original_forcing)})
    return {
        'schema': 'succ.selected-branch.exact.v1',
        'parent_pr': 312, 'parent_sha': '0c306a889f425418c29cbea3193205fb80c0575e',
        'reviewed_sibling_pr': 311, 'reviewed_sibling_sha': 'a34c4484059e667202b97d5ab4102560987b1406',
        'source_hashes': source_hashes(), 'source_cases': cases,
        'authentic_resolution_obstruction': saturation,
        'same_forcing_changed_selector_controls': controls, 'preset_budget_samples': schedules,
        'critical_quadratic_scale_cases': critical,
        'critical_numerator_polynomial_in_N_minus_one': [87, 1478, 2904, 1976, 448],
        'authority': {'carry_spill_count': 'PAPER-PROVED',
                      'conditional_energy_transport': 'PAPER-PROVED',
                      'finite_receipt': 'EXACT FINITE / OUTWARD RATIONAL',
                      'kernel': 'SEPARATE finite declarations; see lean/kernel-observation.json'},
        'new_selected_oN_bound_proved': False,
        'best_selected_modulus_order_improved': False,
        'pi_normality_proved': False,
    }


def render():
    return json.dumps(certificate(), indent=2, sort_keys=True,
                      default=lambda value: str(value) if isinstance(value, Q) else value)+'\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--write', action='store_true')
    action.add_argument('--verify', action='store_true')
    parser.add_argument('--path', type=Path, default=DEFAULT)
    args = parser.parse_args()
    text = render()
    if args.write:
        args.path.parent.mkdir(parents=True, exist_ok=True)
        args.path.write_text(text)
        print('SELECTED_BRANCH_EXACT_RECEIPT_WRITTEN')
    elif not args.path.is_file() or args.path.read_text() != text:
        raise SystemExit('SELECTED_BRANCH_EXACT_RECEIPT_REJECTED')
    else:
        print('SELECTED_BRANCH_EXACT_RECEIPT_VERIFIED')


if __name__ == '__main__':
    main()
