"""Deterministic original-source + eta/Dirichlet proof ledger, no RH zeros.

Invoked on a complete checked-out branch with pinned APOLLO/DYSPON ancestry.
Only exact Fraction/int values enter the receipt. Numeric modular tests are
in the independent calibration suite, not this arithmetic certificate.
"""
import json
import sys
from pathlib import Path
from fractions import Fraction as F

from observational_succ.tate_eta_bernoulli import (
    bernoulli_heat_ledger, original_weil_margin_ablation,
    eta_modular_s_defect, eta_q_log_derivative_coefficients,
    eta_selfdual_first_jet,
    eta_eisenstein_prime_transducer, sigma_one_dirichlet_tail_majorant,
    primary_source_interface_status,
    modular_discriminant_formal_passport, completed_two_critical_track_passport
)


def frozen_receipt() -> dict:
    heat=bernoulli_heat_ledger()
    margin=original_weil_margin_ablation()
    good=eta_eisenstein_prime_transducer(64)
    bad=eta_eisenstein_prime_transducer(64, True)
    q=eta_q_log_derivative_coefficients(12)
    passport=primary_source_interface_status()
    delta=modular_discriminant_formal_passport(12)
    shifts=completed_two_critical_track_passport()
    return {
        "schema":"SUCC_TATE_ETA_BERNOULLI_2026_10_15_v3",
        "status":"CANONICAL_MODULAR_BRIDGE_NOT_RH",
        "bernoulli":{
            "zeta_minus_one":str(heat["zeta_of_minus_one"]),
            "canonical_eta_exponent":str(heat["canonical_eta_exponent"]),
            "heat_t2":str(heat["heat_laurent_t_squared"]),
            "ordinary_divergent_sum_not_equal_finite_value":True,
        },
        "Weil_source":{
            "parent":"SHA_PINNED_ORIGINAL_ZETA",
            "exact_conservative_margin":str(margin["original_source_lower"]),
            "one_over_24_certified":margin["one_twenty_fourth_works"],
            "one_over_22_certified":margin["one_twenty_second_works"],
            "one_over_21_certified_by_this_same_bound":False,
            "eta_exponent_equals_Weil_margin":margin["equal_to_eta_exponent"],
            "modular_origin_of_Weil_margin_claimed":False,
        },
        "eta_transport":{
            "canonical_nonfixed_S_defect_over_minus_pi":
                str(eta_modular_s_defect(F(1,24),F(1))["log_defect_over_minus_pi"]),
            "wrong_1_over_22_nonfixed_S_defect_over_minus_pi":
                str(eta_modular_s_defect(F(1,22),F(1))["log_defect_over_minus_pi"]),
            "wrong_exponent_selfdual_false_pass":
                eta_modular_s_defect(F(25,24),F(2))["self_dual_false_pass_possible"],
            "canonical_selfdual_first_jet":str(eta_selfdual_first_jet(F(1,24))["logarithmic_first_derivative_defect"]),
            "wrong_1_over_22_selfdual_first_jet":str(eta_selfdual_first_jet(F(1,22))["logarithmic_first_derivative_defect"]),
            "wrong_25_over_24_selfdual_first_jet":str(eta_selfdual_first_jet(F(25,24))["logarithmic_first_derivative_defect"]),
            "finite_q_constant":str(q[0]),
            "finite_q_coefficients_1_to_12":[str(x) for x in q[1:]],
        },
        "arithmetic_prime_transport":{
            "horizon":good["finite_horizon"],
            "normalization":"Gamma(s)*zeta(s)*zeta(s-1) for Re(s)>2",
            "authentic_transport_pass":good["transport_preserves_genuine_von_mangoldt"],
            "true_composite_6_basis":good["composite_six_residual_prime_log_basis"],
            "mutated_6_basis":{str(k):v for k,v in bad["composite_six_residual_prime_log_basis"].items()},
            "mutated_6_discriminated":6 in bad["mismatch_indices"],
            "analytic_tail_bound_sigma5_N16":str(sigma_one_dirichlet_tail_majorant(5,16)),
        },
        "two_track_firewall":{
            "Delta_cusp_coefficients_q1_through_q6":
                list(delta["Delta_q_coefficients_through_degree_N"][1:7]),
            "Delta_q_log_derivative_coefficients_constant_to_q6":
                list(delta["q_dlog_Delta_coefficients_through_degree_N_minus_one"][:7]),
            "E2_source_is_not_Ramanujan_tau_source":
                not delta["Delta_Ramanujan_tau_coefficients_are_sigma1"],
            "completed_shifted_object":shifts["completed_object"],
            "completed_shifted_functional_equation":shifts["functional_equation"],
            "conditional_two_critical_tracks":[str(k) for k in shifts["conditional_on_RH_two_real_tracks"]],
            "nontrivial_zero_locations_used":shifts["nontrivial_zero_locations_used_as_inputs"],
            "RH_proved":False,
        },
        "missing_interfaces":{
            "eta_archimedean":passport["eta_heat_archimedean"],
            "original_Weil_archimedean":passport["original_zeta_archimedean"],
            "full_Weil_identification":False,
            "source_derived_all_test_positivity":False,
            "RH_proved":False,
        },
    }


if __name__=="__main__":
    data=frozen_receipt()
    if sys.argv[1:]==["--verify"]:
        p=Path(__file__).resolve().parents[1]/"research/2026-10-15/TATE_ETA_BERNOULLI_RECEIPT.json"
        existing=json.loads(p.read_text(encoding="utf-8"))
        if data!=existing:
            raise SystemExit("Original-source eta transport proof receipt mismatch")
        print("TATE-ETA canonical normalization and prime-current proof receipt verified")
    elif not sys.argv[1:]:
        print(json.dumps(data,sort_keys=True,indent=2))
    else:
        raise SystemExit("usage: python scripts/tate_eta_bernoulli_probe.py [--verify]")
