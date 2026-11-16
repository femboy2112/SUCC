"""Exact finite linear observers of integer Gamma resolvent operators.

``integer_gamma_operator(K, m)`` computes (2 I - K)^(-m).  Its algebraic
domain is a finite rational square matrix with nonsingular 2 I - K and a
positive integer m.  Algebraic invertibility alone does NOT establish a
contraction, a Markov law, the convergence of a positive Gamma series, or
physical causality.  Those interpretations need separate hypotheses.

``linear_descent(A, P)`` certifies whether the complete linear report P
supports A: P A = Q P.  A failed certificate supplies an exact hidden
vector v with P v = 0 but P A v != 0.  This is global linear factorization,
not one observed trajectory or an assertion about every future target.

Only integers and Fraction values enter claim-bearing arithmetic.  The
all-shape Gamma-family theorem is a paper result, not a finite scan here.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


class GammaDescentError(ValueError):
    """The finite exact matrix/source contract was not supplied."""


@dataclass(frozen=True)
class LinearDescentCertificate:
    """A quotient factor or a dual obstruction, all in exact arithmetic."""

    descends: bool
    factor: Matrix | None
    kernel_witness: Vector | None
    image_witness: Vector | None


def _matrix(value, name: str) -> Matrix:
    try:
        rows = tuple(tuple(row) for row in value)
    except TypeError as error:
        raise GammaDescentError(f"{name} must be a rectangular exact matrix") from error
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise GammaDescentError(f"{name} must be a nonempty rectangular matrix")
    if any(type(entry) not in (int, Fraction) for row in rows for entry in row):
        raise GammaDescentError(f"{name} entries must be int or Fraction, never floats")
    return tuple(tuple(Fraction(entry) for entry in row) for row in rows)


def _identity(size: int) -> Matrix:
    return tuple(tuple(Fraction(i == j) for j in range(size)) for i in range(size))


def _multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(sum((left[i][k] * right[k][j] for k in range(len(right))),
                           Fraction(0))
                       for j in range(len(right[0])))
                 for i in range(len(left)))


def _solve_with_dual(matrix: Matrix, target: Vector) -> tuple[Vector | None, Vector | None]:
    """Solve A x=b, or return v with v^T A=0 and v^T b != 0.

    Row-operation receipts retain the dual witness even for dependent rows.
    Free solution coordinates are set to zero; uniqueness is not claimed.
    """
    row_count, column_count = len(matrix), len(matrix[0])
    work = [list(row) + [target[i]] for i, row in enumerate(matrix)]
    operations = [list(row) for row in _identity(row_count)]
    pivot_row = 0
    pivots = []
    for column in range(column_count):
        chosen = next((i for i in range(pivot_row, row_count) if work[i][column]), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        operations[pivot_row], operations[chosen] = operations[chosen], operations[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        operations[pivot_row] = [entry / scale for entry in operations[pivot_row]]
        for i in range(row_count):
            if i != pivot_row and work[i][column]:
                coefficient = work[i][column]
                work[i] = [value - coefficient * pivot
                           for value, pivot in zip(work[i], work[pivot_row])]
                operations[i] = [value - coefficient * pivot
                                 for value, pivot in zip(operations[i], operations[pivot_row])]
        pivots.append((pivot_row, column))
        pivot_row += 1
        if pivot_row == row_count:
            break
    for i, row in enumerate(work):
        if not any(row[:column_count]) and row[column_count]:
            return None, tuple(operations[i])
    solution = [Fraction(0)] * column_count
    for row, column in pivots:
        solution[column] = work[row][column_count]
    return tuple(solution), None


def _inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    columns = []
    for column in range(size):
        target = tuple(Fraction(row == column) for row in range(size))
        solution, _ = _solve_with_dual(matrix, target)
        if solution is None:
            raise GammaDescentError("2 I - K is singular; the resolvent is undefined")
        columns.append(solution)
    return tuple(tuple(columns[column][row] for column in range(size)) for row in range(size))


def integer_gamma_operator(source, order: int) -> Matrix:
    """Return the exact rational operator (2 I - source)^(-order).

    Positive integer order only; no floating or fractional matrix powers.
    No contraction or probability interpretation follows just from a result.
    """
    if type(order) is not int or order < 1:
        raise GammaDescentError("Gamma resolvent order must be a positive integer")
    source = _matrix(source, "source")
    size = len(source)
    if len(source[0]) != size:
        raise GammaDescentError("source must be square")
    denominator = tuple(tuple(Fraction(2 if i == j else 0) - source[i][j]
                              for j in range(size)) for i in range(size))
    power = _inverse(denominator)
    result = _identity(size)
    exponent = order
    while exponent:
        if exponent & 1:
            result = _multiply(result, power)
        exponent >>= 1
        if exponent:
            power = _multiply(power, power)
    return result


def linear_descent(operator, report) -> LinearDescentCertificate:
    """Certify P A=Q P, or exhibit v with P v=0 and P A v !=0.

    Report rows may be dependent or zero.  A chosen Q is then an extension
    to the ambient report coordinates, not a uniquely specified map there.
    Its action on the realized report image is unique.
    """
    operator, report = _matrix(operator, "operator"), _matrix(report, "report")
    size = len(operator)
    if len(operator[0]) != size or len(report[0]) != size:
        raise GammaDescentError("operator must be square and report must have matching columns")
    report_after = _multiply(report, operator)
    transpose = tuple(tuple(report[row][column] for row in range(len(report)))
                      for column in range(size))
    factors = []
    for target in report_after:
        solution, witness = _solve_with_dual(transpose, target)
        if solution is None:
            assert witness is not None
            image = tuple(sum((row[i] * witness[i] for i in range(size)), Fraction(0))
                          for row in report_after)
            return LinearDescentCertificate(False, None, witness, image)
        factors.append(solution)
    return LinearDescentCertificate(True, tuple(factors), None, None)
