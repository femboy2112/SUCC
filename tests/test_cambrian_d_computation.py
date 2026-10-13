import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product

from observational_succ.cambrian_d_computation import (
    arbitrary_holdout, bayesian_calibration, construct_memory,
    destructive_greedy_countermodel, exhaustive_minimum_quotient,
    exhaustive_strategy_oracle, hidden_mode_receipt, memory_validation,
    optimal_cost, partial_source, resource_receipt,
    genetic_cost_policy,cegis_cost_policy,similarity_control,
    declared_history_teacher,learn_history_memory,history_learning_validation,
)
from observational_succ.contextual_heuristics import syntax_clone_counterexample
from observational_succ.eodcs_multi_action_source import ActionSource, action_congruence
from observational_succ.noncommuting_proof_transport import FiniteCarrier, Instrument


class PartialCausalTests(unittest.TestCase):
    def test_enabledness_not_silently_hidden(self):
        s = partial_source(("same","same"),("a",),((0,None),))
        self.assertNotEqual(s.report("0"),s.report("1"))
        self.assertEqual(s.step("1","a"),"disabled")
        self.assertEqual(s.step("disabled","a"),"disabled")

    def test_bounded_asynchronous_queue_exact_lower_bound(self):
        for capacity in range(1,7):
            s = partial_source(tuple("empty" if i==0 else "pending"
                                    for i in range(capacity+1)),
                ("enqueue","deliver"),
                (tuple(i+1 if i<capacity else None for i in range(capacity+1)),
                 tuple(i-1 if i>0 else None for i in range(capacity+1))))
            # Failure sink is an additional totalization artifact.
            certificate = action_congruence(s)
            self.assertEqual(len(certificate.equivalence_classes),capacity+2)
            for i in range(capacity):
                self.assertNotEqual(s.observe(str(i),("deliver",)*i),
                                    s.observe(str(i+1),("deliver",)*i))

    def test_hidden_common_legality_relation_is_nontransitive(self):
        # a,b,c all initially report 0; only a,c allow x, with outputs 1,2.
        output = {"a":0,"b":0,"c":0,"d":1,"e":2}
        step = {"a":"d","c":"e"}
        def compatible(s,t):
            if output[s] != output[t]: return False
            if s not in step or t not in step: return True
            return output[step[s]] == output[step[t]]
        self.assertTrue(compatible("a","b"))
        self.assertTrue(compatible("b","c"))
        self.assertFalse(compatible("a","c"))

    def test_invalid_partial_model_rejected(self):
        with self.assertRaises(ValueError):
            partial_source((0,1),("x",),((0,2),))


class MemoryBirthTests(unittest.TestCase):
    def test_forced_four_state_memory_not_preloaded(self):
        s=ActionSource("cycle",0,"model",("0","1","2","3"),
                       ("1","0","0","0"),("next",),(("1","2","3","0"),))
        receipt=memory_validation(s)
        self.assertEqual(receipt["class_counts"],(2,3,4))
        self.assertEqual(receipt["minimal_predictive_classes"],4)
        self.assertEqual(receipt["supplemental_bits_given_current_report"],2)
        self.assertEqual(receipt["exhaustive_partition_oracle"]["partitions_checked"],15)

    def test_fresh_arbitrary_source_tables(self):
        for seed in range(131,155):
            s=arbitrary_holdout(seed,3+(seed%4))
            r=memory_validation(s,genetic_seed=9000+seed)
            self.assertGreater(r["forecast_checks"],0)
            self.assertGreaterEqual(r["minimal_predictive_classes"],2)
            self.assertLessEqual(r["minimal_predictive_classes"],len(s.states))

    def test_null_source_requires_no_representation_birth(self):
        s=ActionSource("null",0,"model",("a","b"),("0","0"),
                       ("x",),(("b","a"),))
        r=memory_validation(s)
        self.assertEqual(r["minimal_predictive_classes"],1)
        self.assertEqual(r["obstructions"],())

    def test_illegal_merged_memory_is_detected(self):
        s=ActionSource("mutation",0,"model",("0","1","2"),
                       ("1","0","0"),("next",),(("1","2","0"),))
        born=construct_memory(s)
        bad=replace(born,classes=(("0",),("1","2")))
        with self.assertRaises(AssertionError): bad.prediction(1,"next")

    def test_history_only_learning_with_exact_teacher_on_fresh_graphs(self):
        for seed in range(271,295):
            r=history_learning_validation(arbitrary_holdout(seed,3+(seed%4)))
            self.assertFalse(r["learning"]["hidden_state_table_given_to_learner"])
            self.assertEqual(r["learned_predictive_states"],r["independent_minimum_state_oracle"])

    def test_history_learner_rejects_false_teacher_witness(self):
        with self.assertRaises(AssertionError):
            learn_history_memory(("a",),lambda word:"0",lambda model:())

    def test_history_memory_unknown_initial_state_is_not_magically_known(self):
        source=arbitrary_holdout(131,6)
        membership,equivalence=declared_history_teacher(source,source.states[0])
        model,r=learn_history_memory(source.actions,membership,equivalence,max_rounds=1)
        if model is None:self.assertEqual(r["status"],"UNRESOLVED_RESOURCE_BUDGET")
        else:self.assertTrue(r["reset_access_assumed"])


