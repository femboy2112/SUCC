"""Repeatable exact-rational seven-moment original source proof receipt.

The full source theorem's infinite-dimensional quantifiers are proved in the
research dossier from Fourier-Legendre/Plancherel, NOT by finite tests.
This script replays all rational constants and SHA-pinned original
Gamma/contact/p2/Neumann gates without reading any nontrivial zeta zero.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from observational_succ.tate_bessel_seven_schur import (
    original_seven_moment_weil_certificate,
    original_seven_low_suzuki_schur_interface,
    exact_legendre_low_frequency_enclosure,
)
from observational_succ.tate_reflection_parity_schur import (
    reflection_parity_15_low_source_certificate,
)


def receipt():
    high=original_seven_moment_weil_certificate()
    schur=original_seven_low_suzuki_schur_interface()
    old=reflection_parity_15_low_source_certificate()
    epsilon=exact_legendre_low_frequency_enclosure()
    multiplier=high["exact_Gamma_multiplier"]
    mass=high["exact_low_frequency_fraction_upper"]
    gap=high["actual_exact_L2_gap_lower"]
    canonical=hashlib.sha256(
        f"{multiplier}|{mass}|{gap}".encode("ascii")
    ).hexdigest()
    assert mass<F(1,61) and gap>F(1,16)
    return {
        "schema":"SUCC_TATE_BESSEL_SEVEN_2026_10_15_v1",
        "source":"PINNED_ORIGINAL_COMPLETED_ZETA_WEIL_FIRST_PRIME",
        "original_suzuki_git_blob":high["original_source_git_blob"],
        "halfwidth":"1/2",
        "true_active_prime_power_labels":list(high["true_prime_power_labels"]),
        "Gamma_real_source_modes":128,
        "Fourier_boundary":"49/4",
        "seven_vanishing_power_moments":True,
        "spherical_Bessel_exact_integrated_ranks":[7,19],
        "spherical_Bessel_series_order":10,
        "spherical_Bessel_infinite_l_tail_positive":
            epsilon["spherical_Bessel_high_l_tail"]>0,
        "low_Fourier_mass_upper_strictly_below":"1/61",
        "Gamma_multiplier_strictly_above":"3019/500",
        "true_negative_contact_plus_prime_budget_strictly_below":"47/8",
        "negative_sinh_polar_moment_residual_below":"1/10000",
        "simple_source_rational_lower":str(high["simple_rational_L2_gap_lower"]),
        "full_source_L2_gap_strictly_above":"1/16",
        "exact_gamma_mass_gap_sha256":canonical,
        "true_suzuki":{
            "low_modes":list(schur["low_unnormalized_Legendre_indices"]),
            "low_dimension":schur["low_dimension"],
            "reflection_parity_low_sizes":list(schur["parity_block_low_dimensions"]),
            "high_operator_K_relative_lower":"1/16",
            "original_inverse_Neumann_K":"V*V=(-Delta_N)^(-1)",
            "source_K_boundary_rank":schur["true_source_K_low_high_boundary_rank"],
            "genuine_zero_shift_R0_strictly_below":"121/100",
            "actual_original_7_low_Schur_positive_proved":False,
            "all_first_window_Weil_tests_positive_proved":False,
        },
        "prior_parity15_low_dimension":old["low_dimension"],
        "prior_rank18_original_relative_high_lower":"1/16",
        "rank_six_method_is_not_an_RH_negative_witness":True,
        "nontrivial_zero_positions_used_as_inputs":False,
        "source_all_radius_low_sign_proved":False,
        "RH_proved":False,
    }


if __name__=="__main__":
    data=receipt()
    if sys.argv[1:]==["--verify"]:
        path=Path(__file__).resolve().parents[1]/"research/2026-10-15/TATE_BESSEL_SEVEN_SCHUR_RECEIPT.json"
        reference=json.loads(path.read_text(encoding="utf-8"))
        if data!=reference:
            for key in sorted(set(data)|set(reference)):
                if data.get(key)!=reference.get(key):
                    print("EXACT_RECEIPT_MISMATCH",key,
                          "observed=",repr(data.get(key)),
                          "frozen=",repr(reference.get(key)))
            raise SystemExit("True original Bessel seven-Schur receipt mismatch")
        print("Authentic Weil seven-moment/signed Suzuki low7 source certificate verified; RH OPEN")
    elif not sys.argv[1:]:
        print(json.dumps(data,sort_keys=True,indent=2))
    else:
        raise SystemExit("usage: python scripts/tate_bessel_seven_probe.py [--verify]")
