"""Exact projective Cayley algebra and paid BBP completion clocks.

The projective arithmetic is over Q and includes the point at infinity.  An
authentic BBP phase is generally algebraic, not a rational projective point;
this module never replaces tan(pi*r(n)) with the rational number r(n).
The source certificates instead reuse the canonical rational ``duck_bbp``
prefix/tail API.  Theorems, domains and limitations are in CAYLEY_PROOFS.md.

No function certifies cofinality from a finite schedule or estimates a signed
Weyl mean.  All transcendental phase errors are represented by a rational
coefficient B for the proved inequality ``error <= min(2, 2*pi*B)``.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .duck_bbp import source_tail_budget, tail_interval


def _natural(value: int, name: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def _rational(value: int | Fraction, name: str) -> Fraction:
    if type(value) not in (int, Fraction):
        raise ValueError(f"{name} must be an exact int or Fraction")
    return Fraction(value)


def _multiply(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    a, b = left
    c, d = right
    return a*c - b*d, a*d + b*c


def _power(
    value: tuple[Fraction, Fraction], exponent: int
) -> tuple[Fraction, Fraction]:
    result = (Fraction(1), Fraction(0))
    while exponent:
        if exponent % 2:
            result = _multiply(result, value)
        value = _multiply(value, value)
        exponent //= 2
    return result


@dataclass(frozen=True)
class ProjectivePoint:
    """A rational point [x:y] in RP^1, normalized to [1:y/x] or [0:1].

    The affine coordinate is y/x, and infinity is [0:1].  A negative
    homogeneous rescaling leaves the same point.  Floating inputs are
    rejected because these objects are exact certificates.
    """

    x: Fraction
    y: Fraction

    def __post_init__(self) -> None:
        x = _rational(self.x, "x")
        y = _rational(self.y, "y")
        if not x and not y:
            raise ValueError("[0:0] is not a projective point")
        if x:
            x, y = Fraction(1), y/x
        else:
            x, y = Fraction(0), Fraction(1)
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)

    @property
    def is_infinite(self) -> bool:
        return self.x == 0


def cayley_mode(point: ProjectivePoint, frequency: int = 1) -> tuple[Fraction, Fraction]:
    """Exact real/imaginary parts of ((x+i*y)/(x-i*y))**frequency.

    Every mode is defined at infinity, with value (-1)**frequency.  The
    negative-frequency case uses complex conjugation of a unit complex
    number, so no algebraic or floating approximation is introduced.
    """
    if not isinstance(point, ProjectivePoint) or type(frequency) is not int:
        raise ValueError("ProjectivePoint and integer frequency required")
    x, y = point.x, point.y
    norm = x*x + y*y
    unit = ((x*x-y*y)/norm, 2*x*y/norm)
    if frequency < 0:
        unit = unit[0], -unit[1]
    return _power(unit, abs(frequency))


def projective_power(point: ProjectivePoint, degree: int) -> ProjectivePoint:
    """The point with components Re((x+i*y)**degree), Im((x+i*y)**degree).

    This is the degree-m circle power map in the
    projective chart; tangent denominators may vanish without a failure.
    """
    if not isinstance(point, ProjectivePoint):
        raise ValueError("ProjectivePoint required")
    _natural(degree, "degree", 1)
    return ProjectivePoint(*_power((point.x, point.y), degree))


def projective_rotate(point: ProjectivePoint, rotation: ProjectivePoint) -> ProjectivePoint:
    """Projective angle addition by a declared exact rational rotation.

    A BBP step would use [cos(pi*r(n)):sin(pi*r(n))], usually outside Q.
    This rational routine does not claim to synthesize that rotation.
    """
    if not isinstance(point, ProjectivePoint) or not isinstance(rotation, ProjectivePoint):
        raise ValueError("two ProjectivePoint values required")
    return ProjectivePoint(*_multiply((point.x, point.y), (rotation.x, rotation.y)))


def source_completed_interval(time: int, horizon: int) -> tuple[Fraction, Fraction]:
    """Canonical strict enclosure of 16**(time-1)*pi, 0<=time<=horizon.

    Reuses P_L and its source-sensitive upper tail from duck_bbp.  The
    geometric-pi identification depends on the classical BBP identity.
    No seed or source can be silently replaced through this interface.
    """
    _natural(time, "time")
    _natural(horizon, "horizon", time)
    low, high = tail_interval(0, horizon)
    scale = 16**time
    return scale*low, scale*high


def band_phase_error_coefficient(time: int, horizon: int, cutoff: int) -> Fraction:
    """B controlling all times 0..time and all integer modes |h|<=cutoff.

    The corresponding complex phase error is at most min(2,2*pi*B).
    This is a finite, checkable bandwidth/horizon payment, not an infinite
    cofinality assertion.  The largest interval occurs at the final time.
    """
    _natural(time, "time")
    _natural(horizon, "horizon", time)
    _natural(cutoff, "cutoff")
    return Fraction(cutoff, 16**(horizon-time))*source_tail_budget(horizon)


def source_phase_error_coefficient(time: int, horizon: int, frequency: int) -> Fraction:
    """Rational B for one declared integer Fourier frequency."""
    if type(frequency) is not int:
        raise ValueError("frequency must be an integer")
    return band_phase_error_coefficient(time, horizon, abs(frequency))


def coupled_horizon(time: int, cutoff: int, tolerance: int | Fraction) -> int:
    """Least L>=time paying B<=tolerance for the whole finite probe band.

    The search terminates because the proved source tail decays and the
    factor 16**(time-L) tends to zero.  It says nothing about the sign or
    cancellation of the measured modes.
    """
    _natural(time, "time")
    _natural(cutoff, "cutoff")
    tolerance = _rational(tolerance, "tolerance")
    if tolerance <= 0:
        raise ValueError("positive tolerance required")
    horizon = time
    while band_phase_error_coefficient(time, horizon, cutoff) > tolerance:
        horizon += 1
    return horizon


def quadratic_resonance_frequency(time: int) -> int:
    """Explicit hostile growing mode h_n=32*n*n (n>=1)."""
    _natural(time, "time", 1)
    return 32*time*time


def resonance_turn_interval(time: int, depth: int) -> tuple[Fraction, Fraction]:
    """Exact enclosure for h_n*T_n, which tends to 1/2 analytically."""
    frequency = quadratic_resonance_frequency(time)
    _natural(depth, "depth")
    low, high = tail_interval(time, depth)
    return frequency*low, frequency*high


def resonance_chord_lower_bound(time: int, depth: int) -> Fraction:
    """A rational lower bound for |e(h_n*T_n)-1|, approaching 2.

    If |h_n*T_n-1/2|<=epsilon<=1/2, concavity of cosine on [0,pi/2]
    gives 2*cos(pi*epsilon)>=2-4*epsilon.  Larger enclosures return the
    safe bound zero.  No floating sine/cosine is used as a certificate.
    """
    low, high = resonance_turn_interval(time, depth)
    epsilon = max(abs(low-Fraction(1, 2)), abs(high-Fraction(1, 2)))
    return max(Fraction(0), 2-4*epsilon)


def _epoch_source_scale(epoch_start: int, cutoff: int) -> Fraction:
    _natural(epoch_start, "epoch_start", 1)
    _natural(cutoff, "cutoff")
    # The rational constant 7 is a strict upper bound for 2*pi.
    return 7*cutoff*source_tail_budget(2*epoch_start)


def common_horizon_epoch_phase_bound(epoch_start: int, cutoff: int) -> Fraction:
    """Exact clipped phase-mean budget for A<=n<2A, common horizon L=2A.

    Returns A**(-1) sum_{j=1}^A min(2,D/16**j), D=7*H*r(2A+1)/15.
    This uniformly bounds the difference of completed and finite-completed
    Weyl means for |h|<=H.  The saturated prefix is counted and the remaining
    geometric sum is evaluated exactly.  This does not bound either mean.
    """
    scale = _epoch_source_scale(epoch_start, cutoff)
    term = scale/16
    saturated = 0
    while saturated < epoch_start and term >= 2:
        saturated += 1
        term /= 16
    remaining = epoch_start-saturated
    tail = term*Fraction(16, 15)*(1-Fraction(1, 16**remaining))
    return (2*saturated+tail)/epoch_start


def common_horizon_epoch_linear_bound(epoch_start: int, cutoff: int) -> Fraction:
    """Unclipped geometric budget D*(1-16**(-A))/(15*A)."""
    scale = _epoch_source_scale(epoch_start, cutoff)
    return scale*(1-Fraction(1, 16**epoch_start))/(15*epoch_start)


def common_horizon_epoch_log_bound(epoch_start: int, cutoff: int) -> tuple[int, Fraction]:
    """Return k and min(2,(2*k+2/15)/A), with D/16**k<=2 first true.

    It follows analytically that this tends to zero whenever
    log(1+H_A)=o(A).  The returned finite budget alone does not assert that
    a user-supplied infinite cutoff sequence meets this hypothesis.
    """
    scaled = _epoch_source_scale(epoch_start, cutoff)
    threshold = 0
    while scaled > 2:
        threshold += 1
        scaled /= 16
    return threshold, min(Fraction(2), (2*threshold+Fraction(2, 15))/epoch_start)
