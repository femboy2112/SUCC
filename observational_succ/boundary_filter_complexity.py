"""Finite, outward-rational certificates for a BBP boundary Hankel matrix.

Positive certificates exclude short constant-coefficient recurrences on the
specified window only. They do not certify an asymptotic spectral gap or normality.
The source is duck_bbp's unchanged four-pole, zero-seeded source. Machin/Taylor
character enclosures are reused from pi_source_genesis, not reinvented here.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from .duck_bbp import forcing, source_tail_budget
from .pi_source_genesis import ComplexBox, character_interval


def _nat(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def sqrt_upper(value, bits=60):
    """Outward dyadic square root; integer arithmetic only."""
    if type(value) not in (int, Q) or value < 0:
        raise ValueError("nonnegative exact rational required")
    _nat(bits, "bits", 1)
    value = Q(value)
    scale = 1 << bits
    root = isqrt(value.numerator * scale * scale // value.denominator)
    if Q(root * root, scale * scale) < value:
        root += 1
    return Q(root, scale)


def completed_source_interval(horizon):
    """Strict enclosure of x=pi/16; positive omitted tail is proved elsewhere."""
    _nat(horizon, "horizon", 1)
    partial = sum((forcing(k) / 16**k for k in range(1, horizon + 1)), Q())
    return partial, partial + source_tail_budget(horizon) / 16**horizon


def _scaled_interval(interval, factor):
    a, b = interval
    return (factor*a, factor*b) if factor >= 0 else (factor*b, factor*a)


def _conjugate(box):
    return ComplexBox(box.real_low, box.real_high, -box.imag_high, -box.imag_low)


def gram_from_phase_intervals(phases, degree, harmonic=1, *, bits=72):
    """Enclose H*H/M, H[n,j]=e(harmonic*16**j*phase[n]).

    Generic input, with no source-authentication claim. Phase intervals are real
    lifts; crossing a circle seam is allowed. Gershgorin supplies a rigorous
    lower bound, with zero meaning INCONCLUSIVE, not rank deficient.
    """
    _nat(degree, "degree")
    _nat(bits, "bits", 16)
    if degree > 16 or type(harmonic) is not int or harmonic == 0:
        raise ValueError("degree <= 16 and nonzero integer harmonic required")
    phases = tuple(phases)
    if not phases:
        raise ValueError("nonempty phase window required")
    for pair in phases:
        if len(pair) != 2 or any(type(x) not in (int, Q) for x in pair) or pair[0] > pair[1]:
            raise ValueError("ordered exact rational phase intervals required")
    size = degree + 1
    one = ComplexBox(Q(1), Q(1), Q(), Q())
    matrix = [[one if j == k else None for k in range(size)] for j in range(size)]
    bounds = [[Q() for _ in range(size)] for _ in range(size)]
    for j in range(size):
        for k in range(j + 1, size):
            frequency = harmonic * (16**k - 16**j)
            total = ComplexBox(Q(), Q(), Q(), Q())
            for interval in phases:
                low, high = _scaled_interval(interval, frequency)
                total += character_interval(low, high, bits=bits).outward(bits)
            box = ComplexBox(*(x / len(phases) for x in (
                total.real_low, total.real_high, total.imag_low, total.imag_high))).outward(bits)
            matrix[j][k], matrix[k][j] = box, _conjugate(box)
            bounds[j][k] = bounds[k][j] = min(Q(1), sqrt_upper(box.modulus_squared_upper(), bits))
    lower = max(Q(), Q(1) - max(map(sum, bounds)))
    return tuple(tuple(row) for row in matrix), lower


@dataclass(frozen=True)
class BoundaryRankCertificate:
    start: int
    length: int
    degree: int
    harmonic: int
    horizon: int
    source_interval: tuple[Q, Q]
    gram: tuple[tuple[ComplexBox, ...], ...]
    eigenvalue_lower: Q

    @property
    def verdict(self):
        return "FULL_COLUMN_RANK" if self.eigenvalue_lower > 0 else "INCONCLUSIVE"


def certify_bbp_boundary_rank(start, length, degree, *, harmonic=1, lookahead=10, bits=72):
    """Certify the literal-zero completed BBP window, with a paid common horizon."""
    _nat(start, "start")
    _nat(length, "length", 1)
    _nat(degree, "degree")
    _nat(lookahead, "lookahead")
    horizon = max(1, start + length - 1 + degree + lookahead)
    if horizon > 8192:
        raise ValueError("finite implementation horizon budget exceeded")
    source = completed_source_interval(horizon)
    phases = [_scaled_interval(source, 16**n) for n in range(start, start + length)]
    gram, lower = gram_from_phase_intervals(phases, degree, harmonic, bits=bits)
    return BoundaryRankCertificate(start, length, degree, harmonic, horizon, source, gram, lower)
