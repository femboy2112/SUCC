#!/usr/bin/env python3
"""Exact Voyager projective observer / source-realization science receipt.

The infinite statements are mathematical theorems with explicit hypotheses
and Lean proofs, not infinite Python experiments or physical measurements.
The executable data are finite independently cross-checked witnesses.
"""
from __future__ import annotations
import json
from observational_succ.voyager_profinite_frontier import (
    voyager_demo, ideal_eventual_zero_stage, eventual_zero_lift,
    powers_of_two_pulse, power_two_gap_memory_lower_bound,
    truncated_ultrametric, power_two_period_refutation,
)


def receipt() -> dict:
    result=voyager_demo()
    stages=tuple(ideal_eventual_zero_stage(h) for h in range(0,11))
    projection=all({word[:-1] for word in stages[h+1]}==set(stages[h])
                   for h in range(10))
    gap=[]
    for k in range(1,8):
        h=2**(k+1)+1
        source=eventual_zero_lift(
            tuple(powers_of_two_pulse(i) for i in range(h)),
            source_id="controlled-pulse-gap-"+str(k))
        debt=power_two_gap_memory_lower_bound(source,k)
        gap.append({
            "k":k,
            "required_prefix":h,
            "source_memory_lower_bound":debt["certified_minimum_states"],
            "constructed_witness_machine_states":debt["actual_machine_states"]})
    if not projection or any(
        stages[h] != tuple(
            sorted(set(w[:-1] for w in stages[h+1])))
        for h in range(10)
    ):
        raise AssertionError("Every finite prefix should have extendible sources")
    result["all_eventually_zero_prefix_stage_counts"]=[
        len(stage) for stage in stages]
    result["all_finite_stage_restrictions_surjective"]=projection
    result["observational_memory_debt_by_horizon"]=gap
    result["source_specific_finite_refutation_is_not_infinite_execution"]=True
    result["independent_original_source_ontology_attested"]=False
    return result


if __name__=="__main__":
    print(json.dumps(receipt(),indent=2,sort_keys=True))
