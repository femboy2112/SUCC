"""Hilbert-curve / Hilbert-cube Zeno certificates for Observational SUCC.

Mathematical-source exactness only: no physical probe is executed by this module.
No zero-location oracle, Gamma replacement, or assertion of Weil positivity.

Classical Hilbert's 2D recursive curve, a compact weighted Hilbert cube and
quadratic-form approximation are assembled with an exact source/cost interface.
The proofs and missing RH-specific arrows are in HILBERT_ZENO_COMPLETION.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from typing import Iterator


class HilbertZenoError(ValueError):
    """Source, mathematical contract or explicit finite resource gate failure."""


def exact(x: F | int) -> F:
    if type(x) is int or isinstance(x, F):
        return F(x)
    raise HilbertZenoError("EXACT_RATIONAL_REQUIRED: floats and bools are not source certificates")


def _stage(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise HilbertZenoError("finite successor stage must be an integer in the declared domain")
    return n


@dataclass(frozen=True)
class SourceKey:
    source_id: str
    epoch: int
    basis: str
    domain: str

    def __post_init__(self) -> None:
        if any(not isinstance(s, str) or not s.strip()
               for s in (self.source_id, self.basis, self.domain)):
            raise HilbertZenoError("source, basis and mathematical domain must be named")
        _stage(self.epoch)

    def check(self, other: "SourceKey") -> None:
        if type(other) is not SourceKey or self != other:
            raise HilbertZenoError("SOURCE_EPOCH_BASIS_DOMAIN_MISMATCH")

    @classmethod
    def from_zeno_stamp(cls, stamp: object) -> "SourceKey":
        """Explicit source-key adapter; conversion is not a physical calibration."""
        return cls(stamp.source_id, stamp.epoch, stamp.basis, stamp.domain)


def hilbert_xy(level: int, index: int) -> tuple[int, int]:
    """One exact cell in the depth-level 2D Hilbert traversal; O(level) work.

    The four self-similar blocks are (y,x), (x,y+m), (x+m,y+m),
    (2m-1-y,m-1-x) applied to the previous stage.  These isometries have
    connecting endpoints; the cell walk is a Hamiltonian grid path.
    """
    _stage(level)
    _stage(index)
    if index >= 4**level:
        raise HilbertZenoError("Hilbert index outside current finite-grid carrier")
    if level == 0:
        return (0, 0)
    m = 1 << (level - 1)
    block = 4**(level - 1)
    quadrant, rest = divmod(index, block)
    x, y = hilbert_xy(level - 1, rest)
    if quadrant == 0:
        return y, x
    if quadrant == 1:
        return x, y + m
    if quadrant == 2:
        return x + m, y + m
    return 2*m - 1 - y, m - 1 - x


def hilbert_index(level: int, x: int, y: int) -> int:
    """Inverse to hilbert_xy on the finite 2^level by 2^level grid."""
    _stage(level)
    _stage(x)
    _stage(y)
    side = 1 << level
    if x >= side or y >= side:
        raise HilbertZenoError("cell not in source Hilbert grid")
    if level == 0:
        return 0
    m = side // 2
    if x < m and y < m:
        quad, u, v = 0, y, x
    elif x < m:
        quad, u, v = 1, x, y-m
    elif y >= m:
        quad, u, v = 2, x-m, y-m
    else:
        quad, u, v = 3, m-1-y, 2*m-1-x
    return quad*4**(level-1) + hilbert_index(level-1, u, v)


def hilbert_cells(level: int) -> Iterator[tuple[int, int]]:
    """Pure mathematical enumeration; not an executed physical space-filling event."""
    _stage(level)
    for k in range(4**level):
        yield hilbert_xy(level, k)


def cell_center(level: int, x: int, y: int) -> tuple[F, F]:
    _stage(level)
    side = 1 << level
    if type(x) is not int or type(y) is not int or not (0 <= x < side and 0 <= y < side):
        raise HilbertZenoError("cell coordinates outside mathematical observation window")
    return F(2*x+1, 2*side), F(2*y+1, 2*side)



@dataclass(frozen=True)
class HilbertPrefixCertificate:
    """One source-qualified finite address denotes a WHOLE dyadic cell of
    possible mathematical completions, never one performed omega-event.
    """
    stamp: SourceKey
    digits: tuple[int, ...]
    level: int
    hilbert_index: int
    cell: tuple[int, int]
    lower_left: tuple[F, F]
    upper_right: tuple[F, F]
    midpoint: tuple[F, F]
    completion_radius_inf: F
    physical_completion_executed: bool = False


def hilbert_prefix(stamp: SourceKey, digits: tuple[int, ...]) -> HilbertPrefixCertificate:
    """A base-4 prefix resolves a nested cell with a Zeno tail 2^(-n-1).

    Four children of source Hilbert cell index i have indices 4*i..4*i+3
    at the next level. Therefore any infinite digit extension lies in the
    SAME coarse cell, and its limit point is within completion_radius_inf
    of the reported midpoint.
    """
    if type(stamp) is not SourceKey or type(digits) is not tuple:
        raise HilbertZenoError("source-qualified immutable base-4 address required")
    index=0
    for digit in digits:
        if type(digit) is not int or not 0 <= digit <= 3:
            raise HilbertZenoError("Hilbert address must consist of exact base-4 digits")
        index=4*index+digit
    level=len(digits)
    xy=hilbert_xy(level,index)
    N=1 << level
    lower=(F(xy[0],N),F(xy[1],N))
    upper=(F(xy[0]+1,N),F(xy[1]+1,N))
    return HilbertPrefixCertificate(stamp,digits,level,index,xy,
                                    lower,upper,cell_center(level,*xy),F(1,2*N))


def hilbert_refinement_children(level: int, x: int, y: int) -> tuple[int,int,int,int]:
    """Exact parent-child index block. A level-n cell i refines to the
    consecutive level-(n+1) Hilbert indices (4i,4i+1,4i+2,4i+3).
    """
    _stage(level)
    parent_index=hilbert_index(level,x,y)
    addresses=tuple(sorted(hilbert_index(level+1,2*x+u,2*y+v)
                           for u in (0,1) for v in (0,1)))
    if addresses != tuple(4*parent_index+j for j in range(4)):
        raise AssertionError("source Hilbert recursion violated the refinement law")
    return addresses


def optimal_open_path_length(level: int) -> F:
    """Exact ℓ1 grid-center length: (4^level-1)/2^level, optimal for any tour."""
    _stage(level)
    return F(4**level-1, 2**level)


@dataclass(frozen=True)
class RationalPolynomial2:
    """Complete exact coefficient law f(x,y)=sum c_ij x^i y^j on [0,1]^2.

    The mathematics is conditional on this supplied polynomial being the
    actual source target. No finite samples authenticate that source law.
    """
    stamp: SourceKey
    terms: tuple[tuple[int, int, F], ...]

    def __post_init__(self) -> None:
        if type(self.stamp) is not SourceKey or type(self.terms) is not tuple or not self.terms:
            raise HilbertZenoError("named source and immutable nonempty polynomial required")
        used: set[tuple[int, int]] = set()
        for row in self.terms:
            if type(row) is not tuple or len(row) != 3:
                raise HilbertZenoError("polynomial law requires immutable coefficient triples")
            i, j, c = row
            _stage(i)
            _stage(j)
            exact(c)
            if (i, j) in used:
                raise HilbertZenoError("duplicate polynomial monomial; normalize first")
            used.add((i, j))

    def at(self, x: F, y: F) -> F:
        x, y = exact(x), exact(y)
        if not (0 <= x <= 1 and 0 <= y <= 1):
            raise HilbertZenoError("target evaluation outside source domain [0,1]^2")
        return sum((exact(c)*x**i*y**j for i, j, c in self.terms), F(0))

    def gradient_l1_bound(self, upper_x: F = F(1), upper_y: F = F(1)) -> F:
        """Rigorous |f(x)-f(y)| <= L ||x-y||_1 in the stated positive box.

        Bound the coordinate partial derivatives by the absolute polynomial
        coefficients at the upper right; no unproved sampling-fit Lipschitz L.
        """
        upper_x, upper_y = exact(upper_x), exact(upper_y)
        if not (0 <= upper_x <= 1 and 0 <= upper_y <= 1):
            raise HilbertZenoError("derivative enclosure outside nonnegative unit box")
        dx = sum((abs(exact(c))*i*upper_x**(i-1)*upper_y**j
                  for i, j, c in self.terms if i), F(0))
        dy = sum((abs(exact(c))*j*upper_x**i*upper_y**(j-1)
                  for i, j, c in self.terms if j), F(0))
        return max(dx, dy)


@dataclass(frozen=True)
class SquareProof:
    stamp: SourceKey
    level: int
    samples: int
    lowest: F
    highest: F
    global_lower: F
    global_upper: F
    minimum_witness: tuple[F, F, F]
    verdict: str
    mathematical_path_length: F
    physical_observations_performed: bool = False
    source_physically_authenticated: bool = False


def certify_square(poly: RationalPolynomial2, level: int, *, max_samples: int = 100000) -> SquareProof:
    """All-grid exact Lipschitz certificate for the SUPPLIED polynomial law."""
    _stage(level)
    _stage(max_samples, 1)
    count = 4**level
    if count > max_samples:
        raise HilbertZenoError("RESOURCE_BUDGET: no extrapolation from a partial Hilbert scan")
    low: F | None = None
    high: F | None = None
    argmin = (F(0), F(0), F(0))
    for ix, iy in hilbert_cells(level):
        x, y = cell_center(level, ix, iy)
        z = poly.at(x, y)
        if low is None or z < low:
            low, argmin = z, (x, y, z)
        high = z if high is None else max(high, z)
    assert low is not None and high is not None
    L = poly.gradient_l1_bound()
    # Every point lies in a cell of ℓ1 radius 1/2^level about its midpoint.
    eps = L / (2**level)
    lower, upper = low-eps, high+eps
    verdict = ("NEGATIVE_WITNESS" if low < 0 else
               "GLOBAL_NONNEGATIVE" if lower >= 0 else "UNRESOLVED")
    return SquareProof(poly.stamp, level, count, low, high, lower, upper,
                       argmin, verdict, optimal_open_path_length(level))


@dataclass(frozen=True)
class AdaptiveSquareProof:
    stamp: SourceKey
    max_depth: int
    evaluated_cells: int
    resolved_cells: int
    unresolved_cells: int
    global_lower: F | None
    negative_witness: tuple[F, F, F] | None
    verdict: str
    physical_observations_performed: bool = False


def certify_square_adaptive(poly: RationalPolynomial2, max_depth: int,
                            *, max_cells: int = 100000) -> AdaptiveSquareProof:
    """Exact dyadic quadtree: local derivative bounds discharge only lawful cells.

    Hilbert index orders children; pruning creates no extra source observation.
    Lack of a strict margin may mean no finite positive certificate appears.
    """
    _stage(max_depth)
    _stage(max_cells, 1)
    tasks = [(0, 0, 0)]
    seen = resolved = 0
    unresolved = 0
    lower: F | None = None
    witness = None
    while tasks:
        if seen == max_cells:
            raise HilbertZenoError("RESOURCE_BUDGET: unvisited source cells remain")
        lvl, ix, iy = tasks.pop()
        seen += 1
        side = 1 << lvl
        x, y = cell_center(lvl, ix, iy)
        f = poly.at(x, y)
        if f < 0:
            witness = (x, y, f)
            break
        L = poly.gradient_l1_bound(F(ix+1, side), F(iy+1, side))
        block_lower = f - L / side
        if block_lower >= 0:
            resolved += 1
            lower = block_lower if lower is None else min(lower, block_lower)
        elif lvl == max_depth:
            unresolved += 1
            lower = block_lower if lower is None else min(lower, block_lower)
        else:
            children = [(lvl+1, 2*ix+u, 2*iy+v) for u, v in product((0,1), repeat=2)]
            children.sort(key=lambda z: hilbert_index(z[0], z[1], z[2]), reverse=True)
            tasks.extend(children)
    verdict = ("NEGATIVE_WITNESS" if witness else
               "GLOBAL_NONNEGATIVE" if not unresolved and not tasks else "UNRESOLVED")
    return AdaptiveSquareProof(poly.stamp, max_depth, seen, resolved,
                               unresolved+len(tasks),
                               None if witness else lower if lower is not None else F(0),
                               witness, verdict)


@dataclass(frozen=True)
class MissedCell:
    """A finite-observer blind negative Lipschitz tent on an unsampled cell."""
    level: int
    cell: tuple[int, int]
    center: tuple[F, F]
    depth: F

    def at(self, x: F, y: F) -> F:
        x, y = exact(x), exact(y)
        if not (0 <= x <= 1 and 0 <= y <= 1):
            raise HilbertZenoError("witness outside unit square")
        radius = self.depth
        return -max(F(0), radius - max(abs(x-self.center[0]), abs(y-self.center[1])))


def blind_tent(level: int, observed_indices: tuple[int, ...]) -> MissedCell:
    """If fewer than 4^n cells were sampled, one sharp 1-Lipschitz dip hides."""
    _stage(level)
    if any(type(i) is not int or not 0 <= i < 4**level for i in observed_indices):
        raise HilbertZenoError("unlawful Hilbert observation index")
    seen = set(observed_indices)
    if len(seen) >= 4**level:
        raise HilbertZenoError("all cells sampled: this specific blindness mechanism unavailable")
    missed = next(i for i in range(4**level) if i not in seen)
    xy = hilbert_xy(level, missed)
    return MissedCell(level, xy, cell_center(level, *xy), F(1, 2**(level+1)))



def holder_no_go_dimension(alpha: F) -> int:
    """An explicit finite-dimensional slice that obstructs any surjective
    alpha-Hölder [0,1] -> weighted infinite Hilbert cube.

    The cube contains an N-dimensional Euclidean box for every N. An
    alpha-Hölder image of a unit interval has Hausdorff dimension <=1/alpha.
    Take N=floor(1/alpha)+1, so alpha*N>1: onto is impossible.
    This is a theorem about *uniform regularity*, not nonexistence of any
    continuous Peano map onto the Hilbert cube.
    """
    a=exact(alpha)
    if a <= 0:
        raise HilbertZenoError("a positive Hölder exponent is required")
    N=a.denominator//a.numerator+1
    assert a*N>1
    return N


def hilbert_cube_error(operator_norm_cap: F, dimension: int, level: int) -> F:
    """Sharp-scope (not generally optimal constant) norm-form sampling error.

    For K = {sum_j 2^-j t_j e_j : |t_j|<=1}, each point lies within
    norm (1/sqrt(3))*(2^-dimension+2^-level) of the finite dyadic-center
    grid. |<Ax,x>-<Ay,y>| <= (2 M /3)*(...) for ||A||<=M.
    """
    M = exact(operator_norm_cap)
    _stage(dimension, 1)
    _stage(level)
    if M < 0:
        raise HilbertZenoError("operator norm bound must be nonnegative")
    return F(2,3)*M*(F(1,2**dimension)+F(1,2**level))



@dataclass(frozen=True)
class HilbertCubeHorizon:
    """Finite epsilon certification SCHEDULE from the source norm envelope."""
    coordinate_depth: int
    mesh_level: int
    grid_points: int
    error: F
    physical_tasks_executed: bool = False


def hilbert_cube_horizon(operator_norm_cap: F, tolerance: F,
                         *, max_points: int = 1000000, max_level: int = 128) -> HilbertCubeHorizon:
    """Find an effective *symmetric* d=n=k horizon, or report resource debt.

    The existence of a mathematical finite k does not imply affordable
    physical execution. The norm bound M is an externally source-proved law.
    """
    M=exact(operator_norm_cap)
    eps=exact(tolerance)
    _stage(max_points,1)
    _stage(max_level,1)
    if M < 0 or eps <= 0:
        raise HilbertZenoError("nonnegative original operator bound and positive epsilon required")
    for k in range(1,max_level+1):
        error=hilbert_cube_error(M,k,k)
        if error <= eps:
            points = 2**(k*k)
            if points > max_points:
                raise HilbertZenoError("RESOURCE_BUDGET: mathematical Zeno stage exceeds available sampling")
            return HilbertCubeHorizon(k,k,points,error)
    raise HilbertZenoError("COMPUTATION_HORIZON: mathematical existence not refuted")


@dataclass(frozen=True)
class QuadraticSource:
    """Finite source matrix for first d weighted Hilbert coordinates.

    FULL_FINITE_RANK means A is exactly this matrix and 0 on all later
    coordinates; Gershgorin/row sums verify a global norm envelope. For
    PARTIAL_SOURCE, the norm bound and entry_error are EXTERNAL HYPOTHESES,
    not established by this table, even if the stamp says 'zeta'.
    """
    stamp: SourceKey
    entries: tuple[tuple[F, ...], ...]
    operator_norm_cap: F
    entry_error: F = F(0)
    full_finite_rank: bool = False

    def __post_init__(self) -> None:
        if type(self.stamp) is not SourceKey or type(self.entries) is not tuple or not self.entries or any(type(row) is not tuple for row in self.entries):
            raise HilbertZenoError("qualified immutable operator matrix source required")
        d = len(self.entries)
        if any(len(row) != d for row in self.entries):
            raise HilbertZenoError("square matrix required")
        for i in range(d):
            for j in range(d):
                a, b = exact(self.entries[i][j]), exact(self.entries[j][i])
                if a != b:
                    raise HilbertZenoError("self-adjoint source matrix required")
        M, err = exact(self.operator_norm_cap), exact(self.entry_error)
        if M < 0 or err < 0:
            raise HilbertZenoError("negative source norm/error budget")
        if type(self.full_finite_rank) is not bool:
            raise HilbertZenoError("finite-rank proof authority must be an exact boolean")
        if self.full_finite_rank:
            if err:
                raise HilbertZenoError("complete exact finite rank source cannot have unknown matrix entries")
            row_bound = max(sum((abs(exact(v)) for v in row), F(0)) for row in self.entries)
            if M < row_bound:
                raise HilbertZenoError("unjustified finite-rank whole-Hilbert operator norm")

    @property
    def dimension(self) -> int:
        return len(self.entries)


@dataclass(frozen=True)
class HilbertCubeProof:
    stamp: SourceKey
    finite_dimension: int
    mesh_level: int
    evaluated_points: int
    minimum_matrix_value: F
    global_infimum_lower: F
    global_infimum_upper: F
    grid_to_cube_error: F
    entry_error: F
    witness: tuple[F, ...]
    verdict: str
    original_operator_identified: bool
    physical_observations_performed: bool = False
    RH_proved: bool = False


def cube_parameter_grid(level: int, dimension: int) -> Iterator[tuple[F, ...]]:
    """Complete 2^level-ary dyadic center grid in first d Hilbert coords.

    The first two axes use the genuine 2D Hilbert order. Other axes are a
    Cartesian schedule; no d-dimensional Hilbert adjacency is asserted.
    """
    _stage(level)
    _stage(dimension, 1)
    N = 1 << level
    def scaled(j: int, k: int) -> F:
        return F(1, 2**j) * (F(2*k+1, N)-1)
    if dimension == 1:
        for k in range(N):
            yield (scaled(1,k),)
    else:
        for x,y in hilbert_cells(level):
            for rest in product(range(N), repeat=dimension-2):
                yield (scaled(1,x),scaled(2,y))+tuple(scaled(j+3,k) for j,k in enumerate(rest))


def _quadratic(matrix: tuple[tuple[F,...],...], v: tuple[F,...]) -> F:
    return sum((exact(matrix[i][j])*v[i]*v[j]
                for i in range(len(v)) for j in range(len(v))), F(0))


def certify_hilbert_cube(source: QuadraticSource, level: int,
                         *, max_points: int = 100000) -> HilbertCubeProof:
    """True infinite-space extrema bounds conditional on a legitimate source A.

    For PARTIAL_SOURCE, the returned interval is a mathematically conditional
    bound; this routine does not authenticate a Weil/Suzuki source matrix.
    """
    _stage(level)
    _stage(max_points,1)
    n=source.dimension
    count = (1 << level)**n
    if count > max_points:
        raise HilbertZenoError("RESOURCE_BUDGET: finite resolution insufficiently funded")
    best: F | None = None
    point: tuple[F,...] = ()
    for x in cube_parameter_grid(level,n):
        value = _quadratic(source.entries, x)
        if best is None or value < best:
            best,point=value,x
    assert best is not None
    M=exact(source.operator_norm_cap)
    mesh_tail = hilbert_cube_error(M,n,level)
    # Every |x_i|<=2^-i, so l1 norm sum<=1-2^-d. This controls all
    # d×d matrix-entry errors by entry_error*(sum |x_i|)^2.
    value_error=exact(source.entry_error)*(1-F(1,2**n))**2
    lower,upper=best-value_error-mesh_tail,best+value_error
    identified=source.full_finite_rank
    if upper < 0:
        verdict="CERTIFIED_NEGATIVE_FINITE_RANK" if identified else "CONDITIONAL_NEGATIVE_SOURCE_WITNESS"
    elif lower >= 0 and identified:
        verdict="CERTIFIED_GLOBAL_NONNEGATIVE"
    else:
        verdict="UNRESOLVED"
    return HilbertCubeProof(source.stamp,n,level,count,best,lower,upper,
                            mesh_tail,value_error,point,verdict,identified)


def exact_neumann_legendre_2x2(a: F) -> tuple[tuple[F,F], tuple[F,F]]:
    """Source algebra for SUCC's K=V*V in the first two *unnormalized*
    mean-zero Legendre modes P1,P2 (NOT the signed Suzuki G or Weil Q).

    Cross-check against suzuki_moment_schur.low_inverse_neumann(a,2)
    after integration into the actual repository. No second Gamma inserted.
    """
    a=exact(a)
    if not 0 < a <= 1:
        raise HilbertZenoError("Legendre chart interval outside source law")
    k11 = F(2)*a**3/F(3*3)*(F(1,5)+F(1,1))
    k22 = F(2)*a**3/F(5*5)*(F(1,7)+F(1,3))
    return ((k11,F(0)),(F(0),k22))


def hilbert_source_bridge_check(a: F = F(1,2)) -> bool:
    """Re-derive and compare to the REAL already-integrated SUCC module.

    A missing source module is an error, not evidence of a proved connection.
    """
    from .suzuki_moment_schur import low_inverse_neumann
    return exact_neumann_legendre_2x2(a) == low_inverse_neumann(a, 2)


def normalized_neumann_legendre_2x2(a: F) -> tuple[tuple[F,F], tuple[F,F]]:
    """The same genuine SUCC Neumann K=V*V low matrix, but expressed in
    the normalized L² Legendre P1,P2 coordinates (their Gram is diagonal).
    This is the low compression of K, not a finite-rank representation of K.
    """
    a=exact(a)
    raw=exact_neumann_legendre_2x2(a)
    w1,w2=F(2*a,3),F(2*a,5)
    return ((raw[0][0]/w1,F(0)),(F(0),raw[1][1]/w2))
