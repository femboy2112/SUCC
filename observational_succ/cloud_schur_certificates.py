"""Independent, exact rational quadratic-form certificates.

Classical finite symmetric elimination, with no floating-point search, denominator
cutoff, external verifier callback, or source/formal authority claim.  The generator
and the small checker are separate.  The paper proof of completeness is in
``research/2026-10-20/CLOUD_FORMAL_SCHUR.md``; the Python implementation is not itself
kernel verified.
"""

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence, Union

Q = Fraction


def _rational(value):
    if type(value) not in (int, Fraction):
        raise TypeError("only exact int or Fraction entries are accepted")
    return Q(value)


def exact_symmetric(matrix):
    """Validate dimensions, symmetry and exact input, including the empty matrix."""
    rows = tuple(tuple(_rational(x) for x in row) for row in matrix)
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise ValueError("matrix must be square")
    if any(rows[i][j] != rows[j][i] for i in range(n) for j in range(i)):
        raise ValueError("matrix must be symmetric")
    return rows


def quadratic_value(matrix, vector):
    matrix = exact_symmetric(matrix)
    vector = tuple(_rational(x) for x in vector)
    if len(vector) != len(matrix):
        raise ValueError("vector dimension mismatch")
    return sum((vector[i] * matrix[i][j] * vector[j]
                for i in range(len(matrix)) for j in range(len(matrix))), Q(0))


@dataclass(frozen=True)
class NegativeWitness:
    vector: tuple


@dataclass(frozen=True)
class RationalGram:
    """M = sum(weight * row.T * row), with every weight strictly positive."""

    weights: tuple
    rows: tuple


Certificate = Union[NegativeWitness, RationalGram]


def verify_certificate(matrix, certificate):
    """Recompute the exact inequality or Gram identity; accept no supplied code.

    A true return certifies only this explicit finite rational matrix.  It does not
    certify a source-identification map, an infinite form, or a formal-kernel run.
    Malformed matrices or certificates return false.
    """
    try:
        matrix = exact_symmetric(matrix)
        n = len(matrix)
        if type(certificate) is NegativeWitness:
            return quadratic_value(matrix, certificate.vector) < 0
        if type(certificate) is not RationalGram:
            return False
        weights = tuple(_rational(x) for x in certificate.weights)
        rows = tuple(tuple(_rational(x) for x in row) for row in certificate.rows)
        if len(rows) != len(weights) or any(len(row) != n for row in rows):
            return False
        if any(weight <= 0 for weight in weights):
            return False
        return all(matrix[i][j] == sum((w * r[i] * r[j]
                   for w, r in zip(weights, rows)), Q(0))
                   for i in range(n) for j in range(n))
    except (TypeError, ValueError, AttributeError, ZeroDivisionError):
        return False


def certify(matrix):
    """Return either a rational negative vector or a positive weighted Gram.

    Each recursive call lowers dimension.  No assumption of nonsingularity is
    made.  Zero-diagonal nonzero couplings are handled exactly, before division.
    The returned object is rechecked against the original input.
    """
    matrix = exact_symmetric(matrix)
    result = _eliminate(matrix)
    if not verify_certificate(matrix, result):
        raise ArithmeticError("internal certificate verification failed")
    return result


def _eliminate(matrix):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] < 0:
            v = [Q(0)] * n
            v[i] = Q(1)
            return NegativeWitness(tuple(v))
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(n):
                b = matrix[i][j]
                if b:
                    v = [Q(0)] * n
                    v[i] = -(matrix[j][j] + 1) / (2 * b)
                    v[j] = Q(1)
                    return NegativeWitness(tuple(v))  # q(v) = -1
    pivot = next((i for i in range(n) if matrix[i][i] > 0), None)
    if pivot is None:
        return RationalGram((), ())  # Every entry is zero.
    others = tuple(i for i in range(n) if i != pivot)
    p = matrix[pivot][pivot]
    b = tuple(matrix[pivot][i] for i in others)
    schur = tuple(tuple(matrix[i][j] - b[k] * b[l] / p
                        for l, j in enumerate(others))
                  for k, i in enumerate(others))
    child = _eliminate(schur)
    if type(child) is NegativeWitness:
        v = [Q(0)] * n
        for i, value in zip(others, child.vector):
            v[i] = value
        v[pivot] = -sum((x * y for x, y in zip(b, child.vector)), Q(0)) / p
        return NegativeWitness(tuple(v))
    first = [Q(0)] * n
    first[pivot] = Q(1)
    for i, value in zip(others, b):
        first[i] = value / p
    lifted = [tuple(first)]
    for row in child.rows:
        new = [Q(0)] * n
        for i, value in zip(others, row):
            new[i] = value
        lifted.append(tuple(new))
    return RationalGram((p,) + child.weights, tuple(lifted))
