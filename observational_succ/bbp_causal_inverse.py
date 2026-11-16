"""Exact causal convolution inverses of the original four-pole source.

For q(t)=4-2*exp(-3t)-exp(-4t)-exp(-5t), the causal extension H(t)q(t) has
Laplace transform
N(a)/D(a), with N=(240,121,15) and D=(0,60,47,12,1) in ascending powers.
Order m represents its m-fold convolution inverse, whose transform is
D(a)**m/N(a)**m. Polynomial division retains delta derivatives separately
from the proper rational transfer encoding the decaying regular part.

The order is a deconvolution order, not a negative BBP time. Derivatives
at the causal endpoint are essential, and no bounded/noise-stable inverse
on arbitrary continuous data is claimed. All arithmetic here is rational.
Proofs: research/2026-11-15/causal_negative_orders/CONSTRUCTOR_NOTES.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence


MAX_INVERSE_ORDER = 8
MAX_JET_ORDER = 32
SOURCE_NUMERATOR = (Q(240), Q(121), Q(15))
SOURCE_DENOMINATOR = (Q(0), Q(60), Q(47), Q(12), Q(1))

Polynomial = tuple[Q, ...]


def _exact(value: int | Q, name: str) -> Q:
    if type(value) not in (int, Q):
        raise TypeError(f"{name} must be an int or Fraction")
    return Q(value)


def _natural(value: int, name: str, maximum: int) -> int:
    if type(value) is not int or not 0 <= value <= maximum:
        raise ValueError(f"{name} must be an integer in [0, {maximum}]")
    return value


def _trim(coefficients: Sequence[Q]) -> Polynomial:
    values = list(coefficients)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (Q(0),)


def _polynomial(value: Polynomial, name: str) -> Polynomial:
    if type(value) is not tuple or not value:
        raise TypeError(f"{name} must be a nonempty coefficient tuple")
    if len(value) > 4 * MAX_INVERSE_ORDER + 1:
        raise ValueError(f"{name} exceeds the polynomial budget")
    return _trim(tuple(_exact(v, name) for v in value))


def _add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Q(0)] * max(len(left), len(right))
    for i, coefficient in enumerate(left):
        result[i] += coefficient
    for i, coefficient in enumerate(right):
        result[i] += coefficient
    return _trim(result)


def _multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return _trim(result)


def _power(value: Polynomial, exponent: int) -> Polynomial:
    result = (Q(1),)
    for _ in range(exponent):
        result = _multiply(result, value)
    return result


def _divide(numerator: Polynomial, denominator: Polynomial) -> tuple[Polynomial, Polynomial]:
    if denominator == (Q(0),):
        raise ZeroDivisionError("zero polynomial denominator")
    remainder = list(numerator)
    quotient = [Q(0)] * max(1, len(numerator) - len(denominator) + 1)
    while remainder != [Q(0)] and len(remainder) >= len(denominator):
        degree = len(remainder) - len(denominator)
        coefficient = remainder[-1] / denominator[-1]
        quotient[degree] += coefficient
        for i, value in enumerate(denominator):
            remainder[degree + i] -= coefficient * value
        remainder = list(_trim(remainder))
    return _trim(quotient), _trim(remainder)


def _evaluate(polynomial: Polynomial, argument: Q) -> Q:
    result = Q(0)
    for coefficient in reversed(polynomial):
        result = argument * result + coefficient
    return result


def source_laplace(argument: int | Q) -> Q:
    """Original integral int_0^infinity exp(-a*t)*q(t) dt, for rational a>0."""
    argument = _exact(argument, "Laplace argument")
    if argument <= 0:
        raise ValueError("the original source requires a positive Laplace argument")
    return _evaluate(SOURCE_NUMERATOR, argument) / _evaluate(SOURCE_DENOMINATOR, argument)


@dataclass(frozen=True)
class CausalInverseKernel:
    """Source-authenticated delta polynomial plus a regular rational transfer.

    delta_polynomial[k] is the coefficient of delta^(k), with action
    <delta^(k), phi> = (-1)**k * phi^(k)(0). The remaining numerator divided
    by remaining denominator is the Laplace transform of a smooth,
    exponentially decaying function on t>=0. Coefficients ascend in powers.
    """

    order: int
    delta_polynomial: Polynomial
    remainder_numerator: Polynomial
    remainder_denominator: Polynomial

    def __post_init__(self) -> None:
        _natural(self.order, "inverse order", MAX_INVERSE_ORDER)
        delta = _polynomial(self.delta_polynomial, "delta polynomial")
        numerator = _polynomial(self.remainder_numerator, "remainder numerator")
        denominator = _polynomial(self.remainder_denominator, "remainder denominator")
        if len(delta) > 2 * self.order + 1:
            raise ValueError("delta order exceeds the authentic source order")
        if numerator != (Q(0),) and len(numerator) >= len(denominator):
            raise ValueError("the regular remainder must be a proper rational function")
        expected_denominator = _power(SOURCE_NUMERATOR, self.order)
        expected_numerator = _power(SOURCE_DENOMINATOR, self.order)
        if denominator != expected_denominator:
            raise ValueError("the canonical original-source denominator was changed")
        if _add(_multiply(delta, denominator), numerator) != expected_numerator:
            raise ValueError("the original-source inverse identity was changed")
        object.__setattr__(self, "delta_polynomial", delta)
        object.__setattr__(self, "remainder_numerator", numerator)
        object.__setattr__(self, "remainder_denominator", denominator)

    @property
    def full_numerator(self) -> Polynomial:
        return _add(_multiply(self.delta_polynomial, self.remainder_denominator),
                    self.remainder_numerator)

    def laplace(self, argument: int | Q) -> Q:
        """Evaluate the inverse transform for rational a>=0.

        At a=0 the inverse transform remains defined; source_laplace(0)
        is not defined because the original source has infinite total mass.
        """
        argument = _exact(argument, "Laplace argument")
        if argument < 0:
            raise ValueError("nonnegative Laplace argument required")
        return (_evaluate(self.delta_polynomial, argument)
                + _evaluate(self.remainder_numerator, argument)
                / _evaluate(self.remainder_denominator, argument))

    def singular_pairing(self, endpoint_jet: Sequence[int | Q]) -> Q:
        """Action of the delta polynomial only on supplied phi^(k)(0) values."""
        if len(endpoint_jet) != len(self.delta_polynomial):
            raise ValueError("the supplied endpoint jet must match the delta degree")
        jet = tuple(_exact(value, "endpoint derivative") for value in endpoint_jet)
        return sum((coefficient * (-1)**k * jet[k]
                    for k, coefficient in enumerate(self.delta_polynomial)), Q(0))

    def remainder_jet(self, last_order: int) -> tuple[Q, ...]:
        """Return g(0),...,g^(last_order)(0) for the smooth regular remainder.

        These are derivatives, not Taylor coefficients. The recurrence comes
        from its proper rational Laplace transfer expanded at a=infinity.
        """
        _natural(last_order, "last derivative order", MAX_JET_ORDER)
        denominator = self.remainder_denominator
        numerator = self.remainder_numerator
        degree = len(denominator) - 1
        result: list[Q] = []
        for n in range(last_order + 1):
            index = degree - 1 - n
            target = numerator[index] if 0 <= index < len(numerator) else Q(0)
            correction = sum(
                (denominator[degree - j] * result[n - j]
                 for j in range(1, min(n, degree) + 1)),
                Q(0),
            )
            result.append((target - correction) / denominator[-1])
        return tuple(result)

    def convolve(self, other: CausalInverseKernel) -> CausalInverseKernel:
        """Compose two inverse kernels, with all endpoint terms retained."""
        if type(other) is not CausalInverseKernel:
            raise TypeError("expected a CausalInverseKernel")
        order = _natural(self.order + other.order, "combined inverse order", MAX_INVERSE_ORDER)
        numerator = _multiply(self.full_numerator, other.full_numerator)
        denominator = _multiply(self.remainder_denominator, other.remainder_denominator)
        delta, remainder = _divide(numerator, denominator)
        return CausalInverseKernel(order, delta, remainder, denominator)


def inverse_kernel(order: int = 1) -> CausalInverseKernel:
    """Exact order-m inverse of H(t)q(t); order zero is the convolution unit delta."""
    _natural(order, "inverse order", MAX_INVERSE_ORDER)
    numerator = _power(SOURCE_DENOMINATOR, order)
    denominator = _power(SOURCE_NUMERATOR, order)
    delta, remainder = _divide(numerator, denominator)
    return CausalInverseKernel(order, delta, remainder, denominator)
