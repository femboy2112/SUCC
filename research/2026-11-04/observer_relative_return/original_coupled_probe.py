#!/usr/bin/env python3
"""Original-coupled BBP observer-clock finite diagnostics, stdlib only.

Authentic four-pole source; literal U0=Y0=Z0=0; exact Fraction carries.
Finite signed sums are numerical probes, NOT π normality evidence.
Run: python research/2026-11-04/observer_relative_return/original_coupled_probe.py --verify
"""
from __future__ import annotations
import argparse
import cmath
from fractions import Fraction as Q
import json
from math import floor,log,pi

P=(Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))
ANG=(Q(2),Q(2),Q(1),Q(0),Q(-1,2),Q(-1,2),Q(-1,4),Q(0))
RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))

def source(n,w):
    return sum((c/Q(8*(n-1)+j) for j,c in enumerate(w,1)),Q(0))

def build_states(n):
    u=y=z=Q(0)
    U=[u];Y=[y];Z=[z]
    assert tuple(a+r for a,r in zip(ANG,RAD))==P
    for t in range(1,n+1):
        u=(16*u+source(t,P))%1
        y=(16*y+source(t,ANG))%1
        z=16*z+source(t,RAD)
        assert (y+z)%1==u, ("source/carry mismatch",t)
        U.append(u);Y.append(y);Z.append(z)
    return U,Y,Z

def critical_h(A,h):
    if not isinstance(A,int) or A<16 or not isinstance(h,int) or not h:
        raise ValueError("A>=16 and h!=0 required")
    j=floor(log(A*A*log(A)/abs(h),16))
    if j<0:
        raise ValueError("small A/large h outside defined critical schedule")
    return abs(h)*16**j

def max_subinterval(phases):
    prefix=[0j]
    for z in phases:
        prefix.append(prefix[-1]+z)
    return max(abs(prefix[j]-prefix[i])
        for i in range(len(phases)) for j in range(i+1,len(phases)+1))

def probe(A,h=1,lags=(-2,-1,0,1,2)):
    H=critical_h(A,h)
    U,Y,Z=build_states(2*A+max(max(lags),0)+2)
    entries=[]
    for ell in lags:
        values=[]
        for n in range(A,2*A):
            # Exact lift before the final float conversion, preserving carries.
            phase=(H*(U[n]+Z[n+ell]-Z[n]))%1
            values.append(cmath.exp(2j*pi*float(phase)))
        total=sum(values,0j)/A
        maxabs=max_subinterval(values)/A
        entries.append({"lag":ell,"mean_magnitude":round(abs(total),9),
                        "max_subinterval_mean":round(maxabs,9)})
    return {"A":A,"h":h,"H":H,"q":H/(A*A),"results":entries,
            "method":"exact Fraction BBP orbit and radial lag; float complex exponential"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--verify",action="store_true")
    args=ap.parse_args()
    rows=[probe(A) for A in (128,256,512)]
    if args.verify:
        target=next(e["max_subinterval_mean"] for e in rows[-1]["results"] if e["lag"]==0)
        assert abs(4*target-0.238707419)<0.00002, target
        # A wrong claim 'a lag invariably reduces the max' fails at A=512.
        lags={e["lag"]:e for e in rows[-1]["results"]}
        assert lags[2]["max_subinterval_mean"]>lags[0]["max_subinterval_mean"]
        assert lags[-2]["max_subinterval_mean"]<lags[0]["max_subinterval_mean"]
        print("ORIGINAL_COUPLED_OBSERVER_FINITE_REPLAY_PASS")
    print(json.dumps(rows,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
