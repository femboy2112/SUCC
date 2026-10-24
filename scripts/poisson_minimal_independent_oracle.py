"""Method-distinct exact cyclotomic/Fourier audit of Poisson minimum geometry.

Uses integer cyclotomic polynomial reduction and Q[i] powers, not Taylor/Wallis
or the implementation's source arithmetic. A successful finite check is NOT a
pi-normality theorem or an independent academic referee.
"""
from __future__ import annotations

import json
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.poisson_circle_minimal import (
    exact_point, rational_greedy_circle, exact_energy,
    ternary_periodic_counterfeit_energy,
)


def complex_power(z, h):
    # This independent implementation uses straight repeated multiplication,
    # not the production fast square-and-multiply or chord-Chebyshev method.
    ar=Q(1); ai=Q(0)
    for _ in range(h):
        ar,ai=ar*z[0]-ai*z[1],ar*z[1]+ai*z[0]
    return ar,ai


def finite_fourier_lower(points, H):
    N=len(points)
    total=Q(1)
    for h in range(1,H+1):
        ar=ai=Q(0)
        for z in points:
            x,y=complex_power(z,h)
            ar+=x;ai+=y
        total+=Q(2,2**h)*(ar**2+ai**2)/(N**2)
    return total


def cyclo_reduce_3power(q, frequency):
    s=q//3
    coeff=[0]*q
    for a in range(q):
        if gcd(a,q)==1:
            coeff[(frequency*a)%q]+=1
    # Phi_(3^r)(X)=1+X^s+X^(2s) for q=3s.
    for k in range(q-1,2*s-1,-1):
        c=coeff[k]
        if c:
            coeff[k]=0
            coeff[k-2*s]-=c
            coeff[k-s]-=c
    return tuple(coeff[:2*s])


def independent_ternary_character(q,h):
    s=q//3
    return (2*s if h%q==0 else -s if h%s==0 else 0)


def audit():
    complex_cases=0
    for num,den in ((0,1),(1,1),(-1,1),(1,2),(2,3),(-3,4)):
        z=exact_point(num,den)
        samples=tuple((z,)*1)+(exact_point(0),exact_point(-1),exact_point(1))
        for n in range(1,5):
            for H in (2,5,10):
                lo=finite_fourier_lower(samples[:n],H)
                actual=exact_energy(samples[:n])
                assert lo<=actual<=lo+Q(2,2**H)
                complex_cases+=1
    cyclotomic_cases=0
    for depth in (1,2,3,4):
        q=3**depth
        for h in range(0,2*q+1):
            coeff=cyclo_reduce_3power(q,h)
            expected=independent_ternary_character(q,h)
            assert coeff==(expected,)+(0,)*(len(coeff)-1)
            cyclotomic_cases+=1
        assert ternary_periodic_counterfeit_energy(depth)>1
    return {"independent_exact_fourier_enclosures":complex_cases,
            "independent_cyclotomic_integral_character_identities":cyclotomic_cases,
            "status":"finite_exact_probes_only_not_pi_normality"}


if __name__=="__main__":
    print(json.dumps(audit(),sort_keys=True,indent=2))
