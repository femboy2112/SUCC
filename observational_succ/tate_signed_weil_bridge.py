"""Tate source-window -> existing signed completed-Weil diagnostic adapter.

This adapter NEVER upgrades mpmath quadrature to a certified interval or
supposes the completed Weil form positive. It asserts genuine prime events
are contained in the exact Tate/SUCC support bound, then tests an explicit
counterfeit non-Euler n=6 impulse under the same Gamma/pole geometry.
"""
from __future__ import annotations

from fractions import Fraction as F

from .completed_weil_transport import (
    compact_weil_tent, tent_convolution,
)
from .diagonal_adele_zeta import rational
from .tate_weil_window import CompactWeilSourceWindow


def compare_signed_weil_tent(a: int | F = F(1), *, J: int = 6,
                             dps: int = 45, fake6: int | F = 1) -> dict:
    """Scoped signed Weil evaluation, NOT an all-test sign proof.

    Numerical comparisons use mpmath and are diagnostics only. The integer
    source-support upper bound itself is exact and proof-backed by e<3.
    """
    import mpmath as mp
    aa,mut=rational(a),rational(fake6)
    if not F(9,10) <= aa <= F(4) or mut<=0:
        raise ValueError("Mutant detection requires 0.9<=a<=4 and positive source mutation")
    if type(J) is not int or not 1<=J<=50 or type(dps) is not int or not 35<=dps<=150:
        raise ValueError("Finite analytic diagnostic J and working precision required")
    # For a>=0.9, 2a>=1.8>log(6) (true, not numerically proved here):
    # h(log 6)>0, hence the fake n=6 signed contribution cannot vanish.
    window=CompactWeilSourceWindow(aa).certificate()
    allowed={n for n,p in window["included_genuine_prime_power_labels"]}
    genuine=compact_weil_tent(aa,J=J,dps=dps)
    mutant=compact_weil_tent(aa,J=J,dps=dps,fake6=mut)
    if not genuine["genuine"] or mutant["genuine"]:
        raise AssertionError("Counterfeit must not be accepted as a genuine Euler source")
    if not set(genuine["prime_support"]).issubset(allowed):
        raise AssertionError("Completed signed source uses an uncertified prime impulse")
    if 6 in genuine["prime_support"]:
        raise AssertionError("Composite 6 is not a genuine von Mangoldt event")
    mp.mp.dps=dps
    # Test the actual signed difference on the same h=tent*tilde tent.
    impulse=-2*mp.mpf(str(mut.numerator))/mut.denominator*mp.log(6)/mp.sqrt(6)*tent_convolution(mp.log(6),aa)
    observed=mutant["q_ladder"]-genuine["q_ladder"]
    tolerance=mp.power(10,-max(10,dps-12))
    if not (abs(observed-impulse)<tolerance and impulse<0):
        raise AssertionError("Weil signed arithmetic mutation did not register as predicted")
    return {
        "a":aa, "source_cutoff":window["strict_integer_cutoff"],
        "prime_power_events_allowed":len(allowed),
        "original_prime_support":genuine["prime_support"],
        "genuine_source":genuine["genuine"],
        "fake6_source_is_not_genuine":not mutant["genuine"],
        "pole_term_numeric":str(genuine["pole"]),
        "prime_term_numeric":str(genuine["prime"]),
        "archimedean_ladder_numeric":str(genuine["arch_ladder"]),
        "genuine_total_numeric":str(genuine["q_ladder"]),
        "non_Euler_total_numeric":str(mutant["q_ladder"]),
        "predicted_non_Euler_signed_change":str(impulse),
        "measured_non_Euler_signed_change":str(observed),
        "numerical_comparison_error":str(abs(observed-impulse)),
        "arch_ladder_analytic_tail_bound_only":str(genuine["error_bound"]),
        "pole_Gamma_terms_retained":True,
        "half_density":F(1,2),
        "full_distributional_identification_proved_here":False,
        "numeric_sign_proven_by_rigorous_interval":False,
        "Weil_PSD_proved":False,
        "RH_proved":False,
    }
