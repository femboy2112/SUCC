"""Exact finite boundary geometry and source-labelled zero-forcing inverse.

Paper scope: REALITY_PIN_OBSERVABLE_GEOMETRY.md. These routines use rational
matrices only; source passports are mathematical assumptions, not empirical
source authentication. No physical spacetime or universal graph inverse.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from .boundary_realization_selection import matrix_inverse


class GeometryError(ValueError):
    """Missing source condition or inconsistent exact boundary data."""


def _q(value):
    if type(value) not in (int, Q):
        raise GeometryError("exact integer/Fraction required")
    return Q(value)


def matrix(rows):
    out = tuple(tuple(_q(x) for x in row) for row in rows)
    if not out or not out[0] or any(len(row) != len(out[0]) for row in out):
        raise GeometryError("nonempty rectangular matrix required")
    return out


def transpose(a):
    return tuple(zip(*a))


def multiply(a, b):
    a, b = matrix(a), matrix(b)
    if len(a[0]) != len(b):
        raise GeometryError("matrix domain mismatch")
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), Q())
                       for col in transpose(b)) for row in a)


def identity(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def _symmetric(a):
    a = matrix(a)
    if len(a) != len(a[0]) or a != transpose(a):
        raise GeometryError("real symmetric operator required")
    return a


def coordinate_boundary(n, boundary):
    if (type(n) is not int or n < 1 or not boundary
            or len(set(boundary)) != len(boundary)
            or any(type(v) is not int or v < 0 or v >= n for v in boundary)):
        raise GeometryError("ordered distinct source boundary coordinates required")
    return tuple(tuple(Q(i == v) for v in boundary) for i in range(n))


def boundary_moments(a, b, maximum):
    """Return B^T A^k B for 0 <= k <= maximum, without diagonalization."""
    a, b = _symmetric(a), matrix(b)
    if len(a) != len(b) or type(maximum) is not int or maximum < 0:
        raise GeometryError("wrong source dimension or moment budget")
    out, current = [], b
    for k in range(maximum + 1):
        out.append(multiply(transpose(b), current))
        if k < maximum:
            current = multiply(a, current)
    return tuple(out)


def boundary_response(a, b, s):
    """Exact B^T(A+sI)^(-1)B at a nonpole rational parameter."""
    a, b, s = _symmetric(a), matrix(b), _q(s)
    shifted = tuple(tuple(x + (s if i == j else 0) for j, x in enumerate(row))
                    for i, row in enumerate(a))
    return multiply(transpose(b), multiply(matrix_inverse(shifted), b))


def block_hankel(moments, depth):
    """Gram of [B, AB, ..., A^(depth-1) B]."""
    if type(depth) is not int or depth < 1 or len(moments) < 2 * depth - 1:
        raise GeometryError("insufficient moment budget")
    m = len(moments[0])
    blocks = tuple(_symmetric(x) for x in moments)
    if any(len(x) != m for x in blocks):
        raise GeometryError("boundary dimensions changed")
    return tuple(tuple(blocks[i + j][u][v]
                       for j in range(depth) for v in range(m))
                 for i in range(depth) for u in range(m))


def rank(a):
    a = [list(row) for row in matrix(a)]
    pivot_row = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][j]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for i in range(pivot_row + 1, len(a)):
            scale = a[i][j]
            a[i] = [x - scale * y for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def first_return_extension(a, b, coupling):
    """Return (first differing order, positive Gram jump), or None if dark.

    The extension is [[A,C],[C^T,D]] with B extended by zero. D is arbitrary
    symmetric and does not enter the first jump. Cayley-Hamilton bounds the
    search by dim(A). No assumption of unsigned shortest-path visibility.
    """
    a, b, coupling = _symmetric(a), matrix(b), matrix(coupling)
    if len(a) != len(b) or len(coupling) != len(a):
        raise GeometryError("extension source dimensions disagree")
    current = b
    for depth in range(len(a)):
        outgoing = multiply(transpose(coupling), current)
        if any(x for row in outgoing for x in row):
            return 2 * depth + 2, multiply(transpose(outgoing), outgoing)
        current = multiply(a, current)
    return None


@dataclass(frozen=True)
class GraphPassport:
    """Predeclared labelled graph, boundary order and nonzero edge signs.

    Edge triples are (u,v,sign), u<v, sign in {-1,1}. A passport carries no
    weights and no inaccessible matrix entries. The topology is a prior.
    """
    size: int
    boundary: tuple[int, ...]
    edges: tuple[tuple[int, int, int], ...]
    source_id: str

    def __post_init__(self):
        coordinate_boundary(self.size, self.boundary)
        if not isinstance(self.source_id, str) or not self.source_id:
            raise GeometryError("explicit mathematical source identifier required")
        seen = set()
        for u, v, sign in self.edges:
            if (type(u) is not int or type(v) is not int
                    or not 0 <= u < v < self.size
                    or type(sign) is not int or sign not in (-1, 1)
                    or (u, v) in seen):
                raise GeometryError("unique labelled edges and orientations required")
            seen.add((u, v))

    def sign(self, u, v):
        u, v = min(u, v), max(u, v)
        return next((s for x, y, s in self.edges if (x, y) == (u, v)), 0)


def zero_forcing_schedule(passport):
    """Deterministic graph-only schedule; refuse a non-forcing boundary."""
    if type(passport) is not GraphPassport:
        raise GeometryError("source graph passport required")
    colored = set(passport.boundary)
    schedule = []
    while len(colored) < passport.size:
        step = None
        for v in sorted(colored):
            unseen = [w for w in range(passport.size)
                      if w not in colored and passport.sign(v, w)]
            if len(unseen) == 1:
                step = v, unseen[0]
                break
        if step is None:
            raise GeometryError("boundary is not a zero-forcing set of this graph")
        schedule.append(step)
        colored.add(step[1])
    return tuple(schedule)


def _rational_positive_sqrt(x):
    if x <= 0:
        raise GeometryError("forced edge has zero/nonpositive squared weight")
    p, q = isqrt(x.numerator), isqrt(x.denominator)
    if p * p != x.numerator or q * q != x.denominator:
        raise GeometryError("oracle supports rational weights only")
    return Q(p, q)


def reconstruct_zero_forcing(passport, moments):
    """Reconstruct A using only its passport and observed boundary moments.

    Sufficient maximum order is 2*(n-|boundary|)+1. The returned matrix is
    replayed against *all* supplied moments. True rational models always pass;
    algebraic nonrational weights are outside this exact executable's domain.
    """
    schedule = zero_forcing_schedule(passport)
    maximum = 2 * len(schedule) + 1
    if len(moments) < maximum + 1:
        raise GeometryError("insufficient predeclared moment precision/order budget")
    original = tuple(_symmetric(x) for x in moments)
    m = len(passport.boundary)
    if any(len(x) != m for x in original) or original[0] != identity(m):
        raise GeometryError("moments do not use the declared orthonormal boundary")
    colors = list(passport.boundary)
    current = original[:maximum + 1]
    for v, w in schedule:
        i = colors.index(v)
        # Current first moments must respect all already exposed source edges.
        for p, u in enumerate(colors):
            for q, z in enumerate(colors):
                if u != z:
                    value, expected = current[1][p][q], passport.sign(u, z)
                    actual = (value > 0) - (value < 0)
                    if actual != expected:
                        raise GeometryError("observed source edge/sign contradicts passport")
        coefficients = tuple(current[1][j][i] for j in range(len(colors)))
        squared = current[2][i][i] - sum((x*x for x in coefficients), Q())
        edge = passport.sign(v, w) * _rational_positive_sqrt(squared)
        enlarged = []
        for k in range(len(current) - 2):
            cross = tuple((current[k+1][i][u] - sum(
                (coefficients[j] * current[k][j][u] for j in range(len(colors))), Q()))
                / edge for u in range(len(colors)))
            corner = (current[k+2][i][i] - 2 * sum(
                (coefficients[j] * current[k+1][j][i] for j in range(len(colors))), Q())
                + sum((coefficients[j] * coefficients[l] * current[k][j][l]
                       for j in range(len(colors)) for l in range(len(colors))), Q())) / squared
            enlarged.append(tuple(tuple(row) + (cross[j],)
                                  for j, row in enumerate(current[k])) + (cross + (corner,),))
        colors.append(w)
        current = tuple(enlarged)
        if current[0] != identity(len(colors)):
            raise GeometryError("derived source coordinates are not orthonormal")
    lookup = {v: i for i, v in enumerate(colors)}
    out = tuple(tuple(current[1][lookup[u]][lookup[v]] for v in range(passport.size))
                for u in range(passport.size))
    for u in range(passport.size):
        for v in range(u + 1, passport.size):
            value = out[u][v]
            if (value > 0) - (value < 0) != passport.sign(u, v):
                raise GeometryError("reconstructed graph/sign differs from passport")
    b = coordinate_boundary(passport.size, passport.boundary)
    if boundary_moments(out, b, len(original)-1) != original:
        raise GeometryError("reconstruction fails original boundary-history replay")
    return out
