"""Forward Fibonacci observer of the authentic BBP finite local clock.

The ternary input is the cleared forcing numerator A(n), never U_n mod 3^b.
This map factors through the recovered source clock and supplies no real-phase
cancellation. The all-depth mathematical statement is in THEOREMS.md; imported
finite source codecs intentionally cap binary/ternary depths at 32/15.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, gcd, lcm

from observational_succ.bbp_primal_recursive_geometry import (
    binary_code,
    binary_inverse_from_gates,
    regularized_ternary_code,
    ternary_inverse_from_lifts,
)
from observational_succ.duck_bbp import forcing

T = (
    (16, 32, 24, 8, 1),
    (8, 20, 18, 7, 1),
    (4, 12, 13, 6, 1),
    (2, 7, 9, 5, 1),
    (1, 4, 6, 4, 1),
)


def integer(value, name, minimum=0, maximum=None):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name}: integer >= {minimum} required")
    if maximum is not None and value > maximum:
        raise ValueError(f"{name}: finite implementation cap is {maximum}")
    return value


def multiply(a, b, modulus):
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) % modulus
                       for col in zip(*b)) for row in a)


def power(exponent, modulus):
    integer(exponent, "forward exponent")
    integer(modulus, "modulus", 2)
    result = tuple(tuple(int(i == j) for j in range(5)) for i in range(5))
    base = T
    while exponent:
        if exponent & 1:
            result = multiply(result, base, modulus)
        base = multiply(base, base, modulus)
        exponent //= 2
    return result


def quartic(a, b, modulus=None):
    values = tuple(a**(4-j)*b**j for j in range(5))
    return values if modulus is None else tuple(x % modulus for x in values)


def fibonacci_pair(n):
    """Independent fast doubling, returns (F_n,F_(n+1))."""
    integer(n, "Fibonacci index")
    if not n:
        return 0, 1
    a, b = fibonacci_pair(n//2)
    c, d = a*(2*b-a), a*a+b*b
    return (d, c+d) if n & 1 else (c, d)


def predicted_quartic(n, modulus):
    """First column of T^n, i.e. quartic observation of A^(2n)(1,0)."""
    return tuple(row[0] for row in power(n, modulus))


def periods(a, b):
    integer(a, "binary depth", 1)
    integer(b, "ternary depth", 1)
    two = 3*2**max(a-3, 0)
    three = 2*3**(b-1)
    return two, three, lcm(two, three)


def clock_from_bbp_labels(code2, code3, a, b):
    """Recover present clock residue without reading any future source state."""
    integer(a, "binary depth", 1, 32)
    integer(b, "ternary depth", 1, 15)
    m2, m3 = 2**a, 3**b
    integer(code2, "binary source label", 0, m2-1)
    integer(code3, "cleared ternary label", 0, m3-1)
    n2 = binary_inverse_from_gates(code2, a)
    n3 = ternary_inverse_from_lifts(code3, b)
    return n2 + m2*((n3-n2)*pow(m2, -1, m3) % m3)


def observer_from_bbp_labels(code2, code3, a, b):
    """Compatible pair of five-component observations, no new information."""
    n = clock_from_bbp_labels(code2, code3, a, b)
    return predicted_quartic(n, 2**a), predicted_quartic(n, 3**b)


def source_labels(n, a, b):
    return binary_code(n, a), regularized_ternary_code(n, b)


def source_states(horizon):
    integer(horizon, "horizon")
    result = [Fraction(0)]
    for n in range(1, horizon+1):
        result.append(16*result[-1]+forcing(n))
    return result


def delayed_null(history, now, depth, stride):
    """Signed past filter at the actual clock now; no future reads.

    history[n] must hold the sample r(n).  The value is
    sum_j (-1)^j C(depth,j) r(now-depth*stride+j*stride).
    """
    integer(now, "present clock", 1)
    integer(depth, "depth")
    integer(stride, "stride", 1)
    start = now-depth*stride
    if start < 1 or now >= len(history):
        raise ValueError("required samples are outside retained past history")
    return sum(((-1)**j*comb(depth,j)*history[start+j*stride]
                for j in range(depth+1)), Fraction(0))


def phase_distance_squared_bounds(state, tail_upper):
    """Rational bounds for ||state+tail||_T², 0<=tail<=tail_upper.

    Used as a finite certificate only; no floating pi or fitted cosine.
    """
    state, tail_upper = Fraction(state), Fraction(tail_upper)
    if tail_upper < 0:
        raise ValueError("negative tail allowance")
    fraction = state-state.numerator//state.denominator
    distance = min(fraction, 1-fraction)
    lower = max(Fraction(0), distance-tail_upper)
    upper = min(Fraction(1,2), distance+tail_upper)
    return lower*lower, upper*upper


def source_shell_certificate(states, start):
    """Exact observed R0-energy interval on a specified finite shell.

    Label this a finite calibration, not evidence for an eventual bound.
    Source-tail estimate is r(n+1)/15, from the unchanged positive BBP source.
    """
    integer(start, "shell start", 1)
    if 2*start > len(states):
        raise ValueError("source history does not cover requested shell")
    bounds = [phase_distance_squared_bounds(states[n], forcing(n+1)/15)
              for n in range(start, 2*start)]
    return tuple(sum((p[i] for p in bounds), Fraction(0))/start for i in (0,1))


def local_pair_compatibility(residue2, residue3, a, b):
    """Are these exponent phases realizable by ONE forward clock?"""
    p2, p3, _ = periods(a, b)
    integer(residue2, "binary exponent phase", 0, p2-1)
    integer(residue3, "ternary exponent phase", 0, p3-1)
    return (residue2-residue3) % gcd(p2, p3) == 0
