"""Exact successor graphs for the central SU(2) Haar and Wilson state.

The paper contract is qm_graph_bridge/SUCC_CHARACTER_PROOF.md in the
2026-11-13 Yang--Mills dossier.  Index zero here represents the existing
positive-integer carrier's e_1.  J=(S+S*)/2 is a trace observable, not the
physical Yang--Mills Hamiltonian.  All finite outputs use rational arithmetic.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial
from typing import Sequence


def _natural(value: int) -> int:
    if type(value) is not int or value < 0:
        raise ValueError("an exact nonnegative integer is required")
    return value


def _rational(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise TypeError("exact int/Fraction required; no float or bool")
    return Q(value)


def _polynomial(coefficients: Sequence[int | Q]) -> tuple[Q, ...]:
    result = tuple(_rational(c) for c in coefficients)
    while len(result) > 1 and result[-1] == 0:
        result = result[:-1]
    return result or (Q(0),)


def jacobi_action(vector: Sequence[int | Q]) -> tuple[Q, ...]:
    """J_N on indices 0,...,N, with both open boundaries retained."""
    v = tuple(_rational(x) for x in vector)
    if not v:
        raise ValueError("a nonempty finite carrier is required")
    return tuple(
        ((v[j - 1] if j else Q(0))
         + (v[j + 1] if j + 1 < len(v) else Q(0))) / 2
        for j in range(len(v))
    )


def graph_return_moment(power: int, cutoff: int | None = None) -> Q:
    """Weight of all length-power return walks from zero on the half-line.

    Each edge has amplitude 1/2.  A finite cutoff gives indices 0,...,cutoff.
    Omitting it includes every vertex reachable in the requested finite walk.
    """
    _natural(power)
    cutoff = power if cutoff is None else _natural(cutoff)
    counts = {0: 1}
    for _ in range(power):
        next_counts: dict[int, int] = {}
        for vertex, count in counts.items():
            if vertex:
                next_counts[vertex - 1] = next_counts.get(vertex - 1, 0) + count
            if vertex < cutoff:
                next_counts[vertex + 1] = next_counts.get(vertex + 1, 0) + count
        counts = next_counts
    return Q(counts.get(0, 0), 2**power)


def chebyshev_character(degree: int) -> tuple[Q, ...]:
    """Polynomial U_degree = character of the SU(2) spin-degree/2 irrep."""
    _natural(degree)
    if degree == 0:
        return (Q(1),)
    previous, current = (Q(1),), (Q(0), Q(2))
    for _ in range(1, degree):
        following = [Q(0)] + [2 * c for c in current]
        for j, c in enumerate(previous):
            following[j] -= c
        previous, current = current, tuple(following)
    return current


def polynomial_action(
    coefficients: Sequence[int | Q], vector: Sequence[int | Q]
) -> tuple[Q, ...]:
    """Horner evaluation of f(J_N) on a declared finite vector."""
    p = _polynomial(coefficients)
    v = tuple(_rational(x) for x in vector)
    if not v:
        raise ValueError("a nonempty finite carrier is required")
    result = tuple(Q(0) for _ in v)
    for c in reversed(p):
        result = tuple(a + c * b for a, b in zip(jacobi_action(result), v))
    return result


def required_cutoff(taylor_degree: int, observable_degree: int) -> int:
    """Smallest uniform horizon paying the polynomial moment degree budget."""
    return _natural(taylor_degree) + _natural(observable_degree) // 2


def wilson_graph_vector(
    beta: int | Q, taylor_degree: int, cutoff: int | None = None
) -> tuple[Q, ...]:
    """Unnormalized P_K((beta/2) J_N)e_0; keep normalization as a metric.

    For N>=K this is exactly the finitely supported vector in the infinite
    character carrier.  Squared norm is rational and at least one.
    """
    beta = _rational(beta)
    _natural(taylor_degree)
    cutoff = taylor_degree if cutoff is None else _natural(cutoff)
    if cutoff < taylor_degree:
        raise ValueError("cutoff must retain every Taylor-amplitude path")
    term = (Q(1),) + (Q(0),) * cutoff
    vector = term
    for k in range(1, taylor_degree + 1):
        term = tuple(beta * x / (2 * k) for x in jacobi_action(term))
        vector = tuple(a + b for a, b in zip(vector, term))
    return vector


def pure_state_error_bound(
    beta: int | Q, taylor_degree: int, observable_bound: int | Q
) -> Q:
    """Proved error for a bounded observable in the normalized vector state.

    Caller supplies M >= operator norm.  The bound is
    4 M 3^ceil(|beta|/2) (|beta|/2)^(K+1)/(K+1)!.
    It can be loose.  For polynomial graph evaluation, the horizon must also
    satisfy required_cutoff(K,degree); build_wilson_certificate enforces this.
    """
    half_beta = abs(_rational(beta)) / 2
    _natural(taylor_degree)
    bound = _rational(observable_bound)
    if bound < 0:
        raise ValueError("observable norm bound must be nonnegative")
    ceiling = (half_beta.numerator + half_beta.denominator - 1) // half_beta.denominator
    return (4 * bound * 3**ceiling * half_beta**(taylor_degree + 1)
            / factorial(taylor_degree + 1))


def wilson_graph_expectation(
    beta: int | Q,
    taylor_degree: int,
    coefficients: Sequence[int | Q],
    cutoff: int | None = None,
) -> Q:
    """Exact rational approximation to the single-plaquette Wilson moment."""
    p = _polynomial(coefficients)
    minimum = required_cutoff(taylor_degree, len(p) - 1)
    cutoff = minimum if cutoff is None else _natural(cutoff)
    if cutoff < minimum:
        raise ValueError("cutoff does not pay the observable's moment horizon")
    v = wilson_graph_vector(beta, taylor_degree, cutoff)
    norm = sum((x * x for x in v), Q(0))
    fv = polynomial_action(p, v)
    return sum((x * y for x, y in zip(v, fv)), Q(0)) / norm


@dataclass(frozen=True)
class WilsonGraphCertificate:
    """Finite exact data plus a bound justified by the separate paper proof."""

    beta: Q
    polynomial: tuple[Q, ...]
    tolerance: Q
    taylor_degree: int
    cutoff: int
    unnormalized_vector: tuple[Q, ...]
    norm_squared: Q
    expectation: Q
    error_bound: Q


def build_wilson_certificate(
    beta: int | Q, coefficients: Sequence[int | Q], tolerance: int | Q
) -> WilsonGraphCertificate:
    """Terminating exact construction for rational beta, polynomial and epsilon.

    This computes a finite graph approximation of one Wilson observable.
    It is not a certificate for a four-dimensional QFT or its mass gap.
    """
    beta = _rational(beta)
    p = _polynomial(coefficients)
    tolerance = _rational(tolerance)
    if tolerance <= 0:
        raise ValueError("a strictly positive rational tolerance is required")
    bound = sum((abs(c) for c in p), Q(0))
    degree = 0
    error = pure_state_error_bound(beta, degree, bound)
    while error > tolerance:
        degree += 1
        error = pure_state_error_bound(beta, degree, bound)
    cutoff = required_cutoff(degree, len(p) - 1)
    vector = wilson_graph_vector(beta, degree, cutoff)
    norm = sum((x * x for x in vector), Q(0))
    return WilsonGraphCertificate(
        beta, p, tolerance, degree, cutoff, vector, norm,
        wilson_graph_expectation(beta, degree, p, cutoff), error,
    )
