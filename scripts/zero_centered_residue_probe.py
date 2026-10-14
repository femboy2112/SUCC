#!/usr/bin/env python3
"""Exact, zero-independent finite residue-clock receipt; RH PROVED: no."""
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fractions import Fraction as Q
from observational_succ.zero_centered_residue import (
    coefficients,receipt,distance_interval,blackout,fake_cell_delta)


def run():
    good={k:receipt(k) for k in (2,3,4,6,8,12,20,26)}
    bad=receipt(12,{6:-1})
    assert all(v["all_prefix_cells_exact"] for v in good.values())
    assert bad["first_bad_divisor"] == 6
    cases={}
    for K in (2,3,4,6,8,12):
        a=coefficients(K)
        lo,hi=distance_interval(a,512)
        cases[K]={"squared_distance_rational_interval":[str(lo),str(hi)],
                  "LCM_blind_spot":blackout(a)}
    return {"status":"FINITE_SUCC_RESIDUE_CERTIFIED",
            "genuine_horizons":list(good),"fake_six":bad,
            "mellin_fake_six_delta_at_s2":str(fake_cell_delta(2,6,Q(1,2))),
            "distance_cases":cases,"zero_locations_used":False,
            "full_Gamma_and_Weil_identified":False,
            "L2_convergence_proved":False,"RH_proved":False}


if __name__=="__main__":
    output=json.dumps(run(),indent=2,sort_keys=True)
    if len(sys.argv)==3 and sys.argv[1]=="--output":
        Path(sys.argv[2]).write_text(output+"\n")
    elif len(sys.argv)==1:
        print(output)
    else:
        raise SystemExit("usage: python scripts/zero_centered_residue_probe.py [--output PATH]")
