"""Separate pole-prefix and symbolic-integral calibration, no implementation import."""
from fractions import Fraction as Q
import json
import sympy as s


def prefix(n):
    return sum((Q(16**(n-k))*sum((Q(c,8*k-d)
        for c,d in ((4,7),(-2,4),(-1,3),(-1,2))),Q())
        for k in range(1,n+1)),Q())


def radius(q):
    num=q.numerator%q.denominator
    return Q(min(num,q.denominator-num),q.denominator)


def run():
    k=s.symbols('k',positive=True,integer=True)
    # Integrating each exponential term independently gives these resolvents.
    integral=2*(1/(8*k-7)-1/(8*k-4))+1/(8*k-7)-1/(8*k-3)+1/(8*k-7)-1/(8*k-2)
    combined=(120*k*k-89*k+16)/((2*k-1)*(4*k-1)*(8*k-7)*(8*k-3))
    assert s.cancel(integral-combined)==0
    # Multiplication by (1-exp(-8x)) shifts every resolvent by eight.
    diff=s.cancel(integral-integral.subs(k,k+1))
    assert s.cancel(diff-(combined-combined.subs(k,k+1)))==0
    rows=[]
    for a in (4,12,28,44,76):
        vals={n:prefix(n) for n in range(a,2*a+1)}
        for h in ((a*a+1)//2,3*a*a//4,a*a):
            total=Q()
            for i in vals:
                for j in vals:
                    if i<j: total+=8*radius(h*(vals[i]-vals[j]))**2
            lower=total/(a+1)
            target=Q(81*a,34694450)
            assert lower>=target
            rows.append({'A':a,'h':h,'deficit_lower':str(lower),'target':str(target)})
    return {'status':'PASS','symbolic_resolvent_checks':2,'direct_prefix_rows':rows,
            'scope':'exact finite independent implementation; same model lineage'}


if __name__=='__main__': print(json.dumps(run(),indent=2))
