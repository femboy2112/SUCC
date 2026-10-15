"""Classical source compactness theorem vs executable witness/uniqueness boundaries."""
import unittest

from observational_succ.field_limit_trichotomy import FieldLimitError
from observational_succ.field_limit_compactness import (
    classical_compact_fiber_theorem,finite_closed_cylinder_prefix,
    bounded_effective_path_prefix,idealhard_requires_multiple_paths,
    source_dependent_field_frontier,
)


class SourceIndexedFiniteIntersectionTests(unittest.TestCase):
    def test_true_compact_closed_fibers_give_only_conditional_global_existence(self):
        p=classical_compact_fiber_theorem()
        self.assertTrue(p.source_compact)
        self.assertTrue(p.observation_fibers_closed)
        self.assertTrue(p.source_separating)
        self.assertTrue(p.unique_if_realized)
        self.assertFalse(p.construction_algorithm_delivered)
        self.assertEqual(p.finite_intersection_property,
                         "ASSUMED_FOR_ALL_FINITE_SOURCE_SUBFAMILIES")
        self.assertFalse(p.RH_proved)

    def test_nested_finite_cantor_cylinders_are_mathematically_compatible(self):
        for words in (
            ((0,), (0,1), (0,1,0), (0,1,0,1)),
            ((), (1,), (1,0), (1,0,0)),
            ((1,1),),
        ):
            r=finite_closed_cylinder_prefix(words)
            self.assertTrue(r["finite_closed_fibers_have_nonempty_intersection"])
            self.assertFalse(r["finitely_verified_global_source"])
            self.assertFalse(r["infinite_nested_family_exists_as_declared_source"])
            self.assertFalse(r["RH_proved"])

    def test_forged_nested_source_fibers_or_untyped_reports_fail_closed(self):
        for history in (
            (),
            ((0,), (1,)),
            ((0,1),(0,)),
            ((0,True),),
            ((0,2),),
            ((0,), (0,0,0.5)),
            ("0",),
        ):
            with self.assertRaises(FieldLimitError):
                finite_closed_cylinder_prefix(history)


class EffectiveCompactnessAndInfiniteUniquenessTests(unittest.TestCase):
    def test_exact_unique_path_prefix_is_computable_with_legal_finite_probes(self):
        for n in (1,2,3,7,10):
            r=bounded_effective_path_prefix("unique-zero",n,11)
            self.assertEqual(r["prefix"],(0,)*n)
            self.assertEqual(r["agreed_level"],n)
            self.assertTrue(r["every_infinite_path_has_that_prefix"])
            self.assertFalse(r["global_uniqueness_from_finite_certificate"])
            self.assertFalse(r["RH_proved"])

    def test_delayed_second_global_source_keeps_early_prefix_identical(self):
        # Two incompatible complete paths can agree on first d bits.
        early=bounded_effective_path_prefix("two-branches",4,10,split_depth=5)
        self.assertEqual(early["prefix"],(0,0,0,0))
        self.assertFalse(early["global_uniqueness_from_finite_certificate"])
        ambiguous=bounded_effective_path_prefix("two-branches",6,10,split_depth=5)
        self.assertIsNone(ambiguous["prefix"])
        self.assertTrue(ambiguous["budget_exhaustion_does_not_disprove_existence"])

    def test_kleene_no_computable_path_forces_nonuniqueness_but_not_emptiness(self):
        t=idealhard_requires_multiple_paths()
        self.assertEqual(t["infinite_path_exists"],"CLASSICAL_KONIG_LEMMA")
        self.assertTrue(t["global_paths_not_unique"].startswith("PROVED"))
        self.assertTrue(t["every_path_noncomputable"].startswith("PROVED"))
        self.assertFalse(t["source_naturality_or_uniqueness_implies_RH"])
        r=bounded_effective_path_prefix("kleene",1,7)
        self.assertEqual(r["prefix"],(1,))
        self.assertFalse(r["global_uniqueness_from_finite_certificate"])

    def test_unsupported_tree_or_unbounded_source_search_does_not_infer_sign(self):
        for args in (
            ("fake",1,4),
            ("unique-zero",2,1),
            ("two-branches",1,13),
            ("kleene",True,8),
        ):
            with self.assertRaises(FieldLimitError):
                bounded_effective_path_prefix(*args)

    def test_RH_not_categorized_as_intrinsically_fucked_or_unprovable(self):
        d=source_dependent_field_frontier()
        self.assertEqual(d["RH_intrinsic_field_type"],"UNVERIFIED")
        self.assertEqual(d["Weil_positive_source_at_all_stages"],"UNVERIFIED")
        self.assertFalse(d["RH_proved"])


if __name__=="__main__":
    unittest.main()
