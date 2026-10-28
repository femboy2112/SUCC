"""Exact audit of a Fourier ladder that is also a shift in source time.

For x_(n+1) = b*x_n + r_(n+1), n=1,...,N, and e(t)=exp(2*pi*i*t),

  S_N(b*h)-S_N(h)
    = e(h*x_(N+1))-e(h*x_1)
      + sum_n e(h*x_(n+1)) * (e(-h*r_(n+1))-1).

The identity is certified in Q[Q/Z]. Its COMPLEX evaluation obeys
|A_N(b*h)-A_N(h)| <= (2 + 2*pi*|h|*sum |r_(n+1)|)/N.
We use the outward rational majorant 2*pi < 7. No norm estimate is
claimed for the free group algebra; its evaluation is the observable.

Authentic BBP r(m)>0 and r(m)<=15/(8*m-7)^2, m>=2, imply
sum_(m>=2) r(m) <= 15*(1/81+1/72)=85/216. Hence the authentic
normalized ladder defect is O_h(1/N), uniformly in N. Saturating each
phase error at 2 improves the moving-frequency bound to O(sqrt(|h|)/N),
so |h_N|=o(N^2) is sufficient. This reuses the saturation method already
proved for Green/Fejer transport in OPERATION_SPECTRAL_PURITY.md, section 3;
the new application is to the source-time ladder defect.

A strict fixed ratio |A_N(16*h)|<=q|A_N(h)|, q<1, therefore ALREADY
implies |A_N(h)|=O_h(1/N). It is a stronger cancellation premise, not
an independently available multiplicative improvement. The code returns
this implication's conditional bound; it never asserts the premise.

For fixed finite rational history, the literal condition
limsup_(h->infinity) |A_N(16*h)|/|A_N(h)| < 1 is false: every positive
multiple of the common denominator has both averages exactly equal to 1.
Any proposed frequency-band restriction must be stated separately.

Classical elementary identities, source-specific audit. No pi normality
or RH theorem is claimed. Original arithmetic sources remain unchanged.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from . import succ_internal_matrix_walk as mw


PP = mw.PhasePoly
BBP_FORCING_TAIL_UPPER = Q(85, 216)
pi_normality_proved = False
ladder_contraction_proved = False


def _positive_integer(value, label):
    if type(value) is not int or value < 1:
        raise ValueError(f"{label} must be a positive integer")
    return value


def _frequency(value):
    if type(value) is not int or value == 0:
        raise ValueError("frequency must be a nonzero integer")
    return value


@dataclass(frozen=True)
class LadderShiftAudit:
    """Finite exact identity plus a bound on its complex evaluation."""

    length: int
    radix: int
    frequency: int
    difference: PP
    endpoint: PP
    forcing_defect: PP
    forcing_l1: Q
    forcing_phase_bound: Q

    @property
    def residual(self):
        return self.difference - self.endpoint - self.forcing_defect

    @property
    def normalized_bound(self):
        return min(Q(2), (2 + self.forcing_phase_bound) / self.length)


def ladder_shift_audit(states, forcings, frequency, radix=16):
    """Audit N+1 states x_1,...,x_(N+1) and N declared transition forces.

    Explicit forces are required: the routine will not infer a new source
    from a mutated history. This generic identity is forcing-agnostic;
    ``authentic_ladder_audit`` separately authenticates the BBP input.
    """
    _positive_integer(radix, "radix")
    if radix < 2:
        raise ValueError("radix must be at least two")
    _frequency(frequency)
    xs = tuple(mw.rat(x) for x in states)
    rs = tuple(mw.rat(r) for r in forcings)
    if len(xs) < 2 or len(rs) != len(xs) - 1:
        raise ValueError("N+1 states and N transition forces are required")
    for n, force in enumerate(rs):
        if xs[n + 1] != radix * xs[n] + force:
            raise ValueError("history does not obey the declared source recurrence")

    difference = sum((mw.formal_character(radix * frequency, x)
                      - mw.formal_character(frequency, x)
                      for x in xs[:-1]), PP.zero())
    endpoint = (mw.formal_character(frequency, xs[-1])
                - mw.formal_character(frequency, xs[0]))
    defect = sum((mw.formal_character(frequency, xs[n + 1])
                  * (mw.formal_character(-frequency, force) - PP.one())
                  for n, force in enumerate(rs)), PP.zero())
    phase_bound = sum((min(Q(2), 7 * abs(frequency * r)) for r in rs), Q())
    return LadderShiftAudit(len(rs), radix, frequency, difference,
                            endpoint, defect, sum(map(abs, rs), Q()), phase_bound)


def authentic_ladder_audit(length, frequency=1):
    """Authentic U_1,...,U_(N+1), generated from the original U_0=0."""
    mw.natural(length, 1, 2000)
    _frequency(frequency)
    state = Q()
    states = []
    for n in range(1, length + 2):
        state = 16 * state + mw.authentic_r(n)
        states.append(state)
    forcings = tuple(mw.authentic_r(n) for n in range(2, length + 2))
    return ladder_shift_audit(states, forcings, frequency)


def authentic_linear_shift_bound(length, frequency=1):
    """The simple O(|h|/N) all-N bound from the total forcing mass.

    The quantitative statement is min(2, (2+595*|h|/216)/N).
    It gives no fixed-h asymptotic conclusion when h itself grows like N.
    """
    _positive_integer(length, "length")
    _frequency(frequency)
    return min(Q(2),
               (2 + 7 * abs(frequency) * BBP_FORCING_TAIL_UPPER) / length)


def authentic_normalized_shift_bound(length, frequency=1):
    """All-N rational bound using both total mass and saturated tail.

    For K=ceil(sqrt(|h|)), r(n+1)<=15/(64*n^2) gives
    sum_n min(2,7|h|r(n+1)) <= 2*K + 105*|h|/(64*K).
    Thus the bound vanishes whenever |h_N|=o(N^2). The exact integral
    majorant is (2+sqrt(105*|h|/8))/N; the finite split used here avoids
    floating-point square roots and is a slightly looser rational bound.
    """
    linear = authentic_linear_shift_bound(length, frequency)
    h = abs(frequency)
    split = isqrt(h)
    if split * split < h:
        split += 1
    saturated = (2 + 2 * split + Q(105 * h, 64 * split)) / length
    return min(linear, saturated)


def bound_if_contraction(length, frequency, ratio_upper):
    """Conditional bound on |A_N(h)| IF |A_N(16h)|<=q*|A_N(h)|.

    This function computes the logical consequence, not a certificate
    that its missing contraction premise is true on the authentic orbit.
    """
    q = mw.rat(ratio_upper)
    if not Q(0) <= q < 1:
        raise ValueError("conditional ratio bound must lie in [0,1)")
    return min(Q(1), authentic_normalized_shift_bound(length, frequency)
               / (1 - q))
