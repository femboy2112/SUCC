#!/usr/bin/env python3
"""Reproducible finite inverse-tree, transfer, and dual-source receipts."""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from observational_succ.logistic_observer_tree import (
    Source,PrefixReceipt,TerminalReceipt, join_observers, join_interval,
    transfer_polynomial,transfer_depth, chebyshev_mode,
    arcsine_moment, equilibrium_mean, exact_completion_depth,
    report_information, zero_lag_one_covariance_receipt,cylinders_at,cylinder,
    lipschitz_uniform_bound_pi_coefficient,period_two_bifurcation_receipt,
    forward_pullback_polynomial,
)


def report() -> dict:
    src=Source('single-chaotic-carrier-r4',1)
    word=(0,1,0,1,1,0,0,1)
    left=PrefixReceipt(src,word)
    right=TerminalReceipt(src,len(word),F(2,7))
    both=join_observers(left,right)
    lo,hi=join_interval(left,src,len(word),F(1,4),F(3,4))
    cols=cylinders_at(9)
    assert len(cols)==512 and sum((b-a for _,(a,b) in cols),F(0))==1
    assert all(b-a==F(1,512) for _,(a,b) in cols)
    monomials={}
    for k in (1,2,3,4,7,8,16):
        p=(0,)*k+(1,)
        n=exact_completion_depth(p)
        result=transfer_depth(p,n)
        assert result==(arcsine_moment(k),)
        monomials[str(k)]={'depth':n,'constant_mean':str(result[0])}
    modes={}
    for k in (1,2,3,4,8,15,16,32):
        got=transfer_polynomial(chebyshev_mode(k))
        expected=chebyshev_mode(k//2) if k%2==0 else (F(0),)
        assert got==expected
        modes[str(k)]={'first_step':'halves to '+str(k//2) if k%2==0 else 'annihilated',
                       'zero_after_depth':k.bit_length()}
    entropy=report_information(12,0)
    detail=report_information(12,4)
    moving={str(n):{'polynomial_degree':2**n,'residual_after_matched_depth':'x',
                    'completed_one_level_later':'1/2'} for n in range(7)}
    for n in range(7):
        g=forward_pullback_polynomial((0,1),n)
        assert len(g)-1==2**n and transfer_depth(g,n)==(F(0),F(1))
        assert transfer_depth(g,n+1)==(F(1,2),)
    covariance=zero_lag_one_covariance_receipt()
    periodic=period_two_bifurcation_receipt(F(16,5))
    unstable=period_two_bifurcation_receipt(4)
    assert covariance['covariance']==0
    assert hi-lo==F(1,512)
    assert len(both['orbit'])==9
    return {
        'status':'CLASSICAL_EXACT_FINITE_INVERSE_TREE_CERTIFICATE',
        'source':'logistic f_4(x)=4x(1-x); x=h(theta), tent conjugacy',
        'root_E_is_observation_origin_not_physical_x_zero':True,
        'inverse_tree':{'checked_depth':9,'leaves':len(cols),
            'all_intervals_length':'1/512','total_tent_mass':'1',
            'weighted_full_coverage':True},
        'polynomial_completion':monomials,
        'moving_target_rate_matched_noncompletion':moving,
        'chebyshev_mode_chain':modes,
        'dual_observer_join':{'initial_tent_source':str(both['theta_initial']),
            'terminal_tent_source':str(both['endpoint']),
            'checked_path_depth':both['depth'],
            'interval_width_given_terminal_width_half':str(hi-lo),
            'source_version_preserved':both['source']==src},
        'history_information':{'depth_12_constant_E':entropy,
                                'depth_12_retaining_first_four':detail},
        'zero_covariance_deterministic_control':{
            'E_x':str(covariance['E_x']),
            'E_x2':str(covariance['E_x_squared']),
            'E_x_times_next':str(covariance['E_x_times_next']),
            'lag_one_covariance':str(covariance['covariance']),
            'nonlinear_deterministic_relation_retained':True},
        'invariant_ensemble_stationary_not_lossless_state_factor':True,
        'full_inverse_branches_and_equal_weights_required':True,
        'finite_n_prediction_of_individual_generic_orbit_from_stationary_law':False,
        'lipschitz_uniform_upper_bound_coefficient_of_pi_depth_8_L1':str(lipschitz_uniform_bound_pi_coefficient(8,1)),
        'bifurcation_controls':{
            'r_16_over_5_cycle_center':str(periodic['center']),
            'r_16_over_5_radius_squared':str(periodic['radius_square']),
            'r_16_over_5_cycle_multiplier':str(periodic['period_two_derivative_multiplier']),
            'r_16_over_5_cycle_attracting':periodic['period_two_attracting'],
            'r_4_period_two_cycle_multiplier':str(unstable['period_two_derivative_multiplier']),
            'r_4_period_two_cycle_attracting':unstable['period_two_attracting'],
        },
        'generic_r_bifurcation_model_covered':False,
        'physical_carrier_authenticated':False,
        'RH_claimed':False,
    }

if __name__=='__main__':
    print(json.dumps(report(),sort_keys=True,indent=2))