class BayesianTests(unittest.TestCase):
    def test_clone_mass_is_family_invariant(self):
        r=syntax_clone_counterexample()
        self.assertEqual(r["quotient_A_before"],r["quotient_A_after"])
        self.assertNotEqual(r["naive_A_before"],r["naive_A_after_syntax_clone"])

    def test_exact_shared_latent_brier_regret(self):
        for copies in (1,2,8,20):
            r=bayesian_calibration(copies)
            self.assertEqual(r["naive_conditional_brier"]-r["correct_conditional_brier"],
                             r["brier_regret"])
            self.assertEqual(r["correct_posterior_H"],Q(3,4))
            if copies>1:self.assertGreater(r["brier_regret"],0)

    def test_misspecification_confidence_is_not_calibration(self):
        r=bayesian_calibration(balanced_pairs=30)
        self.assertGreater(r["misspecified_model_02_posterior"],Q(999,1000))
        self.assertGreater(r["misspecified_heldout_brier"],r["correct_heldout_brier"])

    def test_stopping_uses_complete_trace_likelihood(self):
        r=bayesian_calibration()
        self.assertEqual(sum(x["mixture_probability"] for x in r["adaptive_stopping"]),1)
        self.assertEqual(r["adaptive_stopping"][0]["posterior_H"],Q(3,4))
        self.assertEqual(r["adaptive_stopping"][-1]["posterior_H"],Q(1,28))


class ProbeCostTests(unittest.TestCase):
    def test_greedy_destruction_and_exact_tree_oracle(self):
        field,target,costs=destructive_greedy_countermodel()
        r=optimal_cost(field,target,costs,2)
        oracle=exhaustive_strategy_oracle(field,target,costs,2)
        self.assertEqual(r["worst_case_cost"],5)
        self.assertEqual(r["first_action"],"full")
        self.assertEqual(r["worst_case_cost"],oracle["worst_case_cost"])
        dead=FiniteCarrier(2,(Instrument("read",(1,1),(0,1),(True,True)),),"dead","model")
        self.assertIsNone(optimal_cost(dead,("1","2"),{"read":Q(1)},3)["worst_case_cost"])

    def test_all_two_state_one_action_sources_against_tree_oracle(self):
        for output,transition,enabled in product(product((0,1),repeat=2),
                                               product((0,1),repeat=2),
                                               product((False,True),repeat=2)):
            field=FiniteCarrier(2,(Instrument("a",output,transition,enabled),),"all","model")
            costs={"a":Q(7,3)}
            answer=optimal_cost(field,("0","1"),costs,2)
            oracle=exhaustive_strategy_oracle(field,("0","1"),costs,2)
            self.assertEqual(answer["worst_case_cost"],oracle["worst_case_cost"])

    def test_initial_zero_cost_homogeneous_target(self):
        field,target,costs=destructive_greedy_countermodel()
        self.assertEqual(optimal_cost(field,("a",)*3,costs,0)["worst_case_cost"],0)
        with self.assertRaises(ValueError):optimal_cost(field,target,{"cheap":0,"full":1},2)

    def test_evolutionary_policy_credit_is_not_oracle_rescue(self):
        field,target,costs=destructive_greedy_countermodel()
        missed=genetic_cost_policy(field,target,costs,seed=0,generations=1)
        self.assertIsNone(missed["best_verified_cost"])
        self.assertFalse(missed["exhaustive_rescue_used"])
        exact=cegis_cost_policy(field,target,costs)
        self.assertEqual(exact["best_verified_cost"],5)
        self.assertTrue(exact["counterexamples"])


class BehavioralResourceTests(unittest.TestCase):
    def test_hidden_mode_requires_new_intervention(self):
        r=hidden_mode_receipt()
        self.assertEqual(r["old_input_moments"],r["minimal_two_state_moments"])
        self.assertEqual(r["old_input_rank"],2)
        self.assertEqual(r["augmented_input_block_rank"],3)
        self.assertEqual(similarity_control(),r["minimal_two_state_moments"])

    def test_every_two_source_strings_have_an_index_collision(self):
        r=resource_receipt(4,19)
        self.assertEqual(r["minimum_messages"],16)
        self.assertEqual(len(r["pair_collision_witnesses"]),120)
        for a,b,index in r["pair_collision_witnesses"]:
            self.assertNotEqual(a[index],b[index])
        self.assertEqual(r["all_zero_target_refutation_probes"],1)
        self.assertEqual(r["shortest_refuting_unary_word_length"],19)


if __name__=="__main__": unittest.main()
