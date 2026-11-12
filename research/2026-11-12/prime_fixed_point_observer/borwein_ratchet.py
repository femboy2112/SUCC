"""Exact Borwein support clock, integer-charge filter, and lifted source walk.

The symmetric uniform convolutions here have zero drift.  Direction is supplied
by a controller that accumulates their SUPPORT radii, latches strict crossings
of positive integer thresholds, and applies the ordinary successor once per
release.  The controller is not a sample path of the centered random sum.

For positive nonincreasing rational half-widths a_j, put A_m=sum(a_j).  Tooth k
releases on its first strict crossing A_(m-1) <= k < A_m.  At that crossing
delta=A_m-k <= a_m=min(a_j), so BOTH boundary caps are simplices and

    1 - P(|sum U[-a_j,a_j]| <= k)
      = delta**m / (2**(m-1) * m! * product(a_j)).

This certificate has no eleven-width limit.  General shifted convolution
queries reuse the legacy inclusion-exclusion routine and retain its explicit
eleven-width budget.  All certificates are rational; the separately named
logarithmic diagnostic is approximate.  Finite state means finitely many
registers with unbounded integer/rational sizes, not bounded memory.

For a nonempty bank with sum(a_j)<=1, the normalized Borwein multiplier at
integer charge c is exactly 1 at c=0, 1/2 at |c|=1, and 0 at |c|>=2.  Applying
this to c=Omega(n)-1 needs the authentic arithmetic degree as input; no prime
oracle, complexity advantage, Goldbach estimate, or physical ratchet follows.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, lgamma, log, log10

from observational_succ.borwein_prime_clock import (
    MAX_WIDTH_COUNT,
    uniform_sum_cdf,
)


MAX_RECTIFIED_WIDTH_COUNT = 8


class BorweinRatchetError(ValueError):
    """Malformed exact data, violated domain, or an explicit query budget."""


def _integer(value: int, name: str, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise BorweinRatchetError(f"{name} must be a plain integer" +
                                 (f" >= {minimum}" if minimum is not None else ""))
    return value


def _rational(value: Q, name: str, *, positive: bool = False) -> Q:
    if type(value) is not Q or (positive and value <= 0):
        qualifier = "positive " if positive else ""
        raise BorweinRatchetError(f"{name} must be a {qualifier}Fraction")
    return value


def _bank(widths: tuple[Q, ...], *, allow_empty: bool = False,
          budget: int | None = None) -> tuple[Q, ...]:
    if type(widths) is not tuple or (not allow_empty and not widths):
        raise BorweinRatchetError("widths must be a " +
                                 ("" if allow_empty else "nonempty ") + "tuple")
    if budget is not None and len(widths) > budget:
        raise BorweinRatchetError(f"this exact query permits at most {budget} widths")
    for width in widths:
        _rational(width, "half-width", positive=True)
    return widths


def window_mass(widths: tuple[Q, ...], half_window: Q = Q(1),
                shift: Q = Q(0)) -> Q:
    """Exact P(|shift + sum U[-a_j,a_j]| <= half_window).

    Nonempty banks use the legacy CDF with at most eleven widths.  An empty
    bank is the point mass at zero, so its CLOSED-window endpoints have mass
    one.  Those endpoints differ from the half-value Fourier convention in
    :func:`borwein_multiplier` and must not be conflated.
    """
    widths = _bank(widths, allow_empty=True, budget=MAX_WIDTH_COUNT)
    _rational(half_window, "half_window", positive=True)
    _rational(shift, "shift")
    if not widths:
        return Q(int(abs(shift) <= half_window))
    return (uniform_sum_cdf(widths, half_window - shift) -
            uniform_sum_cdf(widths, -half_window - shift))


def borwein_multiplier(widths: tuple[Q, ...], charge: Q,
                       half_window: Q = Q(1)) -> Q:
    """Normalized sinc integral (2*b/pi) int sinc(b*x) cos(c*x) prod sinc(a*x).

    For a nonempty bank this is exactly ``window_mass(widths, b, c)``.
    For the empty bank the improper Fourier integral is 1/2 at |c|=b,
    one inside, and zero outside; it is not the closed-window point mass.
    """
    widths = _bank(widths, allow_empty=True, budget=MAX_WIDTH_COUNT)
    _rational(charge, "charge")
    _rational(half_window, "half_window", positive=True)
    if not widths and abs(charge) == half_window:
        return Q(1, 2)
    return window_mass(widths, half_window, charge)


def integer_charge_filter(widths: tuple[Q, ...], charge: int) -> Q:
    """Exact integer-charge multiplier for a nonempty bank with sum(widths)<=1.

    This support/symmetry theorem needs no inclusion-exclusion and therefore
    imposes no width-count budget.  At charge +/-1, exactly half the symmetric
    continuous distribution lies in the translated window, including sum=1.
    """
    widths = _bank(widths)
    _integer(charge, "charge")
    if sum(widths, Q(0)) > 1:
        raise BorweinRatchetError("the integer filter requires total half-width <= 1")
    return Q(1) if charge == 0 else Q(1, 2) if abs(charge) == 1 else Q(0)


def integer_filter_error(rounds: int) -> Q:
    """Exact norm error 2**(-rounds) for powers of the declared degree filter.

    The prime sector has charge zero; the unit and semiprime sectors attain
    the contraction 1/2.  This statement presupposes the authentic Omega
    grading, not independent labels supplied by a kernel.
    """
    _integer(rounds, "rounds", 0)
    return Q(1, 2**rounds)


def strict_tooth_count(radius: Q) -> int:
    """Number of positive integers STRICTLY below radius; equality never fires."""
    _rational(radius, "radius")
    if radius < 0:
        raise BorweinRatchetError("radius must be nonnegative")
    return max(0, (radius.numerator - 1) // radius.denominator)


def _validate_summary(count: int, total: Q, smallest: Q, product: Q) -> None:
    """Necessary exact moment bounds for a positive bank with attained minimum.

    A singleton has total=minimum=product.  With m>=2 widths, one is the
    declared minimum l.  Concentrating the remaining excess minimizes the
    product; AM--GM on the remaining m-1 widths maximizes it:

        l**(m-1) * (A-(m-1)*l) <= P
            <= l * ((A-l)/(m-1))**(m-1).

    Integer cross-products avoid normalizing large intermediate Fractions.
    These are consistency tests, not authentication of an external history.
    """
    if total < count * smallest:
        raise BorweinRatchetError("total is incompatible with the declared minimum")
    if count == 1:
        if not total == smallest == product:
            raise BorweinRatchetError("a one-width summary must have total=minimum=product")
        return
    power = count - 1
    tail = total - power * smallest
    if (product.numerator * smallest.denominator**power * tail.denominator <
            product.denominator * smallest.numerator**power * tail.numerator):
        raise BorweinRatchetError("width product is below its exact feasible lower bound")
    mean = (total - smallest) / power
    if (product.numerator * smallest.denominator * mean.denominator**power >
            product.denominator * smallest.numerator * mean.numerator**power):
        raise BorweinRatchetError("width product is above its exact feasible upper bound")


@dataclass(frozen=True)
class ReleaseCertificate:
    """An exact first-crossing simplex formula, evaluated only when requested."""

    tooth: int
    step: int
    excess: Q
    smallest_width: Q
    width_product: Q

    def __post_init__(self) -> None:
        _integer(self.tooth, "tooth", 1)
        _integer(self.step, "step", 1)
        _rational(self.excess, "excess", positive=True)
        _rational(self.smallest_width, "smallest_width", positive=True)
        _rational(self.width_product, "width_product", positive=True)
        if self.excess > self.smallest_width:
            raise BorweinRatchetError("certificate is not a first monotone-width crossing")
        _validate_summary(self.step, self.tooth + self.excess,
                          self.smallest_width, self.width_product)

    def deficit(self) -> Q:
        """Exact two-tail leakage; the rational can have very large integers."""
        result = self.excess**self.step / (
            2**(self.step - 1) * factorial(self.step) * self.width_product)
        if not 0 < result < 1:
            raise BorweinRatchetError("certificate gives an impossible first-crossing probability")
        return result

    def approximate_log10_deficit(self) -> float:
        """Approximate display diagnostic ONLY; never a sign or equality witness."""
        return (self.step * (log10(self.excess.numerator) -
                             log10(self.excess.denominator)) -
                (self.step - 1) * log10(2) - lgamma(self.step + 1) / log(10) -
                log10(self.width_product.numerator) +
                log10(self.width_product.denominator))


@dataclass(frozen=True)
class RatchetState:
    """Resumable exact state for nonincreasing positive rational half-widths.

    The public constructor checks algebraic invariants, not the provenance of
    an externally fabricated summary.  Starting at ``RatchetState()`` and
    using ``advance`` supplies the declared history.  No width-count cap is
    imposed.  If every width is <=1, each update releases at most one tooth;
    larger widths produce a compact range of consecutive releases.
    """

    processed: int = 0
    radius: Q = Q(0)
    width_product: Q = Q(1)
    last_width: Q | None = None
    clicks: int = 0

    def __post_init__(self) -> None:
        _integer(self.processed, "processed", 0)
        _integer(self.clicks, "clicks", 0)
        _rational(self.radius, "radius")
        _rational(self.width_product, "width_product", positive=True)
        if self.clicks != strict_tooth_count(self.radius):
            raise BorweinRatchetError("click count must use strict support crossings")
        if self.processed == 0:
            if (self.radius, self.width_product, self.last_width, self.clicks) != (
                    Q(0), Q(1), None, 0):
                raise BorweinRatchetError("the empty state has radius 0 and product 1")
        else:
            _rational(self.last_width, "last_width", positive=True)
            _validate_summary(self.processed, self.radius, self.last_width,
                              self.width_product)

    @property
    def source_label(self) -> int:
        """The positive arithmetic label visited after all latched releases."""
        return self.clicks + 1

    def advance(self, width: Q) -> RatchetUpdate:
        """Add one half-width; keep positive-radius accumulation and latch explicit."""
        _rational(width, "width", positive=True)
        if self.last_width is not None and width > self.last_width:
            raise BorweinRatchetError("ratchet widths must be nonincreasing")
        radius = self.radius + width
        after = RatchetState(self.processed + 1, radius,
                             self.width_product * width, width,
                             strict_tooth_count(radius))
        return RatchetUpdate(self, after)

    def lifted(self, circumference: int) -> LiftedAddress:
        return LiftedAddress.from_label(self.source_label, circumference)


@dataclass(frozen=True)
class RatchetUpdate:
    """One validated update; releases are a lazy integer range, not skipped labels."""

    before: RatchetState
    after: RatchetState

    def __post_init__(self) -> None:
        if type(self.before) is not RatchetState or type(self.after) is not RatchetState:
            raise BorweinRatchetError("updates require exact RatchetState objects")
        width = self.after.last_width
        if (width is None or self.after.processed != self.before.processed + 1 or
                self.after.radius != self.before.radius + width or
                self.after.width_product != self.before.width_product * width or
                (self.before.last_width is not None and width > self.before.last_width)):
            raise BorweinRatchetError("update states do not describe one admissible width")

    @property
    def releases(self) -> range:
        return range(self.before.clicks + 1, self.after.clicks + 1)

    def certificate(self, tooth: int) -> ReleaseCertificate:
        _integer(tooth, "tooth", 1)
        if tooth not in self.releases:
            raise BorweinRatchetError("the requested tooth did not first release here")
        return ReleaseCertificate(tooth, self.after.processed,
                                  self.after.radius - tooth,
                                  self.after.last_width, self.after.width_product)


def first_crossing_deficit(widths: tuple[Q, ...], tooth: int = 1) -> Q:
    """Convenience certificate for a complete first-crossing prefix; no CDF cap."""
    widths = _bank(widths)
    _integer(tooth, "tooth", 1)
    state = RatchetState()
    for width in widths:
        update = state.advance(width)
        state = update.after
    return update.certificate(tooth).deficit()


@dataclass(frozen=True)
class LiftedAddress:
    """Source n=1+L*turn+residue; circumference quotient retains its winding.

    The address is n-1.  Consequently multiplication by m acts on addresses
    as c -> m*c+(m-1), including the offset that a residue-only model loses.
    """

    circumference: int
    turn: int
    residue: int

    def __post_init__(self) -> None:
        _integer(self.circumference, "circumference", 2)
        _integer(self.turn, "turn", 0)
        _integer(self.residue, "residue", 0)
        if self.residue >= self.circumference:
            raise BorweinRatchetError("residue must be smaller than circumference")

    @classmethod
    def from_label(cls, label: int, circumference: int) -> LiftedAddress:
        _integer(label, "source label", 1)
        _integer(circumference, "circumference", 2)
        turn, residue = divmod(label - 1, circumference)
        return cls(circumference, turn, residue)

    @property
    def label(self) -> int:
        return 1 + self.circumference * self.turn + self.residue

    def successor(self, steps: int = 1) -> LiftedAddress:
        _integer(steps, "successor steps", 0)
        return type(self).from_label(self.label + steps, self.circumference)

    def multiply(self, multiplier: int) -> LiftedAddress:
        _integer(multiplier, "multiplier", 1)
        return type(self).from_label(multiplier * self.label, self.circumference)

    def divisor_gate(self, modulus: int) -> int:
        """The authentic source Q_m, not a predicate of angle alone."""
        _integer(modulus, "modulus", 1)
        return int(self.label % modulus == 0)


def rectified_cdf(widths: tuple[Q, ...], threshold: Q) -> Q:
    """CDF of sum max(U[-a_j,a_j],0), with the atom at zero retained.

    This OPTIONAL directed stochastic model changes each factor to
    (delta_0 + Uniform[0,a_j])/2.  It is not the original symmetric sinc
    product.  A subset mixture gives an exact finite law, capped at eight
    widths because it calls several bounded inclusion-exclusion CDFs.
    """
    widths = _bank(widths, allow_empty=True, budget=MAX_RECTIFIED_WIDTH_COUNT)
    _rational(threshold, "threshold")
    if threshold < 0:
        return Q(0)
    if threshold >= sum(widths, Q(0)):
        return Q(1)
    total = Q(0)
    for mask in range(1 << len(widths)):
        active = tuple(width / 2 for j, width in enumerate(widths)
                       if mask & (1 << j))
        total += (uniform_sum_cdf(active, threshold - sum(active, Q(0)))
                  if active else Q(1))
    return total / 2**len(widths)


def rectified_moments(widths: tuple[Q, ...]) -> tuple[Q, Q]:
    """Exact (mean, variance) of the explicitly rectified independent sum."""
    widths = _bank(widths, allow_empty=True)
    return (sum(widths, Q(0)) / 4,
            Q(5, 48) * sum((width**2 for width in widths), Q(0)))
