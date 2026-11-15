"""Exact predictive closure for the supplied source T(x,y)=(xy,y), h=x.

The first two reports are (a,b)=(x,xy). They determine every future report,
although the polynomial observable algebras Q[x,xy,...,xy**m] never stabilize.
Division and the source-valid singular branch provide the missing evaluator.

Only integers and Fractions are accepted. These helpers check consistency
with this declared mathematical source; they do not authenticate a physical
source, infer its law from observations, or establish an infinite theorem by
finite testing. Operation counts use unit-cost exact field arithmetic, not
bit complexity. Expanded numerators and denominators can grow with horizon.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

Rational = int | Fraction


def _exact(value: Rational) -> Fraction:
    if type(value) not in (int, Fraction):
        raise TypeError("Only exact integers and Fractions are admitted")
    return Fraction(value)


def _natural(value: int, label: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{label} must be a nonnegative integer")
    return value


def _nonnegative(value: Rational, label: str) -> Fraction:
    result = _exact(value)
    if result < 0:
        raise ValueError(f"{label} must be nonnegative")
    return result


def source_reports(x: Rational, y: Rational) -> tuple[Fraction, Fraction]:
    """Return the initial and next report of the declared source."""
    x, y = _exact(x), _exact(y)
    return x, x * y


def in_source_image(a: Rational, b: Rational) -> bool:
    """Test the exact image {(a,b): a != 0} union {(0,0)}."""
    a, b = _exact(a), _exact(b)
    return a != 0 or b == 0


def validate_reports(a: Rational, b: Rational) -> tuple[Fraction, Fraction]:
    """Normalize a consistent pair, rejecting the off-image pair (0,b!=0)."""
    a, b = _exact(a), _exact(b)
    if a == 0 and b != 0:
        raise ValueError("Reports are outside the declared source image")
    return a, b


@dataclass(frozen=True)
class JumpReceipt:
    """A mathematical value and this algorithm's separate arithmetic counts.

    Multiplications include squarings and the final multiplication by a.
    Counts exclude comparisons, integer bit handling, and output writing.
    """

    value: Fraction
    multiplications: int
    divisions: int


def jump_report_counted(a: Rational, b: Rational, n: int) -> JumpReceipt:
    """Evaluate the time-n report by guarded binary exponentiation.

    On the regular branch n>=1, the multiplication count is
    floor(log2(n)) + popcount(n) + 1, with one division. At the singular
    origin, or at n=0, no multiplication or division is performed.
    All supplied reports are validated even when n=0.
    """
    n = _natural(n, "Horizon")
    a, b = validate_reports(a, b)
    if a == 0:
        return JumpReceipt(Fraction(0), 0, 0)
    if n == 0:
        return JumpReceipt(a, 0, 0)

    base = b / a
    result = Fraction(1)
    remaining = n
    multiplications = 0
    while remaining:
        if remaining & 1:
            result *= base
            multiplications += 1
        remaining >>= 1
        if remaining:
            base *= base
            multiplications += 1
    return JumpReceipt(a * result, multiplications + 1, 1)


def jump_report(a: Rational, b: Rational, n: int) -> Fraction:
    """Return only the exact time-n value; see jump_report_counted for cost."""
    return jump_report_counted(a, b, n).value


def jump_descriptor(a: Rational, b: Rational) -> tuple[Fraction, Fraction]:
    """One descended transition: E(T(x,y)) = jump_descriptor(E(x,y))."""
    a, b = validate_reports(a, b)
    if a == 0:
        return Fraction(0), Fraction(0)
    return b, b * b / a


def satisfies_report_relation(a: Rational, b: Rational, c: Rational) -> bool:
    """Check ac=b**2 only; this polynomial shadow is not the source image."""
    a, b, c = _exact(a), _exact(b), _exact(c)
    return a * c == b * b


def in_three_report_image(a: Rational, b: Rational, c: Rational) -> bool:
    """Check realization as (x,xy,xy**2), including its singular condition."""
    a, b, c = _exact(a), _exact(b), _exact(c)
    if a == 0:
        return b == 0 and c == 0
    return a * c == b * b


def monomial_in_polynomial_stage(x_degree: int, y_degree: int, depth: int) -> bool:
    """Whether x**r*y**s lies in Q[x,xy,...,xy**depth].

    Monomial products have r generators and y-degree between 0 and r*depth;
    every integer in that interval is realizable. Distinct monomials form a
    basis, so sums cannot add an absent monomial. In particular xy**(m+1)
    is absent at every finite stage m. The claim concerns polynomial
    functions over an infinite field, not finite-field function identities.
    """
    r = _natural(x_degree, "x degree")
    s = _natural(y_degree, "y degree")
    m = _natural(depth, "Depth")
    return s <= r * m


def in_bounded_image(a: Rational, b: Rational, bound: Rational) -> bool:
    """Test realization with |y|<=bound: exactly |b|<=bound*|a|.

    A nonnegative bound is a supplied source hypothesis, not an estimate
    established by this check. The origin is realized, for example, by y=0.
    """
    a, b = _exact(a), _exact(b)
    bound = _nonnegative(bound, "Source bound")
    return abs(b) <= bound * abs(a)


def future_error_bound(
    n: int, bound: Rational, delta_a: Rational, delta_b: Rational
) -> Fraction:
    """Conditional bound between two valid reports with |y|<=bound.

    delta_a and delta_b must bound the respective coordinate differences.
    For n>=2 the returned bound is (n-1)M**n*delta_a +
    n*M**(n-1)*delta_b. It applies across both signs of a and at the origin.
    This scalar helper cannot itself authenticate either source or the
    coordinate-error claims; bounded_pair_error_bound checks a given pair.
    """
    n = _natural(n, "Horizon")
    bound = _nonnegative(bound, "Source bound")
    delta_a = _nonnegative(delta_a, "First coordinate error")
    delta_b = _nonnegative(delta_b, "Second coordinate error")
    if n == 0:
        return delta_a
    if n == 1:
        return delta_b
    return (n - 1) * bound**n * delta_a + n * bound ** (n - 1) * delta_b


def bounded_pair_error_bound(
    a: Rational, b: Rational, other_a: Rational, other_b: Rational,
    n: int, bound: Rational,
) -> Fraction:
    """Validate two source-bounded report pairs and bound their target gap."""
    n = _natural(n, "Horizon")
    a, b = validate_reports(a, b)
    other_a, other_b = validate_reports(other_a, other_b)
    bound = _nonnegative(bound, "Source bound")
    if not (in_bounded_image(a, b, bound)
            and in_bounded_image(other_a, other_b, bound)):
        raise ValueError("Report pair violates the supplied source bound")
    return future_error_bound(n, bound, abs(a - other_a), abs(b - other_b))
