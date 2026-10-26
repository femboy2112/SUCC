"""Exact sign-twisted Euler cells and source-preserving Gamma readouts.

Analytic proofs are in TWISTED_DIGAMMA_BOUNDARY.md. These instruments use
Fraction intervals, never floating Gamma/digamma evaluations. The alternate
source sum is a different observable from the authentic BBP orbit character
sum. No normality, RH or geometric seam identification is certified here.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .bbp_source_memory import forcing
from .zero_one_gamma_bridge import (
    GammaBridgeError, RationalInterval, gamma_defect_interval,
)


def _q(value, positive=False):
    if type(value) not in (int, Q):
        raise GammaBridgeError("exact rational, never float/bool, required")
    value = Q(value)
    if positive and value <= 0:
        raise GammaBridgeError("positive rational required")
    return value


def _n(value, minimum=0, maximum=4096):
    if type(value) is not int or not minimum <= value <= maximum:
        raise GammaBridgeError("bounded integer required")
    return value


def beta_integer_second(a, k):
    """B(a,k+1)=k!/[a(a+1)...(a+k)], a rational positive, k>=0."""
    a = _q(a, True)
    _n(k)
    value = 1/a
    for j in range(1, k+1):
        value *= Q(j)/(a+j)
    return value


def alternating_reciprocal_prefix(a, count):
    """Finite sum of (-1)^n/(a+n), starting at n=0."""
    a = _q(a, True)
    _n(count)
    return sum((Q((-1)**n)/(a+n) for n in range(count)), Q())


def alternating_reciprocal_interval(a, depth=32):
    """Enclose F(a)=integral_0^1 t^(a-1)/(1+t) dt by positive Beta terms.

    Expanding 1/(1+t) around t=1 gives a geometric remainder between
    B(a,depth+1)/2^(depth+1) and B(a,depth+1)/2^depth.
    """
    a = _q(a, True)
    _n(depth)
    beta = 1/a
    prefix = Q()
    for k in range(depth):
        prefix += beta/2**(k+1)
        beta *= Q(k+1)/(a+k+1)
    return RationalInterval(prefix+beta/2**(depth+1),
                            prefix+beta/2**depth)


@dataclass(frozen=True)
class ReciprocalGammaWord:
    """Q(a+steps)=multiplier*Q(a)^power for Q(a)=Gamma((a+1)/2)/Gamma(a/2)."""
    origin: Q
    steps: int
    multiplier: Q
    power: int

    def apply(self, initial):
        initial = _q(initial, True)
        return self.multiplier*initial**self.power


def reciprocal_gamma_word(a, steps):
    """Exact iteration of q_(j+1)=(a+j)/(2*q_j), without evaluating Gamma."""
    a = _q(a, True)
    _n(steps)
    multiplier = Q(1)
    for j in range(steps):
        multiplier = (a+j)/(2*multiplier)
    return ReciprocalGammaWord(a, steps, multiplier, (-1)**steps)


def alternating_euler_interval(dilation=1, count=32, logarithm_terms=24):
    """Enclose A(d)=sum_(n>=1)(-1)^(n-1) delta(d*n), d>0.

    delta(x)=1/x-log(1+1/x) is strictly positive and decreasing. The
    alternating remainder has the next sign and magnitude <1/[2d²(N+1)²].
    At d=1 the exact analytic value is log(4/pi), not Euler gamma.
    """
    d = _q(dilation, True)
    _n(count)
    _n(logarithm_terms, 1, 250)
    result = RationalInterval(Q(), Q())
    for n in range(1, count+1):
        result = result.add(gamma_defect_interval(d*n, logarithm_terms)
                            .scale((-1)**(n-1)))
    bound = 1/(2*(d*(count+1))**2)
    tail = RationalInterval(Q(), bound) if count % 2 == 0 else RationalInterval(-bound, Q())
    result = result.add(tail)
    # Positivity follows independently from integral W(t)t^(d-1)/(1+t^d).
    return RationalInterval(max(Q(), result.lower), result.upper)


@dataclass(frozen=True)
class DyadicEulerCertificate:
    levels: int
    terms_per_level: int
    bands: tuple[RationalInterval, ...]
    prefix: RationalInterval
    tail: RationalInterval
    total: RationalInterval


def dyadic_euler_certificate(levels=8, count=32, logarithm_terms=24):
    """gamma=sum_(j<J)2^j A(2^j)+2^J sum_(n>=1)delta(2^j*n), j=J in tail.

    The omitted positive tail is <zeta(2)/(2*2^J)<5/(6*2^J).
    zeta(2)<5/3 follows from an elementary sum/integral bound (see proof).
    """
    _n(levels, 0, 64)
    _n(count)
    _n(logarithm_terms, 1, 250)
    bands = tuple(alternating_euler_interval(2**j, count, logarithm_terms).scale(2**j)
                  for j in range(levels))
    prefix = RationalInterval(Q(), Q())
    for band in bands:
        prefix = prefix.add(band)
    tail = RationalInterval(Q(), Q(5, 6*2**levels))
    return DyadicEulerCertificate(levels, count, bands, prefix, tail, prefix.add(tail))


def normalized_euler_interval(offset=0, *, levels=8, count=32, logarithm_terms=24):
    """Boundary value gamma-offset of H_N-log(exp(offset)*N).

    The offset is a declared normalization, not a change in Euler gamma.
    This routine does not evaluate exp(offset), and offset must be rational.
    """
    c = _q(offset)
    value = dyadic_euler_certificate(levels, count, logarithm_terms).total
    return RationalInterval(value.lower-c, value.upper-c)


def dyadic_finite_weights(levels, blocks=1):
    """Exact coefficients of a finite source-preserving dyadic telescope.

    Horizon=2^levels*blocks; every original Euler cell must retain weight1.
    The terminal tail cells are included, so dropping them is detectable.
    """
    _n(levels, 0, 12)
    _n(blocks, 1)
    horizon = 2**levels*blocks
    if horizon > 16384:
        raise GammaBridgeError("finite coefficient budget exceeded")
    weights = {n: Q() for n in range(1, horizon+1)}
    for j in range(levels):
        d = 2**j
        for n in range(1, horizon//d+1):
            weights[d*n] += d*(-1)**(n-1)
    d = 2**levels
    for n in range(1, blocks+1):
        weights[d*n] += d
    return weights


def bbp_alternating_interval(count=32):
    """Enclose sum_(n>=1)(-1)^(n-1)r(n), not a BBP Weyl average."""
    _n(count)
    prefix = sum(((-1)**(n-1)*forcing(n) for n in range(1, count+1)), Q())
    following = forcing(count+1)
    return (RationalInterval(prefix, prefix+following) if count % 2 == 0
            else RationalInterval(prefix-following, prefix))


def bbp_digamma_interval(depth=32):
    """Independent four-ray readout (1/8)*sum c_j F(a_j), rational intervals."""
    _n(depth)
    shifts = (Q(1,8), Q(1,2), Q(5,8), Q(3,4))
    coefficients = (4, -2, -1, -1)
    result = RationalInterval(Q(), Q())
    for c, a in zip(coefficients, shifts):
        result = result.add(alternating_reciprocal_interval(a, depth).scale(Q(c,8)))
    return result


def finite_resolvent_defect(values, multiplier):
    """For N+1 exact source values, bT_N-E T_N-f0=-b^-N fN.

    T_N=sum_(k<N)b^(-k-1)f_k. b=16 is the BBP backward multiplier;
    b=-1 gives the alternating resolvent. Those are distinct operators.
    """
    b = _q(multiplier)
    if not b or len(values) < 2:
        raise GammaBridgeError("nonzero multiplier and at least two source values required")
    source = tuple(_q(v) for v in values)
    count = len(source)-1
    current = sum((source[k]/b**(k+1) for k in range(count)), Q())
    following = sum((source[k+1]/b**(k+1) for k in range(count)), Q())
    return b*current-following-source[0], -source[-1]/b**count
