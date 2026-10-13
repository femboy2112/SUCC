#!/usr/bin/env python3
"""Deterministic EODCS II scientific receipt; source claims remain conditional."""
from __future__ import annotations

import json

from observational_succ.causal_nerode_succ import causal_repair_demo
from observational_succ.nerode_probe_growth import (
    nerode_moonshot_demo, ObserverDynamics, grow_probe_grammar,
)
from observational_succ.eodcs_multi_action_source import (
    newly_generated_probe_demo, dark_toolkit_demo, ActionSource,
    curvature_resolution,
)
from observational_succ.eodcs_genetic_probe_genesis import genetic_probe_demo


def receipt() -> dict:
    states=tuple("s"+str(i) for i in range(7))
    known_counterexample=ObserverDynamics(
        "greedy-optimum-falsifier",0,"tri",states,
        tuple(states[i] for i in (5,6,0,6,2,4,3)),
        tuple(str(i) for i in (2,2,0,2,1,2,0)))
    false_optimum=grow_probe_grammar(known_counterexample)

    six=("x","y","u","v","c","d")
    extended=ActionSource("curvature-rotated-by-probe",0,"three-actions",
                          six,("0","0","0","0","0","1"),
                          ("A","B","C"),
                          (("u","v","u","v","c","d"),
                           ("x","y","c","d","c","d"),
                           ("x","y","d","v","c","d")))
    curvature=curvature_resolution(extended,"A","B")
    result={
        "status":"EXACT_FINITE_EODCS_II_CAUSAL_AND_PROBE_RECEIPT",
        "source_changing_square":causal_repair_demo(),
        "finite_observer_stabilization":nerode_moonshot_demo(),
        "greedy_not_global_minimum":{
            "source":"greedy-optimum-falsifier",
            "greedy_offsets":list(false_optimum.greedy_offsets),
            "greedy_cost":false_optimum.greedy_declared_cost,
            "independently_exhaustive_offsets":list(
                false_optimum.exact_minimum_cost_offsets),
            "exact_cost":false_optimum.exact_declared_cost,
            "genetic_or_greedy_search_complete":False,
        },
        "composite_probe_birth":newly_generated_probe_demo(),
        "closed_toolkit_darkness":dark_toolkit_demo(),
        "curvature_rotated_by_new_instrument":{
            "immediate_source_states":[x[0] for x in curvature["observable_immediate"]],
            "previously_dark_state_now_delayed":
                [[x[0],list(x[3])]
                 for x in curvature["observable_after_generated_word"]],
            "source_dark_remaining":
                [x[0] for x in curvature["dark_under_available_probe_closure"]],
            "physical_curvature_authenticated":False,
        },
        "genetic_probe_language":genetic_probe_demo(),
        "scope":{
            "finite_complete_declared_source":True,
            "lean_proofs_run_by_this_script":False,
            "actual_physical_counterfactual_probe_constructed":False,
            "physical_source_authenticated":False,
            "uniform_finite_horizon_for_all_source_sizes":False,
            "genetic_heuristic_is_proof":False,
            "unbounded_unexpected_math_invented":False,
            "completed_Weil_Suzuki_or_RH_proved":False,
            "independent_mathematical_priority_claimed":False,
        },
    }
    assert result["source_changing_square"]["first_step_obstruction_not_erased"]
    assert result["greedy_not_global_minimum"]["greedy_cost"] > result["greedy_not_global_minimum"]["exact_cost"]
    assert result["genetic_probe_language"]["dark_source_finite_grammar_empty"]
    return result


if __name__=="__main__":
    print(json.dumps(receipt(),indent=2,sort_keys=True))
