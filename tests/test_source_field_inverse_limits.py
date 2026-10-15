"""Exact source-indexed inverse-limit/field taxonomy controls (NOT RH tests)."""
import unittest
from fractions import Fraction as F

from observational_succ.source_field_inverse_limits import (
    FieldClosureError, FieldSourcePassport, simple_residue_inverse_limit,
    finite_kleene_tree_calibration, noncompact_descending_field,
    hidden_coordinate_phantom, moving_impostor, remote_negative_sign_shadow,
    rh_inverse_limit_interface, original_weil_finite_gamma_sign_gap,
)


class SimpleFieldSourceLaw(unittest.TestCase):
    def test_one_finite_seed_provides_all_2adic_coordinate_queries(self):
        for seed in (0,1,5,1023):
            r=simple_residue_inverse_limit(seed,10)
            self.assertEqual(r["finite_name"],seed)
            self.assertEqual(r["field"],"SimpleField")
            self.assertTrue(r["uniform_requested_stage_algorithm"])
            self.assertTrue(r["global_compatibility_by_modular_identity"])
            self.assertFalse(r["all_infinite_coordinates_physically_executed"])
            for k,x in enumerate(r["observed_stages"]):
                self.assertEqual(x,seed%(1<<k))
            self.assertFalse(r["RH_proved"])

    def test_finite_name_is_not_unlimited_external_source_permission(self):
        with self.assertRaises(FieldClosureError):
            FieldSourcePassport("", "FULL")
        with self.assertRaises(FieldClosureError):
            FieldSourcePassport("SRC", "")
        for epoch in (-1,True,1.0):
            with self.assertRaises(FieldClosureError):
                FieldSourcePassport("SRC", "FULL",epoch)
        for seed,n in ((-1,8),(True,4),(1,65),(1,4.5)):
            with self.assertRaises(FieldClosureError):
                simple_residue_inverse_limit(seed,n)


class IdealHardKleeneConstruction(unittest.TestCase):
    halts=((0,1,0),(1,4,1),(3,7,0))

    def test_finite_law_is_prefix_closed_and_every_tested_level_nonempty(self):
        d=finite_kleene_tree_calibration(7,self.halts)
        self.assertEqual(d["levels_sizes"],(1,1,2,4,4,8,16,16))
        self.assertTrue(d["every_checked_level_nonempty"])
        self.assertTrue(d["every_checked_node_has_valid_prefix"])
        self.assertTrue(d["finitely_branching"])
        self.assertTrue(d["mathematical_infinite_theorem_requires_universal_U_and_WKL"])
        self.assertTrue(d["classical_universal_U_theorem_has_no_computable_path"])
        self.assertTrue(d["classical_universal_U_tree_has_infinite_path"])
        self.assertFalse(d["finite_transcript_proves_no_computable_path"])
        self.assertEqual(d["field_if_universal_U_and_WKL"],"IdealHard")
        self.assertTrue(all(s[0]=="1" and s[1]=="0" and s[3]=="1"
                            for s in d["last_level_nodes"]))
        self.assertFalse(d["RH_proved"])

    def test_finite_calibration_cannot_authenticate_a_universal_machine(self):
        d=finite_kleene_tree_calibration(4,())
        self.assertEqual(d["levels_sizes"],(1,2,4,8,16))
        self.assertFalse(d["finite_transcript_proves_no_computable_path"])
        self.assertEqual(d["source"],"SYNTHETIC_FINITE_BOUNDED_DIAGONAL_TRANSCRIPT")

    def test_malformed_diagonal_or_adversarial_sources_rejected(self):
        invalid=(
            ((0,1,0),(0,3,1)),
            ((0,0,0),),
            ((0,1,2),),
            ((True,1,0),),
            ((1,1.4,0),),
            ((1,1,False),),
            ("fake",),
        )
        for rec in invalid:
            with self.assertRaises(FieldClosureError):
                finite_kleene_tree_calibration(4,rec)
        for depth in (-1,True,12,2.0):
            with self.assertRaises(FieldClosureError):
                finite_kleene_tree_calibration(depth,())


