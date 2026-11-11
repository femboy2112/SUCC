"""Certified finite Haar/Pascal observations of the literal zero BBP source.

This is a finite compiler backend, not a normality prover. Source integer
rounding has an analytic tail bound. No floating-point values enter a proof
certificate. All asymptotic contraction flags remain false.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import comb, isqrt

from .duck_bbp import forcing


def _nat(value: int, name: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an exact integer >= {minimum}")
    return value


@dataclass(frozen=True)
class PhaseGridCertificate:
    """Recomputable source enclosure; phases are lower grid endpoints.

    For each stored k, the true completed phase lies in [k/q,(k+1)/q).
    The global enclosure proves the cell and first digit, including the seam.
    n=0 starts with the integer hexadecimal digit of pi (3).
    """

    start: int
    count: int
    depth: int
    guard: int
    horizon: int
    integer_lower: int
    integer_upper: int
    points: tuple[int, ...]

    @property
    def denominator(self) -> int:
        return 16**self.depth

    @property
    def point_error(self) -> F:
        return F(1, self.denominator)


@lru_cache(maxsize=8, typed=True)
def _source_integer_enclosure(horizon: int) -> tuple[int, int]:
    """16^H alpha lies in [lo,hi], alpha=sum 16^-j r(j).

    Each of H floor operations loses less than 1. The omitted tail after
    scaling is T_H<=r(H+1)/15<1, hence hi=lo+H+1. All source terms are
    evaluated through the canonical combined rational function.
    """
    _nat(horizon, "horizon", 1)
    power = 16**(horizon-1)
    lower = 0
    for n in range(1, horizon+1):
        r = forcing(n)
        direct = F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
        if type(r) is not F or r != direct:
            raise ValueError("source primitive failed four-pole authentication")
        lower += power*r.numerator//r.denominator
        power //= 16
    return lower, lower+horizon+1


def certified_phase_grid(start: int, count: int, *, depth: int = 10,
                         guard: int = 16) -> PhaseGridCertificate:
    """Enclose completed zero-seed phases using one common source horizon.

    No precision fallback silently rounds a boundary: unresolved cells raise
    ArithmeticError, and the caller can explicitly increase the guard.
    """
    _nat(start, "start")
    _nat(count, "count", 1)
    _nat(depth, "depth", 1)
    _nat(guard, "guard", 1)
    horizon = start+count-1+depth+guard
    lower, upper = _source_integer_enclosure(horizon)
    denominator = 16**depth
    points = []
    for n in range(start, start+count):
        shift = 4*(horizon-n-depth)
        left, right = lower >> shift, upper >> shift
        if left != right:
            raise ArithmeticError(f"phase cell unresolved at clock {n}; increase guard")
        points.append(left % denominator)
    return PhaseGridCertificate(start, count, depth, guard, horizon,
                                lower, upper, tuple(points))


def verify_phase_grid(certificate: PhaseGridCertificate) -> bool:
    """Rebuild from the source rather than trust a label or stored bounds."""
    if type(certificate) is not PhaseGridCertificate:
        return False
    try:
        for name, minimum in (("start",0),("count",1),("depth",1),("guard",1),
                              ("horizon",1),("integer_lower",0),("integer_upper",0)):
            _nat(getattr(certificate,name), name, minimum)
        if (type(certificate.points) is not tuple
                or len(certificate.points) != certificate.count
                or any(type(k) is not int or not 0 <= k < certificate.denominator
                       for k in certificate.points)):
            return False
        actual = certified_phase_grid(certificate.start, certificate.count,
                                      depth=certificate.depth,
                                      guard=certificate.guard)
        return actual == certificate
    except (ValueError, TypeError, ArithmeticError, OverflowError):
        return False


def _points(points: tuple[int, ...], denominator: int) -> None:
    _nat(denominator, "denominator", 16)
    if denominator % 16:
        raise ValueError("the phase grid must be divisible by 16")
    if type(points) is not tuple or not points:
        raise ValueError("nonempty immutable point tuple required")
    if any(type(k) is not int or not 0 <= k < denominator for k in points):
        raise ValueError("canonical exact integer grid coordinates required")


def _defect_jumps(points: tuple[int, ...], denominator: int) -> dict[int, int]:
    """CDF jumps of (I-Q)mu in units 1/(16*N), Q=C T*."""
    _points(points, denominator)
    jumps: Counter[int] = Counter()
    for k, count in Counter(points).items():
        jumps[k] += 16*count
        future = k % (denominator//16)
        for digit in range(16):
            jumps[future+digit*(denominator//16)] -= count
    return {k: value for k, value in jumps.items() if value}


def grid_haar_defect(points: tuple[int, ...], denominator: int) -> F:
    """Exact interval W1(mu,Qmu) on a common rational grid."""
    jumps = _defect_jumps(points, denominator)
    area = delta = previous = 0
    for k in sorted(jumps):
        area += (k-previous)*abs(delta)
        delta += jumps[k]
        previous = k
    if delta:
        raise AssertionError("signed measure did not have mass zero")
    return F(area, 16*len(points)*denominator)


@dataclass(frozen=True)
class DefectInterval:
    lower: F
    upper: F
    approximation: F
    error: F

    def __post_init__(self) -> None:
        if any(type(x) is not F for x in (self.lower,self.upper,self.approximation,self.error)):
            raise ValueError("defect interval fields must be exact Fractions")
        if not (0 <= self.lower <= self.upper <= 1 and 0 <= self.approximation <= 1
                and self.error >= 0 and self.lower >= max(F(),self.approximation-self.error)
                and self.upper <= min(F(1),self.approximation+self.error)):
            raise ValueError("invalid defect interval bounds")


def certified_haar_defect(certificate: PhaseGridCertificate,
                          offset: int = 0, count: int | None = None) -> DefectInterval:
    """True completed-source defect within 2/q of the grid computation.

    Cell certification retains each first digit, so both mu and Qmu move
    by at most 1/q in interval W1. No circular/interval switch is hidden.
    """
    if type(certificate) is not PhaseGridCertificate:
        raise TypeError("a source phase certificate is required")
    if not verify_phase_grid(certificate):
        raise ValueError("invalid source phase certificate")
    _nat(offset, "offset")
    if count is None:
        count = certificate.count-offset
    _nat(count, "count", 1)
    if offset+count > certificate.count:
        raise ValueError("requested observation exceeds the certified source window")
    d = grid_haar_defect(certificate.points[offset:offset+count], certificate.denominator)
    error = 2*certificate.point_error
    return DefectInterval(max(F(), d-error), min(F(1), d+error), d, error)


@dataclass(frozen=True)
class SignedOverlap:
    early: F
    late: F
    combined: F
    overlap: F


def signed_block_overlap(early: tuple[int, ...], late: tuple[int, ...],
                         denominator: int) -> SignedOverlap:
    """D_union=(D_early+D_late)/2-overlap, an exact signed CDF identity.

    overlap integrates min(|H_early|,|H_late|) only where signs disagree.
    It is neither assumed positive at a useful scale nor fitted as an error.
    """
    if len(early) != len(late):
        raise ValueError("equal nonempty block lengths required")
    a, b = _defect_jumps(early, denominator), _defect_jumps(late, denominator)
    left = right = previous = area_left = area_right = area_union = overlap = 0
    for k in sorted(a.keys() | b.keys()):
        width = k-previous
        area_left += width*abs(left)
        area_right += width*abs(right)
        area_union += width*abs(left+right)
        if left*right < 0:
            overlap += width*min(abs(left), abs(right))
        left += a.get(k, 0)
        right += b.get(k, 0)
        previous = k
    if left or right:
        raise AssertionError("invalid signed probability difference")
    scale = 16*len(early)*denominator
    answer = SignedOverlap(F(area_left, scale), F(area_right, scale),
                           F(area_union, 2*scale), F(overlap, scale))
    if answer.combined != (answer.early+answer.late)/2-answer.overlap:
        raise AssertionError("signed overlap identity failed")
    return answer


def contraction_residual(larger: DefectInterval, smaller: DefectInterval,
                         theta: F, error: F = F()) -> tuple[F, F]:
    """Enclose D_large-theta*D_small-error. A finite verdict only."""
    if type(larger) is not DefectInterval or type(smaller) is not DefectInterval:
        raise ValueError("exact defect intervals required")
    larger.__post_init__()
    smaller.__post_init__()
    if type(theta) not in (int, F) or not 0 <= theta < 1:
        raise ValueError("exact 0<=theta<1 required")
    if type(error) not in (int, F) or error < 0:
        raise ValueError("exact nonnegative proposed error required")
    return (larger.lower-theta*smaller.upper-error,
            larger.upper-theta*smaller.lower-error)


def finite_verdict(residual: tuple[F, F]) -> str:
    """Verdict conditional on the supplied exact enclosure, not its provenance."""
    if (type(residual) is not tuple or len(residual) != 2
            or any(type(x) is not F for x in residual)):
        raise ValueError("two exact Fraction endpoints are required")
    lo, hi = residual
    if lo > hi:
        raise ValueError("empty residual interval")
    if hi <= 0:
        return "CERTIFIED_FINITE_PASS"
    if lo > 0:
        return "CERTIFIED_FINITE_FAIL"
    return "UNRESOLVED_PRECISION"


def bernstein_vector(degree: int, y: F) -> tuple[F, ...]:
    _nat(degree, "degree")
    if type(y) not in (int, F) or not 0 <= y <= 1:
        raise ValueError("exact y in [0,1] required")
    y = F(y)
    return tuple(comb(degree, j)*y**j*(1-y)**(degree-j)
                 for j in range(degree+1))


@dataclass(frozen=True)
class PascalCharacter:
    """Exact Q(zeta_16) coefficients modulo zeta_16^8+1, plus analytic error."""
    frequency: int
    degree: int
    component: int
    coefficients: tuple[F, ...]
    modulus_error: F

    def __post_init__(self) -> None:
        _nat(self.frequency,"frequency",1)
        _nat(self.degree,"degree")
        _nat(self.component,"component")
        if self.frequency > 15 or self.component > self.degree:
            raise ValueError("invalid Pascal character index")
        if (type(self.coefficients) is not tuple or len(self.coefficients) != 8
                or any(type(x) is not F for x in self.coefficients)
                or type(self.modulus_error) is not F or self.modulus_error < 0):
            raise ValueError("eight exact coefficients and a nonnegative exact error required")

    @property
    def modulus_upper(self) -> F:
        return sum(map(abs, self.coefficients), F())+self.modulus_error


def certified_pascal_characters(certificate: PhaseGridCertificate, degree: int,
                                frequencies: tuple[int, ...] = tuple(range(1, 16))) -> tuple[PascalCharacter, ...]:
    """Finite G_(h;m,j)=mean zeta_16^(h*d_n) B_(m,j)(z_(n+1)).

    The certificate must include the next phase. First digits are exact;
    Bernstein derivatives have absolute value <=m, giving error m/q.
    """
    _nat(degree, "degree")
    if type(certificate) is not PhaseGridCertificate or certificate.count < 2:
        raise ValueError("at least two certified consecutive source phases required")
    if not verify_phase_grid(certificate):
        raise ValueError("invalid source phase certificate")
    if type(frequencies) is not tuple or any(type(h) is not int or not 1 <= h <= 15
                                            for h in frequencies):
        raise ValueError("digit characters h=1,...,15 required")
    if len(set(frequencies)) != len(frequencies):
        raise ValueError("duplicate digit characters are not allowed")
    count, denominator = certificate.count-1, certificate.denominator
    rows = {(h,j): [F() for _ in range(8)]
            for h in frequencies for j in range(degree+1)}
    for k, following in zip(certificate.points, certificate.points[1:]):
        digit = (16*k)//denominator
        bs = bernstein_vector(degree, F(following, denominator))
        for h in frequencies:
            exponent = (h*digit) % 16
            sign = 1 if exponent < 8 else -1
            for j, value in enumerate(bs):
                rows[h,j][exponent % 8] += sign*value/count
    return tuple(PascalCharacter(h, degree, j, tuple(rows[h,j]),
                                 degree*certificate.point_error)
                 for h in frequencies for j in range(degree+1))


def pascal_haar_upper(certificate: PhaseGridCertificate, degree: int) -> F:
    """Conservative exact bound on W1(mu_N,lambda); never an asymptotic flag.

    The source, consecutive orbit, count, and all characters are rebuilt
    together. Caller-supplied character arrays or counts are not accepted as
    proof. The positive-square degree makes 1/(16 sqrt(m)) rational.
    """
    _nat(degree, "degree", 1)
    m = degree
    root = isqrt(m)
    if root < 1 or root*root != m:
        raise ValueError("positive square Bernstein degree required")
    characters = certified_pascal_characters(certificate, degree)
    count = certificate.count-1
    return F(16,15)*(sum((c.modulus_upper for c in characters), F())
                     + F(1,16*root))+F(1,15*count)


def orbit_defect_floor(count: int) -> F:
    """Universal D_N >=11/(64N) for an actual length-N radix-16 orbit."""
    _nat(count, "count", 1)
    return F(11,64*count)


def contraction_error_floor(theta: F) -> F:
    """Necessary limsup N*epsilon_N lower bound for an all-large-N theorem.

    For theta<1/2 this equals 11(1-2theta)/64. The zero returned for larger
    theta supplies no positive restriction; it is not a sufficiency claim.
    """
    if type(theta) not in (int,F) or not 0 <= theta < 1:
        raise ValueError("exact 0<=theta<1 required")
    return max(F(), F(11,64)*(1-2*theta))
