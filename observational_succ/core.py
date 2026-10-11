"""Exact field-relative steps, path domains, and declared unitary basis lifts.

No preferred direction is inferred for a space. Scalars are exact rational
complex numbers; field coordinates are rational tuples (or residue tuples).
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd
from typing import Iterable


class ActualizationError(ValueError):
    """A declared domain, history, or observation contract was violated."""


class DomainError(ActualizationError):
    pass


class BudgetExceeded(ActualizationError):
    pass


class IncompleteObservation(ActualizationError):
    pass


def rational(x: int | str | Q) -> Q:
    if isinstance(x, bool) or not isinstance(x, (int, str, Q)):
        raise DomainError("Use exact int, Fraction or rational string; floats are not exact inputs")
    try:
        y = Q(x)
    except (ValueError, ZeroDivisionError) as exc:
        raise DomainError("Invalid rational") from exc
    if max(y.numerator.bit_length(), y.denominator.bit_length()) > 512:
        raise BudgetExceeded("Rational exceeds the 512-bit coordinate/scalar budget")
    return y


@dataclass(frozen=True)
class Scalar:
    """Q(i), not binary floating-point complex arithmetic."""
    re: Q = Q(0)
    im: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "re", rational(self.re))
        object.__setattr__(self, "im", rational(self.im))

    @classmethod
    def of(cls, x=0) -> Scalar:
        return x if isinstance(x, cls) else cls(rational(x))

    def __add__(self, other):
        b = Scalar.of(other)
        return Scalar(self.re + b.re, self.im + b.im)

    __radd__ = __add__

    def __neg__(self):
        return Scalar(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-Scalar.of(other))

    def __rsub__(self, other):
        return Scalar.of(other) - self

    def __mul__(self, other):
        b = Scalar.of(other)
        return Scalar(self.re*b.re-self.im*b.im, self.re*b.im+self.im*b.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = Scalar.of(other)
        if not b:
            raise DomainError("Division by zero scalar")
        c = self * b.conjugate()
        return Scalar(c.re/b.norm2(), c.im/b.norm2())

    def __pow__(self, n):
        if type(n) is not int or n < 0:
            raise DomainError("Scalar power requires a nonnegative integer")
        result, base = ONE, self
        while n:
            if n & 1:
                result = result * base
            base, n = base * base, n // 2
        return result

    def __bool__(self):
        return bool(self.re or self.im)

    def conjugate(self):
        return Scalar(self.re, -self.im)

    def norm2(self):
        return self.re*self.re + self.im*self.im

    def data(self):
        return {"re": str(self.re), "im": str(self.im)}

    @classmethod
    def from_data(cls, data):
        if not isinstance(data, dict) or set(data) != {"re", "im"}:
            raise DomainError("Malformed exact scalar")
        return cls(data["re"], data["im"])

    def __str__(self):
        return str(self.re) if not self.im else f"({self.re}+({self.im})i)"


ZERO, ONE, I = Scalar(), Scalar(1), Scalar(0, 1)
Coordinate = tuple[Q, ...]


@dataclass(frozen=True)
class Frame:
    """An explicitly chosen additive step, not a claim every space is a field.

    'natural' = N_0^d; 'integer' = Z^d; 'rational' = Q^d;
    'modular' = (Z/mZ)^d (a field only when d=1 and m is prime).
    """
    name: str = "N0"
    domain: str = "natural"
    step: Coordinate = (Q(1),)
    modulus: int | None = None

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name or len(self.name) > 128:
            raise DomainError("Frame needs a bounded nonempty name")
        if self.domain not in {"natural", "integer", "rational", "modular"}:
            raise DomainError("Unsupported domain")
        e = tuple(rational(x) for x in self.step)
        if not 1 <= len(e) <= 16:
            raise BudgetExceeded("Frame dimension must be 1..16")
        if self.domain == "modular":
            if type(self.modulus) is not int or not 2 <= self.modulus <= 1_000_000:
                raise DomainError("Modulus must be an integer in 2..1000000")
            if any(x.denominator != 1 for x in e):
                raise DomainError("Residue step must be integral")
            e = tuple(x % self.modulus for x in e)
        elif self.modulus is not None:
            raise DomainError("Only modular frames have a modulus")
        if self.domain in {"natural", "integer"} and any(x.denominator != 1 for x in e):
            raise DomainError("Integer-lattice step must be integral")
        if not any(e):
            raise DomainError("A successor direction cannot be zero in the declared space")
        object.__setattr__(self, "step", e)

    @property
    def dimension(self):
        return len(self.step)

    def point(self, x) -> Coordinate:
        try:
            xs = (x,) if isinstance(x, (int, str, Q)) else tuple(x)
        except TypeError as exc:
            raise DomainError("Coordinate must be exact scalar or coordinate sequence") from exc
        if len(xs) != self.dimension:
            raise DomainError("Coordinate dimension mismatch")
        xs = tuple(rational(v) for v in xs)
        if self.domain == "rational":
            return xs
        if any(v.denominator != 1 for v in xs):
            raise DomainError("Nonintegral lattice coordinate")
        if self.domain == "natural" and any(v < 0 for v in xs):
            raise DomainError("No predecessor below the N_0 boundary")
        return tuple(v % self.modulus for v in xs) if self.domain == "modular" else xs

    def succ(self, x, direction=1) -> Coordinate:
        if type(direction) is not int or direction not in {-1, 1}:
            raise DomainError("Direction must be +1 or -1")
        return self.point(tuple(v + direction*e for v, e in zip(self.point(x), self.step)))

    def scale(self, x, a, inverse=False):
        a = rational(a)
        if not a:
            raise DomainError("FUCC multiplier must be nonzero")
        if self.domain == "modular":
            if a.denominator != 1:
                raise DomainError("Residue multiplier must be integral")
            if inverse:
                if gcd(int(a), self.modulus) != 1:
                    raise DomainError("Nonunit modular multiplication has no single-valued inverse")
                a = Q(pow(int(a), -1, self.modulus))
        elif inverse:
            a = 1/a
        return self.point(tuple(v*a for v in self.point(x)))

    def data(self):
        return {"name": self.name, "domain": self.domain,
                "step": list(map(str, self.step)), "modulus": self.modulus}

    @classmethod
    def from_data(cls, d):
        if not isinstance(d, dict) or set(d) != {"name", "domain", "step", "modulus"}:
            raise DomainError("Malformed frame")
        return cls(d["name"], d["domain"], tuple(d["step"]), d["modulus"])


@dataclass(frozen=True)
class Operation:
    kind: str
    amount: Q = Q(1)

    def __post_init__(self):
        if self.kind not in {"succ", "inverse_succ", "multiply", "divide"}:
            raise DomainError("Unknown operation")
        object.__setattr__(self, "amount", rational(self.amount))
        if self.kind in {"multiply", "divide"} and not self.amount:
            raise DomainError("Zero multiplier is not reversible")
        if self.kind in {"succ", "inverse_succ"} and self.amount != 1:
            raise DomainError("Bare SUCC is one frame step, not a silently rescaled step")

    def apply(self, frame, x):
        if self.kind == "succ":
            return frame.succ(x)
        if self.kind == "inverse_succ":
            return frame.succ(x, -1)
        return frame.scale(x, self.amount, self.kind == "divide")

    def reversed(self):
        return Operation({"succ": "inverse_succ", "inverse_succ": "succ",
                          "multiply": "divide", "divide": "multiply"}[self.kind], self.amount)


@dataclass(frozen=True)
class Execution:
    frame: Frame
    states: tuple[Coordinate, ...]
    operations: tuple[Operation, ...]

    def reverse(self):
        return execute(self.frame, self.states[-1], tuple(op.reversed() for op in reversed(self.operations)))

    def fits(self, horizon: int):
        """Position-window test, distinct from structural shadow availability."""
        if self.frame.domain != "natural" or self.frame.dimension != 1:
            raise DomainError("Numeric prefix horizon applies only to one-dimensional N_0")
        return all(0 <= x[0] <= horizon for x in self.states)


def execute(frame: Frame, start, operations: Iterable[Operation], max_steps=256) -> Execution:
    ops = tuple(operations)
    if len(ops) > max_steps:
        raise BudgetExceeded("Execution path budget exceeded")
    states = [frame.point(start)]
    for op in ops:
        states.append(op.apply(frame, states[-1]))
    return Execution(frame, tuple(states), ops)


@dataclass(frozen=True)
class AffineChart:
    """Invertible diagonal affine change of rational coordinates only.

    We do not pretend an arbitrary rechart is a Q_p/R equivalence.
    """
    scale: Coordinate
    offset: Coordinate

    def __post_init__(self):
        a, b = tuple(map(rational, self.scale)), tuple(map(rational, self.offset))
        if not a or len(a) != len(b) or not all(a):
            raise DomainError("Affine chart needs matching dimensions and nonzero scales")
        object.__setattr__(self, "scale", a)
        object.__setattr__(self, "offset", b)

    def point(self, x):
        if len(x) != len(self.scale):
            raise DomainError("Chart dimension mismatch")
        return tuple(a*rational(v)+b for a, v, b in zip(self.scale, x, self.offset))

    def inverse(self):
        return AffineChart(tuple(1/a for a in self.scale), tuple(-b/a for a, b in zip(self.scale, self.offset)))

    def frame(self, original: Frame, name="transported"):
        if original.domain != "rational" or original.dimension != len(self.scale):
            raise DomainError("This chart implements Q^d coordinate covariance only")
        return Frame(name, "rational", tuple(a*e for a, e in zip(self.scale, original.step)))


@dataclass(frozen=True)
class BasisLift:
    """A declared exact unitary transport for a finite synthetic fiber basis."""
    name: str
    matrix: tuple[tuple[Scalar, ...], ...]
    initial: tuple[Scalar, ...]

    def __post_init__(self):
        m = tuple(tuple(Scalar.of(x) for x in row) for row in self.matrix)
        v = tuple(Scalar.of(x) for x in self.initial)
        n = len(v)
        if not self.name or not 1 <= n <= 16 or len(m) != n or any(len(row) != n for row in m):
            raise DomainError("Malformed finite basis lift")
        for i in range(n):
            for j in range(n):
                if sum((m[k][i].conjugate()*m[k][j] for k in range(n)), ZERO) != Scalar.of(int(i == j)):
                    raise DomainError("Declared norm-conserving basis transport is not unitary")
        object.__setattr__(self, "matrix", m)
        object.__setattr__(self, "initial", v)

    def apply(self, vector, direction=1):
        v = tuple(Scalar.of(x) for x in vector)
        if len(v) != len(self.initial) or direction not in {-1, 1}:
            raise DomainError("Invalid basis transport")
        m = self.matrix if direction == 1 else tuple(zip(*(tuple(x.conjugate() for x in row) for row in self.matrix)))
        out = tuple(sum((a*b for a, b in zip(row, v)), ZERO) for row in m)
        if sum(x.norm2() for x in out) != sum(x.norm2() for x in v):
            raise ActualizationError("Declared norm conservation failed")
        return out

    def data(self):
        return {"name": self.name, "matrix": [[x.data() for x in r] for r in self.matrix],
                "initial": [x.data() for x in self.initial]}

    @classmethod
    def from_data(cls, d):
        if not isinstance(d, dict) or set(d) != {"name", "matrix", "initial"}:
            raise DomainError("Malformed basis lift")
        return cls(d["name"], tuple(tuple(Scalar.from_data(x) for x in r) for r in d["matrix"]),
                   tuple(Scalar.from_data(x) for x in d["initial"]))
