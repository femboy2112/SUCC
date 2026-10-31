"""Finite exact hexadecimal occupancy certificates for the REAL selected pi orbit.

Uses rational U_n(0) and proven 0<T_n<1/(8n+1)^2. Finite N ONLY:
these counts are not a normality proof or all-horizon occupancy bound.
"""
from fractions import Fraction
from prime_stroboscope import source_term


def frac(x):
    return x - x.numerator//x.denominator


def certified_bin(u:Fraction,n:int,bins:int=16):
    if n<1 or bins<1:raise ValueError('positive n and bins')
    x=frac(u)
    eps=Fraction(1,(8*n+1)**2)
    lower=(bins*x).numerator//(bins*x).denominator
    y=bins*(x+eps)
    upper=y.numerator//y.denominator
    return (lower if lower==upper else None),lower,upper


def certified_counts(N:int,bins:int=16):
    if N<1:raise ValueError('positive horizon required')
    lower=[0]*bins
    upper=[0]*bins
    ambiguous=[]
    u=Fraction(0)
    for n in range(1,N+1):
        u=16*u+source_term(n)
        b,first,last=certified_bin(u,n,bins)
        if b is not None:
            lower[b]+=1
            upper[b]+=1
        else:
            touched={k%bins for k in range(first,last+1)}
            for val in touched:upper[val]+=1
            ambiguous.append(dict(n=n,grid_start=first%bins,grid_end=last%bins,possible_bins=sorted(touched)))
    return dict(horizon=N,bins=bins,lower=lower,upper=upper,ambiguous=ambiguous)


if __name__=='__main__':
    import json
    print(json.dumps(certified_counts(256,16),indent=2))
