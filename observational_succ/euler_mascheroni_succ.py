"""Exact finite interfaces for the Euler--Mascheroni successor defect.

Classical analytic source: G(s) = zeta(s) - 1/(s-1), with G(1)=gamma.
This module constructs rational finite sums, rigorous rational logarithm
enclosures, Hurwitz boundary differences, and positive finite Mellin kernels.
It does not use zeta zeros, pi digits, or floating-point certificate endpoints.

The positive kernel is G(s)/s on Re(s)>0, NOT the completed Weil form.
No RH or digit-normality conclusion follows from its positivity.
Proofs and all limits are in the accompanying Euler--Mascheroni dossier.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb

Q = Fraction


def _int(value: int, name: str, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def _positive_q(value: int | Q, name: str) -> Q:
    if type(value) is not int and not isinstance(value, Q):
        raise ValueError(f"{name} must be an exact rational")
    result = Q(value)
    if result <= 0:
        raise ValueError(f"{name} must be positive")
    return result


def _unit_log_bounds(value: Q, terms: int) -> tuple[Q, Q]:
    # 1 <= value <= 2.  The atanh series is positive, and its remaining
    # denominators are at least 2*terms+1.
    z = (value - 1) / (value + 1)
    partial = 2 * sum((z ** (2*j+1) / (2*j+1) for j in range(terms)), Q())
    remainder = 2*z**(2*terms+1) / ((2*terms+1)*(1-z*z))
    return partial, partial + remainder


def rational_log_bounds(value: int | Q, terms: int = 24) -> tuple[Q, Q]:
    """Enclose log(value); exact binary reduction keeps |atanh input|<=1/3."""
    value = _positive_q(value, "logarithm argument")
    _int(terms, "series terms")
    if value < 1:
        low, high = rational_log_bounds(1/value, terms)
        return -high, -low
    exponent = 0
    while value >= 2:
        value /= 2
        exponent += 1
    low, high = _unit_log_bounds(value, terms)
    low2, high2 = _unit_log_bounds(Q(2), terms)
    return low + exponent*low2, high + exponent*high2


def harmonic_prefix(count: int, offset: int | Q = 1, power: int = 1) -> Q:
    """sum_(0<=n<count) (n+offset)^(-power), with exact rational inputs."""
    _int(count, "prefix count", 0)
    offset = _positive_q(offset, "offset")
    _int(power, "integer power")
    return sum(((Q(n)+offset)**(-power) for n in range(count)), Q())


def continuum_prefix_bounds(count: int, power: int = 1,
                            terms: int = 24) -> tuple[Q, Q]:
    """The integral from 1 to count of x^(-power), including the pole seam."""
    _int(count, "prefix count")
    _int(power, "integer power")
    if power == 1:
        return rational_log_bounds(count, terms)
    value = (1-Q(count)**(1-power)) / (power-1)
    return value, value


def regularized_prefix_bounds(count: int, offset: int | Q = 1,
                              power: int = 1,
                              terms: int = 24) -> tuple[Q, Q]:
    """B_N(s,a)=sum_(n<N)(n+a)^(-s)-integral_1^N x^(-s) dx.

    For every a>0 and Re(s)>0 the analytic version tends to G(s,a).
    This function evaluates positive integer s; the s=1 logarithm is enclosed.
    """
    _int(count, "prefix count")
    total = harmonic_prefix(count, offset, power)
    low, high = continuum_prefix_bounds(count, power, terms)
    return total-high, total-low


def gamma_bounds(count: int = 64, terms: int = 24) -> tuple[Q, Q]:
    """Rigorous gamma bracket using 1/(2(N+1)) < H_N-log N-gamma < 1/(2N)."""
    _int(count, "prefix count")
    low, high = regularized_prefix_bounds(count, 1, 1, terms)
    return low-Q(1, 2*count), high-Q(1, 2*(count+1))


def hurwitz_difference_bounds(a: int | Q, b: int | Q, count: int = 64,
                               terms: int = 24) -> tuple[Q, Q]:
    """Enclose G(1,a)-G(1,b)=psi(b)-psi(a), without a gamma input.

    The signed decreasing tail lies between its integral and that integral
    plus its first term; their order depends on the sign of b-a.
    """
    a, b = _positive_q(a, "first offset"), _positive_q(b, "second offset")
    _int(count, "prefix count", 0)
    prefix = harmonic_prefix(count, a)-harmonic_prefix(count, b)
    low, high = rational_log_bounds((count+b)/(count+a), terms)
    first = 1/(count+a)-1/(count+b)
    return prefix+low+min(Q(), first), prefix+high+max(Q(), first)


def hurwitz_boundary_bounds(a: int | Q, count: int = 64,
                            terms: int = 24) -> tuple[Q, Q]:
    """Enclose G(1,a)=-psi(a) using gamma plus its exact offset difference."""
    low, high = gamma_bounds(count, terms)
    delta_low, delta_high = hurwitz_difference_bounds(a, 1, count, terms)
    return low+delta_low, high+delta_high


def finite_successor_boundary(count: int, offset: int | Q = 1,
                              power: int = 1) -> Q:
    """B_N(s,a+1)-B_N(s,a)=(N+a)^(-s)-a^(-s), including its endpoint."""
    _int(count, "prefix count")
    offset = _positive_q(offset, "offset")
    _int(power, "integer power")
    return (count+offset)**(-power)-offset**(-power)


def refinement_affine_data(multiplier: int, power: int = 1,
                           terms: int = 24) -> tuple[Q, tuple[Q, Q]]:
    """(scale, offset interval) for x -> p^(s-1)x + (p^(s-1)-1)/(s-1).

    The normalized p-residue refinement of B_N equals this map of B_(pN).
    At s=1 the scale is one and the offset is log p. Composite multipliers
    obey the same source law and are not independent prime Euler factors.
    """
    _int(multiplier, "integer multiplier")
    _int(power, "integer power")
    scale = Q(multiplier)**(power-1)
    if power == 1:
        return scale, rational_log_bounds(multiplier, terms)
    anomaly = (scale-1)/(power-1)
    return scale, (anomaly, anomaly)


def paired_raw_prefix(count: int, power: int) -> Q:
    """The user's equal-index finite sum at integer r=power>=2."""
    _int(count, "prefix count")
    _int(power, "integer power", 2)
    return harmonic_prefix(count, 1, power)-sum(
        (Q(power)**(-k) for k in range(1, count+1)), Q())


