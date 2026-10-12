"""Adversarial exact finite checkpoint enumeration / E-tower proof controls."""
import itertools
import random
import unittest
from fractions import Fraction as F

from observational_succ.carrier_observational_frontier import (
    ControlledCarrier, destructive_parity_model, ontology_alias_model,
)
from observational_succ.checkpoint_meta_tower import (
    MetaTowerError, GroundRule, Report, HornTheory, BranchLicense,
    FiniteController, checkpoint_closure, proof_policy_checkpoint,
    verify_policy_tree, enumerate_action_words, certify_parallel_roots,
    nonmonotone_default_countermodel, meta_tower_demo, finite_source_soundness,
)


class MetaTowerTests(unittest.TestCase):
    def theory(self):
        return HornTheory("carrier-1", "basis-v1", ("a",), (
            GroundRule(("a",), "b"),
            GroundRule(("b", "observed"), "c"),
            GroundRule(("c",), "target"),
            GroundRule(("target",), "z"),
        ))

    def test_arbitrary_rule_order_fair_iterates_to_same_closure(self):
        r=self.theory().all_rule_orders(("observed",))
        self.assertEqual(r["checked_permutations"],24)
        self.assertEqual(r["closure"],("a","b","c","observed","target","z"))

    def test_missing_empirical_premise_cannot_be_invented_by_rule_order(self):
        r=self.theory().all_rule_orders(())
        self.assertEqual(r["closure"],("a","b"))

    def test_rule_permutation_rejection_and_forged_conclusion(self):
        theory=self.theory()
        with self.assertRaises(MetaTowerError):
            theory.closure(("observed",),order=(0,0,1,2))
        r=theory.closure(("observed",))
        changed=dict(r,closure=("a","b","fabricated"))
        with self.assertRaises(MetaTowerError): theory.check_proof(changed)
        forged=dict(r,steps=(("target",2,("c",)),))
        with self.assertRaises(MetaTowerError): theory.check_proof(forged)

    def test_checkpoint_strict_event_origin_delayed_macro_proof(self):
        theory=HornTheory("carrier-1","basis-v1",(),(
            GroundRule(("left",),"known-left"),
            GroundRule(("right",),"known-right"),
            GroundRule(("known-left","known-right"),"parity"),
        ))
        events=((Report("e0","carrier-1","basis-v1",1,"A","right"),),
                (),
                (Report("e1","carrier-1","basis-v1",2,"B","left"),))
        stages=checkpoint_closure(theory,events,trusted_event_ids=frozenset(("e0","e1")),target="parity")
        self.assertEqual([s["target_certified"] for s in stages],[False,False,True])
        self.assertEqual(stages[-1]["macro_steps_at_E"],1)
        self.assertFalse(stages[-1]["source_outcomes_authenticated"])
        self.assertEqual(stages[-1]["accepted_event_ids"],("e0","e1"))

    def test_future_bogus_untrusted_or_foreign_event_rejected(self):
        theory=self.theory()
        legit=Report("id","carrier-1","basis-v1",1,"A","observed")
        for e in (Report("id","carrier-1","basis-v2",1,"A","observed"),
                  Report("id","other","basis-v1",1,"A","observed"),
                  Report("id","carrier-1","basis-v1",3,"A","observed")):
            with self.assertRaises(MetaTowerError):
                checkpoint_closure(theory,((e,),),trusted_event_ids=frozenset(("id",)),target="target")
        with self.assertRaises(MetaTowerError):
            checkpoint_closure(theory,((legit,),),trusted_event_ids=frozenset(),target="target")

    def test_replay_conflict_cannot_forge_second_source_fact(self):
        theory=self.theory()
        with self.assertRaises(MetaTowerError):
            checkpoint_closure(theory,(
                (Report("e0","carrier-1","basis-v1",1,"A","observed"),),
                (Report("e0","carrier-1","basis-v1",2,"B","new"),)),
                trusted_event_ids=frozenset(("e0",)),target="target")

    def test_exact_dovetail_word_count_and_order(self):
        words=enumerate_action_words(("A","B"),4)
        self.assertEqual(len(words),31)
        self.assertEqual(words[:7],((),("A",),("B",),("A","A"),("A","B"),("B","A"),("B","B")))
        with self.assertRaisesRegex(MetaTowerError,"budget"):
            enumerate_action_words(("A","B"),8,word_budget=100)

    def test_bare_finite_controller_is_ultimately_periodic(self):
        r=FiniteController(("start","tick","tock"),(1,2,1)).eventual_period()
        self.assertEqual(r["prefix"],("start",))
        self.assertEqual(r["period"],("tick","tock"))
        self.assertTrue(r["requires_external_unbounded_storage_for_arbitrary_word_dovetailing"])

    def test_destructive_parity_no_go_survives_all_executable_orderings(self):
        model,target=destructive_parity_model()
        for depth in range(5):
            r=proof_policy_checkpoint(model,target,depth,full_model_no_go=True)
            self.assertEqual(r["status"],"MODEL_CERTIFIED_NO_FINITE_POLICY")
            self.assertIsNone(r["adaptive_policy"])
            self.assertIsNone(r["first_winning_fixed_word"])
            self.assertEqual(r["physical_branches_executed"],0)

    def test_conditional_reversible_action_beats_every_fixed_order_of_two(self):
        states=tuple((a,b) for a,b in itertools.product((0,1),repeat=2))
        rows={}
        for a,b in states:
            rows[(a,b),"Q"]=(a,(a,a^b))
            rows[(a,b),"R0"]=(b if a==0 else 0,(a,b))
            rows[(a,b),"R1"]=(b if a==1 else 0,(a,b))
        model=ControlledCarrier("orig",states,("Q","R0","R1"),rows)
        target={s:s[0]^s[1] for s in states}
        self.assertIsNone(proof_policy_checkpoint(model,target,1)["adaptive_policy"])
        r=proof_policy_checkpoint(model,target,2)
        self.assertEqual(r["status"],"FOUND_ADAPTIVE_POLICY")
        self.assertEqual(r["adaptive_policy"][1],"Q")
        self.assertIsNone(r["first_winning_fixed_word"])
        self.assertEqual(r["verification"]["maximum_depth"],2)
        for state in states:self.assertEqual(len(r["verification"]["source_traces"][states.index(state)]),2)
        with self.assertRaises(MetaTowerError):
            verify_policy_tree(model,target,("DONE",1),max_depth=2)

    def test_ontology_alias_cannot_be_cured_by_more_search(self):
        model,claim=ontology_alias_model()
        for depth in (1,2,4):
            self.assertEqual(proof_policy_checkpoint(model,claim,depth,full_model_no_go=True)["status"],
                             "MODEL_CERTIFIED_NO_FINITE_POLICY")
        enlarged,new=ontology_alias_model(allow_separator=True)
        self.assertEqual(proof_policy_checkpoint(enlarged,new,1)["status"],"FOUND_ADAPTIVE_POLICY")

    def test_immutable_first_action_branch_requires_distinct_source_leases(self):
        carrier,_=destructive_parity_model()
        one=BranchLicense(carrier.source_id,"source-copy-1","same-original-state")
        two=BranchLicense(carrier.source_id,"source-copy-2","same-original-state")
        with self.assertRaises(MetaTowerError):
            certify_parallel_roots(carrier,((one,"READ_A"),(one,"READ_B")))
        report=certify_parallel_roots(carrier,((one,"READ_A"),(two,"READ_B")))
        self.assertEqual(report["distinct_source_preparations"],2)
        self.assertFalse(report["true_state_reprepared_identically"])
        with self.assertRaises(MetaTowerError):
            certify_parallel_roots(carrier,((BranchLicense("another","t","same"),"READ_A"),))

    def test_nonmonotone_default_branches_disagree_and_cannot_be_unioned(self):
        self.assertEqual(nonmonotone_default_countermodel(("A","B")),("A",))
        self.assertEqual(nonmonotone_default_countermodel(("B","A")),("B",))
        with self.assertRaises(MetaTowerError):
            nonmonotone_default_countermodel(("A","A"))

    def test_full_small_automata_pair_ranks_vs_independent_solver(self):
        # Exhaust all 4^4 total two-state, two-action deterministic Mealy maps.
        states=(0,1);actions=("A","B");claims={0:0,1:1}
        for signature in itertools.product(range(4),repeat=4):
            rows={}
            for (s,a),code in zip(itertools.product(states,actions),signature):
                rows[s,a]=(code%2,code//2)
            model=ControlledCarrier("tiny-exhaustive",states,actions,rows)
            exact=model.adaptive_original_claim(claims)
            first=next((d for d in range(5)
                        if proof_policy_checkpoint(model,claims,d)["adaptive_policy"] is not None),None)
            if exact["rank"] is None:
                self.assertIsNone(first,signature)
            else:
                self.assertEqual(first,exact["rank"],signature)

    def test_exhaustive_three_rule_order_covers_all_evidence_subsets(self):
        rules=(GroundRule(("a",),"b"),GroundRule(("b",),"c"),GroundRule(("a","c"),"d"))
        theory=HornTheory("S","V",(),rules)
        for n in range(16):
            facts=tuple(x for i,x in enumerate(("a","b","c","d")) if n>>i&1)
            receipt=theory.all_rule_orders(facts)
            self.assertEqual(receipt["checked_permutations"],6)

    def test_inference_permutation_cannot_certify_an_unsound_rule(self):
        theory=HornTheory("S","v",(),(GroundRule(("observed",),"false"),))
        self.assertEqual(theory.closure(("observed",))["closure"],("false","observed"))
        audit=finite_source_soundness(theory,{"real":("observed",)})
        self.assertFalse(audit["sound_relative_to_worlds"])
        self.assertEqual(audit["failing_rule"],0)
        self.assertFalse(audit["source_semantics_authenticated"])

    def test_true_finite_source_semantics_supports_closure_induction(self):
        theory=self.theory()
        result=finite_source_soundness(theory,{
            "w0":("a","b"),
            "w1":("a","b","observed","c","target","z"),
        })
        self.assertTrue(result["sound_relative_to_worlds"])
        self.assertFalse(result["source_semantics_authenticated"])

    def test_fake_trusted_axiom_has_independent_world_refutation(self):
        theory=HornTheory("S","v",("outside-reality",),(
            GroundRule(("outside-reality",),"all-proven"),))
        audit=finite_source_soundness(theory,{"actual":()})
        self.assertFalse(audit["sound_relative_to_worlds"])
        self.assertEqual(audit["failing_axiom"],"outside-reality")

    def test_end_to_end_meta_receipt(self):
        r=meta_tower_demo()
        self.assertEqual(r["destructive_full_order_enumeration"],"MODEL_CERTIFIED_NO_FINITE_POLICY")
        self.assertTrue(r["adaptive_succeeds_where_fixed_length_two_fails"])
        self.assertEqual(r["checkpoint_e_knowledge"],[{'index':1,'proved':False},{'index':2,'proved':True}])
        self.assertFalse(r["physical_infinity_completed"])
        self.assertFalse(r["source_authentication_claimed"])


if __name__ == "__main__":
    unittest.main()
