"""Exact finite SU(2) Wilson trace observers, with classical completeness.

Reuse SUCC's Hamilton-rational arithmetic; no BBP-to-Wilson source identity
is implied.  Singles, pairs and ordered triples separate simultaneous SU(2)
conjugacy of every finite tuple.  The paper proof and conditioned inverse
bound are in research/2026-11-13/yang_mills_succ/coupled_wilson/TRACE_OBSERVER.md.
This is finite gauge kinematics, not continuum existence or a mass gap.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations
from typing import Iterable

from .hopf_source_exact import H, ONE


def _unit(value: H) -> H:
    if not isinstance(value, H):
        raise TypeError("an exact Hamilton quaternion H is required")
    if value.norm2() != 1:
        raise ValueError("the SU(2) carrier requires norm squared exactly one")
    return value


def stereographic_unit(coordinates: Iterable[int | Q]) -> H:
    """Rational chart t -> (1-|t|²,2t)/(1+|t|²), excluding only -1."""
    t = tuple(coordinates)
    if len(t) != 3 or any(type(x) not in (int, Q) for x in t):
        raise TypeError("three exact int/Fraction coordinates are required")
    t = tuple(Q(x) for x in t)
    radius2 = sum((x*x for x in t), Q())
    denominator = 1 + radius2
    return H((1-radius2)/denominator, *(2*x/denominator for x in t))


def conjugate_tuple(values: Iterable[H], gauge: H) -> tuple[H, ...]:
    """One shared SU(2) conjugation; independent conjugations are not allowed."""
    g = _unit(gauge)
    return tuple(g*_unit(q)*g.conj() for q in values)


def word_trace(values: Iterable[H], word: Iterable[int]) -> Q:
    """Normalized fundamental trace of an ordered word; letters are signed 1-based indices."""
    values = tuple(_unit(q) for q in values)
    result = ONE
    for letter in word:
        if type(letter) is not int or not 1 <= abs(letter) <= len(values):
            raise ValueError("each word letter must be a nonzero signed carrier index")
        factor = values[abs(letter)-1]
        result = result * (factor if letter > 0 else factor.conj())
    return result.a


def vector_dot(left: H, right: H) -> Q:
    return left.b*right.b + left.c*right.c + left.d*right.d


def oriented_volume(first: H, second: H, third: H) -> Q:
    """det[v_first v_second v_third] in the fixed i,j,k convention."""
    return (
        first.b*(second.c*third.d-second.d*third.c)
        - first.c*(second.b*third.d-second.d*third.b)
        + first.d*(second.b*third.c-second.c*third.b)
    )


@dataclass(frozen=True)
class TraceBank:
    """An observed finite trace bank, in lexicographic combination order.

    Shape and exact types are checked; arbitrary constructed banks are not
    asserted to be realizable by SU(2) tuples. Use ``trace_bank`` for a source.
    """

    singles: tuple[Q, ...]
    pairs: tuple[Q, ...]
    triples: tuple[Q, ...]

    def __post_init__(self) -> None:
        n = len(self.singles)
        if len(self.pairs) != n*(n-1)//2 or len(self.triples) != n*(n-1)*(n-2)//6:
            raise ValueError("trace-bank shape does not match its carrier size")
        for name in ("singles", "pairs", "triples"):
            entries = getattr(self, name)
            if type(entries) is not tuple or any(type(x) not in (int, Q) for x in entries):
                raise TypeError("immutable exact rational trace coordinates required")
            object.__setattr__(self, name, tuple(Q(x) for x in entries))

    @property
    def size(self) -> int:
        return len(self.singles)

    @property
    def pair_dictionary(self) -> dict[tuple[int, int], Q]:
        return dict(zip(combinations(range(self.size), 2), self.pairs))

    def gram(self) -> tuple[tuple[Q, ...], ...]:
        """Recover every imaginary-vector inner product, including diagonals."""
        pairs = self.pair_dictionary
        a = self.singles
        return tuple(tuple(
            1-a[i]*a[i] if i == j else a[i]*a[j]-pairs[tuple(sorted((i, j)))]
            for j in range(self.size)) for i in range(self.size))

    def volumes(self) -> tuple[Q, ...]:
        """Recover the signed triple volumes; squaring them would lose orientation."""
        a, pairs = self.singles, self.pair_dictionary
        return tuple(
            -2*a[i]*a[j]*a[k] + a[i]*pairs[j, k] + a[j]*pairs[i, k]
            + a[k]*pairs[i, j] - triple
            for (i, j, k), triple in zip(combinations(range(self.size), 3), self.triples)
        )


def trace_bank(values: Iterable[H]) -> TraceBank:
    values = tuple(_unit(q) for q in values)
    return TraceBank(
        tuple(q.a for q in values),
        tuple((values[i]*values[j]).a for i, j in combinations(range(len(values)), 2)),
        tuple((values[i]*values[j]*values[k]).a
              for i, j, k in combinations(range(len(values)), 3)),
    )


def same_gauge_orbit(left: Iterable[H], right: Iterable[H]) -> bool:
    """Exact SU(2) simultaneous-conjugacy decision, by the proved trace criterion.

    The conjugating unit quaternion may have irrational coordinates; the
    theorem does not restrict the gauge group to rational quaternions.
    """
    return trace_bank(left) == trace_bank(right)