def paired_boundary_correction(count: int, power: int) -> Q:
    """(N^(1-r)-r^(-N))/(r-1), the exact missing two-clock boundary."""
    _int(count, "prefix count")
    _int(power, "integer power", 2)
    return (Q(count)**(1-power)-Q(power)**(-count))/(power-1)


def paired_boundary_limit_bounds(count: int,
                                 terms: int = 24) -> tuple[Q, Q]:
    """Removable r=1 boundary correction: N-log N, not zero."""
    _int(count, "prefix count")
    low, high = rational_log_bounds(count, terms)
    return count-high, count-low


def successor_cell_defect(index: int, power: int) -> Q:
    """n^(-s)-integral_n^(n+1) x^(-s) dx > 0 for integer s>=2."""
    _int(index, "cell index")
    _int(power, "integer power", 2)
    integral = (Q(index)**(1-power)-Q(index+1)**(1-power))/(power-1)
    return Q(index)**(-power)-integral


def finite_mellin_value(count: int, power: int) -> Q:
    """F_N(s)=sum_(n=1)^N cell_defect(n,s)/s.

    It is exactly integral_1^(N+1) (ceil x-x)*x^(-s-1) dx. Its limit
    is G(s)/s and has a positive tail bounded by mellin_tail_bound.
    """
    _int(count, "prefix count", 0)
    _int(power, "integer power", 2)
    return sum((successor_cell_defect(n, power)
                for n in range(1, count+1)), Q())/power


def mellin_tail_bound(count: int, power: int) -> Q:
    """0 <= F(s)-F_N(s) <= (N+1)^(-s)/s for real integer s>=2."""
    _int(count, "prefix count", 0)
    _int(power, "integer power", 2)
    return Q(count+1)**(-power)/power


def finite_mellin_kernel(count: int,
                         exponents: tuple[int, ...]) -> tuple[tuple[Q, ...], ...]:
    """Exact PSD Gram matrix [F_N(s_i+s_j)] for positive integer s_i.

    Positivity is the integral of a square against (ceil x-x) dx/x;
    it is not a numeric eigenvalue inference or a completed-Weil identity.
    """
    _int(count, "prefix count", 0)
    if not exponents:
        raise ValueError("at least one exponent is required")
    for value in exponents:
        _int(value, "kernel exponent")
    cache = {i+j: finite_mellin_value(count, i+j)
             for i in exponents for j in exponents}
    return tuple(tuple(cache[i+j] for j in exponents) for i in exponents)


def jet_counterfeit_coefficients(preserved_order: int) -> tuple[Q, ...]:
    """Coefficients of P_(M+1)(8*y-1), on 0<=y<=1/4.

    Adding +/- one quarter of this polynomial to the true gamma moment
    density v(y)=(1-{exp y})exp(-y) preserves moments through degree M.
    On this interval v=2exp(-y)-1>1/2 and |P|<=1, so both perturbed
    densities stay positive. This is a source-altering control, not zeta.
    """
    _int(preserved_order, "preserved order", 0)
    degree = preserved_order+1
    return tuple(Q((-1)**(degree-k)*comb(degree, k)*comb(degree+k, k)*4**k)
                 for k in range(degree+1))


def polynomial_moment(coefficients: tuple[Q, ...], order: int,
                       endpoint: Q = Q(1, 4)) -> Q:
    """Exact integral_0^endpoint y^order sum_k coefficients[k] y^k dy."""
    _int(order, "moment order", 0)
    endpoint = _positive_q(endpoint, "moment endpoint")
    if any(type(c) is not int and not isinstance(c, Q) for c in coefficients):
        raise ValueError("polynomial coefficients must be exact rationals")
    return sum((Q(c)*endpoint**(k+order+1)/(k+order+1)
                for k, c in enumerate(coefficients)), Q())
