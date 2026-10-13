"""Reproduce exact structural heuristics evidence and negative controls."""
from __future__ import annotations
import json
from fractions import Fraction as Q
from observational_succ.heuristic_bridge_discovery import (
    holdout_shape_demo,cross_context_analogy_demo)
from observational_succ.heuristic_shape_learning import learning_demo
from observational_succ.heuristic_joint_noise import repeated_measurement_witness
from observational_succ.contextual_heuristics import syntax_clone_counterexample
from observational_succ.heuristic_evidence_martingales import (
    noisy_limit_witness,adaptive_crossing_probability)
from observational_succ.contextual_heuristics import ModelProbe


def receipt():
    p=ModelProbe("up","declared",("positive","negative"),
                 {"null":(Q(1,2),Q(1,2)),"alternative":(Q(3,4),Q(1,4))})
    q=ModelProbe("left","declared",("positive","negative"),
                 {"null":(Q(1,3),Q(2,3)),"alternative":(Q(2,3),Q(1,3))})
    def policy(history):
        return p if (not history or history[-1][1]=="positive") else q
    r={"schema":"SUCC_CONTEXTUAL_HEURISTIC_OBSERVER_V1",
       "scope":"FINITE_DECLARED_SOURCE_PROBABILISTIC_AND_CATEGORICAL_MODEL_SEARCH",
       "positive_stieltjes_alias":holdout_shape_demo(),
       "structural_bridge":cross_context_analogy_demo(),
       "learned_analogy":learning_demo(),
       "shared_latent_double_count_rejected":repeated_measurement_witness(),
       "syntax_duplicate_counterexample":syntax_clone_counterexample(),
       "noise_full_support_limit":noisy_limit_witness(Q(3,4),20),
       "null_optional_stopping":adaptive_crossing_probability(
           policy,7,null="null",alternative="alternative",alpha=Q(1,10)),
       "formal_math_proof_from_heuristic_posterior":False,
       "physical_source_authenticated":False,
       "Weil_positivity_or_RH_proved":False}
    assert r["positive_stieltjes_alias"]["s4_expected_target_gini_gain"]==Q(2,1946711832863)
    assert r["shared_latent_double_count_rejected"]["sourced_conditional"]["source_conditional_law_verified"]
    assert r["syntax_duplicate_counterexample"]["quotient_A_after"]==Q(1,2)
    return r


def as_json(v):
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):as_json(w) for k,w in v.items()}
    if isinstance(v,tuple) or isinstance(v,list):return [as_json(x) for x in v]
    return v


if __name__=="__main__":
    print(json.dumps(as_json(receipt()),sort_keys=True,indent=2))
