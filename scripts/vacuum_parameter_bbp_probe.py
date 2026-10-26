#!/usr/bin/env python3
"""Exact rational source-vacuum and BBP Krylov certificate replay."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q

from observational_succ.vacuum_parameter_bbp import (
    forcing, kernel, krylov_certificate, certified_hex_prefix,
    source_tail_bracket, source_orbit, selected_hex_digit,
    finite_adelic_norm, diagonal_product_formula, prime_valuations,
    vacuum_rank_one_factor, hidden_determinant_example,
    rational_moment_counterfeit,
)


def _serialize(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,tuple):return [_serialize(v) for v in x]
    if isinstance(x,dict):return {k:_serialize(v) for k,v in x.items()}
    if isinstance(x,list):return [_serialize(v) for v in x]
    return x


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--verify',action='store_true')
    args=ap.parse_args()
    cert=krylov_certificate(8)
    prefix=certified_hex_prefix(8,23)
    selected=[selected_hex_digit(n) for n in range(1,16)]
    bogus=rational_moment_counterfeit()
    gate=vacuum_rank_one_factor(((2,1),(1,2)),(1,0),1)
    hidden1=hidden_determinant_example(1,1)
    hidden2=hidden_determinant_example(2,3)
    if args.verify:
        assert kernel(1)==0 and kernel(0)==4
        assert forcing(1)==Q(47,15)
        assert cert.moments_used==17
        assert prefix=='3.243F6A8885A308D313198A2'
        assert cert.lower < cert.upper
        assert cert.upper-cert.lower<=cert.baseline_neumann_tail_upper
        assert selected[:6]==[3,2,4,3,15,6]
        assert diagonal_product_formula(12)
        assert finite_adelic_norm(12,2)==3
        assert finite_adelic_norm(12,3)==1
        assert gate['determinant_ratio']==Q(5,3)
        assert hidden1['static_one_port']==hidden2['static_one_port']==0
        assert (hidden1['hidden_determinant'],hidden2['hidden_determinant'])==(1,6)
        assert bogus['matching_moments']==2
        assert bogus['pi_like_rational']!=cert.lower
    report={
        'research':'vacuum_parameter_bbp_krylov',
        'local_verification':'passed' if args.verify else 'not_requested',
        'source':'authenticated four pole r(n) from SUCC gearbox',
        'integral_vacuum_kernel_at_one':kernel(1),
        'first_moment':forcing(1),
        'dimension':cert.dimension,
        'rational_source_moments_used':cert.moments_used,
        'krylov_rational_lower':cert.lower,
        'krylov_rational_upper':cert.upper,
        'exact_rational_width':cert.upper-cert.lower,
        'all_depth_neumann_tail_cap':cert.baseline_neumann_tail_upper,
        'certified_pi_hex_23':prefix,
        'selected_first_15_hex_digits':selected,
        'selected_source_U5':source_orbit(5),
        'selected_T5_interval':source_tail_bracket(5),
        'diagonal_q12_adelic_prime_support':prime_valuations(12),
        'adelic_q12_partial_2':finite_adelic_norm(12,2),
        'adelic_q12_complete_3':finite_adelic_norm(12,3),
        'rank_one_vacuum_det_ratio':gate['determinant_ratio'],
        'hidden_same_port_determinant_variants':[hidden1['hidden_determinant'],hidden2['hidden_determinant']],
        'two_moment_counterfeit_rational_pi_like':bogus['pi_like_rational'],
        'source_signs_changed':False,
        'source_phase_carry_cancellation_proved':False,
        'pi_normality_proved':False,
        'RH_proved':False,
    }
    print(json.dumps(_serialize(report),indent=2,sort_keys=True))


if __name__=='__main__':main()
