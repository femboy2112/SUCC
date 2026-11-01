"""Independent finite-source checks (different combinatorics from unit_seam.py).

Algorithmic independence is not an independent mathematical witness.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb


def source_combined(n: int) -> F:
    x=F(n)
    return (120*x*x-89*x+16)/((2*x-1)*(4*x-1)*(8*x-7)*(8*x-3))


def finite_differences_at_one(k:int)->F:
    table=[source_combined(i+1) for i in range(k+1)]
    for _ in range(k):table=[table[j]-table[j+1] for j in range(len(table)-1)]
    return table[0]


def path_count(n:int,k:int)->int:
    """Independent path count by recursion on weighted radix16/pascal grid."""
    if n<=0 or k>=n or k<0:return 0
    row=[1]
    for i in range(1,n):
        row=[16*(row[j] if j<len(row) else 0)+comb(i,j) for j in range(i+1)]
    return row[k]


def source_reconstruct(n:int)->F:
    return sum(((-1)**k*path_count(n,k)*finite_differences_at_one(k)
                for k in range(n)),F())


def finite_shift_dilation_source(n:int,m:int)->F:
    """f(x)=r(x+1), compute V_m(S^m f)(n) directly from ORIGINAL 4 poles."""
    return source_combined(m*n+m+1)


def moment_quadrature_discrete(weights:list[F],nodes:list[F],k:int)->F:
    return sum((w*(1-node)**k for w,node in zip(weights,nodes)),F())


def finite_difference_signed_weights(n:int)->tuple[F,...]:
    return tuple(F((-1)**(n-j)*comb(n,j),2**n) for j in range(n+1))


def binomial_shift_moment(weights:list[F],nodes:list[F],m:int,k:int)->F:
    return sum((w*node**m*(1-node**m)**k for w,node in zip(weights,nodes)),F())
