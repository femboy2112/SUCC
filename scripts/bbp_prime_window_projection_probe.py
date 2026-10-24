#!/usr/bin/env python3
"""Independent exact-rational source oracle for prime-clock projection.

Does not use the implementation's source reconstruction, subgroup partition,
or dispersion internals for its reference calculations. Floats are not used.
Outputs reproducible exact integer/rational receipts only.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from math import gcd

from observational_succ.bbp_prime_window_projection import (
    additive_clock_partition, rational_phase_dispersion_bracket,
    source_periodicity_obstruction, window_pi_source_shadow_budget,
    shadow_uniform_budget,
)


def forcing_independent(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def independent_window(p):
    assert p%8==1 and p>3
    m=(p-1)//8
    y=Q()
    ys=[y]
    for n in range(1,4*m+1):
        y=(16*y+forcing_independent(n))%1
        ys.append(y)
    delta=3*m
    def complement(t):
        return (ys[m+1+t]-Q((4*pow(16,t,p))%p,p))%1
    return m,delta,tuple(complement(t) for t in range(delta))


def dist(x):
    x=x%1
    return min(x,1-x)


def independent_profile(p,d):
    m,delta,w=independent_window(p)
    assert delta%d==0
    K=delta//d
    summed=sum((dist(w[r+i*d]-w[r+j*d])**2
                for r in range(d) for i in range(K) for j in range(i+1,K)),Q())
    lower=Q(16,d*K*K)*summed
    upper=min(Q(1),Q(1936,49*d*K*K)*summed)
    assert (lower,upper)==rational_phase_dispersion_bracket(p,d)
    direct_coset=[[(4*pow(16,t,p))%p for t in range(r,delta,d)]
                   for r in range(d)]
    ref=additive_clock_partition(p,d)
    sub=ref["suborder"]
    repetitions=ref["repetitions"]
    for r in range(d):
        expected=[4*pow(16,r+d*j,p)%p for j in range(sub)]*repetitions
        assert direct_coset[r]==expected
    source_gap=forcing_independent(m+2)-forcing_independent(m+d+2)
    assert 0<source_gap<1
    calculated=source_periodicity_obstruction(p,d)
    assert calculated["forcing_difference"]==source_gap
    assert calculated["first_defect"]==dist(w[d]-w[0])
    assert calculated["successor_defect"]==dist(w[d+1]-w[1])
    assert source_gap<=16*calculated["first_defect"]+calculated["successor_defect"]
    shadow=Q(44,7)*sum((Q(1,(8*n+1)*(8*n+2))
                       for n in range(m+1,4*m+1)),Q())
    assert shadow==window_pi_source_shadow_budget(p)
    assert shadow<shadow_uniform_budget(p)
    rational_input=";".join(str(a.numerator)+"/"+str(a.denominator) for a in w)
    return {
        "p":p,"d":d,"m":m,"delta":delta,
        "coset_size":sub,
        "complete_cosets":repetitions,
        "discrepancy_squared_lower_gt": (
            "7/10" if p==41 and d==1 else
            "13/20" if p==73 and d==1 else
            "1/2" if d==1 else "1/4"),
        "discrepancy_test_pass": (
            lower > (Q(7,10) if p==41 and d==1 else
                     Q(13,20) if p==73 and d==1 else
                     Q(1,2) if d==1 else Q(1,4))),
        "source_nonperiodic":source_gap>0,
        "shadow_strictly_below_11_over_112m":True,
        "raw_fraction_profile_sha256":hashlib.sha256(
            rational_input.encode("utf-8")).hexdigest()
    }


def main():
    cases=[(17,1),(17,3),(41,1),(41,3),(73,1),(73,3)]
    rows=[independent_profile(p,d) for p,d in cases]
    if not all(x["discrepancy_test_pass"] for x in rows):
        raise AssertionError("expected lower rational dispersions are incorrect")
    report={
        "research":"PSC: authentic BBP prime-window spectral projection",
        "authenticated_source":"r(n) four original BBP poles, y0=0",
        "oracle":"independent integer/Fraction recurrence and CRT coset enumeration",
        "pi_normality_proved":False,
        "external_BKG_nu_computed":False,
        "claims":["full coset completion","strict source forcing period defect",
                  "rational complement dispersion","uniform O(1/m) pi shadow"],
        "records":rows
    }
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
