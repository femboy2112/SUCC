"""Certified rational enclosures for a constant-coefficient finite RC line.

The continuum ODE and identifiability proofs are in REALITY_PIN_CONTINUUM_LAYER.md.
Only a fixed, predeclared homogeneous line is covered. No experimental data,
variable-coefficient inverse problem, or physical source authentication.
"""
from fractions import Fraction as Q
from math import isqrt


class ContinuumError(ValueError):
    """Outside the stated source class or explicit computation budget."""


def _q(x):
    if type(x) not in (int, Q):
        raise ContinuumError("exact integer/Fraction required")
    return Q(x)


def _positive(x):
    x = _q(x)
    if x <= 0:
        raise ContinuumError("strictly positive source parameter required")
    return x


def exp_interval(x, width, max_terms=512):
    """Enclose exp(x), x>=0, with a geometric bound on the Taylor tail.

    Explicit cap prevents pretending an exhausted precision budget succeeded.
    """
    x, width = _q(x), _positive(width)
    if x < 0 or type(max_terms) is not int or max_terms < 2:
        raise ContinuumError("nonnegative argument and at least two terms required")
    if not x:
        return Q(1), Q(1)
    total, term = Q(1), Q(1)
    for n in range(1, max_terms):
        term *= x / n
        total += term
        ratio = x / (n+2)
        if ratio < 1:
            tail = term * x / (n+1) / (1-ratio)
            if tail <= width:
                return total, total+tail
    raise ContinuumError("Taylor term budget exhausted; no interval certificate")


def ratio_interval(z, width=Q(1, 10**10)):
    """Enclose h(z)=z*coth(z); use continuous h(0)=1."""
    z, width = _q(z), _positive(width)
    if z < 0:
        raise ContinuumError("nonnegative dimensionless depth required")
    if z == 0:
        return Q(1), Q(1)
    lo, hi = exp_interval(2*z, 2*z*width)
    # h decreases as E=exp(2z) increases; denominators are positive.
    return z*(hi+1)/(hi-1), z*(lo+1)/(lo-1)


def sqrt_interval(x, width):
    x, width = _q(x), _positive(width)
    if x < 0:
        raise ContinuumError("nonnegative square-root argument required")
    if x == 0:
        return Q(), Q()
    lo, hi = Q(), Q(isqrt(x.numerator // x.denominator)+1)
    while hi-lo > width:
        mid = (lo+hi)/2
        if mid*mid == x:
            return mid, mid
        if mid*mid < x:
            lo = mid
        else:
            hi = mid
    return lo, hi


def line_invariants(conductivity, capacity, length):
    """Complete response invariants (DC conductance, diffusion time scale)."""
    a, c, length = map(_positive, (conductivity, capacity, length))
    return a/length, c*length*length/a


def line_response_interval(conductivity, capacity, length, s, width=Q(1, 10**8)):
    g, tau = line_invariants(conductivity, capacity, length)
    s, width = _q(s), _positive(width)
    if s < 0:
        raise ContinuumError("nonnegative real Laplace parameter required")
    if s == 0:
        return g, g
    lo, hi = sqrt_interval(tau*s, width/(2*g))
    rlo = ratio_interval(lo, width/(4*g))[0]
    rhi = ratio_interval(hi, width/(4*g))[1]
    return g*rlo, g*rhi


def invert_ratio_interval(ratio, width=Q(1, 10**7)):
    """Enclose the unique positive z with z*coth(z)=ratio>1.

    Two interior trial points avoid relying on a possibly undecidable exact
    equality at a single midpoint. Strict monotonicity proves termination.
    """
    ratio, width = _positive(ratio), _positive(width)
    if ratio <= 1:
        raise ContinuumError("positive-depth homogeneous line requires ratio>1")
    lo, hi = Q(), ratio  # h(0)=1; h(ratio)>ratio.
    while hi-lo > width:
        p, q = (2*lo+hi)/3, (lo+2*hi)/3
        precision = min(Q(1), hi-lo)
        while True:
            hp = ratio_interval(p, precision)
            hq = ratio_interval(q, precision)
            if hp[1] < hq[0]:
                break
            precision /= 2
        if ratio > hp[1]:
            lo = p
        if ratio < hq[0]:
            hi = q
    return lo, hi


def known_capacity_pin(dc_conductance, capacity, s, ratio_band, z_width=Q(1, 10**7)):
    """Parameter bands with independently fixed c, g and positive s.

    ratio_band is synthetic or externally calibrated Y(s)/g. This routine
    cannot attest to that external calibration. Uncertain g,c require another
    error propagation step and are not treated as exact measured constants.
    """
    g, c, s = map(_positive, (dc_conductance, capacity, s))
    if len(ratio_band) != 2:
        raise ContinuumError("two ratio interval endpoints required")
    rlo, rhi = map(_q, ratio_band)
    if not 1 < rlo <= rhi:
        raise ContinuumError("ratio band must lie wholly above one")
    lo = invert_ratio_interval(rlo, z_width)[0]
    hi = invert_ratio_interval(rhi, z_width)[1]
    length = g*lo*lo/(c*s), g*hi*hi/(c*s)
    conductivity = g*length[0], g*length[1]
    return {"dimensionless_depth": (lo, hi), "length": length,
            "conductivity": conductivity, "physical_measurement_authenticated": False}
