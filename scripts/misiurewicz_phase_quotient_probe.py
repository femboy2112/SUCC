#!/usr/bin/env python3
"""Exact source-derived nonconstant periodic E quotient on a chaotic logistic map."""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import json
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from observational_succ.logistic_observer_tree import Source
from observational_succ.misiurewicz_phase_quotient import (
    ALPHA, ONE, LOW, FIXED, MAXIMUM, CRITICAL, BOUNDARIES,
    CubicElement, MisiurewiczError, EXPECTED_A, PARRY_PRIOR,
    f, isolate_alpha, markov_adjacency, postcritical_orbit_certificate,
    phase_parry_receipt, path_count, path_entropy_bits, legal_path,
    classify_actual_cell, actual_source_cells, dual_phase_correlation,
    PhaseReceipt, verify_E_Eprime_phase, alternate_stationary_symbolic_source,
)


def exact_json(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, CubicElement):
        return list(x.as_strings())
    if isinstance(x, tuple) or isinstance(x, list):
        return [exact_json(v) for v in x]
    if isinstance(x, dict):
        return {str(k):exact_json(v) for k,v in x.items()}
    if isinstance(x, (str,bool,int)) or x is None:
        return x
    raise TypeError(f"Unexpected nonexact receipt type {type(x)}")


