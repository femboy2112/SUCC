"""Exact controls for the Main VIII restricted conic incidence theorem.

The universal theorem is the accompanying paper proof. These immutable exact
records are research evidence, not proof-authority objects. Every selected
divisor triple remains a separate record; no source-level deduplication occurs.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import gcd, isqrt


def _positive(*values: int) -> None:
    if any(type(v) is not int or v < 1 for v in values):
        raise ValueError("expected positive integers, excluding bool")


def _rational(value: int | Fraction, name: str, minimum=0) -> Fraction:
    if type(value) not in (int, Fraction) or value < minimum:
        raise ValueError(f"{name} must be an exact rational >= {minimum}")
    return Fraction(value)


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    _positive(n)
    result = []
    p = 2
    while p*p <= n:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k:
            result.append((p, k))
        p += 1
    if n > 1:
        result.append((n, 1))
    return tuple(result)


def ris(n: int) -> int:
    _positive(n)
    answer = 1
    for p, k in factorization(n):
        answer *= p**(k-1)
    return answer


def powerful_divisors(n: int) -> tuple[int, ...]:
    """All eligible selections, including 1; not just maximal divisors."""
    result = [1]
    for p, k in factorization(n):
        result = [d*p**j for d in result for j in (0, *range(2, k+1))]
    return tuple(sorted(result))


def integer_weight(d: int, t: int) -> int:
    """Exact g_t(d) at nonnegative integer t, including its zero coefficients."""
    _positive(d)
    if type(t) is not int or t < 0:
        raise ValueError("t must be a nonnegative integer")
    result = 1
    for p, k in factorization(d):
        if k == 1:
            return 0
        result *= p**(t*(k-1)) - p**(t*(k-2))
    return result


@dataclass(frozen=True)
class CofactorSelection:
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int

    def __post_init__(self):
        _positive(self.a, self.b, self.c, self.d, self.e, self.f)
        if self.a + self.b != self.c or gcd(self.a, self.b) != 1:
            raise ValueError("need a primitive positive source a+b=c")
        if any(n % q for n, q in ((self.a,self.d),(self.b,self.e),(self.c,self.f))):
            raise ValueError("each selected modulus must divide its actual source")
        if any(k == 1 for q in (self.d,self.e,self.f) for _, k in factorization(q)):
            raise ValueError("selected moduli must be powerful, or 1")

    @property
    def cofactors(self) -> tuple[int, int, int]:
        return self.a//self.d, self.b//self.e, self.c//self.f

    @property
    def D(self) -> int:
        return self.d*self.e*self.f

    @property
    def U(self) -> int:
        u,v,w = self.cofactors
        return u*v*w

    @property
    def square_roots(self) -> tuple[int, int, int] | None:
        roots = tuple(isqrt(q) for q in (self.d,self.e,self.f))
        return roots if all(r*r == q for r,q in zip(roots,(self.d,self.e,self.f))) else None


def source_selections(a: int, b: int) -> tuple[CofactorSelection, ...]:
    _positive(a,b)
    if gcd(a,b) != 1:
        raise ValueError("source must be primitive")
    return tuple(CofactorSelection(a,b,a+b,d,e,f) for d,e,f in product(
        powerful_divisors(a), powerful_divisors(b), powerful_divisors(a+b)))


@dataclass(frozen=True)
class ConicSeed:
    """A displayed integral point on u*r^2+v*s^2=w*z^2."""
    u: int
    v: int
    w: int
    r0: int
    s0: int
    z0: int

    def __post_init__(self):
        _positive(self.u,self.v,self.w,self.r0,self.s0,self.z0)
        if self.u*self.r0**2 + self.v*self.s0**2 != self.w*self.z0**2:
            raise ValueError("the displayed seed does not lie on this conic")

    @property
    def cancellation_multiple(self) -> int:
        return 2*self.u*self.v*self.w*self.z0**3

    @property
    def count_coefficient_squared(self) -> int:
        """Count <=16*z0^2*sqrt(uvw*X); squared coefficient is an integer."""
        return 256*self.z0**4*self.u*self.v*self.w

    def parameter_image(self, n: int, m: int) -> tuple[int,int,int]:
        if type(n) is not int or type(m) is not int or gcd(n,m) != 1:
            raise ValueError("direction coordinates must be coprime integers")
        Q = self.u*n*n + self.v*m*m
        L = self.u*self.r0*n + self.v*self.s0*m
        return self.r0*Q-2*n*L, self.s0*Q-2*m*L, self.z0*Q


def conic_selections(seed: ConicSeed, X: int | Fraction) -> tuple[CofactorSelection, ...]:
    """Independent direct conic census; retains actual source primitivity.

    Root primitivity alone is insufficient when coefficients have prime factors.
    No radical-depth cutoff or high-D cutoff is silently imposed here.
    """
    X = _rational(X,"X",2)
    if type(seed) is not ConicSeed:
        raise ValueError("expected an immutable ConicSeed")
    answer = []
    for z in range(1,isqrt(X//seed.w)+1):
        c = seed.w*z*z
        for r in range(1,isqrt((c-1)//seed.u)+1):
            remaining = c-seed.u*r*r
            if remaining % seed.v:
                continue
            s = isqrt(remaining//seed.v)
            if s*s*seed.v != remaining or gcd(seed.u*r*r,remaining) != 1:
                continue
            answer.append(CofactorSelection(seed.u*r*r,remaining,c,r*r,s*s,z*z))
    return tuple(answer)


@dataclass(frozen=True)
class CatalogGrowthBudget:
    t: Fraction
    kappa: Fraction
    theta: Fraction
    exponent: Fraction
    saving: Fraction
    source_moment: bool
    coefficient: int = 23


def catalog_growth_budget(t: int | Fraction, kappa: int | Fraction,
                          theta: int | Fraction, *, source_moment=False) -> CatalogGrowthBudget:
    """Paper budget for u,v<=X^theta, w=u+v, ris(r*s*z)<=X^kappa.

    Square-divisor incidence has cofactor exponent (7-3t)/2. The full
    restricted source moment has exponent (7+3t)/2 instead. A positive saving
    is needed for a subquadratic conclusion. Arbitrary sources are not covered.
    """
    t = _rational(t,"t")
    kappa = _rational(kappa,"kappa")
    theta = _rational(theta,"theta")
    if t > 1 or type(source_moment) is not bool:
        raise ValueError("need 0<=t<=1 and a boolean source_moment selector")
    sign = 1 if source_moment else -1
    exponent = (1+3*t)/2 + kappa*t + theta*(7+sign*3*t)/2
    return CatalogGrowthBudget(t,kappa,theta,exponent,2-exponent,source_moment)
