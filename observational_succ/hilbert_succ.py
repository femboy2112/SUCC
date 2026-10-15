"""Hilbert-curve SUCC: exact dyadic space filling, source-typed Weil kernel scanning.

A Hilbert scan is an ORDERING/MEASUREMENT of a 2D kernel, never a new
positive operator, a physical omega-computation, or a proof of RH.

Reference parent: Phoenix-II main 03db44203147a7b28d445bb9f970fa71360e78c4.
Authentic Suzuki source pinned by original Git blob hash (PR #85).
The mathematical proof contract is research/2026-10-14/HILBERT_SUCC_SOURCE_STRATA.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha1
from math import comb
from pathlib import Path
from typing import Callable, Iterator


class HilbertSourceError(ValueError):
    """A dyadic/source/measure-type proof obligation was not met."""


PINNED_WEIL_BLOB = "0cc8510b71d178fc79e8d410a86d8b6014cf9178"
PARENT_MAIN_SHA = "03db44203147a7b28d445bb9f970fa71360e78c4"
ORIGINAL_WEIL_SOURCE = "AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3"


def rational(x):
    if type(x) not in (int, Q):
        raise HilbertSourceError("exact integer/Fraction required; no bool/float laundering")
    return Q(x)


def _level(level, maxlevel=8):
    if type(level) is not int or not 0 <= level <= maxlevel:
        raise HilbertSourceError("Hilbert level outside declared finite budget")
    return level


def _rotate(side, x, y, rx, ry):
    if ry == 0:
        if rx == 1:
            x, y = side - 1 - x, side - 1 - y
        x, y = y, x
    return x, y


def hilbert_index_xy(level: int, index: int) -> tuple[int, int]:
    """Canonical quadrant-recursive Hilbert index, 4**level dyadic tiles."""
    level = _level(level)
    side = 1 << level
    if type(index) is not int or not 0 <= index < side * side:
        raise HilbertSourceError("Hilbert index outside this source resolution")
    x = y = 0
    remaining = index
    scale = 1
    while scale < side:
        rx = 1 & (remaining // 2)
        ry = 1 & (remaining ^ rx)
        x, y = _rotate(scale, x, y, rx, ry)
        x += scale * rx
        y += scale * ry
        remaining //= 4
        scale *= 2
    return x, y


def hilbert_xy_index(level: int, x: int, y: int) -> int:
    level = _level(level)
    side = 1 << level
    if any(type(t) is not int or not 0 <= t < side for t in (x, y)):
        raise HilbertSourceError("coordinate outside Hilbert square")
    d = 0
    scale = side // 2
    while scale:
        rx = int(bool(x & scale))
        ry = int(bool(y & scale))
        d += scale * scale * ((3 * rx) ^ ry)
        x, y = _rotate(scale, x, y, rx, ry)
        scale //= 2
    return d


@dataclass(frozen=True)
class HilbertCell:
    level: int
    index: int
    x: int
    y: int
    clock_midpoint: Q
    spatial_midpoint: tuple[Q, Q]


def hilbert_cell(level: int, index: int) -> HilbertCell:
    x, y = hilbert_index_xy(level, index)
    n = 1 << level
    return HilbertCell(level, index, x, y, Q(2 * index + 1, 2 * n * n),
                       (Q(2 * x + 1, 2 * n), Q(2 * y + 1, 2 * n)))


def hilbert_cells(level: int) -> Iterator[HilbertCell]:
    level = _level(level, maxlevel=7)
    for d in range(1 << (2 * level)):
        yield hilbert_cell(level, d)


def hilbert_parent(level: int, index: int) -> tuple[int, int]:
    if _level(level) == 0:
        raise HilbertSourceError("level-zero root has no predecessor")
    hilbert_index_xy(level, index)
    return level - 1, index // 4


def hilbert_parent_consistency(level: int) -> bool:
    if _level(level, maxlevel=6) == 0:
        raise HilbertSourceError("parent consistency needs positive level")
    return all((x // 2, y // 2) == hilbert_index_xy(level - 1, d // 4)
               for d in range(1 << (2 * level))
               for (x, y) in (hilbert_index_xy(level, d),))


def hilbert_adjacency_receipt(level: int) -> dict:
    level = _level(level, maxlevel=6)
    n = 1 << level
    prev = None
    seen = set()
    bad = []
    max_taxicab = 0
    for cell in hilbert_cells(level):
        point = (cell.x, cell.y)
        if point in seen:
            bad.append(("duplicate", cell.index))
        seen.add(point)
        if prev is not None:
            step = abs(prev[0] - point[0]) + abs(prev[1] - point[1])
            max_taxicab = max(step, max_taxicab)
            if step != 1:
                bad.append(("nonadjacent", cell.index))
        prev = point
    return {"level": level, "source_cells": n * n, "distinct": len(seen),
            "max_taxicab_step": max_taxicab, "nonlawful_transitions": tuple(bad),
            "parent_consistency": hilbert_parent_consistency(level) if level else True,
            "actual_infinity_completed": False}


def interval_clock_vector(level: int, values: tuple) -> tuple[Q, ...]:
    level = _level(level, maxlevel=6)
    if type(values) is not tuple or len(values) != 1 << (2 * level):
        raise HilbertSourceError("exact declared Hilbert clock dimension required")
    return tuple(rational(v) for v in values)


def spatial_chart_to_clock(level: int, spatial_rows: tuple) -> tuple[Q, ...]:
    level = _level(level, maxlevel=6)
    n = 1 << level
    if type(spatial_rows) is not tuple or len(spatial_rows) != n or any(
        type(row) is not tuple or len(row) != n for row in spatial_rows
    ):
        raise HilbertSourceError("complete rectangular source law required")
    return tuple(rational(spatial_rows[xy[0]][xy[1]])
                 for d in range(n * n) for xy in (hilbert_index_xy(level, d),))


def clock_to_spatial_chart(level: int, values: tuple) -> tuple[tuple[Q, ...], ...]:
    values = interval_clock_vector(level, values)
    n = 1 << level
    rows = [[Q() for _ in range(n)] for _ in range(n)]
    for d, value in enumerate(values):
        x, y = hilbert_index_xy(level, d)
        rows[x][y] = value
    return tuple(tuple(row) for row in rows)


def hilbert_inner_product(level: int, first: tuple, second: tuple) -> Q:
    first = interval_clock_vector(level, first)
    second = interval_clock_vector(level, second)
    return sum((a * b for a, b in zip(first, second)), Q()) / len(first)


def hilbert_refinement(level: int, parent: tuple) -> tuple[Q, ...]:
    """Source-preserving isometric L2 step refinement: child cells inherit parent."""
    parent = interval_clock_vector(level, parent)
    if level >= 6:
        raise HilbertSourceError("finite refinement exceeds software budget")
    return tuple(v for value in parent for v in (value,) * 4)


def lipschitz_square_error(level: int, lipschitz_L) -> Q:
    """|integral(f)-midpoint_sum(f)| <= L/(2**(level+1)), sup metric."""
    _level(level, maxlevel=8)
    lipschitz_L = rational(lipschitz_L)
    if lipschitz_L < 0:
        raise HilbertSourceError("nonnegative proved spatial Lipschitz bound required")
    return lipschitz_L / (1 << (level + 1))


def hilbert_square_midpoint_average(level: int, evaluate: Callable[[Q, Q], Q]) -> Q:
    level = _level(level, maxlevel=6)
    if not callable(evaluate):
        raise HilbertSourceError("source function must be supplied")
    total = Q()
    for cell in hilbert_cells(level):
        total += rational(evaluate(*cell.spatial_midpoint))
    return total / (1 << (2 * level))


def monomial_square_integral(i: int, j: int) -> Q:
    if any(type(k) is not int or k < 0 or k > 30 for k in (i, j)):
        raise HilbertSourceError("nonnegative polynomial exponents in finite budget")
    return Q(1, (i + 1) * (j + 1))


def monomial_strata(i: int, j: int, shift) -> dict:
    """Three different MEASURES on the same 2D square, not one area integral.

    Bulk dx dy; diagonal delta(x-y); graph y=x-b, b in (0,1).
    This is an exact *polynomial geometric* control, NOT a prime logp.
    """
    area = monomial_square_integral(i, j)
    b = rational(shift)
    if not 0 < b < 1:
        raise HilbertSourceError("graph shift must be geometric 0<b<1")
    graph = sum((Q(comb(i, k)) * b ** (i - k) * (1 - b) ** (j + k + 1)
                 / (j + k + 1) for k in range(i + 1)), Q())
    return {"bulk_area_measure": area,
            "diagonal_contact_measure": Q(1, i + j + 1),
            "one_dimensional_shift_graph_measure": graph,
            "graph_shift": b,
            "measure_channels_distinct": True,
            "geometric_shift_is_NOT_authenticated_prime": True}


def diagonal_band_true_integral(thickness) -> Q:
    """Exact Lebesgue bulk integral for eps^-1 1_(|x-y|<eps/2), unit square."""
    eps = rational(thickness)
    if not 0 < eps <= 1:
        raise HilbertSourceError("certified band thickness 0<eps<=1")
    return 1 - eps / 4


def diagonal_band_hilbert_sample(level: int, thickness) -> Q:
    """Midpoint quadrature of a diagonal mollifier; not a delta/contact certificate."""
    level = _level(level, maxlevel=6)
    eps = rational(thickness)
    if not 0 < eps <= 1:
        raise HilbertSourceError("positive mollifier thickness required")
    n = 1 << level
    count = sum(abs(cell.x - cell.y) * Q(1, n) < eps / 2
                for cell in hilbert_cells(level))
    return Q(count, n * n) / eps


def diagonal_zeno_mutant(level: int) -> dict:
    """eps=(cell width)^2 makes grid midpoint estimate diverge vs true 1."""
    level = _level(level, maxlevel=6)
    n = 1 << level
    eps = Q(1, n * n)
    discrete = diagonal_band_hilbert_sample(level, eps)
    analytic = diagonal_band_true_integral(eps)
    assert discrete == n
    return {"level": level, "thickness": eps,
            "bulk_2d_midpoint_observer": discrete,
            "true_2d_area_integral": analytic,
            "limit_true": Q(1),
            "contact_delta_is_not_area_density": True,
            "two_limit_exchange_unjustified": True}


def hilbert_dimension_obstruction(dimension: int, holder_exponent: Q) -> dict:
    """Surjection [0,1] -> [0,1]^d cannot be alpha-Holder for alpha>1/d.

    This reports a classical covering exponent; the argument is in the dossier.
    """
    if type(dimension) is not int or dimension < 1 or dimension > 10000:
        raise HilbertSourceError("finite coordinate projection dimension required")
    exponent = rational(holder_exponent)
    if not 0 < exponent <= 1:
        raise HilbertSourceError("Hölder exponent in (0,1]")
    return {"dimension": dimension, "exponent": exponent,
            "covering_volume_power": 1 - dimension * exponent,
            "surjective_holder_map_refuted": exponent * dimension > 1,
            "dimension_free_positive_holder_for_hilbert_cube": False}


def _pinned_original_weil_source():
    """Import EXACT integrated original g_J; refuse drift, not a source forgery proof."""
    try:
        from . import source_weil_hierarchy as source
    except ImportError as exc:
        raise HilbertSourceError("original Suzuki source module not mounted") from exc
    raw = Path(source.__file__).read_bytes()
    blob = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    if blob != PINNED_WEIL_BLOB:
        raise HilbertSourceError("original signed Suzuki source has drifted")
    source.assert_original_source_tape()
    return source


@dataclass(frozen=True)
class SourceHilbertScan:
    level: int
    a: Q
    J: int
    spatial_N: int
    hilbert_matrix_cells: tuple[tuple[int, int, Q], ...]
    source_operator_norm_error: Q
    pointwise_interval_radius: Q
    source: str = ORIGINAL_WEIL_SOURCE
    signed_kernel: bool = True
    source_blob: str = PINNED_WEIL_BLOB
    rh_proved: bool = False


def genuine_suzuki_hilbert_scan(a, J: int, level: int) -> SourceHilbertScan:
    """Authentic original g_J matrix in Hilbert ORDER, not redefined from a toy.

    Already-existing full source norm error is reused and NOT improved by reordering.
    """
    a = rational(a)
    level = _level(level, maxlevel=4)
    if level == 0 or type(J) is not int or not 1 <= J <= 36 or not 0 < a <= 1:
        raise HilbertSourceError("bounded authenticated Suzuki source stage")
    n = 1 << level
    src = _pinned_original_weil_source()
    stage = src.stage(a, J, n)
    src._authenticated(stage)
    data = tuple((cell.x, cell.y, stage.center[cell.x][cell.y])
                 for cell in hilbert_cells(level))
    return SourceHilbertScan(level, a, J, n, data, stage.norm_error,
                             stage.kernel_entry_radius)


def _authenticated_scan(scan: SourceHilbertScan):
    if type(scan) is not SourceHilbertScan or scan.source != ORIGINAL_WEIL_SOURCE or \
       scan.signed_kernel is not True or scan.rh_proved is not False or \
       scan.source_blob != PINNED_WEIL_BLOB or type(scan.a) is not Q or \
       type(scan.level) is not int or type(scan.J) is not int or \
       type(scan.spatial_N) is not int or \
       type(scan.hilbert_matrix_cells) is not tuple or \
       type(scan.source_operator_norm_error) is not Q or \
       type(scan.pointwise_interval_radius) is not Q:
        raise HilbertSourceError("incorrect source stamp, domain or proof status")
    exact = genuine_suzuki_hilbert_scan(scan.a, scan.J, scan.level)
    if scan != exact:
        raise HilbertSourceError("stale, forged or permuted signed original source")
    return scan


def source_rayleigh_by_hilbert_succ(scan: SourceHilbertScan, vector: tuple) -> Q:
    """Exact Rayleigh quotient on source-authenticated mean-zero cell space."""
    _authenticated_scan(scan)
    if type(vector) is not tuple or len(vector) != scan.spatial_N:
        raise HilbertSourceError("source mean-zero cell vector dimensions")
    v = tuple(rational(x) for x in vector)
    if sum(v, Q()) != 0 or all(x == 0 for x in v):
        raise HilbertSourceError("original H=L²_0 requires nonzero mean-zero test")
    energy = sum((v[x] * value * v[y]
                  for x, y, value in scan.hilbert_matrix_cells), Q())
    return energy / sum((x * x for x in v), Q())


def source_locality_budget(scan: SourceHilbertScan) -> Q:
    """Bound adjacent Hilbert observations of original signed normalized M.

    Exact |M_d-M_(d+1)| <= h*(L_J*h + 2*eta), not a positivity bound.
    """
    _authenticated_scan(scan)
    src = _pinned_original_weil_source()
    h = Q(2) * scan.a / scan.spatial_N
    return h * (src.lipschitz_safe(scan.a, scan.J) * h +
                2 * scan.pointwise_interval_radius)


def source_scan_locality_check(scan: SourceHilbertScan) -> dict:
    _authenticated_scan(scan)
    budget = source_locality_budget(scan)
    differences = tuple(abs(left[2] - right[2]) for left, right in
                        zip(scan.hilbert_matrix_cells, scan.hilbert_matrix_cells[1:]))
    return {"all_consecutive_original_source_readouts_lipschitz_certified":
            all(d <= budget for d in differences),
            "declared_bound": budget,
            "maximum_exact_difference": max(differences, default=Q()),
            "number_of_readouts": scan.spatial_N ** 2,
            "whole_Weil_PSD_proved": False}


def source_certified_rayleigh_interval(scan: SourceHilbertScan,
                                       vector: tuple) -> tuple[Q, Q]:
    """Bound TRUE infinite signed G_a Rayleigh from source stage. Negative is real only if upper<0."""
    midpoint = source_rayleigh_by_hilbert_succ(scan, vector)
    return midpoint - scan.source_operator_norm_error, midpoint + scan.source_operator_norm_error



def original_weil_measure_strata(a) -> dict:
    """Real original Weil components by measure dimension, with source intervals.

    For real v in C_c^infty(-a,a):
       Q = E_G - C_G||v||²
           -2 sum_(p^k<e^(2a)) w_n Re< T_logn v, v >
           +2|<v,cosh(x/2)>|² -2|<v,sinh(x/2)>|².
    Here E_G is the authentic singular-but-renormalized 2D positive jump
    energy. Delta/contact and shift graphs are ONE-dimensional measures,
    NOT 2D Lebesgue densities. Pole rank-two terms are 2D separable.
    All analytic identities imported from the completed Weil/PR86 source.
    """
    a = rational(a)
    if not 0 < a <= 1:
        raise HilbertSourceError("original Weil strata calibrated for 0<a<=1")
    src = _pinned_original_weil_source()
    nodes=[]
    for n,p in src.AUTHENTIC_TAPE:
        ln=src.log_iv(n)
        if ln.hi < 2*a:
            w=src.log_iv(p)*src.sqrt_inverse(n)
            nodes.append({"n":n,"primitive_prime":p,
                          "shift_log_n_interval":(ln.lo,ln.hi),
                          "positive_half_density_weight_interval":(w.lo,w.hi),
                          "signed_correlation_coefficient":-2,
                          "measure":"graph_x_minus_y_equals_log_n",
                          "measure_dimension":1})
        elif ln.lo <= 2*a <= ln.hi:
            raise HilbertSourceError("unresolved true-prime activation at source boundary")
    c=src.contact_iv()
    return {"source":ORIGINAL_WEIL_SOURCE,
            "source_blob":PINNED_WEIL_BLOB,
            "a":a,
            "gamma_positive_bulk":{
                "dimension":2,"signed":False,
                "source":"one_real_Gamma_Carleman_jump_energy",
                "kernel_needs_diagonal_cancellation":True},
            "contact_diagonal":{
                "dimension":1,"signed":True,
                "coefficient_interval":(-c.hi,-c.lo),
                "source":"completed_archimedean_contact_not_area_density"},
            "prime_shift_graphs":tuple(nodes),
            "pole_even":{
                "dimension":2,"rank":1,"coefficient":2,
                "source":"original_completed_pole_cosh"},
            "pole_odd":{
                "dimension":2,"rank":1,"coefficient":-2,
                "source":"original_completed_pole_sinh"},
            "all_signed_channels_preserved":True,
            "original_RH_positivity_proved":False}



def source_hilbert_hilbert_schmidt_identity(scan: SourceHilbertScan) -> dict:
    """EXACT finite HS identity for original signed matrix M, not a PSD claim.

    Summing all entries of M^2 equals (2a)^2 times the 1D Hilbert-clock
    mean-square of the corresponding kernel g_J mids (M=h*g_J).
    The construction Hilbertizes a KERNEL as an L2 signal; it does not
    conjugate the source signed OPERATOR to a multiplication operator.
    """
    _authenticated_scan(scan)
    h = 2 * scan.a / scan.spatial_N
    lhs = sum((value * value for x, y, value in scan.hilbert_matrix_cells), Q())
    rhs = (2 * scan.a)**2 * sum(
        ((value / h)**2 for x, y, value in scan.hilbert_matrix_cells), Q()
    ) / len(scan.hilbert_matrix_cells)
    if lhs != rhs:
        raise HilbertSourceError("L2 Hilbert-clock / original HS matrix mismatch")
    return {"signed_matrix_HS_norm_squared": lhs,
            "hilbert_clock_energy_scaled": rhs,
            "exact_L2_source_identity":True,
            "Hilbert_flattening_does_not_imply_PSD":True}
