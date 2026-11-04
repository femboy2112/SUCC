"""Independent exact combined-source / pole occurrence / CRT oracle.

Uses a different rational construction from prime_phase.state(), and checks
predicted appearances directly against the raw four pole denominators.
"""
from fractions import Fraction
from math import gcd


def r_combined(j):
    return Fraction(120*j*j-89*j+16,(2*j-1)*(4*j-1)*(8*j-7)*(8*j-3))


def u_convolution(N):
    return sum((16**(N-j)*r_combined(j) for j in range(1,N+1)),Fraction(0))


def occurrences(N,p):
    """Raw source-pole multiples of p for j<=N; (j,term,quotient)."""
    return [(j,a,(8*j-a)//p)
            for j in range(1,N+1) for a in (7,4,3,2)
            if (8*j-a)%p==0]


def verify_horizon(N,p):
    assert 2*N<p<8*N and p%4==1 and p>5
    expected=(p+7)//8 if p%8==1 else (p+3)//8
    assert occurrences(N,p)==[(expected,7 if p%8==1 else 3,1)]
    u=u_convolution(N)
    assert u.denominator%p==0 and (u.denominator//p)%p!=0
    pu=p*u
    assert gcd(pu.denominator,p)==1
    coeff=4 if p%8==1 else -1
    got=pu.numerator*pow(pu.denominator,-1,p)%p
    assert got==coeff*pow(16,N-expected,p)%p
    return {"p":p,"n":expected,"pole":7 if coeff==4 else 3,"residue":got}


def ramanujan_trace_sum(p,a):
    """Exact exponent counts of a nontrivial primitive-p Galois orbit."""
    if a%p==0:raise ValueError("a must be nonzero mod p")
    counts=[0]*p
    for k in range(1,p):counts[a*k%p]+=1
    assert counts==[0]+[1]*(p-1)
    # Each nonzero residue once; 1 + zeta+...+zeta^(p-1)=0.
    return -1


def positive_integer_poles_for_n(N):
    """Independent slow prime enumeration over only the necessary interval."""
    result=[]
    for p in range(2*N+1,8*N):
        if p<=5 or p%4!=1:continue
        if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
        result.append(p)
    return result
