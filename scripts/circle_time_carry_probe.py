#!/usr/bin/env python3
"""Reproduce source-typed exact time-carry, 3-adic and Hankel witnesses."""
import argparse
import json
from fractions import Fraction as Q
from math import comb
from observational_succ.circle_time_carry import (
    haar_joint,first_time_carry_defect,periodic_moment,periodic_fejer_energy,
    hankel_det,haar_single,finite_probe_alias,periodic_joint)
from observational_succ.circle_collision_rigidity import pi_interval

def make_receipt():
    cases=[]
    for r in (2,3,4):
        length=3**(r-1);n=(length+1)//2
        cases.append({
            "r":r,"period":length,
            "first_hidden_moment_index":length,
            "haar_moment":str(comb(2*length,length)),
            "first_periodic_moment":str(periodic_moment(r,length)),
            "fejer_energy_below_period":str(periodic_fejer_energy(r,length-1)),
            "first_visible_fejer":str(periodic_fejer_energy(r,length)),
            "last_aliased_hankel":str(hankel_det(
                lambda k: periodic_moment(r,k),n-1)),
            "first_changed_hankel":str(hankel_det(
                lambda k: periodic_moment(r,k),n)),
            "haar_hankel":str(hankel_det(haar_single,n)),
        })
    lo,hi=pi_interval(23,80)
    results={
        "schema_version":1,
        "source_head":"5a2922986719c03dfd4e20d23d3b266b8b775c8e",
        "theorem_scope":"classical/paper exact, finite source tests",
        "pi_normality_proved":False,
        "physical_measurement":False,
        "first_time_carry_hex":first_time_carry_defect(16),
        "3adic_periodic_witnesses":cases,
        "finite_multitime_alias":finite_probe_alias(9,(0,1,3),(2,1,1)),
        "finite_multitime_haar":haar_joint(16,(0,1,3),(2,1,1)),
        "finite_multitime_periodic":periodic_joint(9,(0,1,3),(2,1,1)),
        "pi_source_bracket_valid":bool(Q(3)<lo<hi<Q(4))
    }
    assert results["first_time_carry_hex"]==-2
    for c in cases:
        assert int(c["first_periodic_moment"])==int(c["haar_moment"])+1
        assert Q(c["first_changed_hankel"])==Q(3,4)*Q(c["haar_hankel"])
    assert results["finite_multitime_alias"]
    assert results["finite_multitime_haar"]==results["finite_multitime_periodic"]
    return results

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--check",action="store_true")
    args=p.parse_args()
    data=make_receipt()
    if args.check and (data["pi_normality_proved"] or
                       data["first_time_carry_hex"]!=-2):
        raise SystemExit("source/claim mismatch")
    print(json.dumps(data,sort_keys=True,indent=2))
