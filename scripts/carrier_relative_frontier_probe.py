#!/usr/bin/env python3
"""Reproducible exact carrier/ontology/structural-lower-bound evidence."""
import json
import sys
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.carrier_observational_frontier import (
    destructive_parity_model, ontology_alias_model,
)
from observational_succ.carrier_statistical_limit import (
    ExperimentPair,rational_bernoulli_tree,
)
from observational_succ.carrier_hankel_bounds import (
    hankel_dimension_receipt,verify_dimension_receipt,impulse_realization_check,
    linear_recurrence_prefix,
)
from observational_succ.carrier_shadow_fibers import (
    DelayedSeparatingTower,FiniteShadowSuite,
)


def receipt():
    alias, claim=ontology_alias_model()
    shadow=alias.claim_quotient(claim)
    parity,original_claim=destructive_parity_model()
    parity_quotient=parity.claim_quotient(original_claim)
    parity_policy=parity.adaptive_original_claim(original_claim)
    expanded,claim2=ontology_alias_model(allow_separator=True)
    simulator=rational_bernoulli_tree(3)
    chosen={h:("LEFT" if len(h)%2==0 else "RIGHT") for h,a in simulator.rows if a=="LEFT"}
    source_law=simulator.policy_distribution(chosen)
    internal_law=simulator.internal_realization().run_policy(chosen)
    if source_law!=internal_law:raise AssertionError('Internal source simulator mismatch')
    stats=ExperimentPair('noisy',(0,1),(F(3,4),F(1,4)),(F(1,4),F(3,4)))
    hseq=tuple(F(1+(-1)**n) for n in range(9))
    hankel=hankel_dimension_receipt(hseq,4,4)
    if not verify_dimension_receipt(hseq,hankel):raise AssertionError('Invalid linear lower proof')
    tower=DelayedSeparatingTower()
    witness={str(n):tower.alias_after(n) for n in (1,3,7,31)}
    values=tuple((a,b) for a in range(2) for b in range(2))
    suite=FiniteShadowSuite('2-bit',values,{
        'left':tuple(x[0] for x in values),'right':tuple(x[1] for x in values)},
        {x:x[0]^x[1] for x in values}).minimal_complete_suite()
    root={
       'status':'exact finite mathematical certificates; no physical source authentication',
       'carrier_ontology_certain':False,
       'ontology_pair_same_history_all_policies':shadow['status']=='PERMANENTLY_DARK_UNDER_ACTIONS',
       'ontology_additional_probe_breaks_alias':expanded.adaptive_original_claim(claim2)['rank']==1,
       'source_behavior_state_lower_bound':alias.minimal_behavior_quotient()['minimum_behavior_state_count'],
       'original_parity_pairwise_separable':parity_quotient['status']=='BEHAVIORALLY_FACTORABLE_ONLY',
       'original_parity_uniformly_decidable':parity_policy['rank'] is not None,
       'destructive_parity_policy':parity_policy['status'],
       'finite_horizon_internalization':{'horizon':simulator.horizon,
          'number_of_legal_adaptive_histories':len(source_law),
          'all_observed_joint_probabilities_equal': source_law==internal_law,
          'simulation_state_count':simulator.internal_history_state_bound()['reachable_internal_states']},
       'stochastic_ontology_risk':{'one_trial':str(stats.equal_prior_risk),
          'seven_trials':str(stats.independent_product_risk(7)),
          'one_trial_tv':str(stats.total_variation),
          'always_positive_at_seven':stats.independent_product_risk(7)>0},
       'hankel':{'observations':list(map(int,hseq)),
          'verified_min_linear_state_dimension':hankel['linear_state_lower_bound'],
          'minor_determinant':str(hankel['minor_determinant']),
          'recurrence':list(map(str,linear_recurrence_prefix(hseq,2)['coefficients'])),
          'global_recurrence_authenticated':False},
       'delayed_impulse_minimal_linear_dimension_10':impulse_realization_check(9)['minimal_linear_state_dimension'],
       'finite_versus_limit':{'late_alias_examples':witness,
          'zero_finitely_certified_without_source_bound':False,
          'source_bound_7_sufficient_probe_depth':tower.bounded_source_horizon(7)},
       'minimal_source_relative_2bit_parity_suite':{'size':suite['minimum'],'probes':suite['suite']},
       'physical_entanglement_claimed':False,
       'RH_or_archimedean_identification_claimed':False,
    }
    assert root['destructive_parity_policy']=='NO_UNIFORM_FINITE_POLICY'
    assert root['hankel']['verified_min_linear_state_dimension']==2
    assert root['finite_horizon_internalization']['all_observed_joint_probabilities_equal']
    assert root['stochastic_ontology_risk']['always_positive_at_seven']
    return root

if __name__=='__main__':
    print(json.dumps(receipt(),indent=2,sort_keys=True))
