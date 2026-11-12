"""Exact mixed arithmetic return paths on the positive-integer carrier.

For n >= 2 and 1 <= a <= n, R(n,a) = V_n* S**(n-a) V_a.  The
nontrivial family uses a < n; a == n is retained only as an explicit identity
control.  Put g = gcd(n,a), q = n/g, r = a/g.  Then

    R(n,a) e_(1+q*k) = e_(1+r*k),  k >= 0,

and all other basis vectors are killed.  Sparse states and amplitudes below
are exact real rationals.  A coherent sum is a declared linear observation,
not an inferred physical wave, probability, or new primality algorithm.

The companion proof note supplies the infinite-dimensional statements.
Finite evaluation alone does not establish strong convergence on all l2.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, Mapping


Rational = int | Fraction
SparseState = dict[int, Fraction]


def _integer(value: int, name: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    return value


def _rational(value: Rational, name: str = "amplitude") -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be an exact integer or Fraction")
    return Fraction(value)


def sparse_state(state: Mapping[int, Rational]) -> SparseState:
    """Validate a finite state without accepting floating-point coefficients."""
    result = {}
    for label, coefficient in state.items():
        _integer(label, "basis label", 1)
        coefficient = _rational(coefficient)
        if coefficient:
            result[label] = coefficient
    return result


def norm_squared(state: Mapping[int, Rational]) -> Fraction:
    """Squared l2 norm; it is an intensity, not necessarily a probability."""
    return sum((coefficient**2 for coefficient in sparse_state(state).values()),
               Fraction(0))


@dataclass(frozen=True)
class Affine:
    """An authentic map m -> a*m+b, with a >= 1 and b >= 0."""

    a: int
    b: int = 0

    def __post_init__(self) -> None:
        _integer(self.a, "multiplier", 1)
        _integer(self.b, "offset", 0)

    def __call__(self, label: int) -> int:
        _integer(label, "basis label", 1)
        return self.a * label + self.b

    def after(self, previous: Affine) -> Affine:
        """Return self composed after previous, keeping composition order."""
        if not isinstance(previous, Affine):
            raise TypeError("previous must be Affine")
        return Affine(self.a * previous.a, self.a * previous.b + self.b)


def affine_hom(source: int, target: int) -> tuple[Affine, ...]:
    """All positive affine maps taking source to target, in multiplier order.

    These are morphisms of the forward action category.  It has no return
    arrows between unequal objects.  R(n,a) additionally uses the Hilbert
    adjoint/partial division, so it belongs to an extended operator setting.
    """
    _integer(source, "source", 1)
    _integer(target, "target", 1)
    return tuple(Affine(a, target - a * source)
                 for a in range(1, target // source + 1))


def evaluate_word(label: int, steps: Iterable[tuple[str, int]]) -> int | None:
    """Evaluate typed steps in execution order, without a gcd shortcut.

    S,k means k successors, V,d means multiply by d, and D,d means the
    partial division V_d*.  None denotes the zero vector, not basis label 0.
    Every step is validated even after a partial division has killed input.
    """
    _integer(label, "basis label", 1)
    result: int | None = label
    for operation, amount in steps:
        if operation not in ("S", "V", "D"):
            raise ValueError(f"unknown operation: {operation!r}")
        _integer(amount, "step amount", 0 if operation == "S" else 1)
        if result is None:
            continue
        if operation == "S":
            result += amount
        elif operation == "V":
            result *= amount
        else:
            result = result // amount if result % amount == 0 else None
    return result


@dataclass(frozen=True)
class ReturnPath:
    """R(n,a); a=n is the explicitly identified trivial return."""

    n: int
    a: int

    def __post_init__(self) -> None:
        _integer(self.n, "n", 2)
        _integer(self.a, "a", 1)
        if self.a > self.n:
            raise ValueError("a must not exceed n")

    @property
    def proper(self) -> bool:
        return self.a < self.n

    @property
    def initial_period(self) -> int:
        return self.n // gcd(self.n, self.a)

    @property
    def range_period(self) -> int:
        return self.a // gcd(self.n, self.a)

    @property
    def forward(self) -> Affine:
        return Affine(self.a, self.n - self.a)

    @property
    def word(self) -> tuple[tuple[str, int], ...]:
        return (("V", self.a), ("S", self.n - self.a), ("D", self.n))

    def basis(self, label: int) -> int | None:
        return self.power_basis(label, 1)

    def adjoint_basis(self, label: int) -> int | None:
        return self.power_basis(label, 1, adjoint=True)

    def power_basis(self, label: int, rounds: int,
                    *, adjoint: bool = False) -> int | None:
        """Exact R**rounds (or its adjoint), including the zero-round identity."""
        _integer(label, "basis label", 1)
        _integer(rounds, "rounds", 0)
        if not isinstance(adjoint, bool):
            raise TypeError("adjoint must be a bool")
        q, r = self.initial_period, self.range_period
        if adjoint:
            q, r = r, q
        quotient, remainder = divmod(label - 1, q**rounds)
        return None if remainder else 1 + r**rounds * quotient

    def apply(self, state: Mapping[int, Rational], *, rounds: int = 1,
              adjoint: bool = False) -> SparseState:
        """Apply to a finite rational state, with no finite-matrix truncation."""
        _integer(rounds, "rounds", 0)
        if not isinstance(adjoint, bool):
            raise TypeError("adjoint must be a bool")
        result: SparseState = {}
        for label, coefficient in sparse_state(state).items():
            target = self.power_basis(label, rounds, adjoint=adjoint)
            if target is not None:
                result[target] = result.get(target, Fraction(0)) + coefficient
        return {label: coefficient for label, coefficient in result.items()
                if coefficient}


def return_family(n: int) -> tuple[ReturnPath, ...]:
    """The n-1 proper paths; the a=n identity is deliberately excluded."""
    _integer(n, "n", 2)
    return tuple(ReturnPath(n, a) for a in range(1, n))


def domain_multiplicities(n: int) -> dict[int, int]:
    """Count paths with each pointed initial period q = n/gcd(n,a)."""
    return dict(sorted(Counter(path.initial_period
                               for path in return_family(n)).items()))


def family_eigenvalue(n: int, label: int) -> int:
    """K_n e_m = (gcd(n,m-1)-1)e_m for K_n = sum_(a<n) R*R."""
    _integer(n, "n", 2)
    _integer(label, "basis label", 1)
    return gcd(n, label - 1) - 1


def normalized_eigenvalue(n: int, label: int) -> Fraction:
    return Fraction(family_eigenvalue(n, label), n - 1)


def projection_defect(n: int, label: int) -> Fraction:
    """Eigenvalue of K/(n-1) - (K/(n-1))**2; always nonnegative."""
    eigenvalue = normalized_eigenvalue(n, label)
    return eigenvalue * (1 - eigenvalue)


def family_observation(n: int, state: Mapping[int, Rational],
                       *, normalized: bool = False) -> SparseState:
    """Apply the positive family Gram, or its normalized contraction."""
    _integer(n, "n", 2)
    if not isinstance(normalized, bool):
        raise TypeError("normalized must be a bool")
    denominator = n - 1 if normalized else 1
    result = {label: coefficient * Fraction(family_eigenvalue(n, label), denominator)
              for label, coefficient in sparse_state(state).items()}
    return {label: coefficient for label, coefficient in result.items()
            if coefficient}


def _weighted_paths(n: int, coefficients: Mapping[int, Rational]):
    _integer(n, "n", 2)
    for a, coefficient in coefficients.items():
        path = ReturnPath(n, a)
        if not path.proper:
            raise ValueError("coherent family excludes the a=n identity")
        yield path, _rational(coefficient, "path coefficient")


def coherent_sum(n: int, coefficients: Mapping[int, Rational],
                 state: Mapping[int, Rational]) -> SparseState:
    """Sum exact real amplitudes after the paths reach a common carrier.

    No normalization is implicit.  Distinct output labels remain orthogonal;
    amplitudes interfere only when their output labels coincide.
    """
    state = sparse_state(state)
    result: SparseState = {}
    for path, weight in _weighted_paths(n, coefficients):
        for label, amplitude in path.apply(state).items():
            result[label] = result.get(label, Fraction(0)) + weight * amplitude
    return {label: coefficient for label, coefficient in result.items()
            if coefficient}


def separate_intensity(n: int, coefficients: Mapping[int, Rational],
                       state: Mapping[int, Rational]) -> Fraction:
    """Sum separate path intensities, retaining the path label until readout."""
    state = sparse_state(state)
    return sum((weight**2 * norm_squared(path.apply(state))
                for path, weight in _weighted_paths(n, coefficients)), Fraction(0))
