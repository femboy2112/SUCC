"""Exact data for the original BBP Dirichlet resolvent.

The universal analytic proofs are in BBP_DIRICHLET_RESOLVENT.md.  This module
provides rational certificates and bounds, not a numerical continuation oracle
or a signed Weyl estimate.  The forcing itself is imported from the source.
"""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction as Q
from math import comb, factorial

from .pi_source_collision import bbp_forcing


POLES = (Q(7, 8), Q(1, 2), Q(3, 8), Q(1, 4))
WEIGHTS = (Q(1, 2), Q(-1, 4), Q(-1, 8), Q(-1, 8))
# Ascending powers; Q(T) F(s) = P(T) zeta(s), T f(s) = f(s-1).
SHIFT_DENOMINATOR = (Q(21, 512), Q(-103, 256), Q(89, 64), Q(-2), Q(1))
SHIFT_NUMERATOR = (Q(1, 32), Q(-89, 512), Q(15, 64))
FINITE_PART_BASIS = ("1", "gamma", "pi", "sqrt(2)*pi", "log(2)",
                     "sqrt(2)*log(1+sqrt(2))")


def _integer(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def _rational(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("integer or Fraction required")
    return Q(value)


def polynomial_value(coefficients: tuple[Q, ...], argument: int | Q) -> Q:
    """Evaluate ascending rational polynomial coefficients exactly."""
    x = _rational(argument)
    result = Q(0)
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def source_shift_identity(n: int) -> tuple[Q, Q]:
    """Both sides of Q(n) r(n) = P(n), using the imported original r."""
    _integer(n, 1)
    return (polynomial_value(SHIFT_DENOMINATOR, n) * bbp_forcing(n),
            polynomial_value(SHIFT_NUMERATOR, n))


def asymptotic_coefficient(k: int) -> Q:
    """a_k in r(n)=sum_(k>=1) a_k/n^k; a_1=0, a_k>0 for k>=2."""
    _integer(k, 1)
    return sum((w * b ** (k - 1) for w, b in zip(WEIGHTS, POLES)), Q(0))


def pole_residue(m: int) -> Q:
    """Residue of F at s=-m, m>=1; no seed is an input to this object."""
    return asymptotic_coefficient(_integer(m, 1) + 1)


def coefficient_bounds(k: int) -> tuple[Q, Q]:
    """Universal positive bounds (15/56) q^(k-1) <= a_k < q^(k-1)/2."""
    _integer(k, 2)
    power = Q(7, 8) ** (k - 1)
    return Q(15, 56) * power, power / 2


def coefficient_recurrence_residual(k: int) -> Q:
    """Zero for all k>=1 by the four source pole roots of Q."""
    _integer(k, 1)
    return sum((q * asymptotic_coefficient(k + j)
                for j, q in enumerate(SHIFT_DENOMINATOR)), Q(0))


def source_jet(n: int, terms: int) -> Q:
    _integer(n, 1)
    _integer(terms, 1)
    return sum((asymptotic_coefficient(k) / n ** k
                for k in range(1, terms + 1)), Q(0))


def source_jet_remainder_bound(n: int, terms: int) -> Q:
    """0 < r(n)-jet <= q^terms/[2*n^terms*(n-q)], q=7/8."""
    _integer(n, 1)
    _integer(terms, 1)
    q = Q(7, 8)
    return q ** terms / (2 * n ** terms * (n - q))


def zeta_expansion_tail_bound(terms: int, real_part_lower: int | Q) -> Q:
    """Uniform absolute tail for sum_(k>terms) a_k zeta(s+k).

    Valid on Re(s)>=sigma when terms+sigma>0.  This rational bound does
    not enclose floating-point evaluation errors of the retained terms.
    """
    _integer(terms, 1)
    sigma = _rational(real_part_lower)
    if terms + sigma <= 0:
        raise ValueError("terms + real_part_lower must be positive")
    return 4 * Q(7, 8) ** terms * (1 + 1 / (terms + sigma))


@lru_cache(maxsize=None)
def bernoulli_number(index: int) -> Q:
    """Classical B_n, with B_1=-1/2, by its triangular rational recurrence."""
    _integer(index)
    if index == 0:
        return Q(1)
    return -sum((comb(index + 1, k) * bernoulli_number(k)
                 for k in range(index)), Q(0)) / (index + 1)


def zeta_nonpositive(index: int) -> Q:
    """The classical exact value zeta(-index), index>=0."""
    _integer(index)
    return (-1) ** index * bernoulli_number(index + 1) / (index + 1)


def finite_part_basis_coefficients(m: int) -> tuple[Q, ...]:
    """Laurent constant of F(s) at s=-m in FINITE_PART_BASIS.

    m=0 is the ordinary value F(0), not a pole.  This is exact symbolic
    data; the constants in the basis are not asserted independent.
    """
    _integer(m)
    t1, t2, t3, t4 = (w * b ** m for w, b in zip(WEIGHTS, POLES))
    rational = sum((asymptotic_coefficient(j + 1) * zeta_nonpositive(m - 1 - j)
                    for j in range(m)), Q(0))
    return (rational, t1 + t2 + t3 + t4, (t1 + t3 - t4) / 2,
            (t1 - t3) / 2, 4 * t1 + 2 * t2 + 4 * t3 + 3 * t4, t1 - t3)


def gamma_regularized_negative_value(m: int) -> Q:
    """Exact entire value (F/Gamma(s+1))(-m), m>=1."""
    _integer(m, 1)
    return (-1) ** (m - 1) * factorial(m - 1) * pole_residue(m)


def moment_matched_altered_forcing(n: int) -> Q:
    """HOSTILE CONTROL: positive wrong source with the first two residues.

    Replaces numerator A by A-3/5, preserving the four pole locations and
    a_1,a_2,a_3, while changing a_4.  It must never drive the genuine orbit.
    """
    _integer(n, 1)
    return bbp_forcing(n) - Q(3, 5) / (
        (2 * n - 1) * (4 * n - 1) * (8 * n - 7) * (8 * n - 3))
