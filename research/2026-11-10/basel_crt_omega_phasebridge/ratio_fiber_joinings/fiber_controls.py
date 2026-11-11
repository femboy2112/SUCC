"""Elementary false-positive / false-negative controls for the 3/2 fiber.
No normality inference is drawn from synthetic digits.
"""
from __future__ import annotations
from math import floor, log
import random


def f(n:int)->int:
    if n<2: raise ValueError('n>=2')
    return (3*n)//2


def parent(n:int):
    if n<2: return None
    if n%3==0: return 2*(n//3)
    if n%3==1 and n>=4: return 2*((n-1)//3)+1
    return None


def root(n:int)->int:
    while True:
        p=parent(n)
        if p is None: return n
        n=p


def coupled_digits(N:int,seed:int=2026,twist:int=0):
    """Finite prefix of iid-root-class construction (finite smoke, not a proof of normality)."""
    if N<=0: return []
    if twist not in (0,1): raise ValueError("twist must be 0 or 1")
    rng=random.Random(seed)
    a=[0]*(N+1)
    for n in range(1,N+1):
        pred=parent(n)
        a[n]=((a[pred]+(twist if pred%2==0 else 0))%16 if pred is not None
               else rng.randrange(16))
    return a


def block_counts(digits,k):
    """Counts of a base16 linear k-word in 1-indexed finite digits list."""
    d=digits
    out={}
    for s in range(1,len(d)-k+1):
        w=tuple(d[s:s+k])
        out[w]=out.get(w,0)+1
    return out


def periodic_K9(ell):
    return {0:0,1:6,2:3}[ell%3]


def period9_mean_components(J,h):
    """Exact cyclotomic decomposition: real and sqrt(3)-imag coeff for alpha=1/9.
    Output is (constant part, real third-root coefficient, imaginary coeff) as ints.
    If 3∤h and J has length multiple 3: (0,0,0).
    """
    from collections import Counter
    c=Counter((h*periodic_K9(ell)//3)%3 for ell in J)
    # 1 real=1; w^1/w^2 real=-1/2, imaginary = +/-sqrt(3)/2
    return (2*c[0]-c[1]-c[2],c[1]-c[2])


def coupled_digits_null_twist(N:int,seed:int=2026):
    """Finite fair-independent edge-twist control; never a normality proof."""
    if N<=0: return []
    roots=random.Random(seed)
    twists=random.Random(seed+101)
    a=[0]*(N+1)
    for n in range(1,N+1):
        pred=parent(n)
        if pred is None:
            a[n]=roots.randrange(16)
        else:
            delta=twists.randrange(2) if pred%2==0 else 0
            a[n]=(a[pred]+delta)%16
    return a
