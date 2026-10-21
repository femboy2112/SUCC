"""Exact finite objects for the Duck RH/ABC-to-digit contingency audit.

The RH budget is CONDITIONAL on a quantified Chebyshev estimate. Computing
the budget does not prove RH, certify an infinite prime tail, or prove Fourier
cancellation. The ABC helper checks one finite numerical premise; it never
registers the integer abc conjecture as proved authority.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


def _integer(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError("genuine integer in the declared domain required")
    return value


def _positive_rational(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction) or value <= 0:
        raise ValueError("positive exact integer or Fraction required")
    return Fraction(value)


def _prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def prime_power_terms(limit: int) -> tuple[tuple[int, int, int, Fraction], ...]:
    """Return (p,k,p**k,1/(k*p**(2*k))) for genuine p**k <= limit.

    The executable enumeration domain is 2 <= limit <= 10000. The paper
    theorem has no such upper bound. A composite such as six never supplies
    a prime-power atom; a square such as four carries coefficient 1/32.
    """
    _integer(limit, 2)
    if limit > 10000:
        raise ValueError("finite enumeration limit must be at most 10000")
    atoms = []
    for p in range(2, limit + 1):
        if not _prime(p):
            continue
        power, k = p, 1
        while power <= limit:
            atoms.append((p, k, power, Fraction(1, k * power * power)))
            power *= p
            k += 1
    return tuple(sorted(atoms, key=lambda atom: atom[2]))


def log_zeta2_partial(limit: int) -> Fraction:
    """Exact S(limit); its infinite sum is log(zeta(2)), not zeta(2)."""
    return sum((atom[3] for atom in prime_power_terms(limit)), Fraction())


@dataclass(frozen=True)
class ConditionalFourierBudget:
    limit: int
    horizon: int
    frequency: int
    psi_constant: Fraction
    log_tail_error_upper: Fraction
    mean_difference_upper: Fraction
    status: str = "CONDITIONAL_PAPER_BOUND_NOT_CANCELLATION"
    premise: str = "for all real t>=limit: |psi(t)-t|<=C*sqrt(t)*log(t)^2"


def conditional_fourier_budget(
    limit: int, horizon: int, frequency: int,
    psi_constant: int | Fraction = Fraction(1, 24),
) -> ConditionalFourierBudget:
    """Rational envelope for a conditional, genuine-prime approximation.

    For limit>=101, RH plus Lee--Nosal (arXiv:2312.05628v4, Thm 1.2)
    supplies C=1/24. Other C values require their own quantified premise.
    Let S=sum_{p**k<=X}1/(k*p**(2*k)), J=int_X^inf dt/(t² log t), and
    a_X=sqrt(6)*exp((S+J)/2). This bounds |W_N(pi)-W_N(a_X)|, not either
    Weyl mean alone. It does not numerically evaluate J or a_X.

    bit_length(X) >= log X and isqrt(X) <= sqrt X make the budget rational.
    epsilon<=1 is required for the displayed exponential-error simplification.
    """
    _integer(limit, 101)
    _integer(horizon, 1)
    if type(frequency) is not int or frequency == 0:
        raise ValueError("nonzero genuine integer Fourier frequency required")
    c = _positive_rational(psi_constant)
    epsilon = c * (Fraction(7, 3) * limit.bit_length() + Fraction(14, 9)) / (
        limit * isqrt(limit)
    )
    if epsilon > 1:
        raise ValueError("rational tail bound exceeds the epsilon<=1 regime")
    difference = Fraction(32 * abs(frequency) * (16**horizon - 1), 15 * horizon) * epsilon
    return ConditionalFourierBudget(limit, horizon, frequency, c, epsilon,
                                    min(Fraction(2), difference))


def thue_morse_digit(index: int) -> int:
    _integer(index)
    return index.bit_count() % 2


def thue_morse_prefix_interval(base: int, length: int) -> tuple[Fraction, Fraction]:
    """Enclose sum_{k>=1} t_k/base**k from its first length digits.

    All remaining digits lie in {0,1}, so the exact remaining upper budget is
    1/((base-1)*base**length). This is an interval, not a floating sample.
    """
    _integer(base, 2)
    _integer(length)
    prefix = sum((Fraction(thue_morse_digit(k), base**k)
                  for k in range(1, length + 1)), Fraction())
    return prefix, prefix + Fraction(1, (base - 1) * base**length)


def _radical(n: int) -> int:
    _integer(n, 1)
    result, factor = 1, 2
    while factor * factor <= n:
        if n % factor == 0:
            result *= factor
            while n % factor == 0:
                n //= factor
        factor += 1
    return result * n


@dataclass(frozen=True)
class ResidualSquareConsequence:
    p: int
    q: int
    prefix: int
    base: int
    depth: int
    common_gcd: int
    u: int
    v: int
    residual: int
    height: int
    radical_uv: int
    abc_constant: Fraction
    squared_residual_lower: Fraction
    squared_distance_lower: Fraction
    actual_squared_distance: Fraction
    status: str = "EXACT_FINITE_CHECK_NOT_UNIVERSAL_ABC"


def residual_square_consequence(
    p: int, q: int, prefix: int, base: int, depth: int,
    abc_constant: int | Fraction,
) -> ResidualSquareConsequence:
    """Check one exponent-two abc premise and its rational residual bound.

    Put g=gcd(p*b**n,q*A), U=p*b**n/g, V=q*A/g, D=|U-V|, H=max(U,V).
    If H<=K*rad(U*V*D)^2 holds for this exact triple, derive
    D²>=H/(K*rad(U*V)^2), then transport to |p/q-A/b**n|².
    Reject a false premise or zero residual. The function does not assert
    that any one K works for every triple, and does not assert p/q≈pi.
    """
    for value in (p, q, prefix):
        _integer(value, 1)
    _integer(base, 2)
    _integer(depth)
    constant = _positive_rational(abc_constant)
    denominator = base**depth
    left, right = p * denominator, q * prefix
    common = gcd(left, right)
    u, v = left // common, right // common
    residual, height = abs(u - v), max(u, v)
    if residual == 0:
        raise ValueError("zero residual is not a positive abc triple")
    if height > constant * _radical(u * v * residual)**2:
        raise ValueError("the exact finite abc premise is false")
    rad_uv = _radical(u * v)
    lower = Fraction(height, 1) / (constant * rad_uv**2)
    distance_lower = Fraction(common**2, q**2 * denominator**2) * lower
    actual = (Fraction(p, q) - Fraction(prefix, denominator))**2
    return ResidualSquareConsequence(
        p, q, prefix, base, depth, common, u, v, residual, height, rad_uv,
        constant, lower, distance_lower, actual,
    )
