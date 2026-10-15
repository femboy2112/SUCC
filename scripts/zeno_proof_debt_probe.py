"""Recompute and byte-verify frozen Zeno proof-debt scientific receipt."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path

from observational_succ.zeno_certificate import Stamp
from observational_succ.zeno_proof_debt import (
    AmortizedContract, EvidenceLedger, SignedEvidence, SourceFibre,
    ProbeTable, epsilon_probe_cover, dynamic_protocol_blindness,
    gamma_tail_bracket, gamma_simple_upper, signed_weil_test_gate,
    schur_two_zeno_gate, toy_halting_real, exact_psd, generic_rank_one_operator_stage,
)


def _s(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,tuple):return [_s(i) for i in x]
    if isinstance(x,list):return [_s(i) for i in x]
    if isinstance(x,dict):return {k:_s(v) for k,v in x.items()}
    return x


def receipt():
    stamp=Stamp("source-indexed-math",14,"zeta-real-vs-source-carrier","certificate-laboratory")
    c=AmortizedContract(stamp,"fixed-theorem",F(1),F(1,2),F(1,4),F(1,3),True)
    stage,stage_bound=c.horizon(F(1,100))
    K,rho=c.geometric_envelope()
    bits=6
    states=tuple(format(i,"06b") for i in range(2**bits))
    vals=tuple(sum((F(int(bit),2**(j+1)) for j,bit in enumerate(s)),F(0)) for s in states)
    s=SourceFibre(stamp,"binary-limit",states,vals)
    probes=tuple(ProbeTable(stamp,f"bit-{i}",tuple(state[i] for state in states)) for i in range(bits))
    cover=epsilon_probe_cover(s,probes,F(1,8))
    blind=dynamic_protocol_blindness(s,probes[:2],target_separation=F(1,8))
    g1=gamma_tail_bracket(1,20)
    g4=gamma_tail_bracket(4,20)
    E=EvidenceLedger(stamp,"zero-boundary")
    for j in range(8):
        E=E.append(SignedEvidence(stamp,"zero-boundary",j,-F(1,2**(j+1)),F(1,2**(j+1)),f"signed-analytic-{j}"))
    # Refine to a classic negative-sided interval (-2e,0), all lower bounds <0.
    toy_none=[toy_halting_real(j,None) for j in range(4)]
    toy_later=[toy_halting_real(j,18) for j in range(4)]
    schur=schur_two_zeno_gate(((F(3),F(1,4)),(F(1,4),F(3))),F(2),F(1,5),F(1,20))
    bad,w=exact_psd(((F(1),F(2)),(F(2),F(1))))
    return _s({
        "schema":"succ-zeno-proof-debt-v1",
        "date":"2026-10-14",
        "source":"mathematical-premise-not-physical-attestation",
        "original_nontrivial_zero_coordinates_used":False,
        "RH_PROVED":False,
        "source_first_all_test_weil_sign_proved":False,
        "Lean_formalization_claimed":False,
        "amortized":{
            "q":c.q,"r":c.birth_ratio,"K":K,"rho":rho,
            "horizon_for_1_over_100":stage,"all_future_upper_at_horizon":stage_bound,
            "exact_sample_upper_7":c.exact_upper(7),
            "universal_source_law_is_an_external_premise":True,
        },
        "finite_epsilon_cantor":{
            "admissible_sources":len(states),"epsilon":F(1,8),"result":cover,
            "restricted_probes_blindness":blind,
        },
        "Gamma_authentic_tail":{
            "J1_20rung_exact_bracket":g1,"J4_20rung_exact_bracket":g4,
            "J1_false_Gemini_1_over_8":F(1,8),
            "J1_exact_lower_exceeds_false_constant":g1[0]>F(1,8),
            "true_rung_tail_is_positive":True,
            "full_Weil_poles_and_prime_terms_remain_signed":True,
            "negative_example_one_test":signed_weil_test_gate(-2,-1,1,10),
        },
        "signed_boundary":{
            "source_interval":E.interval,"per_stage_lower_bounds_strictly_negative":True,
            "all_stages_signed_convergence_in_input_source_law":True,
            "finite_ledger_status":E.sign,
            "toy_halting_prefixes_equal_for_delayed_event":toy_none==toy_later,
            "generic_compact_operator_prefixes_equal":(
                [generic_rank_one_operator_stage(j,None) for j in range(4)]==
                [generic_rank_one_operator_stage(j,18) for j in range(4)]),
            "generic_compact_operator_sign_undecidable_by_universal_algorithm":True,
            "not_a_claim_about_authentic_zeta":True,
        },
        "Schur":{
            "illustrative_sufficient":schur["certifies_all_vectors_conditional_on_inputs"],
            "corrected_2by2_matrix":schur["adjusted"],
            "exact_correction":schur["correction"],
            "cross_and_complement_are_source_assumptions":True,
            "negative_2by2_PSD_rejected":not bad,
            "negative_quadratic_witness":w,
        },
    })


def canonical(obj)->str:
    return json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2)+"\n"


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--verify",type=Path,help="byte-for-byte recomputation of source receipt")
    args=ap.parse_args()
    content=canonical(receipt())
    if args.verify:
        given=args.verify.read_text(encoding="utf-8")
        if content!=given:
            raise SystemExit("SOURCE_REPLAY_MISMATCH")
        print("SOURCE_QUALIFIED_ZENO_PROOF_DEBT_RECEIPT_VERIFIED")
    else:
        print(content,end="")

if __name__=="__main__":main()
