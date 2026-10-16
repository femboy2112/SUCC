"""Exact source-authentic Tate p-adic two-axis ordinal chart normalization."""
import unittest
from fractions import Fraction as F

from observational_succ.ordinal_ranked_succ import OrdinalDescentError
from observational_succ.tate_observer_completion import PadicBruhatChart
from observational_succ.tate_ordinal_chart_normalizer import (
    TateOrdinalChartStage,complete_tate_source_chart,
    growing_tate_target_rank_no_go,
)


class TwoAxisTateOrdinalNormalizationTests(unittest.TestCase):
    def test_actual_finite_padic_source_fourier_commutes_under_both_ordinal_paths(self):
        cases=(
          (2,0,1,1,2,(F(1),F(-3))),
          (2,1,0,2,2,(F(1),F(-2))),
          (2,1,1,2,2,(F(1),F(2),F(-3),F(4))),
          (3,0,1,1,1,(F(1),F(0),F(-1))),
          (3,0,1,1,2,(F(1),F(3),F(-2))),
          (5,0,1,1,1,(F(0),F(2),F(-1),F(3),F(1))),
        )
        for p,r,s,R,S,values in cases:
            c=PadicBruhatChart(p,r,s)
            a=complete_tate_source_chart(c,values,R,S,strategy="support-first")
            b=complete_tate_source_chart(c,values,R,S,strategy="precision-first")
            self.assertEqual(a["terminal_source_values"],b["terminal_source_values"])
            self.assertEqual(a["terminal_rank"],"0")
            self.assertEqual(a["actual_completed_refinements"],R-r+S-s)
            self.assertTrue(a["ordinal_decrease_on_every_executed_refinement"])
            self.assertTrue(a["same_exact_cyclotomic_Fourier_under_opposite_refinement_order"])
            self.assertFalse(a["completed_global_Tate_adelic_Poisson"])
            self.assertFalse(a["RH_proved"])

    def test_original_cyclotomic_hilbert_tate_chart_values_not_provenance_free_guess(self):
        c=PadicBruhatChart(2,0,1)
        a=complete_tate_source_chart(c,(F(1),F(2)),1,2)
        self.assertEqual(a["terminal_source_values"],
                         (F(1),F(0),F(2),F(0),F(1),F(0),F(2),F(0)))
        self.assertEqual(a["initial_rank"],"ω + 1")
        self.assertEqual(a["terminal_rank"],"0")
        self.assertEqual(a["actual_completed_refinements"],2)

    def test_cofinal_target_growth_resets_rank_and_is_not_one_executable_infinite_stage(self):
        x=growing_tate_target_rank_no_go()
        self.assertEqual(x["first_fixed_target_finished_rank"],"0")
        self.assertEqual(x["new_larger_target_started_rank"],"ω")
        self.assertFalse(x["single_uniform_ordinal_descent_across_all_growing_targets"])
        self.assertFalse(x["cofinal_Tate_Topology_done_by_finite_trace"])
        self.assertFalse(x["RH_proved"])

    def test_invalid_chart_source_target_and_wrong_strategy_rejected(self):
        c=PadicBruhatChart(2,0,1)
        cases=(
            (0,0,(1,0),"support-first"),
            (1,0,(1,0),"support-first"),
            (1,2,(1,0),"evil"),
            (1,2,(1,),"support-first"),
            (1,2,(1,0.5),"support-first"),
            (True,2,(1,0),"support-first"),
        )
        for R,S,values,strategy in cases:
            with self.assertRaises((OrdinalDescentError,ValueError)):
                complete_tate_source_chart(c,values,R,S,strategy=strategy)
        with self.assertRaises(OrdinalDescentError):
            TateOrdinalChartStage(c,(F(1),F(2)),0,0)
        with self.assertRaises(OrdinalDescentError):
            TateOrdinalChartStage(c,(F(1),F(2)),2,5) # 2^7 cells over budget

    def test_terminal_observer_cannot_keep_claiming_ord_steps(self):
        a=TateOrdinalChartStage(PadicBruhatChart(2,0,1),(F(1),F(2)),0,1)
        self.assertTrue(a.completed)
        with self.assertRaises(OrdinalDescentError):
            a.increase_support()
        with self.assertRaises(OrdinalDescentError):
            a.increase_precision()


if __name__=="__main__":
    unittest.main()
