"""Outward integer intervals for the authentic BBP collision observable.

No supplied digits, floating point, or asymptotic inference. Machin's formula
is an independent source instrument; BBP's exact identity selects y_0=0.
See PI_LAG_CARRY_RIGIDITY.md for all error and binary-splitting proofs.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


def _nat(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return n


def _atan_split(q: int, a: int, b: int) -> tuple[int, int, int]:
    """Return (P,Q,T): P=q^(2(b-a)), Q=prod(2k+1).

    T=sum((-1)^k q^(2(b-1-k)) Q/(2k+1), a<=k<b).
    """
    if b-a == 1:
        return q*q, 2*a+1, (-1 if a % 2 else 1)
    mid = (a+b)//2
    p1, q1, t1 = _atan_split(q, a, mid)
    p2, q2, t2 = _atan_split(q, mid, b)
    return p1*p2, q1*q2, t1*q2*p2+t2*q1


def atan_dyadic_bounds(q: int, bits: int) -> tuple[int, int]:
    """Integer endpoints enclosing 2^bits atan(1/q), strictly.

    N=ceil(bits/(2 floor(log2 q))) makes the alternating remainder
    smaller than 2^-bits; rounding adds less than one unit.
    """
    _nat(q, 2)
    _nat(bits, 1)
    rate = 2*(q.bit_length()-1)
    terms = max(1, (bits+rate-1)//rate)
    p, denominator, numerator = _atan_split(q, 0, terms)
    partial_floor = (numerator*q << bits)//(denominator*p)
    return partial_floor-1, partial_floor+2


def machin_dyadic_bounds(bits: int) -> tuple[int, int]:
    """Enclose 2^bits*pi using pi=16 atan(1/5)-4 atan(1/239)."""
    a, b = atan_dyadic_bounds(5, bits)
    c, d = atan_dyadic_bounds(239, bits)
    return 16*a-4*d, 16*b-4*c


def tail_dyadic_bounds(n: int, bits: int, terms: int = 20) -> tuple[int, int]:
    """Outward bounds on 2^bits*t_n, including positive residual tail."""
    _nat(n)
    _nat(bits, 1)
    _nat(terms, 1)
    scale = 1 << bits
    lower = 0
    for j in range(1, terms+1):
        k = n+j
        numerator = 120*k*k-89*k+16
        denominator = (2*k-1)*(4*k-1)*(8*k-7)*(8*k-3)
        lower += (scale*numerator)//(denominator << (4*j))
    # Exact residual is 16^-terms*t_(n+terms), strictly below beta bound.
    denominator = ((8*(n+terms)+1)*(8*(n+terms)+2)) << (4*terms)
    residual_ceiling = (scale+denominator-1)//denominator
    return lower, lower+terms+residual_ceiling


@dataclass(frozen=True)
class SourceIntervals:
    start: int
    bits: int
    bounds: tuple[tuple[int, int], ...]
    pi_bits: int
    pi_width_units: int


def source_intervals(start: int, length: int, bits: int = 80,
                     tail_terms: int = 20) -> SourceIntervals:
    """Enclose y_start,...,y_(start+length-1), start>=1.

    Refuses any circular boundary crossing. Precision can then be increased;
    an ambiguous interval is never converted to a phase or a count.
    """
    _nat(start, 1)
    _nat(length, 1)
    _nat(bits, 1)
    _nat(tail_terms, 1)
    last = start+length-1
    pi_bits = 4*(last-1)+bits+8
    pi_lo, pi_hi = machin_dyadic_bounds(pi_bits)
    scale = 1 << bits
    result = []
    for n in range(start, last+1):
        shift = pi_bits-4*(n-1)-bits
        # Outward integer enclosure of 2^bits*16^(n-1)*pi.
        lo = (pi_lo >> shift) & (scale-1)
        hi = ((pi_hi >> shift) & (scale-1))+1
        if hi < lo:
            hi += scale
        tail_lo, tail_hi = tail_dyadic_bounds(n, bits, tail_terms)
        lo -= tail_hi
        hi -= tail_lo
        quotient = lo//scale
        lo -= quotient*scale
        hi -= quotient*scale
        if not 0 <= lo <= hi < scale:
            raise ArithmeticError("source interval crosses circle boundary; refine")
        result.append((lo, hi))
    return SourceIntervals(start, bits, tuple(result), pi_bits, pi_hi-pi_lo)


def _validated_bounds(sample: SourceIntervals) -> tuple[list[tuple[int, int]], int]:
    _nat(sample.bits, 1)
    scale = 1 << sample.bits
    if not sample.bounds or any(type(a) is not int or type(b) is not int
                               or not 0 <= a <= b < scale
                               for a, b in sample.bounds):
        raise ValueError("nonempty valid outward integer intervals required")
    return sorted(sample.bounds), scale


def certified_pair_count(sample: SourceIntervals, cells: int) -> int:
    """Certify ordered ||y_s-y_t||<=1/cells, including all diagonals.

    Counts with certainly-close and possibly-close directed arc tests must
    agree. Interval ordering must also be certified strictly. Equality at a
    threshold is correctly unresolved unless the endpoints certify it.
    """
    _nat(cells, 3)
    ordered, scale = _validated_bounds(sample)
    if any(ordered[i][1] >= ordered[i+1][0]
           for i in range(len(ordered)-1)):
        raise ArithmeticError("phase ordering unresolved; refine")
    n = len(ordered)
    doubled = ordered+[(a+scale, b+scale) for a, b in ordered]
    counts = []
    for certain in (True, False):
        j = 1
        forward = 0
        for i in range(n):
            j = max(j, i+1)
            while j < i+n:
                distance = (doubled[j][1]-doubled[i][0] if certain
                            else doubled[j][0]-doubled[i][1])
                if distance*cells > scale:
                    break
                j += 1
            forward += j-i-1
        counts.append(n+2*forward)
    if counts[0] != counts[1]:
        raise ArithmeticError(f"close-pair decisions unresolved: {counts}; refine")
    return counts[0]


def certified_cell_counts(sample: SourceIntervals, cells: int) -> dict[int, int]:
    _nat(cells, 1)
    ordered, scale = _validated_bounds(sample)
    counts: dict[int, int] = {}
    for lo, hi in ordered:
        a, b = lo*cells//scale, hi*cells//scale
        if a != b:
            raise ArithmeticError("cell boundary unresolved; refine")
        counts[a] = counts.get(a, 0)+1
    return counts


def canonical_cells(p: int) -> int:
    """Predetermined c=2/5 schedule, computed without logarithms."""
    _nat(p, 2)
    cells = 1
    while (16*cells)**5 <= p*p:
        cells *= 16
    return cells


def interval_contains(sample: SourceIntervals, offset: int, value: Fraction) -> bool:
    lo, hi = sample.bounds[offset]
    return lo <= value*(1 << sample.bits) <= hi
