"""Source-retaining fractional Oily grades and exact projected-memory probes.

The inherited source has u=x-x**2/2, v=x**2/2 and
G_x(z)=(1-u)(1-v)/((1-uz)(1-vz)), 0<=x<=1. The fractional
family G_x(z)**alpha is a declared observer extension. Only alpha=1
recovers the original normalized two-loop Oily grade law.
At x=1 this normalized law is the inherited conditional limit; raw R(1)=0.

For the authentic auxiliary measure mu(dx)=16*R(x)dx/pi, the zero-grade
depth moment is m_n=E_mu[((1-u)(1-v))**n]. This module computes exact
rational coefficients pi*m_n (n>=1), finite Hankel determinants and
source-BBP rational enclosures. The all-size positive-definiteness proof
is an integral argument in the paper; a finite scan is not that proof.

Infinite linear realization rank does not exclude a finite program:
m_n=(pi*m_n)/2 * m_1, with a finite exact coefficient algorithm for each n.
The module does not change the BBP seed or certify selected Weyl decay.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

from .bbp_natural_carrier import alpha_enclosure
from .pascal_gamma_turn import fractional_coefficient
from .wavefront_oracle_two_stage import SourceGeometry

Q = Fraction
Rational = int | Fraction
MAX_GRADE = 128
MAX_DEPTH = 32
MAX_MOMENT = 16
MAX_HANKEL_SIZE = 5


def _exact(value: Rational) -> Q:
    if type(value) not in (int, Q):
        raise TypeError("Only exact integers and Fractions are admitted")
    return Q(value)


def _integer(value: int, low: int, high: int, label: str) -> int:
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f"{label} must be an integer in {low}..{high}")
    return value


def _geometry(x: Rational) -> SourceGeometry:
    return SourceGeometry(_exact(x))


def _shape(alpha: Rational) -> Q:
    alpha = _exact(alpha)
    if not 0 <= alpha <= MAX_DEPTH:
        raise ValueError(f"Shape must be in [0,{MAX_DEPTH}]")
    return alpha


def fractional_grade_prefix(x: Rational, alpha: Rational, last_grade: int) -> tuple[Q, ...]:
    """Exact prefactors of G_x(z)**alpha, excluding a(x)**alpha.

    For noninteger rational alpha the normalization can be irrational;
    it is deliberately not rounded or silently treated as rational.
    The coefficient returned at n is sum_j c_alpha(j)c_alpha(n-j)u**j*v**(n-j).
    At alpha=0 the full family and these prefactors are the identity delta_0.
    """
    geometry = _geometry(x)
    alpha = _shape(alpha)
    last_grade = _integer(last_grade, 0, MAX_GRADE, "Last grade")
    if alpha == 0:
        return (Q(1),) + (Q(0),) * last_grade
    coefficients = tuple(fractional_coefficient(alpha, j) for j in range(last_grade + 1))
    u, v = geometry.u, geometry.v
    return tuple(
        sum((coefficients[j] * coefficients[n - j] * u**j * v ** (n - j)
             for j in range(n + 1)), Q(0))
        for n in range(last_grade + 1)
    )


def fractional_grade_prefactor(x: Rational, alpha: Rational, grade: int) -> Q:
    """One exact unnormalized fractional grade coefficient."""
    return fractional_grade_prefix(x, alpha, grade)[-1]


def integer_grade_prefix(x: Rational, depth: int, last_grade: int) -> tuple[Q, ...]:
    """Normalized exact grade probabilities at an integer observer depth."""
    depth = _integer(depth, 0, MAX_DEPTH, "Depth")
    geometry = _geometry(x)
    prefactors = fractional_grade_prefix(geometry.x, depth, last_grade)
    normalizer = geometry.normalization**depth
    return tuple(normalizer * value for value in prefactors)


def integer_grade_probability(x: Rational, depth: int, grade: int) -> Q:
    return integer_grade_prefix(x, depth, grade)[-1]


def integer_grade_pgf(x: Rational, depth: int, z: Rational) -> Q:
    """Exact full PGF on the declared real generating-function slice -1<=z<=1."""
    geometry = _geometry(x)
    depth = _integer(depth, 0, MAX_DEPTH, "Depth")
    z = _exact(z)
    if not -1 <= z <= 1:
        raise ValueError("Require -1<=z<=1")
    return (geometry.normalization / ((1 - geometry.u * z) * (1 - geometry.v * z)))**depth


def _polynomial_product(left: tuple[Q, ...], right: tuple[Q, ...]) -> tuple[Q, ...]:
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return tuple(result)


@lru_cache(maxsize=MAX_MOMENT)
def _moment_pi_coefficient(n: int) -> Q:
    # a(x)=(1-u)(1-v)=1-x+x**3/2-x**4/4.
    a = (Q(1), Q(-1), Q(0), Q(1, 2), Q(-1, 4))
    power = (Q(1),)
    for _ in range(n - 1):
        power = _polynomial_product(power, a)
    # 4 integral_0^1 (1-x)*a(x)**(n-1) dx.
    return 4 * sum((coefficient / ((j + 1) * (j + 2))
                    for j, coefficient in enumerate(power)), Q(0))


def source_moment_pi_coefficient(n: int) -> Q:
    """Return c_n=pi*m_n exactly, n>=1; m_0=1 is a separate boundary.

    The identity uses the inherited authentic integral int R=pi/16.
    It does not introduce a numerical approximation to pi.
    """
    n = _integer(n, 1, MAX_MOMENT, "Moment index")
    return _moment_pi_coefficient(n)


def source_depth_ratio(n: int) -> Q:
    """Exact finite-program multiplier m_n/m_1=c_n/2 for n>=1.

    The source family must be supplied/authenticated. One observed scalar
    does not infer this entire family from an unrestricted candidate class.
    """
    return source_moment_pi_coefficient(n) / 2


def _determinant(matrix: tuple[tuple[Q, ...], ...]) -> Q:
    if not matrix:
        return Q(1)
    work = [list(row) for row in matrix]
    result = Q(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return Q(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column]
        result *= value
        for row in range(column + 1, len(work)):
            ratio = work[row][column] / value
            for j in range(column + 1, len(work)):
                work[row][j] -= ratio * work[column][j]
            work[row][column] = Q(0)
    return result


@dataclass(frozen=True)
class AffinePiDeterminant:
    """Represent (pi_coefficient*pi + constant)/pi**denominator_power."""

    pi_coefficient: Q
    constant: Q
    denominator_power: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "pi_coefficient", _exact(self.pi_coefficient))
        object.__setattr__(self, "constant", _exact(self.constant))
        _integer(self.denominator_power, 1, MAX_HANKEL_SIZE, "Denominator power")

    def enclose(self, pi_lower: Rational, pi_upper: Rational) -> tuple[Q, Q]:
        """Rational interval extension; actual pi must lie in the input interval."""
        lo, hi = _exact(pi_lower), _exact(pi_upper)
        if not 0 < lo <= hi:
            raise ValueError("A positive ordered pi interval is required")
        numerators = (self.pi_coefficient * lo + self.constant,
                      self.pi_coefficient * hi + self.constant)
        denominators = (lo**self.denominator_power, hi**self.denominator_power)
        ratios = tuple(numerator / denominator
                       for numerator in numerators for denominator in denominators)
        return min(ratios), max(ratios)


def source_hankel_determinant(size: int) -> AffinePiDeterminant:
    """Exact determinant of H[i,j]=m_(i+j), 0<=i,j<size.

    Multiplying H by pi leaves only the (0,0) entry symbolic (equal to pi).
    Its determinant is affine in pi. No floating-point determinant is used.
    """
    size = _integer(size, 1, MAX_HANKEL_SIZE, "Hankel size")
    zero_matrix = tuple(
        tuple(Q(0) if i + j == 0 else source_moment_pi_coefficient(i + j)
              for j in range(size))
        for i in range(size)
    )
    minor = tuple(tuple(zero_matrix[i][j] for j in range(1, size))
                  for i in range(1, size))
    return AffinePiDeterminant(_determinant(minor), _determinant(zero_matrix), size)


@dataclass(frozen=True)
class HankelCertificate:
    size: int
    pi_lower: Q
    pi_upper: Q
    determinant: AffinePiDeterminant
    lower: Q
    upper: Q

    @property
    def strict_positive(self) -> bool:
        return self.lower > 0


def source_hankel_certificate(size: int, pi_terms: int = 8) -> HankelCertificate:
    """Finite exact sign enclosure using the original BBP alpha=pi/16 series."""
    size = _integer(size, 1, MAX_HANKEL_SIZE, "Hankel size")
    pi_terms = _integer(pi_terms, 1, 32, "BBP enclosure depth")
    alpha_lo, alpha_hi = alpha_enclosure(pi_terms)
    pi_lo, pi_hi = 16 * alpha_lo, 16 * alpha_hi
    determinant = source_hankel_determinant(size)
    lo, hi = determinant.enclose(pi_lo, pi_hi)
    return HankelCertificate(size, pi_lo, pi_hi, determinant, lo, hi)


def _finite_sources(sources) -> tuple[tuple[Q, Q], ...]:
    if not isinstance(sources, (tuple, list)) or not 1 <= len(sources) <= 32:
        raise ValueError("Supply 1..32 finite (source coordinate, probability) pairs")
    result = []
    for pair in sources:
        if not isinstance(pair, (tuple, list)) or len(pair) != 2:
            raise ValueError("Each source entry must be a coordinate/probability pair")
        x, weight = _geometry(pair[0]).x, _exact(pair[1])
        if weight < 0:
            raise ValueError("Source probabilities must be nonnegative")
        result.append((x, weight))
    if sum((weight for _, weight in result), Q(0)) != 1:
        raise ValueError("Finite source probabilities must sum exactly to one")
    return tuple(result)


@dataclass(frozen=True)
class MixtureGradeComparison:
    """A finite synthetic control; this discrete prior is not the authentic mu."""

    shared: Q
    redrawn: Q

    @property
    def defect(self) -> Q:
        return self.shared - self.redrawn


def shared_redrawn_grade(sources, left_depth: int, right_depth: int, grade: int) -> MixtureGradeComparison:
    """Compare a retained source x against independently redrawing x per layer.

    The shared source uses sum_x p_x q_(left+right,x)(grade). The redrawn
    source convolves the two independently averaged grade laws. The zero-
    grade defect is nonnegative; arbitrary coefficient defects need not be.
    """
    sources = _finite_sources(sources)
    left_depth = _integer(left_depth, 0, MAX_DEPTH, "Left depth")
    right_depth = _integer(right_depth, 0, MAX_DEPTH, "Right depth")
    _integer(left_depth + right_depth, 0, MAX_DEPTH, "Total depth")
    grade = _integer(grade, 0, MAX_GRADE, "Grade")
    shared = sum((weight * integer_grade_probability(x, left_depth + right_depth, grade)
                  for x, weight in sources), Q(0))
    left = [Q(0)] * (grade + 1)
    right = [Q(0)] * (grade + 1)
    for x, weight in sources:
        for j, value in enumerate(integer_grade_prefix(x, left_depth, grade)):
            left[j] += weight * value
        for j, value in enumerate(integer_grade_prefix(x, right_depth, grade)):
            right[j] += weight * value
    redrawn = sum((left[j] * right[grade - j] for j in range(grade + 1)), Q(0))
    return MixtureGradeComparison(shared, redrawn)
