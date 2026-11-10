#!/usr/bin/env python3
"""Deterministic finite receipt for origin-locked source/spectral research.

No π digits supplied, no claim that finite observations prove normality.
Run: python research/2026-11-08/origin_locked_spectral_fingerprint/receipt.py --verify
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.origin_spectral_fingerprint import (
    original_forcing, mutant_forcing, partial_source, original_tail_upper,
    certified_hex_digits, rational_clock, word_counts, word_energy,
    p_primary_part, decaying_g, critical_relative_phase,
    machin_pi_over_16_interval,
)

FILE = Path(__file__).with_name('FINITE_RECEIPT.json')


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_receipt() -> dict:
    m, depth = 40, 32
    digits = certified_hex_digits(m, depth)
    lo = partial_source(m)
    hi = lo + original_tail_upper(m)
    ml, mh = machin_pi_over_16_interval(70)
    assert lo < mh and ml < hi
    assert (16**depth*ml).__floor__() == (16**depth*mh).__floor__()
    values = [int(c, 16) for c in digits]
    energy = {str(k): str(word_energy(word_counts(values, k), k)) for k in (1,2,3)}
    clocks = {}
    for q in (Fraction(1,5), Fraction(1,7), Fraction(1,17), Fraction(1,257),
              Fraction(3, 512*17)):
        a, d, res = rational_clock(q)
        clocks[str(q)] = {'preperiod': a, 'period': d,
                          'rational_phase_residues': [str(x) for x in res]}
    critical = {}
    for A in (24, 48, 96, 192):
        z=critical_relative_phase(A)
        assert z.real < 13/16
        critical[str(A)] = {
            'frequency':2056*A*A,
            'relative_mean_real_approx': format(z.real,'.12f'),
            'relative_mean_imag_approx': format(z.imag,'.12f'),
            'proven_all_A_real_upper': '13/16 for A>=24',
            'proven_asymptotic_error': '5*pi/A',
        }
    src=ROOT/'observational_succ/origin_spectral_fingerprint.py'
    test=ROOT/'tests/test_origin_spectral_fingerprint.py'
    return {
        'schema':'succ-origin-spectral-fingerprint-v1',
        'scope':'finite diagnostic; source- and rational-interval theorem proofs separate; pi normality OPEN',
        'source_sha256':_sha(src),
        'tests_sha256':_sha(test),
        'four_pole_first_forcing':str(original_forcing(1)),
        'certified_pi_over_16_prefix32':digits,
        'source_truncation_depth':m,
        'tail_upper_exact':str(original_tail_upper(m)),
        'bbp_machin_prefix_agreement':True,
        'rational_seed_line_clocks':clocks,
        'cyclic_prefix_word_energy':energy,
        'positive_mutant_first_source_difference':str(mutant_forcing(1)-original_forcing(1)),
        'positive_mutant_prime257_component':str(p_primary_part(mutant_forcing(1)-original_forcing(1),257)),
        'exact_mutant_residual_n1':str(decaying_g(1)),
        'critical_relative_spectrum_diagnostics':critical,
    }


def main():
    p=argparse.ArgumentParser()
    group=p.add_mutually_exclusive_group(required=True)
    group.add_argument('--write',action='store_true')
    group.add_argument('--verify',action='store_true')
    args=p.parse_args()
    actual=build_receipt()
    if args.write:
        FILE.write_text(json.dumps(actual,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
        print('WROTE',FILE)
    else:
        if not FILE.exists():raise SystemExit('MISSING FINITE_RECEIPT.json')
        prior=json.loads(FILE.read_text(encoding='utf-8'))
        if prior!=actual:raise SystemExit('FAIL: source/tests or finite receipt mismatch')
        print('PASS: source/test hashes, exact digit intervals, clock strands, mutant and critical finite spectra')


if __name__=='__main__':main()
