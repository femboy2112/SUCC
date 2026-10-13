#!/usr/bin/env python3
"""Source-indexed SUCC carrier theorem and hostile exact-law scientific receipt."""
from __future__ import annotations

import json
from fractions import Fraction as Q

from observational_succ.carrier_indexed import (
    Carrier, CarrierStage, CarrierInstrument, CarrierQuotient,
    CarrierStep, audit_descent, checked_descent,
    transport_actual_history, repair_one_step,
    minimal_stationary_repair, forget_probabilities,
    possibility_descent, deterministic_instrument,
)


def report() -> dict:
    c0=CarrierStage("carrier-source","source-basis",0,"root",(0,1,2,3))
    c1=CarrierStage("carrier-source","source-basis",1,"after-swap",(0,1,2,3))
    c2=CarrierStage("carrier-source","source-basis",2,"after-erase",(0,))
    preparation=tuple(tuple(Q(1,4) if x==y else Q(0)
                            for y in range(4))
                      for x in range(4))
    carrier=Carrier(("s0","s1","s2","s3"),c0,preparation)
    q0=CarrierQuotient(c0,(0,0,1,1),"E0")
    q1=CarrierQuotient(c1,(0,0,1,1),"E1")
    q2=CarrierQuotient(c2,(0,),"E2")
    swap=CarrierInstrument(
        "swap",c0,c1,("ok",),(True,)*4,
        tuple(((0,d,Q(1)),) for d in (1,0,3,2)))
    read=CarrierInstrument(
        "read/erase",c1,c2,("left","right"),(True,)*4,
        tuple(((0 if c<2 else 1,0,Q(1)),) for c in range(4)))
    cert=transport_actual_history(
        carrier,q0,
        (CarrierStep(swap,q0,q1,"ok"),
         CarrierStep(read,q1,q2,"right")),
        original_target=("L","L","R","R"))
    if not cert.original_joint_law_equal_at_every_prefix:
        raise AssertionError("Carrier is not a lawful history object")

    future=CarrierStage("carrier-source","source-basis",1,"two-states",(0,1))
    qfuture=CarrierQuotient(future,(0,1),"future")
    probe=CarrierInstrument(
        "future-revelation",c0,future,("ok",),(True,)*4,
        tuple(((0,d,Q(1)),) for d in (0,1,1,1)))
    minimal=repair_one_step(q0,((probe,qfuture),))
    if minimal.after.labels!=(0,1,2,2):
        raise AssertionError("Canonical one-step repair not minimal")
    bad=CarrierInstrument(
        "counterfeit-marginal",c0,c0,("yes","no"),(True,)*4,
        (
          ((0,0,Q(1,4)),(1,0,Q(3,4))),
          ((0,1,Q(3,4)),(1,1,Q(1,4))),
          ((0,2,Q(1,2)),(1,2,Q(1,2))),
          ((0,3,Q(1,2)),(1,3,Q(1,2)))
        ))
    same_support=possibility_descent(forget_probabilities(bad),q0,q0)
    no_stochastic=audit_descent(bad,q0,q0)
    if not same_support or no_stochastic.valid:
        raise AssertionError("Support/law firewall was incorrectly removed")
    stationary=CarrierInstrument(
        "stationary-read",c0,c0,("L","R"),(True,)*4,
        tuple(((0 if c<2 else 1,c,Q(1)),) for c in range(4)))
    split=CarrierInstrument(
        "stationary-split",c0,c0,("ok",),(True,)*4,
        tuple(((0,d,Q(1)),) for d in (0,2,2,0)))
    final=minimal_stationary_repair(c0,(stationary,split),(0,0,1,1))
    if not final.stabilized or final.partition != (0,1,2,3):
        raise AssertionError("Stationary current-carrier repair lost dynamic distinction")

    return {
        "status":"EXACT_SOURCE_INDEXED_CARRIER_HISTORY_AND_REPAIR",
        "source_id":carrier.stage.source_id,
        "original_states":len(carrier.originals),
        "initial_current_states":carrier.stage.count,
        "actual_history":[[a,z] for a,z in cert.public_trace],
        "final_original_posterior":[str(x) for x in cert.original_posterior],
        "evidence":str(cert.fine_path_probability),
        "fine_coarse_evidence_equal":cert.fine_path_probability ==
            cert.coarse_path_probability,
        "actual_original_source_support":sorted(cert.original_support),
        "all_prefix_joint_laws_transport":cert.original_joint_law_equal_at_every_prefix,
        "original_target_certified_relative_to_declared_source":
            cert.original_target_transport_valid,
        "one_step_minimal_refined_labels":list(minimal.after.labels),
        "one_step_new_classes":minimal.new_information_classes,
        "stationary_refinement_labels":list(final.partition),
        "stationary_refinement_count":len(final.steps),
        "support_only_lumps_but_law_does_not":same_support and not no_stochastic.valid,
        "failed_law_witness_reason":no_stochastic.witness.issue,
        "exact_deterministic_embedding":deterministic_instrument(swap),
        "scope":{
            "declared_finite_original_and_current_carriers":True,
            "empirically_authenticated_source":False,
            "physically_executed_counterfactual_branches":False,
            "unrestricted_causal_history_sheaf_proved":False,
            "whole_program_Lean_refinement_proved":False,
            "completed_Weil_positivity_or_RH_proved":False,
            "main_merge_executed":False,
        }
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
