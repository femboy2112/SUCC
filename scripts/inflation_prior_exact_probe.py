#!/usr/bin/env python3
"""Deterministic source receipts for inflation/prior research.

Run from repository root: PYTHONPATH=. python scripts/inflation_prior_exact_probe.py
Uses only standard library and exact fractions for stochastic/source controls.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from observational_succ.causal_inflation_prior import (
    BinaryTreePrior, oily_parameters, oily_matrix_power, linear_branch_energy,
    ks_signal_to_noise, normalized_census_variance, discrete_conformal_budget,
    correlated_remote_update, golden_lucas_scale, embedded_causal_tree,
    original_deflated_oily_L, oily_preobservation_unnormalized,
    oily_postobservation_unnormalized, oily_frontier_event_likelihood,
)
from observational_succ.chiral_virtual_phase_prior import (
    uniform_phase_prior,predicted_activity,posterior_phase,
    minimum_identifying_horizon,authentic_chiral_tap,guaranteed_silence_cycle,
)
from observational_succ.bbp_virtual_seed_prior import (
    authentic_forcing, rational_source_passport, finite_coherent_tail,
    changed_seed_abs_bound, haar_seed_character_expectation,
    comoving_arithmetic_state,comoving_arithmetic_increment,comoving_completion_error_upper,
)


def represent(x):
    if isinstance(x,F):
        return f"{x.numerator}/{x.denominator}"
    if isinstance(x,(tuple,list)):
        return [represent(y) for y in x]
    if isinstance(x,dict):
        return {k:represent(v) for k,v in x.items()}
    return x


def main():
    original=BinaryTreePrior(2,F(1,2),F(1,2))
    noise=BinaryTreePrior(2,F(0),F(1,2))
    exact_stats={str(n):original.level_statistics(n) for n in (1,2,3)}
    assert all(exact_stats[str(n)]['accuracy_exact']>=exact_stats[str(n+1)]['accuracy_exact'] for n in (1,2))
    energy={str(n):linear_branch_energy(2,n) for n in (1,3,5,10,20,30)}
    horizon={str(n):discrete_conformal_budget(2,n) for n in (0,1,2,3,6,10,20)}
    c={str(n): {str(t): finite_coherent_tail(n,t) for t in (0,3,7,12)} for n in (1,2,5,10)}
    embed=embedded_causal_tree(2,5,2)
    prior_likelihood=all(
        oily_postobservation_unnormalized(F(j,10),8)==
        oily_preobservation_unnormalized(F(j,10),8)*oily_frontier_event_likelihood(F(j,10))
        for j in range(11)
    )
    phase_data=tuple((t,predicted_activity(0,t)) for t in range(5))
    phase_posterior=posterior_phase(uniform_phase_prior(),phase_data)
    results={
        "source":"virtual-binary-broadcast-prior-and-authentic-four-pole-BBP-firewall-v1",
        "status":"EXACT_FINITE + PAPER_PROVED identities; NOT signed Weyl theorem",
        "binary_source":{"theta":"1/2","branching":2,"prior_root":"1/2",
                         "reconstruction_by_frontier":exact_stats,
                         "conditioned_remote_plus_given_local_plus":correlated_remote_update(F(1,2),1),
                         "independent_noise_accuracy":noise.level_statistics(2)['accuracy_exact']},
        "branching_threshold":{"b2_theta_half":ks_signal_to_noise(2,F(1,2)),
                              "b4_theta_half":ks_signal_to_noise(4,F(1,2)),
                              "b5_theta_half":ks_signal_to_noise(5,F(1,2)),
                              "census_variance_b2_level3":normalized_census_variance(2,F(1,2),3),
                              "census_variance_b5_level3":normalized_census_variance(5,F(1,2),3)},
        "inflation_discrete":{"scale_b":2,"conformal_budget":horizon,
                               "finite_inflation_end3_t10":discrete_conformal_budget(2,10,end=3),
                               "source_embedded_depth5_physical_extreme_separation":32*(embed[-1][-1]-embed[-1][0]),
                               "pisot_lucas_first12":[golden_lucas_scale(n) for n in range(12)]},
        "oily_source":{"u_v_at_endpoint":oily_parameters(1),
                       "M_at_endpoint_power4":oily_matrix_power(1,4),
                       "replicated_frobenius_b2":energy,
                       "prior_event_posterior_exact_at_11_rational_samples":prior_likelihood},
        "source_phase":{"five_receipt_minimum":minimum_identifying_horizon(),
                        "true_phase_posterior_after_five":phase_posterior[0],
                        "late_absolute_sensor_floor_1_over_100_silent_cycle":guaranteed_silence_cycle(F(1,100)),
                        "original_tap_at_index16":authentic_chiral_tap(16)},
        "true_BBP_prior_firewall":{
           "original_four_pole_source_passport_first10":all(authentic_forcing(n)==rational_source_passport(n) for n in range(1,11)),
           "haar_expected_h1_n0":haar_seed_character_expectation(1,0),
           "haar_expected_h1_n12":haar_seed_character_expectation(1,12),
           "coherent_seed_tail_intervals":c,
           "coherent_seed_abs_bound_n1":changed_seed_abs_bound(1),
           "coherent_seed_abs_bound_n10":changed_seed_abs_bound(10),
           "actual_comoving_state_n4":comoving_arithmetic_state(4),
           "actual_comoving_increment_n4":comoving_arithmetic_increment(4),
           "actual_comoving_completion_error_upper_n4":comoving_completion_error_upper(4)
        },
        "boundaries": [
           "tree edge theta=1/2 is a DECLARED observational control, not forced by Oily retention",
           "Haar expected phase cancellation is only ANNEALED, not actual zero-seeded BBP cancellation",
           "inflationary expansion of physical distance is not superluminal signal transfer",
           "finite inflation stage is not automatically a permanent causal event horizon",
           "Oily M linear replicated energy is not a stochastic reconstruction theorem",
           "source labels, prior over virtual histories, Bayesian update and physical feedback remain distinct"
        ]
    }
    out=Path('research/2026-10-28/INFLATION_PRIOR_EXACT_RECEIPT.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(represent(results),sort_keys=True,indent=2)+'\n')
    print(json.dumps({"receipt":str(out),"tree_level_stats":represent(exact_stats),"ks":represent(results['branching_threshold']),"source_check":results['true_BBP_prior_firewall']['original_four_pole_source_passport_first10']},indent=2))

if __name__=='__main__': main()
