"""Tate/APOLLO arithmetic clock transducers: exact local forms and UV gates.

Mathematical domain: original zeta Weil form on C_c^infinity(-a,a);
half-density, prime weights, real Gamma, both poles and contact are pinned
to the APOLLO source.  No zero locations are inputs.  No all-a sign claim.

This module intentionally separates:
  * rational, source-independent shift-path and signed-hinge checks;
  * SHA-pinned original zeta first-prime source + exact rational proof budget.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .apollo_krein_factor import brownian_increment_kernel, prime_hinge_kernel
from .apollo_derivative_jets import _source, true_third_prime_wavefronts


class PrimeClockGateError(ValueError):
    """An illegal source/window/positivity assertion was attempted."""


def _q(value):
    if type(value) not in (int, Q):
        raise PrimeClockGateError("Only exact int/Fraction source inputs accepted")
    return Q(value)


def _positive(value):
    q = _q(value)
    if q <= 0:
        raise PrimeClockGateError("Positive source quantity required")
    return q


def shift_path_geometry(a, b):
    """Sharp compressed translation-chain theorem, in rational clock charts.

    For I=(-a,a), b>0, P_I(S_b+S_-b)P_I is a direct integral
    of finite path adjacency matrices.  Essential maximal chain length is
    m=ceil(2a/b); the sharp operator norm is 2*cos(pi/(m+1)).
    Do not replace the last exact expression by a floating certificate.
    """
    aa, bb = _positive(a), _positive(b)
    ratio = 2 * aa / bb
    m = (ratio.numerator + ratio.denominator - 1) // ratio.denominator
    return {
        "halfwidth": aa,
        "source_clock": bb,
        "length_ratio": ratio,
        "maximum_essential_chain_vertices": m,
        "prime_active": m >= 2,
        "sharp_norm_expression": f"2*cos(pi/{m+1})",
        "sharp_norm_rational": Q(0) if m == 1 else Q(1) if m == 2 else None,
        "general_norm_upper": Q(2),
        "RH_proved": False,
    }


def exact_two_cell_negative_witness(a, b, weight=1):
    """Exact four-point Gram witness attaining -weight in Brownian norm.

    Applicable when b < 2a <= 2b.  Its two positive indicator cells
    J and J+b each have length ell=(2a-b)/2.  The anchored four-point
    source coefficients are (1,-1,1,-1), with exact Q_prime=-2w*ell.
    Synthetic rational clocks are NEVER authenticated zeta primes.
    """
    aa, bb, ww = _positive(a), _positive(b), _positive(weight)
    if not bb < 2 * aa <= 2 * bb:
        raise PrimeClockGateError("A two-cell prime activation window is required")
    ell = (2 * aa - bb) / 2
    left = -aa
    right = left + bb
    points = (left + ell, left, right + ell, right)
    coeffs = (1, -1, 1, -1)

    def energy(kernel):
        return sum(
            (Q(coeffs[i] * coeffs[j]) * kernel(points[i], points[j])
             for i in range(4) for j in range(4)), Q()
        )

    signed = ww * energy(lambda x, y: prime_hinge_kernel(x, y, bb))
    brownian = energy(brownian_increment_kernel)
    if brownian != 2 * ell or signed != -2 * ww * ell:
        raise ArithmeticError("Exact prime path witness failed original hinge identity")
    return {
        "points": points, "coefficients": coeffs, "cell_length": ell,
        "original_shape_prime_signed_energy": signed,
        "brownian_energy": brownian,
        "sharp_relative_negative": signed / brownian,
        "synthetic_clock_not_genuine_prime": True,
        "RH_proved": False,
    }


def gamma_sparse_lower(dyadic_exponent, support_measure):
    """Exact analytic lower bound for first J=2^k real Gamma OU modes.

    If (4J-3)*mu<=2, Schur on measurable E of measure<=mu gives
    ||1_E R_alpha 1_E|| <= alpha*mu/2 <= 1/2 for j<J.
    Thus Q_Gamma >= sum_{j<J} 2/(4j+1) *||f||²
                > (1/2)log(4J+1)*||f||²
                > (k+2)/3 *||f||²,
    using log(2)>2/3 and 4J+1>2^(k+2).
    No sampled spectral eigenvalue or numerical transcendental value enters.
    """
    if type(dyadic_exponent) is not int or not 1 <= dyadic_exponent <= 128:
        raise PrimeClockGateError("A positive bounded integer exponent is required")
    mu = _positive(support_measure)
    J = 1 << dyadic_exponent
    if (4 * J - 3) * mu > 2:
        raise PrimeClockGateError("Source support does not resolve the chosen UV clock")
    return {
        "gamma_modes_used": J, "support_measure_bound": mu,
        "max_schur_ratio": Q(4 * J - 3, 4) * mu,
        "gamma_energy_strictly_above": Q(dyadic_exponent + 2, 3),
        "uncomputed_infinite_gamma_tail_is_positive": True,
        "all_smooth_tests_on_any_measurable_support_of_this_size": True,
        "RH_proved": False,
    }


def genuine_first_prime_sparse_weil_certificate(a=Q(1, 2),
                                                 support_measure=Q(1, 1 << 17)):
    """Source-derived genuine Weil coercivity for sparse supports.

    For 0<a<=1/2 and f in C_c^infinity(-a,a) supported on a measurable
    set of measure<=2^-17, Q_zeta(f) > (1/16)||f||² if f is nonzero.
    An actual prime 2 IS active at a=1/2.  This is not positivity for all
    tests on that interval and implies no RH conclusion.
    """
    aa, mu = _positive(a), _positive(support_measure)
    if aa > Q(1, 2) or mu > Q(1, 1 << 17):
        raise PrimeClockGateError("Only first-prime radius/support theorem certified")
    source = _source()  # pinned original Suzuki source SHA; no zeros
    if not source.contact_iv().hi < Q(43, 8):
        raise ArithmeticError("Authentic real contact C_inf<43/8 missing")
    if not source.log2_iv().lo > Q(2, 3):
        raise ArithmeticError("Authentic log 2 lower bound missing")
    if not source.log2_iv().hi < Q(7, 10):
        raise ArithmeticError("Authentic log 2 upper bound missing")
    labels = tuple(j.n for j in true_third_prime_wavefronts(2 * aa))
    if any(n != 2 for n in labels):
        raise ArithmeticError("Unexpected true prime-power activation")
    gamma = gamma_sparse_lower(16, mu)
    contact = Q(43, 8)
    # The original first-prime weight log(2)/sqrt(2)<1/2:
    # log2<7/10; sqrt2>7/5. Compressed shift path has <=2 vertices.
    prime = Q(1, 2)
    # 2(sinh(a)-a) <= 2(sinh(1/2)-1/2) < 1/16,
    # by sinh(t)-t <= t^3/[6(1-t^2)], t<=1/2.
    pole = Q(1, 16)
    lower = gamma["gamma_energy_strictly_above"] - contact - prime - pole
    if lower != Q(1, 16):
        raise ArithmeticError("Exact real Gamma/true-prime budget mismatch")
    return {
        "source": "SHA_PINNED_ORIGINAL_ZETA",
        "radius": aa, "actual_prime_power_labels": labels,
        "support_measure_max": mu, "gamma_clock_modes": 1 << 16,
        "gamma_strict_lower": gamma["gamma_energy_strictly_above"],
        "completed_real_contact_strict_upper": contact,
        "first_prime_shift_strict_upper": prime,
        "negative_pole_strict_upper": pole,
        "original_completed_Weil_L2_margin_strictly_above": lower,
        "quantifier": "all nonzero complex C_c^infinity tests with support measure <= bound",
        "prime_active_at_radius_half": aa == Q(1, 2) and labels == (2,),
        "all_tests_at_radius_half_proved": False,
        "all_a_positivity_proved": False,
        "RH_proved": False,
    }


def mutated_source_budget(delta_contact=0, extra_prime_weight=0):
    """EXPLICITLY SYNTHETIC mutation control; no true-source sign conclusion."""
    c = _q(delta_contact)
    w = _q(extra_prime_weight)
    baseline = Q(1, 16)
    return {
        "mutant_margin_from_same_conservative_budget": baseline - c - w,
        "negative_mutation_detected": baseline - c - w < 0,
        "authentic_source": False,
        "RH_proved": False,
    }
