"""Exact q-product seam certificates; no source-selection or normality claim.

For an affine recurrence with multiplier b=1/q, the normalized coefficient
of X0 in XN-lambda*X0 is 1-lambda*q**N. Aggregation across horizons is a
declared product, not the determinant of an asserted infinite BBP operator.
See research/2026-10-25/QGAMMA_SEAM_DETERMINANT.md for the analytic proofs.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import prod

from .zero_one_gamma_bridge import RationalInterval, log_positive_interval


def _exact(value):
    if type(value) not in (int, Q):
        raise ValueError("exact int or Fraction required")
    return Q(value)


def _q(value):
    value = _exact(value)
    if not 0 < value < 1:
        raise ValueError("require 0 < q < 1")
    return value


def _index(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError("integer index in the declared domain required")
    return value


def normalized_seam_coefficient(q, horizon: int, twist=-1) -> Q:
    """1-lambda*q**N, valid for N>=1 and any exact rational lambda."""
    q = _q(q)
    _index(horizon, 1)
    twist = _exact(twist)
    return 1-twist*q**horizon


def finite_seam_product(q, horizons: int, twist=-1) -> Q:
    """The declared product over N=1..M, including its empty value1."""
    q = _q(q)
    _index(horizons)
    twist = _exact(twist)
    return prod((1-twist*q**n for n in range(1, horizons+1)), start=Q(1))


def antiperiodic_factorization(q, horizons: int) -> tuple[Q, Q]:
    """Return independently factored plus product and doubled/minus ratio."""
    q = _q(q)
    _index(horizons)
    plus = finite_seam_product(q, horizons, -1)
    ratio = finite_seam_product(q*q, horizons, 1)/finite_seam_product(q, horizons, 1)
    return plus, ratio


def antiperiodic_product_interval(q, horizons: int) -> RationalInterval:
    """Strict rational enclosure of product_(N>=1)(1+q**N).

    For S=q**(M+1)/(1-q)<1, the tail product lies strictly between
    1+S and 1/(1-S). An insufficient horizon is rejected explicitly.
    """
    q = _q(q)
    _index(horizons)
    head = finite_seam_product(q, horizons, -1)
    tail_mass = q**(horizons+1)/(1-q)
    if tail_mass >= 1:
        raise ValueError("increase horizon until q**(M+1)/(1-q) < 1")
    return RationalInterval(head*(1+tail_mass), head/(1-tail_mass))


def qgamma_integer(q, argument: int) -> Q:
    """Gamma_q(k), k>=1, from the finite q-factorial recurrence."""
    q = _q(q)
    _index(argument, 1)
    return prod(((1-q**n)/(1-q) for n in range(1, argument)), start=Q(1))


def shifted_twist_gamma_ratio(q, argument: int) -> tuple[Q, Q]:
    """Two exact forms of P_q(k)/P_q(1), for positive integer k.

    Cancelling finitely many plus factors gives the first value; the
    q-Gamma quotient (1+q)**(1-k)*Gamma_q(k)/Gamma_(q*q)(k) gives the second.
    """
    q = _q(q)
    _index(argument, 1)
    direct = 1/finite_seam_product(q, argument-1, -1)
    gamma = (1+q)**(1-argument)*qgamma_integer(q, argument)/qgamma_integer(q*q, argument)
    return direct, gamma


def periodic_lambert_interval(q, terms: int) -> RationalInterval:
    """Strict rational enclosure of sum_(N>=1) q**N/(1-q**N).

    The omitted denominators lie between 1-q**(terms+1) and1.
    This certifies an infinite tail; finite sampling does not supply it.
    """
    q = _q(q)
    _index(terms)
    head = sum((q**n/(1-q**n) for n in range(1, terms+1)), Q())
    geometric = q**(terms+1)/(1-q)
    return RationalInterval(head+geometric, head+geometric/(1-q**(terms+1)))


def q_euler_constant_interval(q, terms: int=12, log_terms: int=40) -> RationalInterval:
    """Certified gamma_q=-psi_q(1), not the ordinary Euler constant at fixed q.

    gamma_q=log(1-q)-log(q)*sum_(N>=1)q**N/(1-q**N).
    Its q->1 limit is a separate paper theorem, not asserted by this code.
    """
    q = _q(q)
    lambert = periodic_lambert_interval(q, terms)
    first = log_positive_interval(1-q, terms=log_terms)
    log_q = log_positive_interval(q, terms=log_terms)
    negative_log = RationalInterval(-log_q.upper, -log_q.lower)
    products = tuple(x*y for x in (negative_log.lower, negative_log.upper)
                     for y in (lambert.lower, lambert.upper))
    return first.add(RationalInterval(min(products), max(products)))