def report():
    certificate=postcritical_orbit_certificate()
    a=markov_adjacency()
    assert a==EXPECTED_A
    assert f(CRITICAL)==MAXIMUM and f(MAXIMUM)==LOW
    assert f(LOW)==FIXED and f(FIXED)==FIXED
    assert f(CubicElement.coerce(F(2,5)))==f(CubicElement.coerce(F(3,5)))==ALPHA*F(6,25)
    assert classify_actual_cell(F(2,5))==0
    assert classify_actual_cell(F(3,5))==1
    assert classify_actual_cell(f(CubicElement.coerce(F(2,5))))==2
    roots=isolate_alpha()
    assert roots[0]<roots[1]

    parry=phase_parry_receipt(14)
    assert parry['stationary_phase_masses']==(F(1,2),F(1,2))
    assert parry['parry_stationary_prior']==PARRY_PRIOR
    assert parry['two_step_from_A']==(F(1,2),F(1,2),F(0))
    assert parry['two_step_from_C']==(F(0),F(0),F(1))
    assert parry['expected_fresh_symbol_bits_per_step']==F(1,2)
    assert parry['coarse_phase_entropy_rate_bits']==0
    assert parry['path_count_from_A']==128
    assert parry['path_count_from_C']==128

    ablations={str(p):alternate_stationary_symbolic_source(p)
               for p in (F(0),F(1,5),F(1,3),F(1,2),F(3,4),F(1))}
    assert all(z['stationary_phase_probabilities']==(F(1,2),F(1,2))
               for z in ablations.values())
    assert ablations['1/2']['stationary_prior']==PARRY_PRIOR
    assert not ablations['0']['microscopic_entropy_strictly_positive']
    assert ablations['1/3']['microscopic_entropy_strictly_positive']

    source_paths={str(x):list(actual_source_cells(F(x),7))
                  for x in (F(2,5), F(3,5), F(4,5))}
    assert all(len(path)==8 and legal_path(path) for path in source_paths.values())
    assert source_paths['2/5'][1:]==source_paths['3/5'][1:]
    assert source_paths['2/5'][0]!=source_paths['3/5'][0]

    s=Source('one-real-algebraic-logistic-source',12)
    observed={}
    for lag in (0,1,2,3,5,12,51):
        r=dual_phase_correlation(lag)
        start=PhaseReceipt(s,7,0)
        later=PhaseReceipt(s,7+lag,0 if lag%2==0 else 2)
        check=verify_E_Eprime_phase(start,later)
        assert check['lag']==lag and check['phase_valid']
        assert r['raw_phase_covariance']==F(1 if lag%2==0 else -1,4)
        assert r['transported_phase_covariance']==F(1,4)
        assert not check['complete_micro_path_recovered']
        observed[str(lag)]={
            'raw_covariance':r['raw_phase_covariance'],
            'declared_parity_transport_sign':r['parity_transport_sign'],
            'transported_covariance':r['transported_phase_covariance'],
            'mutual_information_bits':r['raw_phase_mutual_information_bits'],
            'phase_receipt_valid':check['phase_valid'],
            'complete_micro_path_recovered':check['complete_micro_path_recovered']}

    try:
        verify_E_Eprime_phase(PhaseReceipt(s,7,0),PhaseReceipt(Source(s.name,13),8,2))
    except MisiurewiczError:
        stale_source_rejected=True
    else:
        stale_source_rejected=False
    assert stale_source_rejected
    try:
        verify_E_Eprime_phase(PhaseReceipt(s,7,0),PhaseReceipt(s,8,1))
    except MisiurewiczError:
        forged_phase_rejected=True
    else:
        forged_phase_rejected=False
    assert forged_phase_rejected
    try:
        classify_actual_cell(FIXED)
    except MisiurewiczError:
        fixed_point_exception_rejected=True
    else:
        fixed_point_exception_rejected=False
    assert fixed_point_exception_rejected

    return exact_json({
      'status':'PROVED_LOCAL_EXACT_POSITIVE_ENTROPY_PERIOD_TWO_E_FACTOR',
      'parameter':{
          'minimal_polynomial':'r^3-2*r^2-4*r-8',
          'certified_rational_root_bracket':roots,
          'uniqueness_r_gt_2':'p_prime=(3r+2)(r-2)>0',
          'postcritical_orbit':certificate['position_aliases'],
          'actual_critical_orbit_equalities':certificate['inverse_alpha_exact'] and certificate['minimum_polynomial_remainder_zero'],
      },
      'real_carrier':{
          'invariant_interval_from_1_over_r_to_r_over_4':(LOW,MAXIMUM),
          'partition_boundaries':BOUNDARIES,
          'boundary_fixed_point_exact':f(FIXED)==FIXED,
          'exceptional_boundary_preorbit_excluded':True,
          'algebraic_actual_source_2_over_5_path':source_paths['2/5'],
          'algebraic_actual_source_3_over_5_path':source_paths['3/5'],
          'algebraic_actual_source_4_over_5_path':source_paths['4/5'],
          'original_two_over_five_and_three_over_five_collapse':True,
          'collapsed_next_state':ALPHA*F(6,25),
      },
      'certified_markov':{
          'adjacency':a,
          'characteristic_polynomial':'lambda*(lambda^2-2)',
          'spectral_radius':'sqrt(2)',
          'exact_topological_entropy_nats':'(1/2)*ln(2)',
          'exact_topological_entropy_bits':'1/2',
          'phase_transition':parry['phase_transition'],
          'phase_alternates_on_every_legal_nondisputed_orbit':True,
          'phase_entropy_rate_bits':parry['coarse_phase_entropy_rate_bits'],
          'global_continuous_period_two_factor_claimed':False,
      },
      'chosen_symbolic_parry_law':{
          'source_law_is_physical_acim':False,
          'stationary_cell_prior':parry['parry_stationary_prior'],
          'transition_matrix':parry['parry_rows'],
          'stationary_phase_probabilities':parry['stationary_phase_masses'],
          'two_step_A':parry['two_step_from_A'],
          'two_step_C':parry['two_step_from_C'],
          'micro_entropy_bits_per_step':parry['expected_fresh_symbol_bits_per_step'],
          'phase_entropy_bits_per_step':parry['coarse_phase_entropy_rate_bits'],
      },
      'symbolic_source_prior_ablation':ablations,
      'moving_history_debt':{
          'start_A_14_step_paths':path_count(0,14),
          'start_C_14_step_paths':path_count(2,14),
          'start_A_minimum_fixed_width_path_bits':path_entropy_bits(0,14),
          'start_C_minimum_fixed_width_path_bits':path_entropy_bits(2,14),
          'terminal_phase_minimum_bits':1,
          'source_path_recovery_from_phase_alone':False,
      },
      'dual_E_parity_transport':observed,
      'hostile_controls':{
          'fixed_point_prevents_everywhere_flipping':True,
          'stale_source_or_version_rejected':stale_source_rejected,
          'illegal_phase_report_rejected':forged_phase_rejected,
          'ambiguous_boundary_source_rejected':fixed_point_exception_rejected,
          'micro_history_not_reconstructed':True,
          'metric_entropy_measured_from_physical_source':False,
          'physical_source_authenticated':False,
          'RH_claimed':False,
      }
    })


if __name__=='__main__':
    print(json.dumps(report(),sort_keys=True,indent=2,ensure_ascii=False))
