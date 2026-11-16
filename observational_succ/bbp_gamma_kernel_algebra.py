"""Exact convolution powers of the original signed four-pole BBP source.

For a > 0, write

    R(a) = 4/a - 2/(a+3) - 1/(a+4) - 1/(a+5) = Laplace[Q](a),
    Q(t) = 4 - 2 exp(-3t) - exp(-4t) - exp(-5t).

``source_kernel_power(j)`` represents Q convolved with itself j times by
the labelled terms C[d,k] t**(k-1) exp(-d*t) / (k-1)!.  Its Laplace
transform is R(a)**j.  All 4*j pole/order slots are retained, including
zero coefficients: no signs or source-channel labels are discarded.

The constructor uses finite Laurent expansions with Fraction arithmetic,
not a symbolic-algebra dependency.  At each pole -d, put z=a+d and expand
z*R(z-d) through degree j-1.  Its j-th power determines the complete
principal part of R**j at that pole.  There is no remaining polynomial
part, since R**j vanishes at infinity.  Uniqueness of partial fractions
therefore proves the identity for every admissible j, independently of
the tests.  The same construction works for every positive integer j;
the implementation deliberately bounds j by MAX_POWER.

Q(0)=0 and Q'(0)=15, so the first 2*j-1 Taylor coefficients of Q**(*j)
vanish and its coefficient of t**(2*j-1) is 15**j/(2*j-1)!.  The methods
below calculate these coefficients from the complete signed expansion;
they do not return the asserted cancellation as a hard-coded value.

Continuous convolution time t and BBP arithmetic time n are different
variables.  The source substitution is a=8*n-7 for n >= 1.

Proof, domains, provenance and controls:
research/2026-11-15/bbp_volume_algebra/TRANSLATION_NOTES.md.
"""

from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from math import factorial


SOURCE_SHIFTS = (0, 3, 4, 5)
SOURCE_RESIDUES = (4, -2, -1, -1)
MAX_POWER = 12
MAX_TAYLOR_DEGREE = 64


def _bounded_integer(value: int, lower: int, upper: int, name: str) -> int:
    if type(value) is not int or not lower <= value <= upper:
        raise ValueError(f"{name} must be an integer in [{lower}, {upper}]")
    return value


def _positive_rational(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction):
        raise ValueError("Laplace argument must be an exact int or Fraction")
    result = Fraction(value)
    if result <= 0:
        raise ValueError("Laplace argument must be positive")
    return result


def source_laplace(a: int | Fraction) -> Fraction:
    """Return the authentic R(a) exactly, on positive rational a only."""
    a = _positive_rational(a)
    return sum((Fraction(c) / (a + d)
                for d, c in zip(SOURCE_SHIFTS, SOURCE_RESIDUES)), Fraction())


@dataclass(frozen=True)
class PoleTerm:
    """C/(a+shift)**order and its inverse-Laplace exponential monomial.

    The inverse transform is
    ``kernel_coefficient * t**kernel_degree * exp(-shift*t)``.
    A zero coefficient still retains its labelled basis slot.
    """

    shift: int
    order: int
    coefficient: Fraction

    def __post_init__(self) -> None:
        if type(self.shift) is not int or self.shift not in SOURCE_SHIFTS:
            raise ValueError("shift must be one of the four authentic source shifts")
        _bounded_integer(self.order, 1, MAX_POWER, "pole order")
        if type(self.coefficient) not in (int, Fraction):
            raise ValueError("pole coefficient must be an exact int or Fraction")
        object.__setattr__(self, "coefficient", Fraction(self.coefficient))

    @property
    def kernel_degree(self) -> int:
        return self.order - 1

    @property
    def kernel_coefficient(self) -> Fraction:
        return self.coefficient / factorial(self.kernel_degree)


def _truncated_product(left: tuple[Fraction, ...],
                       right: tuple[Fraction, ...],
                       size: int) -> tuple[Fraction, ...]:
    result = [Fraction() for _ in range(size)]
    for i, x in enumerate(left):
        for k in range(min(len(right), size - i)):
            result[i + k] += x * right[k]
    return tuple(result)


def _principal_parts(power: int) -> tuple[PoleTerm, ...]:
    terms = []
    for shift, residue in zip(SOURCE_SHIFTS, SOURCE_RESIDUES):
        # F(z)=z*R(z-shift)=residue + z*H(z).  Only degrees < power
        # can contribute to the principal part z**(-power) F(z)**power.
        local = (Fraction(residue),) + tuple(
            sum((Fraction(other_residue * (-1) ** (degree - 1),
                          (other_shift - shift) ** degree)
                 for other_shift, other_residue
                 in zip(SOURCE_SHIFTS, SOURCE_RESIDUES)
                 if other_shift != shift), Fraction())
            for degree in range(1, power)
        )
        raised = (Fraction(1),)
        for _ in range(power):
            raised = _truncated_product(raised, local, power)
        terms.extend(PoleTerm(shift, order, raised[power - order])
                     for order in range(1, power + 1))
    return tuple(terms)


@dataclass(frozen=True)
class GammaKernelPower:
    """The source-authenticated j-fold continuous-lag convolution kernel.

    ``terms`` is derived from ``power`` and cannot be supplied by a caller.
    Construction uses O(power**3) rational operations and O(power) stored
    coefficients per pole.  Bit complexity also depends on integer sizes.
    A Taylor request uses at most 4*power*(degree+1) term contributions.
    No numerical integration, infinite expansion or floating-point input
    is part of this exact interface.
    """

    power: int
    terms: tuple[PoleTerm, ...] = field(init=False)

    def __post_init__(self) -> None:
        _bounded_integer(self.power, 1, MAX_POWER, "convolution power")
        object.__setattr__(self, "terms", _principal_parts(self.power))

    def laplace(self, a: int | Fraction) -> Fraction:
        """Evaluate the partial-fraction transform at positive rational a."""
        a = _positive_rational(a)
        return sum((term.coefficient / (a + term.shift) ** term.order
                    for term in self.terms), Fraction())

    def taylor_coefficient(self, degree: int) -> Fraction:
        """Return [t**degree]Q**(*power), not its unnormalized derivative."""
        _bounded_integer(degree, 0, MAX_TAYLOR_DEGREE, "Taylor degree")
        return sum((term.kernel_coefficient
                    * Fraction((-term.shift) ** (degree - term.kernel_degree),
                               factorial(degree - term.kernel_degree))
                    for term in self.terms if term.kernel_degree <= degree),
                   Fraction())

    def taylor_coefficients(self, through: int) -> tuple[Fraction, ...]:
        """Return the exact Taylor coefficients in degrees 0 through through."""
        _bounded_integer(through, 0, MAX_TAYLOR_DEGREE, "Taylor degree")
        return tuple(self.taylor_coefficient(degree)
                     for degree in range(through + 1))


@lru_cache(maxsize=MAX_POWER)
def _cached_kernel_power(power: int) -> GammaKernelPower:
    return GammaKernelPower(power)


def source_kernel_power(power: int) -> GammaKernelPower:
    """Construct a bounded exact kernel; reject booleans, floats and j=0.

    Power zero would be the convolution identity delta distribution,
    outside this ordinary-kernel interface.  Validate before caching so
    Python's equal/hash-compatible numeric types cannot bypass the guard.
    """
    _bounded_integer(power, 1, MAX_POWER, "convolution power")
    return _cached_kernel_power(power)
