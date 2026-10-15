"""Finite Hilbert feature contraction / compact infinite gluing controls."""
import unittest
from fractions import Fraction as Q

from observational_succ.field_contractivity_compactness import (
    ContractiveDescentError, exact_finite_feature_contraction,
    unbounded_finite_growth_obstruction,
    compact_operator_constraint_lift_theorem,
    true_source_suzuki_contractivity_wall,
)


class ActualFiniteRationalContractionTests(unittest.TestCase):
    def test_exact_unique_prescribed_map_and_zero_orthogonal_extension(self):
        inputs=((1,0,0),(0,1,0),(1,1,0),(0,0,0))
        targets=((Q(1,2),0),(0,Q(1,3)),(Q(1,2),Q(1,3)),(0,0))
        o=exact_finite_feature_contraction(inputs,targets)
        self.assertTrue(o.signed_gram_psd)
        self.assertTrue(o.exact_source_equations_verified)
        self.assertTrue(o.exact_operator_contractivity_verified)
        self.assertEqual(o.rational_canonical_operator,
                         ((Q(1,2),0,0),(0,Q(1,3),0)))
        self.assertFalse(o.global_infinite_source_certified)
        self.assertFalse(o.RH_proved)

    def test_dependent_positive_features_still_yield_unique_prescribed_image(self):
        pos=((1,0),(2,0),(3,0),(0,0))
        neg=((Q(1,2),0),(1,0),(Q(3,2),0),(0,0))
        c=exact_finite_feature_contraction(pos,neg)
        self.assertTrue(c.signed_gram_psd)
        self.assertEqual(c.rational_canonical_operator,((Q(1,2),0),(0,0)))

    def test_finite_local_sign_without_cross_dominance_fails_exactly(self):
        # Source-positive each singleton, but incompatible prescribed images.
        c=exact_finite_feature_contraction(((1,0),(0,1)),((1,0),(2,0)))
        self.assertFalse(c.signed_gram_psd)
        self.assertIsNotNone(c.negative_principal_witness)
        self.assertFalse(c.exact_operator_contractivity_verified)
        self.assertIsNone(c.rational_canonical_operator)
        # v1=v2 but distinct target w1,w2: no single lawful source map.
        d=exact_finite_feature_contraction(((1,),(1,)),((1,),(0,)))
        self.assertFalse(d.signed_gram_psd)

    def test_zero_positive_source_cannot_transport_nonzero_negative(self):
        c=exact_finite_feature_contraction(((0,0),),((1,),))
        self.assertFalse(c.signed_gram_psd)
        good=exact_finite_feature_contraction(((0,0),),((0,),))
        self.assertTrue(good.signed_gram_psd)
        self.assertEqual(good.rational_canonical_operator,((0,0),))

    def test_rational_full_tmatrix_exact_bounds_not_floating_svd(self):
        inputs=((1,0),(0,1))
        targets=((Q(3,5),Q(4,5)),(-Q(4,5),Q(3,5)))
        o=exact_finite_feature_contraction(inputs,targets)
        self.assertEqual(o.rational_canonical_operator,
                         ((Q(3,5),-Q(4,5)),(Q(4,5),Q(3,5))))
        self.assertTrue(o.exact_operator_contractivity_verified)

    def test_bad_vector_types_and_source_label_refused(self):
        for P,M in (
            ((),()),
            (((1,2),),()),
            (((1.0,),),((1,),)),
            (((True,),),((0,),)),
            (((1,2),(1,)),((1,),(2,))),
        ):
            with self.assertRaises(ContractiveDescentError):
                exact_finite_feature_contraction(P,M)
        with self.assertRaises(ContractiveDescentError):
            exact_finite_feature_contraction(((1,),),((1,),),source="")


class HilbertOperatorCompactnessProofFirewallTests(unittest.TestCase):
    def test_norm_bound_not_merely_finite_solvability_is_essential(self):
        for n in (1,2,3,16,100):
            d=unbounded_finite_growth_obstruction(n)
            self.assertEqual(d["optimal_prefix_operator_norm"],n+1)
            self.assertTrue(d["one_bounded_operator_per_finite_prefix"])
            self.assertFalse(d["uniform_operator_bound_across_all_stages"])
            self.assertFalse(d["global_bounded_operator_exists"])
            self.assertFalse(d["RH_proved"])

    def test_uniform_finite_contraction_gives_global_exists_only_conditionally(self):
        d=compact_operator_constraint_lift_theorem()
        self.assertTrue(d["each_exact_constraint_WOT_closed"])
        self.assertEqual(d["global_solution"],"CLASSICAL_COMPACTNESS_CONDITIONAL_THEOREM")
        self.assertEqual(d["canonical_restriction_to_generated_positive_span"],
                         "UNIQUE_IF_SOLUTION_EXISTS")
        self.assertFalse(d["actual_Suzuki_all_finite_constraints_verified"])
        self.assertFalse(d["RH_proved"])

    def test_actual_arithmetic_source_is_not_a_fake_positive_gram(self):
        d=true_source_suzuki_contractivity_wall()
        self.assertEqual(d["authentic_Suzuki_source_relation"],"K_g=K_plus-K_minus")
        self.assertFalse(d["uniform_source_transports_for_all_a_proved"])
        self.assertFalse(d["all_finite_source_difference_grams_PSD"])
        self.assertFalse(d["WOT_compactness_can_replace_source_sign_proof"])
        self.assertFalse(d["RH_proved"])


if __name__=="__main__":
    unittest.main()
