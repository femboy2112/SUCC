"""Exact bounded controls for SUCC Simple/IdealHard/Fucked field gates.

Infinite noncomputability, compactness and no-continuous-selector theorems are
paper claims, not established by these tests of declared finite toy sources.
"""
import random
import unittest

from observational_succ.field_completion_gates import (
    DyadicGlobalCode, FieldGateError, FiniteGlobalSource, HaltTrace,
    antidiagonal_stage, antidiagonal_tree_member, stagewise_candidate_failure,
    noncompact_escape, phantom_target_receipt, delayed_discriminator,
)


class SimpleProgramControls(unittest.TestCase):
    def setUp(self):
        self.source = FiniteGlobalSource("integer-succ-seed", "standard-2-adic", "canonical-seed")

    def test_source_types(self):
        for args in (("", "b", "g"), ("s", "", "g"), ("s", "b", "")):
            with self.assertRaises(FieldGateError):
                FiniteGlobalSource(*args)
        with self.assertRaises(FieldGateError):
            FiniteGlobalSource("s", "b", 0)

    def test_finite_program_global_residue_coherence(self):
        for seed in (0, 1, -1, -7, 1927, 2**31 + 5):
            code = DyadicGlobalCode(self.source, seed)
            for fine in range(1, 14):
                for coarse in range(fine + 1):
                    r = code.coherence(fine, coarse)
                    self.assertTrue(r["bonding_verified"])
                    self.assertEqual(r["fine_residue"] % (2**coarse), r["coarse_residue"])
                    self.assertFalse(r["covers_all_2_adic_points"])

    def test_distinct_lifts_not_necessarily_distinguished_at_small_precision(self):
        small = DyadicGlobalCode(self.source, 3)
        large = DyadicGlobalCode(self.source, 3 + 2**18)
        for depth in range(19):
            self.assertEqual(small.residue(depth), large.residue(depth))
        self.assertNotEqual(small.residue(19), large.residue(19))

    def test_malformed_depths_and_seeds_rejected(self):
        with self.assertRaises(FieldGateError):
            DyadicGlobalCode(self.source, True)
        code = DyadicGlobalCode(self.source, 9)
        for depth in (True, -1, 4097, 0.5):
            with self.assertRaises(FieldGateError):
                code.residue(depth)
        with self.assertRaises(FieldGateError):
            code.coherence(1, 2)


