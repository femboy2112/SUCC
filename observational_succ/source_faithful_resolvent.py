"""Exact a=2 source-resolved Schur witnesses and all-radix paper error budgets.

No floating point, no signed Weil identification, and no physical access claim.
Analytic Bloch theorems: research/2026-10-23/SOURCE_FAITHFUL_RESOLVENT_MEMORY.md.
"""
from fractions import Fraction as Q


class ResolventSourceError(ValueError):
    """A source fiber or quantitative-band hypothesis is invalid."""


def _q(x, positive=False):
    if type(x) not in (int, Q):
        raise ResolventSourceError("exact rational required")
    x = Q(x)
    if positive and x <= 0:
        raise ResolventSourceError("strictly positive rational required")
    return x


def radix_two_schur(alpha, spacing, cosine):
    """Exact uniform/alternating decomposition of the two-residue heat fiber.

    For z on the unit circle, c=Re(z), B=i Im(z)/h^2 up to orientation.
    Raw phase is not reconstructed from c; only |B|^2 and its Schur effect are.
    """
    alpha = _q(alpha, True)
    h = _q(spacing, True)
    c = _q(cosine)
    if not -1 <= c <= 1:
        raise ResolventSourceError("cosine must lie in [-1,1]")
    visible = (1-c)/h**2
    hidden = (3+c)/h**2
    coupling_squared = (1-c*c)/h**4
    correction = coupling_squared/(alpha+hidden)
    effective = alpha+visible-correction
    return {"visible_generator": visible, "hidden_generator": hidden,
            "coupling_squared": coupling_squared, "memory_correction": correction,
            "effective_denominator": effective, "visible_resolvent": 1/effective,
            "forgotten_memory_resolvent": 1/(alpha+visible)}


def uniform_band_budget(radix, spacing, radius, alpha_lower, alpha_upper):
    """Exact rational upper bounds from the all-radix analytic proof.

    h*a*R<=3 is a convenient rational sufficient condition for <=pi.
    alpha in [alpha_lower,alpha_upper], lost-weight bound <=1/2.
    """
    if type(radix) is not int or radix < 1:
        raise ResolventSourceError("positive exact integer radix required")
    h = _q(spacing, True)
    r = _q(radius)
    lo = _q(alpha_lower, True)
    hi = _q(alpha_upper, True)
    if r < 0 or hi < lo:
        raise ResolventSourceError("nonnegative radius and ordered alpha band required")
    constant = Q(radix*radix-1, 12)
    lost_weight = constant*h*h*r*r
    if lost_weight > Q(1, 2) or radix*h*r > 3:
        raise ResolventSourceError("low-frequency inversion hypotheses fail")
    resolvent = h*h*(constant*r*r/lo+r**4/(12*lo**2))
    inverse = h*h*(r**4/12+2*constant*r*r*(hi+r*r))
    memory = inverse+Q(radix**3, 12)*h*h*r**4
    return {"lost_weight_upper": lost_weight,
            "resolvent_error_upper": resolvent,
            "inverse_error_upper": inverse,
            "memory_error_upper": memory,
            "coarse_dispersion_upper": Q(radix**3, 12)*h*h*r**4}
