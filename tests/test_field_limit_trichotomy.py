"""Prove scoped Simple/IdealHard/Fucked observer-limit distinctions by exact controls."""
import unittest
from itertools import product

from observational_succ.field_limit_trichotomy import (
    FieldLimitError,FieldClassification,field_contracts,
    simple_symbolic_padic_one,_cantor_unpair,bounded_binary_turing_diagonal,
    kleene_source_tree_accepts,kleene_finite_stage,finite_prefix_versus_global_path,
    noncompact_escape_prefix,phantom_source_prefix,nonfaithful_toolkit_pair,
    effective_unique_compact_path_theorem,tate_rh_field_boundary,
)


class SourceRelativeSimpleFieldTests(unittest.TestCase):
    def test_symbolic_infinite_two_adic_source_is_finitely_executable_per_query(self):
        for n in (1,2,3,4,9,18,64,128,256):
            val=simple_symbolic_padic_one(n)
            self.assertEqual(val["value"],1)
            self.assertEqual(val["modulus"],2**n)
            self.assertTrue(val["finite_representation_not_finite_materialization"])
            self.assertFalse(val["whole_profinite_carrier_enumerated"])
            self.assertFalse(val["RH_proved"])
        for n in (0,-1,257,True,2.0):
            with self.assertRaises(FieldLimitError):
                simple_symbolic_padic_one(n)

    def test_effectively_compact_unique_path_is_computable_not_mystical(self):
        for n in (0,1,3,9,20,64):
            result=effective_unique_compact_path_theorem(n)
            self.assertEqual(result["only_infinite_path_prefix"],(0,)*n)
            self.assertTrue(result["unique_global_path"])
            self.assertTrue(result["finite_branching"])
            self.assertFalse(result["finite_uniform_bound_on_all_requested_bits_proved"])


