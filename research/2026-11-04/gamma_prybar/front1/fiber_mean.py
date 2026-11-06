"""Exhaustive small-epoch check of the counting measure in the silent fiber."""
from fractions import Fraction as F
from math import gcd, lcm, prod
import json
from cofactor_probe import four_poles, primes_up_to


def mean_probe(A,q):
    states,Q,x = [],1,F(0)
    for n in range(1,2*A):
        r = four_poles(n)
        Q = lcm(Q,r.denominator)
        x=16*x+r
        if n>=A:
            states.append(x)
    S = [p for p in primes_up_to(8*A-11) if p%8==5 and p>4*A]
    H=prod(S)
    nums = [int(x*Q)%Q for x in states]
    shifts = [(Q//H)*pow(16,n,H) for n in range(A,2*A)]
    def kernel_num(v):
        u=v%Q
        return q*max(0,Q-q*min(u,Q-u))
    def score(v):
        return F(sum(kernel_num(x-y) for x in v for y in v),A*A*Q)
    all_sum=F(0)
    good=[]
    selected=score(nums)
    for b in range(H):
        v=[a+b*w for a,w in zip(nums,shifts)]
        s=score(v)
        assert s>=1
        all_sum+=s
        if gcd(v[0],H)==1:
            good.append(s)
            if b==0:
                assert s==selected
    assert len(good)==prod(p-1 for p in S)
    grid=F(0)
    for i in range(A):
        for j in range(A):
            order=H//gcd(H,pow(16,abs(i-j),H)-1)
            grid+=F(sum(kernel_num(nums[i]-nums[j]+k*(Q//order)) for k in range(order)),order)
    grid/=A*A*Q
    assert grid==all_sum/H
    return {"A":A,"q":q,"H":H,"admissible":len(good),"mean":str(grid),
            "conditional_mean":str(sum(good)/len(good)),"selected":str(selected),
            "min":str(min(good)),"max":str(max(good))}


if __name__=="__main__":
    print(json.dumps([mean_probe(A,4) for A in (5,7)],indent=2))