class FuckedFieldBoundary(unittest.TestCase):
    def test_noncompact_tree_has_all_finite_levels_but_proved_no_path(self):
        for n in (0,1,2,3,17):
            c=noncompact_descending_field(n)
            self.assertEqual(len(c["finite_level_witness"]),n)
            self.assertEqual(c["finite_level_witness"],tuple(range(n-1,-1,-1)))
            self.assertTrue(c["all_finite_levels_have_such_witnesses"])
            self.assertFalse(c["branching_at_root_finite"])
            self.assertFalse(c["global_inverse_limit_nonempty"])
            self.assertEqual(c["field"],"FuckedField/PROVED_NO_REALIZATION")
            self.assertFalse(c["RH_proved"])

    def test_nonidentification_is_a_restricted_probe_not_nonexisting_source(self):
        for n in (1,3,12):
            d=hidden_coordinate_phantom(n)
            self.assertEqual(d["full_actual_prefix"],"00"*n)
            self.assertEqual(d["full_phantom_prefix"],"01"*n)
            self.assertTrue(d["even_reports_equal"])
            self.assertTrue(d["all_n_even_only_nonseparating_by_symbolic_source_law"])
            self.assertTrue(d["first_hidden_odd_probe_distinguishes"])
            self.assertTrue(d["full_projection_distinguishes_if_n_positive"])
            self.assertTrue(d["source_rule_allows_both_histories"])
            self.assertEqual(d["field"],"FuckedField/PROVED_OBSERVER_NONIDENTIFICATION")
            self.assertFalse(d["RH_proved"])

    def test_moving_finite_impostor_does_not_imply_one_permanent_phantom(self):
        for n in (0,1,8,64):
            d=moving_impostor(n)
            self.assertEqual(d["actual_prefix"],"0"*(n+1))
            self.assertEqual(d["moving_rival_prefix"],"0"*n+"1")
            self.assertEqual(d["reports_equal_up_to_depth"],n)
            self.assertEqual(d["next_full_prefix_separates"],n+1)
            self.assertTrue(d["forall_n_exists_rival_matching_first_n"])
            self.assertFalse(d["exists_one_fixed_rival_matching_all_prefixes"])
            self.assertTrue(d["full_prefix_observers_jointly_separate_points"])
            self.assertFalse(d["FuckedField_phantom_inferred"])
            self.assertFalse(d["RH_proved"])

    def test_remote_negative_has_eventual_finite_witness_not_permanent_phantom(self):
        for hidden in (0,1,10,257):
            blind=remote_negative_sign_shadow(hidden,hidden)
            visible=remote_negative_sign_shadow(hidden+1,hidden)
            self.assertTrue(blind["finite_compressions_appear_identical"])
            self.assertFalse(blind["negative_direction_is_visible"])
            self.assertFalse(visible["finite_compressions_appear_identical"])
            self.assertTrue(visible["negative_direction_is_visible"])
            self.assertTrue(visible["some_finite_distinguishing_observation_always_exists"])
            self.assertFalse(visible["permanently_invisible_negative_direction"])
            self.assertFalse(visible["RH_proved"])

    def test_distinguish_hard_missing_vs_diagnostic_unavailable(self):
        for fn,arg in ((noncompact_descending_field,-1),
                       (hidden_coordinate_phantom,1.1),
                       (moving_impostor,True)):
            with self.assertRaises(FieldClosureError):
                fn(arg)


class TateSuzukiToolRelativeTruth(unittest.TestCase):
    def test_real_negative_truncated_low_J2_can_be_rescued_by_true_Gamma_tail(self):
        d=original_weil_finite_gamma_sign_gap(2)
        self.assertEqual(d["source"],"ORIGINAL_PINNED_ZETA_WEIL_SUZUKI_LOW_LEGENDRE_1")
        self.assertEqual(d["a"],F(1,2))
        self.assertEqual(d["low_mode_L2_norm_squared"],F(1,3))
        self.assertEqual(d["omitted_Gamma_kernel_uniform_upper"],F(13,81))
        self.assertTrue(d["omitted_original_Gamma_tail_PSD"])
        self.assertTrue(d["truncated_stage_is_strictly_negative"])
        self.assertLess(d["original_truncated_low_rayleigh_interval"][1],0)
        self.assertLess(d["full_source_rayleigh_enclosure"][0],0)
        self.assertGreater(d["full_source_rayleigh_enclosure"][1],0)
        self.assertFalse(d["true_completed_low_mode_sign_decidable_from_this_stage"])
        self.assertFalse(d["mathematically_permanent_phantom_or_RH_counterexample_inferred"])
        self.assertEqual(d["field_label"],"UNRESOLVED_STAGE_TO_GLOBAL_SIGN")
        self.assertFalse(d["RH_proved"])
        with self.assertRaises(FieldClosureError):
            original_weil_finite_gamma_sign_gap(3)

    def test_actual_source_is_not_promoted_from_high_to_full_Weil_sign(self):
        result=rh_inverse_limit_interface()
        self.assertEqual(result["source"],"SHA_PINNED_ORIGINAL_COMPLETED_ZETA_WEIL_SUZUKI")
        self.assertEqual(result["first_prime_radius"],F(1,2))
        self.assertEqual(result["first_prime_legendre_high_rank"],18)
        self.assertTrue(result["first_prime_K_relative_high_coercivity_proved"])
        self.assertTrue(result["all_finite_radii_some_high_sector_coercivity_proved"])
        self.assertTrue(result["finite_stage_index_does_not_make_smooth_test_space_finite"])
        self.assertFalse(result["first_prime_actual_low_Schur_positive_certified"])
        self.assertFalse(result["all_radii_actual_low_Schur_positive_certified"])
        self.assertTrue(result["each_strict_negative_original_test_would_be_a_finite_mathematical_witness"])
        self.assertTrue(result["negative_witness_effectively_findable_requires_certified_dense_probe_enumeration"])
        self.assertFalse(result["uniform_finite_global_RH_positive_test_cutoff_proved"])
        self.assertEqual(result["field_classification"],"UNRESOLVED_TOOL_CLOSURE")
        self.assertTrue(result["not_authorized_to_label_RH_FuckedField"])
        self.assertFalse(result["RH_proved"])


if __name__=="__main__":
    unittest.main()
