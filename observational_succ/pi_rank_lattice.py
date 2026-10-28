"""Source-faithful rank-r multiplicative lattice for the original BBP pi stream.

These are finite exact rational identities and rigorous upper envelopes.
They are not a normality proof or a second independently sampled source.

The genuine two-adic BBP clock, source numerator over Z_3, and real
winding memory live in different observable types. No local prime clock
is silently identified with an archimedean Fourier character.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
from math import isqrt, prod
from typing import Sequence

RADIX = 16
SOURCE_TAG = "signed-four-pole-zero-seed-original-BBP"


def authentic_r(n: int) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError("source index must be a positive integer")
    return (Q(4, 8*n-7) - Q(2, 8*n-4)
            - Q(1, 8*n-3) - Q(1, 8*n-2))


def canceled_r(n: int) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError("source index must be a positive integer")
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def original_state(n: int) -> Q:
    if type(n) is not int or not 0 <= n <= 500:
        raise ValueError("state time must be a bounded nonnegative integer")
    state = Q()
    for k in range(1, n+1):
        state = 16*state + authentic_r(k)
    return state


def pi_source_prefix(cutoff: int) -> Q:
    """Exact first cutoff terms of pi = sum_{j>=1}16**(1-j)*r(j)."""
    if type(cutoff) is not int or not 1 <= cutoff <= 500:
        raise ValueError("cutoff must be an integer in [1,500]")
    return sum((Q(16,16**j)*authentic_r(j) for j in range(1,cutoff+1)), Q())


def finite_green_tail(time: int, cutoff: int) -> Q:
    """Finite truncation T_time^(cutoff), with time>=1 and cutoff>=time.

    T_time = sum_{j>=1} 16**(-j) * r(time+j) and
    16**(time-1)*pi_prefix(cutoff) - U_time = T_time^(cutoff).
    """
    if type(time) is not int or type(cutoff) is not int or not 1 <= time <= cutoff <= 500:
        raise ValueError("require 1 <= time <= cutoff <= 500")
    return sum((Q(1, 16**j)*authentic_r(time+j)
                for j in range(1,cutoff-time+1)), Q())


def green_tail_upper(time: int) -> Q:
    """Inherited strict Green bound T_time < 1/[15(time+1)^2]."""
    if type(time) is not int or time < 1:
        raise ValueError("positive time required")
    return Q(1,15*(time+1)**2)


def _graded_axes(multipliers: Sequence[int], widths: Sequence[int]) -> tuple[tuple[int,...],tuple[int,...]]:
    q, w = tuple(multipliers), tuple(widths)
    if len(q) != len(w) or len(q) < 1:
        raise ValueError("rank r>=2 needs one width for each transverse multiplier")
    if any(type(b) is not int or b < 2 for b in q):
        raise ValueError("integer multipliers >=2 required")
    if any(type(M) is not int or not 1 <= M <= 10000 for M in w):
        raise ValueError("transverse widths must be positive integers <=10000")
    return q,w


def transverse_multiplier(index: Sequence[int], multipliers: Sequence[int]) -> int:
    idx = tuple(index)
    q = tuple(multipliers)
    if len(idx) != len(q) or any(type(m) is not int or m < 0 for m in idx):
        raise ValueError("nonnegative integral multi-index with matching multipliers required")
    if any(type(b) is not int or b < 2 for b in q):
        raise ValueError("integer multipliers >=2 required")
    return prod(b**m for b,m in zip(q,idx))


def selected_lattice_state(time_index: int, transverse_index: Sequence[int], multipliers: Sequence[int]) -> Q:
    """U_(n+1) transported by product q_j**m_j; time index n>=0."""
    if type(time_index) is not int or not 0 <= time_index <= 499:
        raise ValueError("source time index outside 0..499")
    return transverse_multiplier(transverse_index,multipliers)*original_state(time_index+1)


def flat_square(time_index: int, transverse_index: Sequence[int], multipliers: Sequence[int], axis: int) -> tuple[Q,Q]:
    """Two commuting paths around a horizontal--vertical rank-two square.

    Horizontal: V[n+1,m]=16 V[n,m]+Q_m*r(n+2).
    Vertical j: V[n,m+e_j]=q_j V[n,m].
    This is source consistency, NOT mixing or independent sampling.
    """
    q = tuple(multipliers)
    idx = tuple(transverse_index)
    if not 0 <= axis < len(q):
        raise ValueError("unknown transverse axis")
    base = selected_lattice_state(time_index,idx,q)
    scale=transverse_multiplier(idx,q)
    source=authentic_r(time_index+2)
    horizontal_then_vertical=q[axis]*(16*base+scale*source)
    vertical_then_horizontal=16*q[axis]*base+q[axis]*scale*source
    return horizontal_then_vertical,vertical_then_horizontal


def _ceil_sqrt_fraction(value: Q) -> int:
    """Smallest integer s with s*s>=value, no floating-point rounding."""
    if value < 0:
        raise ValueError("sqrt of negative rational")
    numerator,denominator = value.numerator,value.denominator
    ceil_num=(numerator+denominator-1)//denominator
    floor=isqrt(ceil_num)
    return floor if floor**2>=ceil_num else floor+1


def certified_rank_transport_bound(N: int, widths: Sequence[int], multipliers: Sequence[int], h: int) -> Q:
    """Sound *rational* bound on normalized rank-r pi-source phase difference.

    Derived from |e(t)-e(s)|<=min(2,2*pi*|t-s|), pi<22/7,
    T_(n+1)<1/(15(n+2)**2), and sum_n min(2,t/(n+2)**2)
    <=2*sqrt(2*t). Sum over arbitrary transverse multi-indices.

    The returned Fraction is an upper bound, not a computed difference.
    Complexity O(product widths). For analytic scaling see the proof dossier.
    """
    if type(N) is not int or N < 1:
        raise ValueError("positive horizontal width required")
    if type(h) is not int:
        raise ValueError("integer Fourier frequency required")
    q,w=_graded_axes(multipliers,widths)
    if h==0:
        return Q(0)
    n_states=prod(w)
    if n_states>100000:
        raise ValueError("exact enumeration budget 100000 transverse states")
    total=0
    for multi in product(*(range(M) for M in w)):
        scale=transverse_multiplier(multi,q)
        # 2t < 88*|h|*scale/105 (using pi<22/7)
        total+=_ceil_sqrt_fraction(Q(88*abs(h)*scale,105))
    return min(Q(2), Q(2*total,N*n_states))


def transverse_trace_recovery(values: Sequence[Q]) -> tuple[Q,Q,Q]:
    """Exact cochain homotopy: f(0) = average_m f(m) + weighted Delta_m f.

    Delta f(m)=f(m)-f(m+1). For several ranks tensor these operators;
    any mixed Delta correction is a separate, unproved normality obligation.
    """
    f=tuple(values)
    if not f or any(type(v) not in (int,Q) for v in f):
        raise ValueError("nonempty exact rational sequence required")
    M=len(f)
    average=sum((Q(v) for v in f),Q())/M
    correction=sum((Q(M-1-m,M)*(f[m]-f[m+1])
                    for m in range(M-1)),Q())
    assert average+correction==f[0]
    return average, correction, Q(f[0])
