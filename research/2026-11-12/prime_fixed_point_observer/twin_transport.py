"""Exact two-boundary transport and lossless arithmetic return extensions.

Finite linear maps use real rational coefficients, so transpose implements
the adjoint.  The accompanying derivation states the complex Hilbert-space
theorems separately.  Sparse return maps act on actual nonnegative integer
labels: no finite matrix boundary is silently imposed.

Keeping an environment flag is a mathematical information-preserving
construction.  It is not a claim of a physical quantum implementation or
of an observer deciding an infinite arithmetic statement.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, Mapping, Sequence


Rational = int | Fraction
Vector = tuple[Fraction, ...]
Matrix = tuple[Vector, ...]
SparseState = dict[int, Fraction]
BlockState = tuple[SparseState, SparseState]
FlaggedState = dict[tuple[tuple[int, ...], int], Fraction]


def _integer(value: int, name: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    return value


def _rational(value: Rational) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("amplitudes must be exact integers or Fractions")
    return Fraction(value)


def vector(values: Sequence[Rational], dimension: int | None = None) -> Vector:
    result = tuple(_rational(value) for value in values)
    if dimension is not None:
        _integer(dimension, "dimension", 1)
        if len(result) != dimension:
            raise ValueError("vector dimension does not match its space")
    return result


def inner(left: Sequence[Rational], right: Sequence[Rational]) -> Fraction:
    left, right = vector(left), vector(right)
    if len(left) != len(right):
        raise ValueError("inner product requires matching dimensions")
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


@dataclass(frozen=True)
class Space:
    """A named finite channel; equally sized distinct names stay distinct."""

    name: str
    dimension: int

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("space name must be a nonempty string")
        _integer(self.dimension, "dimension", 1)


@dataclass(frozen=True)
class LinearMap:
    """Target-row/source-column exact matrix with declared channel types."""

    source: Space
    target: Space
    entries: Matrix

    def __post_init__(self) -> None:
        if not isinstance(self.source, Space) or not isinstance(self.target, Space):
            raise TypeError("map endpoints must be Space objects")
        rows = tuple(vector(row, self.source.dimension) for row in self.entries)
        if len(rows) != self.target.dimension:
            raise ValueError("matrix row count does not match target space")
        object.__setattr__(self, "entries", rows)

    @classmethod
    def identity(cls, space: Space) -> LinearMap:
        return cls(space, space, tuple(tuple(Fraction(i == j)
                       for j in range(space.dimension))
                       for i in range(space.dimension)))

    def apply(self, state: Sequence[Rational]) -> Vector:
        state = vector(state, self.source.dimension)
        return tuple(inner(row, state) for row in self.entries)

    def adjoint(self) -> LinearMap:
        return LinearMap(self.target, self.source,
                         tuple(tuple(self.entries[i][j]
                                     for i in range(self.target.dimension))
                               for j in range(self.source.dimension)))

    def after(self, previous: LinearMap) -> LinearMap:
        if not isinstance(previous, LinearMap):
            raise TypeError("previous must be a LinearMap")
        if previous.target != self.source:
            raise ValueError("composition has mismatched channel types")
        rows = tuple(tuple(sum((self.entries[i][k] * previous.entries[k][j]
                               for k in range(self.source.dimension)), Fraction(0))
                           for j in range(previous.source.dimension))
                     for i in range(self.target.dimension))
        return LinearMap(previous.source, self.target, rows)

    def minus(self, other: LinearMap) -> LinearMap:
        if self.source != other.source or self.target != other.target:
            raise ValueError("map difference has mismatched channel types")
        return LinearMap(self.source, self.target,
                         tuple(tuple(a - b for a, b in zip(row_a, row_b))
                               for row_a, row_b in zip(self.entries, other.entries)))

    def is_unitary(self) -> bool:
        adjoint = self.adjoint()
        return (adjoint.after(self) == self.identity(self.source)
                and self.after(adjoint) == self.identity(self.target))


@dataclass(frozen=True)
class CutProfile:
    """Analyst-only all-cut calibration, not a meeting protocol transcript.

    An actual meeting compares the current pair of declared outputs at
    one selected cut, after their frame transport into the same fiber.
    These arrays must not be interpreted as histories available to the
    other observer or as permission to compare raw observation histories.
    """

    forward: tuple[Vector, ...]
    backward: tuple[Vector, ...]
    pairings: tuple[Fraction, ...]
    local_defects: tuple[Fraction, ...]
    squared_state_gaps: tuple[Fraction, ...]


@dataclass(frozen=True)
class LinearChain:
    """A finite typed path, including a zero-arrow identity path."""

    spaces: tuple[Space, ...]
    arrows: tuple[LinearMap, ...]

    def __post_init__(self) -> None:
        spaces, arrows = tuple(self.spaces), tuple(self.arrows)
        if not spaces or len(spaces) != len(arrows) + 1:
            raise ValueError("a chain needs one more space than arrows")
        if any(not isinstance(space, Space) for space in spaces):
            raise TypeError("chain entries must be Space objects")
        for i, arrow in enumerate(arrows):
            if not isinstance(arrow, LinearMap):
                raise TypeError("chain arrows must be LinearMap objects")
            if arrow.source != spaces[i] or arrow.target != spaces[i + 1]:
                raise ValueError("chain arrow has mismatched channel types")
        object.__setattr__(self, "spaces", spaces)
        object.__setattr__(self, "arrows", arrows)

    def total(self) -> LinearMap:
        total = LinearMap.identity(self.spaces[0])
        for arrow in self.arrows:
            total = arrow.after(total)
        return total

    def cuts(self, left: Sequence[Rational], right: Sequence[Rational],
             *, reverse_chain: LinearChain | None = None) -> CutProfile:
        """Forward A, backward B*, with B=A unless explicitly supplied.

        Pairing differences equal <y_(k+1),(A_(k+1)-B_(k+1))x_k>.
        Backward transport is dual propagation, not inversion of A.
        All-cut arrays are a mathematical calibration, not actual
        comparison of the observers' histories.  Only the outputs at the
        selected meeting cut enter a meeting comparator, after declared
        frame alignment.  Space names alone do not implement that alignment.
        """
        reverse_chain = self if reverse_chain is None else reverse_chain
        if not isinstance(reverse_chain, LinearChain):
            raise TypeError("reverse_chain must be a LinearChain")
        if reverse_chain.spaces != self.spaces:
            raise ValueError("the twin chains must use the same channel types")
        forward = [vector(left, self.spaces[0].dimension)]
        for arrow in self.arrows:
            forward.append(arrow.apply(forward[-1]))
        backward = [vector(right, self.spaces[-1].dimension)]
        for arrow in reversed(reverse_chain.arrows):
            backward.append(arrow.adjoint().apply(backward[-1]))
        backward.reverse()
        pairings = tuple(inner(y, x) for x, y in zip(forward, backward))
        defects = tuple(inner(backward[k + 1],
                              a.minus(b).apply(forward[k]))
                        for k, (a, b) in enumerate(zip(self.arrows,
                                                      reverse_chain.arrows)))
        gaps = []
        for x, y in zip(forward, backward):
            difference = tuple(a - b for a, b in zip(x, y))
            gaps.append(inner(difference, difference))
        return CutProfile(tuple(forward), tuple(backward), pairings,
                          defects, tuple(gaps))


def sparse_state(state: Mapping[int, Rational]) -> SparseState:
    """Finite support in l2(N_0); label zero is a nonzero basis vector."""
    result = {}
    for label, coefficient in state.items():
        _integer(label, "basis label")
        coefficient = _rational(coefficient)
        if coefficient:
            result[label] = coefficient
    return result


def sparse_inner(left: Mapping[int, Rational],
                 right: Mapping[int, Rational]) -> Fraction:
    left, right = sparse_state(left), sparse_state(right)
    return sum((value * right.get(label, Fraction(0))
                for label, value in left.items()), Fraction(0))


def _add_scaled(target: SparseState, source: Mapping[int, Fraction],
                scale: int = 1) -> None:
    for label, value in source.items():
        target[label] = target.get(label, Fraction(0)) + scale * value
        if not target[label]:
            del target[label]


@dataclass(frozen=True)
class CenteredReturn:
    """The proper reduced return T_(q,r)=D_r D_q*, q>r>=1, gcd(q,r)=1."""

    q: int
    r: int

    def __post_init__(self) -> None:
        _integer(self.q, "q", 2)
        _integer(self.r, "r", 1)
        if self.r >= self.q or gcd(self.q, self.r) != 1:
            raise ValueError("a proper reduced return needs q>r and gcd(q,r)=1")

    def basis(self, label: int, *, adjoint: bool = False) -> int | None:
        _integer(label, "basis label")
        if not isinstance(adjoint, bool):
            raise TypeError("adjoint must be a bool")
        divisor, multiplier = (self.r, self.q) if adjoint else (self.q, self.r)
        return multiplier * (label // divisor) if label % divisor == 0 else None

    def apply(self, state: Mapping[int, Rational], *, adjoint: bool = False
              ) -> SparseState:
        if not isinstance(adjoint, bool):
            raise TypeError("adjoint must be a bool")
        result: SparseState = {}
        for label, value in sparse_state(state).items():
            target = self.basis(label, adjoint=adjoint)
            if target is not None:
                result[target] = value
        return result

    def reject(self, state: Mapping[int, Rational], *, range_side: bool = False
               ) -> SparseState:
        """(I-P_q)x, or (I-P_r)x on the range side."""
        if not isinstance(range_side, bool):
            raise TypeError("range_side must be a bool")
        divisor = self.r if range_side else self.q
        return {label: value for label, value in sparse_state(state).items()
                if label % divisor}

    def unitary(self, state: tuple[Mapping[int, Rational], Mapping[int, Rational]],
                *, adjoint: bool = False) -> BlockState:
        """U=[[T,I-P_r],[I-P_q,-T*]] on H directsum H, or its adjoint.

        This is a one-step extension.  U**j compressed to the first block is
        not asserted to equal T**j.  Use fresh_flags for the finite-path
        all-accept branch, retaining every unused branch in the output.
        Compression is not intertwining: U J differs from J T on rejected
        inputs.  Independently selected extensions need not preserve the
        original category's composition relations.
        """
        if not isinstance(adjoint, bool):
            raise TypeError("adjoint must be a bool")
        if len(state) != 2:
            raise ValueError("a block state needs two components")
        x, y = sparse_state(state[0]), sparse_state(state[1])
        if not adjoint:
            first = self.apply(x)
            _add_scaled(first, self.reject(y, range_side=True))
            second = self.reject(x)
            _add_scaled(second, self.apply(y, adjoint=True), -1)
        else:
            first = self.apply(x, adjoint=True)
            _add_scaled(first, self.reject(y))
            second = self.reject(x, range_side=True)
            _add_scaled(second, self.apply(y), -1)
        return first, second


def fresh_flags(returns: Iterable[CenteredReturn],
                state: Mapping[int, Rational]) -> FlaggedState:
    """Retain a fresh accept/reject bit at each step of a finite path.

    The output key is (history, basis_label), with 0=accept and 1=reject.
    Every branch continues through later returns.  All-zero history has
    amplitude T_n...T_1 x; other histories are retained, never normalized
    away.  Memory grows with the finite number of steps.
    These records are internal environmental state, not cross-observer
    history-comparison inputs.  A meeting uses separately declared current
    outputs in a common transported frame.
    """
    returns = tuple(returns)
    if any(not isinstance(item, CenteredReturn) for item in returns):
        raise TypeError("returns must contain CenteredReturn objects")
    current: FlaggedState = {((), label): value
                            for label, value in sparse_state(state).items()}
    for item in returns:
        updated: FlaggedState = {}
        for (history, label), value in current.items():
            target = item.basis(label)
            key = (history + (int(target is None),),
                   label if target is None else target)
            updated[key] = updated.get(key, Fraction(0)) + value
            if not updated[key]:
                del updated[key]
        current = updated
    return current


def flag_branch(state: FlaggedState, history: tuple[int, ...]) -> SparseState:
    if any(type(flag) is not int or flag not in (0, 1) for flag in history):
        raise ValueError("history flags must be integers 0 or 1")
    return sparse_state({label: value for (flags, label), value in state.items()
                         if flags == history})
