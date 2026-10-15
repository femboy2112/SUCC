"""Reproducible zero-independent Tate local/global reflection-source receipt.

The machine checks exact Fraction outward-source interval properties and
analytic theorem interfaces. Infinitary Euler prime harmonic divergence,
the global Poisson functional equation and strip-wide convergence are
proved in the dossier, not by enumerating some finite sample.
"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from observational_succ.tate_central_reflection import (
    central_Gamma_Brownian_contact,
    reflected_local_prime_central_jet,
    original_finite_prime_reflection_slope,
    real_reflection_diodes, actual_center_high_prime_power_tail,
    high_jet_reflection_residual_contract,
    finite_prime_reflection_counterterm_tape,
    theta_selfdual_reflection_gauge,
    reflected_center_jet_offline_mutant,
)


def receipt():
    c=central_Gamma_Brownian_contact()
    p=original_finite_prime_reflection_slope(11)
    twisted=reflected_local_prime_central_jet(2,"chi_minus_3")
    high=actual_center_high_prime_power_tail(11)
    tail=high_jet_reflection_residual_contract(64,7)
    tape=finite_prime_reflection_counterterm_tape((2,3),2)
    gauge=theta_selfdual_reflection_gauge(F(1,4))
    wrong=theta_selfdual_reflection_gauge(F(1,2))
    mutant=reflected_center_jet_offline_mutant(3)
    if not (c["source_contact_C_infinity_interval"][0]>5 and
            c["source_contact_C_infinity_interval"][1]<F(43,8)):
        raise ArithmeticError("Original Brownian contact not imported")
    return {
        "schema":"SUCC_TATE_REFLECTION_JET_v1",
        "status":"TRUE_LOCAL_PRIME_GAMMA_CONTACT_NOT_RH_POSITIVITY",
        "source":"SHA_PINNED_ORIGINAL_ZETA_TATE_COMPLETED_WEIL",
        "center":{
            "s":"1/2",
            "Gamma_contact_between_5_and_43over8":True,
            "central_zeta_log_derivative_is_original_contact_over_two":
                c["source_contact_equals_twice_analytic_zeta_log_derivative"],
            "global_reflection_log_slope_is_original_C_infty":True,
            "zeta_half_nonzero_without_looking_up_zeros":
                c["zeta_half_nonzero_by_positive_alternating_eta"],
            "full_completed_Weil_sign_proved":False,
        },
        "finite_primes":{
            "prime_cutoff":11,
            "actual_prime_labels":list(p["actual_prime_labels"]),
            "each_local_reflection_exact_value_at_center":"1",
            "all_finite_stage_log_slopes_strictly_negative":
                p["finite_slope_is_strictly_negative"],
            "all_prime_raw_slope_to_minus_infinity":
                p["all_prime_raw_center_slope_diverges_to_negative_infinity"],
            "finite_samples_by_themselves_prove_divergence":False,
            "twisted_odd_chi3_at_p2_has_opposite_positive_slope":
                twisted["local_center_logarithmic_slope_interval"][0]>0,
            "ramified_p3_must_not_use_unramified_chart":True,
            "real_sigma_two_fifths_raw_product":
                real_reflection_diodes(F(2,5))["ordinary_all_prime_product_extended_limit"],
            "real_sigma_half_raw_product":
                real_reflection_diodes(F(1,2))["ordinary_all_prime_product_extended_limit"],
            "real_sigma_three_fifths_raw_product":
                real_reflection_diodes(F(3,5))["ordinary_all_prime_product_extended_limit"],
        },
        "prime_power_counterterms":{
            "true_source_tape":list((n,prime,str(weight))
                                    for n,prime,weight in tape[
                                        "source_coefficients_n_parent_and_exact_1overk"]),
            "fake_primitive_six":tape["primitive_composite_six_in_tape"],
            "high_power_k_three_plus_absolute":high[
                "k_at_least_three_all_prime_source_absolutely_convergent"],
            "first_two_prime_power_layers_diverge":high[
                "k_one_and_k_two_source_prime_sums_both_diverge"],
            "low_prime_jet_analytic_completion_by_high_tail_alone":False,
        },
        "renormalized_reflection_residual":{
            "vertical_real_strip":["1/4","3/4"],
            "prime_cutoff":64,
            "remove_prime_jet_orders_1_to":7,
            "remaining_jet_starts_at":8,
            "absolute_complex_log_tail_upper":str(tail[
                "complex_log_residual_tail_absolute_upper"]),
            "uniform_in_imaginary_height":tail["valid_for_every_imaginary_part"],
            "nonzero_reflection_and_center_phase":tail[
                "critical_line_residual_unit_modulus"],
            "analytic_zeta_ratio_from_raw_high_tail_alone":False,
        },
        "theta_half_density":{
            "log_heat_selfdual_weight":str(gauge["unique_exact_theta_selfdual_exponent"]),
            "correct_first_jet_zero":str(gauge[
                "log_reflection_ratio_slope_in_heat_log_coordinate"]),
            "wrong_one_half_weight_first_jet":str(wrong[
                "log_reflection_ratio_slope_in_heat_log_coordinate"]),
            "Poisson_source_fixes_weight":gauge["full_theta_log_kernel_even_for_all_x"],
        },
        "hostile_non_Euler_mutant":{
            "center_matching_derivatives_through_order":
                mutant["all_center_derivatives_through_order"],
            "preserves_zero_and_one_pole_residues":
                mutant["preserves_original_completed_pole_residues"],
            "source_offline_zeros":[str(z) for z in mutant["off_critical_line_zeros"]],
            "preserves_original_Euler_product":
                mutant["preserves_original_prime_Euler_multiplicativity"],
            "RH_not_proved_by_reflection_alone":True,
        },
        "RH_proved":False,
    }


if __name__=="__main__":
    data=receipt()
    if sys.argv[1:]==["--verify"]:
        file=Path(__file__).resolve().parents[1]/"research/2026-10-15/TATE_CENTRAL_REFLECTION_RECEIPT.json"
        if json.loads(file.read_text(encoding="utf-8"))!=data:
            raise SystemExit("Original Tate central reflection source receipt MISMATCH")
        print("TATE reflection prime-power jets / Brownian center / non-Euler controls VERIFIED (not RH)")
    elif not sys.argv[1:]:
        print(json.dumps(data,indent=2,sort_keys=True))
    else:
        raise SystemExit("usage: python scripts/tate_central_reflection_probe.py [--verify]")
