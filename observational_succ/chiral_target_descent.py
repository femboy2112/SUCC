"""Source-faithful chiral gauge, two-clock filters, and a Weyl-equivalent metric.

The analytic proofs are in CHIRAL_TARGET_DESCENT_REASSEMBLY.md.  This module
never asserts normality from a finite receipt.  Only stdlib exact arithmetic
is used, including outward-enclosed trigonometric evaluations.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from typing import Sequence

from .rank_two_chiral_towers import source_moment


def natural(n: int, label: str, low: int = 0, high: int = 4096) -> int:
    if type(n) is not int or not low <= n <= high:
        raise ValueError(f"{label}: exact integer required in [{low},{high}]")
    return n


def gauge(n: int) -> Q:
    """Exact common endpoint moment, not a changed source or seed."""
    natural(n, "time", high=100_000)
    return Q(1, 4 * (8 * n + 1))


def tail_kernel(t: Q, lane: str) -> Q:
    t = Q(t)
    if not 0 <= t <= 1:
        raise ValueError("kernel argument outside [0,1]")
    if lane == "plus":
        return (2-t)/(4*(t*t-2*t+2))
    if lane == "minus":
        return -t/(4*(2-t*t))
    raise ValueError("lane must be plus or minus")


def residual_kernel(t: Q, lane: str) -> Q:
    """Positive exact residual after removing the signed common endpoint."""
    t = Q(t)
    if not 0 <= t <= 1:
        raise ValueError("kernel argument outside [0,1]")
    if lane == "plus":
        return t*(1-t)/(4*(t*t-2*t+2))
    if lane == "minus":
        return (1-t)*(t+2)/(4*(2-t*t))
    raise ValueError("lane must be plus or minus")


def residual_bounds(n: int) -> tuple[Q, Q]:
    natural(n, "time", low=1, high=100_000)
    return (Q(1, 4*(8*n+2)*(8*n+3)),
            Q(3, 4*(8*n+1)*(8*n+2)))


def phase_history(count: int) -> tuple[tuple[Q, Q], ...]:
    """Authentic zero-seeded chiral states reduced mod 1 at each step.

    Since 16 is integral, this yields exactly the phases of the unwrapped
    rational states, without converting either huge value to float.
    """
    natural(count, "count", low=1)
    a = b = Q(0)
    out = []
    for n in range(1, count+1):
        a = (16*a + source_moment(n, channel="even")) % 1
        b = (16*b + source_moment(n, channel="odd")) % 1
        out.append((a, b))
    return tuple(out)


def corrected_pair(n: int, plus: Q, minus: Q) -> tuple[Q, Q]:
    return Q(plus)+gauge(n), Q(minus)-gauge(n)


def polynomial(values: Sequence[int]) -> tuple[int, ...]:
    cs = tuple(values)
    if not cs or len(cs) > 256 or any(type(x) is not int for x in cs):
        raise ValueError("nonempty integer polynomial of degree <256 required")
    while len(cs) > 1 and cs[-1] == 0:
        cs = cs[:-1]
    return cs


def evaluate(cs: Sequence[int], x: int) -> int:
    out = 0
    for c in reversed(polynomial(cs)):
        out = out*x+c
    return out


def divide_linear(cs: Sequence[int], root: int) -> tuple[tuple[int, ...], int]:
    cs = polynomial(cs)
    if len(cs) == 1:
        return (0,), cs[0]
    out = [0]*(len(cs)-1)
    out[-1] = cs[-1]
    for j in range(len(out)-2, -1, -1):
        out[j] = cs[j+1]+root*out[j+1]
    return polynomial(out), cs[0]+root*out[0]


@dataclass(frozen=True)
class FilterCertificate:
    endpoint_residue: int
    pi_coefficient: int
    log2_coefficient: int
    neutral_quotient: tuple[int, ...] | None


def classify_filter(plus: Sequence[int], minus: Sequence[int]) -> FilterCertificate:
    a, b = polynomial(plus), polynomial(minus)
    d = tuple((a[j] if j < len(a) else 0)-(b[j] if j < len(b) else 0)
              for j in range(max(len(a), len(b))))
    d1, d16 = evaluate(d, 1), evaluate(d, 16)
    quotient = None
    if d1 == 0 and d16 == 0:
        once, r1 = divide_linear(d, 1)
        quotient, r16 = divide_linear(once, 16)
        if r1 or r16:
            raise ArithmeticError("neutral polynomial division failed")
    return FilterCertificate(d1, evaluate(a, 16), 2*d16, quotient)


def harmonic_shift_cost(shift: int) -> Q:
    natural(shift, "shift")
    return sum((gauge(j) for j in range(1, shift+1)), Q(0))


def neutral_budget(plus: Sequence[int], minus: Sequence[int]) -> Q:
    """Rational upper bound on sum of absolute RAW Green defects.

    Uses B<1/15. Only defined when the endpoint residues cancel. No
    numerical phase cancellation is assumed. Symbol at 16 may be nonzero.
    """
    a, b = polynomial(plus), polynomial(minus)
    cert = classify_filter(a, b)
    if cert.endpoint_residue:
        raise ValueError("raw defect is not summable: D(1) is nonzero")
    out = Q(0)
    for j in range(max(len(a), len(b))):
        x = a[j] if j < len(a) else 0
        y = b[j] if j < len(b) else 0
        out += Q(max(abs(x), abs(y)), 15) + abs(x-y)*harmonic_shift_cost(j)
    return out


def quotient_multiplier(a: int, b: int, finite_order: int | None = None) -> int:
    """Haar anti-diagonal projection; finite version retains aliases."""
    if type(a) is not int or type(b) is not int:
        raise ValueError("integer Fourier labels required")
    if finite_order is None:
        return int(a == b)
    natural(finite_order, "finite gauge order", low=1)
    return int((a-b) % finite_order == 0)


@dataclass(frozen=True)
class Bounds:
    low: Q
    high: Q

    def __post_init__(self) -> None:
        if self.low > self.high:
            raise ValueError("reversed exact interval")


def _atan_inverse(d: int, terms: int) -> Bounds:
    value = sum((Q((-1)**k, (2*k+1)*d**(2*k+1))
                 for k in range(terms)), Q(0))
    error = Q(1, (2*terms+1)*d**(2*terms+1))
    return Bounds(value-error, value) if terms % 2 else Bounds(value, value+error)


@lru_cache(maxsize=8)
def pi_bounds(bits: int = 64) -> Bounds:
    natural(bits, "precision", low=16, high=256)
    terms = max(8, bits//4)
    den = 1 << bits
    while True:
        a, b = _atan_inverse(5, terms), _atan_inverse(239, terms)
        lo, hi = 16*a.low-4*b.high, 16*a.high-4*b.low
        if hi-lo < Q(1, den):
            return Bounds(Q((lo*den).__floor__(), den),
                          Q((hi*den).__ceil__(), den))
        terms += 1


def _outward(low: Q, high: Q, bits: int) -> Bounds:
    den = 1 << bits
    return Bounds(max(Q(-1), Q((low*den).__floor__(), den)),
                  min(Q(1), Q((high*den).__ceil__(), den)))


@lru_cache(maxsize=32768)
def _trig_cell(cell: int, bits: int, terms: int) -> tuple[Bounds, Bounds]:
    """Enclose all turns in [cell/2^bits,(cell+1)/2^bits]."""
    den = 1 << bits
    t = Q(cell, den)
    p = pi_bounds(bits)
    mid, radius = (p.low+p.high)/2, (p.high-p.low)/2
    angle = 2*mid*t
    angle_error = 2*p.high/den + 2*abs(t)*radius
    cosine = sum(((-1)**k * angle**(2*k)/factorial(2*k)
                  for k in range(terms)), Q(0))
    sine = sum(((-1)**k * angle**(2*k+1)/factorial(2*k+1)
                for k in range(terms)), Q(0))
    ec = abs(angle)**(2*terms)/factorial(2*terms) + angle_error
    es = abs(angle)**(2*terms+1)/factorial(2*terms+1) + angle_error
    return (_outward(cosine-ec, cosine+ec, bits),
            _outward(sine-es, sine+es, bits))


def trig_turn(turn: Q, bits: int = 64, terms: int = 18) -> tuple[Bounds, Bounds]:
    if type(turn) not in (int, Q):
        raise ValueError("turn must be an exact integer or Fraction")
    natural(bits, "precision", low=16, high=256)
    natural(terms, "Taylor terms", low=2, high=128)
    r = Q(turn) % 1
    if r > Q(1, 2):
        r -= 1
    return _trig_cell((r*(1 << bits)).__floor__(), bits, terms)


def _square(b: Bounds) -> Bounds:
    return Bounds(Q(0) if b.low <= 0 <= b.high else min(b.low*b.low, b.high*b.high),
                  max(b.low*b.low, b.high*b.high))


def mode_square_bounds(phases: Sequence[Q], h: int) -> Bounds:
    if (not phases or type(h) is not int or h == 0
            or any(type(x) not in (int, Q) for x in phases)):
        raise ValueError("nonempty phase data and nonzero integer mode required")
    vals = [trig_turn(h*Q(x)) for x in phases]
    n = len(vals)
    c = Bounds(sum((x[0].low for x in vals), Q(0))/n,
               sum((x[0].high for x in vals), Q(0))/n)
    s = Bounds(sum((x[1].low for x in vals), Q(0))/n,
               sum((x[1].high for x in vals), Q(0))/n)
    sc, ss = _square(c), _square(s)
    return Bounds(max(Q(0), sc.low+ss.low), min(Q(1), sc.high+ss.high))


@dataclass(frozen=True)
class EnergyCertificate:
    n: int
    modes: int
    partial: Bounds
    spectral_tail: Q

    @property
    def full(self) -> Bounds:
        return Bounds(self.partial.low, min(Q(2), self.partial.high+self.spectral_tail))


def poisson_energy(phases: Sequence[Q], modes: int = 16) -> EnergyCertificate:
    """Q_N=2 sum(h>=1) 2^-h |mean e(h*x_n)|^2 with exact tail bound.

    Finite output is NOT a certificate of an infinite-time limit. Every
    nonzero mode has positive fixed weight, avoiding a prescribed growing
    CRT or frequency schedule as an extra hypothesis.
    """
    natural(modes, "modes", low=1, high=128)
    if not phases or any(type(x) not in (int, Q) for x in phases):
        raise ValueError("nonempty exact rational phases required")
    lo = hi = Q(0)
    for h in range(1, modes+1):
        v = mode_square_bounds(phases, h)
        weight = Q(2, 2**h)
        lo += weight*v.low
        hi += weight*v.high
    return EnergyCertificate(len(phases), modes, Bounds(lo, hi), Q(2, 2**modes))


def rational_control(count: int) -> tuple[Q, ...]:
    """PR320's explicitly different zero-seeded nonnormal source phases."""
    natural(count, "count", low=1)
    return tuple((-Q(n+1, (2*n+1)*(4*n+1)*(8*n+1))) % 1
                 for n in range(1, count+1))


def poisson_kernel(turn: Q) -> Bounds:
    """Exact enclosure of 3/(5-4*cos(2*pi*t))-1, range [-2/3,2]."""
    c, _ = trig_turn(turn)
    return Bounds((4*c.low-2)/(5-4*c.low), (4*c.high-2)/(5-4*c.high))


def innovation(phases: Sequence[Q], next_phase: Q) -> Bounds:
    """Signed full-spectrum innovation; no frequency truncation."""
    if not phases or any(type(x) not in (int, Q) for x in phases):
        raise ValueError("nonempty exact phase history required")
    if type(next_phase) not in (int, Q):
        raise ValueError("exact next phase required")
    vals = [poisson_kernel(Q(next_phase)-Q(x)) for x in phases]
    return Bounds(sum((x.low for x in vals), Q(0))/len(vals),
                  sum((x.high for x in vals), Q(0))/len(vals))
