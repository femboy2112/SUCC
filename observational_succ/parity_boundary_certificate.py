"""Exact finite payments for the BBP parity observer.

The paper proofs are in research/2026-11-09/cayley_source_observer/.
All enclosure and error-budget arithmetic here is rational.  The optional
Fourier evaluator also encloses sine by rational Taylor bounds; it does not
treat floating-point quadrature as a certificate.  Identifying the original
BBP sum with pi is the existing classical source dependency.

These instruments transfer a statistic; they do not prove its decay.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, floor

from observational_succ import duck_bbp
from observational_succ.selected_orbit import SelectedOrbit


def _natural(n: int, name: str, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return n


def _rational(x) -> Q:
    if type(x) not in (int, Q):
        raise TypeError("exact int or Fraction required")
    return Q(x)


@dataclass(frozen=True)
class PhaseEnclosure:
    """Closed real-lift enclosure; its circle image may cross any seam."""
    lo: Q
    hi: Q

    def __post_init__(self):
        object.__setattr__(self, 'lo', _rational(self.lo))
        object.__setattr__(self, 'hi', _rational(self.hi))
        if self.lo > self.hi:
            raise ValueError("empty enclosure")

    @property
    def center(self) -> Q:
        return (self.lo + self.hi) / 2

    @property
    def radius(self) -> Q:
        return (self.hi - self.lo) / 2

    def digit(self) -> int | None:
        """Certify the whole enclosure, without comparing reduced endpoints."""
        a, b = floor(16*self.lo), floor(16*self.hi)
        return a % 16 if a == b else None


def source_phase_enclosures(A: int, depth: int = 8) -> tuple[PhaseEnclosure, ...]:
    """Original-zero completed phases on A<=n<2A, local horizon n+depth."""
    _natural(A, 'A', 1)
    _natural(depth, 'depth')
    orbit = SelectedOrbit()
    out = []
    for n in range(A, 2*A):
        u = orbit.state(n)
        lo, hi = duck_bbp.tail_interval(n, depth)
        out.append(PhaseEnclosure(u+lo, u+hi))
    return tuple(out)


def common_horizon_enclosures(A: int, horizon: int) -> tuple[PhaseEnclosure, ...]:
    """Same source prefix for the entire epoch, horizon>=2A-1.

    The lower endpoints modulo one form an EXACT times-16 orbit.  Unlike
    raw U_n, they already include all source terms through this horizon.
    """
    _natural(A, 'A', 1)
    _natural(horizon, 'horizon', 2*A-1)
    p_lo, p_hi = duck_bbp.pi_interval(horizon)
    p_lo, p_hi = p_lo/16, p_hi/16
    out = []
    for n in range(A, 2*A):
        lo, hi = 16**n*p_lo, 16**n*p_hi
        deck = floor(lo)
        out.append(PhaseEnclosure(lo-deck, hi-deck))
    return tuple(out)


def certified_source_digit(n: int, initial_depth: int = 8,
                           max_depth: int = 4096) -> tuple[int, int, PhaseEnclosure]:
    """Adaptive exact digit certificate with an explicit finite budget.

    Irrationality proves eventual termination without an a-priori rate if
    the budget is removed; a finite exhausted budget raises RuntimeError.
    No assertion is used as a correctness gate (Python -O is safe).
    """
    _natural(n, 'n')
    _natural(initial_depth, 'initial_depth')
    _natural(max_depth, 'max_depth', initial_depth)
    u = SelectedOrbit().state(n)
    depth = initial_depth
    while True:
        lo, hi = duck_bbp.tail_interval(n, depth)
        iv = PhaseEnclosure(u+lo, u+hi)
        digit = iv.digit()
        if digit is not None:
            return digit, depth, iv
        if depth == max_depth:
            raise RuntimeError("digit not certified within source-horizon budget")
        depth = min(max_depth, max(depth+1, 2*depth))


def distance_to_digit_boundary(t: Q) -> Q:
    """Circle distance to all sixteen cuts, including 0 and the Cayley pole."""
    s = (16*_rational(t)) % 1
    return min(s, 1-s)/16


def fejer_weights(H: int) -> tuple[tuple[int, Q], ...]:
    _natural(H, 'H')
    return tuple((m, 1-Q(m, H+1)) for m in range(8, H+1, 16))


def fejer_lipschitz(H: int) -> Q:
    """Exact circle Lipschitz norm of sigma_H f, attained at every integer."""
    _natural(H, 'H')
    k = (H+8)//16
    return 64*k-Q(512*k*k, H+1)


def fejer_error_budget(enclosures, H: int, delta: Q) -> dict:
    """Rigorous bound on mean f(true phase) minus sigma_H f(center).

    Bhat counts intervals that may hit a delta-neighborhood of a digit cut.
    The finite Fourier approximation uses a nonnegative Fejer kernel, so
    both the truncation and source-transfer payments may be clipped at 2.
    The rational tail bound follows from sin(pi*u)>=2u on [0,1/2].
    """
    enclosures = tuple(enclosures)
    if not enclosures or any(type(iv) is not PhaseEnclosure for iv in enclosures):
        raise ValueError("a nonempty sequence of PhaseEnclosure objects is required")
    _natural(H, 'H')
    delta = _rational(delta)
    if not 0 < delta <= Q(1, 32):
        raise ValueError("0 < delta <= 1/32 required")
    N = len(enclosures)
    count = sum(distance_to_digit_boundary(iv.center) <= delta+iv.radius
                for iv in enclosures)
    L = fejer_lipschitz(H)
    transfer = sum((min(Q(2), L*iv.radius) for iv in enclosures), Q())/N
    tail = 1/((H+1)*delta)
    raw = Q(2*count, N)+tail+transfer
    return {
        'sample_count': N, 'cutoff': H, 'delta': delta,
        'possible_boundary_count': count,
        'boundary_payment': Q(2*count, N),
        'fejer_tail_payment': tail,
        'lipschitz_constant': L,
        'mean_radius': sum((iv.radius for iv in enclosures), Q())/N,
        'clipped_source_payment': transfer,
        'raw_error_bound': raw, 'error_bound': min(Q(2), raw),
    }


@lru_cache(maxsize=1)
def _pi_enclosure() -> tuple[Q, Q]:
    # This is the authenticated BBP interval, not an unrelated pi oracle.
    return duck_bbp.pi_interval(24)


def sine_turns_enclosure(t: Q, bits: int = 48, terms: int = 16) -> tuple[Q, Q]:
    """Enclose sin(2*pi*t) using dyadic argument rounding and Taylor's theorem."""
    _natural(bits, 'bits', 16)
    _natural(terms, 'terms', 1)
    t = _rational(t) % 1
    if t > Q(1, 2):
        t -= 1
    plo, phi = _pi_enclosure()
    a, b = sorted((2*t*plo, 2*t*phi))
    scale = 2**bits
    # Outward dyadic rounding prevents denominator growth with BBP time.
    a = Q(floor(a*scale), scale)
    b = Q(-floor(-b*scale), scale)
    y, radius = (a+b)/2, (b-a)/2
    if abs(y) > Q(22, 7):
        raise ArithmeticError("Taylor argument escaped proved compact range")
    polynomial = sum(((-1)**j*y**(2*j+1)/factorial(2*j+1)
                      for j in range(terms)), Q())
    remainder = Q(22, 7)**(2*terms+1)/factorial(2*terms+1)
    error = radius+remainder  # sine is 1-Lipschitz
    return max(Q(-1), polynomial-error), min(Q(1), polynomial+error)


