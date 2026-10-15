#!/usr/bin/env python3
"""Reproducible exact finite structural coupling experiment and falsifiers."""
from __future__ import annotations

import json
from fractions import Fraction
from observational_succ.structural_coupling import (
    CouplingError, EventReceipt, ObserverContract, OutOfModel,
    abstract_isomorphism_classes, cohomology_signature, discover_couplings,
    exact_posterior, gauge_change, gauge_transported_transcripts, groups_isomorphic,
    lift_wrap, quotient_darkness_certificate, replay_policy, simulate_trace,
    theoretical_extension_count, transcript_signature, winning_policy,
    rank_actions_by_target_gain,
)


def _contract(actions, mode):
    return ObserverContract("synthetic_cyclic_extension", "declared_common_basis", 0,
                            tuple(actions), mode)


def _policy_case(k, q, actions, labels, *, depth=6):
    d=discover_couplings(k,q)
    o=_contract(actions,"kernel")
    plan=winning_policy(d.candidates,o,labels,depth)
    qonly=_contract(actions,"quotient")
    simulations=[]
    if plan.policy is not None:
        for index,c in enumerate(d.candidates):
            value,events=replay_policy(plan.policy,c,o)
            simulations.append({
                "candidate":index,"identified":value,
                "synthetic_event_word":[list(a) for a,_ in events],
                "synthetic_readouts":[readout for _,readout in events]})
    return {
        "components":{"kernel_order":k,"quotient_order":q},
        "raw_normalized_cocycles":d.raw_cocycles,
        "action_multipliers":list(d.actions),
        "cyclic_cohomology_predicted_classes":sum(
            theoretical_extension_count(k,q,g) for g in d.actions),
        "gauge_classes":len(d.candidates),
        "abstract_isomorphism_classes":[list(x) for x in abstract_isomorphism_classes(d.candidates)],
        "candidate_invariants":[{
            "action":c.multiplier,"wrap":lift_wrap(c),
            "cohomology_signature":list(cohomology_signature(c)),
            "abelian":c.is_abelian(),
            "order_histogram":[list(p) for p in c.order_histogram()]
        } for c in d.candidates],
        "declared_licensed_actions":[list(a) for a in actions],
        "kernel_readout_plan":{"status":plan.status,"minimax_depth":plan.depth,
                               "synthetic_replays":simulations},
        "quotient_only_all_horizon_no_go":quotient_darkness_certificate(d.candidates,qonly),
        "source_authenticated":False,
    }


def receipt():
    cases={
        "C2_by_C2":_policy_case(2,2,((0,1),),("V4","C4")),
        "C3_by_C2":_policy_case(3,2,((0,1),(1,0)),("C6","S3")),
        "C3_by_C3":_policy_case(3,3,((0,1),),
                                  ("C3xC3","C9_fr_1","C9_fr_2")),
        "C4_by_C2":_policy_case(4,2,((0,1),(1,0)),
                                  ("C4xC2","C8","D8","Q8")),
    }
    d=discover_couplings(2,2)
    obs=_contract(((0,1),),"kernel")
    actual=simulate_trace(d.candidates[1],obs,((0,1),(0,1)))
    prior=(Fraction(1,2),)*2
    before=exact_posterior(d.candidates,obs,prior,actual[:1])
    after=exact_posterior(d.candidates,obs,prior,actual)

    c=discover_couplings(3,2).candidates[0]
    t=(0,1)
    counterpart=gauge_change(c,t)
    licensed=_contract(((0,1),(1,0)),"kernel")
    untransported=(transcript_signature((c,),licensed,((0,1),(0,1)))[0],
                   transcript_signature((counterpart,),licensed,((0,1),(0,1)))[0])
    transported=gauge_transported_transcripts(c,t,licensed,((0,1),(0,1)))

    def refused(thunk, exc):
        try:
            thunk()
        except exc:
            return True
        return False

    advanced=discover_couplings(4,2)
    advanced_contract=_contract(((0,1),(1,0)),"kernel")
    advanced_first=simulate_trace(advanced.candidates[0],advanced_contract,((0,1),))
    advanced_labels=("C4xC2","C8","D8","Q8")
    ranked=rank_actions_by_target_gain(advanced.candidates,advanced_contract,
                                       advanced_labels,(Fraction(1,4),)*4,advanced_first)
    costly=ObserverContract(advanced_contract.source_id,advanced_contract.basis_id,
                            advanced_contract.epoch,advanced_contract.actions,
                            advanced_contract.readout,(Fraction(4),Fraction(1)))
    ranked_costed=rank_actions_by_target_gain(advanced.candidates,costly,
                                             advanced_labels,(Fraction(1,4),)*4,
                                             advanced_first)

    mutations={
        "out_of_model_observation": refused(lambda: exact_posterior(
            d.candidates,obs,prior,
            (EventReceipt(obs.source_id,obs.basis_id,obs.epoch,(0,1),999),)),OutOfModel),
        "stale_epoch": refused(lambda: exact_posterior(
            d.candidates,obs,prior,
            (EventReceipt(obs.source_id,obs.basis_id,obs.epoch+1,(0,1),0),)),CouplingError),
        "unlicensed_action": refused(lambda: transcript_signature(
            d.candidates,obs,((1,0),)),CouplingError),
        "bad_prior": refused(lambda: exact_posterior(
            d.candidates,obs,(Fraction(1),Fraction(1)),()),CouplingError),
    }
    return {
        "status":"EXACT_DECLARED_FINITE_STRUCTURAL_COUPLING_RECEIPT",
        "source_family":"C_k by C_q, action + normalized twisted 2-cocycle",
        "cases":cases,
        "conditional_bayesian_example":{
            "prior":[str(w) for w in prior],
            "after_first_licensed_synthetic_report":[str(w) for w in before],
            "after_second_licensed_synthetic_report":[str(w) for w in after],
            "not_mathematical_truth_probabilities":True,
        },
        "source_map_gauge_control":{
            "untransported_signatures":[list(a) for a in untransported],
            "transported_signatures":[list(a) for a in transported],
            "untransported_differ":untransported[0] != untransported[1],
            "transported_agree":transported[0] == transported[1],
            "apparatus_map_empirically_authenticated":False,
        },
        "contextual_heuristic_example":{
            "context":"after one quotient-generator actuation and its synthetic kernel receipt",
            "uniform_prior_one_per_extension_class":"1/4",
            "unit_cost_action_ranking":[{
                "action":list(x.action),"target_gini_gain":str(x.target_gini_gain),
                "declared_cost":str(x.declared_cost),
                "gain_per_cost":str(x.gain_per_cost)} for x in ranked],
            "cost_mutation_action_ranking":[{
                "action":list(x.action),"target_gini_gain":str(x.target_gini_gain),
                "declared_cost":str(x.declared_cost),
                "gain_per_cost":str(x.gain_per_cost)} for x in ranked_costed],
            "ranking_is_heuristic_not_proof":True,
        },
        "negative_controls":mutations,
        "boundaries":{
            "mathematical_tables_stipulated":True,
            "complete_only_within_declared_finite_grammar":True,
            "experiments_are_synthetic":True,
            "actual_external_source_authenticated":False,
            "unbounded_source_model_invention":False,
            "analytic_global_completion":False,
            "RH_or_Weil_positivity_proved":False,
            "independent_academic_priority_claimed":False,
        },
    }


def main():
    print(json.dumps(receipt(),indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
