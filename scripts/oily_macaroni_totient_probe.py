#!/usr/bin/env python3
"""Create and replay source-pinned EXACT Oily–Macaroni totient receipt.

Usage: PYTHONPATH=. python scripts/oily_macaroni_totient_probe.py --write
       PYTHONPATH=. python scripts/oily_macaroni_totient_probe.py --verify

Does not rely on floats or pi digits for certification. A JSON mutation fails.
"""
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path
from observational_succ import oily_macaroni_totient as t

ROOT=Path(__file__).resolve().parents[1]
RECEIPT=ROOT/'research'/'2026-10-26'/'OILY_TOTIENT_EXACT_RECEIPT.json'
PIN='8e9d8a4d7d42bb0931f899ac221f27fccf090b36'


def snapshot():
    q2=t.finite_primitive_log_covariance(3,8)
    return {
        'source':'BBP original four-pole Green R(x)=P(x)/(16-x^8), source-time n, PR #309 packet law',
        'pinned_donor_pr309_head':PIN,
        'claim_status':'exact finite + analytic asymptotic; pi normality OPEN',
        'primitive_mass':{str(q):str(t.primitive_mass(q)) for q in (1,2,3,4,6,16)},
        'nonmultiplicativity_q6_q2q3':str(t.primitive_mass(6)-t.primitive_mass(2)*t.primitive_mass(3)),
        'dyadic_limit_character_rational_function':'4z/(4-z^2)^2',
        'dyadic_shadow_coefficient':'4z*(4-5z^2)/(4-z^2)^3',
        'dyadic_odd_first_log_shadow':str(t.parity_shadow_predictions()['first_log_shadow']),
        'dyadic_odd_golden_log_square_coefficient':str(t.parity_shadow_predictions()['third_shadow_multiplier'])+'*(phi^-1-gamma)',
        'exact_finite_packet_log_covariance_n3_m8':{
            'constant':str(q2['coefficient_constant']),
            'log_coefficient':str(q2['coefficient_log']),
            'normalizer':str(q2['normalizer']),
            'primitive_mass':str(q2['primitive_mass'])},
        'packet_first_values':{str(j):[str(q) for q in t.packet_log_moments(2,j)] for j in range(4)},
        'finite_n256_m21_budget':{k:str(v) for k,v in t.weighted_selected_transport_budget(256,21).items()},
        'euler_totient_not_source_selected':True,
        'third_order_center_is_grading_dependent':True,
        'selected_fourier_saving_proved':False,
        'pi_normality_proved':False,
        'RH_proved':False
    }


def main():
    parser=argparse.ArgumentParser()
    actions=parser.add_mutually_exclusive_group(required=True)
    actions.add_argument('--write',action='store_true')
    actions.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    payload=json.dumps(snapshot(),sort_keys=True,ensure_ascii=False,indent=2)+'\n'
    if args.write:
        RECEIPT.parent.mkdir(parents=True,exist_ok=True)
        RECEIPT.write_text(payload,encoding='utf8')
        print('WROTE',RECEIPT)
    else:
        actual=RECEIPT.read_text(encoding='utf8')
        if actual!=payload:
            raise SystemExit('OILY_TOTIENT_EXACT_RECEIPT: FAIL (stale or mutated)')
        print('OILY_TOTIENT_EXACT_RECEIPT: VERIFIED')

if __name__=='__main__':main()
