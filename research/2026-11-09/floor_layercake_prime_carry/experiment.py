"""Exact finite carry floor/prime-threshold probe for SUCC research FLP.

Run from repo root: PYTHONPATH=. python research/2026-11-09/floor_layercake_prime_carry/experiment.py --verify
No pi digit oracle, no forced randomness, no asymptotic claims.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import ceil
from pathlib import Path

from observational_succ.duck_bbp import forcing
from observational_succ.bbp_floor_layercake import (
    carry_from_thresholds, modular_injection, prime_carry,
    boundary_distance, joint_carry_step,
)


def observed_epoch(A: int, p: int) -> dict:
    if A < 32 or p <= 5 or p % 2 == 0:
        raise ValueError("positive source epoch and odd prime candidate required")
    original=F(0)
    changed=F(1,5)
    prime=0
    matched=0
    different=0
    corrections=0
    near=0
    born=[]
    births=[]
    real_sum=0
    prime_sum=0
    epsilon=F(1,512)
    for n in range(1,2*A):
        r=forcing(n)
        j=modular_injection(n,p)
        if j:born.append(n)
        if n>=2:
            next_prime,z=prime_carry(prime,j,p)
            if A<=n<2*A:
                step=joint_carry_step(original,prime,n,p)
                k=step["kappa"]
                kw=carry_from_thresholds(changed,r)
                matched+=int(k==z)
                different+=int(k%16!=kw%16)
                corrections+=int(k!=carry_from_thresholds(original,F(0)))
                near+=int(boundary_distance(original,r)<epsilon)
                real_sum+=k
                prime_sum+=z
                if j:births.append({"n":n,"prime_injection":j,"prime_carry":z,
                                    "real_carry":k,"slip":k-z})
            prime=next_prime
        else:
            prime=j
        original=(16*original+r)%1
        changed=(16*changed+r)%1
    C=F(1920,2457)
    L=0
    while C*16**(L+1) <= 15*(A+1)**2:
        L+=1
    return {"A":A,"p":p,"source_index_n":f"{A}..{2*A-1}",
            "prime_births_in_prefix":born,"inside_prime_births":births,
            "real_prime_equal_carry_count":matched,
            "changed_seed_one_fifth_real_mod16_mismatch_count":different,
            "forcing_induced_carry_correction_count":corrections,
            "inherited_AC01_bound":ceil(A/L),"AC01_gap_depth":L,
            "moving_boundary_radius":"1/512","moving_boundary_count":near,
            "Fejer_H4096_bound":str(F(2*near,A)+F(512,4096)),
            "actual_real_carry_mean":str(F(real_sum,A)),
            "actual_prime_carry_mean":str(F(prime_sum,A)),
            "p_primeity_provided_by_source_passport_not_this_probe":True}


def receipt() -> dict:
    cases=[(100,241),(128,313),(256,617)]
    return {"status":"OBSERVED_FINITE_EXACT","pi_base16_normality":"OPEN",
            "source":"original four signed BBP poles; U0=0; n>=2 layercake",
            "prime_simple_pole_passport":"#497/#554 assumed; finite residues checked",
            "threshold_integral":"Haar reference only; not selected orbit",
            "cases":[observed_epoch(a,p) for a,p in cases],
            "notes":["All count/progression quantities are exact integer/Fraction computations",
                     "Fejer budget is deterministic upper bound, not measured cancellation",
                     "The same-forcing seed 1/5 is a p-unit and preserves all odd p-primary histories",
                     "No unverified all-epoch signed estimate is inferred"]}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",action="store_true")
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    dst=Path(__file__).with_name("FINITE_RECEIPT.json")
    text=json.dumps(receipt(),sort_keys=True,indent=2)+"\n"
    if args.verify:
        assert dst.read_text(encoding="utf-8")==text,"receipt mismatch"
        print("PASS exact FLP finite receipt")
    elif args.write:
        dst.write_text(text,encoding="utf-8")
        print("wrote",dst)
    else:
        print(text)

if __name__=="__main__":main()
