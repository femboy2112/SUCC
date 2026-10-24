"""Finite rational Fourier enclosures from the polygon source.

No normality or asymptotic cancellation claim is made. The pi-specific entry
point constructs its source bracket itself, rather than trusting a caller's
claimed bracket. All outputs and error budgets are exact rational numbers.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial

from .pi_polygon_normality import (
    PolygonBracket, orbit_lipschitz_error_bound, polygon_pi_bracket,
)


def _integer(value, name, minimum=None, maximum=None):
    if type(value) is not int or (minimum is not None and value < minimum) or (
            maximum is not None and value > maximum):
        raise ValueError(f'invalid exact integer {name}')
    return value


def _rational(value, name):
    if type(value) not in (int, Q):
        raise ValueError(f'{name} must be an exact integer or Fraction')
    return Q(value)


def _unit_interval(lower, upper):
    lower, upper = max(Q(-1), lower), min(Q(1), upper)
    if lower > upper:
        raise ArithmeticError('Taylor enclosure contradicts unit range')
    return lower, upper


@dataclass(frozen=True)
class FourierEnclosure:
    source: str
    base: int
    frequency: int
    depth: int
    source_midpoint: Q
    polygon: PolygonBracket
    taylor_order: int
    real: tuple[Q, Q]
    imag: tuple[Q, Q]
    squared_modulus: tuple[Q, Q]
    source_transport_error: Q
    angle_rounding_error: Q
    cosine_taylor_error: Q
    sine_taylor_error: Q


def _character(turns, pi_bracket, order):
    # Reduce modulo a full turn before Taylor evaluation. The argument is in
    # [-pi,pi], so its rational midpoint has magnitude <4.
    turns = turns % 1
    if turns > Q(1, 2):
        turns -= 1
    center = (pi_bracket.lower+pi_bracket.upper)/2
    radius = (pi_bracket.upper-pi_bracket.lower)/2
    x = 2*center*turns
    cosine = sum(((-1)**j*x**(2*j)/factorial(2*j)
                  for j in range(order+1)), Q())
    sine = sum(((-1)**j*x**(2*j+1)/factorial(2*j+1)
                for j in range(order+1)), Q())
    # Lagrange remainders, with the missing odd/even coefficient included as
    # zero: all real derivatives of sin/cos have absolute value at most one.
    cosine_error = abs(x)**(2*order+2)/factorial(2*order+2)
    sine_error = abs(x)**(2*order+3)/factorial(2*order+3)
    angle_error = 2*abs(turns)*radius
    return (cosine, sine, cosine_error, sine_error, angle_error)


def _squared_modulus(real, imag):
    def square(interval):
        lo, hi = interval
        lower = Q() if lo <= 0 <= hi else min(lo*lo, hi*hi)
        return lower, max(lo*lo, hi*hi)
    re, im = square(real), square(imag)
    return re[0]+im[0], min(Q(1), re[1]+im[1])


def _enclose(source, midpoint, base, frequency, depth, bracket, order, error):
    _integer(base, 'base', 2)
    _integer(frequency, 'frequency')
    _integer(depth, 'depth', 1, 4096)
    _integer(order, 'taylor_order', 1, 128)
    if frequency == 0:
        raise ValueError('nonzero frequency required')
    c = s = ce = se = ae = Q()
    phase = (frequency*midpoint) % 1
    for _ in range(depth):
        cosine, sine, cosine_error, sine_error, angle_error = _character(phase, bracket, order)
        c += cosine; s += sine
        ce += cosine_error; se += sine_error; ae += angle_error
        phase = (base*phase) % 1
    c /= depth; s /= depth; ce /= depth; se /= depth; ae /= depth
    transport = orbit_lipschitz_error_bound(base, depth, error, 8*abs(frequency))
    real = _unit_interval(c-ce-ae-transport, c+ce+ae+transport)
    imag = _unit_interval(s-se-ae-transport, s+se+ae+transport)
    return FourierEnclosure(source, base, frequency, depth, midpoint, bracket,
        order, real, imag, _squared_modulus(real, imag), transport, ae, ce, se)


def pi_orbit_fourier_enclosure(base: int, frequency: int, depth: int,
        polygon_steps: int = 36, precision_bits: int = 256,
        taylor_order: int = 20) -> FourierEnclosure:
    """Enclose N^-1 sum_(j<N) exp(2*pi*i*h*b**j*pi).

    The returned interval pays BOTH pi's role as the orbit source and its role
    in the angle conversion. Correlation between those errors is not assumed
    away: the triangle inequality pays each separately.
    """
    bracket = polygon_pi_bracket(polygon_steps, precision_bits)
    midpoint = (bracket.lower+bracket.upper)/2
    return _enclose('polygon_pi', midpoint, base, frequency, depth, bracket,
                    taylor_order, (bracket.upper-bracket.lower)/2)


def rational_orbit_fourier_enclosure(phase, base: int, frequency: int, depth: int,
        polygon_steps: int = 36, precision_bits: int = 256,
        taylor_order: int = 20) -> FourierEnclosure:
    """Same instrument for an exact rational source; no source transport cost."""
    phase = _rational(phase, 'phase')
    bracket = polygon_pi_bracket(polygon_steps, precision_bits)
    return _enclose('exact_rational', phase, base, frequency, depth, bracket,
                    taylor_order, Q())
