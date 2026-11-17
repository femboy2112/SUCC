"""Exact source-typed observer sections and compensation in PCE and BBP.

No analytic value of pi is used to compute the zero-seeded rational BBP source.
Only finite Fraction operations and provable source laws are implemented.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import isqrt
from typing import Iterable

Z_NEG1 = Fraction(-1, 12)


def _nat(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise ValueError(f"expected integer >= {minimum}")
    return n


def forcing(n: int) -> Fraction:
    _nat(n, 1)
    return (Fraction(4, 8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def orbit(n: int, seed: Fraction = Fraction(0)) -> Fraction:
    _nat(n)
    a=Fraction(seed)
    for j in range(1,n+1):
        a=16*a+forcing(j)
    return a


def floorq(x: Fraction) -> int:
    return x.numerator//x.denominator


def ceilq(x: Fraction) -> int:
    return -floorq(-x)


def state(n: int) -> tuple[int, Fraction]:
    x=orbit(n)
    c=floorq(x)
    return c,x-c


def source_lift(n:int, carry:int) -> tuple[Fraction,Fraction]:
    """(reconstructed full state, required seed), valid for n>=1.

    Only carry=authentic carry has the literal zero seed. Every other carry
    represents the same forcing under an explicitly changed rational seed.
    """
    _nat(n,1)
    if type(carry) is not int:
        raise ValueError("integer carry required")
    c0,u=state(n)
    return Fraction(carry)+u, Fraction(carry-c0,16**n)


def forced_shift(n:int,h:int) -> Fraction:
    _nat(n);_nat(h)
    return sum((16**(h-j)*forcing(n+j) for j in range(1,h+1)),Fraction())


def observed_force(n:int) -> int:
    """True source-selected C_(n+1)-16 C_n for n>=1."""
    _nat(n,1)
    c,u=state(n)
    return floorq(16*u+forcing(n+1))


def compensation(n:int,h:int=1) -> tuple[Fraction,Fraction]:
    """(coarse integer response, hidden fractional response), sum exactly 0."""
    _nat(n,1);_nat(h,1)
    c,u=state(n)
    d,w=state(n+h)
    coarse=Fraction(d-16**h*c)
    hidden=w-16**h*u-forced_shift(n,h)
    return coarse,hidden


def digit_carry(n:int) -> tuple[int,int,int]:
    """j_n, epsilon_n, kappa_n for the original zero seed; n>=1."""
    _nat(n,1)
    _,u=state(n)
    v=16*u
    j=floorq(v)
    r=forcing(n+1)
    eps=floorq(v+r)-j
    return j,eps,j+eps


def fiber_interval(n:int,depth:int) -> tuple[int,int,Fraction,Fraction]:
    """A set-valued readout [c+k/M,c+(k+1)/M), containing original U_n."""
    _nat(n,1);_nat(depth,1)
    c,u=state(n)
    M=16**depth
    k=floorq(M*u)
    return c,k,Fraction(c)+Fraction(k,M),Fraction(c)+Fraction(k+1,M)


def forecast_carries(n:int,depth:int,horizon:int) -> tuple[int,int]:
    """Inclusive min/max future integer carry for ALL states in the readout fiber.

    The interval is half-open. The original pointed trajectory is one of
    these states; this is a set-valued reinjection, not a fake zero-seed reset.
    """
    _,_,low,high=fiber_interval(n,depth)
    _nat(horizon,1)
    z=forced_shift(n,horizon)
    return floorq(16**horizon*low+z),ceilq(16**horizon*high+z)-1


def _is_prime(p:int) -> bool:
    return type(p) is int and p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def _primes(primes: Iterable[int]) -> tuple[int,...]:
    ps=tuple(primes)
    if len(set(ps))!=len(ps) or not all(map(_is_prime,ps)):
        raise ValueError("distinct genuine primes required")
    return ps


def prime_pair(primes: Iterable[int]) -> tuple[Fraction,Fraction]:
    """Exact PCE finite Euler/Hurwitz values at zeta(-1)."""
    ps=_primes(primes)
    e=Fraction(1)
    for p in ps:
        e/=1-p
    return e,Z_NEG1/e


def uv_from_pair(e:Fraction,r:Fraction) -> tuple[Fraction,Fraction]:
    return (e+r)/2,(e-r)/2


def prime_uv(primes:Iterable[int]) -> tuple[Fraction,Fraction,int]:
    ps=_primes(primes)
    u,v=uv_from_pair(*prime_pair(ps))
    return u,v,(-1)**len(ps)


def rational_sqrt(x:Fraction) -> Fraction:
    x=Fraction(x)
    if x<0: raise ValueError("nonnegative required")
    a,b=isqrt(x.numerator),isqrt(x.denominator)
    if a*a!=x.numerator or b*b!=x.denominator:
        raise ValueError("square root not rational on this input")
    return Fraction(a,b)


def source_branch_section(u:Fraction,prime_parity:int) -> tuple[Fraction,Fraction]:
    """Section of real hyperbola u²-v²=-1/12, with explicit orientation bit.

    This function requires a rational perfect-square source point. The
    symbolic definition for general u is v=parity*sqrt(u²+1/12).
    """
    if prime_parity not in (-1,1):
        raise ValueError("orientation bit ±1 required")
    u=Fraction(u)
    return u,prime_parity*rational_sqrt(u*u+Fraction(1,12))


def signed_boost(u:Fraction,v:Fraction,p:int) -> tuple[Fraction,Fraction]:
    if not _is_prime(p):raise ValueError("genuine prime required")
    a=Fraction(p-1)
    c=(a+1/a)/2
    s=(a-1/a)/2
    return (-c*u+s*v,s*u-c*v)


def projected_section_gap(primes:Iterable[int],p:int,q:int,
                          wrong_parity:int=1) -> tuple[Fraction,Fraction,Fraction]:
    """(authentic full u, correct-section u, wrong-section u) after two steps.

    Preexisting genuine prime inventory is distinct from new p and q.
    Wrong section is still on zeta hyperbola, but not the authentic
    prime-history branch when its parity differs from recorded history.
    """
    ps=_primes(primes)
    if p==q or p in ps or q in ps or not _is_prime(p) or not _is_prime(q):
        raise ValueError("new distinct genuine primes required")
    u,v,_=prime_uv(ps)
    u1,v1=signed_boost(u,v,p)
    exact,_=signed_boost(u1,v1,q)
    right_uv=source_branch_section(u1,(-1)**(len(ps)+1))
    wrong_uv=source_branch_section(u1,wrong_parity)
    true_v,_=signed_boost(*right_uv,q)
    wrong_v,_=signed_boost(*wrong_uv,q)
    return exact,true_v,wrong_v
