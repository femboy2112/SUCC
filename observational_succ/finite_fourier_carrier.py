"""Exact rational cyclotomic finite Fourier clock for SUCC/FUCC.

Implements Q[X]/Phi_N(X) via elementary monic polynomial division, with
no floating roots, no SymPy dependency and no assumption that a multiplier
m is prime merely because the shift-dilation equation holds. This is a
finite algebraic calibration, NOT the Fourier theory of all adeles.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import gcd
from typing import Sequence

from .diagonal_adele_zeta import DiagonalSourceError, prime, rational


def _trim(x:tuple[F,...])->tuple[F,...]:
    x=list(x)
    while len(x)>1 and x[-1]==0:
        x.pop()
    return tuple(x)


def _poly_mul(a:tuple[F,...],b:tuple[F,...])->tuple[F,...]:
    t=[F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            t[i+j]+=u*v
    return _trim(tuple(t))


def _poly_divmod(f:tuple[F,...],g:tuple[F,...])->tuple[tuple[F,...],tuple[F,...]]:
    a=list(_trim(f));g=_trim(g)
    if not g or g== (F(0),):
        raise DiagonalSourceError("Divisor must be nonzero")
    if len(a)<len(g):return (F(0),),tuple(a)
    q=[F(0)]*(len(a)-len(g)+1)
    while len(a)>=len(g) and any(a):
        shift=len(a)-len(g)
        c=a[-1]/g[-1]
        q[shift]=c
        for j,z in enumerate(g):a[shift+j]-=c*z
        a=list(_trim(tuple(a)))
    return _trim(tuple(q)),_trim(tuple(a))


@lru_cache(maxsize=128)
def cyclotomic_polynomial(n:int)->tuple[F,...]:
    """Exact Phi_n constant-first. Validated via x^n-1 product identity."""
    if type(n) is not int or not 1<=n<=200:
        raise DiagonalSourceError("Finite cyclotomic N must lie 1..200")
    poly=tuple([F(-1)]+[F(0)]*(n-1)+[F(1)])
    for d in range(1,n):
        if n%d==0:
            q,r=_poly_divmod(poly,cyclotomic_polynomial(d))
            if r!=(F(0),):raise AssertionError("Cyclotomic division not exact")
            poly=q
    return poly


@dataclass(frozen=True)
class CyclotomicElement:
    modulus:int
    polynomial:tuple[F,...]

    def __post_init__(self):
        phi=cyclotomic_polynomial(self.modulus)
        p=tuple(rational(x) for x in self.polynomial)
        _,rem=_poly_divmod(p,phi)
        object.__setattr__(self,"polynomial",rem)

    def __add__(self,other:"CyclotomicElement") ->"CyclotomicElement":
        if self.modulus!=other.modulus:raise DiagonalSourceError("Different Fourier roots")
        length=max(len(self.polynomial),len(other.polynomial))
        return CyclotomicElement(self.modulus,tuple((self.polynomial[i] if i<len(self.polynomial) else 0)+
                        (other.polynomial[i] if i<len(other.polynomial) else 0) for i in range(length)))

    def __mul__(self,other:"CyclotomicElement") ->"CyclotomicElement":
        if self.modulus!=other.modulus:raise DiagonalSourceError("Different Fourier roots")
        return CyclotomicElement(self.modulus,_poly_mul(self.polynomial,other.polynomial))

    def scale(self,x:int|F)->"CyclotomicElement":
        return CyclotomicElement(self.modulus,tuple(rational(x)*v for v in self.polynomial))

    @staticmethod
    def scalar(n:int,x:int|F)->"CyclotomicElement":
        return CyclotomicElement(n,(rational(x),))

    @staticmethod
    def root(n:int,e:int)->"CyclotomicElement":
        if type(e) is not int:raise DiagonalSourceError("Integral character exponent required")
        v=[F(0)]*((e%n)+1)
        v[-1]=F(1)
        return CyclotomicElement(n,tuple(v))


def exact_dft(values:Sequence[int|F])->tuple[CyclotomicElement,...]:
    n=len(values)
    if n<2 or n>100:raise DiagonalSourceError("Finite clock length 2..100")
    xs=tuple(rational(v) for v in values)
    result=[]
    for k in range(n):
        total=CyclotomicElement.scalar(n,0)
        for x,value in enumerate(xs):
            if value:
                total=total+CyclotomicElement.root(n,k*x).scale(value)
        result.append(total)
    return tuple(result)


def exact_idft(spectrum:Sequence[CyclotomicElement])->tuple[CyclotomicElement,...]:
    n=len(spectrum)
    if n<2 or any(z.modulus!=n for z in spectrum):
        raise DiagonalSourceError("Spectrum must inhabit ONE finite Fourier clock")
    result=[]
    for y in range(n):
        total=CyclotomicElement.scalar(n,0)
        for k,val in enumerate(spectrum):
            total=total+val*CyclotomicElement.root(n,-k*y)
        result.append(total.scale(F(1,n)))
    return tuple(result)


def shift_function(values:Sequence[int|F],d:int)->tuple[F,...]:
    n=len(values)
    if n<2 or type(d) is not int:raise DiagonalSourceError("Invalid shift clock")
    return tuple(rational(values[(x-d)%n]) for x in range(n))


def dilate_function(values:Sequence[int|F],m:int,*,require_prime:bool=False)->tuple[F,...]:
    n=len(values)
    if n<2 or type(m) is not int or gcd(m,n)!=1:
        raise DiagonalSourceError("Finite Fourier FUCC requires clock-unit multiplier")
    if require_prime and not prime(m):
        raise DiagonalSourceError("Composite FUCC is not a genuine Euler place")
    inv=pow(m,-1,n)
    return tuple(rational(values[(inv*x)%n]) for x in range(n))


def fourier_covariance_receipt(values:Sequence[int|F],d:int,m:int,*,require_prime:bool=False)->dict:
    n=len(values)
    if type(d) is not int:raise DiagonalSourceError("Integral step required")
    f=exact_dft(values)
    shifted=exact_dft(shift_function(values,d))
    for k in range(n):
        if shifted[k]!=CyclotomicElement.root(n,k*d)*f[k]:
            raise AssertionError("Fourier SUCC covariance violation")
    dilated=exact_dft(dilate_function(values,m,require_prime=require_prime))
    for k in range(n):
        if dilated[k]!=f[(m*k)%n]:
            raise AssertionError("Fourier FUCC dual-map violation")
    if exact_idft(f)!=tuple(CyclotomicElement.scalar(n,v) for v in values):
        raise AssertionError("Exact Fourier inversion failed")
    return {"modulus":n,"step":d,"multiplier":m,
            "exact_inverse":True,"shift_fourier_square":True,
            "fucc_dual_frequency_square":True,"prime_source_attested":require_prime and prime(m),
            "physical_carrier_authenticated":False}
