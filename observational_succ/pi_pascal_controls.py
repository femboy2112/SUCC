"""Exact finite controls for the Pascal-to-real-distribution boundary.

The moment constructor changes the BBP forcing.  It certifies only the
displayed finite jet constraints; its infinite extension is a paper theorem.
No numerical integration or floating decisions are used.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import ceil, comb, factorial
from typing import Sequence


def _natural(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def _exact(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def valuation_two(value: int | Q) -> int | None:
    """Exact valuation; None denotes the infinite valuation of zero."""
    value = _exact(value)
    if not value:
        return None
    n, d = abs(value.numerator), value.denominator
    return (n & -n).bit_length() - (d & -d).bit_length()


def weighted_moment(power: int) -> Q:
    """Integral_0^1 x^power (1-x) dx."""
    _natural(power)
    return Q(1, (power + 1) * (power + 2))


def polynomial_inner(left: Sequence[Q], right: Sequence[Q]) -> Q:
    return sum((_exact(a) * _exact(b) * weighted_moment(i + j)
                for i, a in enumerate(left) for j, b in enumerate(right)), Q())


def monic_moment_polynomials(depth: int) -> tuple[tuple[Q, ...], ...]:
    """Rational Gram-Schmidt for weight 1-x on [0,1], degrees 0..depth."""
    _natural(depth)
    result: list[tuple[Q, ...]] = []
    for n in range(depth + 1):
        current = [Q()] * n + [Q(1)]
        for previous in result:
            scale = polynomial_inner(current, previous) / polynomial_inner(previous, previous)
            for j, coefficient in enumerate(previous):
                current[j] -= scale * coefficient
        result.append(tuple(current))
    return tuple(result)


def rational_coset_near(
    center: Q | int, reference: Q | int, bits: int, tolerance: Q | int
) -> Q:
    """Meet a real interval and reference+2^bits Z_(2), using an odd denominator."""
    center, reference, tolerance = map(_exact, (center, reference, tolerance))
    _natural(bits)
    if tolerance <= 0 or reference.denominator % 2 == 0:
        raise ValueError("positive tolerance and 2-integral reference required")
    step = 1 << bits
    denominator = 2 * ceil(Q(step) / tolerance) + 1
    scaled = (center - reference) * denominator / step
    nearest = (scaled + Q(1, 2)).__floor__()
    answer = reference + Q(step * nearest, denominator)
    if not abs(answer - center) < tolerance:
        raise ArithmeticError("real approximation certificate failed")
    if ((answer - reference) / step).denominator % 2 == 0:
        raise ArithmeticError("dyadic congruence certificate failed")
    return answer


@dataclass(frozen=True)
class FiniteMomentCountermodel:
    """A positive polynomial density and its first certified Newton jets.

    The real moment sequence is defined at all nonnegative integers.  The
    dyadic jet constraints are certified only through len(reference).
    """

    density: tuple[Q, ...]
    reference: tuple[Q, ...]
    newton: tuple[Q, ...]
    precision: int
    perturbations: tuple[Q, ...]
    disc_norms: tuple[Q, ...]
    perturbation_bound: Q

    @property
    def depth(self) -> int:
        return len(self.reference)

    def moment(self, index: int) -> Q:
        _natural(index)
        return sum((a * weighted_moment(index + j)
                    for j, a in enumerate(self.density)), Q())

    def unwrapped(self, index: int) -> Q:
        _natural(index)
        return Q(16**index) - self.moment(index)

    def forcing(self, index: int) -> Q:
        _natural(index, 1)
        return 16 * self.moment(index - 1) - self.moment(index)

    def phase(self, index: int) -> Q:
        return self.unwrapped(index) % 1


def positive_moment_countermodel(
    reference: Sequence[Q | int], precision: int
) -> FiniteMomentCountermodel:
    """Match normalized authentic Newton jets to prescribed dyadic precision.

    reference[n-1] must have exact valuation n-1.  The returned a_n obeys
    a_n-reference[n-1] in 2^(n-1+precision) Z_(2).  A rational positive
    polynomial density w gives eta_n=int x^n(1-x)w(x)dx and H_n=16^n-eta_n.
    Orthogonality preserves every earlier moment as the construction grows.

    Norms on complex disks of radius n support the paper's entire-kernel
    infinite extension; a finite return is not a certificate for all jets.
    """
    _natural(precision, 1)
    refs = tuple(_exact(x) for x in reference)
    if not refs or any(valuation_two(x) != n - 1 for n, x in enumerate(refs, 1)):
        raise ValueError("nonempty reference with valuation n-1 required")
    polynomials = monic_moment_polynomials(len(refs))
    density = [Q(2)]
    newton: list[Q] = []
    perturbations: list[Q] = []
    norms: list[Q] = []
    total_bound = Q()
    for n, ref in enumerate(refs, 1):
        polynomial = polynomials[n]
        beta = sum((a * weighted_moment(n + j)
                    for j, a in enumerate(polynomial)), Q())
        if beta <= 0 or beta != polynomial_inner(polynomial, polynomial):
            raise ArithmeticError("orthogonality certificate failed")
        moment = sum((a * weighted_moment(n + j)
                      for j, a in enumerate(density)), Q())
        previous = sum((a * Q(factorial(n), factorial(n - j))
                        for j, a in enumerate(newton, 1)), Q())
        current = (16**n - moment - previous) / factorial(n)
        disc_norm = sum((abs(a) * n**j for j, a in enumerate(polynomial)), Q())
        budget = Q(1, 2**(n + 1))
        tolerance = beta * budget / (factorial(n) * disc_norm)
        chosen = rational_coset_near(current, ref, n - 1 + precision, tolerance)
        coefficient = (current - chosen) * factorial(n) / beta
        cost = abs(coefficient) * disc_norm
        if not cost < budget or valuation_two(chosen) != n - 1:
            raise ArithmeticError("density/jet certificate failed")
        density += [Q()] * (n + 1 - len(density))
        for j, a in enumerate(polynomial):
            density[j] += coefficient * a
        newton.append(chosen)
        perturbations.append(coefficient)
        norms.append(disc_norm)
        total_bound += cost
    if not total_bound < Q(1, 2):
        raise ArithmeticError("positive-density certificate failed")
    return FiniteMomentCountermodel(
        tuple(density), refs, tuple(newton), precision,
        tuple(perturbations), tuple(norms), total_bound,
    )


def pascal_weights(order: int) -> tuple[Q, ...]:
    _natural(order)
    return tuple(Q(comb(order, j), 2**order) for j in range(order + 1))


def pascal_window_average(
    values: Sequence[int | Q], window_length: int, order: int
) -> Q:
    """Average normalized Pascal translates of one finite observable window."""
    _natural(window_length, 1)
    weights = pascal_weights(order)
    values = tuple(_exact(x) for x in values)
    if len(values) != window_length + order:
        raise ValueError("exactly window_length+order samples required")
    return sum((weight * sum(values[j:j + window_length], Q()) / window_length
                for j, weight in enumerate(weights)), Q())


def pascal_endpoint_budget(
    window_length: int, order: int, absolute_bound: int | Q
) -> Q:
    """m*M/N, with all endpoints retained; it is not a mixing estimate."""
    _natural(window_length, 1)
    _natural(order)
    bound = _exact(absolute_bound)
    if bound < 0:
        raise ValueError("nonnegative absolute observable bound required")
    return Q(order, window_length) * bound
