"""Exact lattice data for rational sections of the exterior source lattice.

Paper proof: research/2026-10-21/VIII_SECTION_LATTICES_AND_SIMPLEX_LAWS.md.
These immutable arithmetic records are not proof-authority objects. In
particular a box enclosure is not a lower bound for a simplex section.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd, prod

from sympy import Matrix, eye
from sympy.matrices.normalforms import hermite_normal_form


class SectionGeometryError(ValueError):
    pass


def _integer(value, name, minimum=None):
    if type(value) is not int or (minimum is not None and value < minimum):
        raise SectionGeometryError(f"{name} must be an integer >= {minimum}")
    return value


def _matrix(rows):
    rows = tuple(tuple(row) for row in rows)
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise SectionGeometryError("a nonempty rectangular matrix is required")
    for row in rows:
        for entry in row:
            _integer(entry, "matrix entry")
    return Matrix(rows)


def _freeze(mat):
    return tuple(tuple(int(mat[i, j]) for j in range(mat.cols))
                 for i in range(mat.rows))


def _bezout(a, b):
    """Return nonnegative g and s,t with sa+tb=g, without numerical arithmetic."""
    old_r, r, old_s, s, old_t, t = abs(a), abs(b), 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s * (1 if a >= 0 else -1), old_t * (1 if b >= 0 else -1)


def _one_congruence_kernel(row, modulus):
    """Basis of {z: row*z=0 mod modulus}, using unimodular Bezout steps."""
    rank = len(row)
    transform = eye(rank)
    reduced = list(row)
    for j in range(1, rank):
        a, b = reduced[0], reduced[j]
        g, s, t = _bezout(a, b)
        if g == 0:
            continue
        step = eye(rank)
        step[0, 0], step[j, 0] = s, t
        step[0, j], step[j, j] = -b // g, a // g
        transform = transform * step
        reduced[0], reduced[j] = g, 0
    index = modulus // gcd(modulus, reduced[0])
    transform[:, 0] = index * transform[:, 0]
    return transform, index


@dataclass(frozen=True)
class SectionLattice:
    saturated_basis: tuple
    divisor_moduli: tuple
    sum_modulus: int
    coordinate_kernel: tuple
    lattice_basis: tuple
    section_index: int
    ambient_index: int
    covolume_squared: int
    projection_rows: tuple
    projection_hnf: tuple
    projection_index: int

    @property
    def rank(self):
        return len(self.coordinate_kernel)


def section_lattice(basis, divisor_moduli, sum_modulus):
    """Construct Lambda intersect V from a *saturated* integer basis of V.

    Saturation is checked by gcd of maximal minors = 1. The congruence kernel
    is constructed by Bezout transformations. HNF is used only for a coordinate
    projection and its change of basis is rechecked to be integral unimodular.
    Rank zero is intentionally outside this API (its positive source is empty).
    """
    B = _matrix(basis)
    m, r = B.shape
    if r > m:
        raise SectionGeometryError("basis has more columns than rows")
    ds = tuple(divisor_moduli)
    if len(ds) != m:
        raise SectionGeometryError("one divisor modulus per ambient coordinate")
    for d in ds:
        _integer(d, "divisor modulus", 1)
    q = _integer(sum_modulus, "sum modulus", 1)
    minor_gcd, projection = 0, None
    for rows in combinations(range(m), r):
        minor = int(B.extract(rows, range(r)).det())
        minor_gcd = gcd(minor_gcd, minor)
        if minor and projection is None:
            projection = rows
    if minor_gcd != 1:
        raise SectionGeometryError("basis must have full rank and be saturated (minor gcd 1)")

    K, index = eye(r), 1
    constraints = [(B[i, :], ds[i]) for i in range(m)]
    constraints.append((Matrix([[sum(B[i, j] for i in range(m)) for j in range(r)]]), q))
    for row, modulus in constraints:
        pulled = row * K
        step, factor = _one_congruence_kernel([int(v) for v in pulled], modulus)
        K = K * step
        index *= factor
    C = B * K
    if abs(int(K.det())) != index:
        raise ArithmeticError("congruence kernel determinant disagrees with index")
    for row, modulus in constraints:
        if any(int(v) % modulus for v in row * K):
            raise ArithmeticError("constructed basis violates a congruence")
    projected = C.extract(projection, range(r))
    H = hermite_normal_form(projected)
    change = projected.inv() * H
    if any(not value.is_Integer for value in change) or abs(change.det()) != 1:
        raise ArithmeticError("HNF did not preserve the projected lattice")
    covolume_squared = int((C.T * C).det())
    if covolume_squared != index ** 2 * int((B.T * B).det()):
        raise ArithmeticError("section covolume identity failed")
    ambient_index = prod(ds) * q // gcd(q, gcd(*ds))
    return SectionLattice(_freeze(B), ds, q, _freeze(K), _freeze(C), index,
                          ambient_index, covolume_squared, tuple(projection),
                          _freeze(H), abs(int(H.det())))


@dataclass(frozen=True)
class BoxEnclosure:
    lower: int
    upper: int
    volume_over_index: Fraction
    absolute_error: Fraction


def projected_box_enclosure(upper_triangular_basis, side_lengths):
    """Enclose any translate's count in integer intervals of these lengths.

    Applies to the *whole projected rectangle*, not to its simplex subset.
    The matrix is a column lattice basis and must be upper triangular with
    positive diagonal. No HNF reduction of off-diagonal entries is needed.
    """
    H = _matrix(upper_triangular_basis)
    r = H.rows
    lengths = tuple(side_lengths)
    if H.cols != r or len(lengths) != r:
        raise SectionGeometryError("square basis and matching side lengths required")
    for n in lengths:
        _integer(n, "side length", 0)
    if any(H[i, j] for i in range(r) for j in range(i)) or any(H[i, i] <= 0 for i in range(r)):
        raise SectionGeometryError("basis must be upper triangular with positive diagonal")
    diagonal = [int(H[i, i]) for i in range(r)]
    lower = prod(n // d for n, d in zip(lengths, diagonal))
    upper = prod((n + d - 1) // d for n, d in zip(lengths, diagonal))
    main = Fraction(prod(lengths), prod(diagonal))
    return BoxEnclosure(lower, upper, main, max(main - lower, upper - main))


def section_cell_budget(lattice_basis, center):
    """Exact beta for the simplex-section volume enclosure in the paper.

    The rational center z must belong to the column space, have positive
    coordinates, and sum(z)<1. The supplied basis describes the actual lattice;
    this function alone makes no assertion that it is a saturated section.
    """
    C = _matrix(lattice_basis)
    zs = tuple(center)
    if len(zs) != C.rows or any(type(z) not in (int, Fraction) for z in zs):
        raise SectionGeometryError("center must be an exact rational ambient vector")
    zs = tuple(Fraction(z) for z in zs)
    if any(z <= 0 for z in zs) or sum(zs) >= 1:
        raise SectionGeometryError("center must be positive with sum below one")
    Z = Matrix(zs)
    if C.rank() != C.cols or C.row_join(Z).rank() != C.cols:
        raise SectionGeometryError("full-column-rank basis and center in its span required")
    coordinate_radii = [Fraction(sum(abs(int(C[i, j])) for j in range(C.cols)), 2)
                        for i in range(C.rows)]
    sum_radius = Fraction(sum(abs(sum(int(C[i, j]) for i in range(C.rows)))
                              for j in range(C.cols)), 2)
    return max([radius / z for radius, z in zip(coordinate_radii, zs)]
               + [sum_radius / (1 - sum(zs))])


def section_volume_factors(rank, cutoff, beta):
    """Return ((X-beta)_+^r,(X+beta)^r); multiply by vol(K_1)/covol."""
    _integer(rank, "rank", 1)
    if type(cutoff) not in (int, Fraction) or type(beta) not in (int, Fraction):
        raise SectionGeometryError("exact rational cutoff and cell budget required")
    X, b = Fraction(cutoff), Fraction(beta)
    if X < 0 or b <= 0:
        raise SectionGeometryError("cutoff must be nonnegative and beta positive")
    return max(Fraction(0), X - b) ** rank, (X + b) ** rank
