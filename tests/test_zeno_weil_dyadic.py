"""SUCC's signed Weil source interpreted as a quantified dyadic Zeno rate."""
import unittest
from fractions import Fraction as Q
from observational_succ import zeno_weil_dyadic as z
from observational_succ import source_weil_hierarchy as source


class GenuineDyadicWeilTests(unittest.TestCase):
    def test_schedule_all_sources_and_shapes(self):
        for k in range(1,10):
            p=z.dyadic_stage(Q(1,2),k)
            self.assertEqual(p["Gamma_modes"],2**k)
            self.assertEqual(p["cell_count"],4**k)
            self.assertEqual(p["finite_Zeno_clock"],1-Q(1,2**k))
            self.assertEqual(p["original_source"],
                             "AUTHENTIC_ZETA_PRIME_POWER_GAMMA_POLE_HALF_DENSITY")
            self.assertFalse(p["rh_proved"])
            self.assertFalse(p["negative_depth_vanishes_proved"])
            self.assertFalse(p["matrix_constructed"])
            self.assertFalse(p["node_interval_error_included"])

    def test_true_parent_bound_dominated_by_dyadic_rational_rule(self):
        for radius in (Q(1,4),Q(1,2),Q(3,4),Q(1)):
            for k in (1,2,3,4):
                p=z.dyadic_stage(radius,k)
                J,N=2**k,4**k
                actual_spatial=2*radius*(2*radius/N*source.lipschitz_safe(radius,J))
                actual_tail=source.authentic_positive_gamma_tail_norm(J)
                self.assertLessEqual(actual_spatial+actual_tail,
                                     p["structural_norm_error"])
                self.assertEqual(actual_tail,p["positive_Gamma_tail_bound"])

    def test_explicit_effective_structural_modulus(self):
        self.assertEqual(z.structural_modulus(Q(1,2),Q(1,1000)),7)
        self.assertEqual(z.structural_modulus(Q(1),Q(1,1000)),9)
        for radius in (Q(1,4),Q(1,2),Q(1)):
            values=[z.dyadic_stage(radius,k)["structural_norm_error"]
                    for k in range(1,13)]
            self.assertTrue(all(a>b>0 for a,b in zip(values,values[1:])))
            for m in (4,6,8,10):
                k=z.structural_modulus(radius,Q(1,2**m))
                self.assertLess(z.dyadic_stage(radius,k)["structural_norm_error"],
                                Q(1,2**m))

    def test_ancestor_source_rung_tail_and_zeno_rate(self):
        for k in range(1,12):
            p=z.dyadic_stage(Q(1,2),k)
            self.assertEqual(p["positive_Gamma_tail_bound"],
                             source.authentic_positive_gamma_tail_norm(2**k))
            self.assertGreater(p["analytic_spatial_bound"],0)
            self.assertGreater(p["positive_Gamma_tail_bound"],0)

    def test_spectral_truth_was_not_inserted_by_modulus(self):
        for k in (1,4,10):
            out=z.signed_source_gap_contract(Q(1,2),k)
            self.assertFalse(out["signed_global_negative_depth_identified"])
            self.assertTrue(out["requires_authentic_finite_operator_spectrum"])
            self.assertTrue(out["no_nontrivial_zero_input"])
            self.assertFalse(out["rh_proved"])

    def test_missing_original_node_intervals_not_forged(self):
        p=z.dyadic_stage(Q(1,2),4)
        conditional=z.add_certified_node_error(p,Q(1,100))
        self.assertFalse(conditional["actual_all_nodes_interval_bound_authenticated"])
        self.assertFalse(conditional["arithmetic_operator_positivity_certified"])
        self.assertEqual(conditional["total_error_if_node_bound_valid"],
                         p["structural_norm_error"]+Q(1,100))

    def test_hostile_budget_and_source_mutations(self):
        p=z.dyadic_stage(Q(1,2),4)
        mutated=dict(p);mutated["original_source"]="AUXILIARY_CHIRAL"
        with self.assertRaises(z.WeilZenoError):
            z.add_certified_node_error(mutated,Q(1,100))
        modified=dict(p);modified["structural_norm_error"]=Q(0)
        with self.assertRaises(z.WeilZenoError):
            z.add_certified_node_error(modified,Q(1,100))
        # Equal numeric float values are NOT equivalent exact proof objects.
        float_laundered=dict(p)
        float_laundered["finite_Zeno_clock"]=float(p["finite_Zeno_clock"])
        self.assertEqual(float_laundered["finite_Zeno_clock"],p["finite_Zeno_clock"])
        with self.assertRaises(z.WeilZenoError):
            z.add_certified_node_error(float_laundered,Q(1,100))
        with self.assertRaises(z.WeilZenoError):
            z.add_certified_node_error(p,Q(1,100),authenticator="self-certified")

    def test_domain_exclusion_and_no_fake_rate(self):
        for fn in (
            lambda:z.dyadic_stage(0.5,2),
            lambda:z.dyadic_stage(Q(2),2),
            lambda:z.dyadic_stage(Q(1,2),0),
            lambda:z.dyadic_stage(Q(1,2),257),
            lambda:z.structural_modulus(Q(1,2),0),
            lambda:z.add_certified_node_error(z.dyadic_stage(Q(1,2),2),-1),
        ):
            with self.assertRaises(z.WeilZenoError):fn()


if __name__=="__main__":
    unittest.main()
