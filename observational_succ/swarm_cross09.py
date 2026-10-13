"""Exact finite witnesses for X09; continuum realization is a paper theorem.

Coefficient intervals and pairwise bounds are necessary conditions. They do
not decide simultaneous infinite interpolation or authenticate a source bound.
All external scalars must be integers or Fraction objects; no float oracle.
"""
from fractions import Fraction as Q
from math import factorial


def _q(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise ValueError("An exact integer or Fraction is required")
    return Q(value)


def _natural(value, minimum=0):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError("Integer outside the declared domain")
    return value


def polynomial_value(coefficients, x):
    """Coefficient order is constant term first."""
    x = _q(x)
    result = Q(0)
    for a in reversed(tuple(_q(a) for a in coefficients)):
        result = result * x + a
    return result


def interpolate(points):
    """Exact Lagrange interpolant over Q, with duplicate abscissae rejected."""
    points = tuple((_q(x), _q(y)) for x, y in points)
    if not points or len({x for x, _ in points}) != len(points):
        raise ValueError("A nonempty set of distinct abscissae is required")
    answer = [Q(0)] * len(points)
    for i, (x, y) in enumerate(points):
        basis, denominator = [Q(1)], Q(1)
        for j, (other, _) in enumerate(points):
            if i == j:
                continue
            product = [Q(0)] * (len(basis) + 1)
            for k, a in enumerate(basis):
                product[k] -= other * a
                product[k + 1] += a
            basis = product
            denominator *= x - other
        for k, a in enumerate(basis):
            answer[k] += y * a / denominator
    return tuple(answer)


def coefficient_prefix_enclosure(coefficients, bound, x):
    """Outer value interval given |a_n|<=bound for ALL coefficients.

    The supplied prefix must obey the same bound; the unseen tail is a
    mathematical premise, not an output certified by this finite routine.
    """
    bound, x = _q(bound), _q(x)
    coefficients = tuple(_q(a) for a in coefficients)
    if bound < 0 or abs(x) >= 1 or any(abs(a) > bound for a in coefficients):
        raise ValueError("Coefficient bound and open unit-disk domain required")
    center = polynomial_value(coefficients, x)
    radius = bound * abs(x) ** len(coefficients) / (1 - abs(x))
    return center - radius, center + radius


def pairwise_difference_bound(bound, x, y):
    """Sharp |f(x)-f(y)| bound on K_M for nonnegative real x,y<1."""
    bound, x, y = _q(bound), _q(x), _q(y)
    if bound < 0 or not (0 <= x < 1 and 0 <= y < 1):
        raise ValueError("Nonnegative interior evaluation points required")
    return bound * abs(x / (1 - x) - y / (1 - y))


def alternating_data(count):
    _natural(count, 1)
    return tuple((Q(1, j + 2), Q((-1) ** j)) for j in range(count))


def alternating_coefficient_lower_bound(count):
    """Any polynomial fitting count>=2 alternating points needs M>=2n(n-1)."""
    _natural(count, 2)
    return Q(2 * count * (count - 1))


def gamma_product_cutoff(cutoff, z):
    """Independent factorial/product Gamma approximant at positive integers."""
    _natural(cutoff, 2)
    _natural(z, 1)
    denominator = 1
    for k in range(cutoff + 1):
        denominator *= z + k
    return Q(factorial(cutoff) * cutoff ** z, denominator)


def quarter_periodic_multiplier(index):
    """1+sin(2pi z)/2 at z=index/4, independently exact on quarter phases."""
    if isinstance(index, bool) or not isinstance(index, int):
        raise ValueError("Integer quarter phase required")
    return Q(1) + Q((0, 1, 0, -1)[index % 4], 2)


def binomial_polynomial_value(x, degree):
    _natural(degree)
    x, numerator = _q(x), Q(1)
    for k in range(degree):
        numerator *= x - k
    return numerator / factorial(degree)
