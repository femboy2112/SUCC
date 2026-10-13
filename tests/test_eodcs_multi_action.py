"""Independent multi-action word exhaustive witnesses, darkness and curvature."""
import unittest
from itertools import product
from random import Random

from observational_succ.eodcs_multi_action_source import (
    ActionSource, SourceTransportError, action_congruence,
    shortest_distinguishing_word, action_curvature,
    newly_generated_probe_demo, dark_toolkit_demo, curvature_resolution,
)


def independent_walk(source, s, word):
    """Uses raw transition tables and indices, never ActionSource.run."""
    state=s
    for a in word:
        j=source.actions.index(a)
        state=source.transitions[j][source.states.index(state)]
    return source.outputs[source.states.index(state)]


def all_words(actions, maximum_length):
    for n in range(maximum_length+1):
        yield from product(actions, repeat=n)


class TestMultiActionSUCC(unittest.TestCase):
    def test_two_single_probes_fail_but_composite_A_B_is_new_separator(self):
        r=newly_generated_probe_demo()
        self.assertTrue(r["both_one_action_probes_alias"])
        self.assertEqual(r["synthesized_minimum_word"],["A","B"])
        self.assertEqual(r["synthesized_probe_results"],["0","1"])
        self.assertIn("y",r["observable_two_path_commutator"])
        self.assertFalse(r["physical_implementation_created"])

    def test_dark_pairs_need_new_lamp_not_longer_available_words(self):
        r=dark_toolkit_demo()
        self.assertEqual(r["dark_pair"],["a","b"])
        self.assertTrue(r["all_finite_words_unable_to_separate"])
        self.assertTrue(r["external_lamp_would_separate"])
        self.assertFalse(r["lamp_present_in_available_menu"])
        self.assertFalse(r["physical_source_authenticated"])

    def test_200_random_complete_sources_vs_independent_all_word_oracle(self):
        rng=Random(314159)
        for seed in range(200):
            n=rng.choice((2,3,4,5))
            states=tuple("x"+str(i) for i in range(n))
            reports=tuple(str(rng.randrange(3)) for _ in states)
            trans=tuple(tuple(rng.choice(states) for _ in states)
                        for action in ("A","B"))
            source=ActionSource("declared-"+str(seed),0,"named",
                                states,reports,("A","B"),trans)
            receipt=action_congruence(source)
            self.assertTrue(receipt.finite_fixpoint_verified)
            brute_witness={}
            # n is a conservative complete refinement-horizon bound.
            words=tuple(all_words(source.actions,n))
            for i,s in enumerate(states):
                for t in states[i+1:]:
                    first=next((w for w in words
                                if independent_walk(source,s,w) !=
                                   independent_walk(source,t,w)),None)
                    brute_witness[(s,t)]=first
                    self.assertEqual(
                        shortest_distinguishing_word(source,s,t),first)
            for s,t in receipt.eternally_indistinguishable_pairs:
                self.assertIsNone(brute_witness[s,t])
            expected={p for p,w in brute_witness.items() if w is None}
            self.assertEqual(set(receipt.eternally_indistinguishable_pairs),
                             expected)
            self.assertLessEqual(len(receipt.block_counts),n)
            self.assertTrue(all(a<b for a,b in zip(receipt.block_counts,
                                                    receipt.block_counts[1:])))

    def test_observation_can_hide_noncommutation_in_unseen_fiber(self):
        states=("a","b","c")
        src=ActionSource("s",0,"b",states,("0","0","0"),("U","V"),
                         (("b","a","c"),("a","c","b")))
        r=action_curvature(src,"U","V")
        self.assertTrue(r["source_noncommuting_states"])
        self.assertEqual(r["observable_noncommuting_states"],())
        self.assertTrue(r["source_nonflat_but_observer_flat"])
        self.assertFalse(r["physical_curvature_claimed"])
        self.assertEqual(len(action_congruence(src).equivalence_classes),1)

    def test_one_curvature_immediate_another_dark_in_same_source(self):
        states=("x","y","u","v","c","d")
        src=ActionSource("s",0,"basis",states,("0","0","0","0","0","1"),
                         ("A","B"),
                         (("u","v","u","v","c","d"),
                          ("x","y","c","d","c","d")))
        r=curvature_resolution(src,"A","B")
        self.assertEqual([w[0] for w in r["observable_immediate"]],["y"])
        self.assertEqual([w[0] for w in r["dark_under_available_probe_closure"]],
                         ["x"])
        self.assertEqual(r["observable_after_generated_word"],())
        self.assertFalse(r["physical_curvature_claimed"])

    def test_new_sensor_rotates_dark_source_defect_into_delayed_visibility(self):
        states=("x","y","u","v","c","d")
        src=ActionSource("s",0,"basis",states,("0","0","0","0","0","1"),
                         ("A","B","C"),
                         (("u","v","u","v","c","d"),
                          ("x","y","c","d","c","d"),
                          ("x","y","d","v","c","d")))
        r=curvature_resolution(src,"A","B")
        self.assertEqual([w[0] for w in r["observable_immediate"]],["y"])
        self.assertEqual([(s,w) for s,_,_,w in r["observable_after_generated_word"]],
                         [("x",("C",))])
        self.assertEqual(r["dark_under_available_probe_closure"],())
        self.assertEqual(r["source_noncommuting_state_count"],2)

    def test_110_seeded_curvature_witnesses_against_independent_word_oracle(self):
        rng=Random(3355)
        for _ in range(110):
            n=rng.choice((2,3,4,5))
            states=tuple(str(i) for i in range(n))
            output=tuple(str(rng.randrange(3)) for _ in states)
            trans=tuple(tuple(rng.choice(states) for _ in states)
                        for a in ("A","B"))
            src=ActionSource("s",0,"b",states,output,("A","B"),trans)
            actual=curvature_resolution(src,"A","B")
            immediate={s for s,_,_ in actual["observable_immediate"]}
            delayed={s:w for s,_,_,w in actual["observable_after_generated_word"]}
            dark={s for s,_,_ in actual["dark_under_available_probe_closure"]}
            flat=set(actual["source_flat_states"])
            self.assertEqual(len(immediate)+len(delayed)+len(dark)+len(flat),n)
            for s in states:
                left=src.run(s,("A","B"))
                right=src.run(s,("B","A"))
                brute=next((w for w in all_words(src.actions,n)
                            if independent_walk(src,left,w)!=
                               independent_walk(src,right,w)),None)
                if left==right:
                    self.assertIn(s,flat)
                elif brute is None:
                    self.assertIn(s,dark)
                elif len(brute)==0:
                    self.assertIn(s,immediate)
                else:
                    self.assertEqual(delayed[s],brute)

    def test_curvature_with_injective_report_is_always_visible(self):
        rng=Random(19)
        for _ in range(100):
            states=("a","b","c","d")
            trans=tuple(tuple(rng.choice(states) for _ in states)
                        for a in ("A","B"))
            src=ActionSource("s",0,"b",states,states,("A","B"),trans)
            r=action_curvature(src,"A","B")
            self.assertEqual(set(r["source_noncommuting_states"]),
                             set(r["observable_noncommuting_states"]))
            self.assertFalse(r["source_nonflat_but_observer_flat"])

    def test_immutable_source_and_unavailable_actions_are_gated(self):
        src=ActionSource("s",0,"b",("a","b"),("0","1"),("A",),
                         (("b","a"),))
        with self.assertRaises(SourceTransportError):
            src.run("a",("imaginary",))
        with self.assertRaises(SourceTransportError):
            src.step("ghost","A")
        with self.assertRaises(SourceTransportError):
            shortest_distinguishing_word(src,"a","ghost")
        with self.assertRaises(SourceTransportError):
            action_curvature(src,"A","B")
        with self.assertRaises(SourceTransportError):
            ActionSource("s",0,"b",("a","b"),("0","1"),("A",),
                         (("b","a"),), source_authenticated=True)
        with self.assertRaises(SourceTransportError):
            ActionSource("s",0,"b",("a","b"),("0","1"),("A",),
                         (("b","ghost"),))

    def test_all_six_two_state_two_action_boolean_transition_machines_sample(self):
        # Exhaustively iterate all two-state two-action transition pairs
        # with the nonconstant Boolean report; independent word semantics.
        states=("0","1")
        for u in product(states,repeat=2):
            for v in product(states,repeat=2):
                src=ActionSource("exhaustive",0,"bit",states,states,
                                  ("a","b"),(u,v))
                r=action_congruence(src)
                self.assertEqual(len(r.equivalence_classes),2)
                self.assertEqual(r.block_counts,(2,))
                self.assertEqual(shortest_distinguishing_word(src,"0","1"),())
                self.assertFalse(r.eternally_indistinguishable_pairs)


if __name__=="__main__":
    unittest.main()
