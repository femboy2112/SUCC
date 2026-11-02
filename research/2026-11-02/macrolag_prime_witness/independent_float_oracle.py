#!/usr/bin/env python3
"""Independent four-pole Fraction source; floating trig DIAGNOSTIC only."""
from fractions import Fraction as F
from math import cos, sin, pi, isqrt, hypot
import json

def r(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def calc(primes,hs=(1,3,5,7)):
    top=max((p-1)//2 for p in primes)
    sels={p:(p+3)//8 for p in primes}
    sums={p:{h:0j for h in hs} for p in primes}
    U=F()
    for n in range(1,top+1):
        U=16*U+r(n)
        for p in primes:
            if sels[p] <=n<= (p-1)//2:
                for h in hs:
                    z=(h*U.numerator)%U.denominator
                    angle=2*pi*(z/U.denominator)
                    sums[p][h]+=complex(cos(angle),sin(angle))
    return {p:{h:abs(sums[p][h])/(((p-1)//2)-sels[p]+1) for h in hs} for p in primes}

if __name__=='__main__':
    out=calc([4013,4021,4093,10037,10061,10069])
    print(json.dumps(out,indent=2))
    with open('/mnt/data/succ_macrolag/independent_float_receipt.json','w') as f:json.dump(out,f,indent=2)
