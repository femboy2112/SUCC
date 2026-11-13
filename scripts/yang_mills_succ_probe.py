#!/usr/bin/env python3
"""Emit exact, bounded witnesses for the 2026-11-13 Yang--Mills/SUCC dossier."""

from fractions import Fraction as F
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.ym_phase_transport import (  # noqa: E402
    common_phase_comparison,
    target_reader,
    target_stability_bound,
)
from observational_succ.ym_reflection_bridge import (  # noqa: E402
    TaylorWilsonState,
    finite_hilbert_correlation,
    haar_moment,
    haar_moment_recurrence,
    haar_polynomial,
    hilbert_correlation,
    is_psd_exact,
    lattice_physical_mass_bounds,
    polynomial_product,
    quarter_turn_cos,
    reflection_matrix,
    toeplitz_matrix,
)


def receipt() -> dict:
    state = TaylorWilsonState(F(3, 2), 20)
    polynomials = ((1,), (0, 1), (0, 0, 1), (1, -2, 1))
    odd_square = haar_polynomial(polynomial_product(
        polynomial_product((1, -1), (1, -1)), (1, 3)))
    invisible = target_stability_bound(((1, 0), (0, F(1, 2))), ((0, 1),), F(1, 100))
    visible_rejected = False
    try:
        target_reader(((1, 0), (0, F(1, 2))), ((1, 0),))
    except ValueError:
        visible_rejected = True
    closing = [target_stability_bound(((1 - F(1, n),),), ((1,),), F(1, 2*n))
               for n in (2, 13, 1009)]
    result = {
        "schema_version": 1,
        "source_base": "db9fb4b84672050efa79b13377f1e73364598a14",
        "scope": "finite rational witnesses; universal claims have separate paper proofs",
        "full_upstream_lean_replayed": False,
        "yang_mills_continuum_reproduced": False,
        "yang_mills_mass_gap_proved": False,
        "pi_normality_proved": False,
        "su2_wilson": {
            "source": "one SU(2) plaquette with action 1-Tr(U)/2",
            "beta": state.beta,
            "taylor_order": state.order,
            "normalization": state.expectation((1,)),
            "trace_expectation": state.expectation((0, 1)),
            "trace_error_bound": state.error_bound(1),
            "gram_psd": is_psd_exact(state.gram(polynomials)),
            "two_moment_routes_agree_through_degree": 200,
            "moment_routes_agree": all(haar_moment(n) == haar_moment_recurrence(n)
                                       for n in range(201)),
            "odd_taylor_negative_square": odd_square,
        },
        "reflection": {
            "cosine_toeplitz_psd": is_psd_exact(toeplitz_matrix(quarter_turn_cos, (0, 1, 2, 3))),
            "cosine_reflected_one_point": reflection_matrix(quarter_turn_cos, (1,))[0][0],
            "hilbert_reflected_psd": is_psd_exact(reflection_matrix(hilbert_correlation,
                                                                    (0, 1, 2, 4, 7))),
            "finite_hilbert_N17_t3": finite_hilbert_correlation(17, 3),
            "hilbert_limit_t3": hilbert_correlation(3),
            "finite_hilbert_error_bound": F(1, 17),
            "physical_mass_bounds_at_spacing_1_100": lattice_physical_mass_bounds(F(1, 100)),
        },
        "phase_transport": {
            "sharp_factor_two": common_phase_comparison((2, -3), F(29, 4), (2, -1),
                                                          F(-9, 4), (2, 2), F(1, 4)),
            "invisible_resonance_reader": invisible,
            "visible_resonance_rejected": visible_rejected,
            "closing_margin_cases": closing,
        },
    }
    if not (result["su2_wilson"]["gram_psd"] and result["su2_wilson"]["moment_routes_agree"]
            and odd_square == -F(1, 4) and visible_rejected
            and result["reflection"]["cosine_reflected_one_point"] == -1
            and all(item["target_difference_bound"] == 1 for item in closing)):
        raise RuntimeError("a calibrated exact witness failed")
    return result


if __name__ == "__main__":
    print(json.dumps(receipt(), indent=2, default=str, sort_keys=True))
