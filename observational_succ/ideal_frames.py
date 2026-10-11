"""Finite exact derivative-probe laboratory for ideal observational frames.

Scope: finite polynomial sources and finite jets ONLY. This module does not
sample infinite derivative families, prove a source is analytic, or reconstruct
arbitrary smooth/analytic germs. The corresponding infinite-stage theorems
and counterexamples are proved/discussed in the research note.

Each source query is a derivative-at-zero probe, and each SUCC frame adds
one new probe while preserving all actual earlier results. Selecting the
"most plausible" polynomial is NEVER evidence that the true source belongs
to a stipulated finite-degree model class.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial


class IdealFrameError(ValueError):
    """An invalid finite probe, conflicting source record or unjustified report."""


def _q(value) -> Fraction:
    if type(value) is int or isinstance(value, Fraction):
        return Fraction(value)
    raise IdealFrameError("Exact integer/Fraction coordinates required, not floats")


def _order(value: int) -> int:
    if type(value) is not int or not 0 <= value <= 63:
        raise IdealFrameError("Finite derivative order must be an integer in 0..63")
    return value


@dataclass(frozen=True)
class PolynomialSource:
    """A polynomial in powers of x, given by exact rational coefficients."""

    coefficients: tuple[Fraction, ...]

    def __post_init__(self):
        if type(self.coefficients) is not tuple or not 1 <= len(self.coefficients) <= 64:
            raise IdealFrameError("Finite polynomial coefficients must be a nonempty bounded tuple")
        values = tuple(_q(v) for v in self.coefficients)
        while len(values) > 1 and values[-1] == 0:
            values = values[:-1]
        object.__setattr__(self, "coefficients", values)

    @property
    def degree(self) -> int:
        return len(self.coefficients) - 1

    def derivative_at_zero(self, order: int) -> Fraction:
        order = _order(order)
        if order > self.degree:
            return Fraction(0)
        return self.coefficients[order] * factorial(order)

    def jet(self, horizon: int) -> tuple[Fraction, ...]:
        horizon = _order(horizon)
        return tuple(self.derivative_at_zero(k) for k in range(horizon + 1))

    def value(self, x) -> Fraction:
        x = _q(x)
        return sum((a * x**k for k, a in enumerate(self.coefficients)), Fraction(0))


@dataclass(frozen=True)
class IdealJetFrame:
    """A source-faithful finite history of every derivative probe through horizon."""

    horizon: int
    observed_jet: tuple[Fraction, ...]

    def __post_init__(self):
        n = _order(self.horizon)
        if type(self.observed_jet) is not tuple or len(self.observed_jet) != n + 1:
            raise IdealFrameError("One source outcome required for every probe through horizon")
        object.__setattr__(self, "observed_jet", tuple(_q(v) for v in self.observed_jet))

    @classmethod
    def initial(cls, source: PolynomialSource) -> "IdealJetFrame":
        if not isinstance(source, PolynomialSource):
            raise IdealFrameError("Source must be an explicitly typed polynomial")
        return cls(0, source.jet(0))

    def compatible(self, candidate: PolynomialSource) -> bool:
        if not isinstance(candidate, PolynomialSource):
            raise IdealFrameError("Only polynomial candidates accepted in the finite lab")
        return candidate.jet(self.horizon) == self.observed_jet

    def succ(self, source: PolynomialSource) -> "IdealJetFrame":
        """Advance by one ideal probe; reject attempts to rewrite past outcomes."""
        if self.horizon == 63:
            raise IdealFrameError("Finite probe horizon exceeded")
        if not self.compatible(source):
            raise IdealFrameError("New source conflicts with previously observed history")
        return IdealJetFrame(
            self.horizon + 1,
            self.observed_jet + (source.derivative_at_zero(self.horizon + 1),),
        )

    def reconstruct_under_degree_assumption(self, degree_bound: int) -> PolynomialSource:
        """Unique fitting member of P_degree_bound, CONDITIONAL on that premise.

        The premise that the genuine source is a polynomial of degree <= d
        is EXTERNAL to observed finite jets. It is not itself certified.
        A higher observed nonzero derivative refutes the proposed bound.
        """
        d = _order(degree_bound)
        if self.horizon < d:
            raise IdealFrameError("Insufficient probes for stipulated polynomial degree")
        if any(self.observed_jet[k] != 0 for k in range(d + 1, self.horizon + 1)):
            raise IdealFrameError("Recorded derivative contradicts the degree bound")
        return PolynomialSource(
            tuple(self.observed_jet[k] / factorial(k) for k in range(d + 1))
        )


def finite_probe_equivalent(a: PolynomialSource, b: PolynomialSource, horizon: int) -> bool:
    """Indistinguishability by exactly the currently accessible probe family."""
    if not isinstance(a, PolynomialSource) or not isinstance(b, PolynomialSource):
        raise IdealFrameError("Finite source must be a typed polynomial")
    return a.jet(horizon) == b.jet(horizon)


def analytic_finite_stage_adversary(horizon: int) -> tuple[PolynomialSource, PolynomialSource]:
    """0 versus x^(n+1): both analytic, same jets through n, different at n+1."""
    n = _order(horizon)
    if n == 63:
        raise IdealFrameError("Need a finite next derivative outside the current horizon")
    return PolynomialSource((0,)), PolynomialSource((0,) * (n + 1) + (1,))


def divergent_analytic_jet_prefix(horizon: int) -> tuple[Fraction, ...]:
    """Taylor coefficients a_k=k! through n; every prefix is polynomial-realizable.

    The infinite formal series sum(k! x^k) has radius of convergence ZERO,
    so the compatible finite analytic-polynomial stages do not yield an
    analytic germ at omega. This code returns only a finite prefix.
    """
    return tuple(Fraction(factorial(k)) for k in range(_order(horizon) + 1))
