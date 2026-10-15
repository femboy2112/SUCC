"""Exact hybrid ordinal epoch + stochastic ranking-supermartingale controls."""
import unittest
from fractions import Fraction as F

from observational_succ.ordinal_ranked_succ import OrdinalDescentError
from observational_succ.ordinal_epoch_supermartingale import (
    uniform_hazard_ordinal_epoch,summable_hazard_stuttering_countermodel,
    omega_branch_infinite_expected_length,giant_geometric_ranked_succ_path,
    true_source_ordinal_martingale_boundary,
)


class HybridOrdinalMartingaleTheorems(unittest.TestCase):
    def test_uniform_conditional_hazard_plus_ranked_epoch_yields_a_s_termination(self):
        for p in (F(1,2),F(1,3),F(2,3),F(1)):
            for t in (0,1,3,7,16):
                z=uniform_hazard_ordinal_epoch((1,0,0),p,t)
                self.assertEqual(z["initial_source_rank"],"ω^(2)")
                self.assertEqual(z["survival_upper_at_fixed_rank"],(1-p)**t)
                self.assertEqual(z["almost_sure_epoch_exit"],"PROVED_FROM_UNIFORM_HAZARD")
                self.assertTrue(z["macro_rank_never_increases_by_declared_transition_law"])
                self.assertTrue(z["progress_milestone_strict_ordinal_descent_declared"])
                self.assertFalse(z["original_completed_Weil_terminal_positive"])
                self.assertFalse(z["RH_proved"])
        for state,p,t in (((0,0,0),F(1,2),1),((1,0,0),F(0),1),
                          ((1,0,0),F(3,2),2),((1,0,0),0.5,2),
                          ((1,0,0),F(1,2),-1)):
            with self.assertRaises(OrdinalDescentError):
                uniform_hazard_ordinal_epoch(state,p,t)

    def test_positive_hazard_at_every_tick_can_still_permit_nonterminal_probability(self):
        last=F(1)
        for t in (0,1,2,3,5,10,20,40,70):
            z=summable_hazard_stuttering_countermodel(t)
            self.assertGreater(z["finite_survival_exact"],F(1,2))
            self.assertGreaterEqual(z["finite_survival_exact"],z["finite_survival_lower"])
            self.assertLessEqual(z["finite_survival_exact"],last)
            self.assertEqual(z["infinite_survival_probability_lower"],F(1,2))
            self.assertFalse(z["almost_sure_epoch_exit"])
            self.assertFalse(z["RH_proved"])
            last=z["finite_survival_exact"]
        for t in (-1,True,257):
            with self.assertRaises(OrdinalDescentError):
                summable_hazard_stuttering_countermodel(t)

    def test_sure_ordinal_termination_with_infinite_expected_time(self):
        previous=F()
        for h in (0,1,2,5,12,30,60,100):
            z=omega_branch_infinite_expected_length(h)
            self.assertTrue(z["terminates_on_EVERY_sample_path"])
            self.assertEqual(z["exact_tail_probability_tau_gt_horizon"],F(1,h+1))
            self.assertEqual(z["unseen_probability_mass"],F(1,h+2))
            self.assertEqual(z["finite_branch_probability_sum"],1-F(1,h+2))
            self.assertGreaterEqual(z["truncated_expected_length_lower"],previous)
            self.assertEqual(z["full_expected_length"],
                             "INFINITE_BY_HARMONIC_DIVERGENCE")
            self.assertFalse(z["one_uniform_finite_path_length_bound"])
            self.assertFalse(z["RH_proved"])
            previous=z["truncated_expected_length_lower"]
        for h in (-1,True,257):
            with self.assertRaises(OrdinalDescentError):
                omega_branch_infinite_expected_length(h)

    def test_huge_exact_milestone_count_with_nonnegative_supermartingale_drift(self):
        for p in (F(1,2),F(2,3),F(1)):
            z=giant_geometric_ranked_succ_path((1,0,0),128,p)
            self.assertEqual(z["source_milestone_count"],2**256)
            self.assertEqual(z["expected_total_attempts"],F(2**256)/p)
            self.assertEqual(z["ranking_supermartingale_conditional_drift"],p)
            self.assertTrue(z["almost_sure_finite_source_completion"])
            self.assertFalse(z["original_Weil_positive_terminal_proved"])
            self.assertFalse(z["RH_proved"])
            self.assertEqual(z["all_graph_paths_finite"],p==1)
        with self.assertRaises(OrdinalDescentError):
            giant_geometric_ranked_succ_path((1,0,0),128,F(0))
        with self.assertRaises(OrdinalDescentError):
            giant_geometric_ranked_succ_path((1,0,0),128,0.5)

    def test_completed_original_Weil_does_not_get_free_ordinal_stochastic_sign(self):
        source=true_source_ordinal_martingale_boundary()
        self.assertEqual(source["actual_completed_Weil_global_positive"],"UNVERIFIED")
        self.assertEqual(source["source_hazard_uniform_or_divergent"],"UNVERIFIED")
        self.assertEqual(source["independent_source_positive_terminal"],"UNVERIFIED")
        self.assertFalse(source["RH_proved"])


if __name__=="__main__":
    unittest.main()
