"""Deterministic finite receipts for the source-indexed field trilemma.

All reported finite objects are exactly computed. Classical Kleene/WKL and
all-real-radius statements are PAPER THEOREMS, never 'proved by the loop'.
No nontrivial zeta-zero location is read.
"""
import json
import sys
from pathlib import Path

from observational_succ.source_field_inverse_limits import (
    simple_residue_inverse_limit, finite_kleene_tree_calibration,
    noncompact_descending_field, hidden_coordinate_phantom,
    moving_impostor, remote_negative_sign_shadow,
    rh_inverse_limit_interface,
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
    return {
        "schema":"SUCC_SOURCE_FIELD_INVERSE_LIMIT_2026_10_15_v1",
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
