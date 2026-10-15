"""Deterministic finite receipts for the source-indexed field trilemma.

All reported finite objects are exactly computed. Classical Kleene/WKL and
all-real-radius statements are PAPER THEOREMS, never 'proved by the loop'.
No nontrivial zeta-zero location is read.
"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from observational_succ.tate_finite_bruhat_observers import (
    finite_bruhat_chart, exact_tate_finite_plancherel,
    finite_tate_refinement_square, conductor_three_probe_gap,
)
from observational_succ.source_field_gluing import (
    recursive_positive_gram_stage, exact_scalar_schur_gluing,
    paired_neutral_source_birth,
)
from observational_succ.source_field_inverse_limits import (
    simple_residue_inverse_limit, finite_kleene_tree_calibration,
    noncompact_descending_field, hidden_coordinate_phantom,
    moving_impostor, remote_negative_sign_shadow,
    rh_inverse_limit_interface, original_weil_finite_gamma_sign_gap,
    finite_unique_path_selector,
)


def receipt():
    s=simple_residue_inverse_limit(5,6)
    i=finite_kleene_tree_calibration(7,((0,1,0),(1,4,1),(3,7,0)))
    no=noncompact_descending_field(5)
    phantom=hidden_coordinate_phantom(3)
    moving=moving_impostor(5)
    blind=remote_negative_sign_shadow(7,7)
    visible=remote_negative_sign_shadow(8,7)
    rh=rh_inverse_limit_interface()
    signed=original_weil_finite_gamma_sign_gap()
    synth=recursive_positive_gram_stage(4,F(1,2))
    valid=exact_scalar_schur_gluing(1,F(1,2),F(1,4))
    ghost=exact_scalar_schur_gluing(0,F(1,2),1)
    neutral=paired_neutral_source_birth(3,2,F(1,4))
    candidate=finite_unique_path_selector(3,11)
    solved=finite_unique_path_selector(3,12)
    local=finite_bruhat_chart(3,0,1)
    local_parseval=exact_tate_finite_plancherel(3,0,1,(0,1,-1))
    local_square=finite_tate_refinement_square(3,0,1,(0,1,-1))
    ramified=conductor_three_probe_gap()
    return {
        "schema":"SUCC_SOURCE_FIELD_INVERSE_LIMIT_2026_10_15_v5",
        "source_schemas_are_NOT_empirical_attestation":True,
        "simple":{
            "field":s["field"],
            "finite_name":s["finite_name"],
            "finite_stages":list(s["observed_stages"]),
            "finite_all_n_source_rule_certified":s["global_compatibility_by_modular_identity"],
            "physical_omega_execution":s["all_infinite_coordinates_physically_executed"],
        },
        "idealhard":{
            "finite_synthetic_tree_levels":list(i["levels_sizes"]),
            "prefix_closed":i["every_checked_node_has_valid_prefix"],
            "classical_universal_Kleene_no_computable_path":
                i["classical_universal_U_theorem_has_no_computable_path"],
            "classical_WKL_nonempty":i["classical_universal_U_tree_has_infinite_path"],
            "finite_synthetic_trace_is_universal_computer":False,
            "field_if_hypotheses":i["field_if_universal_U_and_WKL"],
        },
        "fucked_no_global":{
            "field":no["field"],
            "finite_level_witness":list(no["finite_level_witness"]),
            "finite_branching":no["branching_at_root_finite"],
            "global_path_exists":no["global_inverse_limit_nonempty"],
        },
        "fucked_phantom_observer":{
            "field":phantom["field"],
            "actual_full_stage":"000000",
            "phantom_full_stage":"010101",
            "reports_even_only":"000",
            "all_available_reports_equal":phantom["all_n_even_only_nonseparating_by_symbolic_source_law"],
            "new_odd_probe_separates":phantom["first_hidden_odd_probe_distinguishes"],
        },
        "quantifier_control":{
            "moving_actual_prefix":moving["actual_prefix"],
            "moving_alternative_prefix":moving["moving_rival_prefix"],
            "forall_n_different_finite_rival":moving["forall_n_exists_rival_matching_first_n"],
            "fixed_permanent_phantom":moving["exists_one_fixed_rival_matching_all_prefixes"],
        },
        "signed_operator_control":{
            "blind_at_seven":blind["finite_compressions_appear_identical"],
            "visible_at_eight":visible["negative_direction_is_visible"],
            "uniform_finite_visibility_bound":visible["uniform_cutoff_independent_of_hidden_index_exists"],
        },
        "true_low_mode_source_tail":{
            "source":signed["source"],
            "Gamma_J":signed["Gamma_finite_stage"],
            "signed_stage_strictly_negative":signed["truncated_stage_is_strictly_negative"],
            "missing_Gamma_tail_PSD":signed["omitted_original_Gamma_tail_PSD"],
            "omitted_Gamma_bound":str(signed["omitted_Gamma_kernel_uniform_upper"]),
            "full_original_source_sign_interval_straddles_zero":
                signed["full_source_rayleigh_enclosure"][0]<0<signed["full_source_rayleigh_enclosure"][1],
            "full_original_low_mode_sign_proved":False,
            "field_status":signed["field_label"],
            "RH_proved":False,
        },
        "recursive_global_positive_gluing":{
            "source":synth["source"],
            "finite_stage_n":synth["size_n"],
            "finite_to_global_positive_law":"G=(I+t*S)(I+t*S)* on ell2",
            "uniform_positive_gap":str(synth["uniform_infinite_positive_gap"]),
            "finite_stage_factorization_exact":synth["exact_factorization_G_equals_L_Lstar"],
            "all_n_prefix_compatibility_by_formula":synth["all_n_compatible_prefix_law_by_formula"],
            "physically_executed_infinitely_many_matrices":False,
            "synthetic_not_original_Weil":True,
        },
        "singular_source_schur":{
            "valid_rank_deficient_positive_block":valid["complete_block_PSD"],
            "valid_zero_schur":str(valid["true_schur_when_defined"]),
            "ghost_parent_range_failed":not ghost["cross_in_parent_range"],
            "ghost_negative_determinant":str(ghost["principal_determinant"]),
            "ghost_block_PSD":ghost["complete_block_PSD"],
            "paired_neutral_signed_old_and_new_equal":
                neutral["old_signed_source_value"]==neutral["new_signed_source_value"],
            "paired_features_both_changed":neutral["both_feature_carriers_changed"],
            "original_source_all_a_contraction":False,
        },
        "unique_effective_compact_selector":{
            "source":solved["source"],
            "requested_bit_index":solved["requested_bit_index"],
            "finite_budget_eleven_unresolved":
                not candidate["terminates_with_this_budget"],
            "finite_budget_twelve_computes_bit":solved["terminates_with_this_budget"],
            "computed_bit":solved["bit_value"],
            "finite_agreement_proves_bit":solved["finite_prefix_agreement_is_a_proof_of_this_bit"],
            "math_theorem":"unique path of decidable infinite binary tree is computable",
            "unknown_depth_does_not_imply_noncomputable_path":True,
            "RH_proved":False,
        },
        "actual_finite_Tate_local_chart":{
            "source":local["source"],
            "prime":local["p"],
            "support_M":local["support_exponent_M"],
            "constancy_N":local["constancy_exponent_N"],
            "finite_complex_dimension":local["finite_complex_dimension"],
            "Haar_cell":str(local["input_additive_Haar_cell"]),
            "input_L2_squared":str(local_parseval["input_exact_L2_squared"]),
            "dual_L2_squared":str(local_parseval["dual_exact_L2_squared"]),
            "Fourier_inversion_and_isometry_exact":local_parseval[
                "isometry_certified_by_character_orthogonality"],
            "both_refinement_Fourier_squares_commute":
                local_square["support_refinement_dual_constancy_square"] and
                local_square["constancy_refinement_dual_support_square"],
            "Schwartz_Bruhat_test_direct_limit":local_square[
                "direct_limit_of_all_finite_Schwartz_Bruhat_charts"],
            "carrier_Qp_has_infinite_points":local["entire_local_Qp_has_infinitely_many_points"],
            "all_complex_coefficients_computable":local[
                "all_complex_coefficients_automatically_computable"],
            "actual_ramified_chi3_coarse_unit_zero":
                str(ramified["true_coarse_unit_observation"]),
            "actual_ramified_chi3_fine_Fourier_phase":"sqrt(-3)/3",
            "actual_ramified_chi3_phase_norm_squared":
                str(ramified["fine_phase_norm_squared"]),
            "full_Weil_sign_proved":False,
            "RH_proved":False,
        },
        "original_Weil_RH_frontier":{
            "source":rh["source"],
            "first_prime_high_K_positive":rh["first_prime_K_relative_high_coercivity_proved"],
            "all_fixed_radii_some_high_K_positive":rh["all_finite_radii_some_high_sector_coercivity_proved"],
            "all_radii_low_short_positive":rh["all_radii_actual_low_Schur_positive_certified"],
            "finite_stage_smooth_tests_are_finite":False,
            "RH_classified_by_this_calculus":rh["field_classification"],
            "RH_proved":False,
        },
    }


if __name__=="__main__":
    d=receipt()
    if sys.argv[1:]==["--verify"]:
        p=Path(__file__).resolve().parents[1]/"research/2026-10-15/SOURCE_FIELD_INVERSE_LIMIT_RECEIPT.json"
        expected=json.loads(p.read_text(encoding="utf-8"))
        if d!=expected:
            raise SystemExit("SOURCE-FIELD inverse-limit exact receipt mismatch")
        print("Source-field inverse limit receipts verified, RH sign UNVERIFIED")
    elif not sys.argv[1:]:
        print(json.dumps(d,indent=2,sort_keys=True))
    else:
        raise SystemExit("usage: python scripts/source_field_inverse_limit_probe.py [--verify]")
