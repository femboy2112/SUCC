#!/usr/bin/env python3
"""Replay six cluster-D assignments; exact rationals serialized as strings."""
import argparse
import hashlib
import json
import platform
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fractions import Fraction as Q
from observational_succ.cambrian_d_computation import (
    arbitrary_holdout,bayesian_calibration,destructive_greedy_countermodel,
    exhaustive_strategy_oracle,hidden_mode_receipt,memory_validation,
    optimal_cost,partial_source,resource_receipt,genetic_cost_policy,cegis_cost_policy,
    similarity_control,
    history_learning_validation,
)
from observational_succ.contextual_heuristics import syntax_clone_counterexample
from observational_succ.eodcs_multi_action_source import action_congruence
from observational_succ.noncommuting_proof_transport import FiniteCarrier,Instrument

BASE="5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def replay():
    partial=[]
    for cap in range(1,7):
        s=partial_source(tuple("empty" if i==0 else "pending" for i in range(cap+1)),
            ("enqueue","deliver"),
            (tuple(i+1 if i<cap else None for i in range(cap+1)),
             tuple(i-1 if i>0 else None for i in range(cap+1))))
        r=action_congruence(s)
        partial.append({"capacity":cap,"live_residual_classes":len(r.equivalence_classes)-1,
                        "sink_is_totalization_artifact":True,"class_counts":r.block_counts})
    holdouts=[memory_validation(arbitrary_holdout(seed,3+(seed%4)),genetic_seed=9000+seed)
              for seed in range(131,155)]
    histories=[history_learning_validation(arbitrary_holdout(seed,3+(seed%4)))
               for seed in range(271,295)]
    field,target,costs=destructive_greedy_countermodel()
    cost=optimal_cost(field,target,costs,2)
    oracle=exhaustive_strategy_oracle(field,target,costs,2)
    cases=trees=0
    from itertools import product
    for output,transition,enabled in product(product((0,1),repeat=2),
                                           product((0,1),repeat=2),
                                           product((False,True),repeat=2)):
        small=FiniteCarrier(2,(Instrument("a",output,transition,enabled),),"oracle","model")
        a=optimal_cost(small,("0","1"),{"a":Q(7,3)},2)
        b=exhaustive_strategy_oracle(small,("0","1"),{"a":Q(7,3)},2)
        if a["worst_case_cost"]!=b["worst_case_cost"]:raise AssertionError("Cost oracle mismatch")
        cases+=1;trees+=b["trees_enumerated"]
    module=Path(__file__).resolve().parents[1]/"observational_succ/cambrian_d_computation.py"
    return {"campaign":"CAMBRIAN_D_COMPUTATION","base_sha":BASE,
        "python":platform.python_version(),
        "implementation_sha256":hashlib.sha256(module.read_bytes()).hexdigest(),
        "formal_lean_verified":False,"physical_source_authenticated":False,
        "assignments": {
            "19":{"status":"CLASSICAL / PROVED CONDITIONAL / EXACT FINITE TESTED",
                  "bounded_queue_controls":partial,"infinite_queue_finite_realization":False,
                  "hidden_common_legality_relation_is_equivalence":False},
            "20":{"status":"PROVED CONDITIONAL / TESTED MODEL / CLASSICAL MECHANISM",
                  "heldout_generation_seeds":list(range(131,155)),"heldouts":holdouts,
                  "history_only_learning":histories,
                  "history_only_heldout_seeds":list(range(271,295)),
                  "genetic_separator_successes":sum(r["genetic_successes"] for r in holdouts),
                  "deterministic_repairs":sum(r["deterministic_repairs"] for r in holdouts),
                  "novel_representation_type_supplied_by":"residual-signature/table metaconstructor",
                  "grammar_invents_its_own_metagrammar":False},
            "21":{"status":"PROVED FINITE MODEL / EXACT CALIBRATION / MISSPECIFICATION COUNTERMODEL",
                  "cloning":syntax_clone_counterexample(),"calibration":bayesian_calibration()},
            "22":{"status":"CLASSICAL / PROVED FINITE HORIZON / INDEPENDENT EXHAUSTIVE TESTED",
                  "bellman":cost,"complete_strategy_tree_oracle":oracle,
                  "all_two_state_one_action_cases":cases,"oracle_trees_checked":trees,
                  "greedy_cost_normalized_gini_cheap":Q(1,3),
                  "greedy_cost_normalized_gini_full":Q(2,15),
                  "genetic_depth_two_policy_runs":[genetic_cost_policy(field,target,costs,seed=i) for i in range(10)],
                  "cegis_bounded_policy":cegis_cost_policy(field,target,costs),
                  "cheap_first_irreversibly_loses_original_claim":True},
            "23":{"status":"CLASSICAL / PROVED CONDITIONAL / EXACT RATIONAL TESTED",
                  "hidden_mode":hidden_mode_receipt(),"similarity_twin_moments":similarity_control(),
                  "internal_physical_topology_identified":False},
            "24":{"status":"CLASSICAL / PROVED LOWER BOUND / EXACT FINITE COLLISION WITNESSES",
                  "resources":resource_receipt(),"generic_effective_witness_search_claimed":False}}}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output")
    args=parser.parse_args()
    data=json.dumps(replay(),indent=2,sort_keys=True,default=lambda q:str(q) if isinstance(q,Q) else q)+"\n"
    if args.output:Path(args.output).write_text(data)
    else:print(data,end="")
