"""Exact arithmetic checks and budgets for effective primitive abc means.

Universal authority is the paper proof ABC_EFFECTIVE_MEAN.md, not successful
execution or these immutable data records. No float is accepted as an exact
parameter. The primitive count uses full Mobius inversion, including k sharing
prime factors with the divisor modulus.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_triple_moment import power_enclosure
from .cloud_abc_correlations import MomentBudget, mobius, moment_budget


def _rational(value: int | Fraction, name: str, minimum: int = 0) -> Fraction:
    if type(value) not in (int, Fraction) or value < minimum:
        raise ValueError(f"{name} must be an int or Fraction >= {minimum}")
    return Fraction(value)


def _moduli(d: int, e: int, f: int) -> None:
    if any(type(n) is not int or n < 1 for n in (d, e, f)):
        raise ValueError("moduli must be positive integers")
    if any(gcd(a, b) != 1 for a, b in ((d, e), (d, f), (e, f))):
        raise ValueError("moduli must be pairwise coprime")


def harmonic(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError("harmonic index must be a positive integer")
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction())


def raw_divisor_count(X: int | Fraction, d: int, e: int, f: int) -> int:
    """Count positive a+b<=X, d|a, e|b, f|(a+b), without primitivity.

    Slice a=d*u; the residual variable v=b/e lies in one residue mod f.
    """
    X = _rational(X, "X")
    _moduli(d, e, f)
    inverse = 0 if f == 1 else pow(e, -1, f)
    total = 0
    for u in range(1, X // d + 1):
        residue = (-d * u * inverse) % f
        first = residue or f
        cap = (X - d * u) // e
        if cap >= first:
            total += 1 + (cap - first) // f
    return total


def raw_discrepancy_bound(X: int | Fraction, d: int, e: int, f: int) -> Fraction:
    """Proved bound for |M_X-X^2/(2def)|; valid for all modulus sizes."""
    X = _rational(X, "X")
    _moduli(d, e, f)
    return X / d + X / (2 * e * f)


def primitive_divisor_count_mobius(
    X: int | Fraction, d: int, e: int, f: int,
) -> int:
    """Exact primitive count by Mobius inversion after reducing ALL moduli."""
    X = _rational(X, "X")
    _moduli(d, e, f)
    return sum(
        mobius(k) * raw_divisor_count(
            X / k, d // gcd(d, k), e // gcd(e, k), f // gcd(f, k)
        )
        for k in range(1, X // 2 + 1)
    )


@dataclass(frozen=True)
class PrimitiveDivisorBudget:
    """Rational finite center and two different, explicitly named errors.

    |N_X - finite_center| <= lattice_error.
    |rho_D*X^2/2 - finite_center| <= density_tail.
    Hence |N_X-rho_D*X^2/2| <= discrepancy. rho_D is an infinite density,
    not an exactly computed rational number in this record.
    """
    X: Fraction
    d: int
    e: int
    f: int
    M: int
    finite_center: Fraction
    lattice_error: Fraction
    density_tail: Fraction

    @property
    def discrepancy(self) -> Fraction:
        return self.lattice_error + self.density_tail

    @property
    def normalized_discrepancy(self) -> Fraction:
        return self.discrepancy / self.X**2


def primitive_divisor_budget(
    X: int | Fraction, d: int, e: int, f: int,
) -> PrimitiveDivisorBudget:
    """Uniform absolute discrepancy, with NO dependency of the error on def."""
    X = _rational(X, "X", 2)
    _moduli(d, e, f)
    D = d * e * f
    M = X // 2
    finite_center = X**2 / (2 * D) * sum(
        (Fraction(mobius(k) * gcd(D, k), k*k) for k in range(1, M + 1)),
        Fraction(),
    )
    return PrimitiveDivisorBudget(
        X, d, e, f, M, finite_center, 3 * X * harmonic(M) / 2,
        X**2 / (2 * M),
    )


@dataclass(frozen=True)
class EffectiveRateParameters:
    """The proved log-rate exponent; not a formal proof authority token."""
    t: Fraction
    h: Fraction
    s: Fraction
    alpha: Fraction
    beta: Fraction
    rate: Fraction
    cutoff_power: Fraction


def effective_rate_parameters(
    t: int | Fraction, h: int | Fraction | None = None,
) -> EffectiveRateParameters:
    """Choose s=2/3-h and alpha=(1+t+h)/2; 0<h<2/3-t.

    Error <= C*((1+log X)/X)**rate, with C specified in the dossier.
    The supremum (2-3t)/5 is NOT asserted to be attained.
    """
    t = _rational(t, "t")
    gap = Fraction(2, 3) - t
    if gap <= 0:
        raise ValueError("proved moment range is 0 <= t < 2/3")
    h = gap / 2 if h is None else _rational(h, "h")
    if not 0 < h < gap:
        raise ValueError("need 0 < h < 2/3-t")
    s = Fraction(2, 3) - h
    alpha = (1 + t + h) / 2
    beta = (s - t) / 2
    return EffectiveRateParameters(t, h, s, alpha, beta,
                                   beta / (alpha + beta), 1 / (alpha + beta))


def euler_constant_power(
    t: int | Fraction, alpha: int | Fraction, *, precision: int = 10**6,
) -> int:
    """Integer E with the product E(t,alpha) <= 2**E, by rational root bounds.

    Requires alpha>t and 2alpha-t>1. Uses exp(u)<4**u; deliberately loose.
    """
    t = _rational(t, "t")
    alpha = _rational(alpha, "alpha")
    if alpha <= t or 2 * alpha - t <= 1:
        raise ValueError("need alpha>t and 2*alpha-t>1")
    if type(precision) is not int or precision < 1:
        raise ValueError("precision must be a positive integer")
    exponent = alpha - t
    lower, _ = power_enclosure(2, exponent.numerator, exponent.denominator, precision)
    if lower <= 1:
        raise ValueError("increase precision to separate 2**(alpha-t) from 1")
    exp_upper = 3 / ((2 * alpha - t - 1) * (1 - 1 / lower))
    two_power = 2 * exp_upper
    return -((-two_power.numerator) // two_power.denominator)


@dataclass(frozen=True)
class EffectiveConstantBudget:
    """Encoded constant <= (7/2)*2**euler_power + 2*moment.constant_upper()."""
    parameters: EffectiveRateParameters
    euler_power: int
    moment: MomentBudget

    def constant_upper(self) -> Fraction:
        """Materialize a potentially very large but exact rational majorant."""
        return Fraction(7, 2) * 2**self.euler_power + 2 * self.moment.constant_upper()


def effective_constant_budget(
    t: int | Fraction, h: int | Fraction | None = None,
    *, precision: int = 10**6,
) -> EffectiveConstantBudget:
    """Certified rational encoding of the constant in the logarithmic rate."""
    parameters = effective_rate_parameters(t, h)
    return EffectiveConstantBudget(
        parameters,
        euler_constant_power(parameters.t, parameters.alpha, precision=precision),
        moment_budget(parameters.s, precision=precision),
    )


def dyadic_first_moment_lower(X: int | Fraction, K: int) -> int:
    """Exact finite lower bound for S_1(X), hence for every S_t(X) with t>=1.

    Retain the three single-slot powers 2**k, 2<=k<=K, in the positive
    divisor expansion. This evaluates finite counts, not an infinite theorem.
    """
    X = _rational(X, "X", 2)
    if type(K) is not int or K < 2:
        raise ValueError("K must be an integer >= 2")
    return sum(
        2**(k-2) * sum(
            primitive_divisor_count_mobius(X, *moduli)
            for moduli in ((2**k,1,1), (1,2**k,1), (1,1,2**k))
        )
        for k in range(2, K+1)
    )
