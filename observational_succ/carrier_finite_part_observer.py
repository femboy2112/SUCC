"""Two source-compatible regulator readouts identify a finite part, not a source.

Classical extrapolation, with exact rational observation and remainder bounds.
The applied Abel remainder bound is paper-derived from NIST DLMF 4.36.3 and
classical zeta(2), zeta(4). No QFT or divergent-ordinary-sum identity is asserted.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from .carrier_relative_targets import CarrierError, rational, label


@dataclass(frozen=True)
class ScaleReading:
    source: str
    scale: Q
    lower: Q
    upper: Q

    def __post_init__(self):
        label(self.source)
        if (any(type(v) is not Q for v in (self.scale, self.lower, self.upper)) or
                self.scale <= 0 or self.lower > self.upper):
            raise CarrierError("positive exact scale and ordered rational enclosure required")


@dataclass(frozen=True)
class FinitePartCertificate:
    source: str
    scale: Q
    lower: Q
    upper: Q
    residual_coefficient: Q
    premise: str = "SAME F(s)=a/s^2+b+R(s); 0<=R(s)<=C*s^2 AT BOTH SCALES"

    @property
    def midpoint(self):
        return (self.lower+self.upper)/2

    @property
    def radius(self):
        return (self.upper-self.lower)/2


def paired_finite_part(first, second, remainder_coefficient):
    """Cancel unknown a using (4 F(2t)-F(t))/3; keep both finite errors.

    Since 0<=R(t)<=C t² and 0<=R(2t)<=4C t²,
    b is in [contrast_lower-16C t²/3, contrast_upper+C t²/3].
    This is conditional on the stated model class, not empirical attestation.
    """
    if type(first) is not ScaleReading or type(second) is not ScaleReading:
        raise CarrierError("two typed source readouts required")
    if first.source != second.source or second.scale != 2*first.scale:
        raise CarrierError("same source and exact two-scale transport required")
    c = rational(remainder_coefficient)
    if c < 0:
        raise CarrierError("nonnegative remainder coefficient required")
    t = first.scale
    return FinitePartCertificate(first.source, t,
        (4*second.lower-first.upper)/3-16*c*t*t/3,
        (4*second.upper-first.lower)/3+c*t*t/3, c)


def abel_reading(scale, terms=32):
    """Exact enclosure of sum n exp(-n*t)=q/(1-q)^2, 0<t<=1.

    Consecutive alternating Taylor sums enclose q=exp(-t); the rational
    function q/(1-q)^2 is increasing on (0,1). No floating point or pi input.
    """
    t = rational(scale)
    if not 0 < t <= 1 or type(terms) is not int or not 2 <= terms <= 100:
        raise CarrierError("0<t<=1 and Taylor term count 2..100 required")
    partial, term = Q(1), Q(1)
    for k in range(1, terms):
        term *= -t/k
        partial += term
    following = partial+term*(-t)/terms
    lo, hi = sorted((partial, following))
    if not 0 < lo <= hi < 1:
        raise CarrierError("Taylor enclosure too coarse for the rational denominator")
    return ScaleReading("Q:exponential-Abel-natural-source", t,
                        lo/(1-lo)**2, hi/(1-hi)**2)


def abel_finite_part(scale, terms=32):
    """Known zeta(-1) finite-part calibration using two actual Abel readouts.

    PAPER premise: 0<F(t)-t^-2+1/12<=t²/240 for t>0.
    The ordinary positive divergent series is not assigned a negative sum.
    """
    t = rational(scale)
    if not 0 < t <= Q(1, 2):
        raise CarrierError("both regulator scales must be in (0,1]")
    return paired_finite_part(abel_reading(t, terms), abel_reading(2*t, terms), Q(1, 240))
