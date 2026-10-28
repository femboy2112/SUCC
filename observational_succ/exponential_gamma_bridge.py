"""Finite beta source, exponential Laplace/Mellin limits, and the BBP error.

All certificate endpoints are exact rationals.  Classical beta/Gamma theory
supplies the infinite limit; paper proofs in the accompanying research dossier
supply the universal bounds.  Finite tests do not prove Weyl cancellation.

For m>=1, the finite polynomial probability density is
    p_m(x)=(1-x/m)^(m-1), 0<x<m.
Its Mellin transform is m^z product_(j=1)^m (1+z/j)^(-1), and its logarithmic
mean is log(m)-H_m.  The limit density exp(-x) has Laplace transform 1/(1+s)
and Mellin transform Gamma(1+z).  The positive Laplace fixed point is 1/phi.
These are different observables of a declared common source, not a proof that
the golden ratio determines gamma or the signed BBP orbit.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial

from .bbp_natural_carrier import exact_forcing, forcing_denominator
from .euler_mascheroni_succ import (
    gamma_bounds, harmonic_prefix, rational_log_bounds,
)
from .gamma_bbp_signed_coherence import green_tail_interval
from .zero_one_gamma_bridge import GammaBridgeError, RationalInterval


def _integer(value: int, name: str, lower: int = 1, upper: int = 10000) -> int:
    if type(value) is not int or not lower <= value <= upper:
        raise GammaBridgeError(f"{name} must be an integer in [{lower},{upper}]")
    return value


def _rational(value: int | Q, name: str) -> Q:
    if type(value) not in (int, Q):
        raise GammaBridgeError(f"{name} requires an exact rational")
    return Q(value)


def finite_beta_moment(size: int, degree: int) -> Q:
    """E[X_m^k]=k! product_(j=1)^k m/(m+j), with X_m~m Beta(1,m)."""
    m = _integer(size, "finite beta size")
    k = _integer(degree, "moment degree", 0, 512)
    value = Q(factorial(k))
    for j in range(1, k+1):
        value *= Q(m, m+j)
    return value


def finite_beta_survival(size: int, point: int | Q) -> Q:
    """P(X_m>x), an exact polynomial on its finite support [0,m]."""
    m = _integer(size, "finite beta size")
    x = _rational(point, "survival point")
    if not 0 <= x <= m:
        raise GammaBridgeError("survival point must lie in [0,m]")
    return (1-x/m)**m


def finite_beta_mellin_successor(size: int, exponent: int | Q) -> Q:
    """M_m(z+1)/M_m(z)=m(z+1)/(m+z+1), for real z>-1.

    This finite-size correction tends to the factorial/Gamma successor z+1.
    The expression is exact rational for rational z; M_m(z) itself need not be.
    """
    m = _integer(size, "finite beta size")
    z = _rational(exponent, "Mellin exponent")
    if z <= -1:
        raise GammaBridgeError("Mellin integrability requires z>-1")
    return m*(z+1)/(m+z+1)


def finite_beta_log_mean_interval(size: int, log_terms: int = 24) -> RationalInterval:
    """Enclose E[log X_m]=log(m)-H_m without a numerical gamma input."""
    m = _integer(size, "finite beta size")
    terms = _integer(log_terms, "log terms", 1, 250)
    lo, hi = rational_log_bounds(m, terms)
    harmonic = harmonic_prefix(m)
    return RationalInterval(lo-harmonic, hi-harmonic)


def finite_beta_laplace_interval(size: int, argument: int | Q,
                                terms: int = 96) -> RationalInterval:
    """Enclose E[exp(-s X_m)] using consecutive Taylor polynomials.

    For x>=0 the exponential Taylor remainder has its next term's sign and
    magnitude at most that term.  Integration preserves the bracket, even
    when the initial term magnitudes increase.  Term k is (-s*m)^k m!/(m+k)!.
    """
    m = _integer(size, "finite beta size")
    s = _rational(argument, "Laplace argument")
    if s < 0:
        raise GammaBridgeError("Laplace argument must be nonnegative")
    count = _integer(terms, "Taylor terms", 0, 512)
    term = Q(1)
    partial = term
    for k in range(1, count+1):
        term *= -s*m/(m+k)
        partial += term
    following = term*(-s*m)/(m+count+1)
    lo, hi = sorted((partial, partial+following))
    return RationalInterval(max(Q(0), lo), min(Q(1), hi))


def golden_laplace_fixed_point_interval(bits: int = 64) -> RationalInterval:
    """Rational enclosure of the positive fixed point of 1/(1+s)."""
    count = _integer(bits, "bisection bits", 1, 512)
    lo, hi = Q(0), Q(1)
    for _ in range(count):
        mid = (lo+hi)/2
        if mid*mid+mid < 1:
            lo = mid
        else:
            hi = mid
    return RationalInterval(lo, hi)


def finite_beta_fixed_point_interval(size: int, bits: int = 32,
                                    terms: int = 128) -> RationalInterval:
    """Certified root of L_m(s)=s in (0,1), via exact Laplace intervals.

    L_m is continuous and strictly decreasing, so the root is unique.  This
    routine raises on an unresolved midpoint; it never guesses a sign.
    """
    m = _integer(size, "finite beta size")
    count = _integer(bits, "bisection bits", 1, 256)
    _integer(terms, "Taylor terms", 0, 512)
    lo, hi = Q(0), Q(1)
    for _ in range(count):
        mid = (lo+hi)/2
        value = finite_beta_laplace_interval(m, mid, terms)
        if value.lower > mid:
            lo = mid
        elif value.upper < mid:
            hi = mid
        else:
            raise GammaBridgeError("Laplace midpoint unresolved; increase Taylor terms")
    return RationalInterval(lo, hi)


def golden_gamma_offset_interval(gamma_count: int = 256, log_terms: int = 32,
                                 bits: int = 64) -> RationalInterval:
    """Canonical offset 1/phi-gamma, with its scale/normalization declared."""
    _integer(gamma_count, "gamma count")
    _integer(log_terms, "log terms", 1, 250)
    fixed = golden_laplace_fixed_point_interval(bits)
    lo, hi = gamma_bounds(gamma_count, log_terms)
    return RationalInterval(fixed.lower-hi, fixed.upper-lo)


def euler_remainder_interval(index: int) -> RationalInterval:
    """1/(2n)-1/(12n^2) < H_n-log(n)-gamma < 1/(2n), n>=1.

    Proof: integrate exp(-nt)[1/t-1/(exp(t)-1)], bounded strictly between
    1/2-t/12 and 1/2.  The lower kernel inequality follows from the positive
    series sum_(k>=5) (k-3)(k-4)t^k/k!.
    """
    n = _integer(index, "Euler remainder index", 1, 100000)
    return RationalInterval(Q(6*n-1, 12*n*n), Q(1, 2*n))


# For n=m+1, these are the increasing-power coefficients of
# 15(6n-1)^2 D(n+1) - 2304 n^4 P(n+1).
UPPER_BRIDGE_SHIFTED_COEFFICIENTS = (
    188703, 906498, 1686012, 1519128, 664032, 112896,
)


def upper_bridge_polynomial_certificate(index: int) -> dict:
    """Exact source-sensitive certificate for r(n+1)/15 < epsilon_low(n)^2/16."""
    n = _integer(index, "bridge index", 1, 99999)
    shifted = n-1
    numerator = sum((Q(c)*shifted**k
                     for k, c in enumerate(UPPER_BRIDGE_SHIFTED_COEFFICIENTS)), Q())
    denominator = 34560*n**4*forcing_denominator(n+1)
    expected_gap = numerator/denominator
    epsilon_low = euler_remainder_interval(n).lower
    observed_gap = epsilon_low**2/16-exact_forcing(n+1)/15
    if observed_gap != expected_gap or expected_gap <= 0:
        raise ArithmeticError("authentic BBP/Euler polynomial certificate failed")
    return {"index": n, "numerator": numerator, "denominator": denominator,
            "positive_gap": expected_gap,
            "shifted_coefficients": UPPER_BRIDGE_SHIFTED_COEFFICIENTS}


@dataclass(frozen=True)
class BBPEulerTailBridge:
    index: int
    euler_remainder: RationalInterval
    green_tail: RationalInterval
    analytic_tail_lower: Q
    analytic_tail_upper: Q
    normalized_ratio: RationalInterval
    upper_polynomial_gap: Q


def bbp_euler_tail_bridge(index: int, depth: int = 16) -> BBPEulerTailBridge:
    """Exact finite interface to the universal source-specific theorem

        1/(8n+7/2)^2 < T_n < epsilon_n^2/16,
        (n/(n+7/16))^2 < 16 T_n/epsilon_n^2 < 1.

    T_n is the authentic discounted BBP future tail, epsilon_n is the Euler
    remainder.  The all-n proof uses Jensen and a positive polynomial; these
    exact finite enclosures calibrate it.  No golden reference is needed.
    """
    n = _integer(index, "bridge index", 1, 99000)
    _integer(depth, "Green depth", 0, 300)
    euler = euler_remainder_interval(n)
    green = green_tail_interval(n, depth)
    lower = 1/(8*Q(n)+Q(7, 2))**2
    upper = exact_forcing(n+1)/15
    proof = upper_bridge_polynomial_certificate(n)
    intersection = RationalInterval(max(lower, green.lower), min(upper, green.upper))
    ratio = RationalInterval(
        max((Q(n)/(n+Q(7, 16)))**2, 16*intersection.lower/euler.upper**2),
        min(Q(1), 16*intersection.upper/euler.lower**2),
    )
    return BBPEulerTailBridge(n, euler, intersection, lower, upper, ratio,
                             proof["positive_gap"])


def bbp_euler_asymptotic_coefficients() -> dict:
    """Exact coefficients; the all-order remainder authority is the paper proof.

    Powers in tail and Euler-square tuples begin at n^-2.  Ratio powers begin
    at n^0.  These are source-derived expansions, not fitted decimals.
    """
    return {
        "green_tail": (Q(1, 64), Q(-7, 512), Q(55, 4096)),
        "euler_remainder_squared_over_16": (Q(1, 64), Q(-1, 192), Q(1, 2304)),
        "normalized_ratio": (Q(1), Q(-13, 24), Q(125, 192)),
        "euler_square_minus_tail_leading": Q(13, 1536),
    }
