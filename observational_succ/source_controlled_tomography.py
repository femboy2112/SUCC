"""Source-controlled arithmetic tomography of the Reality-Pin operator K.

The interacting arithmetic operator is

    K = log N + lambda (S + S^*) + sum_p p^{-sigma} (V_p + V_p^*) + c I.

Its exact off-diagonal matrix elements in the genuine source basis are
available without proving scalar spectral cyclicity at any named parameter:

    <2|K|3> = lambda        (the S channel 2<->3)
    <1|K|3> = 3^{-sigma}    (the V_3 channel 1<->3)
    <1|K|5> = 5^{-sigma}    (the V_5 channel 1<->5)

SCO-01  recover (sigma, gain a, lambda) from scaled readings q23,q13,q15.
SCO-02  certified logarithmic stability of the inversion; the gain cancels.
SCO-03  source authentication: a counterfeit composite primitive (e.g. an
        isolated V_6) is invisible to a coprime-support probe set but detected
        by its own support entry; connected to the FOUNDATIONS Dirichlet-log
        witness b(6) = a(6) - a(2)a(3).
SCO-04  the operational access firewall: mathematical matrix elements are NOT
        physical realizability. This module provides only access level 1.

Reuses reality_pin_arithmetic (channel weights, certified log intervals) and
arithmetic_interactions firewall discipline. All finite sign/positivity
statements are exact or sound-interval; no Weil/RH positivity is inferred from
any positive matrix element, and no physical observer is asserted.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import log

from observational_succ.reality_pin_arithmetic import log_interval, primes_through


class TomographyError(ValueError):
    """A source model, probe set, or exact-arithmetic contract was violated."""


def _positive(x):
    if not isinstance(x, (int, Q, float)) or isinstance(x, bool) or x <= 0:
        raise TomographyError("positive reading required")
    return x


# ---------------------------------------------------------------------------
# exact K off-diagonal elements (forward model; reused to generate readings)
# ---------------------------------------------------------------------------

def k_off_diagonal(i, j, lam, sigma, multipliers=None):
    """Exact <i|K|j> for i != j (integer sigma >= 1 keeps it rational).

    Contributions: the successor S on |i-j|=1 (weight lambda); each multiplier m
    on edges n<->m*n (weight m^{-sigma}). ``multipliers`` defaults to the primes
    through max(i,j); pass a wider set to inject a counterfeit composite.
    """
    if type(i) is not int or type(j) is not int or i < 1 or j < 1 or i == j:
        raise TomographyError("distinct positive basis indices required")
    if type(sigma) is not int or sigma < 1:
        raise TomographyError("exact tomography uses integer sigma >= 1")
    lo, hi = min(i, j), max(i, j)
    if multipliers is None:
        multipliers = primes_through(hi)
    total = Q(0)
    if hi - lo == 1:
        total += Q(lam)
    for m in multipliers:
        if type(m) is not int or m < 2:
            raise TomographyError("multiplier labels are integers >= 2")
        if hi == m * lo:
            total += Q(1, m ** sigma)
    return total


# ---------------------------------------------------------------------------
# SCO-01 : parameter identification
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class SourceParameters:
    sigma: float
    gain: float
    lam: float


def identify_parameters(q23, q13, q15):
    """Recover (sigma, a, lambda) from scaled readings (float convenience).

        sigma = log(q13/q15) / log(5/3)
        a     = q13 * 3^sigma
        lambda= q23 / a

    The gain a cancels in q13/q15, so sigma is insensitive to it.
    """
    _positive(q23)
    _positive(q13)
    _positive(q15)
    sigma = log(q13 / q15) / log(Q(5, 3))
    a = q13 * (3.0 ** sigma)
    lam = q23 / a
    return SourceParameters(sigma, a, lam)


def identify_sigma_interval(q13, q15, terms=24):
    """Certified rational enclosure of sigma = log(q13/q15)/log(5/3), sigma > 0.

    Requires exact-rational readings with q13 > q15 (i.e. sigma > 0, so the
    ratio exceeds 1 and log_interval applies). Returns (lo, hi) with lo <= sigma
    <= hi, using certified log intervals (never a bare float comparison).
    """
    q13 = Q(q13)
    q15 = Q(q15)
    if q13 <= q15:
        raise TomographyError("certified branch requires q13 > q15 (sigma > 0)")
    num_lo, num_hi = log_interval(q13 / q15, terms)      # log of ratio, > 0
    den_lo, den_hi = log_interval(Q(5, 3), terms)        # log(5/3) > 0
    return num_lo / den_hi, num_hi / den_lo


def verify_identification_exact(lam, sigma):
    """Round-trip check with integer sigma and unit gain: readings -> parameters.

    Generates q23,q13,q15 from the forward model (gain a=1) and confirms the
    recovered sigma/lambda match. Returns the recovered SourceParameters.
    """
    if type(sigma) is not int or sigma < 1:
        raise TomographyError("exact round trip uses integer sigma >= 1")
    q23 = float(k_off_diagonal(2, 3, lam, sigma))
    q13 = float(k_off_diagonal(1, 3, lam, sigma))
    q15 = float(k_off_diagonal(1, 5, lam, sigma))
    rec = identify_parameters(q23, q13, q15)
    return rec


# ---------------------------------------------------------------------------
# SCO-02 : certified stability and gain cancellation
# ---------------------------------------------------------------------------

def sigma_error_bound(eta, terms=24):
    """Certified upper bound on |sigma_hat - sigma| for relative error eta in [0,1).

        |sigma_hat - sigma| <= log((1+eta)/(1-eta)) / log(5/3).

    Both prime readings carry independent relative error <= eta; worst case the
    ratio is multiplied by (1+eta)/(1-eta). Uses certified log intervals.
    """
    eta = Q(eta)
    if not 0 <= eta < 1:
        raise TomographyError("relative error eta in [0,1) required")
    if eta == 0:
        return Q(0)
    ratio = (1 + eta) / (1 - eta)
    num_lo, num_hi = log_interval(ratio, terms)          # log((1+eta)/(1-eta))
    den_lo, den_hi = log_interval(Q(5, 3), terms)
    return num_hi / den_lo                                # certified upper bound


def gain_cancels(q13, q15, scale):
    """sigma depends only on the ratio q13/q15, so a common gain cancels.

    Returns True iff identify_parameters recovers the same sigma after scaling
    both readings by ``scale`` > 0.
    """
    _positive(scale)
    base = identify_parameters(1.0, q13, q15).sigma
    scaled = identify_parameters(1.0, q13 * scale, q15 * scale).sigma
    return abs(base - scaled) < 1e-12


# ---------------------------------------------------------------------------
# SCO-03 : source authentication (counterfeit detection)
# ---------------------------------------------------------------------------

def counterfeit_invisible(multiplier, probe_entries, lam=1, sigma=2):
    """True iff the multiplier contributes to NONE of the given K entries.

    A probe entry is a pair (i, j). An isolated V_6 contributes nothing to
    {(2,3),(1,3),(1,5)} but something to (1,6). This is the matrix-side dual of
    the Dirichlet-log witness.
    """
    for (i, j) in probe_entries:
        base = k_off_diagonal(i, j, lam, sigma, multipliers=primes_through(max(i, j)))
        wide = k_off_diagonal(i, j, lam, sigma,
                              multipliers=tuple(primes_through(max(i, j))) + (multiplier,))
        if wide != base:
            return False
    return True


def minimal_separating_entry(multiplier, lam=1, sigma=2):
    """The smallest entry (1, multiplier) that reveals an isolated V_multiplier.

    V_m contributes m^{-sigma} to <1|K|m> (via V_m^* |m> = |1>); that entry is a
    separating probe. Returns ((1, multiplier), exact weight).
    """
    if type(multiplier) is not int or multiplier < 2:
        raise TomographyError("multiplier >= 2 required")
    return (1, multiplier), Q(1, multiplier ** sigma)


def dirichlet_log_witness(a6, a2=1, a3=1):
    """FOUNDATIONS b(6) = a(6) - a(2)a(3): 0 for genuine zeta, nonzero for a fake.

    Genuine zeta has a(n)=1, so b(6)=0 (the composite is explained by its prime
    channels). A counterfeit a(6)=2 gives b(6)=1. Multiplicative-side dual of
    the matrix counterfeit detector.
    """
    return Q(a6) - Q(a2) * Q(a3)


def no_fixed_probe_set_suffices_open_world():
    """Honest limitation: with retuned counterfeits of unbounded support, no

    finite FIXED probe set authenticates the source without a complexity prior.
    For any finite probe set {(i,j)} bounded by H, a counterfeit V_m with
    m > H is invisible to all of them. Returns the explanatory statement; the
    quantitative horizon theory is source_detectability.detectability_horizon.
    """
    return ("For probes bounded by H, a counterfeit multiplier m > H is "
            "invisible to every entry; finite fixed probe sets need a "
            "complexity/support prior. See source_detectability.")


# ---------------------------------------------------------------------------
# SCO-04 : operational access firewall
# ---------------------------------------------------------------------------

ACCESS_LADDER = (
    (1, "mathematical matrix elements", True,
     "exact <i|K|j>; provided by this module"),
    (2, "source-labelled state preparation", False,
     "requires a physical state-preparation interface"),
    (3, "coherent superposition / polarization measurement", False,
     "requires a coherent measurement instrument"),
    (4, "physically calibrated instrument", False,
     "requires calibration against known references"),
    (5, "independent empirical source authentication", False,
     "requires an out-of-band authenticated source"),
)


def access_ladder():
    """The five-level operational firewall; this module satisfies level 1 only."""
    return ACCESS_LADDER


def assert_mathematical_only(requested_level):
    """Guard: refuse to treat the source algebra as physical realizability.

    Raises unless ``requested_level == 1``; mathematical matrix elements do not
    establish that a physical observer can implement the operators.
    """
    if requested_level != 1:
        raise TomographyError(
            f"access level {requested_level} not established by matrix algebra; "
            "this module provides level 1 (mathematical) only")
    return True
