"""Exact original-four-pole SUCC prime conductor and observer-projection audit.

Research-only: classical modular arithmetic / cyclotomic trace. No signed
selected normality theorem, no physical quantum claim, no new canonical core.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt

F = Fraction


def source(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer source index required")
    return (F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2))


def source_independent(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer source index required")
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def state(n: int, seed: F | int = 0) -> F:
    if type(n) is not int or n < 0 or type(seed) not in (int,F):
        raise ValueError("exact nonnegative n, rational seed")
    u=F(seed)
    for j in range(1,n+1):
        u=16*u+source(j)
    return u


def state_independent(n: int, seed: F | int = 0) -> F:
    if type(n) is not int or n < 0 or type(seed) not in (int,F):
        raise ValueError("exact nonnegative n, rational seed")
    return F(seed)*16**n + sum((16**(n-j)*source_independent(j) for j in range(1,n+1)),F(0))


def prime(p: int) -> bool:
    if type(p) is not int or p<2:return False
    if p%2==0:return p==2
    for d in range(3,isqrt(p)+1,2):
        if p%d==0:return False
    return True


@dataclass(frozen=True)
class Birth:
    p:int
    n:int
    coefficient:int
    first_reuse:int

    @property
    def length(self) -> int:
        return self.first_reuse-self.n


def birth(p: int) -> Birth:
    if not prime(p) or p<=5 or p%8 not in (1,5):
        raise ValueError("eligible prime p>5, p congruent 1 or 5 mod 8")
    if p%8==1:
        n,c=(p+7)//8,4
    else:
        n,c=(p+3)//8,-1
    return Birth(p,n,c,(p+1)//2)


def primes_upto(bound:int)->list[int]:
    if type(bound) is not int or bound<0:raise ValueError("nonnegative bound")
    if bound<2:return []
    sieve=bytearray(b'\x01')*(bound+1)
    sieve[0:2]=b'\x00\x00'
    for x in range(2,isqrt(bound)+1):
        if sieve[x]:sieve[x*x:bound+1:x]=b'\x00'*(((bound-x*x)//x)+1)
    return [p for p in range(2,bound+1) if sieve[p]]


def horizon_primes(N:int)->list[int]:
    """Exactly the large p=1 mod4 births persisting through N (p>5)."""
    if type(N) is not int or N<1:raise ValueError("N positive")
    return [p for p in primes_upto(8*N) if 2*N<p<8*N and p>5 and p%4==1]


def residue(x:F,p:int)->int:
    """Rational x mod p; only lawful when denominator prime to p."""
    if gcd(x.denominator,p)!=1:raise ValueError("p-divisible rational denominator")
    return (x.numerator*pow(x.denominator,-1,p))%p


def p_residue_of_state(u:F,p:int)->int:
    """One-pole residue, certifies v_p(u)=-1."""
    if u.denominator%p or (u.denominator//p)%p==0:
        raise ValueError("not an exactly once p-divisible denominator")
    return residue(p*u,p)


def persistent_residue(p:int,j:int,seed:F|int=0)->int:
    b=birth(p)
    if type(j) is not int or not b.n<=j<b.first_reuse:
        raise ValueError("not in the source prime birth window")
    if type(seed) not in (int,F) or F(seed).denominator%p==0:
        raise ValueError("seed must be p-integral; this is NOT an irrational-seed theorem")
    actual=p_residue_of_state(state(j,seed),p)
    expected=b.coefficient*pow(16,j-b.n,p)%p
    if actual!=expected:raise ArithmeticError("original four-pole source residue mismatch")
    return actual


def phase_split(u:F,ps:list[int])->tuple[F,tuple[tuple[int,int],...]]:
    """Canonical p-primary rationals plus a component integral at every p."""
    if type(u) is not F:raise TypeError("exact Fraction required")
    if len(ps)!=len(set(ps)) or any(not prime(p) for p in ps):
        raise ValueError("pairwise distinct primes required")
    parts=tuple((p,p_residue_of_state(u,p)) for p in sorted(ps))
    v=u-sum((F(a,p) for p,a in parts),F(0))
    if any(v.denominator%p==0 for p in ps):
        raise ArithmeticError("cofactor not p-free")
    if v+sum((F(a,p) for p,a in parts),F(0))!=u:
        raise ArithmeticError("phase split failed")
    return v,parts


def trace_factor(parts:tuple[tuple[int,int],...],h:int)->F:
    """Normalized Galois relative-trace multiplier, NOT a temporal average."""
    if type(h) is not int:raise ValueError("integer frequency only")
    out=F(1)
    for p,a in parts:
        if not prime(p) or not 0<a<p:raise ValueError("primitive p factor required")
        out*=F(1) if h%p==0 else -F(1,p-1)
    return out


def spoof_cofactors(p:int,exponents:list[int],q:int|None=None)->list[F]:
    """p-free rational phases nearly cancel any prescribed p-clock.

    This is an adversarial *different path*, NOT the original BBP source.
    """
    if not prime(p):raise ValueError("prime required")
    if q is None:q=isqrt(p)+1
    if type(q) is not int or q<=1 or gcd(q,p)!=1:raise ValueError("p-free q >1")
    vals=[]
    for a in exponents:
        if type(a) is not int:raise ValueError("integer exponent")
        a%=p
        k=-((2*a*q+p)//(2*p))
        v=F(k,q)
        eps=F(a,p)+v
        if abs(eps)>F(1,2*q):raise ArithmeticError("exact p-free spoof bound failed")
        vals.append(v)
    return vals


def source_mass_certificate()->tuple[F,F]:
    """Σ_{n>=2}r(n) < Σ_{n=2}^{16}r(n)+1/64 < 65/256."""
    partial=sum((source(n) for n in range(2,17)),F(0))
    capped=partial+F(1,64)
    if not capped<F(65,256):raise ArithmeticError("source mass certificate failed")
    return partial,capped


def quarter_frame(h:int)->int:
    """0: observe Im at h, 1: observe -Re at h."""
    if type(h) is not int or h<=0:raise ValueError("positive harmonic")
    k=0
    while h%16==0:
        k+=1;h//=16
    return k%2


def ladder_uniform_error(N:int,h:int)->F:
    """Proved |A_N(16h)-A_N(h)| < this rational number.

    Uses 2π < 44/7 and the exact prime-independent original source bound.
    """
    if type(N) is not int or N<1 or type(h) is not int:
        raise ValueError("N positive and h integer")
    source_mass_certificate()
    return (F(2)+F(715,448)*abs(h))/N
