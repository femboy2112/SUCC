"""Exact hostile tests: r=4 Markov quotient and r<4 source-faithful Bayes."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from random import Random
import unittest

from observational_succ.logistic_observer_tree import (
    Source, logistic as logistic4, cylinder, cylinder_mass, tent, symbolic_path
)
from observational_succ.chaos_source_quotient import (
    ChaosQuotientError, exact, logistic_r, parameter, postimage_interval,
    postcritical_threshold, phantom_terminal_fraction, admissible_pair_from_witness, SymbolWindow,
    FiniteLogisticSource,
)


class FiniteWindowTheorems(unittest.TestCase):
    def test_exact_fraction_only(self):
        for x in (0.5,True,'1/2',None):
            with self.assertRaises(ChaosQuotientError): exact(x)
        self.assertEqual(exact(3),F(3))

    def test_window_invalid_lengths_and_probabilities(self):
        for width in (0,-1,13,2.0,True):
            with self.assertRaises(ChaosQuotientError): SymbolWindow(width)
        for p in (F(0),F(1),F(5,4),-F(1,3),True,0.2):
            with self.assertRaises(ChaosQuotientError): SymbolWindow(2,p)

    def test_rows_are_two_fair_legal_paths(self):
        for m in range(1,7):
            kernel=SymbolWindow(m)
            for w in range(kernel.size):
                expected=((w<<1)&(kernel.size-1))
                self.assertEqual(kernel.row(w),{expected:F(1,2),expected+1:F(1,2)})
                self.assertEqual(sum(kernel.row(w).values()),1)

    def test_bad_source_laws_rejected(self):
        w=SymbolWindow(2)
        for law in ({}, {-1:F(1)}, {4:F(1)}, {0:F(2)},
                    {0:F(1,2)}, {0:-F(1), 1:F(2)}, {True:F(1)}):
            with self.subTest(law=law),self.assertRaises(ChaosQuotientError):
                w.push(law)
        for steps in (-1,2.0,True):
            with self.assertRaises(ChaosQuotientError):w.push({0:1},steps)

    def test_steady_distribution_and_direct_stationarity(self):
        for m in range(1,8):
            w=SymbolWindow(m)
            expected={j:F(1,w.size) for j in range(w.size)}
            self.assertEqual(w.equilibrium(),expected)
            self.assertEqual(w.push(expected),expected)

    def test_rank_one_finite_memory_washout(self):
        for m in range(1,7):
            w=SymbolWindow(m)
            target=w.equilibrium()
            for s in range(w.size):
                self.assertEqual(w.push({s:1},m),target)
                self.assertEqual(w.push({s:1},m+1),target)

    def test_partial_support_exact_power_of_two(self):
        for m in range(1,8):
            w=SymbolWindow(m)
            for n in range(0,m+4):
                law=w.push({w.size-1:1},n)
                self.assertEqual(len([p for p in law.values() if p]),2**min(m,n))
                self.assertEqual(sum(law.values(),F(0)),1)
                self.assertEqual(w.causal_path_count(n),2**n)
                self.assertEqual(w.terminal_support_count(n),2**min(m,n))

    def test_history_bit_cost_differs_from_terminal_bit_cost(self):
        r=SymbolWindow(3).source_audit(12)
        self.assertEqual(r['causal_path_count'],4096)
        self.assertEqual(r['full_path_minimum_new_bits'],12)
        self.assertEqual(r['terminal_support_count'],8)
        self.assertEqual(r['terminal_minimum_new_bits'],3)
        self.assertTrue(r['rank_one_completion_reached'])

    def test_failure_of_deterministic_state_factor(self):
        for m in range(1,7):
            w=SymbolWindow(m)
            for state in range(w.size):
                u,v=w.deterministic_factor_counterexample(state)
                self.assertNotEqual(u,v)
                self.assertEqual(u//2,v//2)

    def test_independent_direct_word_construction(self):
        for m in range(1,6):
            q=SymbolWindow(m)
            for n in range(m+2):
                initial=2**m-1
                expected={}
                for bits in product((0,1),repeat=n):
                    state=initial
                    for bit in bits:
                        state=((state<<1)|bit)&(q.size-1)
                    expected[state]=expected.get(state,F(0))+F(1,2**n)
                self.assertEqual(q.push({initial:F(1)},n),expected)

    def test_markov_rows_are_derived_from_real_tent_cylinders(self):
        # This is NOT an abstract fair-coin model disconnected from the
        # deterministic r=4 source: the cylinders ARE true tent cylinders.
        for m in range(1,7):
            w=SymbolWindow(m)
            for bits in product((0,1),repeat=m):
                source_word=0
                for bit in bits:
                    source_word=(source_word<<1)|bit
                parent=cylinder(bits)
                self.assertEqual(parent[1]-parent[0],F(1,2**m))
                for appended in (0,1):
                    child=bits+(appended,)
                    interval=cylinder(child)
                    self.assertEqual(cylinder_mass(child)/cylinder_mass(bits),F(1,2))
                    point=(interval[0]+interval[1])/2
                    self.assertEqual(symbolic_path(point,m+1),child)
                    actual_next=symbolic_path(tent(point),m)
                    observed_word=0
                    for bit in actual_next:
                        observed_word=(observed_word<<1)|bit
                    expected=((source_word<<1)|appended)&(w.size-1)
                    self.assertEqual(observed_word,expected)
                    self.assertEqual(w.row(source_word)[observed_word],F(1,2))

    def test_biased_symbolic_prior_mutation(self):
        w=SymbolWindow(3,F(1,3))
        expected={s:F(1,3)**s.bit_count()*F(2,3)**(3-s.bit_count()) for s in range(8)}
        self.assertEqual(w.equilibrium(),expected)
        self.assertEqual(w.push({0:1},3),expected)
        self.assertEqual(w.push(expected,1),expected)
        self.assertNotEqual(expected, SymbolWindow(3).equilibrium())

    def test_all_small_rational_biases_direct_enumeration(self):
        for m in (1,2,3):
            for p in (F(1,7),F(1,3),F(1,2),F(2,3),F(6,7)):
                w=SymbolWindow(m,p)
                for n in range(m+2):
                    actual=w.push({0:F(1)},n)
                    target={}
                    for bits in product((0,1),repeat=n):
                        word=0
                        prob=F(1)
                        for bit in bits:
                            word=((word<<1)|bit)&(w.size-1)
                            prob*=p if bit else 1-p
                        target[word]=target.get(word,F(0))+prob
                    self.assertEqual(actual,target)

    def test_dual_E_shared_observability_horizon(self):
        w=SymbolWindow(5)
        checks=[(0,32,5,0),(1,16,4,1),(4,2,1,4),(5,1,0,5),(12,1,0,5)]
        for lag,component_count,shared,conditional in checks:
            result=w.dual_common_information(lag)
            self.assertEqual(result['maximal_common_deterministic_component_count'],component_count)
            self.assertEqual(result['shared_symbol_count'],shared)
            self.assertEqual(result['fair_source_mutual_information_bits'],shared)
            self.assertEqual(result['fair_source_conditional_entropy_bits'],conditional)
        with self.assertRaises(ChaosQuotientError):w.dual_common_information(-1)

    def test_dual_E_GK_support_components_independent_graph_oracle(self):
        # Independent construction of the bipartite support graph.
        # Every complete (m+n)-bit symbolic source word has nonzero fair mass.
        for m in range(1,6):
            w=SymbolWindow(m)
            for lag in range(0,7):
                adjacency={}
                for tape in product((0,1),repeat=m+lag):
                    left=tuple(tape[:m])
                    right=tuple(tape[lag:lag+m])
                    a=('L',left)
                    b=('R',right)
                    adjacency.setdefault(a,set()).add(b)
                    adjacency.setdefault(b,set()).add(a)
                seen=set()
                comps=0
                for vertex in adjacency:
                    if vertex in seen:
                        continue
                    comps+=1
                    stack=[vertex]
                    seen.add(vertex)
                    while stack:
                        for nxt in adjacency[stack.pop()]:
                            if nxt not in seen:
                                seen.add(nxt)
                                stack.append(nxt)
                self.assertEqual(comps,w.dual_common_information(lag)
                                      ['maximal_common_deterministic_component_count'])

    def test_biased_common_support_not_fair_entropy(self):
        w=SymbolWindow(4,F(1,3))
        result=w.dual_common_information(2)
        self.assertEqual(result['maximal_common_deterministic_component_count'],4)
        self.assertIsNone(result['fair_source_mutual_information_bits'])
        self.assertIsNone(result['fair_source_conditional_entropy_bits'])

    def test_singular_source_not_arcsine_by_assumption(self):
        self.assertNotEqual(SymbolWindow(4,F(1,3)).equilibrium(),
                            SymbolWindow(4,F(1,2)).equilibrium())

    def test_mutation_missing_one_fair_branch_destroys_full_support(self):
        w=SymbolWindow(4)
        actual=w.push({0:1},4)
        forged={0:F(1)}
        self.assertNotEqual(actual,forged)
        self.assertEqual(len(actual),16)


class LogisticSourceTheorems(unittest.TestCase):
    @staticmethod
    def two(r=3,weights=(F(1,4),F(3,4))):
        return FiniteLogisticSource(Source('one-deterministic-carrier',7),F(r),
                                    (F(1,3),F(2,3)),tuple(weights))

    def test_parameter_and_state_guards(self):
        for r in (0,-1,5,F(17,4),0.25,True):
            with self.assertRaises(ChaosQuotientError):parameter(r)
        for x in (-1,F(11,10),F(-1,100)):
            with self.assertRaises(ChaosQuotientError):logistic_r(4,x)
        for x in (F(0),F(1,8),F(1,2),F(3,4),F(1)):
            self.assertEqual(logistic_r(4,x),logistic4(x))

    def test_postimage_interval_forward_invariant_exact(self):
        for r in (F(1,2),F(2),F(5,2),F(3),F(16,5),F(39,10),F(4)):
            lo,hi=postimage_interval(r)
            self.assertEqual((lo,hi),(0,r/4))
            for i in range(33):
                x=hi*F(i,32)
                self.assertTrue(lo<=logistic_r(r,x)<=hi)

    def test_source_admissible_r3_incomplete_inverse(self):
        a=admissible_pair_from_witness(3,F(1,8))
        self.assertEqual(a['terminal'],F(21,64))
        self.assertEqual(a['postcritical_threshold'],F(9,16))
        self.assertEqual(a['algebraic_preimages'],(F(1,8),F(7,8)))
        self.assertEqual(a['source_admissible_preimages'],(F(1,8),))
        self.assertTrue(a['has_phantom_branch'])
        self.assertEqual(a['algebraic_equal_branch_mean'],F(1,2))
        self.assertEqual(a['admissible_equal_branch_mean'],F(1,8))

    def test_r4_source_no_phantom_preimages(self):
        for i in range(17):
            w=F(i,16)
            a=admissible_pair_from_witness(4,w)
            self.assertFalse(a['has_phantom_branch'])
            self.assertEqual(a['algebraic_preimages'],a['source_admissible_preimages'])

    def test_r3_high_terminal_two_admissible_sources(self):
        a=admissible_pair_from_witness(3,F(1,3))
        self.assertEqual(a['terminal'],F(2,3))
        self.assertEqual(a['source_admissible_preimages'],(F(1,3),F(2,3)))
        self.assertFalse(a['has_phantom_branch'])

    def test_phantom_terminal_fraction_exact_and_nonprobabilistic(self):
        self.assertEqual(phantom_terminal_fraction(3),F(3,4))
        self.assertEqual(phantom_terminal_fraction(F(39,10)),F(39,400))
        self.assertEqual(phantom_terminal_fraction(4),0)
        for r in (F(2),F(3,2)):
            with self.assertRaises(ChaosQuotientError):
                phantom_terminal_fraction(r)

    def test_near_four_every_strict_perturbation_has_a_real_phantom(self):
        for r in (F(5,2),F(3),F(16,5),F(19,5),F(39,10),F(399,100)):
            witness=(1-r/4)/2
            a=admissible_pair_from_witness(r,witness)
            self.assertTrue(0 < a['terminal'] < postcritical_threshold(r))
            self.assertTrue(a['has_phantom_branch'])
            self.assertEqual(a['source_admissible_preimages'],(witness,))
            self.assertEqual(a['admissible_equal_branch_mean'],witness)

    def test_r3_critical_branch_is_a_single_source(self):
        a=admissible_pair_from_witness(3,F(1,2))
        self.assertEqual(a['algebraic_preimages'],(F(1,2),))
        self.assertEqual(a['source_admissible_preimages'],(F(1,2),))

    def test_r3_illegal_predecessor_refused(self):
        with self.assertRaises(ChaosQuotientError):
            admissible_pair_from_witness(3,F(7,8))

    def test_finite_source_rejects_inexact_or_unbound(self):
        s=Source('v',1)
        for originals,weights in (((F(1,3),F(1,3)),(F(1,2),F(1,2))),
                                  ((F(1,3),F(2,3)),(F(1,3),F(1,3))),
                                  ((F(1,3),F(2,3)),(F(0),F(1))),
                                  ((F(-1),F(1,2)),(F(1,2),F(1,2))),
                                  ((.1,F(1,2)),(F(1,2),F(1,2)))):
            with self.assertRaises(ChaosQuotientError):
                FiniteLogisticSource(s,F(3),originals,weights)
        with self.assertRaises(ChaosQuotientError):
            FiniteLogisticSource('untyped',F(3),(F(1,3),),(F(1),))

    def test_source_merge_and_weighted_actual_posterior(self):
        s=self.two()
        self.assertEqual(s.law(0),{F(1,3):F(1,4),F(2,3):F(3,4)})
        self.assertEqual(s.law(1),{F(2,3):F(1)})
        self.assertEqual(s.reverse_kernel(0),{F(2,3):{F(1,3):F(1,4),F(2,3):F(3,4)}})
        # Posterior mean is 7/12, not algebraic equal branch mean 1/2.
        self.assertEqual(s.backwards_target(s.originals,1),{F(2,3):F(7,12)})
        self.assertNotEqual(F(7,12),F(1,2))

    def test_equal_inverse_branch_algebra_is_not_generic_bayes(self):
        for r in (3,4):
            s=self.two(r)
            y=logistic_r(r,F(1,3))
            self.assertEqual(s.backwards_target(s.originals,1)[y],F(7,12))
            self.assertEqual(admissible_pair_from_witness(r,F(1,3))['algebraic_equal_branch_mean'],F(1,2))

    def test_koopman_reverse_left_inverse_on_support(self):
        s=self.two()
        for step in range(3):
            before=s.law(step)
            kernel=s.reverse_kernel(step)
            for y,dist in kernel.items():
                self.assertEqual(sum(dist.values(),F(0)),1)
                self.assertEqual(sum((p*(3+2*logistic_r(s.r,x))
                                     for x,p in dist.items()),F(0)),3+2*y)
                self.assertEqual(sum((before[x] for x in dist),F(0)),s.law(step+1)[y])

    def test_forward_then_backwards_does_not_invert_source(self):
        s=self.two()
        y=F(2,3)
        conditional=s.backwards_target((0,1),1)[y]
        self.assertEqual(conditional,F(3,4))
        self.assertNotEqual(conditional,F(0))
        self.assertNotEqual(conditional,F(1))

    def test_source_fiber_original_target_factor(self):
        s=self.two()
        self.assertFalse(s.claim_factors((0,1),1))
        self.assertTrue(s.claim_factors((5,5),1))
        self.assertTrue(s.claim_factors((0,1),0))

    def test_dual_observers_join_trajectory(self):
        s=self.two()
        y=F(2,3)
        self.assertEqual(s.source_fiber(1,y),(F(1,3),F(2,3)))
        self.assertEqual(s.source_fiber(1,y,(0,),s.source),(F(1,3),))
        self.assertEqual(s.source_fiber(1,y,(1,),s.source),(F(2,3),))
        self.assertEqual(s.source_fiber(1,F(1,4)),())

    def test_stale_source_join_rejected(self):
        s=self.two()
        for other in (Source('one-deterministic-carrier',8),Source('forged',7)):
            with self.assertRaises(ChaosQuotientError):
                s.source_fiber(1,F(2,3),(0,),other)
        with self.assertRaises(ChaosQuotientError):
            s.source_fiber(1,F(2,3),(0,1))
        with self.assertRaises(ChaosQuotientError):
            s.source_fiber(1,F(2,3),(2,))

    def test_finite_horizons_and_targets_rejected(self):
        s=self.two()
        for t in (-1,51,2.5,True):
            with self.assertRaises(ChaosQuotientError):s.orbit(t)
        for t in (-1,50):
            with self.assertRaises(ChaosQuotientError):s.reverse_kernel(t)
        with self.assertRaises(ChaosQuotientError):s.backwards_target((0,),1)
        with self.assertRaises(ChaosQuotientError):s.direct_target((0,),1)
        with self.assertRaises(ChaosQuotientError):s.claim_factors((0,),0)

    def test_direct_oracle_tower_bayes_replay_with_collisions(self):
        rands=Random(20261012)
        for r in (F(2),F(3),F(16,5),F(4)):
            for _ in range(35):
                distinct=tuple(sorted(rands.sample(range(1,15),rands.randint(2,5))))
                atoms=tuple(F(q,16) for q in distinct)
                raw=[rands.randint(1,9) for _ in atoms]
                weights=tuple(F(p,sum(raw)) for p in raw)
                source=FiniteLogisticSource(Source('seeded',4),r,atoms,weights)
                vals=tuple(F(rands.randint(-10,10),rands.randint(1,5)) for _ in atoms)
                for step in range(4):
                    self.assertEqual(source.backwards_target(vals,step),source.direct_target(vals,step))
                    for y, posterior in source.reverse_kernel(step).items():
                        self.assertEqual(sum(posterior.values(),F(0)),1)
                        self.assertEqual(set(posterior),{x for x in source.law(step)
                                                          if logistic_r(r,x)==y})

    def test_even_split_includes_two_distinct_pasts(self):
        source=FiniteLogisticSource(Source('different-prior',0),F(4),
                                    (F(1,4),F(3,4)),(F(1,2),F(1,2)))
        self.assertEqual(source.law(1),{F(3,4):F(1)})
        self.assertEqual(source.reverse_kernel(0)[F(3,4)],{F(1,4):F(1,2),F(3,4):F(1,2)})
        self.assertFalse(source.claim_factors((1,0),1))

    def test_delayed_source_collision_demands_time_indexed_reverse_kernel(self):
        s=FiniteLogisticSource(Source('delayed-source',0),F(4),
                               (F(0),F(1,2)),(F(1,3),F(2,3)))
        self.assertEqual(s.law(0),{F(0):F(1,3),F(1,2):F(2,3)})
        self.assertEqual(s.law(1),{F(0):F(1,3),F(1):F(2,3)})
        self.assertEqual(s.law(2),{F(0):F(1)})
        self.assertEqual(s.reverse_kernel(0),{F(0):{F(0):1},F(1):{F(1,2):1}})
        self.assertEqual(s.reverse_kernel(1),{F(0):{F(0):F(1,3),F(1):F(2,3)}})
        self.assertEqual(s.backwards_target((0,1),2),{F(0):F(2,3)})
        self.assertEqual(s.backwards_target((0,1),2),s.direct_target((0,1),2))
        self.assertNotEqual(s.reverse_kernel(0).get(F(0)),s.reverse_kernel(1).get(F(0)))

    def test_source_prior_weights_change_bayes_not_forward_dynamics(self):
        a=self.two(weights=(F(1,4),F(3,4)))
        b=self.two(weights=(F(3,4),F(1,4)))
        self.assertEqual(a.orbit(2),b.orbit(2))
        self.assertNotEqual(a.backwards_target(a.originals,1),b.backwards_target(b.originals,1))

    def test_source_cannot_identify_physical_attestation(self):
        s=self.two()
        self.assertEqual(s.source.name,'one-deterministic-carrier')
        self.assertEqual(s.source.version,7)
        self.assertEqual(s.source_fiber(1,F(2,3),(0,),s.source),(F(1,3),))
        # Source tags and the local deterministic replay are mathematical, not signatures.


if __name__ == '__main__':
    unittest.main()
