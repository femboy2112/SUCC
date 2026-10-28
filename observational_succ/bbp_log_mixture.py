"""Exact log-scale interfaces for the authentic BBP Gamma(shape 2) mixture.

The auxiliary probability measure is derived from the four-pole source. It is
not a distribution of actual arithmetic trajectories. Its logarithmic defect
does not certify cancellation of the selected circle orbit.

Paper proof: research/2026-10-26/OILY_MACARONI_SOURCE_BRIDGE.md.
All certificate endpoints use Fraction and proved logarithm/tail bounds.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb

from .bbp_natural_carrier import exact_forcing
from .euler_mascheroni_succ import rational_log_bounds
from .gamma_bbp_signed_coherence import green_tail_interval


# r(n) = sum v*d/[a*(a+d)], a=8*n-7.  No new source weights.
POLE_DIFFERENCES = ((3, 2), (4, 1), (5, 1))


def _integer(value, name, low=0, high=100000):
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f"{name}: integer in [{low}, {high}] required")
    return value


def _q(value, name, low=Q(0)):
    if type(value) not in (int, Q) or Q(value) < low:
        raise ValueError(f"{name}: exact rational >= {low} required")
    return Q(value)


def source_mixture_mass(n: int) -> Q:
    """Integral of the exact unnormalized Gamma-2 source density = r(n)."""
    _integer(n, "source index", 1)
    a = 8*n-7
    return sum((Q(v*d, a*(a+d)) for d, v in POLE_DIFFERENCES), Q())


def tail_base_moment(order: int) -> Q:
    """E[B**order] for dmu(B)=sum_j 16^-j sum_d v du, B=8j-7+u.

    The measure has total mass one. Geometric moments are evaluated by
    their exact recurrence, not truncated or supplied as numerical constants.
    """
    _integer(order, "moment order", 0, 16)
    ratio = Q(1, 16)
    geometric = []
    for k in range(order+1):
        geometric.append(ratio/(1-ratio) * (
            1+sum((comb(k, i)*geometric[i] for i in range(k)), Q())))
    total = Q()
    for k in range(order+1):
        interval_moment = sum((Q(v*d**(k+1), k+1)
                               for d, v in POLE_DIFFERENCES), Q())
        degree = order-k
        clock_moment = sum((comb(degree, i)*8**i*(-7)**(degree-i)*geometric[i]
                            for i in range(degree+1)), Q())
        total += comb(order, k)*interval_moment*clock_moment
    return total


def tail_jensen_bounds(n: int) -> tuple[Q, Q]:
    """1/(8n+7/2)^2 < T_n < 1/(8n+1)^2, n>=1 (paper proof)."""
    _integer(n, "tail index", 1)
    a = Q(8*n)
    return 1/(a+tail_base_moment(1))**2, 1/(a+1)**2


def tail_log_defect_bounds(n: int, log_terms: int = 24) -> tuple[Q, Q]:
    """All-n bounds for eta_n = E_n log(1+B/(8n)).

    max(log(1+1/a), E B/a - 3 E B^2/a^2) <= eta_n
      <= log(1+E B/a) <= E B/a, a=8n.
    The log endpoints below are outward rational enclosures.
    """
    _integer(n, "tail index", 1)
    _integer(log_terms, "log terms", 1, 200)
    a = Q(8*n)
    mean, second = tail_base_moment(1), tail_base_moment(2)
    lower, _ = rational_log_bounds(1+1/a, log_terms)
    _, upper = rational_log_bounds(1+mean/a, log_terms)
    return max(lower, mean/a-3*second/a**2), min(upper, mean/a)


def _log_integral_bounds(a: Q, start: Q, width: int,
                         log_terms: int) -> tuple[Q, Q]:
    # Integral_start^(start+width) log(1+b/a)/(a+b)^2 db.
    left, right = a+start, a+start+width
    ll, lu = rational_log_bounds(left/a, log_terms)
    rl, ru = rational_log_bounds(right/a, log_terms)
    return (1+ll)/left-(1+ru)/right, (1+lu)/left-(1+rl)/right


@dataclass(frozen=True)
class LogMixtureCertificate:
    n: int
    depth: int
    log_terms: int
    mass_lower: Q
    mass_upper: Q
    numerator_lower: Q
    numerator_upper: Q
    eta_lower: Q
    eta_upper: Q
    numerator_tail_upper: Q
    pi_normality_proved: bool = False


def tail_log_mixture_certificate(n: int, depth: int = 12,
                                 log_terms: int = 24) -> LogMixtureCertificate:
    """Finite exact certificate for T_n and eta_n, using no gamma or pi input.

    eta_n is the source-dependent difference between the Gamma-2 log mean
    1-gamma and the rescaled authentic tail law's log mean.
    """
    _integer(n, "tail index", 1)
    _integer(depth, "tail depth", 1, 300)
    _integer(log_terms, "log terms", 1, 200)
    a = Q(8*n)
    lo = hi = Q()
    for j in range(1, depth+1):
        for d, v in POLE_DIFFERENCES:
            lower, upper = _log_integral_bounds(a, Q(8*j-7), d, log_terms)
            lo += Q(v, 16**j)*lower
            hi += Q(v, 16**j)*upper
    # mu(j>depth)=16^-depth; B >= 8*depth+1 in that tail.
    # log(1+x)/(1+x)^2 <= x/(1+x)^2 <= 1/4.
    remainder = Q(1, 16**depth)*min(1/(4*a*a), 1/(a*(a+8*depth+1)))
    mass = green_tail_interval(n, depth)
    num_lo, num_hi = max(Q(), lo), hi+remainder
    global_lo, global_hi = tail_log_defect_bounds(n, log_terms)
    eta_lo = max(global_lo, num_lo/mass.upper)
    eta_hi = min(global_hi, num_hi/mass.lower)
    if eta_lo > eta_hi:
        raise ArithmeticError("inconsistent log-mixture bounds")
    return LogMixtureCertificate(n, depth, log_terms, mass.lower, mass.upper,
                                num_lo, num_hi, eta_lo, eta_hi, remainder)


def source_log_defect_interval(n: int, log_terms: int = 24) -> tuple[Q, Q]:
    """eta^r_n for the forcing law scaled by a=8n-7, not the tail law.

    eta^r_n = 1 - sum_d v log(1+d/a)/(a+d) / r(n).
    This identity uses the exact four-pole differences.
    """
    _integer(n, "source index", 1)
    _integer(log_terms, "log terms", 1, 200)
    a, lower, upper = Q(8*n-7), Q(), Q()
    for d, v in POLE_DIFFERENCES:
        lo, hi = rational_log_bounds(1+d/a, log_terms)
        lower += v*lo/(a+d)
        upper += v*hi/(a+d)
    mass = exact_forcing(n)
    return max(Q(), 1-upper/mass), 1-lower/mass


def tail_laplace_interval(n: int, s, depth: int = 12) -> tuple[Q, Q]:
    """E exp(-s*Y_n), Y_n=8n*T under the normalized tail density.

    Positive rational s is handled by the same exact Gamma-2 mixture.
    Classical limit is (1+s)^-2, not the Exp(1) transform (1+s)^-1.
    """
    _integer(n, "tail index", 1)
    _integer(depth, "tail depth", 1, 300)
    s = _q(s, "Laplace parameter")
    if s == 0:
        return Q(1), Q(1)
    a = Q(8*n)
    scaled = a*(1+s)
    numerator = Q()
    for j in range(1, depth+1):
        b = 8*j-7
        numerator += sum((Q(v,16**j)*(1/(scaled+b)-1/(scaled+b+d))
                          for d, v in POLE_DIFFERENCES), Q())
    remainder = Q(1,16**depth)/(scaled+8*depth+1)**2
    mass = green_tail_interval(n,depth)
    return numerator/mass.upper, min(Q(1),(numerator+remainder)/mass.lower)


def source_authentication_check(n: int) -> bool:
    """Algebraic equality, not authentication by a source-name string."""
    return source_mixture_mass(n) == exact_forcing(n)


def relative_mellin_loss_bound(n: int, frequency) -> Q:
    """Upper bound on 1-|E_n exp(-it log(1+B/(8n)))|^2.

    At fixed t the bound is summable in n, although the mean log phase is
    asymptotically 7/(16n). A common phase drift is not a modulus loss.
    """
    _integer(n, "tail index", 1)
    if type(frequency) not in (int,Q):
        raise ValueError("exact rational Mellin frequency required")
    t=Q(frequency)
    return min(Q(1),t*t*tail_base_moment(2)/Q((8*n)**2))


MATCHED_MOMENT_CONTROL = ((Q(1),Q(73,148)),(Q(89,15),Q(75,148)))


def counterfeit_moment(order: int) -> Q:
    """Two-atom hostile law; matches mu only through moment order two."""
    _integer(order,"control moment",0,16)
    return sum((weight*offset**order for offset,weight in MATCHED_MOMENT_CONTROL),Q())


def counterfeit_tail(n: int) -> Q:
    """Positive rational tail with identical first two mixing moments."""
    _integer(n,"control tail index",0,100000)
    return sum((weight/(8*n+offset)**2
                for offset,weight in MATCHED_MOMENT_CONTROL),Q())


def counterfeit_forcing(n: int) -> Q:
    _integer(n,"control forcing index",1,100000)
    return 16*counterfeit_tail(n-1)-counterfeit_tail(n)


def counterfeit_orbit(n: int) -> Q:
    """Zero-initialized source orbit with rational expanding coefficient.

    Its limiting phase orbit is periodic, so it is not equidistributed.
    It does NOT obey the authentic four-pole law; source comparison rejects it.
    """
    _integer(n,"control orbit index",0,10000)
    return 16**n*counterfeit_tail(0)-counterfeit_tail(n)
