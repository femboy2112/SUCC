"""Exact signed folding of original-BBP positive lag shear."""
from __future__ import annotations
from fractions import Fraction as F
from alias_valve import force, shear


def double_shear(A:int)->F:
    if not isinstance(A,int) or A<2: raise ValueError("A>=2")
    return sum((shear(n,d) for d in range(1,A)
                for n in range(A,2*A-d-1)),F(0))


def folded_shear(A:int)->F:
    if not isinstance(A,int) or A<2: raise ValueError("A>=2")
    return sum(((3*A-2*k)*force(k) for k in range(A+1,2*A)),F(0))


def refined_flux_cap(A:int,q:int)->F:
    if A<2 or q<2: raise ValueError("A,q>=2")
    # normalized |leak - lateral| upper; exact source-total shear
    return F(q,A*A)*(A-1+q*folded_shear(A))
