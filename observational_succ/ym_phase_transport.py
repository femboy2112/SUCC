"""Exact finite probes for common expansions and their stability margin.

The paper theorem permits complex normed spaces. This implementation is its
rational-real specialization. It neither constructs a Yang--Mills field nor
proves a BBP statistical estimate. See the dated Yang--Mills/SUCC dossier.
"""

from fractions import Fraction
from typing import Sequence


Rational = int | Fraction


def _q(value: Rational) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("exact int or Fraction required")
    return Fraction(value)


def _vector(values: Sequence[Rational]) -> tuple[Fraction, ...]:
    return tuple(_q(value) for value in values)


def _square(matrix: Sequence[Sequence[Rational]]) -> tuple[tuple[Fraction, ...], ...]:
    result = tuple(_vector(row) for row in matrix)
    if not result or any(len(row) != len(result) for row in result):
        raise ValueError("a nonempty square matrix is required")
    return result


def _weights(values: Sequence[Rational], size: int) -> tuple[Fraction, ...]:
    result = _vector(values)
    if len(result) != size or any(weight <= 0 for weight in result):
        raise ValueError("one strictly positive weight per coordinate is required")
    return result


def dot(left: Sequence[Rational], right: Sequence[Rational]) -> Fraction:
    lhs, rhs = _vector(left), _vector(right)
    if len(lhs) != len(rhs):
        raise ValueError("vector dimensions differ")
    return sum((a * b for a, b in zip(lhs, rhs)), Fraction())


def common_phase_comparison(
    coefficients: Sequence[Rational],
    left_value: Rational,
    left_channels: Sequence[Rational],
    right_value: Rational,
    right_channels: Sequence[Rational],
    remainder_bound: Rational,
) -> dict[str, Fraction]:
    """Validate supplied same-coefficient residuals and return the exact defect.

    Coefficients are supplied once, before either phase. A false supplied
    residual budget raises ValueError; the function never repairs a witness.
    This is a finite algebra check, not evidence of source identity or a limit.
    """
    coeff = _vector(coefficients)
    lhs, rhs = _vector(left_channels), _vector(right_channels)
    if len(coeff) != len(lhs) or len(coeff) != len(rhs):
        raise ValueError("coefficient and channel dimensions differ")
    epsilon = _q(remainder_bound)
    if epsilon < 0:
        raise ValueError("remainder bound must be nonnegative")
    lvalue, rvalue = _q(left_value), _q(right_value)
    lresidual = lvalue - dot(coeff, lhs)
    rresidual = rvalue - dot(coeff, rhs)
    if abs(lresidual) > epsilon or abs(rresidual) > epsilon:
        raise ValueError("a supplied phase violates the common expansion budget")
    defect = (lvalue - rvalue) - dot(coeff, tuple(a - b for a, b in zip(lhs, rhs)))
    return {
        "left_residual": lresidual,
        "right_residual": rresidual,
        "difference_defect": defect,
        "difference_budget": 2 * epsilon,
    }


def weighted_sup(values: Sequence[Rational], weights: Sequence[Rational]) -> Fraction:
    vector = _vector(values)
    if not vector:
        raise ValueError("a nonempty vector is required")
    scales = _weights(weights, len(vector))
    return max(abs(value) / weight for value, weight in zip(vector, scales))


def contraction_factor(
    matrix: Sequence[Sequence[Rational]], weights: Sequence[Rational]
) -> Fraction:
    """The exact weighted row bound for the ENTRYWISE ABSOLUTE matrix.

    Signed row sums are not a valid replacement for this operator-norm bound.
    Returning q >= 1 deliberately gives no contraction certificate.
    """
    operator = _square(matrix)
    scales = _weights(weights, len(operator))
    return max(
        sum((abs(value) * weight for value, weight in zip(row, scales)), Fraction())
        / scales[index]
        for index, row in enumerate(operator)
    )


def affine_residual(
    matrix: Sequence[Sequence[Rational]],
    bias: Sequence[Rational],
    values: Sequence[Rational],
) -> tuple[Fraction, ...]:
    operator = _square(matrix)
    constant, vector = _vector(bias), _vector(values)
    if len(vector) != len(operator) or len(constant) != len(operator):
        raise ValueError("matrix, bias and vector dimensions differ")
    return tuple(
        vector[index] - dot(row, vector) - constant[index]
        for index, row in enumerate(operator)
    )


