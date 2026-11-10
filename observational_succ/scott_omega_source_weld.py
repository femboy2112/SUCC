"""SUCC Scott–Omega causal-weld finite arithmetic instrument.

Preserves the original four-pole BBP source and literal zero seed.
Claims are finite algebra/interval certificates, not pi normality.
Uses only Python's standard library; see accompanying THEOREMS.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import floor


@dataclass(frozen=True)
class RationalInterval:
    lo: Q
    hi: Q

    def __post_init__(self) -> None:
        object.__setattr__(self, 'lo', Q(self.lo))
        object.__setattr__(self, 'hi', Q(self.hi))
        if self.lo > self.hi:
            raise ValueError('empty interval cannot represent a nonempty compact')

    @property
    def width(self) -> Q:
        return self.hi - self.lo

    def below(self, other: 'RationalInterval') -> bool:
        """More-informed-than relation in the reverse-inclusion domain."""
        return other.lo <= self.lo and self.hi <= other.hi

    def scaled(self, k: int) -> 'RationalInterval':
        if not isinstance(k, int) or k <= 0:
            raise ValueError('positive integer scaling required')
        return RationalInterval(self.lo * k, self.hi * k)


def bbp_forcing(n: int) -> Q:
    if not isinstance(n, int) or n < 1:
        raise ValueError('BBP source indices must be >= 1')
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def selected_state(n: int) -> Q:
    """Original rational U_0=0 state, with no floating point operations."""
    if not isinstance(n, int) or n < 0:
        raise ValueError('nonnegative SUCC time required')
    u = Q(0)
    for j in range(1, n+1):
        u = 16*u + bbp_forcing(j)
    return u


def prefix_pi_over_16(horizon: int) -> Q:
    if not isinstance(horizon, int) or horizon < 1:
        raise ValueError('positive finite source horizon required')
    return sum((bbp_forcing(j) / 16**j for j in range(1, horizon+1)), Q())


def finite_green_tail(n: int, horizon: int) -> Q:
    if not isinstance(n, int) or n < 0 or not isinstance(horizon, int) or horizon < n:
        raise ValueError('0 <= n <= horizon required')
    return sum((Q(bbp_forcing(j), 16**(j-n)) for j in range(n+1, horizon+1)), Q())


def prefix_error_bound(horizon: int) -> Q:
    """Strict bound 0 < pi/16 - P_L < 4*16^-L/(15*(L+1)^2)."""
    if not isinstance(horizon, int) or horizon < 1:
        raise ValueError('positive horizon required')
    return Q(4, 15 * (horizon+1)**2 * 16**horizon)


def completed_interval(n: int, horizon: int) -> RationalInterval:
    """Certified compact rational interval containing 16**(n-1)*pi."""
    if not isinstance(n, int) or n < 0 or not isinstance(horizon, int) or horizon < max(1,n):
        raise ValueError('0 <= n <= horizon with positive horizon required')
    low = 16**n * prefix_pi_over_16(horizon)
    return RationalInterval(low, low + 16**n * prefix_error_bound(horizon))


def circle_arcs(interval: RationalInterval) -> tuple[tuple[Q, Q], ...]:
    """Closed interval image in R/Z, encoded in [0,1] with endpoints identified.

    A degenerate circle point [0] is represented by (0,0); a seam-crossing
    connected arc has two representative intervals. This is an observation,
    NOT an invertible change of coordinates.
    """
    a, b = interval.lo, interval.hi
    if b-a >= 1:
        return ((Q(), Q(1)),)
    ka,kb = floor(a),floor(b)
    aa,bb = a-ka,b-kb
    if ka == kb:
        return ((aa,bb),)
    if kb == ka+1:
        arcs = [(Q(0),bb),(aa,Q(1))]
        return tuple(pair for pair in arcs if pair[0] <= pair[1])
    raise AssertionError('short interval cannot cross multiple integer seams')


def trace_omega_k(arity: int, steps: int) -> tuple[int, ...]:
    """Occurrence counts after explicitly indexed leftmost Ω_k beta contractions.

    Counts are not geometric dimensions. The raw Ω terms have NO finite beta
    normal form. This is a finite syntactic trace of one reduction strategy.
    """
    if not isinstance(arity,int) or arity<2 or not isinstance(steps,int) or steps<0:
        raise ValueError('arity >= 2, steps >= 0')
    return tuple(2+(arity-2)*i for i in range(steps+1))


def circular_point_distance(a: Q, b: Q) -> Q:
    """Exact geodesic distance of rational points in R/Z."""
    d=(Q(a)-Q(b)) % 1
    return min(d,1-d)


def seam_pair(stage: int) -> tuple[RationalInterval,RationalInterval]:
    """Opposite directed chains, never equal at finite stages, equal at q-limit."""
    if not isinstance(stage,int) or stage<1:
        raise ValueError('stage >= 1')
    eps=Q(1,16**stage)
    return RationalInterval(1-eps,1),RationalInterval(0,eps)


def digit_if_certified(n: int, horizon: int) -> int | None:
    """Return a certified hexadecimal digit of 16^(n-1) pi; otherwise None.

    This does not evaluate pi with an oracle. For n=0, the digit is the
    integer 3 of pi; for n>=1, these are its successive hex fractional digits.
    """
    iv=completed_interval(n,horizon)
    a,b=floor(16*iv.lo),floor(16*iv.hi)
    return a%16 if a==b else None


def source_weyl_error_over_pi_bound(h: int, n: int, horizon: int) -> Q:
    """Rational coefficient B in |e(h*low)-e(h*x)| <= 2*pi*B.

    x=16^(n-1)*pi; B=|h|*width. This is an error certificate, NOT
    cancellation of the finite rational exponential mean.
    """
    if not isinstance(h,int):
        raise ValueError('integer Fourier frequency required')
    return abs(h)*completed_interval(n,horizon).width
