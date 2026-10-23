"""Independent integer-polynomial cyclotomic audit of signed unit orbit moments.

This does not import the production Ramanujan or circle-cosine evaluator.
It checks equality inside Q[X]/Phi_q(X), not floating cosine approximations.
"""
from __future__ import annotations

import json


def polynomial_quotient(dividend: list[int], monic: list[int]) -> tuple[list[int],list[int]]:
    a=dividend[:]
    b=monic[:]
    while len(a)>1 and a[-1]==0:a.pop()
    while len(b)>1 and b[-1]==0:b.pop()
    if not b or b[-1]!=1:
        raise ValueError("monic divisor required")
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b):
        d=len(a)-len(b)
        v=a[-1]
        q[d]=v
        for j,w in enumerate(b):
            a[d+j]-=v*w
        while len(a)>1 and a[-1]==0:a.pop()
    return q,a


def cyclotomic(q: int) -> list[int]:
    if q<1:raise ValueError("q>=1")
    built={}
    for n in range(1,q+1):
        poly=[-1]+[0]*(n-1)+[1]
        for d in range(1,n):
            if n%d==0:
                poly,rem=polynomial_quotient(poly,built[d])
                if any(rem):raise ArithmeticError("cyclotomic division not exact")
        built[n]=poly
    return built[q]


def orbit_for(base:int,q:int)->tuple[int,...]:
    from math import gcd
    if gcd(base,q)!=1:raise ValueError("unit required")
    vals=[];x=1
    while x not in vals:
        vals.append(x); x=x*base%q
    if x!=1:raise ArithmeticError("not a cycle")
    return tuple(vals)


def validate_single(q:int,base:int,h:int,expected_num:int,expected_den:int)->bool:
    unit=orbit_for(base,q)
    numerator=[0]*q
    for r in unit:
        numerator[(h*r)%q]+=expected_den
        numerator[(-h*r)%q]+=expected_den
    numerator[0]-=2*len(unit)*expected_num
    _,rem=polynomial_quotient(numerator,cyclotomic(q))
    return all(v==0 for v in rem)


def run_oracle()->dict:
    from fractions import Fraction
    # Independently hard-code Ramanujan values via direct divisor-Mobius sieve:
    def mobius_direct(n):
        if n==1:return 1
        value=1
        for p in range(2,n+1):
            if n%p==0 and all(p%d for d in range(2,int(p**0.5)+1)):
                if n%(p*p)==0:return 0
                value=-value
        return value
    from math import gcd
    verified=0
    for q in (3,5,7,9,11,25):
        units=[j for j in range(1,q) if gcd(q,j)==1]
        orbit=orbit_for(2,q)
        if set(orbit)|{-j%q for j in orbit}!=set(units):
            raise AssertionError("unexpected incomplete source")
        for h in range(1,2*q+2):
            g=gcd(q,h)
            ram=sum(d*mobius_direct(q//d) for d in range(1,g+1) if g%d==0)
            predicted=Fraction(ram,len(units))
            if not validate_single(q,2,h,predicted.numerator,predicted.denominator):
                raise AssertionError((q,h,ram,predicted))
            verified+=1
    # Orientation is load-bearing: the UNSYMMETRIZED 7th roots from 1,2,4
    # are NOT equal to the real average -1/6 in Q[X]/Phi_7(X).
    q=7
    one_sided=[0]*q
    for a in orbit_for(2,q):one_sided[a]+=6
    one_sided[0]+=3   # 3*(+1/6), wrongly asserting sum=-1/2
    _,rem=polynomial_quotient(one_sided,cyclotomic(q))
    if not any(rem):raise AssertionError("one-sided phase fake passed")
    return {"exact_cyclotomic_moment_checks":verified,
            "one_sided_phase_mutant_rejected":True,
            "interpretation":"finite algebra oracle, no infinite normality claim"}


if __name__=="__main__":
    print(json.dumps(run_oracle(),sort_keys=True,indent=2))