def phase_diameter_bound(
    matrix: Sequence[Sequence[Rational]],
    weights: Sequence[Rational],
    weighted_remainder_bound: Rational,
) -> Fraction:
    """Return 2*epsilon/(1-q); the caller must establish the shared expansion."""
    q = contraction_factor(matrix, weights)
    epsilon = _q(weighted_remainder_bound)
    if epsilon < 0:
        raise ValueError("remainder bound must be nonnegative")
    if q >= 1:
        raise ValueError("no positive contraction margin")
    return 2 * epsilon / (1 - q)


def check_affine_phases(
    matrix: Sequence[Sequence[Rational]],
    weights: Sequence[Rational],
    bias: Sequence[Rational],
    phases: Sequence[Sequence[Rational]],
    weighted_remainder_bound: Rational,
) -> dict[str, Fraction | int]:
    """Check finitely supplied phases; no unlisted phase is certified."""
    operator = _square(matrix)
    scales = _weights(weights, len(operator))
    constant = _vector(bias)
    if len(constant) != len(operator):
        raise ValueError("matrix and bias dimensions differ")
    states = tuple(_vector(state) for state in phases)
    if not states or any(len(state) != len(operator) for state in states):
        raise ValueError("nonempty phases of the declared dimension are required")
    epsilon = _q(weighted_remainder_bound)
    bound = phase_diameter_bound(operator, scales, epsilon)
    maximum_residual = max(
        weighted_sup(affine_residual(operator, constant, state), scales)
        for state in states
    )
    if maximum_residual > epsilon:
        raise ValueError("a phase violates the common affine residual budget")
    diameter = max(
        weighted_sup(tuple(a - b for a, b in zip(left, right)), scales)
        for left in states for right in states
    )
    if diameter > bound:
        raise AssertionError("finite arithmetic contradicted the proved inequality")
    return {
        "checked_phases": len(states),
        "contraction_factor": contraction_factor(operator, scales),
        "maximum_residual": maximum_residual,
        "observed_diameter": diameter,
        "diameter_bound": bound,
    }


def target_reader(
    matrix: Sequence[Sequence[Rational]], target: Sequence[Sequence[Rational]]
) -> tuple[tuple[Fraction, ...], ...]:
    """Construct B with target = B(I-A), or reject a target-visible kernel.

    Exact row reduction sets free coordinates to zero. The criterion is
    ker(I-A) <= ker(target); q < 1 is NOT necessary. A returned reader may
    have a large norm, which must still be paid in a limit argument.
    """
    operator = _square(matrix)
    n = len(operator)
    readout = tuple(_vector(row) for row in target)
    if not readout or any(len(row) != n for row in readout):
        raise ValueError("a nonempty target with the declared input dimension is required")
    difference = tuple(
        tuple(Fraction(int(i == j)) - operator[i][j] for j in range(n))
        for i in range(n)
    )
    readers = []
    for wanted in readout:
        # Solve (I-A)^T b = wanted^T independently for each target row.
        augmented = [[difference[j][i] for j in range(n)] + [wanted[i]]
                     for i in range(n)]
        pivots = []
        active = 0
        for column in range(n):
            pivot = next((i for i in range(active, n) if augmented[i][column]), None)
            if pivot is None:
                continue
            augmented[active], augmented[pivot] = augmented[pivot], augmented[active]
            scale = augmented[active][column]
            augmented[active] = [value / scale for value in augmented[active]]
            for row in range(n):
                if row != active:
                    multiplier = augmented[row][column]
                    augmented[row] = [x - multiplier * y for x, y in
                                      zip(augmented[row], augmented[active])]
            pivots.append(column)
            active += 1
            if active == n:
                break
        if any(not any(row[:n]) and row[n] for row in augmented):
            raise ValueError("the target sees a direction in ker(I-A)")
        reader = [Fraction() for _ in range(n)]
        for row, column in enumerate(pivots):
            reader[column] = augmented[row][n]
        readers.append(tuple(reader))
    result = tuple(readers)
    # Recompute the certificate independently of row-reduction state.
    for row, wanted in zip(result, readout):
        actual = tuple(sum((row[i] * difference[i][j] for i in range(n)), Fraction())
                       for j in range(n))
        if actual != wanted:
            raise AssertionError("exact target-reader certificate failed")
    return result


def target_stability_bound(
    matrix: Sequence[Sequence[Rational]],
    target: Sequence[Sequence[Rational]],
    remainder_bound: Rational,
) -> dict[str, object]:
    """A finite infinity-norm bound; source/limit hypotheses remain external."""
    epsilon = _q(remainder_bound)
    if epsilon < 0:
        raise ValueError("remainder bound must be nonnegative")
    reader = target_reader(matrix, target)
    norm = max(sum((abs(value) for value in row), Fraction()) for row in reader)
    return {"reader": reader, "reader_norm": norm, "target_difference_bound": 2 * norm * epsilon}
