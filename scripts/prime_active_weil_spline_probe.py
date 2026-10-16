"""Exact rational original-source Weil B-spline certificate; no zeros, no RH claim.

Run from SUCC checkout:
  python scripts/prime_active_weil_spline_probe.py --verify
  python scripts/prime_active_weil_spline_probe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from fractions import Fraction as Q

from observational_succ.prime_active_weil_splines import (
    two_spline_prime_active_gram, original_legendre_spline_projection,
    contact_neumann_gram, contact_mutant_gram, fake6_source_probe,
    arbitrarily_hidden_positive_non_euler_source, normalized_test_continuity_budget, log_int,
    original_two_mode_low_block,
)

SCALE=10**10


def floor_div(q:Q):
    return (q.numerator*SCALE)//q.denominator


def ceil_div(q:Q):
    return -((-q.numerator*SCALE)//q.denominator)


def outward(qlo,qhi):
    return [f"{floor_div(qlo)}/{SCALE}",f"{ceil_div(qhi)}/{SCALE}"]


def exact_receipt():
    s=two_spline_prime_active_gram(J=64)
    k=contact_neumann_gram()
    contact=contact_mutant_gram(Q(-1,8),64)
    fake=fake6_source_probe()
    proj=[original_legendre_spline_projection(t=t,rank=30) for t in (Q(0),Q(1,10))]
    proj4=[original_legendre_spline_projection(t=t,rank=4) for t in (Q(0),Q(1,10))]
    hidden=arbitrarily_hidden_positive_non_euler_source(8)
    low=original_two_mode_low_block(J=64)
    cont=normalized_test_continuity_budget(Q(1,2),Q(1),Q(1),Q(1,1000),Q(1,1000))
    if not s['is_positive_certified'] or not s['certified_relative_neumann_coercive']:
        raise AssertionError('strict source-certified Weil finite sign not established')
    if not s['smallest_eigenvalue_lower']>Q(1,16):
        raise AssertionError('original scalar Gram margin failed')
    if not s['source_relative_neumann_lower']>Q(1,50):
        raise AssertionError('original K-relative slice margin failed')
    if not all(p['high_residual_nonzero'] for p in proj):
        raise AssertionError('Legendre leakage cannot be silently erased')
    if not contact['mutant_has_certified_negative'] or fake['fake6_signed_effect'].upper>=0:
        raise AssertionError('adversarial source controls failed')
    return {
        'schema':'SUCC_PWS_SOURCE_CERTIFIED_SPLINES_v2',
        'status':'PROVED_LOCAL_ORIGINAL_SIGNED_WEIL_NOT_LOW_SCHUR',
        'parent_branch_head':'d7545a1c5fe7b16d12af877513283f802f3d151d',
        'source':{'object':'zeta','conductor':1,'parity':0,'half_density':'1/2',
                  'root_number':'1','completed_poles':[0,1],
                  'prime_tape':[list(e) for e in s['diag']['source_tape']],
                  'all_original_prime_power_tape_slices_equal':s['diag']['source_tape']==s['cross']['source_tape'],
                  'gamma_ladder_depth':64,'nontrivial_zeros_as_inputs':False},
        'test_basis':{'type':'two real cubic cardinal B3 translates',
                      'mesh':'1/5','centers':['0','1/10'],'radius':'1/2',
                      'autocorrelation':'1/h * B7((u-d)/h)'},
        'certified_intervals':{
             'diag':outward(s['diag']['value'].lower,s['diag']['value'].upper),
             'cross':outward(s['cross']['value'].lower,s['cross']['value'].upper),
             'eigen_plus':outward(*s['eigenvalue_intervals'][0]),
             'eigen_minus':outward(*s['eigenvalue_intervals'][1]),
             'gamma_tail_bound':str(s['diag']['analytic_tail_error']),
             'relative_K_lower_floor':f'{floor_div(s["source_relative_neumann_lower"])}/{SCALE}',
        },
        'strict_rational_theorem_checks':{
            'original_M_above_one_sixteenth_I':s['smallest_eigenvalue_lower']>Q(1,16),
            'original_M_above_one_fiftieth_K':s['source_relative_neumann_lower']>Q(1,50),
            'original_low_A11_above_one_over_10000':low['low_A11']['interval'].lower>Q(1,10000),
            'original_low_A22_above_one_over_5000':low['low_A22']['interval'].lower>Q(1,5000),
            'contact_negative_mutant_upper_below_minus_quarter':contact['positive_vector_branch'][1]<Q(-1,4),
            'fake6_outside_small_test_support':Q(9,10)<log_int(6).lower,
            'fake6_larger_support_negative':fake['fake6_signed_effect'].upper<0,
            'non_Euler_right_halfplane_uniform_defect_under_10e_minus_12':hidden['uniform_multiplier_error_on_Re_s_at_least_5_over_4']<Q(1,10**12),
        },
        'Neumann_metric':{
            'diag':str(k['diag']),'cross':str(k['cross']),
            'eigenvalues':[str(x) for x in k['eigenvalues']],
            'K_identity':'int_{-a}^a f_i*f_j = <(-Delta_N)^-1 i*f_i_prime, i*f_j_prime>'},
        'P30_projection':[
            {'center':str(p['center']),
             'full_norm_sq':str(p['full_L2_norm_squared']),
             'leakage_norm_sq_outward':outward(p['high_residual_norm_squared'],p['high_residual_norm_squared']),
             'strictly_nonzero':p['high_residual_nonzero'],
             'relative_leakage_below_1_over_60000':p['high_residual_norm_squared']/p['full_L2_norm_squared']<Q(1,60000)}
            for p in proj],
        'P4_projection':[
           {'center':str(p['center']),
            'exact_high_fraction_of_L2':str(p['high_residual_norm_squared']/p['full_L2_norm_squared']),
            'high_residual_strictly_positive':p['high_residual_nonzero'],
            'WB4_previous_full_A4_positive':True,
            'P4_zero_shift_Schur_positive_proved':False} for p in proj4],
        'original_low_P1_P2_A':{
           'A11':outward(low['low_A11']['interval'].lower,low['low_A11']['interval'].upper),
           'A22':outward(low['low_A22']['interval'].lower,low['low_A22']['interval'].upper),
           'A12':'0 (exact parity)',
           'Neumann_metric_unscaled':['1/30','1/210'],
           'both_original_A_diagonal_positive':low['original_low_A_on_span_P1_P2_positive'],
           'original_R0_computed':False,
           'original_S0_positive_proved':False,
        },
        'source_mutations':{'contact_delta':'-1/8',
              'contact_negative_branch':outward(*contact['positive_vector_branch']),
              'fake6_impulse_change':outward(fake['fake6_signed_effect'].lower,fake['fake6_signed_effect'].upper),
              'non_euler_multiplier_N':str(hidden['N']),
              'non_euler_multiplier_A':str(hidden['positive_dirichlet_weight']),
              'non_euler_multiplier_zero_real_part':'3/4',
              'non_euler_right_halfplane_max_error':str(hidden['uniform_multiplier_error_on_Re_s_at_least_5_over_4'])},
        'test_continuity_budget_scoped_premises':'C1 bounds given by caller; example budget '+str(cont),
        'original_low_schur_sign_verified':False,
        'original_high_resolvent_response_computed':False,
        'RH_proved':False,
        'numerical_calibrations_are_proofs':False,
    }

if __name__=='__main__':
    data=exact_receipt()
    if sys.argv[1:]==['--verify']:
        f=Path(__file__).resolve().parents[1]/'research/2026-10-16/PRIME_ACTIVE_WEIL_SPLINE_RECEIPT.json'
        expected=json.loads(f.read_text(encoding='utf-8'))
        if data!=expected:
            raise SystemExit('PWS ORIGINAL signed-Weil exact receipt mismatch')
        print('PWS original-source rational Weil Gram, source controls and Schur firewall VERIFIED')
    elif not sys.argv[1:]:
        print(json.dumps(data,indent=2,sort_keys=True))
    else:
        raise SystemExit('usage: python scripts/prime_active_weil_spline_probe.py [--verify]')
