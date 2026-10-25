"""Exact Pascal differences of the fixed BBP forcing and authenticated source.

The companion report proves the valuation and minimal-degree statements.
These evaluators do not prove real-circle collision or normality estimates.
No floating arithmetic or supplied digits of pi are used.
"""
from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial, isqrt

from observational_succ.bbp_two_adic import particular_mod, rational_mod


# Algebraically identical to the original four poles.  The half coefficients
# are retained individually; their finite differences are 2-integral for k>=1.
POLES = ((8, -7, Q(4)), (8, -3, Q(-1)),
         (2, -1, Q(-1, 2)), (4, -1, Q(-1, 2)))


def _integer(value, name, minimum=None):
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError(f"{name} must be an integer"
                         + (f" >= {minimum}" if minimum is not None else ""))
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("an exact integer or Fraction is required")
    return Q(value)


def _two_integral(value):
    value = _rational(value)
    if value.denominator % 2 == 0:
        raise ValueError("the rational start must belong to Z_2")
    return value


def _prime(prime):
    _integer(prime, "prime", 2)
    if any(prime % d == 0 for d in range(2, isqrt(prime) + 1)):
        raise ValueError("prime required")
    return prime


def rational_valuation(value, prime=2):
    """The exact rational p-valuation; None denotes the zero value."""
    value = _rational(value)
    _prime(prime)
    if value == 0:
        return None
    numerator, denominator = abs(value.numerator), value.denominator
    result = 0
    while numerator % prime == 0:
        numerator //= prime
        result += 1
    while denominator % prime == 0:
        denominator //= prime
        result -= 1
    return result


def reciprocal_difference(start, order, slope, offset):
    """Delta^k [1/(a*t+b)] at t=start, by the exact product formula."""
    start = _rational(start)
    _integer(order, "order", 0)
    _integer(slope, "slope", 1)
    _integer(offset, "offset")
    denominator = Q(1)
    for j in range(order + 1):
        factor = slope * (start+j) + offset
        if factor == 0:
            raise ValueError("the requested difference encounters a pole")
        denominator *= factor
    return Q((-slope)**order * factorial(order), 1) / denominator


def forcing_difference(start, order):
    """Exact Delta^k r(t), for a rational t in Z_2 and k>=0."""
    start = _two_integral(start)
    _integer(order, "order", 0)
    return sum((weight * reciprocal_difference(start, order, slope, offset)
                for slope, offset, weight in POLES), Q(0))


def difference_valuation(order):
    """nu(k)=k-1+v2(k!)=2*k-popcount(k)-1, for k>=1.

    This is the proved exact valuation of Delta^k r(t) and Delta^k F(t)
    for EVERY t in Z_2, not a numerical fit.  It is not an odd-prime rule.
    """
    _integer(order, "order", 1)
    return 2*order-order.bit_count()-1


def source_difference_mod(index, order, bits):
    """Exact Pascal difference of F modulo a power of two.

    Uses the separately implemented backwards-source evaluator, retaining
    the signed row coefficients.  Integer indices may be negative.
    """
    _integer(index, "index")
    _integer(order, "order", 0)
    _integer(bits, "bits", 1)
    return sum((-1)**(order-j)*comb(order, j)
               * particular_mod(index+j, bits)
               for j in range(order+1)) % (1 << bits)


@lru_cache(maxsize=None)
def mahler_coefficients(kind, maximum_order):
    """Exact rational Newton/Mahler coefficients through maximum_order.

    For the source b_0=0 and b_(k+1)=15*b_k+Delta^k r(1).  This follows
    from the authenticated recurrence and is checked against independent
    unwrapped rational source values in the test suite.
    """
    if kind not in ("forcing", "source"):
        raise ValueError("kind must be 'forcing' or 'source'")
    _integer(maximum_order, "maximum_order", 0)
    if kind == "forcing":
        return tuple(forcing_difference(0, k)
                     for k in range(maximum_order+1))
    result = [Q(0)]
    for k in range(maximum_order):
        result.append(15*result[-1]+forcing_difference(1, k))
    return tuple(result)


def minimal_mahler_degree(bits):
    """Minimal integer-valued polynomial degree for r or F mod 2**bits.

    Optimality is a statement about the FUNCTION on Z_2: applying Delta^K
    at zero excludes every polynomial of degree below K.  It is stronger
    than asserting that one particular truncation has a nonzero last term.
    """
    _integer(bits, "bits", 1)
    degree = 1
    while difference_valuation(degree+1) < bits:
        degree += 1
    return degree


def newton_mod(index, bits, kind="source"):
    """Evaluate the exact minimal-degree Mahler polynomial modulo 2**bits.

    The isometry makes reduction of the integer index modulo 2**bits valid.
    This implementation precomputes O(bits) rational coefficients using
    O(bits**2) rational product operations and uses O(bits) terms per value.
    Those are arithmetic-operation counts, not unit-cost bit-complexity
    claims.  Coefficient and binomial-integer sizes grow with precision.
    """
    _integer(index, "index")
    _integer(bits, "bits", 1)
    if kind not in ("forcing", "source"):
        raise ValueError("kind must be 'forcing' or 'source'")
    modulus = 1 << bits
    degree = minimal_mahler_degree(bits)
    coefficients = mahler_coefficients(kind, degree)
    representative = index % modulus
    total, binomial = 0, 1
    for k, coefficient in enumerate(coefficients):
        if k:
            binomial = binomial * (representative-k+1) // k
        total += rational_mod(coefficient, bits) * (binomial % modulus)
    return total % modulus


def odd_pole_counts(start, order, slope, offset, prime):
    """Prime-power denominator counts for an individual dyadic-slope pole.

    The return entries are (prime_power, denominator_count, factorial_count).
    For every entry denominator_count-factorial_count is 0 or 1.  Their
    negative sum is the odd-prime valuation of the reciprocal difference.
    These per-pole values cannot be minimized to obtain the valuation of
    the four-pole SUM when the minimum is attained more than once.
    """
    _integer(start, "start")
    _integer(order, "order", 0)
    _integer(slope, "slope", 2)
    _integer(offset, "offset")
    _prime(prime)
    if slope & (slope-1) or offset % 2 == 0 or prime == 2:
        raise ValueError("a power-of-two slope, odd offset and odd prime are required")
    factors = tuple(slope*(start+j)+offset for j in range(order+1))
    limit = max(abs(x) for x in factors)
    rows = []
    power = prime
    while power <= limit:
        count = sum(x % power == 0 for x in factors)
        rows.append((power, count, order//power))
        power *= prime
    return tuple(rows)


def odd_pole_valuation(start, order, slope, offset, prime):
    """Exact odd-prime valuation for one reciprocal difference, not r's sum."""
    return sum(factorial_count-count for _, count, factorial_count in
               odd_pole_counts(start, order, slope, offset, prime))
