#!/usr/bin/env python3
"""Exact Fraction-only additive-adelic source receipt and deterministic verification."""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import sys

from observational_succ.adelic_additive_gluing import (
    orbit_states, original_phase_parts, epoch_conductor_and_support,
    exact_crt_tv_from_haar, full_crt_spectral_energy,
    source_p_history, source_prime_injection, holonomy_exponent,
    holonomy_center, holonomy_error_bound, critical_steps,
    coboundary_defect_delta, coboundary_delta_center, coboundary_delta_error,
)

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]


def _hash(relative_path: str) -> str:
    return hashlib.sha256((ROOT/relative_path).read_bytes()).hexdigest()


def build():
    states=orbit_states(85)
    source={}
    for n in (1,2,3,5,8,13,21,34,55,85):
        u=states[n];local=original_phase_parts(n,states=states)
        source[str(n)]={"unwrapped":str(u),"fractional_phase":str(u%1),
          "prime_additive_parts":{str(p):str(v) for p,v in local.items()},
          "crt_phase_verified":sum(local.values())%1==u%1}
    epochs={}
    for a in (4,8,16,32):
        q,s,_=epoch_conductor_and_support(a)
        epochs[str(a)]={"crt_conductor":str(q),"support":s,"A":a,
           "tv_from_Haar":str(exact_crt_tv_from_haar(a)),
           "full_spectral_excess":str(full_crt_spectral_energy(a)),
           "spectral_lower_bound":str(Fraction(q,a)-1)}
    births={}
    for a,p in ((32,73),(80,193),(100,233)):
        nonzero=[(n,source_prime_injection(p,n)) for n in range(1,2*a) if source_prime_injection(p,n)]
        C=source_p_history(p,2*a-1)
        births[str(a)]={"p":p,"births":nonzero,
            "first_observed_residue":C[a],"last_observed_residue":C[2*a-1]}
    holos={}
    for a in (4,16,32,64):
        k=critical_steps(a)
        t=holonomy_exponent(a,k);d=coboundary_defect_delta(a,k)
        holos[str(a)]={"k":k,"theta":str(t),"center":str(holonomy_center(a,k)),
            "residual_bound":str(holonomy_error_bound(a,k)),
            "coboundary_delta":str(d),"delta_center":str(coboundary_delta_center(a,k)),
            "delta_error_bound":str(coboundary_delta_error(a,k))}
    return {"status":"FINITE EXACT DATA; NO PI NORMALITY THEOREM",
            "original_zero_seed":0,"source_poles":"4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)",
            "source_file_sha256":_hash("observational_succ/adelic_additive_gluing.py"),
            "root_tests_sha256":_hash("tests/test_adelic_additive_gluing.py"),
            "source_snapshots":source,"finite_CRT_epochs":epochs,"p_birth_oracles":births,
            "critical_scale_holonomy":holos}


def main():
    expected=HERE/'EXACT_RECEIPT.json'
    data=json.dumps(build(),indent=2,sort_keys=True)+'\n'
    digest=hashlib.sha256(data.encode()).hexdigest()
    if sys.argv[1:]==['--write']:
        expected.write_text(data)
    elif sys.argv[1:]==['--verify']:
        if not expected.exists() or expected.read_text()!=data:
            raise SystemExit('STALE/MISSING exact adelic receipt')
    else:
        raise SystemExit('usage: exact_receipt.py --write|--verify')
    print('PASS exact receipt; sha256',digest)

if __name__=='__main__':
    main()
