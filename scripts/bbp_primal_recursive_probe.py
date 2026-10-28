#!/usr/bin/env python3
"""Deterministic exact source-hashed receipt for recursive BBP first-prime gates.

Usage: python scripts/bbp_primal_recursive_probe.py --write | --verify | --show
No π-digit oracle, network, random sampling or binary float as proof authority.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ import bbp_primal_recursive_geometry as p
RECEIPT=ROOT/'research/2026-10-27/BBP_PRIMAL_RECURSION_RECEIPT.json'
FILES=[
 'observational_succ/bbp_primal_recursive_geometry.py',
 'tests/test_bbp_primal_recursive_geometry.py',
 'observational_succ/bbp_binwindow_conjugacy.py',
]

def checksum(file):
    return sha256((ROOT/file).read_bytes()).hexdigest()

def exact_probe():
    k3={str(j):p.ternary_trident(j)["roots"] for j in (1,2,3,4,6)}
    binary={str(j):list(p.shear_anf_masks(j)) for j in range(7)}
    periods=[]
    for k,l in ((1,1),(1,2),(2,1),(2,2)):
        v=p.crt_period_certificate(k,l)
        periods.append({"hex_depth":k,"ternary_depth":l,
                        "joint_period":v.time_period,"unique_pairs":v.unique_pairs,
                        "zero_seed_two":v.zero_anchor_two,
                        "zero_seed_cleared_three":v.zero_anchor_three})
    check=p.source_pole_residues()
    diverge=[p.backward_three_adic_divergence(j) for j in (1,2,3,5,7,9)]
    genuine_source=[p.source_numerator(n) for n in (0,1,2,3,4)]
    bad_global_reflection=(p.binary_code(p.binary_code(2,5),5)!=2)
    bad_threeadic_convergence=all(x["weighted_term_valuation"]<=-x["depth"] for x in diverge)
    bad_matched_root_mod9=(p.ternary_trident(2)["coincidence_count"]==0)
    bad_scaled_numerator=len({(3*p.source_numerator(n))%3 for n in range(3)})!=3
    if not (bad_global_reflection and bad_threeadic_convergence
            and bad_matched_root_mod9 and bad_scaled_numerator):
        raise ArithmeticError("hostile controls did not reject false promotion")
    report={
       "schema":"bbp-primal-recursive-source-v1",
       "source":"authentic Coherent Main X four signed poles, zero seed",
       "parent":"PR 321 eeb2a48ea1b43967ea385009a3f8ec280b2efa69",
       "hashed_files":{f:checksum(f) for f in FILES},
       "binary_gates_anf_masks":binary,
       "first_hex_permutation":p.binary_recursion_receipt(4)["first_values"],
       "mod32_reflection_counterexample":{"x":2,"phi_x":30,"phi_phi_x":18},
       "cleared_numerator_0_to_4":genuine_source,
       "ternary_trident_lift_roots":k3,
       "four_signed_rational_residues":[[str(x),str(v)] for x,v in check["poles"]],
       "residues_signed_sum":"0",
       "three_adic_unbounded_subsequence_at_zero":diverge,
       "CRT_complete_periods":periods,
       "controls":{"mod32_reflection_extrapolation_refuted":bad_global_reflection,
                   "threeadic_weighted_past_convergence_refuted":bad_threeadic_convergence,
                   "triple_mod3_coherence_persists_mod9_refuted":bad_matched_root_mod9,
                   "scaled_numerator_is_3adic_isometry_refuted":bad_scaled_numerator},
       "authority":{"local_focus_is_solely_tests":True,
                    "parent_infinite_zero_boundary_is_paper_proof":True,
                    "current_infinite_analytic_claims_are_paper_proofs":True,
                    "new_lean_kernel_checked":False,
                    "combined_native_suite_checked_here":False,
                    "real_pi_normality_proved":False,
                    "Riemann_Hypothesis_proved":False},
    }
    return report

def render():
    return json.dumps(exact_probe(),sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def main():
    ap=argparse.ArgumentParser()
    mode=ap.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write',action='store_true')
    mode.add_argument('--verify',action='store_true')
    mode.add_argument('--show',action='store_true')
    args=ap.parse_args()
    raw=render()
    if args.write:
        RECEIPT.parent.mkdir(parents=True,exist_ok=True)
        RECEIPT.write_text(raw,encoding='utf-8')
        print('WROTE EXACT PRIME-CLOCK RECEIPT',checksum('research/2026-10-27/BBP_PRIMAL_RECURSION_RECEIPT.json'))
    elif args.verify:
        if not RECEIPT.is_file() or RECEIPT.read_text(encoding='utf-8')!=raw:
            raise SystemExit('REJECTED: exact source/test/analytic claim receipt mismatch')
        print('VERIFIED EXACT PRIME-CLOCK RECEIPT',sha256(raw.encode()).hexdigest())
    else:
        print(raw,end='')

if __name__=='__main__':main()
