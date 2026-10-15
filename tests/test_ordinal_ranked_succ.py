"""Ordinal certificates, Goodstein growth, long finite paths and martingale guards."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.ordinal_ranked_succ import (
    OrdinalDescentError,OrdinalCNF,ZERO,ordinal_nat,ordinal_monomial,
    ordinal_lex_counters,hereditary_base,goodstein_step,goodstein_prefix,
    HierarchicalCountdown,giant_finite_path_certificate,
    OrdinalProofObligationQueue,gigantic_observer_proof_queue,
)
from observational_succ.ordinal_martingale_boundary import (
    almost_sure_termination_source,ordinal_pathwise_rank_obstruction,
    ordinal_ranked_schur_normalization,ordinal_termination_not_weil_positive,
    actual_weil_ordinal_rank_frontier,
)


class GenuineOrdinalNormalFormTests(unittest.TestCase):
    def test_exact_omega_powers_and_nested_CNF_lexicographic_order(self):
        omega=ordinal_monomial(ordinal_nat(1))
        omega2=ordinal_monomial(ordinal_nat(2))
        omega_omega=ordinal_monomial(omega)
        assert ZERO < ordinal_nat(1) < ordinal_nat(13) < omega
        assert omega<ordinal_lex_counters((1,1))<omega2<omega_omega
        self.assertEqual(str(omega),"ω")
        self.assertEqual(str(omega2),"ω^(2)")
        self.assertEqual(str(omega_omega),"ω^(ω)")
        self.assertEqual(str(ordinal_lex_counters((2,0,3))),"ω^(2)*2 + 3")
        self.assertEqual(str(ordinal_nat(0)),"0")

    def test_source_rejects_non_CNF_order_wrong_types_and_forged_coefficients(self):
        omega=ordinal_monomial(ordinal_nat(1))
        for bad in (
            ((ZERO,1),(ordinal_nat(1),2)),
            ((ZERO,1),(ZERO,2)),
            ((ordinal_nat(1),1),(omega,2)),
            ((ZERO,True),),
            ((ZERO,0),),
        ):
            with self.assertRaises(OrdinalDescentError):
                OrdinalCNF(bad)
        for bad in (True,-1,1.5,2**1025):
            with self.assertRaises(OrdinalDescentError):
                ordinal_nat(bad)
        for x in ((),(1,True),(0,-1),(2**1025,)):
            with self.assertRaises(OrdinalDescentError):
                ordinal_lex_counters(x)


class SourceHereditaryGoodsteinTests(unittest.TestCase):
    def test_original_hereditary_expansion_is_canonical_and_source_executable(self):
        for base,n in product((2,3,4,5,7),(0,1,2,3,4,5,6,7,8,9,10,12,20,32,48,100)):
            code=hereditary_base(n,base)
            self.assertEqual(code.evaluate_at(base),n)
            self.assertIsInstance(code.ordinal(),OrdinalCNF)
        self.assertEqual(str(hereditary_base(3,2).ordinal()),"ω + 1")
        self.assertEqual(str(hereditary_base(4,2).ordinal()),"ω^(ω)")
        self.assertEqual(str(hereditary_base(100,3).ordinal()),
                         "ω^(ω + 1) + ω^(2)*2 + 1")

    def test_actual_goodstein_step_can_grow_natural_while_ordinal_decreases(self):
        p=goodstein_step(4,2)
        self.assertEqual(p.hereditary_replaced_natural,27)
        self.assertEqual(p.natural_after,26)
        self.assertEqual(str(p.ordinal_before),"ω^(ω)")
        self.assertLess(p.ordinal_after,p.ordinal_before)
        self.assertTrue(p.natural_value_increased)
        self.assertTrue(p.rank_strictly_decreased)
        q=goodstein_step(3,2)
        self.assertEqual(q.natural_after,3)
        self.assertEqual(str(q.ordinal_before),"ω + 1")
        self.assertEqual(str(q.ordinal_after),"ω")

    def test_all_bounded_source_transitions_strictly_decrease_original_ordinals(self):
        checked=0
        for base in (2,3,4,5,7,8):
            for n in range(1,67):
                r=goodstein_step(n,base)
                self.assertLess(r.ordinal_after,r.ordinal_before)
                self.assertTrue(r.original_source_mathematical_only)
                self.assertFalse(r.omega_iteration_executed)
                self.assertFalse(r.RH_proved)
                checked+=1
        self.assertEqual(checked,6*66)

    def test_goodstein_short_terminating_and_long_growing_prefixes(self):
        for n in (1,2,3):
            z=goodstein_prefix(n,20)
            self.assertTrue(z["terminal_zero_reached_in_prefix"])
            self.assertEqual(z["last_value"],0)
        large=goodstein_prefix(4,12)
        self.assertTrue(large["natural_growth_occurred"])
        self.assertTrue(large["every_executed_transition_strictly_rank_decreases"])
        self.assertFalse(large["RH_proved"])
        self.assertEqual(large["unbounded_all_n_termination"],
                         "CLASSICAL_GOODSTEIN_WELLFOUNDED_EPSILON_0_THEOREM_NOT_FINITE_TRACE")
        self.assertFalse(large["terminal_zero_reached_in_prefix"])

    def test_goodstein_invalid_source_and_resource_bounds(self):
        for n,b in ((0,2),(3,1),(3,512),(-1,2),(True,2),(3,True)):
            with self.assertRaises(OrdinalDescentError):
                goodstein_step(n,b)
        with self.assertRaises(OrdinalDescentError):
            goodstein_step(16,2,max_bits=8) # genuine growth 3^27 far exceeds declared 8-bit budget
        with self.assertRaises(OrdinalDescentError):
            hereditary_base(1,1)


class AstronomicalFinitePathProofTests(unittest.TestCase):
    def test_rank_decrease_and_exact_base_R_borrow_without_executing_path(self):
        for bits,digits in (
            (2,(1,0,0)),(4,(3,0,2)),(8,(1,1,0,3)),
            (16,(2,0,0,0)),(32,(1,0,0)),(128,(1,0,0)),
        ):
            x=HierarchicalCountdown(digits,bits)
            y=x.successor()
            self.assertLess(y.rank,x.rank)
            self.assertEqual(y.exact_remaining_steps+1,x.exact_remaining_steps)
        giant=giant_finite_path_certificate((1,0,0),128)
        self.assertEqual(giant["steps_to_zero_certified_without_execution"],2**256)
        self.assertEqual(giant["steps_bit_length"],257)
        self.assertEqual(giant["ordinal_rank"],"ω^(2)")
        self.assertTrue(giant["finite_symbolic_proof_of_all_stages"])
        self.assertFalse(giant["path_executed_in_full"])
        self.assertFalse(giant["RH_proved"])

    def test_counter_protocol_runs_at_all_small_reachable_states(self):
        for b in (1,2,3):
            R=2**b
            for a,c in product(range(R),range(R)):
                x=HierarchicalCountdown((a,c),b)
                length=x.exact_remaining_steps
                for i in range(length):
                    x=x.successor()
                    self.assertEqual(x.exact_remaining_steps,length-i-1)
                self.assertEqual(x.digits,(0,0))
                with self.assertRaises(OrdinalDescentError):
                    x.successor()

    def test_huge_rank_source_rejects_invalid_coefficient_and_overwide_protocol(self):
        for digits,bits in (
            ((1,0),0),((1,),513),((True,0),2),((4,),2),
            ((),3),((0,)*8,3),
        ):
            with self.assertRaises(OrdinalDescentError):
                HierarchicalCountdown(digits,bits)
        with self.assertRaises(OrdinalDescentError):
            giant_finite_path_certificate((0,0),10)


class ProbabilityAndSignedWeilCountermodels(unittest.TestCase):
    def test_probabilistic_source_terminates_almost_surely_not_on_every_path(self):
        for p in (F(1,2),F(1,3),F(2,3)):
            prev=None
            for horizon in (0,1,2,5,10,20):
                z=almost_sure_termination_source(horizon,p)
                self.assertEqual(z["exact_survival_probability"],(1-p)**horizon)
                self.assertEqual(z["exact_termination_probability_by_horizon"],
                                 1-(1-p)**horizon)
                self.assertEqual(z["expected_steps"],1/p)
                self.assertEqual(z["real_ranking_supermartingale_drift"],p)
                self.assertTrue(z["infinite_nonhalting_path_in_source_graph"])
                self.assertFalse(z["strict_ordinal_rank_all_positive_probability_edges"])
                self.assertFalse(z["RH_proved"])
                if prev is not None:
                    self.assertLess(z["exact_survival_probability"],prev)
                prev=z["exact_survival_probability"]
        forced=almost_sure_termination_source(3,F(1))
        self.assertFalse(forced["infinite_nonhalting_path_in_source_graph"])
        self.assertTrue(forced["strict_ordinal_rank_all_positive_probability_edges"])

    def test_every_finite_increasing_path_can_have_horizon_specific_rank_not_one_global_rank(self):
        for n in (1,2,5,10,100):
            z=ordinal_pathwise_rank_obstruction(n)
            self.assertTrue(z["each_finite_prefix_has_ordinal_nat_rank"])
            self.assertFalse(z["one_coherent_global_ordinal_rank_exists"])
            self.assertTrue(z["not_a_counterexample_to_almost_sure_termination"])

    def test_schur_completion_and_ordinals_cannot_fix_a_negative_source(self):
        good=ordinal_ranked_schur_normalization(2,1,2)
        self.assertEqual(good["completed_square_schur"],F(3,2))
        self.assertTrue(good["source_quadratic_positive"])
        bad=ordinal_ranked_schur_normalization(1,2,1)
        self.assertTrue(bad["normalization_terminated"])
        self.assertTrue(bad["rank_strict_decrease"])
        self.assertEqual(bad["completed_square_schur"],-3)
        self.assertEqual(bad["negative_exact_direction"],(-2,1))
        self.assertFalse(bad["source_quadratic_positive"])
        counter=ordinal_termination_not_weil_positive()
        self.assertFalse(counter["ordinal_termination_implies_original_Weil_PSD"])
        self.assertFalse(counter["RH_proved"])

    def test_arithmetic_frontier_not_promoted_by_semantic_ordinal_ranks(self):
        d=actual_weil_ordinal_rank_frontier()
        self.assertEqual(d["true_source_Weil_Schur_rank_function"],"UNVERIFIED")
        self.assertEqual(d["true_source_positive_terminal_certificate"],"UNVERIFIED")
        self.assertEqual(d["all_a_completed_Weil_positive"],"UNVERIFIED")
        self.assertFalse(d["RH_proved"])

    def test_source_probability_and_schur_domain_rejections(self):
        for n,p in ((-1,F(1,2)),(1,F(0)),(2,F(4,3)),(2,0.5),(True,F(1))):
            with self.assertRaises(OrdinalDescentError):
                almost_sure_termination_source(n,p)
        for args in ((0,1,1),(-1,0,1),(1,True,1),(1,2,0.25)):
            with self.assertRaises(OrdinalDescentError):
                ordinal_ranked_schur_normalization(*args)



class OrdinalRecursiveModelOfModelsTests(unittest.TestCase):
    def test_source_observer_higher_phase_spawns_lower_work_but_rank_strictly_drops(self):
        original=OrdinalProofObligationQueue((2,1,0))
        high=original.discharge_next(spawn_medium=18,spawn_low=1024)
        self.assertEqual(high.counts,(1,19,1024))
        self.assertLess(high.rank,original.rank)
        another=high.discharge_next(spawn_medium=3,spawn_low=10)
        self.assertEqual(another.counts,(0,22,1034))
        self.assertLess(another.rank,high.rank)
        medium=another.discharge_next(spawn_low=2**64)
        self.assertEqual(medium.counts,(0,21,1034+2**64))
        self.assertLess(medium.rank,another.rank)
        self.assertFalse(medium.finished)
        self.assertFalse(gigantic_observer_proof_queue(256)["RH_proved"])

    def test_arbitrary_long_normalization_path_proved_without_execution(self):
        proof=gigantic_observer_proof_queue(256)
        self.assertEqual(proof["before_rank"],"ω^(2)")
        self.assertEqual(proof["after_rank"],"ω + "+str(2**256))
        self.assertEqual(proof["spawned_low_count"],2**256)
        self.assertTrue(proof["rank_decreased_strictly"])
        self.assertTrue(proof["source_observer_growth_tasks_can_increase"])
        self.assertFalse(proof["source_completed_Weil_claim_proved"])

    def test_all_three_phase_observer_normalizer_small_case_reaches_zero(self):
        state=OrdinalProofObligationQueue((2,0,0))
        steps=0
        while not state.finished:
            if state.counts[0]:
                nxt=state.discharge_next(spawn_medium=1,spawn_low=2)
            elif state.counts[1]:
                nxt=state.discharge_next(spawn_low=1)
            else:
                nxt=state.discharge_next()
            self.assertLess(nxt.rank,state.rank)
            state=nxt
            steps+=1
            self.assertLess(steps,32)
        self.assertTrue(state.finished)
        self.assertEqual(state.rank,ZERO)
        self.assertEqual(steps,2+2+4+2)
        with self.assertRaises(OrdinalDescentError):
            state.discharge_next()

    def test_higher_priority_forgery_and_nonfinite_task_spawn_refused(self):
        for counts in ((True,1,0),(-1,0,0),(1.5,0,0),(),(0,0,0,0)):
            with self.assertRaises(OrdinalDescentError):
                OrdinalProofObligationQueue(counts)
        with self.assertRaises(OrdinalDescentError):
            OrdinalProofObligationQueue((0,1,0)).discharge_next(spawn_medium=1)
        with self.assertRaises(OrdinalDescentError):
            OrdinalProofObligationQueue((0,0,1)).discharge_next(spawn_low=1)
        with self.assertRaises(OrdinalDescentError):
            OrdinalProofObligationQueue((1,0,0)).discharge_next(spawn_low=2**1025)


if __name__=="__main__":
    unittest.main()
