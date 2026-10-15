"""Frozen no-zero source receipt for APOLLO Brownian/prime determinacy.

Exact continuum rational checks + pinned authentic p=2/Gamma source.
The theorem is the proof dossier; the executable code is calibration.
"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from observational_succ.apollo_source_first_interference import (
    source_first_prime_interference, forced_Brownian_cancellation,
    normalized_birth_boundary_wells,true_prime_two_source_phase_triad,
    gamma_positive_first_Brownian_recovery,
    authentic_full_negative_feature_transfer_bound,
    finite_feature_graph_criterion,
)

def receipt():
    pre=source_first_prime_interference(F(1,4),F(3,4),1,
                                       ((0,F(1,8),1,0),))
    left=(-F(1,2),-F(3,8),2,0)
    inp=source_first_prime_interference(F(1,2),F(3,4),1,
                         (left,(F(1,4),F(3,8),2,0)))
    anti=source_first_prime_interference(F(1,2),F(3,4),1,
                         (left,(F(1,4),F(3,8),-2,0)))
    quad=source_first_prime_interference(F(1,2),F(3,4),1,
                         (left,(F(1,4),F(3,8),0,2)))
    real=true_prime_two_source_phase_triad()
    gamma=gamma_positive_first_Brownian_recovery(F(1,2))
    complete=authentic_full_negative_feature_transfer_bound(F(1,2))
    singular=finite_feature_graph_criterion(((1,0),(0,0)),((0,0),(0,1)))
    return {
        "schema":"SUCC_APOLLO_SOURCE_FIRST_INTERFERENCE_v1",
        "source_original_Euler_gamma_signed_Krein_without_zero_lookup":True,
        "synthetic_prebirth":{
            "source":"RATIONAL_CALIBRATION_NOT_TRUE_EULER",
            "positive_energy":str(pre["positive_prime_difference_energy"]),
            "forced_Brownian_energy":str(pre["forced_Brownian_subtraction_energy"]),
            "signed_energy":str(pre["signed_prime_energy"]),
            "correct_subtraction_coefficient":"2",
            "wrong_subtraction_three_ghost_factor":str(
                forced_Brownian_cancellation(F(1,4),F(3,4),1,3)["prebirth_signed_factor_per_w_norm"]),
        },
        "same_clock_phase_family":{
            "clock":"3/4","halfwidth":"1/2","source_weight":"1",
            "in_phase_energy":str(inp["signed_prime_energy"]),
            "anti_phase_energy":str(anti["signed_prime_energy"]),
            "quadrature_energy":str(quad["signed_prime_energy"]),
            "positive_source_recovers_Brownian_all_three":all(
                x["inverse_reconstruction_exact_on_every_piece"] for x in (inp,anti,quad)),
            "reconstruction_shift_steps":inp["finite_inverse_shift_steps"],
        },
        "true_prime_two":{
            "source":real["source"],
            "active_prime_powers":list(real["true_prime_power_labels"]),
            "weight_strictly_between_zero_and_half":
                0<real["true_half_density_weight_bounds"][0] and
                real["true_half_density_weight_bounds"][1]<F(1,2),
            "in_phase_prime_rayleigh":real["in_phase_prime_rayleigh"],
            "anti_phase_prime_rayleigh":real["anti_phase_prime_rayleigh"],
            "quarter_phase_prime_rayleigh":real["quarter_phase_prime_rayleigh"],
            "wavefront_is_mathematical_distribution_not_physical_motion":True,
        },
        "original_full_negative_graph":{
            "first_real_Gamma_L2_lower":str(gamma["Gamma0_L2_relative_lower"]),
            "true_active_prime_powers":list(complete["true_active_prime_powers"]),
            "unique_bounded_negative_feature_from_positive":
                complete["negative_feature_determined_by_positive_without_assuming_sign"],
            "graph_norm_squared_upper_gt_one":
                complete["source_positive_to_negative_graph_operator_norm_squared_upper"]>1,
            "unproved_source_contraction":
                not complete["RH_equivalent_all_windows_contraction_proved"],
            "forbidden_null_negative_feature_detected":
                not singular["Brownian_or_negative_feature_determined_by_positive"],
        },
        "moving_wavefront":{
            "m":5,
            "in_phase_signed":str(normalized_birth_boundary_wells(5)["in_phase_signed_prime_energy"]),
            "anti_phase_signed":str(normalized_birth_boundary_wells(5)["anti_phase_signed_prime_energy"]),
            "fixed_test_strong_limit_zero":True,
            "operator_norm_limit_zero":False,
        },
        "complete_original_Weil_all_tests_positive_proved":False,
        "RH_proved":False,
    }

if __name__=="__main__":
    d=receipt()
    if sys.argv[1:]==["--verify"]:
        p=Path(__file__).resolve().parents[1]/"research/2026-10-15/APOLLO_SOURCE_FIRST_INTERFERENCE_RECEIPT.json"
        if json.loads(p.read_text(encoding="utf-8"))!=d:
            raise SystemExit("APOLLO source-first receipt FAILED")
        print("APOLLO source-first prime/Brownian and original Gamma receipt verified; RH OPEN")
    elif not sys.argv[1:]:
        print(json.dumps(d,indent=2,sort_keys=True))
    else:
        raise SystemExit("usage: python scripts/apollo_source_first_interference_probe.py [--verify]")
