"""Reproduce preregistered 65536 original BBP hex digits and the exact 16x16 table.

Research-only. No pi oracle, no normality inference. Run explicitly:
    python research/2026-11-09/bbp_spatial_haar_lift/reproduce.py
"""
from __future__ import annotations
from hashlib import sha256
from fractions import Fraction
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from observational_succ.bbp_spatial_haar_lift import (
    bulk_pi_hex_digits, word_counts, two_digit_energies,
)

def run() -> dict:
    digits=bulk_pi_hex_digits(65536,24)
    if digits!=bulk_pi_hex_digits(65536,32):
        raise AssertionError("independent BBP guards disagree")
    full_sha=sha256((digits+"\n").encode()).hexdigest()
    prior_sha=sha256((digits[:40960]+"\n").encode()).hexdigest()
    if full_sha!="e42ee060201573db4a32a8c8e0a4ccac5a6cb061ae1ac8d71809234c58dfae53":
        raise AssertionError("new source certificate hash changed")
    if prior_sha!="c4010a291cf411147dd1a6a65104bd4cf995a4d931b6dfefb9fd9277f8434527":
        raise AssertionError("40,960 certified digits disagree with SUCC #561")
    out={"n":len(digits),"sha256_with_newline":full_sha,
         "prior40960_sha256_with_newline":prior_sha,
         "first32":digits[:32],"last32":digits[-32:],
         "status":"CERTIFIED FINITE ONLY; pi normality OPEN"}
    for cyclic in (False,True):
        M=word_counts(digits,cyclic)
        er,ec,e2,em=two_digit_energies(M)
        name="cyclic_artificial_wrap" if cyclic else "linear_actual_pairs"
        out[name]={"pair_count":sum(map(sum,M)),
                   "transition_counts":M,
                   "energy_1_row":str(er),"energy_1_column":str(ec),
                   "energy_2":str(e2),"mixed_225_energy":str(em),
                   "min_count":min(map(min,M)),"max_count":max(map(max,M))}
    if out["cyclic_artificial_wrap"]["energy_2"]!="35323/8388608":
        raise AssertionError("cyclic pair-energy mismatch")
    if out["cyclic_artificial_wrap"]["mixed_225_energy"]!="265587/67108864":
        raise AssertionError("225-mode mixed energy mismatch")
    if out["linear_actual_pairs"]["energy_2"]!="18061567/4294836225":
        raise AssertionError("linear pair-energy mismatch")
    return out

if __name__=="__main__":
    print(json.dumps(run(),sort_keys=True,indent=2))
