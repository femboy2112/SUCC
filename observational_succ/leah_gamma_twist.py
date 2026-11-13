"""Exact centered BBP impulse instrument. No statistical theorem is assumed.

Definitions and paper bounds: research/2026-11-12/leah_gamma_twist/INVERSE_R0.md.
Uses the canonical source and existing sound character enclosure.
"""
from dataclasses import dataclass
from fractions import Fraction as Q

from .duck_bbp import forcing, source_tail_budget
from .oily_signed_certificate import character_enclosure


def _natural(n, minimum=0):
    if type(n) is not int or n < minimum:
        raise ValueError('ordinary integer in the declared range required')
    return n


def _rational(x):
    if type(x) not in (int, Q):
        raise ValueError('exact rational seed required')
    return Q(x)


@dataclass(frozen=True)
class CenteredPath:
    seed: Q
    residuals: tuple[Q, ...]
    impulses: tuple[int, ...]  # a_n, with a_0=nearest(seed)


def centered_path(horizon: int, seed=0) -> CenteredPath:
    """Keep nearest-integer residuals; impulses retain the unwrapped history."""
    _natural(horizon)
    seed = _rational(seed)
    anchor = (seed+Q(1, 2)).__floor__()
    residuals, impulses = [seed-anchor], [anchor]
    for n in range(1, horizon+1):
        raw = 16*residuals[-1]+forcing(n)
        a = (raw+Q(1, 2)).__floor__()
        residuals.append(raw-a)
        impulses.append(a)
    return CenteredPath(seed, tuple(residuals), tuple(impulses))


def shell_metrics(path: CenteredPath, B: int) -> dict:
    """Exact finite energies for B transitions from B through 2B."""
    _natural(B, 1)
    if len(path.residuals) <= 2*B:
        raise ValueError('path must include endpoint 2B')
    E = sum((v*v for v in path.residuals[B:2*B]), Q())
    D = sum(((Q(path.impulses[n])-forcing(n))**2
             for n in range(B+1, 2*B+1)), Q())
    integer_energy = sum(a*a for a in path.impulses[B+1:2*B+1])
    count = sum(a != 0 for a in path.impulses[B+1:2*B+1])
    source_error = sum((16*forcing(n)+forcing(n)**2
                        for n in range(B+1, 2*B+1)), Q())
    return {'B': B, 'residual_energy': E, 'innovation_energy': D,
            'integer_energy': integer_energy, 'impulse_count': count,
            'coercive_lower': 225*E-Q(15, 4),
            'coercive_upper': 289*E+Q(17, 4),
            'integer_energy_error': source_error}


def shell_antilock_interval(path: CenteredPath, B: int,
                            bits: int = 40, order: int = 14) -> tuple[Q, Q]:
    """Enclose the completed source orbit's anti-locking, at this finite B.

    The source is x+seed. Character enclosures use the rational residual,
    and |cos(2*pi*(u+T))-cos(2*pi*u)| <= 8*T since 2*pi<8.
    """
    _natural(B, 1)
    if len(path.residuals) < 2*B:
        raise ValueError('insufficient path')
    lower = upper = Q()
    for n in range(B, 2*B):
        cosine, _ = character_enclosure(path.residuals[n], bits, order)
        err = 8*source_tail_budget(n)
        lower += max(Q(), 1-cosine.upper-err)
        upper += min(Q(2), 1-cosine.lower+err)
    return lower/B, upper/B


def silent_response(path: CenteredPath, n: int, length: int) -> tuple[Q, Q]:
    """Exact finite response: v_n = sum 16^-j(a-r) +16^-L v_(n+L)."""
    _natural(n); _natural(length)
    if n+length >= len(path.residuals):
        raise ValueError('insufficient path')
    response = sum(((Q(path.impulses[n+j])-forcing(n+j))/16**j
                    for j in range(1, length+1)), Q())
    boundary = path.residuals[n+length]/16**length
    return response, boundary


def barycentric_packet(path: CenteredPath, B: int, resolution: int,
                       frequency: int = 1) -> tuple[tuple[Q, Q], ...]:
    """Finite weighted phase dictionary for the continuous carry/arrival filter.

    Sum weights is one. Its signed exponential sum approximates the rational
    Weyl mean within pi² h²/(512 q²). The source correction is retained exactly.
    """
    _natural(B, 1); _natural(resolution, 1)
    if type(frequency) is not int:
        raise ValueError('integer frequency required')
    if len(path.residuals) <= 2*B:
        raise ValueError('path must include endpoint 2B')
    q, h, terms = resolution, frequency, []
    for n in range(B, 2*B):
        u, y = path.residuals[n] % 1, path.residuals[n+1] % 1
        r = forcing(n+1)
        c = (16*u+r).__floor__()  # original literal carry, not centered a
        w = (q*y).__floor__()
        lam = q*y-w
        terms.append(((1-lam)/B, Q(h,16)*(c-r+Q(w,q))))
        terms.append((lam/B, Q(h,16)*(c-r+Q(w+1,q))))
    return tuple(terms)
