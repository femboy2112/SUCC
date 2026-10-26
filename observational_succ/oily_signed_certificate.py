"""Sound finite selected Fourier/Gram enclosures; no asymptotic certificate.

The orbit comes from the existing literal BBP carry adapter. The analytic
circle character uses a separately proved Machin arctangent enclosure for pi,
not a decimal pi constant or an assumed digit distribution. All certification
arithmetic is integer/Fraction arithmetic. Signed cross-block terms survive.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial

from .pi_lag_carry import bbp_carry_path


def _integer(value, minimum=None):
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError("ordinary integer in the declared domain required")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


@dataclass(frozen=True)
class Interval:
    lower: Q
    upper: Q

    def __post_init__(self):
        object.__setattr__(self, "lower", _rational(self.lower))
        object.__setattr__(self, "upper", _rational(self.upper))
        if self.lower > self.upper:
            raise ValueError("reversed enclosure")

    def __add__(self, other):
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def __sub__(self, other):
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, factor):
        factor = _rational(factor)
        a, b = self.lower * factor, self.upper * factor
        return Interval(min(a, b), max(a, b))

    def square(self):
        lo = 0 if self.lower <= 0 <= self.upper else min(self.lower**2, self.upper**2)
        return Interval(lo, max(self.lower**2, self.upper**2))

    def contains(self, rational):
        return self.lower <= _rational(rational) <= self.upper


ZERO = Interval(Q(), Q())


def _atan_reciprocal_enclosure(denominator, terms):
    s = sum((Q((-1)**j, (2*j+1)*denominator**(2*j+1))
             for j in range(terms)), Q())
    next_sum = s + Q((-1)**terms, (2*terms+1)*denominator**(2*terms+1))
    return Interval(min(s, next_sum), max(s, next_sum))


@lru_cache(maxsize=32, typed=True)
def machin_pi_enclosure(terms=32):
    """Alternating series + pi=16 atan(1/5)-4 atan(1/239).

    tan(4 atan(1/5))=120/119, and subtracting atan(1/239)
    gives tangent 1. The angle is in (0,pi/2), proving the identity.
    """
    _integer(terms, 1)
    return (_atan_reciprocal_enclosure(5, terms).scale(16)
            - _atan_reciprocal_enclosure(239, terms).scale(4))


def _floor_grid(value, bits):
    return Q((value * (1 << bits)).__floor__(), 1 << bits)


def _outward(lo, hi, bits):
    scale = 1 << bits
    return Interval(Q((lo*scale).__floor__(), scale),
                    Q(-(-hi*scale).__floor__(), scale))


@lru_cache(maxsize=2048, typed=True)
def character_enclosure(phase, bits=48, order=16):
    """Rectangular enclosure of exp(2*pi*i*phase), modulo one.

    Center angle and endpoints are rounded outward on a dyadic grid.
    The sine/cosine Lagrange remainder uses |derivative|<=1 for real
    arguments; the angle perturbation uses their 1-Lipschitz property.
    Accuracy is finite only. Increasing bits without increasing order
    need not improve the Taylor remainder.
    """
    phase = _rational(phase)
    _integer(bits, 8)
    _integer(order, 1)
    phase -= (phase + Q(1, 2)).__floor__()
    if phase == 0:
        return Interval(1, 1), ZERO
    if phase == Q(-1, 2):
        return Interval(-1, -1), ZERO
    if phase == Q(1, 4):
        return ZERO, Interval(1, 1)
    if phase == Q(-1, 4):
        return ZERO, Interval(-1, -1)
    pi = machin_pi_enclosure(max(16, bits//4 + 4))
    middle = (pi.lower + pi.upper)/2
    p = _floor_grid(phase, bits)
    angle = _floor_grid(2*middle*p, bits)
    angle_error = (2*pi.upper + 1)/2**bits + abs(p)*(pi.upper-pi.lower)
    cosine = sum(((-1)**j*angle**(2*j)/factorial(2*j)
                  for j in range(order+1)), Q())
    sine = sum(((-1)**j*angle**(2*j+1)/factorial(2*j+1)
                for j in range(order+1)), Q())
    ce = abs(angle)**(2*order+2)/factorial(2*order+2) + angle_error
    se = abs(angle)**(2*order+3)/factorial(2*order+3) + angle_error
    return (_outward(max(Q(-1), cosine-ce), min(Q(1), cosine+ce), bits),
            _outward(max(Q(-1), sine-se), min(Q(1), sine+se), bits))


def signed_sum_enclosure(phases, frequency=1, bits=48, order=16):
    _integer(frequency)
    real, imag = ZERO, ZERO
    for phase in phases:
        r, i = character_enclosure(frequency*_rational(phase), bits, order)
        real, imag = real+r, imag+i
    return real, imag


def squared_modulus_enclosure(rectangle):
    real, imag = rectangle
    return real.square() + imag.square()


def authentic_signed_certificate(horizon, frequency=1, block_size=16,
                                 bits=48, order=16):
    """Finite exact-head instrument for the actual source, including all signs.

    Cross = |sum z_n|^2 - sum_blocks |sum_block z_n|^2.
    It is a real SIGNED ordered off-diagonal sum, not a positive energy.
    Authentication applies only to this finite prefix. No o(N) is asserted.
    """
    _integer(horizon, 1)
    _integer(frequency)
    _integer(block_size, 1)
    if frequency == 0:
        raise ValueError("selected nonzero integer frequency required")
    path = bbp_carry_path(horizon)
    phases = path.states[1:]
    blocks = tuple(signed_sum_enclosure(phases[j:j+block_size], frequency, bits, order)
                   for j in range(0, horizon, block_size))
    real = sum((b[0] for b in blocks), ZERO)
    imag = sum((b[1] for b in blocks), ZERO)
    energy = squared_modulus_enclosure((real, imag))
    diagonal = sum((squared_modulus_enclosure(b) for b in blocks), ZERO)
    cross = energy - diagonal
    return {"horizon": horizon, "frequency": frequency, "block_size": block_size,
            "bits": bits, "order": order, "real": real, "imag": imag,
            "squared_modulus": energy, "normalized_squared_modulus": energy.scale(Q(1,horizon**2)),
            "within_block_energy": diagonal, "signed_cross_block": cross,
            "carries": path.carries, "infinite_cancellation_proved": False}
