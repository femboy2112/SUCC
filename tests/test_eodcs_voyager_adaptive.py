"""Independent finite adaptive-source indistinguishability counteroracles."""
import unittest
from itertools import product
from random import Random

from observational_succ.voyager_adaptive_no_go import (
    AdaptiveFinitePolicy, FinitePatchStream, VoyagerPolicyError,
    replay_policy, adaptive_finite_probe_no_go, generated_policy,
    adaptive_no_go_demo,
)
from observational_succ.voyager_profinite_frontier import powers_of_two_pulse


class TestVoyagerAdaptiveSourceNoGo(unittest.TestCase):
    def test_adaptive_decision_impossibility_on_two_source_tail_classes(self):
        r=adaptive_no_go_demo()
        self.assertEqual(r["finite_adaptive_queries"],5)
        self.assertTrue(r["both_witnesses_replay_same_exact_transcript"])
        self.assertTrue(r["one_stream_eventually_zero"])
        self.assertFalse(r["other_stream_eventually_zero"])
        self.assertTrue(r["terminal_decision_for_both_source_classes_not_possible"])
        self.assertFalse(r["physical_adaptive_measurement_executed"])

    def test_80_seeded_history_dependent_query_trees_replay_independently(self):
        rng=Random(2886)
        for trial in range(80):
            horizon=rng.randrange(1,7)
            table=tuple((bits,rng.randrange(0,37))
                        for depth in range(horizon)
                        for bits in product((0,1),repeat=depth))
            policy=AdaptiveFinitePolicy(
                "source"+str(trial),trial,"signed-observation",horizon,table)
            targets=(
                lambda n: int(n%2==0),
                powers_of_two_pulse,
                lambda n:int(n%3==0),
            )
            for target in targets:
                claim=bool(rng.randrange(2))
                r=adaptive_finite_probe_no_go(policy,target,claim)
                self.assertTrue(r.source_transcripts_identical)
                self.assertTrue(r.at_least_one_terminal_label_wrong)
                self.assertNotEqual(r.eventually_zero_witness.eventually_zero,
                                    r.non_eventually_zero_witness.eventually_zero)
                original=replay_policy(policy,target)
                a=replay_policy(policy,r.eventually_zero_witness.report)
                b=replay_policy(policy,r.non_eventually_zero_witness.report)
                self.assertEqual(a,original)
                self.assertEqual(b,original)
                bound=max((n for n,_ in original),default=-1)+1
                for index in range(bound,bound+15):
                    self.assertEqual(r.eventually_zero_witness.report(index),0)
                    self.assertEqual(r.non_eventually_zero_witness.report(index),1)

    def test_exhaustive_two_step_adaptive_query_choices_and_outputs(self):
        # All 8 complete binary trees of depth 2 with probe labels {0,1}.
        nodes=((),(0,),(1,))
        for coords in product((0,1),repeat=3):
            p=AdaptiveFinitePolicy(
                "s",0,"b",2,tuple(zip(nodes,coords)))
            for target_bits in product((0,1),repeat=2):
                target=lambda n,b=target_bits: b[n]
                for label in (False,True):
                    r=adaptive_finite_probe_no_go(p,target,label)
                    self.assertTrue(r.at_least_one_terminal_label_wrong)
                    self.assertEqual(
                        replay_policy(p,r.eventually_zero_witness.report),
                        r.original_transcript)
                    self.assertEqual(
                        replay_policy(p,r.non_eventually_zero_witness.report),
                        r.original_transcript)

    def test_repeated_same_coordinate_must_preserve_original_value(self):
        p=AdaptiveFinitePolicy(
            "repeat-source",0,"basis",3,
            tuple((bits,0) for n in range(3)
                  for bits in product((0,1),repeat=n)))
        r=adaptive_finite_probe_no_go(p,lambda n: 1,False)
        self.assertEqual(r.original_transcript,((0,1),(0,1),(0,1)))
        self.assertEqual(r.eventually_zero_witness.observed,((0,1),))
        self.assertEqual(r.non_eventually_zero_witness.observed,((0,1),))

    def test_invalid_policy_source_and_outcome_mutations_rejected(self):
        with self.assertRaises(VoyagerPolicyError):
            AdaptiveFinitePolicy("bad",0,"b",2,(((),0),((0,),1)))
        with self.assertRaises(VoyagerPolicyError):
            AdaptiveFinitePolicy("bad",0,"b",1,(((),0),),
                                 physical_reset_available=True)
        with self.assertRaises(VoyagerPolicyError):
            AdaptiveFinitePolicy("bad",0,"b",1,(((),0),),
                                 empirically_authenticated=True)
        with self.assertRaises(VoyagerPolicyError):
            FinitePatchStream("s",0,"b",((3,0),(3,1)),0)
        with self.assertRaises(VoyagerPolicyError):
            FinitePatchStream("s",0,"b",((3,2),),1)
        p=generated_policy(3)
        with self.assertRaises(VoyagerPolicyError):
            adaptive_finite_probe_no_go(p,lambda n:2,True)
        with self.assertRaises(VoyagerPolicyError):
            adaptive_finite_probe_no_go(p,lambda n:0,"confident")
        with self.assertRaises(VoyagerPolicyError):
            generated_policy(0)


if __name__=="__main__":
    unittest.main()
