#!/usr/bin/env python3
"""Numerical (NOT proof-authoritative) independent integral check of the jets.

The paper proof of complete monotonicity is by an explicit positive density.
Requires optional mpmath; exact rational regression has no dependencies.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
import mpmath as mp

mp.mp.dps = 65

@lru_cache(None)
def src(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)

@lru_cache(None)
def finite(n):
    return sum((src(n+j)/16**j for j in range(1,n+2)),Q())

def rational_h(n,d):
    val=sum(((-1)**(d-j)*comb(d,j)*finite(n+j)
             for j in range(d+1)),Q())
    val*=(-1)**d
    return mp.mpf(val.numerator)/val.denominator

def honest_h(n,d):
    # Independent v=x^(1/8) change of variables avoids x^(-7/8).
    P=lambda v:4-2*v**3-v**4-v**5
    return mp.quad(lambda v:v**(8*n)*(1-v**8)**d*P(v)/(16-v**8),
                   [0,mp.mpf('0.1'),mp.mpf('0.5'),1])

def main():
    ratios=[]
    for n,d in [(0,0),(0,1),(1,0),(1,1),(1,5),(2,2),(3,8),
                (10,10),(20,20),(30,5)]:
        true=honest_h(n,d)
        shadow=rational_h(n,d)
        ratio=shadow/true
        assert ratio>=mp.mpf(19)/20
        assert ratio<=1
        ratios.append((n,d,mp.nstr(ratio,24)))
    for d in (1,2,4,8,16,32):
        exact=honest_h(1,d-1)
        # sum_n>=1 H_(n,d) equals moment with one n-index and order d-1
        upper=mp.beta(mp.mpf(9)/8,d)/30
        assert 0<exact<=upper
    print('INDEPENDENT_NUMERIC_MOMENT_ORACLE_PASS')
    for n,d,ratio in ratios:print(n,d,ratio)

if __name__=="__main__":
    main()
