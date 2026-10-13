#!/usr/bin/env python3
"""Exact source-debt / symbolic Markov / bifurcation admissibility receipt."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from observational_succ.logistic_observer_tree import Source,cylinder,symbolic_path,tent
from observational_succ.chaos_source_quotient import (
    SymbolWindow,FiniteLogisticSource,admissible_pair_from_witness,
    phantom_terminal_fraction,postcritical_threshold,logistic_r,
    ChaosQuotientError,
)


def fractions(obj):
    if isinstance(obj,F):
        return str(obj)
    if isinstance(obj,dict):
        return {str(k):fractions(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):
        return [fractions(v) for v in obj]
    return obj


def report() -> dict:
    fair=SymbolWindow(5)
    q4=fair.push({7:F(1)},4)
    q5=fair.push({7:F(1)},5)
    q8=fair.push({7:F(1)},8)
    expected=fair.equilibrium()
    assert len(q4)==16 and len(q5)==32 and q5==expected==q8
    assert fair.deterministic_factor_counterexample(7)==(14,15)
    assert fair.causal_path_count(12)==4096
    assert fair.terminal_support_count(12)==32

    # Cross-check that all Markov transitions are realized by actual
    # deterministic tent-orbit cylinder points (not an abstract coin flip).
    word=(0,1,1,0,1)
    descendants=[]
    for bit in (0,1):
        child=word+(bit,)
        lo,hi=cylinder(child)
        center=(lo+hi)/2
        actual=symbolic_path(tent(center),5)
        expected_next=word[1:]+(bit,)
        assert actual==expected_next
        descendants.append({'branch':bit,'child_interval':[str(lo),str(hi)],
                            'next_window':list(actual),'mass_ratio':'1/2'})

    dual_overlap={str(lag):fractions(fair.dual_common_information(lag))
                  for lag in (0,1,4,5,12)}
    assert dual_overlap['4']['maximal_common_deterministic_component_count']==2
    assert dual_overlap['5']['maximal_common_deterministic_component_count']==1
    assert dual_overlap['12']['fair_source_mutual_information_bits']==0

    biased=SymbolWindow(3,F(1,3))
    biased_law=biased.equilibrium()
    assert biased.push({0:1},3)==biased_law
    assert biased_law[0]==F(8,27)
    assert biased_law!=SymbolWindow(3).equilibrium()

    r3=admissible_pair_from_witness(3,F(1,8))
    r4=admissible_pair_from_witness(4,F(1,8))
    assert r3['source_admissible_preimages']==(F(1,8),)
    assert r3['algebraic_preimages']==(F(1,8),F(7,8))
    assert not r4['has_phantom_branch']
    ratios={str(r):str(phantom_terminal_fraction(r))
            for r in (F(5,2),F(3),F(16,5),F(19,5),F(39,10),F(4))}
    assert ratios['39/10']=='39/400' and ratios['4']=='0'
    near4=F(39,10)
    witness=(1-near4/4)/2
    assert admissible_pair_from_witness(near4,witness)['has_phantom_branch']

    src=Source('logistic-finite-source',3)
    ensemble=FiniteLogisticSource(src,F(3),
                     (F(1,3),F(2,3)),(F(1,4),F(3,4)))
    y=F(2,3)
    posterior=ensemble.backwards_target(ensemble.originals,1)[y]
    assert posterior==F(7,12) and posterior!=F(1,2)
    assert ensemble.direct_target(ensemble.originals,1)[y]==posterior
    assert ensemble.source_fiber(1,y)==(F(1,3),F(2,3))
    assert ensemble.source_fiber(1,y,(0,),src)==(F(1,3),)
    assert ensemble.source_fiber(1,y,(1,),src)==(F(2,3),)
    try:
        ensemble.source_fiber(1,y,(0,),Source(src.name,src.version+1))
    except ChaosQuotientError:
        stale_rejected=True
    else:
        stale_rejected=False
    assert stale_rejected

    collision=FiniteLogisticSource(Source('delayed-merge',0),F(4),
                              (F(0),F(1,2)),(F(1,3),F(2,3)))
    assert collision.law(1)=={F(0):F(1,3),F(1):F(2,3)}
    assert collision.law(2)=={F(0):F(1)}
    assert collision.backwards_target((0,1),2)=={F(0):F(2,3)}
    assert collision.direct_target((0,1),2)=={F(0):F(2,3)}
    assert collision.reverse_kernel(0)[F(0)] != collision.reverse_kernel(1)[F(0)]

    return {
        'status':'PROVED_LOCAL_SOURCE_FAITHFUL_CHAOS_QUOTIENT_EXACT',
        'source_logistic_r4_natural_prior_is_arcsine':True,
        'r4_model':{
            'bits_per_window':5,
            'ensemble_size':32,
            'steps_4_terminal_support':len(q4),
            'steps_5_terminal_support':len(q5),
            'after_5_rank_one_exact':q5==expected,
            'after_8_remains_equilibrium':q8==expected,
            'equilibrium_each_word':'1/32',
            'initial_word_7_next_words':list(fair.deterministic_factor_counterexample(7)),
            'fixed_initial_12_step_path_count':fair.causal_path_count(12),
            'fixed_initial_12_step_terminal_support':fair.terminal_support_count(12),
            'full_path_minimum_bits':12,
            'terminal_only_minimum_bits':5,
            'exact_cylinder_children':descendants,
            'dual_E_overlapping_source_factors_by_lag':dual_overlap,
            'underlying_source_is_still_deterministic_and_chaotic':True,
            'deterministic_window_factor_claimed':False,
        },
        'biased_prior_mutation':{
            'one_probability':'1/3',
            'word_zero_stationary_probability':str(biased_law[0]),
            'uniform_arcsine_window_law_preserved':False,
            'biased_stationary_law_exact_after_three_steps':True,
        },
        'source_admissibility':{
            'r3_terminal':str(r3['terminal']),
            'r3_declared_postimage_upper':str(r3['carrier_upper']),
            'r3_full_algebraic_predecessors':fractions(r3['algebraic_preimages']),
            'r3_actual_admissible_predecessors':fractions(r3['source_admissible_preimages']),
            'r3_full_algebraic_mean':str(r3['algebraic_equal_branch_mean']),
            'r3_admissible_equal_mean':str(r3['admissible_equal_branch_mean']),
            'r4_admits_both_for_same_witness':not r4['has_phantom_branch'],
            'relative_geometric_gap_lengths_not_dynamic_probabilities':ratios,
            'r_39_10_postcritical_threshold':str(postcritical_threshold(near4)),
            'r_39_10_one_sided_witness':str(witness),
        },
        'source_aware_dual_E':{
            'source':src.name,'version':src.version,
            'two_initial_states':fractions(ensemble.originals),
            'unequal_prior_weights':fractions(ensemble.weights),
            'merged_terminal':str(y),
            'true_posterior_mean_source':str(posterior),
            'naive_equal_branch_mean':'1/2',
            'one_terminal_report_does_not_identify_original':True,
            'dual_history_and_terminal_join_recovers_originals':True,
            'stale_source_rejected':stale_rejected,
            'physical_signature_verified':False,
        },
        'time_indexed_source_update':{
            'r4_initial_states':fractions(collision.originals),
            't1_law':fractions(collision.law(1)),
            't2_law':fractions(collision.law(2)),
            'two_step_original_source_target_posterior':'2/3',
            'different_step_reverse_kernels_required':True,
            'one_shot_source_oracle_equals_composed_Bayes':True,
        },
        'generic_r_less_than_4_full_chaotic_regime_theorem_claimed':False,
        'generic_r_less_than_4_symbolic_Markov_prior_identified':False,
        'no_individual_trajectory_predictions_from_stationary_law':True,
        'physical_source_authenticated':False,
        'RH_claimed':False,
    }


if __name__=='__main__':
    print(json.dumps(report(),sort_keys=True,indent=2))
