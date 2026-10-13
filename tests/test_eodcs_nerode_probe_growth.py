"""Exact finite future-language refinement and independent long-path oracle."""
import unittest
from itertools import combinations, product
from random import Random

from observational_succ.nerode_probe_growth import (
    ObserverDynamics, SourceTransportError, delayed_signal_chain,
    independently_seeded_unknown_dynamics, nerode_fixpoint,
    grow_probe_grammar, nerode_moonshot_demo,
)


def brute_future_trace(source, state, steps):
    """A distinct direct trajectory simulator, not source.probe or .word."""
    mapping=dict(zip(source.states,source.next_states))
    outputs=dict(zip(source.states,source.reports))
    result=[]
    for _ in range(steps):
        result.append(outputs[state])
        state=mapping[state]
    return tuple(result)


class TestNerodeSUCC(unittest.TestCase):
    def test_long_succ_ladders_have_exact_linear_debt_and_no_uniform_bound(self):
        for n in range(2,13):
            src=delayed_signal_chain(n)
            r=nerode_fixpoint(src)
            self.assertEqual(r.stabilization_horizon, n-2)
            self.assertEqual(r.block_counts, tuple(range(2,n+1)))
            self.assertEqual(len(r.stable_classes),n)
            p=grow_probe_grammar(src)
            self.assertEqual(len(p.exact_minimum_cost_offsets),n-1)
            self.assertEqual(p.exact_minimum_cost_offsets,tuple(range(n-1)))
            self.assertEqual(p.exact_declared_cost,n*(n-1)//2)
            self.assertEqual(p.greedy_declared_cost,p.exact_declared_cost)

    def test_bounded_n_stable_partition_implies_all_future_equivalence(self):
        for seed in range(180):
            src=independently_seeded_unknown_dynamics(seed)
            r=nerode_fixpoint(src)
            n=len(src.states)
            self.assertLess(r.stabilization_horizon,n)
            # Independent raw simulation goes far past the stabilization bound.
            trace={s:brute_future_trace(src,s,4*n+17) for s in src.states}
            expected={
                (s,t) for i,s in enumerate(src.states) for t in src.states[i+1:]
                if trace[s]==trace[t]
            }
            self.assertEqual(expected,set(r.indistinguishable_pairs))
            for s,t,first in r.first_distinguishers:
                self.assertEqual(first,next(k for k in range(4*n+17)
                                            if trace[s][k]!=trace[t][k]))
            # Every returned quotient transition must map whole classes.
            lookup={s:i for i,c in enumerate(r.stable_classes) for s in c}
            for i,block in enumerate(r.stable_classes):
                self.assertEqual(len({lookup[src.step(s)] for s in block}),1)
                self.assertEqual(len({src.report(s) for s in block}),1)
                self.assertEqual(int(r.source_transition_quotient[i][1]),
                                 lookup[src.step(block[0])])

    def test_no_premature_plateau_then_later_split_in_fixed_source(self):
        for seed in range(70):
            src=independently_seeded_unknown_dynamics(seed)
            r=nerode_fixpoint(src)
            h=r.stabilization_horizon
            self.assertEqual(src.future_classes(h),
                             src.future_classes(h+1))
            for more in (h+2,h+10,h+30):
                self.assertEqual(src.future_classes(h),
                                 src.future_classes(more))
            self.assertFalse(r.actually_infinite_source_examined)

    def test_unknown_state_immutable_source_mutation_rejected(self):
        s=delayed_signal_chain(5)
        with self.assertRaises(SourceTransportError):s.step("ghost")
        with self.assertRaises(SourceTransportError):s.report("ghost")
        with self.assertRaises(SourceTransportError):s.probe("s0",-1)
        with self.assertRaises(SourceTransportError):s.word("s0",-2)
        with self.assertRaises(SourceTransportError):s.classes((0,0))
        with self.assertRaises(SourceTransportError):
            ObserverDynamics("s",0,"b",("a","b"),("a","ghost"),("x","y"))
        with self.assertRaises(SourceTransportError):
            ObserverDynamics("s",0,"b",("a",),("a",),("x",),
                             source_authenticated=True)

    def test_exact_probe_set_hitting_oracle_is_distinct_from_greedy(self):
        rng=Random(7372)
        for seed in range(100):
            src=independently_seeded_unknown_dynamics(seed,n=6)
            r=nerode_fixpoint(src)
            p=grow_probe_grammar(src)
            D=r.stabilization_horizon
            trace={s:brute_future_trace(src,s,D+1) for s in src.states}
            need={(s,t) for i,s in enumerate(src.states)
                  for t in src.states[i+1:] if trace[s]!=trace[t]}
            candidates=[]
            for count in range(D+2):
                for offsets in combinations(range(D+1),count):
                    resolved=all(any(trace[s][i]!=trace[t][i] for i in offsets)
                                 for s,t in need)
                    if resolved:
                        candidates.append((sum(i+1 for i in offsets),
                                           len(offsets),offsets))
            self.assertEqual(min(candidates)[2],p.exact_minimum_cost_offsets)
            self.assertGreaterEqual(p.greedy_declared_cost,p.exact_declared_cost)
            self.assertTrue(p.greedy_steps_reduce_unresolved_pairs)
            self.assertFalse(p.physical_counterfactual_reset_available)

    def test_greedy_search_is_not_a_global_optimizer_hard_counterexample(self):
        states=tuple("s"+str(i) for i in range(7))
        u=(5,6,0,6,2,4,3)
        outputs=(2,2,0,2,1,2,0)
        s=ObserverDynamics("greedy-falsifier",0,"tri",states,
                           tuple(states[i] for i in u),
                           tuple(str(v) for v in outputs))
        p=grow_probe_grammar(s)
        self.assertEqual(p.horizon,2)
        self.assertEqual(p.greedy_offsets,(0,1,2))
        self.assertEqual(p.exact_minimum_cost_offsets,(0,2))
        self.assertEqual(p.greedy_declared_cost,6)
        self.assertEqual(p.exact_declared_cost,4)
        self.assertGreater(p.greedy_declared_cost,p.exact_declared_cost)

    def test_genuinely_aliasing_model_is_not_invented_as_true_ontology(self):
        src=ObserverDynamics("alias",0,"b",("a","b","c","d"),
                             ("b","a","d","c"),("x","x","y","y"))
        r=nerode_fixpoint(src)
        self.assertEqual(r.stabilization_horizon,0)
        self.assertEqual(r.stable_classes,(("a","b"),("c","d")))
        self.assertEqual(r.indistinguishable_pairs,(("a","b"),("c","d")))
        self.assertEqual(len(r.source_transition_quotient),2)
        self.assertEqual(grow_probe_grammar(src).exact_minimum_cost_offsets,(0,))

    def test_source_version_and_action_names_preserved(self):
        s=ObserverDynamics("explicit",9,"typed",("a","b"),
                           ("b","a"),("0","1"),action="U")
        p=grow_probe_grammar(s)
        self.assertEqual(p.source_id,"explicit")
        self.assertEqual(p.generated_expression_grammar,("q",))
        with self.assertRaises(SourceTransportError):
            grow_probe_grammar(delayed_signal_chain(8),budget_horizon=3)
        with self.assertRaises(SourceTransportError):
            grow_probe_grammar(s,cost_per_successor=0)

    def test_moonshot_receipt_hard_source_firewalls(self):
        r=nerode_moonshot_demo()
        self.assertEqual(r["source_relative_stabilization_horizon"],6)
        self.assertEqual(r["Nerode_class_counts"],[2,3,4,5,6,7,8])
        self.assertEqual(r["minimum_source_specific_probe_basis"],
                         [0,1,2,3,4,5,6])
        self.assertEqual(r["seeded_independent_source_count"],20)
        self.assertTrue(r["all_test_sources_congruence_checked"])
        self.assertFalse(r["unbounded_uniform_finite_bound_claimed"])


if __name__=="__main__":
    unittest.main()
