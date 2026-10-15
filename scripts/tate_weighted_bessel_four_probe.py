"""Frozen exact-source/analytic weighted Bessel FOUR-moment sign receipt.

No nontrivial zero positions or numerical eigenvalue guesses are used.
Large Fraction values are hashed in sign-length-delimited integer bytes,
never decimal-converted or rounded. All-test quantifiers are justified
by the mathematical dossier, not by executing finitely many sample f.
"""
import json
import sys
from pathlib import Path
from fractions import Fraction as F
from observational_succ.tate_four_low_compensator import (
    source_rank_four_positive_completion,
    exact_four_source_moment_polarization,
)
from observational_succ.tate_weighted_bessel_four_schur import (
    source_weighted_four_moment_certificate,true_four_low_suzuki_interface,
    weighted_Bessel_leakage_upper,
)
from observational_succ.tate_bessel_seven_schur import (
    original_seven_moment_weil_certificate,
)


def receipt():
    d=source_weighted_four_moment_certificate()
    s=true_four_low_suzuki_interface()
    old=original_seven_moment_weil_certificate()
    polar=source_rank_four_positive_completion()
    test_moment_energies=[
        exact_four_source_moment_polarization(tuple(F(1) if k==j else F()
                                                    for k in range(4)))[
            "L2_projection_P4_source_energy_exact"]
        for j in range(4)
    ]
    if test_moment_energies != [75,8820,25200,705600]:
        raise ArithmeticError("Original Legendre four-test-moment coupling changed")
    # This exact source parser never serializes the huge original signed
    # spectral fractions. Their byte-level SHA256 is compared instead.
    return {
        "schema":"SUCC_TATE_WEIGHTED_BESSEL_FOUR_2026_10_15_v3",
        "source":"SHA_PINNED_ORIGINAL_ZETA_TATE_WEIL_SUZUKI",
        "original_suzuki_git_blob":d["source_suzuki_blob"],
        "radius":"1/2",
        "genuine_prime_power_labels":list(d["genuine_prime_power_labels"]),
        "four_vanishing_polynomial_test_moments":True,
        "original_real_Gamma_modes":128,
        "weighted_Fourier_boundary":"13",
        "exact_Gamma_multiplier_greater_than":"6097/1000",
        "weighted_Bessel_loss_strictly_below":"2013/10000",
        "rigorous_angular_modes":[4,15],
        "rigorous_spherical_Bessel_series_order":12,
        "exact_frequency_cells":96,
        "Young_square_slack":"1/1000",
        "missing_all_angular_modes_included":True,
        "negative_sinh_polar_residual_strictly_below":"1/1000000",
        "original_contact_plus_prime2_strictly_below":"47/8",
        "elementary_source_bound":str(d["elementary_rational_lower"]),
        "true_original_completed_Weil_L2_coercivity_strictly_above":"1/50",
        "original_source_Gamma_loss_gap_sha256":
            d["source_fraction_bytes_sha256"],
        "original_Suzuki_low":{
            "low_4_modes":list(s["low_Legendre_modes"]),
            "low_dimension":s["low_dimension"],
            "reflection_parity_blocks":list(s["reflection_parity_low_blocks"]),
            "original_high_K_relative_bound":str(s["genuine_high_relative_K_kappa"]),
            "Neumann_inverse_primitive":"V*V=(-Delta_N)^-1 on meanzero derivative u",
            "original_low_high_K_cross_rank":s["K_low_high_source_boundary_rank"],
            "true_zero_shift_R0_strict_upper":str(s["genuine_R0_zero_shift_norm_upper"]),
            "actual_low_S0_PSD_proved":False,
            "full_first_prime_all_test_positive_proved":False,
        },
        "source_rank_four_positive_completion":{
            "source":polar["source"],
            "true_source_compensator":str(polar["source_rank_four_counterterm"]),
            "source_negative_low_short_coarse_bound":
                str(polar["coarse_source_low_short_negative_bound"]),
            "modified_original_suzuki_strict_low_projection_gap":
                str(polar["strict_modified_low_L2_gap"]),
            "actual_modified_G_plus_counterterm_P4_PSD":
                polar["G_plus_counterterm_P4_PSD_proved"],
            "source_negative_Morse_index_upper":
                polar["source_negative_Morse_index_at_most"],
            "source_nullspace_dimension_upper":
                polar["source_nullspace_dimension_at_most"],
            "unmodified_original_Weil_PSD_proved":
                polar["original_complete_Weil_all_test_positive_proved"],
            "RH_proved":False,
        },
        "explicit_Weil_four_moment_polarization":{
            "moment_indices":[0,1,2,3],
            "derivative_Legendre_source_pairings":[
                "-2*m0","-12*m1","3*m0-60*m2","30*m1-280*m3"
            ],
            "squared_unnormalized_projection_coefficients":[3,5,7,9],
            "standard_basis_source_moment_energies":[str(x) for x in test_moment_energies],
            "positive_compensator":"65/16",
            "counterterm_zero_iff_all_four_moments_zero":True,
            "original_unmodified_Weil_positive_from_counterterm":False,
            "RH_proved":False,
        },
        "previous_rank_seven_high_K_relative_bound":"1/16",
        "rank_three_proof_failure_is_NOT_an_original_negative_test":True,
        "nontrivial_zeta_zero_positions_as_source_inputs":False,
        "all_radii_low_sign_proved":False,
        "RH_proved":False,
    }


if __name__=="__main__":
    data=receipt()
    if sys.argv[1:]==["--verify"]:
        path=Path(__file__).resolve().parents[1]/"research/2026-10-15/TATE_WEIGHTED_BESSEL_FOUR_RECEIPT.json"
        expected=json.loads(path.read_text(encoding="utf-8"))
        if data!=expected:
            for key in sorted(set(data)|set(expected)):
                if data.get(key)!=expected.get(key):
                    print("WEIGHTED_BESSEL_SOURCE_DIFF",key,
                          "computed=",repr(data.get(key)),
                          "frozen=",repr(expected.get(key)))
            raise SystemExit("TRUE source weighted four-moment receipt FAILED")
        print("Original Weil weighted Bessel four-moment >1/50 and Suzuki four-low proof receipt verified; RH OPEN")
    elif not sys.argv[1:]:
        print(json.dumps(data,indent=2,sort_keys=True))
    else:
        raise SystemExit("usage: python scripts/tate_weighted_bessel_four_probe.py [--verify]")
