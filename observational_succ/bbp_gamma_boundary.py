"""Source-preserving Gamma primitive of the exact signed BBP forcing.

Paper object, x>=0:
  G(x)=Gamma(x+1/8)^4/[Gamma(x+1/2)^2 Gamma(x+5/8) Gamma(x+3/4)].
Its ratio G(x+1)/G(x) is rational, and its logarithmic ratio derivative
is 8*r(x+1).  Euler gamma cancels from the balanced digamma readout but
has coefficient 15/8 in log G(0)'s convergent expansion.

All public outputs below are exact rational quantities or proved outward
intervals.  No Gamma/zeta numerical evaluator, pi digits, or zeta zeros are
construction inputs.  These identities do not prove orbit cancellation.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .euler_bbp_regulator import COEFFICIENTS, HURWITZ_SHIFTS
from .euler_mascheroni_succ import gamma_bounds, harmonic_prefix, rational_log_bounds


def _integer(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError("integer in the declared domain required")
    return value


def _nonnegative_q(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    value = Q(value)
    if value < 0:
        raise ValueError("nonnegative source translation required")
    return value


def source_gamma_moment(order: int) -> Q:
    """M_k=sum c_j*(1-a_j)^k; M_0=0, M_1=15/8, M_k>0 for k>=1.

    The a_j are Hurwitz shifts, not circle-orbit states. M_k is eight
    times the inherited signed forcing-pole moment.
    """
    _integer(order)
    return sum((c*(1-a)**order for c, a in
                zip(COEFFICIENTS, HURWITZ_SHIFTS)), Q())


def gamma_successor_ratio(origin: int | Q) -> Q:
    """Exact G(x+1)/G(x), valid x>=0; positive rational for rational x."""
    x = _nonnegative_q(origin)
    result = Q(1)
    for c, a in zip(COEFFICIENTS, HURWITZ_SHIFTS):
        result *= (x+a)**c
    return result


def gamma_ratio_log_derivative(origin: int | Q) -> Q:
    """d/dx log(G(x+1)/G(x))=8*r(x+1), exactly on rational x>=0."""
    x = _nonnegative_q(origin)
    return sum((Q(c)/(x+a) for c, a in
                zip(COEFFICIENTS, HURWITZ_SHIFTS)), Q())


def gamma_successor_product(origin: int | Q, count: int) -> Q:
    """Exact finite G(x+N)/G(x); it does not fix the value G(x)."""
    x = _nonnegative_q(origin)
    _integer(count)
    result = Q(1)
    for j in range(count):
        result *= gamma_successor_ratio(x+j)
    return result


def ordinary_source_tail_interval(origin: int | Q, count: int = 32) -> tuple[Q, Q]:
    """Enclose H(x)=sum_{j>=0}r(x+j+1)=-(log G)'(x)/8.

    Positive source-difference and integral-test bounds prove the omitted
    tail lies between 15/[8(8(x+N)+6)] and 15/[8(8(x+N)-7)].
    """
    x = _nonnegative_q(origin)
    _integer(count, 1)
    prefix = sum((gamma_ratio_log_derivative(x+j)/8
                  for j in range(count)), Q())
    u = 8*(x+count)
    return prefix+Q(15, 8)/(u+6), prefix+Q(15, 8)/(u-7)


def _integer_zeta_interval(order: int, count: int) -> tuple[Q, Q]:
    _integer(order, 2)
    _integer(count, 1)
    prefix = sum((Q(1, j**order) for j in range(1, count+1)), Q())
    return (prefix+Q(1, (order-1)*(count+1)**(order-1)),
            prefix+Q(1, (order-1)*count**(order-1)))


def gamma_zeta_series_tail(order: int) -> Q:
    """Upper bound after degree K of sum_{k>=2} M_k*zeta(k)/k.

    For K>=1, M_k<=4*(7/8)^k and zeta(k)<2, hence the positive
    omitted tail is <64*(7/8)^(K+1)/(K+1).
    """
    _integer(order, 1)
    return 64*Q(7, 8)**(order+1)/(order+1)


def log_gamma_boundary_series_interval(order: int = 48, count: int = 64,
                                       log_terms: int = 24) -> tuple[Q, Q]:
    """Enclose log G(0)=(15/8)*gamma+sum_{k>=2}M_k*zeta(k)/k.

    Inputs are finite harmonic sums and rational log enclosures. The
    presence of gamma in this particular normalization is an identity,
    not an algebraic-independence claim or a digit-statistics theorem.
    """
    _integer(order, 1)
    _integer(count, 1)
    _integer(log_terms, 1)
    gamma_lo, gamma_hi = gamma_bounds(count, log_terms)
    coefficient = source_gamma_moment(1)
    lower, upper = coefficient*gamma_lo, coefficient*gamma_hi
    for k in range(2, order+1):
        lo, hi = _integer_zeta_interval(k, count)
        weight = source_gamma_moment(k)/k
        lower += weight*lo
        upper += weight*hi
    return lower, upper+gamma_zeta_series_tail(order)


def compensated_gamma_product_interval(count: int = 64,
                                       gamma_count: int = 64,
                                       log_terms: int = 24) -> tuple[Q, Q]:
    """Independent product expansion enclosure of log G(0).

    log G(0)=M_1*gamma+sum_{n>=1}[-log q(n-1)-M_1/n].
    Each compensated summand is positive. Its tail after N is bounded
    above by 2*(7/8)^2/[N*(1-(7/8)/(N+1))].
    """
    _integer(count, 1)
    _integer(gamma_count, 1)
    _integer(log_terms, 1)
    gamma_lo, gamma_hi = gamma_bounds(gamma_count, log_terms)
    coefficient = source_gamma_moment(1)
    product = gamma_successor_product(0, count)
    log_lo, log_hi = rational_log_bounds(product, log_terms)
    harmonic = harmonic_prefix(count)
    lower = coefficient*(gamma_lo-harmonic)-log_hi
    upper = coefficient*(gamma_hi-harmonic)-log_lo
    a = Q(7, 8)
    remainder = 2*a*a/(count*(1-a/(count+1)))
    return lower, upper+remainder


def source_zeta_zero_derivative_interval(order: int = 48, count: int = 64,
                                         log_terms: int = 24) -> tuple[Q, Q]:
    """Enclose B'(0)=log G(0)-(15/8)*log8 for inherited source B(s).

    Uses Hurwitz zeta'(0,a)=log Gamma(a)-log(2*pi)/2 as a classical
    paper identity. The constant log(2*pi) cancels by sum c_j=0.
    This is a signed source determinant normalization, not a positive
    spectral determinant or any assertion about nontrivial zeta zeros.
    """
    lo, hi = log_gamma_boundary_series_interval(order, count, log_terms)
    ll, lh = rational_log_bounds(8, log_terms)
    coefficient = source_gamma_moment(1)
    return lo-coefficient*lh, hi-coefficient*ll


def gamma_boundary_receipt(order: int = 32, count: int = 32) -> dict:
    """Compact exact finite readout; all asymptotic authority is paper proof."""
    _integer(order, 1)
    _integer(count, 1)
    return {
        "source": "original-four-pole-BBP-Gamma-primitive",
        "coefficient_sum": sum(COEFFICIENTS),
        "M0": source_gamma_moment(0),
        "M1": source_gamma_moment(1),
        "M2": source_gamma_moment(2),
        "q0": gamma_successor_ratio(0),
        "log_ratio_derivative0": gamma_ratio_log_derivative(0),
        "product_count": count,
        "finite_product": gamma_successor_product(0, count),
        "ordinary_tail_interval": ordinary_source_tail_interval(0, count),
        "log_G0_series_interval": log_gamma_boundary_series_interval(order, count),
        "log_G0_product_interval": compensated_gamma_product_interval(count, count),
        "Bprime0_interval": source_zeta_zero_derivative_interval(order, count),
        "normality_proved": False,
        "new_lean_authority": False,
    }
