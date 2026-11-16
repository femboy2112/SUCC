"""A bounded, source-certified moment instrument for one signed Weyl target.

This is Taylor approximation of an observable, not a normality theorem.
The source grid and angle intervals are imported from the canonical modules.
All certificate arithmetic is integer/Fraction; floats are display-only.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial
from typing import Iterable

from observational_succ.pi_succ_character_intervals import (
    characteristic_interval, machin_pi_interval,
)
from observational_succ.zero_anchored_haar import (
    PhaseGridCertificate, certified_phase_grid, verify_phase_grid,
)


def integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an exact integer >= {minimum}")
    return value


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def scale(x, a):
    if type(a) not in (int, Q):
        raise TypeError("exact scalar required")
    return (a*x[0], a*x[1]) if a >= 0 else (a*x[1], a*x[0])


def multiply(x, y):
    products = tuple(a*b for a in x for b in y)
    return min(products), max(products)


def unit_clip(x):
    lo, hi = max(Q(-1), x[0]), min(Q(1), x[1])
    if lo > hi:
        raise ArithmeticError("inconsistent unit-character enclosure")
    return lo, hi


def exponential_upper(t: Q) -> Q:
    """Rational e^t upper bound on 0<=t<1 from k!>=1, used for conditioning."""
    if not Q() <= t < 1:
        raise ValueError("this convenient upper bound requires 0<=t<1")
    # Sum through degree 4, then use ratio <= t/6 for all later terms.
    return sum((t**j/factorial(j) for j in range(5)), Q()) + (
        t**5/factorial(5))/(1-t/6)


@dataclass(frozen=True)
class MomentPacket:
    """Exact probability moments, separated by leading block.

    This low-level value object is not an authentication token. Construction
    by a caller does not certify that it comes from a probability law or the
    BBP source. Published source claims use certified_shell and re-acquisition
    through verify_packet_source.
    """
    count: int
    radix: int
    terms: int
    moments_by_digit: tuple[tuple[Q, ...], ...]


def packet_from_grid(points: tuple[int, ...], denominator: int, terms: int,
                     radix: int = 16) -> MomentPacket:
    integer(denominator, "grid denominator", 1)
    integer(radix, "radix", 2)
    integer(terms, "Taylor term count", 1)
    if terms > 24 or radix > 256:
        raise ValueError("declared finite implementation budget exceeded")
    if denominator % radix or not points or type(points) is not tuple:
        raise ValueError("nonempty aligned immutable grid required")
    if any(type(k) is not int or not 0 <= k < denominator for k in points):
        raise ValueError("invalid grid point")
    sub = denominator//radix
    accum = [[0 for _ in range(terms)] for _ in range(radix)]
    for k in points:
        a, residue = divmod(k, sub)
        # z=(k+1/2)/denominator, y=radix*z-a, u=2*y-1.
        numerator = 2*residue+1-sub
        power = 1
        for j in range(terms):
            accum[a][j] += power
            power *= numerator
    moments = tuple(tuple(Q(accum[a][j], len(points)*sub**j)
                          for j in range(terms)) for a in range(radix))
    return MomentPacket(len(points), radix, terms, moments)


def packet_from_exact_phases(phases: Iterable[Q], terms: int,
                             radix: int = 16) -> MomentPacket:
    phases = tuple(phases)
    integer(radix, "radix", 2)
    integer(terms, "Taylor term count", 1)
    if not phases or any(type(z) is not Q for z in phases):
        raise ValueError("nonempty exact rational phases required")
    accum = [[Q() for _ in range(terms)] for _ in range(radix)]
    for z in phases:
        z %= 1
        a = (radix*z).numerator//(radix*z).denominator
        u = 2*(radix*z-a)-1
        for j in range(terms):
            accum[a][j] += u**j/len(phases)
    return MomentPacket(len(phases), radix, terms,
                        tuple(tuple(row) for row in accum))


def signed_moment_coordinates(packet: MomentPacket, frequency: int = 1):
    """Q(zeta_16) coordinates for the q measured mixed moments (not powers)."""
    if packet.radix != 16 or type(frequency) is not int:
        raise ValueError("this exact field adapter has radix 16 only")
    out = []
    for j in range(packet.terms):
        coeff = [Q()]*8
        for a, row in enumerate(packet.moments_by_digit):
            k = (frequency*a) % 16
            coeff[k % 8] += (1 if k < 8 else -1)*row[j]
        out.append(tuple(coeff))
    return tuple(out)


def target_interval(packet: MomentPacket, frequency: int = 1,
                    phase_error: Q = Q(), pi_range=None):
    """Certified rectangle for the original target, with all four error bills.

    phase_error bounds circular displacement of the input points from the
    actual points. It is NOT an assertion that their separate digits agree.
    """
    if type(frequency) is not int or frequency == 0:
        raise ValueError("nonzero exact frequency required")
    if type(phase_error) is not Q or phase_error < 0:
        raise ValueError("nonnegative exact phase error required")
    canonical_pi = machin_pi_interval()
    if pi_range is None:
        pi_range = canonical_pi
    pl, pu = pi_range
    if not Q(3) < pl < pu < Q(22, 7):
        raise ValueError("authenticated pi interval expected")
    if not pl <= canonical_pi[0] < canonical_pi[1] <= pu:
        raise ValueError("supplied pi interval must enclose the canonical proof")
    re = im = (Q(), Q())
    for a, row in enumerate(packet.moments_by_digit):
        # e(h(a+1/2)/b) absorbs the e(h/(2b)) multiplier.
        clo, chi, slo, shi = characteristic_interval(
            Q(frequency*(2*a+1), 2*packet.radix), pi_range, order=12)
        real_part, imag_part = (clo, chi), (slo, shi)
        for j, moment in enumerate(row):
            coefficient = scale((pl**j, pu**j),
                                Q(frequency**j, packet.radix**j*factorial(j))*moment)
            k = j % 4
            cr, ci = ((real_part, imag_part) if k == 0 else
                      (scale(imag_part, -1), real_part) if k == 1 else
                      (scale(real_part, -1), scale(imag_part, -1)) if k == 2 else
                      (imag_part, scale(real_part, -1)))
            re = add(re, multiply(cr, coefficient))
            im = add(im, multiply(ci, coefficient))
    t = pu*abs(frequency)/packet.radix
    remainder = t**packet.terms/factorial(packet.terms)
    source_error = 2*pu*abs(frequency)*phase_error
    error = remainder+source_error
    return {
        "real": unit_clip((re[0]-error, re[1]+error)),
        "imag": unit_clip((im[0]-error, im[1]+error)),
        "truncated_real": re, "truncated_imag": im,
        "taylor_remainder": remainder, "source_phase_error": source_error,
        "coefficient_norm_upper": exponential_upper(t) if t < 1 else None,
        "anti_lock": (max(Q(), 1-re[1]-error), min(Q(2), 1-re[0]+error)),
    }


def certified_shell(start: int, terms: int = 6, depth: int = 6):
    integer(start, "shell start", 1)
    cert = certified_phase_grid(start, start, depth=depth, guard=16)
    packet = packet_from_grid(cert.points, cert.denominator, terms)
    interval = target_interval(packet, phase_error=Q(1, 2*cert.denominator))
    return cert, packet, interval


def verify_packet_source(cert: PhaseGridCertificate, packet: MomentPacket) -> bool:
    """Explicit full source re-acquisition; no caller-supplied authentication flag."""
    return (verify_phase_grid(cert) and packet == packet_from_grid(
        cert.points, cert.denominator, packet.terms, packet.radix))


def rational_display(interval, places=9):
    integer(places, "places", 1)
    scale_ = 10**places
    lo, hi = interval
    lower = lo.numerator*scale_//lo.denominator
    upper = -((-hi.numerator*scale_)//hi.denominator)
    def render(n):
        sign = "-" if n < 0 else ""
        n = abs(n)
        return f"{sign}{n//scale_}.{n%scale_:0{places}d}"
    return render(lower), render(upper)
