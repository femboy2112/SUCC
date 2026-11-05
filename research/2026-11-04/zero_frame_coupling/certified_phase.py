"""Rational phase enclosure, audited additive extraction from PR #505.

Source: 00b6385b6e7420b5e108e6766dcf2f7dda875f59,
research/2026-11-04/critical_chirp_source/signed_probe.py.
Only named arithmetic functions are copied. This is shared implementation
provenance, not an independent trigonometric implementation.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
GRID = 1 << 80
OUTPUT = 1 << 60
CHAR_ERROR = F(1, 1 << 50)

def forcing(n: int) -> F:
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)

def critical_schedule(A: int, h: int) -> tuple[int, int]:
    """Certify floor(log_16(A^2 log A / |h|)) for dyadic A."""
    if type(A) is not int or A < 2 or A & (A-1) or type(h) is not int or not h:
        raise ValueError("dyadic A>=2 and nonzero integer h required")
    k = A.bit_length()-1
    terms = 40
    low = 2*sum((F(1, (2*j+1)*3**(2*j+1)) for j in range(terms)), F(0))
    high = low+F(9, 4*(2*terms+1)*3**(2*terms+1))
    low *= k*A*A
    high *= k*A*A
    H, depth = abs(h), 0
    if H > low:
        raise ValueError("no certified nonnegative depth")
    while 16*H <= low:
        H *= 16
        depth += 1
    if not H <= low <= high < 16*H:
        raise ArithmeticError("increase log precision to resolve radix boundary")
    return depth, H

def arctan_bounds(q: int, terms: int = 48) -> tuple[F, F]:
    s = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(terms)), F(0))
    other = s+F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(s, other), max(s, other)

@lru_cache(maxsize=1)
def pi_grid() -> F:
    a, b = arctan_bounds(5)
    c, d = arctan_bounds(239)
    low, high = 16*a-4*d, 16*b-4*c
    middle = (low+high)/2
    p = F((middle.numerator*GRID)//middle.denominator, GRID)
    assert 3 < low < high < F(22, 7)
    assert max(abs(p-low), abs(p-high)) < F(2, GRID)
    return p

def character_grid(phase: F, phase_radius: F = F(0)) -> tuple[int, int]:
    """A point within CHAR_ERROR of e(phase +/- phase_radius)."""
    if phase_radius < 0:
        raise ValueError("negative enclosure radius")
    x = (F(phase)+F(1, 2)) % 1-F(1, 2)
    q = F((x.numerator*GRID)//x.denominator, GRID)
    angle = 2*pi_grid()*q
    assert abs(angle) < 4
    # Degree 47 Taylor polynomial, recurrence independent of libm/mpmath.
    real, imag, term = F(0), F(0), F(1)
    for j in range(48):
        if j:
            term *= angle/j
        if j % 4 == 0:
            real += term
        elif j % 4 == 1:
            imag += term
        elif j % 4 == 2:
            real -= term
        else:
            imag -= term
    # Two component Lagrange errors, phase/pi rounding, output rounding.
    error = F(14, GRID)+2*F(4**48, factorial(48))+F(2, OUTPUT)+7*phase_radius
    if error > CHAR_ERROR:
        raise ArithmeticError("phase enclosure exceeds fixed character budget")
    return ((real.numerator*OUTPUT)//real.denominator,
            (imag.numerator*OUTPUT)//imag.denominator)

def tail_interval(n: int, terms: int = 24) -> tuple[F, F]:
    low = sum((forcing(n+k)/16**k for k in range(1, terms+1)), F(0))
    high = low+forcing(n+terms+1)*F(1, 15*16**terms)
    return low, high

def outward_decimal(x: F, places: int = 9, upper: bool = False) -> str:
    scale = 10**places
    scaled = x*scale
    v = scaled.numerator//scaled.denominator
    if upper and scaled != v:
        v += 1
    sign = "-" if v < 0 else ""
    v = abs(v)
    return f"{sign}{v//scale}.{v%scale:0{places}d}"

