#!/usr/bin/env python3
"""Replay the six Cambrian-B assignment receipts using exact arithmetic."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import platform
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

from observational_succ import cambrian_b_chaos as b
from observational_succ.chaos_source_quotient import FiniteLogisticSource
from observational_succ.logistic_observer_tree import Source


def serial(value):
    if isinstance(value,F): return str(value)
    if isinstance(value,dict): return {str(k):serial(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)): return [serial(v) for v in value]
    return value


def provenance():
    paths=['observational_succ/cambrian_b_chaos.py',
           'scripts/cambrian_b_chaos_probe.py','tests/test_cambrian_b_chaos.py',
           'research/2026-10-13/CAMBRIAN_B_HYPOTHESES.json']
    return {"base_sha":"5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
            "python_version":platform.python_version(),
            "exact_arithmetic":"fractions.Fraction and inherited Q[alpha]",
            "files_sha256":{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            "infinite_claims_authority":"Written proofs, not finite replay or Lean",
            "physical_source_authenticated":False}


def results():
    source=FiniteLogisticSource(Source('cambrian-b-r3-prior-control',0),F(3),
            (F(2,5),F(3,5)),(F(1,3),F(2,3)))
    regimes=[]
    for t in (0,1,4,16):
        for label,n,m in (('faster',2*t,t),('matched',t,t),('slower',t,2*t),
                          ('equal-leading-rate-positive-surplus',t+isqrt(t),t)):
            regimes.append({"time":t,"regime":label,"depth":n,"advance":m,
                "geometric_ratio":F(1,2),
                "exact_residual_sup_norm":F(2)*(F(1,2)**max(n-m,0)),
                "T1_residual_modes":b.advancing({1:F(1)},n,m)})
    channels=[]
    for a,c,d in ((F(0),F(0),F(0)),(F(1,10),F(1,5),F(0)),
                  (F(0),F(0),F(1,2)),(F(0),F(0),F(1)),
                  (F(1,2),F(1,2),F(0))):
        law=b.noisy_phase_joint(a,c,d)
        channels.append({"error_first":a,"error_second":c,"odd_delay_probability":d,
            "joint_law":[[x,y,p] for (x,y),p in sorted(law.items())],
            "covariance":b.noisy_phase_covariance(a,c,d)})
    partial=[]
    for word in ((0,1,0,1),(0,None,0,1),(None,None,0,1)):
        intervals=b.partial_history_intervals(word,F(1,3),F(2,3))
        partial.append({"history":word,"intervals":intervals,
            "component_count":len(intervals),
            "total_uncertainty_length":sum((hi-lo for lo,hi in intervals),F(0))})
    out={
        '07': {"status":"PROVED LOCAL PAPER + TESTED EXACT MODEL; classical operator algebra",
            "claims":["Strong convergence for each C target; each Lp target for 1<=p<infinity",
                      "Mean-zero L2 transfer is direct sum of backward shifts; spectrum closed unit disk",
                      "Nonpolynomial continuous geometric eigenfunction never completes exactly"],
            "geometric_eigenfunction":b.geometric_lacunary(F(9,10),12),
            "high_mode_holdout":{str(n):b.transfer({3*(1<<n):F(1)},n) for n in (1,5,38,70)},
            "L_infinity_strong_convergence_claimed":False,
            "L_infinity_strong_convergence_refutation":{
                "analytic_source_event":"Union of zero blocks of length j+3 at itinerary positions j², j>=1",
                "invariant_event_probability_upper_bound":F(1,8),
                "every_depth_residual_sup_norm_lower_bound":F(7,8),
                "authority":"Written infinite-event proof, not enumerated simulation"},
            "polynomial_completion_generalization":"REFUTED by exact infinite-series proof"},
        '08': {"status":"PF REPRESENTATION PROVED; constant-cell candidate REFUTED; natural acim numerical construction UNVERIFIED",
            "pf_density_formula":"P rho(y)=sum_[f(x)=y,x in J] rho(x)/abs(f_prime(x))",
            "stationary_inverse_formula":"L_mu g=P(rho*g)/rho wherever rho>0",
            "constant_cell_obstruction":b.pf_constant_cell_obstruction(),
            "periodic_multiplier_obstruction":b.alpha_two_cycle_multiplier(),
            "Parry_acim_inequality_status":"Conditional on explicitly stated classical applicability; not a constructed certified density",
            "natural_C_to_A_branch_probability":None},
        '09': {"status":"EXACT SOURCE CONTROLS PROVED + bounded rational/algebraic tests",
            "sources":[{"parameter":"2","critical_itinerary":"C,C","prime_cycle_period":1},
                       {"parameter":"1+sqrt(5)","critical_itinerary":"C,R,C","prime_cycle_period":2},
                       b.superstable_three_certificate(),
                       {"parameter":"4","critical_itinerary":"C,R,L,L,...","natural_law":"arcsine","entropy_bits_per_step":1}],
            "nonstationary_prior_control":{
                "parameter":3,"originals":source.originals,"prior":source.weights,
                "endpoint_law":source.law(1),
                "source_conditioned_original_mean":source.direct_target(source.originals,1),
                "equal_weight_mutant_mean":F(1,2)},
            "all_parameter_kneading_classification":False},
        '10': {"status":"EXPLICIT PERIODIC POSITIVE_ENTROPY EXTENSIONS PROVED; finite counts corroborate",
            "extension_controls":[b.periodic_extension(d,6) for d in (1,2,3,5)],
            "universal_positive_entropy_factor_obstruction":"REFUTED by d=2 extension",
            "r4_CPE_boundary":"Uses Bernoulli source law, not merely positive entropy",
            "source_topological_entropy_equals_selected_metric_entropy_without_prior":False},
        '11': {"status":"EXACT PAPER CATCHUP THEOREM; finite mode controls",
            "normal_form":"L^n U^m g = L^(n-m)g if n>=m, else U^(m-n)g",
            "generic_continuous_completion_criterion":"n(t)-m(t) tends to +infinity",
            "regimes":regimes,
            "positive_lower_bound_on_per_action_time_precludes_finite_time_unbounded_depth":True,
            "physical_Zeno_or_universal_information_debt_law_proved":False},
        '12': {"status":"EXACT FINITE_CHANNEL AND INTERVAL_BOUNDS PROVED; no physical sensor attestation",
            "independent_noise_delay_channels":channels,
            "missing_history_intervals":partial,
            "covariance_formula":"(1-2e0)(1-2e1)(1-2p_odd)/4",
            "bounded_phase_readout_rule":"|x-z|>epsilon certifies phase; no uniform margin on Jstar",
            "shared_error_mutant":"Shared fair bit noise retains covariance 1/4, so independence is load-bearing",
            "bounded_noise_holdout":[{"map_lipschitz":a,"steps":n,
                "initial_error":F(1,10000),"step_error":F(1,10000),
                "certified_error_bound":b.bounded_dynamical_error(a,F(1,10000),F(1,10000),n)}
                for a in (2,4) for n in (0,1,4,8)],
            "bounded_dynamical_noise": "Tent |state_error_t| <= 2^t delta0 +(2^t-1)epsilon; logistic <=4^t delta0 +(4^t-1)epsilon/3"},
    }
    prov=provenance()
    return {k:serial({"assignment":k,"provenance":prov,**v}) for k,v in out.items()}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    receipts=results()
    target=ROOT/'research/2026-10-13'
    for k,v in receipts.items():
        path=target/f'CAMBRIAN_B_{k}_RESULT.json'
        if args.write:
            path.write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
        if args.check:
            actual=json.loads(path.read_text())
            # Runtime version is reported but is not a mathematical input.
            actual['provenance']['python_version']=v['provenance']['python_version']
            if actual!=v: raise AssertionError(f'Receipt mismatch: {path.name}')
    print(json.dumps({"assignments":list(receipts),"written":args.write,"checked":args.check,
                      "no_infinite_computation_or_Lean_claim":True},sort_keys=True))


if __name__=='__main__': main()
