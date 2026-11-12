"""Exact observer ladder: tetrahedral coherence and the Hilbert-completion gate.

No n=5 numerology: this is a *fifth rule* on the same path carrier.
The positive-type kernel on the triangle loop group Z has a canonical
Hilbert realization by the Moore-Aronszajn/GNS construction. Exact finite
witnesses here do NOT certify infinite source-specific BBP estimates.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Mapping, Sequence

from .arity_four_bridge import (GaussQ, Omega3, OMEGA_POWERS, matrix,
                                Matrix2)


Edge = tuple[int, int]


def oriented_edge(edges: Mapping[Edge, Fraction | int], i: int, j: int) -> Fraction:
    """An antisymmetric 1-cochain on a simple graph, stored at i<j."""
    if i == j:
        return Fraction(0)
    lo, hi = min(i, j), max(i, j)
    result = Fraction(edges[lo, hi])
    return result if i < j else -result


def triangle_curvature(edges: Mapping[Edge, Fraction | int], i: int, j: int, k: int) -> Fraction:
    """Cochain curvature da(i,j,k) = a_ij + a_jk + a_ki."""
    if len({i, j, k}) != 3:
        raise ValueError("triangle vertices must be distinct")
    return (oriented_edge(edges, i, j) + oriented_edge(edges, j, k)
            + oriented_edge(edges, k, i))


def tetrahedron_boundary(edges: Mapping[Edge, Fraction | int], a: int, b: int,
                         c: int, d: int) -> Fraction:
    """d(da) on tetrahedron: F_bcd - F_acd + F_abd - F_abc = 0."""
    if len({a, b, c, d}) != 4:
        raise ValueError("tetrahedron vertices must be distinct")
    return (triangle_curvature(edges, b, c, d)
            - triangle_curvature(edges, a, c, d)
            + triangle_curvature(edges, a, b, d)
            - triangle_curvature(edges, a, b, c))


def transform_edges(edges: Mapping[Edge, Fraction | int],
                    vertex_gauge: Mapping[int, Fraction | int]) -> dict[Edge, Fraction]:
    """Gauge coboundary: a_ij -> a_ij + g_j - g_i."""
    return {key: Fraction(value) + Fraction(vertex_gauge[key[1]])
            - Fraction(vertex_gauge[key[0]]) for key, value in edges.items()}


def cycle_character(k: int) -> Omega3:
    """One triangle-loop representation chi(k)=omega^k of pi_1(C3)=Z."""
    if type(k) is not int:
        raise TypeError("integer loop index required")
    return OMEGA_POWERS[k % 3]


def boost_loop(k: int) -> Matrix2:
    """A^k in SL(2,Q), A=diag(2,1/2); same Z source, Lorentz on Herm(2)."""
    if type(k) is not int:
        raise TypeError("integer loop index required")
    return matrix(Fraction(2)**k, 0, 0, Fraction(2)**(-k))


def cubic_loop_kernel(indices: Sequence[int], rho: Fraction | int = Fraction(1, 2)) -> tuple[tuple[Omega3, ...], ...]:
    """K(m,n)=rho^|n-m| omega^(n-m). Strict PD for |rho|<1,
    with positive complex embedding omega=e^(2pi*i/3)."""
    if any(type(i) is not int for i in indices):
        raise TypeError("loop labels must be integers")
    rho = Fraction(rho)
    return tuple(tuple(Omega3(rho**abs(j-i)) * cycle_character(j-i)
                       for j in indices) for i in indices)


def _quarter_character(k: int) -> GaussQ:
    """Exact i^k for k integral (oscillator phase), including negatives."""
    return (GaussQ(1), GaussQ(0, 1), GaussQ(-1), GaussQ(0, -1))[k % 4]


def loop_kernel(indices: Sequence[int], rho: Fraction | int = Fraction(1, 2),
                quarter_turn: int = 0) -> tuple[tuple[GaussQ, ...], ...]:
    """K(m,n)=rho^|n-m| i^(quarter_turn*(n-m)), a positive-type Z kernel
    for |rho|<=1. For 0<|rho|<1 all distinct-index finite Gram matrices
    have full rank, so the canonical Hilbert realization is infinite-dimensional.
    Larger |rho| values are permitted deliberately as hostile controls.
    """
    if any(type(i) is not int for i in indices):
        raise TypeError("loop labels must be integers")
    if type(quarter_turn) is not int:
        raise TypeError("quarter_turn must be an integer")
    rho = Fraction(rho)
    return tuple(tuple(GaussQ(rho ** abs(j - i))
                       * _quarter_character(quarter_turn * (j - i))
                       for j in indices) for i in indices)


def ar1_factorization(n: int, rho: Fraction | int) -> tuple[tuple[tuple[Fraction, ...], ...], tuple[Fraction, ...]]:
    """Exact B,D with K_ij=rho^|i-j| = (B D B^T)_ij,
    B_ij=rho^(i-j) for j<=i; D=diag(1,1-rho²,...).
    """
    if type(n) is not int or n < 1:
        raise ValueError("n must be positive integer")
    rho = Fraction(rho)
    b = tuple(tuple(rho ** (i-j) if j <= i else Fraction(0)
                    for j in range(n)) for i in range(n))
    diagonal = (Fraction(1),) + (Fraction(1) - rho*rho,) * (n - 1)
    return b, diagonal


def rational_determinant(a: Sequence[Sequence[Fraction | int]]) -> Fraction:
    """Exact Fraction determinant by Gaussian elimination, not floating point."""
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("square matrix required")
    matrix = [[Fraction(x) for x in row] for row in a]
    determinant = Fraction(1)
    for c in range(n):
        pivot = next((r for r in range(c, n) if matrix[r][c]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != c:
            matrix[c], matrix[pivot] = matrix[pivot], matrix[c]
            determinant = -determinant
        diag = matrix[c][c]
        determinant *= diag
        for r in range(c + 1, n):
            multiplier = matrix[r][c] / diag
            for j in range(c + 1, n):
                matrix[r][j] -= multiplier * matrix[c][j]
            matrix[r][c] = Fraction(0)
    return determinant


def exact_phase_cocycle(phases: Sequence[Fraction | int]) -> tuple[tuple[Fraction, ...], ...]:
    """Exact *exponents* of K_ij=e(phase_i-phase_j), NOT complex numbers.
    This records the source-blind rank-one Gram law without numerical roots.
    """
    x = [Fraction(t) % 1 for t in phases]
    return tuple(tuple((a - b) % 1 for b in x) for a in x)


def squared_norm(v: Sequence[Fraction | int], kind: str = "l2") -> Fraction:
    """Finite exact candidate norm-square; l1 supplies a hostile control."""
    coords = [Fraction(t) for t in v]
    if kind == "l2":
        return sum((t*t for t in coords), Fraction())
    if kind == "l1":
        return sum((abs(t) for t in coords), Fraction()) ** 2
    raise ValueError("kind must be l1 or l2")


def parallelogram_defect(v: Sequence[Fraction | int], w: Sequence[Fraction | int],
                         kind: str = "l2") -> Fraction:
    """0 iff selected pair satisfies Jordan-von Neumann parallelogram law."""
    if len(v) != len(w):
        raise ValueError("vector sizes differ")
    plus = [Fraction(a)+Fraction(b) for a,b in zip(v,w)]
    minus = [Fraction(a)-Fraction(b) for a,b in zip(v,w)]
    return (squared_norm(plus,kind)+squared_norm(minus,kind)
            - 2*(squared_norm(v,kind)+squared_norm(w,kind)))
