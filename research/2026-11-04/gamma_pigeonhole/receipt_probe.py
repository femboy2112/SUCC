"""Deterministic exact rational Euler/Gamma prime-window receipt. No pi digits."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from gamma_pigeonhole import (pole_split,birth_register,gamma_corrected_pin,
                             coset_count,gamma_delta_bounds)
from fractions import Fraction as F

EPOCHS=(3,6,10,12,13,15,18)

def row(n:int)->dict:
    s=pole_split(n);b=birth_register(n)
    p=s["p"];C=s["C_force"]
    lo,hi=gamma_delta_bounds(p,16)
    countlo=coset_count(p*C,p,4*C,F(0),30*lo)
    counthi=coset_count(p*C,p,4*C,F(0),30*hi)
    pin=gamma_corrected_pin(n,4) if p>=41 else None
    data={"n":n,"p":p,"r":str(s["r"]),"C_force":C,"C_state":b["C_state"],
          "gamma_16_lower":str(30*lo),"gamma_16_upper":str(30*hi),
          "coarse_interval_count_lower":countlo,
          "coarse_interval_count_upper":counthi,
          "corrected_lower":str(pin["window_lo"]) if pin else None,
          "corrected_upper":str(pin["window_hi"]) if pin else None,
          "cofactor_address":pin["cofactor_address"] if pin else None,
          "authentic_p_residue":b["p_residue"]}
    digest=hashlib.sha256(json.dumps(data,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {"n":n,"p":p,"forcing_conductor_bits":(p*C).bit_length(),
            "state_conductor_bits":b["Q"].bit_length(),
            "coarse_gamma_candidate_count_certified": countlo if countlo==counthi else [countlo,counthi],
            "gamma_corrected_unique":pin is not None,
            "corrected_scaled_width":format(float(pin["scaled_width"]),".12f") if pin else None,
            "exact_fraction_record_sha256":digest}

def receipt()->dict:
    return {"name":"SUCC original four-pole Gamma-pigeonhole source pinning",
            "base_main_sha":"a673ec95dfac4ef6a61c60222be8b615fd08535d",
            "instrument":"exact Fraction original source and Gamma alternating enclosures",
            "development_grid_not_blind":True,
            "pi_base16_normality":"OPEN","signed_weyl_gate":"OPEN","RH":"OPEN",
            "rows":[row(n) for n in EPOCHS]}

def output()->str:
    return json.dumps(receipt(),indent=2,sort_keys=True)+"\n"

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--write",type=Path)
    parser.add_argument("--verify",type=Path)
    args=parser.parse_args()
    result=output()
    if args.write: args.write.write_text(result)
    if args.verify:
        assert args.verify.read_text()==result,"exact Fraction receipt failed reproduction"
        print("GAMMA_PIGEONHOLE_SOURCE_PIN_RECEIPT_VERIFIED")
    if not args.write and not args.verify:print(result)
