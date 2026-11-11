"""Exact rational certificates for a Dedekind-cut / Stern--Brocot SUCC probe.

This is a finite observer, NOT an oracle for general real equality, a normality
proof, or an implementation of the whole presheaf category. Source r(n) is the
immutable four-pole BBP forcing, copied here for standalone focused testing.
No floating-point arithmetic enters the mathematical certificates.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt
from typing import Callable


@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q

    def __post_init__(self) -> None:
        if type(self.lo) is not Q or type(self.hi) is not Q or not self.lo < self.hi:
            raise ValueError("require exact rational lo < hi")

    @property
    def width(self) -> Q:
        return self.hi - self.lo


Oracle = Callable[[int], Interval]


def bbp_r(n: int) -> Q:
    """Immutable source r(n), n>=1, with all four signed poles."""
    if type(n) is not int or n < 1:
        raise ValueError("positive integer source clock required")
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def pi_over_16_bounds(depth: int) -> Interval:
    """Strict enclosure for x=pi/16 from a finite original BBP prefix.

    x = sum_{j>=1}16^{-j} r(j); tail in (0, r(depth+1)/(15*16**depth)).
    This uses positivity and decrease of r(j), independent of decimal pi.
    """
    if type(depth) is not int or depth < 1:
        raise ValueError("depth must be positive integer")
    lo = sum((bbp_r(j)/16**j for j in range(1, depth+1)), Q(0))
    hi = lo + bbp_r(depth+1) / (15*16**depth)
    return Interval(lo, hi)


def sqrt2_bounds(depth: int) -> Interval:
    """Strict certified dyadic enclosure of sqrt(2), via integer isqrt."""
    if type(depth) is not int or depth < 1:
        raise ValueError("depth must be positive integer")
    scale = 1 << depth
    k = isqrt(2*scale*scale)
    return Interval(Q(k, scale), Q(k+1, scale))


def affine_oracle(oracle: Oracle, a: Q, b: Q) -> Oracle:
    """Exact interval transport for increasing rational affine maps x->a*x+b."""
    if type(a) is not Q or type(b) is not Q or a <= 0:
        raise ValueError("require rational a>0 and rational b")
    def out(depth: int) -> Interval:
        v = oracle(depth)
        return Interval(a*v.lo+b, a*v.hi+b)
    return out


def cut_probe(oracle: Oracle, q: Q, *, max_depth: int=80) -> bool:
    """Decide q<x using progressively sharper strict rational enclosures.

    Halts for a convergent oracle if x!=q; on an unbounded attempt with x=q
    it may never decide. Budget exhaustion is UNKNOWN, never FALSE.
    """
    if type(q) is not Q or type(max_depth) is not int or max_depth < 1:
        raise ValueError("invalid rational query or depth budget")
    for depth in range(1, max_depth+1):
        box = oracle(depth)
        if q <= box.lo:
            return True
        if q >= box.hi:
            return False
    raise RuntimeError("UNKNOWN: finite budget cannot separate rational probe")


def radix_prefix(oracle: Oracle, digits: int, *, max_depth: int=100) -> tuple[int, ...]:
    """Exact base-16 prefix for an irrational x in (0,1), when certified.

    Requires a shrinking correct enclosure. A valid return is a certificate,
    but termination is not promised for a rational on a digit boundary.
    """
    if type(digits) is not int or digits < 1 or type(max_depth) is not int or max_depth < 1:
        raise ValueError("invalid digit count or depth")
    base = 16**digits
    for depth in range(1, max_depth+1):
        box = oracle(depth)
        if not (0 < box.lo and box.hi < 1):
            continue
        a = (base*box.lo).__floor__()
        b = (base*box.hi).__floor__()
        if a == b:
            acc = a
            out = [0]*digits
            for j in range(digits-1, -1, -1):
                out[j] = acc % 16
                acc //= 16
            assert acc == 0
            return tuple(out)
    raise RuntimeError("UNKNOWN: digit cylinder not certified within budget")


def winding(digits: tuple[int, ...]) -> int:
    out = 0
    for d in digits:
        if type(d) is not int or not 0 <= d < 16:
            raise ValueError("invalid hex digit")
        out = 16*out+d
    return out


@dataclass(frozen=True)
class FareyBounds:
    """Neighboring fractions a/b<c/d; d=0 denotes +infinity."""
    a: int = 0
    b: int = 1
    c: int = 1
    d: int = 0

    def __post_init__(self) -> None:
        if any(type(v) is not int for v in (self.a,self.b,self.c,self.d)):
            raise TypeError("integer Farey matrix required")
        if self.b <= 0 or self.d < 0 or self.b*self.c-self.a*self.d != 1:
            raise ValueError("non-unimodular Farey bounds")

    @property
    def mediant(self) -> Q:
        return Q(self.a+self.c, self.b+self.d)

    @property
    def finite_width(self) -> Q | None:
        return Q(1, self.b*self.d) if self.d else None

    def step(self, direction: str) -> FareyBounds:
        if direction == "L":
            return FareyBounds(self.a,self.b,self.a+self.c,self.b+self.d)
        if direction == "R":
            return FareyBounds(self.a+self.c,self.b+self.d,self.c,self.d)
        raise ValueError("direction must be L or R")


def stern_brocot_prefix(oracle: Oracle, steps: int, *, max_depth: int=120) -> tuple[str, FareyBounds]:
    """Finite path for a positive irrational: L if x<mediant, R if >."""
    if type(steps) is not int or steps < 0:
        raise ValueError("nonnegative integer step count required")
    state = FareyBounds()
    path = []
    for _ in range(steps):
        direction = "R" if cut_probe(oracle, state.mediant, max_depth=max_depth) else "L"
        state = state.step(direction)
        path.append(direction)
    return "".join(path), state


def prime_valuations(n: int) -> dict[int,int]:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")
    ans: dict[int,int] = {}
    k = n
    p = 2
    while p*p <= k:
        while k%p == 0:
            ans[p] = ans.get(p,0)+1
            k //= p
        p += 1
    if k > 1:
        ans[k] = ans.get(k,0)+1
    return ans


def mobius_quotient(a: int, b: int) -> int:
    """Incidence inverse on the divisibility poset: mu(b/a) when a|b."""
    if type(a) is not int or type(b) is not int or a < 1 or b < 1 or b%a:
        raise ValueError("require comparable positive divisors a|b")
    vals = prime_valuations(b//a)
    return 0 if any(v > 1 for v in vals.values()) else (-1)**len(vals)


def divisors(n: int) -> tuple[int,...]:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")
    return tuple(d for d in range(1,n+1) if n%d == 0)