class IdealHardFiniteShadows(unittest.TestCase):
    def test_diagonal_tree_stage_nonempty_by_explicit_witness(self):
        traces = (HaltTrace(0, 6, 0), HaltTrace(1, 2, 1),
                  HaltTrace(4, 3, 0), HaltTrace(10, 11, 1))
        for stage in range(13):
            r = antidiagonal_stage(stage, traces)
            self.assertTrue(r["stage_member"])
            self.assertEqual(len(r["chosen_prefix"]), stage)
            self.assertTrue(antidiagonal_tree_member(r["chosen_prefix"], traces))
            self.assertFalse(r["universal_noncomputable_path_theorem_executed"])
            # Any legal word has legal shorter prefixes.
            for sub in range(stage + 1):
                self.assertTrue(antidiagonal_tree_member(r["chosen_prefix"][:sub], traces))

    def test_late_information_kills_a_naively_chosen_old_prefix(self):
        traces = (HaltTrace(0, 4, 0), HaltTrace(2, 7, 1))
        early = antidiagonal_stage(2, traces)["chosen_prefix"]
        late = antidiagonal_stage(6, traces)["chosen_prefix"]
        self.assertEqual(early, (0, 0))
        self.assertEqual(late[:2], (1, 0))
        r = stagewise_candidate_failure(2, 6, traces)
        self.assertFalse(r["canonical_stage_choices_nested"])
        self.assertFalse(r["early_prefix_survives_at_late_stage"])
        self.assertFalse(r["global_nonexistence_inferred"])

    def test_late_information_without_a_forced_flip_is_not_a_negative_witness(self):
        traces = (HaltTrace(0, 4, 1),)
        r = stagewise_candidate_failure(2, 6, traces)
        self.assertTrue(r["canonical_stage_choices_nested"])
        self.assertTrue(r["early_prefix_survives_at_late_stage"])

    def test_tree_membership_mutation(self):
        traces = (HaltTrace(0, 1, 0),)
        self.assertTrue(antidiagonal_tree_member((1,), traces))
        self.assertFalse(antidiagonal_tree_member((0,), traces))
        self.assertTrue(antidiagonal_tree_member((), traces))
        self.assertTrue(antidiagonal_tree_member((0,), (HaltTrace(0, 2, 0),)))

    def test_source_trace_shape_guards(self):
        for args in ((True, 2, 0), (-1, 2, 0), (0, 0, 0), (0, 1, 2), (0, 1, True)):
            with self.assertRaises(FieldGateError):
                HaltTrace(*args)
        with self.assertRaises(FieldGateError):
            antidiagonal_stage(2, (HaltTrace(0, 2, 0), HaltTrace(0, 2, 1)))
        with self.assertRaises(FieldGateError):
            antidiagonal_tree_member((2,), ())
        with self.assertRaises(FieldGateError):
            antidiagonal_tree_member([0], ())
        with self.assertRaises(FieldGateError):
            antidiagonal_stage(True, ())
        with self.assertRaises(FieldGateError):
            stagewise_candidate_failure(4, 4, ())
        with self.assertRaises(FieldGateError):
            antidiagonal_stage(1, [HaltTrace(0, 1, 1)])

    def test_seeded_finite_trace_holdouts(self):
        r = random.Random(7391)
        for _ in range(80):
            seen = sorted(r.sample(range(12), r.randint(0, 5)))
            traces = tuple(HaltTrace(i, r.randint(1, 14), r.randint(0, 1)) for i in seen)
            n = r.randint(0, 12)
            word = antidiagonal_stage(n, traces)["chosen_prefix"]
            self.assertTrue(antidiagonal_tree_member(word, traces))
            for k in range(n):
                self.assertTrue(antidiagonal_tree_member(word[:k], traces))


class FuckedFieldControlModels(unittest.TestCase):
    def test_noncompact_all_finite_stages_nonempty_but_no_global_point(self):
        for n in (0, 1, 2, 16, 128, 4096):
            r = noncompact_escape(n)
            self.assertTrue(r["all_observed_stages_nonempty"])
            self.assertTrue(r["inverse_limit_empty"])
            self.assertEqual(r["diagonal_obstruction_stage"], n + 1)
            self.assertFalse(r["finite_stages_compact"])

    def test_noncompact_contract_fails_with_out_of_budget_input(self):
        for n in (-1, True, 4097):
            with self.assertRaises(FieldGateError):
                noncompact_escape(n)

    def test_phantom_source_collision_and_real_repair(self):
        dark = phantom_target_receipt()
        self.assertTrue(dark["same_all_current_reports"])
        self.assertFalse(dark["hidden_target_identifiable"])
        self.assertIsNotNone(dark["hidden_target_collision"])
        self.assertTrue(dark["public_target_identifiable"])
        self.assertFalse(dark["physical_authentication"])

        opened = phantom_target_receipt(add_separating_probe=True)
        self.assertFalse(opened["same_all_current_reports"])
        self.assertTrue(opened["hidden_target_identifiable"])
        self.assertIsNone(opened["hidden_target_collision"])
        self.assertTrue(opened["new_source_probe_was_added"])

    def test_delayed_eventual_difference_is_not_eternal_phantom(self):
        for depth in (0, 1, 100, 4096):
            r = delayed_discriminator(depth)
            self.assertEqual(r["first_difference"], depth+1)
            self.assertTrue(r["eventual_separation_exists"])
            self.assertFalse(r["all_depth_indistinguishability_inferred"])
        with self.assertRaises(FieldGateError):
            delayed_discriminator(-1)

    def test_source_target_relativization(self):
        w = phantom_target_receipt()
        self.assertFalse(w["hidden_target_identifiable"])
        self.assertTrue(w["public_target_identifiable"])
        self.assertFalse(w["model_only_recursion_can_separate_hidden_target"])


if __name__ == "__main__":
    unittest.main()
