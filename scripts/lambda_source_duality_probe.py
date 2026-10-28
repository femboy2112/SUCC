#!/usr/bin/env python3
"""Source-typed inside-out BBP exact receipt, write/verify/mutation guard.

Run at repo root:
  python scripts/lambda_source_duality_probe.py --write
  python scripts/lambda_source_duality_probe.py --verify

The receipt is a finite algebraic diagnostic, not a normality theorem.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'research' / '2026-10-26' / 'LAMBDA_SOURCE_DUALITY_RECEIPT.json'
from observational_succ import lambda_source_duality as dual
from observational_succ import oily_macaroni_totient as totient


def qstr(x):
    return str(x) if isinstance(x, Q) else x


def certificate():
    source_file = ROOT / 'observational_succ' / 'lambda_source_duality.py'
    content_hash = hashlib.sha256(source_file.read_bytes()).hexdigest()
    uniform = {str(h):str(dual.uniform_inverse_character(h).coefficients)
               for h in (0,1,2,4,8,16,17,32)}
    if dual.uniform_inverse_character(1) != dual.Cyclo16.zero():
        raise ArithmeticError('uniform inverse character fails')
    packet = dual.packet_fold_mod16()
    odd = dual.primitive_packet_fold_mod16()
    assert totient.primitive_mass(16) == Q(4,9)
    assert dual.branch_fourier(odd,8) == -dual.Cyclo16.one()
    parity = {}
    for N, M in ((16,1),(64,2),(128,4),(256,4),(512,8)):
        source = dual.original_history(N)
        d = dual.branch_defect(source, M)
        summed = sum((d.conditional_mode_energy(h) for h in range(1,16)), dual.Cyclo16.zero())
        assert summed == d.chi_squared*dual.Cyclo16.one()
        parity[f'N{N}_M{M}'] = {
            'chi2_conditional':str(d.chi_squared),
            'h8_parity_energy':str(d.exact_parity_energy()),
            'source_is_authentic':dual.verify_original_history(source),
            'primitive_h1_upper_rational':str(d.exact_upper_for_primitive_h(1)),
            'h16_upper_rational':str(dual.selected_weyl_upper_from_branch_defect(d,16)),
        }
    selected = dual.witness_selected_branches(dual.original_history(8))
    control_uniform = tuple((j+Q(1,3))/16 for j in range(16))
    control_coupled = tuple((j+(Q(0) if j%2==0 else Q(1,2)))/16 for j in range(16))
    report = {
        'schema':1,
        'research_parent_pr':310,
        'research_parent_sha':'a8c7c85b7a1900d422090f1757c174e7aac69f44',
        'original_main_ancestor':'6dd80730c3575d91f746546a25da5aedbd2e2737',
        'module_sha256':content_hash,
        'source_first_forcing':str(dual.authentic_r(1)),
        'uniform_inverse_character_exact_cyclo16':uniform,
        'oily_packet_fold_chi2':str(dual.fourier_parseval_defect(packet)),
        'oily_primitive_packet_fold_chi2':str(dual.fourier_parseval_defect(odd)),
        'oily_primitive_h8_character':str(dual.branch_fourier(odd,8).coefficients),
        'selected_branch_prefix':[
            {'n':w.source_index,'digit':w.digit,'remainder':str(w.remainder),
             'forcing':str(w.forcing),'literal_carry':w.literal_carry,'conductor':w.conductor}
            for w in selected[:4]],
        'selected_exact_conditional_chi2_samples':parity,
        'synthetic_uniform_inverse_ensemble_defect':str(dual.branch_defect(control_uniform,4,authenticate=False).chi_squared),
        'synthetic_uniform_digit_marginal_defect':str(dual.branch_defect(control_coupled,1,authenticate=False).chi_squared),
        'synthetic_digit_future_correlation_defect':str(dual.branch_defect(control_coupled,2,authenticate=False).chi_squared),
        'synthetic_coherent_zero_defect':str(dual.branch_defect((Q(0),)*16,1,authenticate=False).chi_squared),
        'status':dual.status_flags(),
        'selected_weyl_saving_proved':False,
        'pi_normality_proved':False,
        'RH_proved':False,
    }
    return report


def render():
    return json.dumps(certificate(),sort_keys=True,indent=2,ensure_ascii=False)+'\n'


def main():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write',action='store_true')
    group.add_argument('--verify',action='store_true')
    parser.add_argument('--path',type=Path,default=DEFAULT)
    args=parser.parse_args()
    data=render()
    if args.write:
        args.path.parent.mkdir(parents=True,exist_ok=True)
        args.path.write_text(data,encoding='utf8')
        print(f'INSIDEOUT_EXACT_RECEIPT_WRITTEN {args.path}')
    elif not args.path.is_file() or args.path.read_text(encoding='utf8') != data:
        raise SystemExit('INSIDEOUT_EXACT_RECEIPT_FAILED: missing, changed or tampered data')
    else:
        print('INSIDEOUT_EXACT_RECEIPT_VERIFIED')


if __name__=='__main__':main()
