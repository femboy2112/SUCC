"""Exact four-dimensional rational realization of the authentic BBP tail kernel.

R(x)=P(x)/(16-x^8)=(1-x)/[(2-x^2)(x^2-2x+2)],
P(x)=4-2x^3-x^4-x^5.  Two rational quadratic blocks generate its coefficients.
The eight-step clock is their least common scalar return, not eight independent
states.  Minimality means finite-dimensional autonomous linear realization with
scalar output; it is not a lower bound for arbitrary nonlinear SUCC encodings.
The four-dimensional claim concerns c_m=[x^m]R(x), not T_n.  The tail sequence
T_n has infinite Hankel rank (PI_SOURCE_GENESIS_GREEN.md, G2).  That dossier
already contains the reduced quartic, primitive, and endpoint Pell hierarchy;
the new interface here is the explicit two-block coefficient compiler.

All endpoints are exact Fractions.  This realizes the positive Green-tail
kernel and authentic forcing, not selected arithmetic Weyl cancellation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import permutations

from .bbp_natural_carrier import exact_forcing


QUADRATIC_BLOCK = ((Q(0), Q(1, 2)), (Q(1), Q(0)))
COMPLEX_BLOCK = ((Q(1, 2), Q(-1, 2)), (Q(1, 2), Q(1, 2)))
TRANSITION = (
    (Q(0), Q(1, 2), Q(0), Q(0)),
    (Q(1), Q(0), Q(0), Q(0)),
    (Q(0), Q(0), Q(1, 2), Q(-1, 2)),
    (Q(0), Q(0), Q(1, 2), Q(1, 2)),
)
INPUT_VECTOR = (Q(1), Q(0), Q(1), Q(0))
OUTPUT_ROW = (Q(0), Q(-1, 8), Q(1, 4), Q(0))
METRIC_DIAGONAL = (Q(2), Q(1), Q(1), Q(1))
PERIOD_COEFFICIENTS = (Q(1, 4), Q(0), Q(0), Q(-1, 8),
                       Q(-1, 16), Q(-1, 16), Q(0), Q(0))
REDUCED_DENOMINATOR = (Q(4), Q(-4), Q(0), Q(2), Q(-1))


def _integer(value, name, lower=0, upper=100000):
    if type(value) is not int or not lower <= value <= upper:
        raise ValueError(f"{name}: integer in [{lower}, {upper}] required")
    return value


def _source_point(value):
    if type(value) not in (int, Q) or not 0 <= value <= 1:
        raise ValueError("source point must be exact rational in [0,1]")
    return Q(value)


def _identity(size):
    return tuple(tuple(Q(i == j) for j in range(size)) for i in range(size))


def _multiply(left, right):
    return tuple(tuple(sum((a*b for a, b in zip(row, column)), Q())
                       for column in zip(*right)) for row in left)


def _power(matrix, exponent):
    answer = _identity(len(matrix))
    while exponent:
        if exponent & 1:
            answer = _multiply(answer, matrix)
        matrix = _multiply(matrix, matrix)
        exponent //= 2
    return answer


def atomic_state(index: int) -> tuple[Q, ...]:
    """M^m v, with the two quadratic channels and their relative sign retained."""
    m = _integer(index, "coefficient index")
    matrix = _power(TRANSITION, m)
    return tuple(sum((a*b for a, b in zip(row, INPUT_VECTOR)), Q()) for row in matrix)


def atomic_coefficient(index: int) -> Q:
    """c_m=w M^m v, the exact Taylor coefficient of R at zero."""
    return sum((a*b for a, b in zip(OUTPUT_ROW, atomic_state(index))), Q())


def recurrence_coefficients(count: int) -> tuple[Q, ...]:
    """Independent order-four coefficient recurrence, with four initial values."""
    size = _integer(count, "coefficient count", 0, 10000)
    values = [Q(1, 4), Q(0), Q(0), Q(-1, 8)][:size]
    for m in range(4, size):
        values.append(values[m-1]-values[m-3]/2+values[m-4]/4)
    return tuple(values)


def atomic_kernel_value(point: int | Q) -> Q:
    """w(I-xM)^(-1)v, evaluated by the two exact quadratic resolvents."""
    x = _source_point(point)
    quadratic = -x/(4*(2-x*x))
    complex_part = (2-x)/(4*(x*x-2*x+2))
    return quadratic+complex_part


def kernel_identity_certificate(point: int | Q) -> dict:
    """Finite rational check of original, reduced, and two-block representations."""
    x = _source_point(point)
    original = (4-2*x**3-x**4-x**5)/(16-x**8)
    reduced = (1-x)/((2-x*x)*(x*x-2*x+2))
    realized = atomic_kernel_value(x)
    if not original == reduced == realized:
        raise ArithmeticError("BBP kernel factor cancellation failed")
    return {"point": x, "original": original, "reduced": reduced,
            "realization": realized, "source_preserved": True}


def compiled_forcing(index: int) -> Q:
    """Recover all four authentic poles from one eight-output block of the atoms."""
    n = _integer(index, "forcing index", 1)
    return 16*sum((atomic_coefficient(m)/Q(8*(n-1)+m+1)
                   for m in range(8)), Q())


def _determinant(matrix):
    size = len(matrix)
    result = Q()
    for order in permutations(range(size)):
        term = Q((-1)**sum(order[i] > order[j]
                           for i in range(size) for j in range(i+1, size)))
        for i, j in enumerate(order):
            term *= matrix[i][j]
        result += term
    return result


def minimal_realization_certificate() -> dict:
    """A nonzero coefficient Hankel minor proves dimension >=4 for c_m outputs.

    The provided four-state realization attains the bound.  Equivalently the
    reduced generating denominator has degree four and is coprime to 1-x,
    since its value at x=1 is one.  Neither claim covers nonlinear encodings
    or asserts a finite-dimensional linear realization of the tail T_n.
    """
    hankel = tuple(tuple(atomic_coefficient(i+j) for j in range(4))
                   for i in range(4))
    determinant = _determinant(hankel)
    if determinant != Q(1, 16384):
        raise ArithmeticError("four-dimensional Hankel witness failed")
    return {"hankel": hankel, "determinant": determinant,
            "minimal_scalar_linear_dimension": 4,
            "reduced_denominator": REDUCED_DENOMINATOR,
            "denominator_at_numerator_root": sum(REDUCED_DENOMINATOR),
            "nonlinear_dimension_claim": False}


def atomic_clock_certificate() -> dict:
    """Exact atom relations, weighted contraction, and least scalar return eight."""
    a2 = _power(QUADRATIC_BLOCK, 2)
    b4 = _power(COMPLEX_BLOCK, 4)
    fourth = _power(TRANSITION, 4)
    eighth = _power(TRANSITION, 8)
    scalar_returns = []
    for m in range(1, 9):
        p = _power(TRANSITION, m)
        if p == tuple(tuple(p[0][0] if i == j else Q()
                            for j in range(4)) for i in range(4)):
            scalar_returns.append((m, p[0][0]))
    metric = tuple(tuple(METRIC_DIAGONAL[i] if i == j else Q()
                         for j in range(4)) for i in range(4))
    transpose = tuple(zip(*TRANSITION))
    contracted_metric = _multiply(_multiply(transpose, metric), TRANSITION)
    expected_metric = tuple(tuple(entry/2 for entry in row) for row in metric)
    if scalar_returns != [(8, Q(1, 16))] or contracted_metric != expected_metric:
        raise ArithmeticError("atomic clock or weighted norm certificate failed")
    return {"quadratic_square": a2, "complex_fourth": b4,
            "fourth_power": fourth, "eighth_power": eighth,
            "scalar_returns_through_eight": tuple(scalar_returns),
            "metric": metric, "contracted_metric": contracted_metric}


@dataclass(frozen=True)
class AtomicTailCertificate:
    index: int
    blocks: int
    coefficient_prefix: Q
    authentic_green_prefix: Q
    remainder_lower: Q
    remainder_upper: Q
    lower: Q
    upper: Q


def atomic_tail_certificate(index: int, blocks: int = 12) -> AtomicTailCertificate:
    """Finite coefficient integral plus a rigorous source-preserving tail defect.

    T_n=int_0^1 x^(8n)R(x)dx. After D blocks, the exact remainder is
    16^-D T_(n+D).  On [0,1], 0<=R(x)<=1-x, so the remainder is bounded above
    by 16^-D/[(8(n+D)+1)(8(n+D)+2)]. This also holds at n=0, where T_0=pi/16.
    """
    n = _integer(index, "tail index", 0, 99000)
    depth = _integer(blocks, "coefficient blocks", 1, 300)
    prefix = sum((PERIOD_COEFFICIENTS[m % 8]/Q(16**(m//8)*(8*n+m+1))
                  for m in range(8*depth)), Q())
    authentic = sum((exact_forcing(n+j)/Q(16**j) for j in range(1, depth+1)), Q())
    if prefix != authentic:
        raise ArithmeticError("atomic output does not reconstruct authentic Green prefix")
    remainder = Q(1, 16**depth*(8*(n+depth)+1)*(8*(n+depth)+2))
    return AtomicTailCertificate(n, depth, prefix, authentic, Q(), remainder,
                                 prefix, prefix+remainder)
