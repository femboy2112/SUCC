#!/usr/bin/env python3
"""Verify exact cumulative clock/factorial duality; RH remains unproved.

Requires no zero data, floating point, external prime list, or analytics source.
A pinned JSON receipt checks arithmetic evidence, NOT universal theorems.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.clock_factorial_duality import (
    cumulative_incidence_inverse, incidence_mobius, lcm_clock,
    mertens_prefix, prime_weight_response, primitive_increment,
    response_kernel, row_conditioning, single_site_response,
    weighted_factorial_clock, weighted_unit_clock,
)

RECEIPT = ROOT / 'research' / '2026-10-17' / 'TESSAIGA_IROH_CLOCK_FACTORIAL_DUALITY_RECEIPT.json'


def run_probe() -> dict:
    samples = {}
    for n in (6, 8, 12, 24, 60, 100, 120):
        a = lcm_clock(n)
        b = weighted_factorial_clock(n)
        c = weighted_unit_clock(n)
        if a != b or a != c:
            raise AssertionError(f'exact clock reconstruction failed at {n}')
        kernel = response_kernel(n)
        row = row_conditioning(n)
        samples[str(n)] = {
            'L_N': str(a),
            'prime_power_increment': str(primitive_increment(n)),
            'incidence_kernel_sum': row['coefficient_sum'],
            'incidence_linf_norm': row['linf_operator_norm'],
            'M_floor_N_over_2': single_site_response(n, 2),
            'strict_lower_norm_bound': row['unconditional_linear_lower_bound'],
            'kernel_gram_trace': sum(k * k for k in kernel),
        }
    n = 120
    for cutoff in range(1, n + 1):
        if lcm_clock(cutoff) != weighted_factorial_clock(cutoff):
            raise AssertionError(f'factorial duality at {cutoff}')
        if lcm_clock(cutoff) != weighted_unit_clock(cutoff):
            raise AssertionError(f'unit-weight duality at {cutoff}')
        r = row_conditioning(cutoff)
        if r['coefficient_sum'] != 1 or r['linf_operator_norm'] < (cutoff + 1) // 2:
            raise AssertionError(f'failed Green row bound at {cutoff}')
    # Faithful prime-power 8 vs fake composite 6.
    if (primitive_increment(6), primitive_increment(8)) != (1, 2):
        raise AssertionError('fake composite or missing prime-power jet')
    if cumulative_incidence_inverse([0, 1, 0, 0, 0, 0]) != single_site_response(6, 2):
        raise AssertionError('local spike must produce Mertens response')
    coherent = {str(p): prime_weight_response(120, p) for p in (2, 3, 5, 7)}
    if any(a != b for a, b in coherent.values()):
        raise AssertionError('coherent source valuation response inconsistent')
    mobius = incidence_mobius(120)
    return {
        'RH_proved': False,
        'completed_signed_Weil_positive': 'UNVERIFIED',
        'source_parent': 'OCG PR165 @ dea8b7f982fd3eb2361ccd5a12d360bcadfa3689',
        'scope': 'classical exact identities, paper proofs, finite integer tests',
        'horizons_checked': 120,
        'samples': samples,
        'mobius_1_to_24': list(mobius[1:25]),
        'mertens_24': mertens_prefix(mobius)[24],
        'coherent_prime_weight_response_at_120': coherent,
        'fake_composite_6_rejected': True,
        'single_site_and_valuation_source_types_not_conflated': True,
        'not_certified': [
            'source-physical universal rooted quotient tower',
            'square-root-plus-epsilon Mertens bound',
            'RH-scale psi(N)-N error',
            'completed signed Weil positivity / Suzuki S4 sign',
            'hosted exact-head CI, until an actual workflow runs',
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write-receipt', action='store_true')
    mode.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    output = json.loads(json.dumps(run_probe(), sort_keys=True))
    if args.write_receipt:
        RECEIPT.parent.mkdir(parents=True, exist_ok=True)
        RECEIPT.write_text(json.dumps(output, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    elif args.verify:
        if not RECEIPT.is_file():
            raise SystemExit('pinned exact receipt missing')
        expected = json.loads(RECEIPT.read_text(encoding='utf-8'))
        if output != expected:
            raise SystemExit('pinned exact receipt MISMATCH')
        print('TESSAIGA_IROH_EXACT_RECEIPT_VERIFIED RH_PROVED=false')
    else:
        print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
