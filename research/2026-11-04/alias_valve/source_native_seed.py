"""Exact BBP source conductor and source-native counterseed instruments.

Finite arithmetic only. No pi digits are used, no normality asserted.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import lcm


def source_force(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError('integer n>=1 required')
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def collapsed_force(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError('integer n>=1 required')
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def source_conductor(A: int) -> int:
    if type(A) is not int or A<1:
        raise ValueError('A>=1 required')
    B=1
    for n in range(1,A+1):
        B=lcm(B, source_force(n).denominator)
    if B%2!=1:
        raise AssertionError('original source conductor odd')
    return B


def bbp_prefix(M: int) -> F:
    if type(M) is not int or M<1:
        raise ValueError('M>=1 required')
    return sum((source_force(n)/16**n for n in range(1,M+1)), F(0))


def nearest_integer(z: F) -> int:
    z=F(z)
    return (2*z.numerator+z.denominator)//(2*z.denominator)


def source_native_seed(A: int) -> tuple[F,int,F]:
    """Use only the source denominator lattice available at epoch A."""
    if type(A) is not int or A<2:
        raise ValueError('A>=2 required')
    B=source_conductor(A)
    alpha=bbp_prefix(2*A)
    s=F(nearest_integer(-B*alpha), B)
    assert B%s.denominator==0
    assert abs(s+alpha)<=F(1,2*B)
    return s,B,alpha


def original_orbit(N:int,seed:F=F(0))->tuple[F,...]:
    if type(N) is not int or N<0:
        raise ValueError('N>=0 required')
    y=F(seed)
    result=[y%1]
    for n in range(1,N+1):
        y=16*y+source_force(n)
        result.append(y%1)
    return tuple(result)


def native_epoch(A:int)->dict:
    s,B,alpha=source_native_seed(A)
    M=2*A
    # Exact finite future-source residues, computed backwards.
    R=F(0); remainders={}
    for n in range(M-1,A-1,-1):
        R=(source_force(n+1)+R)/16
        remainders[n]=R
        assert F(0)<R<F(1,(8*n+1)*(8*n+2))
    e=s+alpha
    unwrapped=tuple(16**n*e-remainders[n] for n in range(A,M))
    actual=original_orbit(M-1,s)[A:M]
    assert tuple(x%1 for x in unwrapped)==actual
    width=max(unwrapped)-min(unwrapped)
    bound=F(16**(M-1),B)+F(1,64*A*A)
    assert width<bound
    return dict(A=A,M=M,B=B,seed=s,seed_den=s.denominator,
                alpha=alpha,alignment=abs(e),width=width,
                elementary_width_cap=bound,
                certified_early=B > 4*A*A*16**M,
                current_bits=B.bit_length(),
                seed_bits=s.denominator.bit_length(),
                phase_cloud=actual)


def circle_distance(z:F)->F:
    y=F(z)%1
    return min(y,1-y)


def tent(z:F,q:int)->F:
    if type(q) is not int or q<2: raise ValueError('q>=2')
    return max(F(0),1-q*circle_distance(z))


def energy(xs,q:int)->F:
    if not xs: raise ValueError('nonempty')
    N=len(xs)
    return F(q,N*N)*sum((tent(a-b,q) for a in xs for b in xs),F(0))


def finite_virtual_seed_field(K:int,n:int):
    """Exact uniform inverse-seed field vs one realized seed; no randomness."""
    if type(K) is not int or K<1 or type(n) is not int or n<0:
        raise ValueError('K>=1,n>=0')
    M=16**K
    base=original_orbit(n)[-1]
    cloud=tuple((base+F(j*16**n,M))%1 for j in range(M))
    return cloud
