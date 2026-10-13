"""Independent exact controls for source-changing probability swarm missions."""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.swarm_probability import (
    CPInstrument, Experiment, ProbabilityError, SearchBudgetError,
    StochasticHistory, StochasticInstrument, bayes_product_square,
    causal_ville_audit, commutation_defect, compose, compose_cp,
    conditional_product, density, find_garbling, garbling_verifies,
    law_descent, optimal_zero_error_cost, reversible_memory_lift,
)


def deterministic(name, reports, after, *, cost=1, source="bits", space="bits"):
    return StochasticInstrument(name, source, space, space, len(after),
                                tuple(((r, y, Q(1)),) for r, y in zip(reports, after)), Q(cost))


def bits():
    states = tuple(range(4))
    a, b = tuple(s//2 for s in states), tuple(s % 2 for s in states)
    return (deterministic("goodA", a, states),
            deterministic("badA", a, tuple(2*(s//2) for s in states)),
            deterministic("badB", b, tuple(s % 2 for s in states)))


def latent_original():
    # H and reused L: P(L=1|H=0)=3/4; P(L=1|H=1)=1/4.
    return StochasticHistory.from_joint("latent", "HL", (
        (Q(1,8), Q(3,8), 0, 0), (0, 0, Q(3,8), Q(1,8))))


def repeated_latent_read():
    return deterministic("readL", tuple("yes" if s % 2 else "no" for s in range(4)),
                         tuple(range(4)), source="latent", space="HL")


def independent_kernel_read():
    rows = []
    for s in range(4):
        p = Q(3,4) if s < 2 else Q(1,4)
        rows.append((("yes", s, p), ("no", s, 1-p)))
    return StochasticInstrument("fresh", "latent", "HL", "HL", 4, tuple(rows))


class HistoryDescentTests(unittest.TestCase):
    def test_unrestricted_instrument_can_report_before_reset(self):
        read_reset = StochasticInstrument("read_reset", "bit", "bit", "zero", 1,
                                          ((("zero", 0, 1),), (("one", 0, 1),)))
        root = StochasticHistory.original("bit", "bit", (Q(1,2), Q(1,2)))
        h0, h1 = root.advance(read_reset, "zero"), root.advance(read_reset, "one")
        self.assertEqual(h0.current_posterior, h1.current_posterior)
        self.assertEqual(h0.original_posterior, (1, 0))
        self.assertEqual(h1.original_posterior, (0, 1))
        self.assertTrue(h0.verify({"read_reset": read_reset}))
        # No T(y|x) E(r|y) on the singleton post-carrier can realize these rows.
        self.assertNotEqual(read_reset.rows[0], read_reset.rows[1])

    def test_original_current_correlation_not_recovered_from_marginals(self):
        coupled = StochasticHistory.from_joint("s", "b", ((Q(1,2), 0), (0, Q(1,2))))
        independent = StochasticHistory.from_joint("s", "b", ((Q(1,4), Q(1,4)),)*2)
        self.assertEqual(coupled.current_posterior, independent.current_posterior)
        self.assertEqual(coupled.original_posterior, independent.original_posterior)
        read = deterministic("read", (0, 1), (0, 1), source="s", space="b")
        self.assertEqual(coupled.advance(read, 1).original_posterior, (0, 1))
        self.assertEqual(independent.advance(read, 1).original_posterior, (Q(1,2), Q(1,2)))

    def test_composition_matches_independent_latent_path_sum(self):
        first = StochasticInstrument("first", "s", "x", "y", 2, (
            (("a", 0, Q(1,4)), ("b", 1, Q(3,4))),
            (("a", 1, Q(1,2)), ("b", 0, Q(1,2)))))
        second = StochasticInstrument("second", "s", "y", "z", 2, (
            (("c", 1, Q(2,3)), ("d", 0, Q(1,3))),
            (("c", 0, Q(1,5)), ("d", 1, Q(4,5)))))
        root = StochasticHistory.original("s", "x", (Q(2,7), Q(5,7)))
        combined = compose(first, second)
        for a, b in product(first.outcomes, second.outcomes):
            direct = [[Q(0), Q(0)] for _ in range(2)]
            for original, prior in enumerate((Q(2,7), Q(5,7))):
                for report, middle, p in first.rows[original]:
                    for last, after, q in second.rows[middle]:
                        if report == a and last == b:
                            direct[original][after] += prior*p*q
            total = sum((sum(row, Q(0)) for row in direct), Q(0))
            staged = root.advance(first, a).advance(second, b)
            single = root.advance(combined, (a, b))
            self.assertEqual(staged.joint, tuple(tuple(v/total for v in row) for row in direct))
            self.assertEqual(single.joint, staged.joint)
            self.assertEqual(single.path_probability, total)
            self.assertEqual(staged.path_probability, total)

    def test_associativity_after_canonical_report_reassociation(self):
        a = deterministic("a", (0, 1), (1, 0), source="s", space="b")
        b = deterministic("b", ("x", "y"), (0, 1), source="s", space="b")
        c = deterministic("c", ("p", "q"), (0, 0), source="s", space="b")
        left, right = compose(compose(a,b),c), compose(a,compose(b,c))
        for lrow, rrow in zip(left.rows, right.rows):
            self.assertEqual({(u,v,w,y): p for ((u,v),w),y,p in lrow},
                             {(u,v,w,y): p for (u,(v,w)),y,p in rrow})

    def test_stale_source_carrier_and_impossible_event_are_rejected(self):
        h = StochasticHistory.original("bits", "bits", (1,0,0,0))
        good, _, _ = bits()
        with self.assertRaises(ProbabilityError):
            h.advance(good, 1)
        with self.assertRaises(ProbabilityError):
            h.advance(replace(good, source_id="other"), 0)
        with self.assertRaises(ProbabilityError):
            h.advance(replace(good, input_space="future"), 0)

    def test_replay_detects_original_law_corruption(self):
        h = latent_original().advance(repeated_latent_read(), "yes")
        bad = replace(h, joint=((0, 0, 0, 0), (0, 0, 0, 1)))
        with self.assertRaises(ProbabilityError):
            bad.verify({"readL": repeated_latent_read()})

    def test_float_and_negative_and_unnormalized_kernel_rejected(self):
        for rows in (((("a",0,0.5),("b",0,0.5)),),
                     ((("a",0,Q(-1)),("b",0,Q(2))),),
                     ((("a",0,Q(1,2)),),)):
            with self.assertRaises(ProbabilityError):
                StochasticInstrument("bad", "s", "x", "x", 1, rows)

    def test_equal_support_different_laws_fail_descent(self):
        action = StochasticInstrument("coin", "s", "x", "y", 1, (
            (("yes",0,Q(1,4)),("no",0,Q(3,4))),
            (("yes",0,Q(3,4)),("no",0,Q(1,4)))))
        result = law_descent(action, ("same", "same"), ("constant",))
        self.assertFalse(result.descends)
        self.assertEqual(result.witness, (1,0))
        self.assertEqual({r for r,_,_ in action.rows[0]}, {r for r,_,_ in action.rows[1]})
        self.assertEqual(len(set(result.refinement)),2)

    def test_law_descent_positive_full_fiber_control(self):
        action = StochasticInstrument("coin", "s", "x", "y", 2, (
            (("yes",0,Q(1,3)),("no",1,Q(2,3))),
            (("yes",1,Q(1,3)),("no",0,Q(2,3)))))
        self.assertTrue(law_descent(action,(0,0),(0,0)).descends)
        self.assertFalse(law_descent(action,(0,0),(0,1)).descends)


class BayesTests(unittest.TestCase):
    def test_duplicated_evidence_independently_reproduced(self):
        read = repeated_latent_read()
        first = latent_original().advance(read,"yes")
        second = first.advance(read,"yes")
        self.assertEqual(first.original_posterior[0],Q(3,4))
        self.assertEqual(second.original_posterior[0],Q(3,4))
        self.assertEqual(second.events[-1].conditional_probability,1)
        self.assertEqual(second.path_probability,first.path_probability)
        fresh = independent_kernel_read()
        independent = latent_original().advance(fresh,"yes").advance(fresh,"yes")
        self.assertEqual(independent.original_posterior[0],Q(9,10))

    def test_separator_evidence_counted_once_in_correct_product_square(self):
        separator = (Q(1,2),Q(1,2))
        left, right = ((Q(1,3),Q(2,3)),(Q(3,4),Q(1,4))), ((Q(2,5),Q(3,5)),)*2
        u = ((Q(3,4),Q(3,4)),(Q(1,4),Q(1,4)))
        direct, staged = bayes_product_square(separator,left,right,u,((1,1),(1,1)))
        self.assertEqual(direct,staged)
        self.assertEqual(sum((p for row in direct[0] for p in row),Q(0)),Q(3,4))
        squared,_ = bayes_product_square(separator,left,right,u,u)
        self.assertEqual(sum((p for row in squared[0] for p in row),Q(0)),Q(9,10))

    def test_two_local_likelihoods_need_joint_separator_normalization(self):
        direct,_ = bayes_product_square((Q(1,3),Q(2,3)),
            ((Q(1,2),Q(1,2)),)*2,((Q(1,4),Q(3,4)),)*2,
            ((1,0),(Q(1,2),Q(1,2))),((1,Q(1,3)),(Q(1,2),1)))
        self.assertEqual(sum((p for slab in direct for row in slab for p in row),Q(0)),1)
        for slab in direct:
            self.assertEqual(slab[0][0]*slab[1][1],slab[0][1]*slab[1][0])

    def test_joint_nonfactor_evidence_breaks_conditional_independence(self):
        fair = conditional_product((1,),((Q(1,2),Q(1,2)),),((Q(1,2),Q(1,2)),))[0]
        # Observe A=B, an actual likelihood on the pair, then normalize.
        correlated = ((Q(1,2),0),(0,Q(1,2)))
        self.assertEqual(fair,((Q(1,4),Q(1,4)),)*2)
        self.assertNotEqual(correlated[0][0]*correlated[1][1],correlated[0][1]*correlated[1][0])

    def test_zero_evidence_and_bad_shapes_rejected(self):
        with self.assertRaises(ProbabilityError):
            bayes_product_square((1,),((1,),),((1,),),((0,),),((1,),))
        with self.assertRaises(ProbabilityError):
            bayes_product_square((1,),((1,),),((1,),),((1,0),),((1,),))


class BlackwellPolicyTests(unittest.TestCase):
    def test_perfect_experiment_simulates_any_finite_experiment(self):
        perfect = Experiment("three",((1,0,0),(0,1,0),(0,0,1)))
        other = Experiment("three",((Q(1,3),Q(2,3)),(0,1),(Q(3,4),Q(1,4))))
        channel = find_garbling(perfect,other)
        self.assertEqual(channel,other.rows)
        self.assertTrue(garbling_verifies(perfect,other,channel))
        self.assertIsNone(find_garbling(other,perfect))

    def test_exact_noisy_garbling_and_equal_support_non_equivalence(self):
        more = Experiment("bit",((Q(3,4),Q(1,4)),(Q(1,4),Q(3,4))))
        less = Experiment("bit",((Q(5,8),Q(3,8)),(Q(3,8),Q(5,8))))
        channel = find_garbling(more,less)
        self.assertEqual(channel,((Q(3,4),Q(1,4)),(Q(1,4),Q(3,4))))
        self.assertIsNone(find_garbling(less,more))

    def test_noncomparable_common_source_experiments(self):
        a = Experiment("three",((1,0),(0,1),(0,1)))
        b = Experiment("three",((0,1),(1,0),(0,1)))
        self.assertIsNone(find_garbling(a,b))
        self.assertIsNone(find_garbling(b,a))

    def test_cross_source_and_search_budget_are_not_infeasibility(self):
        e = Experiment("a",((Q(1,2),Q(1,2)),))
        with self.assertRaises(ProbabilityError):
            find_garbling(e,Experiment("b",e.rows))
        with self.assertRaises(SearchBudgetError):
            find_garbling(e,e,max_bases=1)

    def test_blackwell_equal_readout_has_unequal_continuation_value(self):
        good,bad,b = bits()
        rows = tuple((1,0) if s < 2 else (0,1) for s in range(4))
        e = Experiment("bits",rows)
        self.assertTrue(garbling_verifies(e,e,((1,0),(0,1))))
        self.assertEqual(tuple(r for r,_,_ in good.rows[0]), tuple(r for r,_,_ in bad.rows[0]))
        root = StochasticHistory.original("bits","bits",(Q(1,4),)*4)
        target = (0,1,1,0)
        for outcome in (0,1):
            after_good,after_bad = root.advance(good,outcome),root.advance(bad,outcome)
            self.assertEqual(optimal_zero_error_cost(after_good,(b,),target,1).cost,1)
            self.assertIsNone(optimal_zero_error_cost(after_bad,(b,),target,5).cost)

    def test_no_reset_original_parity_countermodel(self):
        _,a,b = bits()
        root = StochasticHistory.original("bits","bits",(Q(1,4),)*4)
        for horizon in (0,1,2,4,7):
            self.assertIsNone(optimal_zero_error_cost(root,(a,b),(0,1,1,0),horizon).cost)

    def test_expected_cost_is_exact_and_not_worst_case_rank(self):
        root = StochasticHistory.original("s","x",(Q(1,2),Q(1,4),Q(1,4)))
        cheap = deterministic("cheap",(0,1,1),(0,1,2),source="s",space="x")
        dear = deterministic("dear",(0,1,2),(0,1,2),source="s",space="x",cost=3)
        result = optimal_zero_error_cost(root,(cheap,dear),(0,0,1),2)
        self.assertEqual((result.action,result.cost),("cheap",Q(5,2)))
        self.assertEqual(optimal_zero_error_cost(root,(cheap,dear),(0,0,1),1).cost,3)

    def test_adaptation_strictly_beats_every_fixed_two_action_word(self):
        states = tuple(range(4))
        q = deterministic("Q",tuple(s//2 for s in states),
                          tuple(2*(s//2)+((s//2)^(s%2)) for s in states))
        r0 = deterministic("R0",tuple(s%2 if s//2==0 else 0 for s in states),states)
        r1 = deterministic("R1",tuple(s%2 if s//2==1 else 0 for s in states),states)
        menu=(q,r0,r1)
        root=StochasticHistory.original("bits","bits",(Q(1,4),)*4)
        self.assertEqual(optimal_zero_error_cost(root,menu,(0,1,1,0),2).cost,2)
        for word in product(menu,repeat=2):
            observations={}
            for original in states:
                current=original
                path=[]
                for action in word:
                    outcome,current,_=action.rows[current][0]
                    path.append(outcome)
                observations.setdefault(tuple(path),set()).add((0,1,1,0)[original])
            self.assertTrue(any(len(labels)>1 for labels in observations.values()))

    def test_full_support_noise_never_yields_finite_zero_error(self):
        noisy=StochasticInstrument("noisy","s","x","x",2,(
            ((0,0,Q(3,4)),(1,0,Q(1,4))),((0,1,Q(1,4)),(1,1,Q(3,4)))))
        root=StochasticHistory.original("s","x",(Q(1,2),Q(1,2)))
        for horizon in (1,3,5):
            self.assertIsNone(optimal_zero_error_cost(root,(noisy,),(0,1),horizon).cost)


class ConcurrencyEvidenceMemoryTests(unittest.TestCase):
    def test_separate_nondestructive_bit_reads_commute(self):
        states=tuple(range(4))
        a=deterministic("a",tuple(s//2 for s in states),states)
        b=deterministic("b",tuple(s%2 for s in states),states)
        self.assertIsNone(commutation_defect(a,b))
        root=StochasticHistory.original("bits","bits",(Q(1,4),)*4)
        for aout,bout in product((0,1),repeat=2):
            ab=root.advance(a,aout).advance(b,bout)
            ba=root.advance(b,bout).advance(a,aout)
            self.assertEqual(ab.joint,ba.joint)
            self.assertEqual(ab.path_probability,ba.path_probability)

    def test_commuting_unobserved_transitions_do_not_certify_receipt_commutation(self):
        read=deterministic("read",(0,1),(0,1),source="s",space="b")
        flip=deterministic("flip",("ok","ok"),(1,0),source="s",space="b")
        # Identity and flip commute as unobserved transitions, but the report differs.
        witness=commutation_defect(read,flip)
        self.assertIsNotNone(witness)
        self.assertEqual(witness[0],0)

    def test_destructive_bit_read_commutation_fails(self):
        _,a,b=bits()
        self.assertIsNotNone(commutation_defect(a,b))

    def test_path_conditional_lr_handles_duplicate_evidence(self):
        null=StochasticHistory.original("s","b",(Q(3,4),Q(1,4)))
        alternative=StochasticHistory.original("s","b",(Q(1,4),Q(3,4)))
        read=deterministic("read",("no","yes"),(0,1),source="s",space="b")
        result=causal_ville_audit(null,alternative,(read,),lambda h:"read",2,9)
        self.assertEqual(result["expectation"],1)
        self.assertEqual(result["crossing_probability"],0)
        fake_expectation=Q(1,4)*9+Q(3,4)*Q(1,9)
        self.assertEqual(fake_expectation,Q(7,3))
        self.assertGreater(Q(1,4),Q(1,9))

    def test_predictable_adaptive_ville_policy(self):
        null=StochasticHistory.original("s","b",(Q(3,4),Q(1,4)))
        alt=StochasticHistory.original("s","b",(Q(1,4),Q(3,4)))
        read=deterministic("read",("no","yes"),(0,1),source="s",space="b")
        flip=deterministic("flip",("ok","ok"),(1,0),source="s",space="b")
        policy=lambda h: "flip" if h and h[-1][1]=="yes" else "read"
        result=causal_ville_audit(null,alt,(read,flip),policy,4,3)
        self.assertEqual(result["crossing_probability"],Q(1,4))
        self.assertEqual(result["expectation"],1)

    def test_singular_null_cannot_supply_likelihood_ratio_martingale(self):
        null=StochasticHistory.original("s","b",(1,0))
        alt=StochasticHistory.original("s","b",(0,1))
        read=deterministic("read",(0,1),(0,1),source="s",space="b")
        with self.assertRaises(ProbabilityError):
            causal_ville_audit(null,alt,(read,),lambda h:"read",1,2)

    def test_sharp_memory_lift_pigeonhole_and_positive_controls(self):
        self.assertEqual(reversible_memory_lift((0,0))[0],2)
        self.assertEqual(reversible_memory_lift((0,1,2,3))[0],1)
        count,lift=reversible_memory_lift(("a","a","b","a","b"))
        self.assertEqual(count,3)
        self.assertEqual(len(set(lift)),5)
        # Exhaustively refute every two-label memory assignment for size-three fiber.
        for memory in product(range(2),repeat=3):
            self.assertLess(len({("a",m) for m in memory}),3)


class CPTests(unittest.TestCase):
    zero=((1,0),(0,0))
    one=((0,0),(0,1))
    reset0=((1,0),(0,0))
    reset1=((0,1),(0,0))

    def test_multiple_kraus_reset_channel_and_recorded_measurement(self):
        erase=CPInstrument("erase",(("done",(self.reset0,self.reset1)),))
        measure=CPInstrument("Z",((0,(self.zero,)),(1,(self.one,))))
        self.assertEqual(erase.event(self.zero,"done"),(1,self.zero))
        self.assertEqual(erase.event(self.one,"done"),(1,self.zero))
        recorded=compose_cp(measure,erase)
        for original,rho in enumerate((self.zero,self.one)):
            p,after=recorded.event(rho,(original,"done"))
            self.assertEqual((p,after),(1,self.zero))
            with self.assertRaises(ProbabilityError):
                recorded.event(rho,(1-original,"done"))

    def test_cp_composition_exact_joint_probability_and_posterior(self):
        z=CPInstrument("Z",((0,(self.zero,)),(1,(self.one,))))
        xplus=((Q(1,2),Q(1,2)),(Q(1,2),Q(1,2)))
        xminus=((Q(1,2),Q(-1,2)),(Q(-1,2),Q(1,2)))
        x=CPInstrument("X",(("plus",(xplus,)),("minus",(xminus,))))
        for outcome in ("plus","minus"):
            p,middle=x.event(self.zero,outcome)
            for final in (0,1):
                q,after=z.event(middle,final)
                prob,direct=compose_cp(x,z).event(self.zero,(outcome,final))
                self.assertEqual(prob,p*q)
                self.assertEqual(after,direct)
                self.assertEqual(prob,Q(1,4))

    def test_non_cp_completeness_and_non_psd_density_rejected(self):
        with self.assertRaises(ProbabilityError):
            CPInstrument("missing",((0,(self.zero,)),))
        with self.assertRaises(ProbabilityError):
            density(((Q(1,3),0,0),(0,Q(1,3),Q(1,2)),(0,Q(1,2),Q(1,3))))


if __name__ == "__main__":
    unittest.main()