class IdealHardEffectivePathTests(unittest.TestCase):
    def test_explicit_universal_machine_enumeration_and_bounded_halt(self):
        for e in range(64):
            a,b=_cantor_unpair(e)
            self.assertEqual((a+b)*(a+b+1)//2+b,e)
            self.assertGreaterEqual(a,0)
            self.assertGreaterEqual(b,0)
        self.assertEqual(bounded_binary_turing_diagonal(0,0),None)
        self.assertEqual(bounded_binary_turing_diagonal(0,1),0)
        with self.assertRaises(FieldLimitError):
            bounded_binary_turing_diagonal(0,-1)
        with self.assertRaises(FieldLimitError):
            bounded_binary_turing_diagonal(True,3)

    def test_computable_tree_has_nodes_at_every_checked_finite_level(self):
        for depth in range(0,13):
            report=kleene_finite_stage(depth)
            self.assertEqual(len(report["prefix"]),depth)
            self.assertTrue(report["finite_prefix_source_verified"])
            self.assertTrue(kleene_source_tree_accepts(report["prefix"]))
            for k in range(depth+1):
                self.assertTrue(kleene_source_tree_accepts(report["prefix"][:k]))
            self.assertFalse(report["infinite_stage_choice_algorithm_produced"])
            self.assertTrue(report["mathematical_witness_must_be_noncomputable"])

    def test_source_tree_prefix_closure_on_independent_exhaustive_short_words(self):
        for n in range(0,8):
            for word in product((0,1),repeat=n):
                if kleene_source_tree_accepts(word):
                    self.assertTrue(all(kleene_source_tree_accepts(word[:j])
                                        for j in range(n+1)))
        # TM_0 outputs 0 on input 0 in one step; source diagonal requires bit 0=1.
        self.assertFalse(kleene_source_tree_accepts((0,)))
        self.assertTrue(kleene_source_tree_accepts((1,)))

    def test_proved_global_existence_does_not_create_computable_selector(self):
        for n in (0,1,2,7,12):
            o=finite_prefix_versus_global_path(n)
            self.assertTrue(o["finite_membership_decidable"])
            self.assertTrue(o["mathematical_global_path_exists"])
            self.assertFalse(o["global_path_computable"])
            self.assertFalse(o["finite_symbolic_program_for_a_global_path"])
            self.assertEqual(o["classification"],"IDEALHARD_FOR_COMPUTABLE_PATH_SELECTOR")
            self.assertFalse(o["RH_proved"])


class FuckedFieldSourceBoundaries(unittest.TestCase):
    def test_noncompact_consistent_finite_prefixes_but_empty_global_limit(self):
        for n in (1,2,3,10,1000):
            o=noncompact_escape_prefix(n)
            self.assertEqual(o["finite_source_witness"],n)
            self.assertTrue(o["witness_satisfies_every_prior_stage"])
            self.assertTrue(o["individual_stages_nonempty"])
            self.assertFalse(o["infinite_source_limit_exists"])
            self.assertFalse(o["compact_Konig_hypotheses_satisfied"])
            self.assertFalse(o["RH_proved"])
        for n in (0,-1,True,1.5):
            with self.assertRaises(FieldLimitError):
                noncompact_escape_prefix(n)

    def test_infinite_profinite_ghost_is_not_an_original_integer_and_prefixes_alias(self):
        for n in (1,2,3,4):
            o=phantom_source_prefix(n)
            self.assertEqual(o["matching_integer_reports"],o["ghost_finite_source_reports"])
            self.assertFalse(o["one_original_integer_realizes_all_levels"])
            self.assertTrue(o["the_source_global_profinite_point_exists"])
            self.assertFalse(o["original_integer_source_property_finitely_refutable"])
            self.assertFalse(o["fixed_integer_and_ghost_equivalent_at_all_levels"])
            self.assertFalse(o["RH_proved"])
        self.assertEqual(phantom_source_prefix(4)["ghost_finite_source_reports"],
                         (1,3,9,105))
        for n in (0,5,True,1.0):
            with self.assertRaises(FieldLimitError):
                phantom_source_prefix(n)

    def test_true_forever_undistinguishable_fixed_sources_require_nonfaithful_toolkit(self):
        for n in (0,1,2,7,1000):
            d=nonfaithful_toolkit_pair(n)
            self.assertEqual(d["reports_after_selected_word"],(n%2,n%2))
            self.assertFalse(d["full_source_identity_recoverable"])
            self.assertTrue(d["repair_requires_new_source_authorized_tag_probe"])
            self.assertFalse(d["RH_proved"])
        for n in (-1,True,0.25):
            with self.assertRaises(FieldLimitError):
                nonfaithful_toolkit_pair(n)


class TrichotomyIsNotOneMagicalTruthScore(unittest.TestCase):
    def test_all_claim_ledger_axes_keep_computation_proof_uniqueness_apart(self):
        claims=field_contracts()
        self.assertEqual(len(claims),5)
        self.assertTrue(all(isinstance(v,FieldClassification) for v in claims))
        self.assertEqual(claims[0].classification,"SIMPLE")
        self.assertTrue(claims[0].computable_global_witness)
        self.assertEqual(claims[1].classification,"IDEALHARD")
        self.assertTrue(claims[1].proved_global_existence)
        self.assertFalse(claims[1].computable_global_witness)
        self.assertFalse(claims[2].proved_global_existence)
        self.assertTrue(claims[3].proved_global_existence)
        self.assertFalse(claims[3].source_identifiable_from_finite_reports)
        self.assertFalse(claims[4].source_identifiable_from_finite_reports)
        self.assertTrue(all(not v.RH_proved for v in claims))

    def test_relative_RH_frontier_cannot_be_labelled_intrinsically_fucked(self):
        d=tate_rh_field_boundary()
        self.assertEqual(d["global_adelic_Poisson_from_SUCC_primitives"],"UNVERIFIED")
        self.assertEqual(d["RH_fucked_field_intrinsic_status"],
                         "UNVERIFIED_NOT_CLASSIFIABLE_FROM_CURRENT_CLOSURE")
        self.assertFalse(d["RH_is_mathematically_unprovable"] is True)
        self.assertFalse(d["finite_symbolic_Tate_carrier_is_full_RH_proof"])
        self.assertFalse(d["RH_proved"])


if __name__=="__main__":
    unittest.main()
