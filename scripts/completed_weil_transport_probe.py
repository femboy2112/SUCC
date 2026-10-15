#!/usr/bin/env python3
"""Zero-independent source/Weil/Suzuki finite-law receipt. Never imports zeros.

The mpmath entries are high-precision numerical triangulation, NOT rigorous
interval certificates. The rational spectral-ladder remainder bounds are
proved symbolically in the accompanying note and stored as exact fractions.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp
from observational_succ.completed_weil_transport import (
    von_mangoldt_labels, arch_contact,arch_resolvent_integral,
    arch_exponential_resolvent,arch_resolvent_fourier,
    complete_logderivative_from_heat,independent_xi_logderivative,
    prime_heat_tail_bound,compact_weil_tent,
    tent_convolution,compact_arch,arch_spectral_tent_numeric,
    accelerated_arch_c2_remainder_bound,renormalized_arch_ladder,
    sobolev_operator_ladder_bound,arch_spectral_parity_conductor_resolvent,
    screw_potential_J,screw_potential_full_integral,
    screw_potential_remainder_bound,screw_kernel_J,
    fake6_positive_dirichlet_coefficient,fake6_negative_screw_certificate,
    fake_composite6_resolvent_defect,fake6_reflection_log_defect,
)


def qstr(q:Q)->str:
    return f'{q.numerator}/{q.denominator}' if q.denominator!=1 else str(q.numerator)


def nstr(x)->str:
    return mp.nstr(x,22)


def exact_receipt()->dict:
    mp.mp.dps=48
    source={
        'tested_first_primes':[[n,p] for n,p in von_mangoldt_labels(30)],
        'mutant_positive_coefficients':{str(n):qstr(fake6_positive_dirichlet_coefficient(n,1000)) for n in (1,2,3,6,12,36)},
        'fake6_non_euler_defect':'a(6)=1001 != a(2)a(3)=1',
    }
    arch=[]
    for s in (2,3):
        N=600
        heat=complete_logderivative_from_heat(s,N)
        independent=independent_xi_logderivative(s)
        raw=arch_resolvent_integral(s,dps=48)
        spectral=arch_resolvent_fourier(s,dps=48)
        arch.append({
            's':s,'a':f'{s}-1/2','N':N,
            'arch_digamma':nstr(arch_exponential_resolvent(s)),
            'arch_real_integral':nstr(raw),
            'arch_fourier_integral':nstr(spectral),
            'pole_plus_arch_minus_prime_heat':nstr(heat),
            'independent_zeta_derivative':nstr(independent),
            'observed_heat_remainder_abs':nstr(abs(heat-independent)),
            'rigorous_prime_error_upper':nstr(2*prime_heat_tail_bound(s,N)),
        })
    compact=[]
    for a in (Q(1,4),Q(2,5),Q(4,5)):
        z=compact_weil_tent(a,24,dps=48)
        w=mp.mpf(a.numerator)/a.denominator
        h=lambda x:tent_convolution(x,a)
        full=compact_arch(h,2*w/3,[0,w,2*w],dps=48)
        corrected=renormalized_arch_ladder(z['arch_ladder'],z['h0'],24)
        b=accelerated_arch_c2_remainder_bound(2*a/3,2/a,24)
        compact.append({
            'a':qstr(a),'support_radius':qstr(2*a),'prime_atoms':list(z['prime_support']),
            'pole':nstr(z['pole']),'signed_prime':nstr(z['prime']),
            'arch_direct':nstr(full),'arch_finite_24':nstr(z['arch_ladder']),
            'arch_corrected_24':nstr(corrected),
            'observed_corrected_error':nstr(abs(full-corrected)),
            'rigorous_C2_bound_exact':qstr(b),
            'rigorous_H1_bilinear_bound_exact':qstr(sobolev_operator_ladder_bound(24)),
        })
    screw=[]
    for R in (Q(1,4),Q(1),Q(2)):
        r=mp.mpf(R.numerator)/R.denominator
        exact=screw_potential_full_integral(r,dps=48)
        finite=screw_potential_J(r,24,dps=48)
        screw.append({
            'R':qstr(R),'psi_full_integral':nstr(exact),
            'psi_24_rungs':nstr(finite),
            'observed_absolute_error':nstr(abs(exact-finite)),
            'rigorous_error_upper_exact':qstr(screw_potential_remainder_bound(R,24)),
        })
    s=2
    mutant={
      'fake_composite_6_delta_b':'1000',
      'analytic_strict_Psi_fake_2_upper':qstr(fake6_negative_screw_certificate(1000)),
      'analytic_negative_1x1_kernel':'K_fake(2,2)=2*Psi_fake(2)<0',
      'numerical_fake_screw_2':nstr(screw_potential_J(2,24,fake6=1000,dps=48)),
      'numerical_fake_diagonal_kernel_2_2':nstr(screw_kernel_J(2,2,24,fake6=1000,dps=48)),
      'fake6_resolvent_delta_s2':nstr(fake_composite6_resolvent_defect(s,delta=1000)),
      'fake6_same_zero_divisor_but_functional_equation_log_defect_s2_exact':qstr(fake6_reflection_log_defect(2,1000)),
      'modified_complete_function_has_infinite_order':True,
      'conductor5_odd_arch_resolvent_s2':nstr(arch_spectral_parity_conductor_resolvent(2,5,1,dps=48)),
      'true_source_remains_untouched':True,
    }
    return {
      'status':'SOURCE_NORMALIZED_SIGNED_WEIL_TRANSPORT_EXACT_SCOPE',
      'parent_commit':'53934b3a5a980bb0f6e1001241822da5b6d928e5',
      'source_scope':'authentic von Mangoldt prime powers, real Gaussian, zeta conductor 1 and even Gamma_R',
      'weil_identity_external':'Suzuki, On the Hilbert space derived from the Weil distribution (2025), equation (3.3)',
      'arithmetic_source':source,
      'arch_gamma_heat_resolvent':arch,
      'compact_source_tests':compact,
      'zero_independent_suzuki_screw':screw,
      'negative_and_semantic_controls':mutant,
      'claims':{
        'heat_to_prime_vertical_line_uniqueness':'CLASSICAL PROVED; entire line required, finite samples do not suffice',
        'digamma_to_completed_arch_distribution':'CLASSICAL DERIVED; contact constant preserved',
        'signed_Cc2_weil_identity':'CLASSICAL WEIL EXPLICIT FORMULA IMPORT',
        'accelerated_H1_operator_form_remainder':'PROVED LOCAL WITH ANALYTIC BOUND O(J^-2)',
        'screw_second_derivative_as_distribution':'PROVED LOCAL BY SOURCE WEDGE AND CLASSICAL EXPLICIT FORMULA',
        'strict_H1_coercivity_forbidden':'CLASSICAL compact Suzuki signed kernel on each bounded interval',
        'fake6_positive_dirichlet_negative_kernel':'PROVED LOCAL BY RATIONAL UPPER BOUND',
        'full_Weil_positivity':'UNVERIFIED; RH EQUIVALENT',
        'Suzuki_global_operator_limit':'UNVERIFIED',
        'physical_carrier_attestation':False,
        'zero_positions_read_or_guessed':False,
        'independent_academic_priority_claimed':False,
      }
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    receipt=exact_receipt()
    body=json.dumps(receipt,indent=2,sort_keys=True,ensure_ascii=False)+'\n'
    if args.verify:
        if not args.verify.is_file():raise SystemExit('MISSING_COMPLETED_WEIL_RECEIPT')
        expected=args.verify.read_text(encoding='utf-8')
        if expected!=body:raise SystemExit('COMPLETED_WEIL_RECEIPT_MISMATCH')
        print('COMPLETED_WEIL_RECEIPT_REPLAY_VERIFIED')
    elif args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(body,encoding='utf-8')
        print(str(args.output))
    else:
        print(body,end='')

if __name__=='__main__':main()
