"""Finite source tomography, with exact rational enclosures and explicit scope.

The paper proof in CAMBRIAN_E_ARITHMETIC.md identifies a finite Dirichlet-log
prefix from its causal ramp response. This code reconstructs one connected
coefficient from four rational response queries. It assumes a sound oracle
for the declared response; it does not authenticate an external source.
No zero positions, analytic continuation, or positivity inference are used.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial
from typing import Callable, Mapping

from .observer_reflection import RationalInterval as I
from .source_prime_certificates import rational_log_integer, rational_inverse_sqrt
from .adelic_theta_completion import centered_self_dual_gamma_multiplier
from .diagonal_adele_zeta import prime


class ArithmeticTransportError(ValueError):
    pass


def _rational(value: int | F) -> F:
    if type(value) not in (int, F):
        raise ArithmeticTransportError("Exact integer or Fraction required")
    return F(value)


def dirichlet_exp_prefix(connected: Mapping[int, int | F], horizon: int) -> tuple[F, ...]:
    """Independent finite convolution exp, inverse of the existing log adapter.

    Index zero is unused. The connected coefficient at 1 must be zero.
    Finite nilpotence follows because every nonidentity convolution factor
    has index >=2. This is exact formal algebra, not analytic exponentiation.
    """
    if type(horizon) is not int or not 2 <= horizon <= 256:
        raise ArithmeticTransportError("Finite horizon 2..256 required")
    b = tuple(_rational(connected[n]) for n in range(1, horizon + 1))
    if b[0] != 0:
        raise ArithmeticTransportError("Dirichlet logarithm has b(1)=0")
    base = (F(0),) + b
    power = [F(0)] * (horizon + 1)
    power[1] = F(1)
    answer = power[:]
    for r in range(1, horizon.bit_length()):
        nxt = [F(0)] * (horizon + 1)
        for d in range(1, horizon + 1):
            for k in range(2, horizon // d + 1):
                nxt[d * k] += power[d] * base[k]
        power = nxt
        for n in range(2, horizon + 1):
            answer[n] += power[n] / factorial(r)
    return tuple(answer)


def interior_clock_pair(j: int, *, log_terms: int = 24) -> tuple[F, F]:
    """Two certified rational points strictly between log(j) and log(j+1)."""
    if type(j) is not int or not 1 <= j <= 40:
        raise ArithmeticTransportError("Implemented interior clock labels 1..40")
    left = rational_log_integer(j, terms=log_terms).upper
    right = rational_log_integer(j + 1, terms=log_terms).lower
    if left >= right:
        raise ArithmeticTransportError("Insufficient log accuracy to separate events")
    return ((2 * left + right) / 3, (left + 2 * right) / 3)


def connected_from_four_queries(n: int, oracle: Callable[[F], I], *,
                                log_terms: int = 24, sqrt_places: int = 20) -> dict:
    """Enclose b(n) from the difference of slopes on adjacent event gaps.

    Contract: oracle encloses F_b(t)=-sum b(k)log(k)/sqrt(k)*(t-log(k))_+.
    The contract includes authentic event positions and half density.
    A wrong event phase or half density invalidates that assumption; the
    function then need not recover the declared coefficients. Oracle source
    identity and soundness are not established by this function.
    """
    if type(n) is not int or not 2 <= n <= 40:
        raise ArithmeticTransportError("Implemented tomography labels 2..40")
    before = interior_clock_pair(n - 1, log_terms=log_terms)
    after = interior_clock_pair(n, log_terms=log_terms)
    samples = tuple(oracle(t) for t in before + after)
    if any(not isinstance(x, I) for x in samples):
        raise ArithmeticTransportError("Sound rational interval oracle required")
    incoming = (samples[1] - samples[0]).scale(1 / (before[1] - before[0]))
    outgoing = (samples[3] - samples[2]).scale(1 / (after[1] - after[0]))
    jump = outgoing - incoming
    weight = rational_log_integer(n, terms=log_terms) * rational_inverse_sqrt(
        n, places=sqrt_places)
    if weight.lower <= 0:
        raise ArithmeticTransportError("Positive source normalization required")
    recovered = (-jump) * I(1 / weight.upper, 1 / weight.lower)
    return {"event": n, "times": before + after, "samples": samples,
            "incoming_slope": incoming, "outgoing_slope": outgoing,
            "slope_jump": jump, "coefficient_interval": recovered,
            "oracle_soundness_assumed": True,
            "source_authentication_claimed": False,
            "full_Weil_positivity_claimed": False}


def bounded_denominator_unique(interval: I, denominator_bound: int) -> bool:
    """At most one reduced rational with positive denominator <=D lies here.

    This does not assert that such a rational exists. Distinct such rationals
    differ by at least 1/D^2. The bound is sufficient, not necessary.
    """
    if not isinstance(interval, I) or type(denominator_bound) is not int or denominator_bound < 1:
        raise ArithmeticTransportError("Interval and positive denominator bound required")
    return interval.upper - interval.lower < F(1, denominator_bound ** 2)


def clock_distribution_countermodel(p: int, level: int) -> dict:
    """Projectively coherent p-adic Haar cylinders have UNBOUNDED Q_p norm.

    Uniform cylinder mass p^-r is normalized and additive under refinement,
    but its p-adic norm is p^r. It cannot define a bounded functional on
    continuous Q_p-valued functions equipped with the supremum norm.
    """
    if not prime(p) or type(level) is not int or not 1 <= level <= 12:
        raise ArithmeticTransportError("Genuine prime and finite level 1..12")
    coarse = F(1, p ** level)
    fine = F(1, p ** (level + 1))
    assert p * fine == coarse
    return {"prime": p, "level": level, "coarse_cylinder": coarse,
            "fine_cylinder": fine, "refinement_sum": p * fine,
            "total_mass": p ** level * coarse, "padic_operator_norm_lower_bound": p ** level,
            "uniformly_bounded_over_all_levels": False,
            "scope": "exact finite receipt plus universal unboundedness proof in dossier"}


def selfdual_offline_family(k: int, center_weight: int | F) -> dict:
    """Fresh exact DZ9 family: r=k^2 and 2<k*w<k+1/k.

    The quadratic y^2+k*w*y+1 has two negative roots, moduli R and R^-1
    with 1<R<k. Hence the normalized self-dual Mellin multiplier has
    extra zeros inside the strip and away from its center line.
    It is a mutation of the archimedean test; actual zeta is unchanged.
    """
    w = _rational(center_weight)
    if type(k) is not int or k < 2 or not F(2) < k * w < F(k) + F(1, k):
        raise ArithmeticTransportError("Require k>=2 and 2<k*w<k+1/k")
    a = k * w
    result = centered_self_dual_gamma_multiplier(F(k * k), w, 2)
    return {"k": k, "root_scale": k * k, "center_weight": w,
            "quadratic_constant_first": (F(1), a, F(1)), "discriminant": a * a - 4,
            "root_modulus_R_gt_1": a > 2,
            "root_modulus_R_lt_k": a < F(k) + F(1, k),
            "zeros_inside_strip_and_off_line": True,
            "source_multiplier_at_2": result["relative_to_standard"],
            "pole_normalization": (result["C0"], result["C1"]),
            "zero_formula": "1/2 +/- log(R)/log(k^2) + (2j+1)*pi*i/log(k^2)",
            "unknown_zeta_zero_positions_used": False,
            "classical_gaussian_Fourier_identity_assumed": True,
            "actual_riemann_zeta_changed": False}
