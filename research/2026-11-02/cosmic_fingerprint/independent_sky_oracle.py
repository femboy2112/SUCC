#!/usr/bin/env python3
"""Independent FLOAT-ONLY direct causal-sky sampling on the genuine BBP source.

No Fourier coefficient algebra is used to calculate the grid observables.
Purpose: independently check phase-stepped reference and centered-template
intensity correlations against the exact formulas in PROOFS.md.
No numerical finite sample is a normality proof or a rigorous interval.
"""
from __future__ import annotations
from fractions import Fraction as F
from cmath import exp
from math import pi
import json


def four_pole(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def actual_orbit(M):
    u=F(0)
    out=[]
    for n in range(1,M+1):
        u=16*u+four_pole(n)
        out.append(u)
    return out


def shadow(n):
    # Exact source-derived finite rational tail, not a fitted numerical model.
    q=F(47,240)
    d=sum((four_pole(n+j)/16**j for j in range(1,n+2)),F(0))
    return 16**n*q-d


def phase(x):
    return exp(2j*pi*float(x%1))


def aperture_measure(z,base=16,start=1):
    M=len(z)
    assert M<=3
    Q=32768
    i0=i90=cross=sky1=sky2=0.0
    for j in range(Q):
        s=j/Q
        field=sum(z[n]*exp(2j*pi*base**(start+n)*s) for n in range(M))
        beacon=sum(exp(2j*pi*base**(start+n)*s) for n in range(M))
        az=abs(field)**2/M
        ar=abs(beacon)**2/M
        sky1+=az/Q
        sky2+=ar/Q
        cross+=(az-1)*(ar-1)/Q
        i0+=abs(field+beacon)**2/Q
        i90+=abs(field+1j*beacon)**2/Q
    S=sum(z)
    theo_cross=(abs(S)**2-M)/M**2
    out={"M":M,"Q":Q,"reference_overlap":(S.real,S.imag),
         "observed_backgrounds":(sky1,sky2),
         "cross_observed":cross,"cross_formula":theo_cross,
         "i0_observed":i0,"i0_formula":2*M+2*S.real,
         "i90_observed":i90,"i90_formula":2*M+2*S.imag}
    assert abs(sky1-1)<1e-10 and abs(sky2-1)<1e-10
    assert abs(cross-theo_cross)<1e-10
    assert abs(i0-out['i0_formula'])<1e-9
    assert abs(i90-out['i90_formula'])<1e-9
    return out


def prime_window(p,h=1):
    if p==257:
        first,last=33,128
    else:
        assert p%8==5
        k=(p-5)//8
        first,last=k+1,4*k+2
    actual=actual_orbit(last)
    z=[phase(h*actual[n-1]) for n in range(first,last+1)]
    w=[phase(h*shadow(n)) for n in range(first,last+1)]
    m=len(z)
    S=sum(z);R=sum(w)
    return {"prime":p,"h":h,"n0":first,"n1":last,"M":m,
            "original_mean_amplitude":abs(S)/m,
            "shadow_mean_amplitude":abs(R)/m,
            "original_reference_contrast":(abs(S)**2-m)/m**2,
            "shadow_reference_contrast":(abs(R)**2-m)/m**2,
            "relative_original_shadow_amplitude":abs(sum(a*b.conjugate() for a,b in zip(z,w)))/m}


def main():
    report={"method":"direct independently sampled complex field; FLOAT ONLY",
            "causal_sky":[aperture_measure([phase(x) for x in actual_orbit(3)]),
                          aperture_measure([phase(shadow(n)) for n in range(1,4)])],
            "original_exact_source_windows":[prime_window(257,1),prime_window(257,3)]}
    print(json.dumps(report,indent=2))
    print("INDEPENDENT_DIRECT_CAUSAL_SKY_FLOAT_ORACLE_PASS")

if __name__=='__main__':main()
