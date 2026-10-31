"""Universal multiplicative log-jet lift and original BBP four-pole instance.

Classical algebra. Adapted from independently reviewed sibling SUCC PR #416,
not claimed as original or as a selected normality proof.
"""
from fractions import Fraction
from math import isqrt

COEFF=(4,-2,-1,-1)
OFFSETS=(0,3,4,5)


def potential(a: int,coeff=COEFF) -> Fraction:
    assert a>=1
    result=Fraction(1)
    for d,c in zip(OFFSETS,coeff):
        if c>=0:
            result*=Fraction((a+d)**c)
        else:
            result/=Fraction((a+d)**(-c))
    return result


def logarithmic_source(a: int,coeff=COEFF)->Fraction:
    assert a>=1
    return sum((Fraction(c,a+d) for d,c in zip(OFFSETS,coeff)),Fraction(0))


def multiplicative_carrier(N: int, coeff=COEFF)->Fraction:
    """B_N(0) from B_0=1 and B_(n+1)=B_n^16 * V(a_(n+1))."""
    b=Fraction(1)
    for n in range(1,N+1):
        b=b**16*potential(8*n-7,coeff)
    return b


def logjet_selected(N:int, seed:Fraction=Fraction(0),coeff=COEFF)->Fraction:
    """Derivative log B_N at u=0; finite rational recurrence."""
    u=seed
    for n in range(1,N+1):
        u=16*u+logarithmic_source(8*n-7,coeff)
    return u


def source_product(N:int,coeff=COEFF)->Fraction:
    prod=Fraction(1)
    for n in range(1,N+1):
        prod*=potential(8*n-7,coeff)
    return prod


def source_product_abel(N:int,coeff=COEFF)->Fraction:
    """B_N=P_N product_{j<N}P_j^(15*16^(N-j-1))."""
    q=source_product(N,coeff)
    for j in range(1,N):
        q*=source_product(j,coeff)**(15*16**(N-j-1))
    return q


def v_p_integer(n:int,p:int)->int:
    assert p>=2 and n>0
    v=0
    while n%p==0:
        v+=1
        n//=p
    return v


def v_p_fraction(q:Fraction,p:int)->int:
    return v_p_integer(q.numerator,p)-v_p_integer(q.denominator,p)


def prime_factor_exponents(n:int)->dict[int,int]:
    assert n>=1
    d={};p=2
    while p*p<=n:
        while n%p==0:
            n//=p;d[p]=d.get(p,0)+1
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d


def carrier_valuation_vector(N:int,coeff=COEFF)->dict[int,int]:
    """All prime-place valuations of B_N(0), without forming huge rational."""
    v={}
    for n in range(1,N+1):
        v={p:16*x for p,x in v.items()}
        a=8*n-7
        for d,c in zip(OFFSETS,coeff):
            for p,k in prime_factor_exponents(a+d).items():
                v[p]=v.get(p,0)+c*k
        v={p:x for p,x in v.items() if x}
    return v


def predicted_v2(N:int,mutant:bool=False)->int:
    return -(2 if mutant else 1)*(16**N-1)//3


def initial_seed_first_jet_difference(N:int,seed:Fraction)->Fraction:
    """Pointwise B_N(0) unchanged; initial infinitesimal seed changes jet."""
    return logjet_selected(N,seed)-logjet_selected(N)
