"""Exact fixed-pole source identification, never real-circle digit inference."""
from fractions import Fraction as F
from math import comb, factorial

OFFSETS = (1, 4, 5, 6)
AUTH = (4, -2, -1, -1)
AGE_DIRECTION = (1, -3, 1, 1)
NEWTON = ((60, 15, 12, 10), (1032, 804, 744, 692),
          (2496, 2304, 2240, 2176), (1536, 1536, 1536, 1536))
SHARP_DIRECTION = (-51, 3200, -6825, 3696)


def coefficients(c):
    c = tuple(c)
    if len(c) != 4 or any(type(x) is not int for x in c):
        raise ValueError("four integer coefficients required")
    return c


def source(n, c=AUTH, derivative=0):
    c = coefficients(c)
    if type(n) is not int or type(derivative) is not int or derivative < 0:
        raise ValueError("integer index and nonnegative derivative required")
    return (-8)**derivative * factorial(derivative) * sum(
        (F(a, (8*n-8+d)**(derivative+1)) for a, d in zip(c, OFFSETS)), F())


def orbit(n, c=AUTH):
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative integer time required")
    u = F()
    for j in range(1, n+1):
        u = 16*u + source(j, c)
    return u


def odd_denominator(n):
    return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)


def numerator(n, c):
    value = 4*odd_denominator(n)*source(n, c)
    assert value.denominator == 1
    return value.numerator


def newton_coordinates(c):
    c = coefficients(c)
    return tuple(sum(a*b for a, b in zip(row, c)) for row in NEWTON)


def all_time_zero_mod(c, bits):
    """The proved four-coordinate criterion; not an infinite numerical loop."""
    if type(bits) is not int or bits < 0:
        raise ValueError("nonnegative precision required")
    modulus = 1 << (bits+2)
    return all(x % modulus == 0 for x in newton_coordinates(c))


def valuation(x):
    x = F(x)
    if not x:
        return float("inf")
    a, b = abs(x.numerator), x.denominator
    return (a & -a).bit_length() - (b & -b).bit_length()


def unit_log_jet(n, derivative=0, c=AUTH):
    """d^j/dn^j of (1/8) H_2'/H_2, at t=n-1."""
    c = coefficients(c)
    return (-8)**derivative * factorial(derivative) * (
        F(c[0], (8*n-7)**(derivative+1)) +
        F(c[2], (8*n-3)**(derivative+1)))


def unit_ratio(n, c=AUTH):
    c = coefficients(c)
    # Signs from all four Morita ratios are retained for general coefficients.
    return F(-1)**sum(c) * F(8*n-7)**c[0] * F(8*n-3)**c[2]


def backward_boundary(c, terms):
    return sum((16**j*source(-j, c) for j in range(terms)), F())


def polynomial_reconstruction(n, c):
    """Integer n>=1; Newton binomials are integral at every such n."""
    if type(n) is not int or n < 1:
        raise ValueError("positive integer time required")
    return sum(comb(n-1, j)*x for j, x in enumerate(newton_coordinates(c))
               if n-1 >= j)
