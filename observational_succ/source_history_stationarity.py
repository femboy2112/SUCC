"""Exact finite controls for stationary positive mixtures of observer histories.

For a contraction U and a fixed positive probability polynomial P, the paper
lemma is ker(I-P(U)) = ker(I-U**d), where d is the gcd of the positive supported
history lengths.  These instruments check finite cyclic carriers exactly.
They do not establish stationarity of the authentic BBP source or pi normality.

Signed filters are deliberately supported by a separate function so that the
load-bearing positivity hypothesis can be tested, rather than silently waived.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import reduce
from math import gcd
from typing import Sequence

Rational = int | Q
Measure = tuple[Q, ...]
Matrix = tuple[tuple[Q, ...], ...]


def _integer(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError("expected an integer in the stated domain")
    return value


def _rational(value: Rational) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("expected an exact int or Fraction")
    return Q(value)


def probability_measure(weights: Sequence[Rational]) -> Measure:
    """A probability on residues 0,...,q-1, interpreted as points r/q."""
    values = tuple(_rational(value) for value in weights)
    if not values or any(value < 0 for value in values) or sum(values) != 1:
        raise ValueError("measure must be nonempty, nonnegative and have mass one")
    return values


@dataclass(frozen=True)
class PositiveHistoryMixture:
    """Fixed finite probability weights indexed by nonnegative history length.

    At least one positive length must have positive weight.  Zero-length mass
    is allowed.  The identity-only mixture carries no invariance information
    and is rejected.  Floats and bools never enter an exact certificate.
    """

    weights: tuple[Rational, ...]

    def __post_init__(self) -> None:
        weights = probability_measure(self.weights)
        if not any(weights[1:]):
            raise ValueError("at least one positive history length is required")
        while not weights[-1]:
            weights = weights[:-1]
        object.__setattr__(self, "weights", weights)

    @property
    def support_gcd(self) -> int:
        return reduce(gcd, (index for index, weight in enumerate(self.weights)
                            if index and weight))


def multiplication_pushforward(
    measure: Sequence[Rational], multiplier: int,
) -> Measure:
    """Push a finite probability by x -> multiplier*x mod 1, without floats."""
    weights = probability_measure(measure)
    _integer(multiplier, 1)
    result = [Q()] * len(weights)
    for residue, weight in enumerate(weights):
        result[multiplier * residue % len(weights)] += weight
    return tuple(result)


def apply_history_filter(
    measure: Sequence[Rational], multiplier: int,
    coefficients: Sequence[Rational],
) -> tuple[Q, ...]:
    """Apply sum_j c_j (T_multiplier**j)*, allowing explicit signed c_j.

    This linear filter need not return a probability.  Even when its output
    is positive, signed coefficients do not qualify for the stationarity lemma.
    """
    current = probability_measure(measure)
    _integer(multiplier, 1)
    coefficients = tuple(_rational(value) for value in coefficients)
    if not coefficients:
        raise ValueError("a history filter must have at least one coefficient")
    result = [Q()] * len(current)
    for index, coefficient in enumerate(coefficients):
        if index:
            current = multiplication_pushforward(current, multiplier)
        for residue, weight in enumerate(current):
            result[residue] += coefficient * weight
    return tuple(result)


def total_variation_distance(
    first: Sequence[Rational], second: Sequence[Rational],
) -> Q:
    """Probability-distance convention: one half of the l1 difference."""
    left, right = probability_measure(first), probability_measure(second)
    if len(left) != len(right):
        raise ValueError("both measures must use the same cyclic carrier")
    return sum((abs(a - b) for a, b in zip(left, right)), Q()) / 2


@dataclass(frozen=True)
class StationarityCertificate:
    support_gcd: int
    original: Measure
    mixture_image: Measure
    gcd_image: Measure
    mixture_defect: Q
    gcd_defect: Q

    @property
    def mixture_stationary(self) -> bool:
        return self.mixture_defect == 0

    @property
    def gcd_stationary(self) -> bool:
        return self.gcd_defect == 0

    @property
    def equivalence_holds(self) -> bool:
        return self.mixture_stationary == self.gcd_stationary


def stationarity_certificate(
    measure: Sequence[Rational], multiplier: int,
    mixture: PositiveHistoryMixture,
) -> StationarityCertificate:
    """Compare P(T)*mu=mu with (T**gcd)*mu=mu on one exact finite measure."""
    if type(mixture) is not PositiveHistoryMixture:
        raise ValueError("a validated positive history mixture is required")
    original = probability_measure(measure)
    _integer(multiplier, 1)
    image = apply_history_filter(original, multiplier, mixture.weights)
    gcd_image = original
    for _ in range(mixture.support_gcd):
        gcd_image = multiplication_pushforward(gcd_image, multiplier)
    return StationarityCertificate(
        mixture.support_gcd, original, image, tuple(gcd_image),
        total_variation_distance(original, image),
        total_variation_distance(original, gcd_image),
    )


def _defect_matrix(
    modulus: int, multiplier: int, coefficients: Sequence[Q],
) -> Matrix:
    result = [[Q(row == column) for column in range(modulus)]
              for row in range(modulus)]
    for length, coefficient in enumerate(coefficients):
        factor = pow(multiplier, length, modulus)
        for column in range(modulus):
            result[factor * column % modulus][column] -= coefficient
    return tuple(tuple(row) for row in result)


def _rank(matrix: Matrix) -> int:
    rows = [list(row) for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((index for index in range(rank, len(rows))
                      if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        divisor = rows[rank][column]
        rows[rank] = [value / divisor for value in rows[rank]]
        for index, row in enumerate(rows):
            if index != rank and row[column]:
                factor = row[column]
                rows[index] = [left - factor * right
                               for left, right in zip(row, rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


@dataclass(frozen=True)
class StationarityKernelCertificate:
    modulus: int
    multiplier: int
    support_gcd: int
    mixture_rank: int
    gcd_rank: int
    stacked_rank: int

    @property
    def kernels_equal(self) -> bool:
        """Equal row spaces certify equal kernels on all rational vectors."""
        return self.mixture_rank == self.gcd_rank == self.stacked_rank


def finite_stationarity_kernel_certificate(
    modulus: int, multiplier: int, mixture: PositiveHistoryMixture,
) -> StationarityKernelCertificate:
    """Exact Gaussian elimination; a finite check, not an asymptotic theorem."""
    _integer(modulus, 1)
    _integer(multiplier, 1)
    if type(mixture) is not PositiveHistoryMixture:
        raise ValueError("a validated positive history mixture is required")
    first = _defect_matrix(modulus, multiplier, mixture.weights)
    second = _defect_matrix(
        modulus, multiplier, (Q(),) * mixture.support_gcd + (Q(1),),
    )
    return StationarityKernelCertificate(
        modulus, multiplier, mixture.support_gcd,
        _rank(first), _rank(second), _rank(first + second),
    )
