"""Exact Fraction seed-ensemble pair/triple carry moments from original BBP source.
No pi digits; NOT selected zero-seed time averages.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations

@lru_cache(None)
def r(n):return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def force(n,m):return sum((16**(m-j)*r(n+j) for j in range(1,m+1)),F())

def delay(n,d):return sum((16**(d-j)*r(n+j) for j in range(1,d+1)),F())

def floor_f(x):return x.numerator//x.denominator

def window(y,a,beta,R):
    z=(a*y+beta)%1
    return 1 if z>=1-R else 0

def integrate(n,m,delays):
    """Integrate product of centered carry windows for a uniform initial seed.

    Let y={16^m U_n(S)} uniform, then B U_(n+d)=16^d*y+B*S_d(n).
    Critical windows are step functions with exact rational endpoints.
    """
    B=16**m
    data=[]
    for d in delays:
        a=16**d; beta=(B*delay(n,d))%1
        R=force(n+d,m)
        assert 0<R<1,(n,m,d,R)
        data.append((a,beta,R))
    endpoints={F(0),F(1)}
    for a,beta,R in data:
        for k in range(-2,a+3):
            start=F(k+1,1)-R-beta
            stop=F(k+1,1)-beta
            for v in (start/a,stop/a):
                if 0<=v<=1:endpoints.add(v)
    points=sorted(endpoints)
    output=F(0)
    for l,rgt in zip(points,points[1:]):
        if rgt==l:continue
        mid=(l+rgt)/2
        term=F(1)
        for a,beta,R in data:
            term*=window(mid,a,beta,R)-R
        output+=(rgt-l)*term
    return output, data, len(points)

if __name__=='__main__':
    for n,m in ((13,2),(29,3),(61,3)):
        for lags in ((0,1),(0,2),(0,1,2)):
            v,data,nparts=integrate(n,m,lags)
            print('n',n,'m',m,'lags',lags,'moment',float(v),'exact digits',len(str(v.numerator)),len(str(v.denominator)), 'breakpoints',nparts)
            if lags==(0,1,2):
                print('widths:',[float(t[2]) for t in data])
