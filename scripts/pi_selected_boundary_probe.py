"""Source-typed finite selected-boundary regression (stdlib, research only).

Paper proofs: research/2026-10-27/PI_SELECTED_BOUNDARY_CRT_FRONTIER.md.
Not an all-N normality verifier; no production source import/replacement.
"""
from fractions import Fraction as Q
from math import gcd, pi, cos, sin

def four_pole(n):
    if n < 1: raise ValueError("n>=1")
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)

def cancelled(n):
    return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def states_and_tails(M=100):
    r=[Q(0)]+[four_pole(n) for n in range(1,M+1)]
    U=[Q(0)]
    for n in range(1,M+1): U.append(16*U[-1]+r[n])
    T=[Q(0)]*(M+1)
    for n in range(M-1,-1,-1): T[n]=(r[n+1]+T[n+1])/16
    return r,U,T,16*T[0]

def modr(x,m):
    if gcd(x.denominator,m)!=1: raise ValueError("nonunit")
    return x.numerator*pow(x.denominator,-1,m)%m

def A(n): return 120*n*n-89*n+16

def hex_prefix(j,q,k):
    r=j
    out=[]
    for _ in range(k):
        d,r=divmod(16*r,q);out.append(d)
    return out

def staged_digits(q=17,K=13):
    if q<3 or gcd(q,16)!=1: raise ValueError("q must be odd")
    return [d for k in range(1,K+1) for j in range(q) for d in hex_prefix(j,q,k)]

def sample_mode(ds,h):
    # Illustrative finite stage only.
    xs=[0.]*(len(ds)+1)
    for n in range(len(ds)-1,-1,-1): xs[n]=(ds[n]+xs[n+1])/16
    return sum(complex(cos(2*pi*h*xs[n]),sin(2*pi*h*xs[n])) for n in range(len(ds)))/len(ds)

def check():
    r,U,T,prefix=states_and_tails()
    assert all(r[n]==cancelled(n) for n in range(1,101))
    assert all(U[n]+T[n]==(Q(1,16) if n==0 else Q(16**(n-1)))*prefix for n in range(101))
    assert all(T[n]>0 and T[n]<Q(1,16) for n in range(1,100))
    assert len({(modr(U[n],16),A(n)%3) for n in range(48)})==48
    assert len({(modr(U[n],16),A(n)%3) for n in range(24,72)})==48
    assert all(sorted(pow(16,t,17)*j%17 for j in range(17))==list(range(17)) for t in range(30))
    ds=staged_digits()
    vals={h:abs(sample_mode(ds,h)) for h in (1,2,3,5,8,16,17)}
    assert all(vals[h]<0.04 for h in (1,2,3,5,8,16)),vals
    assert vals[17]>0.9,vals
    # alpha=0: y=0, x=1-T; first hex digit always differs.
    assert all(int(16*((-T[n])%1))==15 for n in range(1,100))
    return vals

if __name__=="__main__": print("FINITE STDLIB CHECK PASS; q17 finite stages:",check())
