#!/usr/bin/env python3
"""Deterministic exact-source replay for Minimal Genesis; no pi digits and no floats."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

from observational_succ.minimal_circle_carry import (
    exact_origin_moment,independent_origin_moment,first_carry_excess,
    haar_bad_frame_upper,finite_green_residual,zero_action_circle_origins)
from observational_succ.minimal_moment_clock import minimum_moment_clock
from observational_succ.minimal_green_obstruction import finite_intertwiner_obstruction

ROOT=Path(__file__).resolve().parents[1]
FROZEN=ROOT/"research/2026-10-24/MINIMAL_GENESIS_FINITE_RECEIPT.json"

def receipt():
    moment3=exact_origin_moment(16,3,17)
    moment4=exact_origin_moment(16,4,17)
    k,prob=haar_bad_frame_upper(16,100,Q(1,2))
    L,factors=finite_intertwiner_obstruction((Q(1,2),Q(15,16)),(1,2,0))
    clock_count=minimum_moment_clock(16,3,16,require_unit=True)
    assert moment3-independent_origin_moment(3,17)==first_carry_excess(16,3)
    assert moment4-independent_origin_moment(4,17)==first_carry_excess(16,4)
    return {
        "schema":1,
        "source":"base16 circle Haar and authentic rational BBP forcing",
        "pi_normality_proved":False,
        "RH_proved":False,
        "no_new_lean_kernel_authority":True,
        "first_carry_degree":17,
        "first_detectable_even_moment":34,
        "hex_N3_first_excess":first_carry_excess(16,3),
        "hex_N3_moment":str(moment3),
        "hex_N3_independent":str(independent_origin_moment(3,17)),
        "hex_N4_first_excess":first_carry_excess(16,4),
        "hex_N4_moment":str(moment4),
        "hex_N4_independent":str(independent_origin_moment(4,17)),
        "hex_N5_first_excess":first_carry_excess(16,5),
        "hex_N100_first_excess":first_carry_excess(16,100),
        "hex_N3_degree16_unit_clock":list(clock_count),
        "hex_N3_degree16_nonunit_clock":list(minimum_moment_clock(16,3,16)),
        "haar_bad_origin_half_N100":{"moment_degree":k,"upper":str(prob)},
        "bbp_first_green_residual":str(finite_green_residual(0,1)),
        "stable_koomp_finite_cycle":{"period":L,"nonzero_factors":[str(z) for z in factors]},
        "hex_source_blind_zero_action_fixed_points":len(zero_action_circle_origins(16))
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--check",action="store_true")
    args=p.parse_args()
    current=receipt()
    if args.check:
        previous=json.loads(FROZEN.read_text())
        if previous!=current:
            raise SystemExit("FAIL: exact-source receipt mismatch")
    print(json.dumps(current,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
