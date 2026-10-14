"""Exact wild-observer topology/probe-language controls. No 3D embedding fabricated."""
import unittest

from observational_succ import wild_embedding_probes as w


class AbstractSphereTests(unittest.TestCase):
    def test_exact_s2_chain_complex(self):
        s=w.intrinsic_double_cone()
        self.assertEqual((s["vertices"],s["edges"],s["faces"]),(6,12,8))
        self.assertEqual(s["Euler"],2)
        self.assertEqual(s["Betti_Q"],(1,0,1))
        self.assertFalse(s["ambient_embedding_certified"])
        self.assertFalse(s["exterior_pi1_computed"])

    def test_intrinsic_chart_cannot_be_exterior_witness(self):
        s=w.intrinsic_double_cone()
        self.assertEqual(s["Betti_Q"][1],0)
        self.assertNotIn("exterior_fundamental_group",s)


class MagnusProbeTests(unittest.TestCase):
    def test_free_reduction_and_inverse(self):
        self.assertEqual(w.reduce_word((1,2,-2,-1)),())
        self.assertEqual(w.reduce_word((1,2,-1)),(1,2,-1))
        self.assertEqual(w.reduce_word((1,2)+w.inverse_word((1,2))),())
        self.assertEqual(w.abelianization((1,1,2,-1,-2)),(1,0))
        with self.assertRaises(w.WildObserverError):
            w.reduce_word((1,3))

    def test_nonabelian_commutator_vanishes_under_abelianization(self):
        word=w.commutator((1,),(2,))
        self.assertEqual(word,(1,2,-1,-2))
        self.assertEqual(w.abelianization(word),(0,0))
        self.assertEqual(w.magnus_report(word,1),())
        self.assertEqual(w.first_visible_order(word,3),2)
        self.assertEqual(dict(w.magnus_report(word,2))[(0,1)],1)
        self.assertEqual(dict(w.magnus_report(word,2))[(1,0)],-1)

    def test_deep_nonabelian_witness_has_strict_information_horizon(self):
        for level in range(1,7):
            result=w.deep_commutator_receipt(level)
            self.assertEqual(result["abelianization"],(0,0))
            self.assertEqual(result["up_to_level"],())
            self.assertEqual(result["first_visible_degree"],level+1)
            self.assertEqual(result["leading_X_power_Y_coefficient"],1)
            self.assertTrue(result["proven_nonidentity_in_free_toy"])
            self.assertFalse(result["proven_actual_alexander_exterior_representation"])

    def test_exact_inverse_truncated_series(self):
        for depth in range(1,7):
            self.assertEqual(w.magnus_expansion((1,-1),depth),{():1})
            self.assertEqual(w.magnus_expansion((2,-2),depth),{():1})
            self.assertEqual(w.magnus_report(w.nested_commutator(depth),depth),())


    def test_independent_full_lie_binomial_oracle(self):
        for level in range(1,7):
            certificate=w.verify_full_magnus_leading_form(level)
            self.assertTrue(certificate["no_lower_order_signal"])
            self.assertTrue(certificate["full_free_lie_layer_matches"])
            self.assertEqual(certificate["nonzero_terms"],level+1)
            self.assertTrue(certificate["not_an_alexander_sphere_group_presentation"])

    def test_wrong_commutator_orientation_changes_the_source_phase(self):
        forward=w.commutator((1,),(2,))
        backward=w.commutator((2,),(1,))
        p=dict(w.magnus_report(forward,2))
        q=dict(w.magnus_report(backward,2))
        self.assertEqual(p[(0,1)],1)
        self.assertEqual(q[(0,1)],-1)
        self.assertNotEqual(p,q)

    def test_bad_generator_and_probe_precision_guards(self):
        for fn in (
            lambda:w.nested_commutator(2.0),
            lambda:w.nested_commutator(9),
            lambda:w.magnus_report((1,2,0),3),
            lambda:w.magnus_expansion((1,),10),
            lambda:w.first_visible_order((1,),0),
        ):
            with self.assertRaises(w.WildObserverError):
                fn()

    def test_noncommuting_words_are_not_3d_source(self):
        for depth in (1,2,3,4):
            self.assertNotEqual(w.nested_commutator(depth),())
            self.assertTrue(w.first_visible_order(w.nested_commutator(depth),depth+1)>1)


class PerfectGroupCalibration(unittest.TestCase):
    def test_small_solvable_target_cannot_be_perfect(self):
        s3=w.permutation_commutator_spectrum(3,even_only=False)
        self.assertEqual(s3["group_order"],6)
        self.assertEqual(s3["distinct_commutators"],3)
        self.assertFalse(s3["every_element_is_a_commutator"])

    def test_perfect_nonabelian_finite_groups_exist(self):
        a5=w.permutation_commutator_spectrum(5,even_only=True)
        self.assertEqual(a5["group_order"],60)
        self.assertEqual(a5["distinct_commutators"],60)
        self.assertTrue(a5["every_element_is_a_commutator"])

    def test_perfect_target_is_not_alexander_representation(self):
        # A5 merely illustrates a nontrivial perfect target group. No
        # homomorphism from Alexander's actual exterior is established.
        a5=w.permutation_commutator_spectrum(5,even_only=True)
        self.assertEqual(a5["group_order"],60)
        self.assertNotIn("horned_sphere_exterior_source",a5)

    def test_permutation_source_errors(self):
        with self.assertRaises(w.WildObserverError):
            w.permutation_commutator_spectrum(6)
        with self.assertRaises(w.WildObserverError):
            w.compose((0,1,2),(0,1))
        with self.assertRaises(w.WildObserverError):
            w.compose((0,0,1),(0,1,2))


if __name__=="__main__":
    unittest.main()