def fejer_mean_enclosure(points, H: int, bits: int = 48,
                         terms: int = 16) -> tuple[Q, Q]:
    """Rational enclosure of the finite Fejer polynomial's empirical mean."""
    points = tuple(_rational(t) for t in points)
    if not points:
        raise ValueError("nonempty points required")
    weights = fejer_weights(H)
    plo, phi = _pi_enclosure()
    total_lo = total_hi = Q()
    for t in points:
        for m, w in weights:
            slo, shi = sine_turns_enclosure(m*t, bits, terms)
            factors = (slo/plo, slo/phi, shi/plo, shi/phi)
            coefficient = 32*w/m
            total_lo += coefficient*min(factors)
            total_hi += coefficient*max(factors)
    return total_lo/len(points), total_hi/len(points)


def circle_distance(a: Q, b: Q = Q()) -> Q:
    d = (_rational(a)-_rational(b)) % 1
    return min(d, 1-d)


def stationary_boundary_recursion(phases, depth: int) -> dict:
    """Exact open-ball recursion for a consecutive rational times-16 orbit.

    Supply N+1 phases, including the final endpoint.  After folding by 8,
    radius r_j=1/(4*16^j) corresponds to distance 1/(32*16^j) from the
    original digit cuts.  All fourteen other preimage fibers are retained
    as a nonnegative omitted-mass term.  The result certifies only this
    finite orbit and the displayed recurrence, not asymptotic symmetry.
    """
    _natural(depth, 'depth')
    phases = tuple(_rational(t) % 1 for t in phases)
    if len(phases) < 2:
        raise ValueError("need a nonempty orbit plus its final endpoint")
    if any(16*a % 1 != b for a, b in zip(phases, phases[1:])):
        raise ValueError("phases are not a consecutive times-16 orbit")
    us = tuple(8*t % 1 for t in phases)
    sample, N = us[:-1], len(us)-1

    def hit(u, r, center=Q()):
        return circle_distance(u, center) < r  # OPEN at r_0=1/4

    rows = []
    masses = []
    contrasts = []
    for j in range(depth+1):
        r = Q(1, 4*16**j)
        a = Q(sum(hit(u, r) for u in sample), N)
        b = Q(sum(hit(u, r, Q(1, 2)) for u in sample), N)
        masses.append(a+b)
        contrasts.append(a-b)
        if j < depth:
            e = Q(int(hit(us[-1], r))-int(hit(us[0], r)), N)
            rnext = r/16
            other = Q(sum(hit(16*u % 1, r)
                          and not hit(u, rnext)
                          and not hit(u, rnext, Q(1, 2)) for u in sample), N)
            rows.append({'level': j, 'radius': r, 'boundary_mass': a+b,
                         'signed_half_turn_contrast': a-b,
                         'endpoint': e, 'other_fourteen_fibers': other})
    for j, row in enumerate(rows):
        row['next_boundary_mass'] = masses[j+1]
        row['identity_residual'] = masses[j+1] - (
            (masses[j]+contrasts[j])/2 + row['endpoint']
            - row['other_fourteen_fibers'])
    contrast = sum((abs(contrasts[j])/2**(depth-j)
                    for j in range(depth)), Q())
    upper = masses[0]/2**depth+contrast+Q(2, N)*(1-Q(1, 2**depth))
    return {'sample_count': N, 'depth': depth, 'rows': rows,
            'boundary_mass': masses[-1], 'initial_boundary_mass': masses[0],
            'digit_boundary_radius': Q(1, 32*16**depth),
            'absolute_contrast_payment': contrast,
            'upper_bound': min(Q(1), upper)}
