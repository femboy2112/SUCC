"""Independent AND/OR policy-tree checks and adaptive/source-backaction controls."""
from itertools import product
from functools import lru_cache
import random
import unittest

from observational_succ.adaptive_proof_policy import (
    PolicyError, solve_adaptive_claim, conditional_source_field,
    adaptive_policy_demo,
)
from observational_succ.noncommuting_proof_transport import (
    FiniteCarrier,Instrument,_bit_field,
)


def brute_can_decide(field,sources,target,horizon):
    """Independent depth-h minimax policy evaluator; no shared solver helpers."""
    start=tuple((s,s) for s in sources)

    @lru_cache(None)
    def rec(worlds,n):
        observed_truths={target[source] for source,_ in worlds}
        if len(observed_truths)==1:
            return True
        if n==0:
            return False
        for probe in field.actions:
            if any(not probe.enabled[current] for _,current in worlds):
                continue
            buckets={}
            for original,current in worlds:
                reported,next_state=probe.step(current)
                buckets.setdefault(reported,[]).append((original,next_state))
            if all(rec(tuple(sorted(set(branch))),n-1)
                   for branch in buckets.values()):
                return True
        return False
    return rec(start,horizon)


class AdaptiveSourcePolicyTests(unittest.TestCase):
    def test_destructive_observers_cannot_decide_original_parity_by_any_policy(self):
        field=_bit_field()
        target=("0","1","1","0")
        result=solve_adaptive_claim(field,(0,1,2,3),target,
                                    target_id="original-parity")
        self.assertFalse(result.winning)
        self.assertIsNone(result.rank)
        self.assertGreater(result.reachable,1)
        for horizon in range(8):
            self.assertFalse(brute_can_decide(field,(0,1,2,3),target,horizon))
        with self.assertRaises(PolicyError):
            result.simulate(0)

    def test_true_reversible_backaction_allows_an_adaptive_two_probe_proof(self):
        field=conditional_source_field()
        goal=("0","1","1","0")
        verdict=solve_adaptive_claim(field,(0,1,2,3),goal,
                                     target_id="original-parity")
        self.assertTrue(verdict.winning)
        self.assertEqual(verdict.rank,2)
        self.assertFalse(brute_can_decide(field,(0,1,2,3),goal,1))
        self.assertTrue(brute_can_decide(field,(0,1,2,3),goal,2))
        for s in range(4):
            run=verdict.simulate(s)
            self.assertEqual(run["outcome"],goal[s])
            self.assertEqual(run["steps"],2)
            self.assertEqual(run["trace"][0][0],"Q")
            self.assertEqual(run["trace"][1][0],
                             "R0" if s//2==0 else "R1")
        self.assertNotEqual(field.run(2,("Q",)).terminal_state,2)

    def test_adaptive_choice_beats_every_fixed_two_action_word(self):
        field=conditional_source_field()
        target=("0","1","1","0")
        actions=("Q","R0","R1")
        for word in product(actions,repeat=2):
            groups={}
            for original in range(4):
                report=field.run(original,word).observed_values
                groups.setdefault(report,set()).add(target[original])
            self.assertTrue(any(len(vals)>1 for vals in groups.values()),
                            f"Unexpected uniform fixed-path proof {word}")

    def test_joint_and_nondestructive_repairs_are_operational(self):
        target=("0","1","1","0")
        for system,depth in ((_bit_field(nondestructive=True),2),
                             (_bit_field(with_joint=True),1)):
            result=solve_adaptive_claim(system,(0,1,2,3),target,target_id="xor")
            self.assertTrue(result.winning)
            self.assertEqual(result.rank,depth)
            for source in range(4):
                self.assertEqual(result.simulate(source)["outcome"],target[source])

    def test_supported_source_law_can_reduce_depth_without_new_observation(self):
        system=_bit_field()
        t=("0","1","1","0")
        prior_same=solve_adaptive_claim(system,(0,3),t,target_id="xor")
        self.assertTrue(prior_same.winning)
        self.assertEqual(prior_same.rank,0)
        rival_class=solve_adaptive_claim(system,(0,1),t,target_id="xor")
        self.assertTrue(rival_class.winning)
        self.assertEqual(rival_class.rank,1)
        self.assertTrue(brute_can_decide(system,(0,1),t,1))

    def test_public_menu_distinction_is_not_a_free_unrecorded_probe(self):
        menu=FiniteCarrier(2,(
            Instrument("only-zero",(0,0),(0,1),(True,False)),
        ),"private-feasibility-source","v1")
        target=("a","b")
        result=solve_adaptive_claim(menu,(0,1),target,target_id="state-bit")
        self.assertFalse(result.winning)
        # Unlike a separate bisimulation model that explicitly EXPOSES
        # menus, this planner only chooses actions executable at EVERY
        # world in current belief. Availability is not an observation.

    def test_exhaust_all_256_two_state_two_action_fields_vs_brute_depth(self):
        arr=tuple(product((0,1),repeat=4))
        for a_spec in arr:
            for b_spec in arr:
                system=FiniteCarrier(2,(
                    Instrument("A",a_spec[:2],a_spec[2:],(True,True)),
                    Instrument("B",b_spec[:2],b_spec[2:],(True,True))
                ),"source","v1")
                verdict=solve_adaptive_claim(
                    system,(0,1),("0","1"),target_id="original-state")
                brute=[brute_can_decide(system,(0,1),("0","1"),h)
                       for h in range(6)]
                first=next((i for i,v in enumerate(brute) if v),None)
                self.assertEqual(verdict.rank,first)
                if verdict.winning:
                    for s in (0,1):
                        self.assertEqual(verdict.simulate(s)["outcome"],str(s))

    def test_random_multistate_targets_against_brute_finite_horizon(self):
        rng=random.Random(271828)
        for case in range(80):
            count=rng.choice((2,3,4))
            src=tuple(range(count))
            actions=tuple(
                Instrument(name,tuple(rng.randrange(3) for _ in src),
                           tuple(rng.randrange(count) for _ in src),
                           (True,)*count)
                for name in ("A","B","C"))
            f=FiniteCarrier(count,actions,f"S{case}","B")
            targets=tuple(str(rng.randrange(3)) for _ in src)
            verdict=solve_adaptive_claim(f,src,targets,target_id="target")
            for depth in range(5):
                self.assertEqual(brute_can_decide(f,src,targets,depth),
                                 verdict.rank is not None and verdict.rank<=depth)

    def test_bad_sources_and_tight_closure_budget_fail_honestly(self):
        f=conditional_source_field()
        with self.assertRaises(PolicyError):
            solve_adaptive_claim(f,(0,1,2,3),("0",),
                                 target_id="broken")
        with self.assertRaises(PolicyError):
            solve_adaptive_claim(f,(0,1,2,3),("0","1","1","0"),
                                 target_id="target",max_beliefs=1)
        with self.assertRaises(Exception):
            solve_adaptive_claim(f,(0,0),("0","1","1","0"),
                                 target_id="duplicate-sources")

    def test_machine_receipt(self):
        d=adaptive_policy_demo()
        self.assertEqual(d["status"],"FINITE_ADAPTIVE_SOURCE_PROOF_GAME_EXACT")
        self.assertFalse(d["destructive_original_parity_winning"])
        self.assertTrue(d["nondestructive_original_parity_winning"])
        self.assertEqual(d["nondestructive_worst_case"],2)
        self.assertEqual(d["joint_probe_worst_case"],1)
        self.assertTrue(d["reversible_state_changing_conditional_probe"])
        self.assertTrue(d["adaptive_conditional_original_parity_winning"])
        self.assertEqual(d["adaptive_conditional_worst_case"],2)
        self.assertFalse(d["any_fixed_two_probe_word_succeeds"])
        self.assertEqual(d["adaptive_action_words"],
                         [["Q","R0"],["Q","R0"],["Q","R1"],["Q","R1"]])
        self.assertFalse(d["original_source_given_to_policy"])
        self.assertFalse(d["menus_offered_as_free_readings"])
        self.assertFalse(d["actual_hardware_or_RH_theorem_claimed"])


if __name__=="__main__":
    unittest.main()
