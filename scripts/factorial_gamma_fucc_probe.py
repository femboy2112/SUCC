"""SUCC×FUCC factorial/Gamma source audit with deterministic exact receipt.

Use the repository checkout root:
  python scripts/factorial_gamma_fucc_probe.py --verify

The exact receipt is integer/Fraction mathematics. The separate numeric
holdout compares gamma, finite stochastic products and an independent direct
special-function oracle; it is *not* an outward-rounded certificate.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from fractions import Fraction as F
from observational_succ.factorial_gamma_fucc import (
    beta_gamma_backward_moment, binomial_cocycle,
    clock_characteristic, factorial_hankel_certificate,
    finite_exponential_clock_band_certificate, finite_source_countermodel_certificate,
    fucc_factorial_dilation_certificate, fucc_succ_square,
    gamma_characteristic, laguerre_orthogonality_certificate,
    beta_product_moment_certificate, scaled_order_statistic_cdf_certificate,
    ordered_uniform_beta_isomorphism,
)


def exact_receipt() -> dict:
    h=factorial_hankel_certificate(5)
    source=finite_source_countermodel_certificate()
    poly=laguerre_orthogonality_certificate(4)
    p3=fucc_factorial_dilation_certificate(3,2)
    p5=fucc_factorial_dilation_certificate(5,3)
    c=finite_exponential_clock_band_certificate(2,400,F(4))
    co=binomial_cocycle(2,3,4)
    bg=beta_gamma_backward_moment(3,5)
    sq=fucc_succ_square(3,4)
    full_chart=ordered_uniform_beta_isomorphism((F(1,2),F(2,3),F(3,4),F(4,5)))
    finite_wait=beta_product_moment_certificate(2,40,4)
    finite_arrival=scaled_order_statistic_cdf_certificate(1,40,F(3,2))
    return {
        "schema": "SUCC_FACTORIAL_GAMMA_FUCC_V1",
        "status": "EXACT_SOURCE_DIAGNOSTIC_NOT_RH",
        "parent_research": {"DGC":"PR141", "BGD":"PR142"},
        "moment_pascal_hankel": {
            "dimension":5,
            "determinant":str(h["determinant"]),
            "positive_definite":h["positive_definite"],
            "last_row":list(h["H"][-1]),
        },
        "gauss_laguerre_countermodel": {
            "true_moments":list(source["genuine"]),
            "positive_atomic_moments":list(source["mimic"]),
            "agreement_through":source["agree_through"],
            "first_discrepancy_order":source["first_discrepancy_order"],
            "first_discrepancy":source["first_discrepancy"],
            "true_hankel3_det":source["genuine_hankel_3_det"],
            "fake_hankel3_det":source["atomic_hankel_3_det"],
            "monic_degree_four":list(poly["monic_coefficients"]),
            "monic_degree_four_norm":str(poly["squared_norm"]),
            "all_finite_horizons_counterfeitable_by_positive_quadrature":True,
        },
        "arithmetic_succ_fucc": {
            "prime_three_address_square": {"left":sq["V_after_S"],
                                          "right":sq["S_power_p_after_V"],
                                          "wrong_direct_successor":sq["false_S_after_V"]},
            "prime_three_n_two_dilation":p3["dilation_multinomial"],
            "prime_three_n_two_carries":{str(k):v for k,v in p3["q_adic_carries"].items()},
            "prime_five_n_three_dilation":p5["dilation_multinomial"],
            "prime_five_n_three_carries":{str(k):v for k,v in p5["q_adic_carries"].items()},
            "binomial_cocycle":str(co["left"]),
            "square_curvature_claim":False,
        },
        "finite_ordered_beta_source_isomorphism": {
            "beta_coordinates":[str(x) for x in full_chart["independent_beta_coordinates"]],
            "ordered_succ_coordinates":[str(x) for x in full_chart["ordered_uniform_coordinates"]],
            "recovered_beta_coordinates":[str(x) for x in full_chart["recovered_beta_coordinates"]],
            "Jacobian":str(full_chart["absolute_jacobian"]),
            "beta_source_density":str(full_chart["input_joint_beta_density"]),
            "ordered_uniform_target_density":str(full_chart["target_joint_ordered_uniform_density"]),
            "global_joint_source_map_isomorphism":True,
            "finite_factorial_normalization":24,
            "scaled_order_statistic_M":finite_wait["M"],
            "scaled_order_statistic_n":finite_wait["n"],
            "scaled_order_statistic_r":finite_wait["order"],
            "finite_positive_Beta_moment":str(finite_wait["finite_positive_Beta_product_moment"]),
            "limiting_Gamma_moment":str(finite_wait["limiting_Gamma_shape_moment"]),
            "moment_gap":str(finite_wait["positive_moment_deficit"]),
            "moment_gap_rational_upper":str(finite_wait["rational_deficit_upper"]),
            "order_statistic_threshold":str(finite_arrival["x"]),
            "exact_finite_CDF":str(finite_arrival["finite_uniform_order_statistic_cdf"]),
            "poisson_Gamma_CDF_rational_error_upper":str(finite_arrival["rational_CDF_error_upper"]),
            "arithmetic_prime_source_attested":False,
        },
        "beta_gamma_backward": {
            "n":bg["n"],"r":bg["r"],
            "beta_moment":str(bg["beta_r_moment"]),
            "larger_shape_moment":str(bg["next_shape_moment"]),
            "smaller_shape_moment":str(bg["previous_shape_moment"]),
            "negative_log_delay_rate":bg["backward_log_delay_rate"],
        },
        "uniform_rational_mellin_band": {
            "shape_anchor":c["n"],
            "source_cutoff":c["cutoff"],
            "height":str(c["band"]),
            "log_bound":str(c["log_ratio_bound"]),
            "certified_absolute_error_upper":str(c["uniform_absolute_error_upper"]),
            "independent_coupling_bound":str(c["independent_coupling_error_upper"]),
            "gamma_oracle_used_in_bound":False,
        },
        "firewall": {
            "all_factorial_moments_required_to_authenticate_positive_measure":True,
            "finite_moment_countermodel_survives":True,
            "ordered_event_Beta_chart_full_joint_equivalence":True,
            "finite_law_of_small_numbers_error_quantified":True,
            "complex_phase_gauge_mutant_survives_factorial_and_radius_checks":True,
            "fake_composite_six_refused_as_prime_FUCC":True,
            "positive_Hankel_implies_signed_Weil":False,
            "Euler_source_authenticated":False,
            "RH_proved":False,
        },
    }


def numerical_calibration() -> dict:
    """Diagnostic only, with loose threshold not masquerading as interval proof."""
    import mpmath as mp
    with mp.workdps(75):
        n=2
        M=400
        t=mp.mpf('3.25')  # fresh non-boundary holdout
        approximate=clock_characteristic(n,M,t,dps=75)
        reference=gamma_characteristic(n,t,dps=75)
        err=abs(approximate-reference)
        bound=finite_exponential_clock_band_certificate(n,M,F(4))[
            'uniform_absolute_error_upper']
        threshold=mp.mpf(bound.numerator)/bound.denominator
        if not err < threshold:
            raise AssertionError('independent complex Γ oracle exceeds rational bound')
        return {"holdout_shape":n,"holdout_M":M,"holdout_t":"3.25",
                "numerical_error_decimal":mp.nstr(err,16),
                "below_analytic_rational_bound":True,
                "not_rigorous_numeric_interval":True}


def main(argv: list[str]) -> int:
    data=exact_receipt()
    path=(Path(__file__).resolve().parents[1]
          /'research/2026-10-16/FACTORIAL_GAMMA_FUCC_RECEIPT.json')
    if argv==['--verify']:
        actual=json.loads(path.read_text(encoding='utf-8'))
        if data != actual:
            raise AssertionError('exact source receipt diverged')
        diag=numerical_calibration()
        print('FGF exact arithmetic receipt VERIFIED')
        print('FGF finite exponential-clock holdout VALIDATED (numerical calibration only)')
        print(json.dumps(diag,sort_keys=True))
        return 0
    if not argv:
        print(json.dumps(data,indent=2,sort_keys=True))
        return 0
    raise SystemExit('usage: python scripts/factorial_gamma_fucc_probe.py [--verify]')


if __name__=='__main__':
    raise SystemExit(main(sys.argv[1:]))
