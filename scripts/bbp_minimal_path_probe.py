#!/usr/bin/env python3
"""Independent arithmetic-source/Galois oracle for Operation MINIMAL PATH.

Runs from repository root, PYTHONPATH=. Finite integer/Fraction reconstruction
from the original BBP formula, NOT by calling source state generators.
Reports only exact finite facts, with separate Machin and BBP pi intervals.
No finite-to-infinite or subgroup exponent proof is inferred.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from math import gcd

from observational_succ.bbp_minimal_path import (
    prime_power_first_birth, prime_power_birth_count,
    rational_first_order_impossibility,
)
from observational_succ.bbp_galois_tomography import (
    source_galois_window, rational_cyclotomic_group_ring_moment,
    source_selected_galois_outlier_interval,
)
from observational_succ.bbp_prime_window_signed_intervals import machin_pi_interval
from observational_succ.bbp_source_memory import tail_interval


def first_source_index(p, depth):
    q=p**depth
    for n in range(1,q+3):
        if any(v%q==0 for v in (8*n-7,8*n-4,8*n-3,8*n-2)):
            return n
    raise AssertionError("independent exact first pole did not exist")


def independent_force(n):
    # Third description: collapsed rational function, not the 4 signed terms.
    return Q(120*n*n-89*n+16,
             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def independent_full_window(p):
    m=(p-1)//8
    y=Q()
    states=[]
    for n in range(1,4*m+1):
        y=(16*y+independent_force(n))%1
        if n>m:states.append(y)
    return tuple(states)


def independent_galois_profile(p):
    inp=source_galois_window(p)
    L,B,delta=inp["L"],inp["B"],inp["delta"]
    source=independent_full_window(p)
    complement=tuple((source[t]-Q(4*pow(16,t,p),p))%1
                     for t in range(delta))
    if complement!=inp["complement"]:
        raise AssertionError("independent rational SUCC source disagreed")
    formal=rational_cyclotomic_group_ring_moment(p)
    if formal["same_p_residue_pair_count"]!=delta*B:
        raise AssertionError("Galois source-period multiplicity mismatch")
    data=";".join(str(q.numerator)+"/"+str(q.denominator)
                  for q in complement)
    return {"p":p,"L":L,"B":B,"Delta":delta,
            "formal_terms":formal["signed_group_ring_terms"],
            "full_complement_sha256":hashlib.sha256(data.encode()).hexdigest()}


def main():
    for n in range(1,40):
        true=Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
        if true!=independent_force(n):
            raise AssertionError("wrong source rational formula")
    rows=[]
    for p in (3,5,7,11,13):
        for k in (1,2,3):
            expected=first_source_index(p,k)
            if expected!=prime_power_first_birth(p,k):
                raise AssertionError("prime-power source index mismatch")
            rows.append({"p":p,"depth":k,"birth":expected})
    for n in (1,8,20,80,250):
        counts=[prime_power_birth_count(n,k) for k in (1,2,3)]
        if not counts[0]>=counts[1]>=counts[2]:
            raise AssertionError("prime-depth census must decrease with depth")
    for n in range(1,12):
        a,r=rational_first_order_impossibility(n,Q(1,3))
        if not a or not r:
            raise AssertionError("Green minimal recurrence premise failed")
    tl,tu=tail_interval(0,16)
    ml,mu=machin_pi_interval(26)
    if not (16*tl<ml<mu<16*tu):
        raise AssertionError("two independent pi sources are inconsistent")
    outlier=source_selected_galois_outlier_interval(97,1,14,26)
    if not (outlier["selected_normalized_amplitude_sq_lower"]>Q(1,20)
            and outlier["galois_mean_square_upper"]<Q(1,40)):
        raise AssertionError("AUTHENTIC selected Galois outlier uncertified")
    receipt={
        "status":"FINITE EXACT PROOF CHECKS; NO PI NORMALITY CLAIM",
        "source":"original four BBP forcing-index poles + y0=0",
        "prime_power_first_births":rows,
        "independent_galois_conductor_profiles":[
            independent_galois_profile(p) for p in (17,41,73,97)],
        "rational_selected_97_gt":"1/20",
        "rational_galois_mean_97_lt":"1/40",
        "galois_selected_amplification_97_gt":"2",
        "all_horizon_equidistribution":"UNVERIFIED",
        "pi_normality":"OPEN"
    }
    print(json.dumps(receipt,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
