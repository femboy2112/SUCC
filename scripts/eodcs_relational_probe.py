#!/usr/bin/env python3
"""EODCS III exact finite source possibility, optimal envelopes and no Bayes forgery."""
import json
from fractions import Fraction as Q
from observational_succ.causal_nerode_succ import SourceChart
from observational_succ.eodcs_relational_choice import (
    RelationalIntervention, relational_descent, modal_envelopes,
    modal_property_verdict, relational_choice_demo,source_likelihood_mutant,
)


def receipt() -> dict:
    demo=relational_choice_demo()
    before=SourceChart("stochastic-countermodel",0,"binary",
                       ("s0","s1"),("0","0"))
    after=SourceChart("stochastic-countermodel",1,"binary",
                      ("u0","u1"),("cold","warm"))
    same_support=RelationalIntervention(
        "same-possibilities",before,after,
        (("u0","u1"),("u0","u1")))
    mutant=source_likelihood_mutant(
        same_support,((Q(1,4),Q(3,4)),(Q(3,4),Q(1,4))))
    different_support=RelationalIntervention(
        "different-possibilities",before,after,
        (("u0",),("u1",)))
    bounded=modal_envelopes(different_support)
    if (not relational_descent(same_support).descended_to_set_valued_observer
            or relational_descent(different_support).descended_to_set_valued_observer
            or bounded[0].exact_report_level_support):
        raise AssertionError("Source supports should distinguish lawful descent")
    report={
        "status":"EXACT_FINITE_EODCS_III_RELATIONAL_SOURCE",
        "set_valued_source":demo,
        "tight_may_common_observation":{
            "original_report":"0",
            "may":list(bounded[0].may_reports),
            "common_possible":list(bounded[0].common_possible_reports),
            "exact_source_support_descends":bounded[0].exact_report_level_support,
            "event_cold":modal_property_verdict(different_support,"0",("cold",)),
            "event_all":modal_property_verdict(
                different_support,"0",("cold","warm")),
            "event_empty":modal_property_verdict(different_support,"0",()),
        },
        "probabilistic_firewall":{
            "same_support_two_source_states":True,
            "source_law_s0":[[k,str(v)] for k,v in
                             mutant["law_by_source_state"][0][1]],
            "source_law_s1":[[k,str(v)] for k,v in
                             mutant["law_by_source_state"][1][1]],
            "law_probabilities_identified_by_support":False,
            "empirical_likelihoods_calibrated":False,
        },
        "scope":{
            "source_conditional_finite_relations":True,
            "lean_proof_run_inside_receipt_script":False,
            "physical_measurement_performed":False,
            "probability_inferred_from_possibility":False,
            "arbitrary_unbounded_category_discovery":False,
            "original_mathematics_priority_claimed":False,
            "RH_or_completed_Weil_positivity_proved":False,
        },
    }
    return report


if __name__=="__main__":
    print(json.dumps(receipt(),indent=2,sort_keys=True))
