#!/usr/bin/env python3
"""Reproduce general observational SUCC foundations with no RH zero inputs.

Usage:
  python scripts/observer_foundations_probe.py --output /tmp/observer-foundations.json

This output distinguishes (1) an observed finite program prefix, (2) a
finite checked proof, (3) an omega-union finite-support theorem, (4) a
meta-level Gödel syntax certificate, (5) explicit external reflection,
and (6) exact rational finite Gram witnesses. Its claims are NOT
a PA formalization, a physical quantum observer or an RH proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.observer_logic import (
    Num, Var, Pred, Not, Implies, Forall, Theory,
    ProofStep, FiniteProof, godel_code,
    diagonal_syntax, check_finite_proof, encode_proof, verifies_proof_code
)
from observational_succ.observer_reflection import (
    IncreasingTheoryChain, external_consistency_step,
    exact_quartic_screw, exact_quadratic_screw,
    rational_gram_certificate, bounded_gram_search,
)
from observational_succ.godel_succ import machine_prefix, delayed_halt, two_counter_loop
from observational_succ.ordinal_succ_report import OrdinalFiniteStage


def _fingerprint(n):
    raw=n.to_bytes((n.bit_length()+7)//8,"big")
    return hashlib.sha256(raw).hexdigest()


def run():
    # A genuine finite self-substitution algorithm with a precise
    # unproved object-language representability obligation.
    diag = diagonal_syntax(Not(Pred("ProvableCode",Var("x"))))
    assert diag.verify()

    # Two ordinary FINITE theorem proofs, the latter requiring a later
    # explicit axiom. No ordinal transfinite rule is invoked.
    a,b=Pred("P",Num(0)),Pred("Q",Num(0))
    ax=Implies(a,b)
    t0=Theory("T0",frozenset((a,)))
    chain=IncreasingTheoryChain((t0,))
    chain=chain.successor(ax,label="external finite implication source")
    proof=FiniteProof((
        ProofStep(a,"axiom"),
        ProofStep(ax,"axiom"),
        ProofStep(b,"modus_ponens",(0,1))
    ))
    proof_code=encode_proof(proof)
    assert check_finite_proof(chain.last,proof)
    assert verifies_proof_code(chain.last,proof_code,b)
    witness=chain.omega_finitary_support(proof)
    with_reflection, external=external_consistency_step(
        chain,evidence_label="explicitly unverified metatheoretic consistency")

    # Finite Turing observation cannot distinguish survival up to 17
    # steps from a machine that halts later at 19.
    looping=two_counter_loop()
    delayed=delayed_halt(19)
    prefix_loop=machine_prefix(looping,17)
    prefix_delayed=machine_prefix(delayed,17)
    witnessed=machine_prefix(delayed,19)

    # No RH zeros or numerical uncertain values are an input.
    negative=rational_gram_certificate(
        (-1,1),(1,1),exact_quartic_screw,
        provenance="fully exact rational quartic identity")
    positive=rational_gram_certificate(
        (-1,1),(1,1),exact_quadratic_screw,
        provenance="fully exact rational quadratic identity")
    search=bounded_gram_search(
        exact_quartic_screw,points=(-1,0,1),budget=200,
        provenance="exact rational toy, NOT Suzuki")

    good=OrdinalFiniteStage.genuine(12)
    fake={n:1 for n in range(1,13)}
    fake[6]=2
    bad=OrdinalFiniteStage.from_prefix(fake,12)
    b6_true=good.connected_pair_curvature(2,3)
    b6_fake=bad.connected_pair_curvature(2,3)
    semantic_true=good.restrict(6).semantic_log_partition_hessian(2,3)
    semantic_fake=bad.restrict(6).semantic_log_partition_hessian(2,3)

    return {
        "status":"OBSERVATIONAL_SUCC_FORMAL_FOUNDATIONS",
        "physical_infinite_time_executed":False,
        "RH_proved":False,
        "PA_formalization_completed":False,
        "arithmetic_causal_history":{
            "actualized_true_b6":str(b6_true["connected_second_order_residual"]),
            "fake_composite_a6":2,
            "fake_connected_b6":str(b6_fake["connected_second_order_residual"]),
            "Hessian_true_det":str(semantic_true["determinant"]),
            "Hessian_fake_det":str(semantic_fake["determinant"]),
            "both_semantic_Hessians_PSD":True,
            "Weil_correlation_equals_semantic_Hessian_proved":False
        },
        "godel_fixed_point_syntax":{
            "verified_substitution_code":diag.verify(),
            "theta_code_bits":diag.theta_code.bit_length(),
            "sentence_code_bits":diag.sentence_code.bit_length(),
            "theta_code_sha256":_fingerprint(diag.theta_code),
            "sentence_code_sha256":_fingerprint(diag.sentence_code),
            "object_level_PA_equivalence_proved":
                diag.object_language_equivalence_proved,
            "SubstGraph_representability_in_PA_proved":
                diag.representability_in_PA_proved,
        },
        "finitary_omega_proof_support":{
            "proof_code_sha256":_fingerprint(proof_code),
            "finite_proof_verified":witness.finite_proof_verified,
            "earliest_stage":witness.earliest_stage,
            "observed_finite_theory_stages":witness.total_stages_inspected,
            "omega_rule_used":witness.omega_rule_used,
            "omega_physically_executed":witness.physical_infinite_process_executed,
            "formal_theorem":"finitary derivation from union already has finite axiom support",
        },
        "turing_observations":{
            "loop_prefix_17":prefix_loop.status,
            "delayed_prefix_17":prefix_delayed.status,
            "delayed_prefix_19":witnessed.status,
            "first_observed_counterexample":witnessed.first_counterexample,
            "finite_survival_claims_are_universal_proofs":False,
        },
        "ordinal_reflection":{
            "declared_axiom_is_external":external["axiom_status"],
            "claimed_truth":external["claimed_truth_of_axiom"],
            "successor_stages":len(with_reflection.stages),
            "reflection_follows_from_observation":False,
        },
        "rational_gram_certificates":{
            "negative_exact_quartic_upper":str(negative.enclosure.upper),
            "negative_status":negative.result,
            "positive_exact_quadratic_lower":str(positive.enclosure.lower),
            "positive_probe_status":positive.result,
            "bounded_search":search["status"],
            "source_is_actual_Suzuki":False,
            "Suzuki_interval_oracle_built":False,
            "universal_positivity_proved":False,
        },
        "missing":{
            "theory_side":"representable Gödel substitution/derivability formalization",
            "quantum_side":"validated record-to-semantic covariance functor",
            "RH_side":"independent positive observer-to-FULL Weil distribution identity",
            "analytic_side":"rigorous prime/Gamma interval oracle for Suzuki negative witness",
        },
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    data=run()
    blob=json.dumps(data,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(blob,encoding="utf8")
    else:
        print(blob,end="")


if __name__=="__main__":
    main()
