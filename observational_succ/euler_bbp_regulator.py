"""Exact Hurwitz/Lerch interface for the authentic four-ray BBP source.

This is a source-labelled two-regulator family, not a normality proof.
Only exponent one preserves the original pi forcing.
The exponent-zero endpoint loses mass if a finite cutoff is taken first.
All certificate functions use integers/Fractions; optional analytic readouts
are explicitly numerical and never labelled interval certificates.
"""
from __future__ import annotations

from fractions import Fraction as Q


OFFSETS = (7, 4, 3, 2)
COEFFICIENTS = (4, -2, -1, -1)
HURWITZ_SHIFTS = (Q(1, 8), Q(1, 2), Q(5, 8), Q(3, 4))


def _integer(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def _rational(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def lerch_prefix(exponent: int, shift: Q, regulator: Q, count: int) -> Q:
    """Sum_{0<=n<count} z**n/(n+a)**s; finite identity, integer s>=0."""
    _integer(exponent)
    _integer(count)
    a, z = _rational(shift), _rational(regulator)
    if a <= 0 or not 0 <= z <= 1:
        raise ValueError("positive shift and regulator in [0,1] required")
    return sum((z**n/(a+n)**exponent for n in range(count)), Q())


def lerch_refined_prefix(exponent: int, shift: Q, regulator: Q,
                         radix: int, blocks: int) -> Q:
    """Finite residue partition with all source indices retained.

    Phi_(pN)(z,s,a)=p**(-s) sum_{j<p} z**j
                                  Phi_N(z**p,s,(a+j)/p).
    Integer p need not be prime; prime refinement is one special case.
    """
    _integer(exponent)
    _integer(radix, 2)
    _integer(blocks)
    a, z = _rational(shift), _rational(regulator)
    if a <= 0 or not 0 <= z <= 1:
        raise ValueError("positive shift and regulator in [0,1] required")
    return sum((z**j*lerch_prefix(exponent, (a+j)/radix, z**radix, blocks)
                for j in range(radix)), Q())/radix**exponent


def source_power_term(n: int, exponent: int = 1) -> Q:
    """r_s(n)=4/(8n-7)^s-2/(8n-4)^s-1/(8n-3)^s-1/(8n-2)^s.

    At s=1 this is the unchanged BBP forcing. At s=0 every term is zero.
    Changing s changes the forcing; only s=1 is used for pi claims.
    """
    _integer(n, 1)
    _integer(exponent)
    return sum((Q(c, (8*n-a)**exponent)
                for a, c in zip(OFFSETS, COEFFICIENTS)), Q())


def source_prefix(count: int, exponent: int = 1, regulator: Q = Q(1)) -> Q:
    """B_(s,N)(z)=sum_{n=1}^N z**(n-1) r_s(n), exact finite source."""
    _integer(count)
    _integer(exponent)
    z = _rational(regulator)
    if not 0 <= z <= 1:
        raise ValueError("regulator in [0,1] required")
    return sum((z**(n-1)*source_power_term(n, exponent)
                for n in range(1, count+1)), Q())


def source_hurwitz_prefix(count: int, exponent: int = 1,
                          regulator: Q = Q(1)) -> Q:
    """Independent four shifted Lerch readouts, exactly the same source."""
    _integer(count)
    _integer(exponent)
    z = _rational(regulator)
    return sum((c*lerch_prefix(exponent, a, z, count)
                for a, c in zip(HURWITZ_SHIFTS, COEFFICIENTS)), Q())/8**exponent


def source_tail_bracket(count: int, exponent: int = 1) -> tuple[Q, Q]:
    """Outward rational endpoints for sum_{n>N} r_s(n), integer s>=1.

    The paper theorem holds for every real s>0:
      (15/8)(8N+6)^(-s) < tail < (15/8)(8N-7)^(-s).
    Its proof is the exact positive three-difference representation followed
    by decreasing-integrand sum/integral bounds, not sampled zeta values.
    """
    _integer(count, 1)
    _integer(exponent, 1)
    return Q(15, 8*(8*count+6)**exponent), Q(15, 8*(8*count-7)**exponent)


def source_sum_interval(count: int, exponent: int = 1,
                        regulator: Q = Q(1)) -> tuple[Q, Q]:
    """Exact interval for the infinite B_s(z), with 0<=z<=1 and integer s>=1.

    At s=1,z=1/16 the enclosed value is pi by the classical BBP identity.
    This function supplies no digit-frequency information.
    """
    _integer(count, 1)
    _integer(exponent, 1)
    z = _rational(regulator)
    if not 0 <= z <= 1:
        raise ValueError("regulator in [0,1] required")
    value = source_prefix(count, exponent, z)
    if z == 0:
        return value, value
    if z == 1:
        lower, upper = source_tail_bracket(count, exponent)
        return value+lower, value+upper
    # Each of the three positive differences is decreasing in n.
    upper = z**count*source_power_term(count+1, exponent)/(1-z)
    return value, value+upper


def balanced_boundary_zero_value() -> Q:
    """B(0)=sum c*(1/2-a)=15/8, using classical zeta(0,a)=1/2-a.

    The literal s=0 series is zero. This is the *analytic* boundary value
    after the infinite sum; interchanging those operations is invalid.
    """
    return sum((c*(Q(1, 2)-a)
                for a, c in zip(HURWITZ_SHIFTS, COEFFICIENTS)), Q())


def cofinal_limit_for_power_clock(base: int) -> Q:
    """Theorem value for s=1/m,N=base**m as m->infinity.

    B_(s,N)(1) -> (15/8)(1-1/base). This computes that exact limit,
    not a finite approximation and not a pi-normality observation.
    """
    _integer(base, 2)
    return Q(15, 8)*(1-Q(1, base))


def numerical_power_clock(m: int, base: int = 2, *, dps: int = 70) -> dict:
    """Numerical-only Hurwitz evaluation of a huge finite prefix.

    The N summands are not materialized; the finite Hurwitz difference
    identity evaluates the same sum. Intermediate values have size near N,
    so at least a bound on decimal_digits(N)+35 working digits is required.
    This is a cancellation guard, NOT an outward precision certificate.
    """
    _integer(m, 2)
    _integer(base, 2)
    _integer(dps, 30)
    if m > 1024 or base > 16:
        raise ValueError("numerical diagnostic budget: m<=1024 and base<=16")
    N = base**m
    decimal_bound = (N.bit_length()*30103+99999)//100000
    if dps < decimal_bound+35:
        raise ValueError("insufficient digits for the large Hurwitz cancellation")
    import mpmath as mp
    with mp.workdps(dps):
        s = mp.mpf(1)/m
        total = mp.mpf(0)
        for a, c in zip(HURWITZ_SHIFTS, COEFFICIENTS):
            shift = mp.mpf(a.numerator)/a.denominator
            total += c*(mp.zeta(s, shift)-mp.zeta(s, N+shift))
        total /= mp.power(8, s)
        return {"m": m, "base": base, "count": str(N),
                "finite_prefix": mp.nstr(total, 25),
                "proved_limit": str(cofinal_limit_for_power_clock(base)),
                "numerical_only": True, "interval_certificate": False,
                "pi_normality_proved": False}
