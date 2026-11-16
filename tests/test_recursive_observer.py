"""Exact hostile tests of source-coupled recursive observation and Bayes policies."""
import unittest
from fractions import Fraction as Q
from itertools import product
from observational_succ.recursive_observer import (
    JointInstrument, instrument_from_post_likelihood, normalize,
    initial_pairs, update_pair, update_current, current_marginal,
    original_marginal, outcome_law, run_trace, optimal_bayes_policy,
    stop_risk, contraction_bound, iterate_same_outcome, tv,
    dobrushin_delta, SourceCostMeter, predictive_span, predictive_partition,
    predictive_operator, direct_sum_instruments, predictively_equivalent_priors,
    brier_loss, expected_brier, brier_excess,
)


def reset_and_read_old(cost=Q(1,8)):
    # Source x=0,1 is reset to 0, but the outcome retains old x.
    return JointInstrument((
        ((Q(1), Q(0)), (Q(0), Q(0))),
        ((Q(0), Q(1)), (Q(0), Q(0))),
    ), cost, 'reset-with-record')


def reset_blind():
    return JointInstrument((
        ((Q(1),), (Q(0),)),
        ((Q(1),), (Q(0),)),
    ), Q(1,10), 'blind-reset')


def read_only_likelihood(p0, p1, cost=Q(1,16)):
    # Outcome 1 probabilities p0 and p1 at each old/current state.
    return JointInstrument((
        ((Q(1)-p0, p0), (Q(0), Q(0))),
        ((Q(0), Q(0)), (Q(1)-p1, p1)),
    ), cost, 'read-only')


def fixed_point_instrument():
    return instrument_from_post_likelihood(
        ((Q(3,5),Q(2,5)),(Q(2,5),Q(3,5))),
        ((Q(2,3),Q(1,3)),(Q(1,3),Q(2,3))),
        Q(1,20))


class RecursiveObserverTests(unittest.TestCase):
    def test_invalid_joint_source_cannot_create_probability(self):
        with self.assertRaises(ValueError):
            JointInstrument((((Q(1,2),Q(0)),),),Q(1))
        with self.assertRaises(ValueError):
            JointInstrument((((Q(1,2),Q(1,2)),),),Q(0))
        with self.assertRaises(ValueError):
            JointInstrument((((0.5,0.5),),),Q(1))
        with self.assertRaises(ValueError):
            normalize((Q(0),Q(0)))
        with self.assertRaises(ValueError):
            normalize((Q(-1),Q(2)))

    def test_retrospective_record_restores_original_after_destructive_reset(self):
        i=reset_and_read_old()
        b=initial_pairs((Q(1,2),Q(1,2)))
        self.assertIsNone(i.post_state_likelihood())
        z,after=update_pair(b,i,1)
        self.assertEqual(z,Q(1,2))
        self.assertEqual(original_marginal(after),(Q(0),Q(1)))
        self.assertEqual(current_marginal(after),(Q(1),Q(0)))
        self.assertEqual(stop_risk(after,(0,1)),Q(0))

    def test_blind_reset_erases_source_but_not_prior_uncertainty(self):
        b=initial_pairs((Q(1,3),Q(2,3)))
        z,after=update_pair(b,reset_blind(),0)
        self.assertEqual(z,Q(1))
        self.assertEqual(original_marginal(after),(Q(1,3),Q(2,3)))
        self.assertEqual(current_marginal(after),(Q(1),Q(0)))
        self.assertEqual(stop_risk(after,(0,1)),Q(1,3))

    def test_strong_joint_coupling_cannot_be_factored_post_state(self):
        i=reset_and_read_old()
        self.assertEqual(i.transition,((Q(1),Q(0)),(Q(1),Q(0))))
        self.assertIsNone(i.post_state_likelihood())
        self.assertIsNone(contraction_bound(i))

    def test_factorized_model_exact_both_outcomes(self):
        i=fixed_point_instrument()
        self.assertEqual(i.post_state_likelihood(),
                         ((Q(2,3),Q(1,3)),(Q(1,3),Q(2,3))))
        self.assertEqual(i.transition,((Q(3,5),Q(2,5)),(Q(2,5),Q(3,5))))
        self.assertEqual(outcome_law(initial_pairs((Q(1,2),Q(1,2))),i),
                         (Q(1,2),Q(1,2)))
        self.assertEqual(contraction_bound(i),Q(4,5))

    def test_source_observations_update_past_without_reverse_causality(self):
        i=read_only_likelihood(Q(1,4),Q(3,4))
        z,b=update_pair(initial_pairs((Q(1,2),Q(1,2))),i,1)
        self.assertEqual(z,Q(1,2))
        self.assertEqual(original_marginal(b),(Q(1,4),Q(3,4)))
        self.assertEqual(current_marginal(b),(Q(1,4),Q(3,4)))
        self.assertEqual(i.transition,((Q(1),Q(0)),(Q(0),Q(1))))

    def test_rare_evidence_can_increase_uncertainty_on_one_path(self):
        # The expected information about a fixed original target increases,
        # but a particular surprising branch can increase uncertainty.
        i=read_only_likelihood(Q(1,9),Q(1),Q(1,10))
        before=initial_pairs((Q(9,10),Q(1,10)))
        self.assertEqual(stop_risk(before,(0,1)),Q(1,10))
        p,after=update_pair(before,i,1)
        self.assertEqual(p,Q(1,5))
        self.assertEqual(original_marginal(after),(Q(1,2),Q(1,2)))
        self.assertEqual(stop_risk(after,(0,1)),Q(1,2))
        _,other=update_pair(before,i,0)
        self.assertEqual(original_marginal(other),(Q(1),Q(0)))

    def test_missing_evidence_is_not_a_posterior(self):
        i=reset_and_read_old()
        _,b=update_pair(initial_pairs((Q(1),Q(0))),i,1)
        self.assertIsNone(b)
        z,b=run_trace(initial_pairs((Q(1),Q(0))),(i,),((0,1),))
        self.assertEqual((z,b),(Q(0),None))
        with self.assertRaises(ValueError):
            update_pair(initial_pairs((Q(1,2),Q(1,2))),i,10)

    def test_model_prior_matters_even_with_identical_source_and_probe(self):
        i=read_only_likelihood(Q(1,4),Q(3,4))
        _,a=update_pair(initial_pairs((Q(1,2),Q(1,2))),i,1)
        _,b=update_pair(initial_pairs((Q(3,4),Q(1,4))),i,1)
        self.assertEqual(original_marginal(a),(Q(1,4),Q(3,4)))
        self.assertEqual(original_marginal(b),(Q(1,2),Q(1,2)))
        self.assertNotEqual(a,b)

    def test_high_cost_prevents_probing_same_informative_source(self):
        prior=initial_pairs((Q(1,2),Q(1,2)))
        low=optimal_bayes_policy(prior,(reset_and_read_old(Q(1,8)),),(0,1),2)
        high=optimal_bayes_policy(prior,(reset_and_read_old(Q(3,4)),),(0,1),2)
        self.assertEqual((low.action,low.value),(0,Q(1,8)))
        self.assertEqual((high.action,high.value),(None,Q(1,2)))

    def test_bayes_budget_noisy_cheaper_than_perfect(self):
        prior=initial_pairs((Q(1,2),Q(1,2)))
        noisy=read_only_likelihood(Q(1,4),Q(3,4),Q(1,16))
        perfect=reset_and_read_old(Q(1,3))
        d=optimal_bayes_policy(prior,(noisy,perfect),(0,1),1)
        self.assertEqual((d.action,d.value),(0,Q(5,16)))
        self.assertEqual(d.branches[0][1].value,Q(1,4))
        self.assertEqual(d.branches[1][1].value,Q(1,4))

    def test_stopping_policy_not_same_as_worst_case_certainty(self):
        prior=initial_pairs((Q(99,100),Q(1,100)))
        d=optimal_bayes_policy(prior,(reset_and_read_old(Q(1,8)),),(0,1),2)
        self.assertEqual((d.action,d.value),(None,Q(1,100)))
        # Rational Bayes risk stopping != proof of full source identity.

    def test_exact_filter_repeated_outcome_fixed_point_certificate(self):
        i=fixed_point_instrument()
        d=contraction_bound(i)
        self.assertEqual(d,Q(4,5))
        xs=iterate_same_outcome((Q(0),Q(1)),i,0,25)
        ys=iterate_same_outcome((Q(1),Q(0)),i,0,25)
        self.assertLessEqual(tv(xs[-1],ys[-1]),d**25)
        # 2-state normalized projective map F(p)=(4+2p)/(7+p), p=Pr(state0).
        for prev,nxt in zip(xs,xs[1:]):
            p=prev[0]
            self.assertEqual(nxt[0],(4+2*p)/(7+p))
        self.assertTrue(Q(70,100)<xs[-1][0]<Q(71,100))

    def test_alternating_evidence_has_limit_cycle_not_one_fixed_point(self):
        i=fixed_point_instrument()
        b=(Q(1,2),Q(1,2))
        evens=[];odds=[]
        for j in range(48):
            z,b=update_current(b,i,j%2)
            self.assertGreater(z,0)
            (evens if j%2 else odds).append(b[0])
        self.assertLess(abs(evens[-1]-evens[-2]),Q(1,10**10))
        self.assertGreater(abs(evens[-1]-odds[-1]),Q(1,100))
        p=evens[-1]
        self.assertLess(abs(p*p+8*p-3),Q(1,10**9))

    def test_same_posterior_fixed_point_can_mask_different_future_laws(self):
        P=((Q(1,2),Q(1,2)),(Q(1,2),Q(1,2)))
        a=instrument_from_post_likelihood(P,
            ((Q(1,2),Q(1,2)),(Q(1,2),Q(1,2))))
        b=instrument_from_post_likelihood(P,
            ((Q(3,4),Q(1,4)),(Q(3,4),Q(1,4))))
        prior=(Q(1,2),Q(1,2))
        self.assertEqual(update_current(prior,a,0)[1],prior)
        self.assertEqual(update_current(prior,b,0)[1],prior)
        self.assertNotEqual(outcome_law(initial_pairs(prior),a),
                            outcome_law(initial_pairs(prior),b))
        self.assertEqual(outcome_law(initial_pairs(prior),a)[0],Q(1,2))
        self.assertEqual(outcome_law(initial_pairs(prior),b)[0],Q(3,4))

    def test_cost_meter_not_automatically_observable(self):
        prior=initial_pairs((Q(1,2),Q(1,2)))
        i=reset_and_read_old(Q(1,20))
        meter=SourceCostMeter((((Q(0),Q(0)),(Q(0),Q(0))),
                                ((Q(0),Q(5)),(Q(0),Q(0)))),unit='joule')
        self.assertEqual(meter.expected(prior,i),Q(5,2))
        # A resource meter that is actually read would itself be a report:
        # it must be included in J, not implicitly conditioned on here.
        before=update_pair(prior,i,1)
        _=meter.expected(prior,i)
        after=update_pair(prior,i,1)
        self.assertEqual(before,after)

    def test_uninformative_wrong_model_has_belief_fixed_point_but_is_wrong(self):
        # True source prepared at state 1. Chosen model resets to 50/50.
        p=((Q(1,2),Q(1,2)),(Q(1,2),Q(1,2)))
        l=((Q(1),),(Q(1),))
        i=instrument_from_post_likelihood(p,l)
        z,b=update_current((Q(0),Q(1)),i,0)
        self.assertEqual(z,Q(1))
        self.assertEqual(b,(Q(1,2),Q(1,2)))
        self.assertEqual(update_current(b,i,0)[1],b)
        self.assertNotEqual(b,(Q(0),Q(1)))

    def test_static_backward_section_failure_dynamic_history_succeeds(self):
        # a -> b -> c -> c, no report distinguishing b,c.
        # A clock/history retained by the observer gives different exact beliefs.
        j=(((Q(0),),(Q(1),),(Q(0),)),
           ((Q(0),),(Q(0),),(Q(1),)),
           ((Q(0),),(Q(0),),(Q(1),)))
        i=JointInstrument(j,Q(1))
        b=initial_pairs((Q(1),Q(0),Q(0)))
        _,b1=update_pair(b,i,0)
        _,b2=update_pair(b1,i,0)
        self.assertEqual(current_marginal(b1),(Q(0),Q(1),Q(0)))
        self.assertEqual(current_marginal(b2),(Q(0),Q(0),Q(1)))
        # Both current states have the SAME coarse report w. A static K(w) cannot equal both.
        q=(0,1,1)
        self.assertEqual(q[current_marginal(b1).index(Q(1))],
                         q[current_marginal(b2).index(Q(1))])
        self.assertEqual(original_marginal(b1),original_marginal(b2))

    def test_current_only_future_does_not_recover_merged_history(self):
        blind=reset_blind()
        read=read_only_likelihood(Q(1,2),Q(1,2))
        prior=initial_pairs((Q(1,4),Q(3,4)))
        _,post=update_pair(prior,blind,0)
        for y in (0,1):
            z,b2=update_pair(post,read,y)
            self.assertEqual(z,Q(1,2))
            self.assertEqual(original_marginal(b2),(Q(1,4),Q(3,4)))

    def test_no_closed_loop_global_contraction_from_common_action_bound(self):
        # Contraction certificate is NOT about a policy with discontinuous action changes.
        i=fixed_point_instrument()
        self.assertLess(contraction_bound(i),1)
        t0=read_only_likelihood(Q(0),Q(1))
        t1=read_only_likelihood(Q(1),Q(0))
        self.assertIsNone(contraction_bound(t0))
        self.assertIsNone(contraction_bound(t1))

    def test_declared_source_meter_changes_optimal_policy(self):
        prior=initial_pairs((Q(1,2),Q(1,2)))
        i=reset_and_read_old(Q(1,20))
        cheap=SourceCostMeter(tuple(tuple(tuple(Q(0) for _ in range(2))
                                       for _ in range(2)) for _ in range(2)),unit='joule')
        costly=SourceCostMeter(tuple(tuple(tuple(Q(1) for _ in range(2))
                                        for _ in range(2)) for _ in range(2)),unit='joule')
        x=optimal_bayes_policy(prior,(i,),(0,1),1,(cheap,))
        y=optimal_bayes_policy(prior,(i,),(0,1),1,(costly,))
        self.assertEqual((x.action,x.value),(0,Q(1,20)))
        self.assertEqual((y.action,y.value),(None,Q(1,2)))
        self.assertEqual(cheap.expected(prior,i),Q(0))
        self.assertEqual(costly.expected(prior,i),Q(1))

    def test_source_meter_is_sensitized_to_latent_source_coupling(self):
        i=reset_and_read_old(Q(1,20))
        table=(((Q(0),Q(0)),(Q(0),Q(0))),
               ((Q(0),Q(2)),(Q(0),Q(0))))
        meter=SourceCostMeter(table,'joule')
        self.assertEqual(meter.expected(initial_pairs((Q(1,2),Q(1,2))),i),Q(1))
        self.assertEqual(meter.expected(initial_pairs((Q(3,4),Q(1,4))),i),Q(1,2))
        with self.assertRaises(ValueError):
            SourceCostMeter((((-1,0),(0,0)),((0,0),(0,0))), 'joule').expected(
                initial_pairs((Q(1,2),Q(1,2))),i)

    def test_predictive_closure_delayed_probe_distinguishes_at_depth_two(self):
        # a->c with output0, b->b with output0, c->c with output1.
        # a,b agree on first output and differ only at the second tick.
        J=(((Q(0),Q(0)),(Q(0),Q(0)),(Q(1),Q(0))),
           ((Q(0),Q(0)),(Q(1),Q(0)),(Q(0),Q(0))),
           ((Q(0),Q(0)),(Q(0),Q(0)),(Q(0),Q(1))))
        i=JointInstrument(J,Q(1))
        basis,depth,stab=predictive_span((i,))
        self.assertEqual((len(basis),max(depth),stab),(3,2,2))
        self.assertEqual(predictive_partition((i,)),((0,),(1,),(2,)))
        word1=predictive_operator(i,0,(Q(1),Q(1),Q(1)))
        word2=predictive_operator(i,0,predictive_operator(i,1,(Q(1),Q(1),Q(1))))
        self.assertEqual((word1[0],word1[1]),(Q(1),Q(1)))
        self.assertNotEqual(word2[0],word2[1])

    def test_predictive_closure_identifies_strictly_distinct_but_hidden_states(self):
        # A lawful T swap changes the hidden source, but output is fair and
        # independent of state at each step; the predictive quotient is one point.
        j=(((Q(0),Q(0)),(Q(1,2),Q(1,2))),
           ((Q(1,2),Q(1,2)),(Q(0),Q(0))))
        inst=JointInstrument(j,Q(1))
        basis,depth,stab=predictive_span((inst,))
        self.assertEqual((len(basis),stab),(1,0))
        self.assertEqual(predictive_partition((inst,)),((0,1),))

    def test_two_distinct_source_models_are_predictively_equivalent(self):
        swap=JointInstrument((((Q(0),Q(0)),(Q(1,2),Q(1,2))),
                              ((Q(1,2),Q(1,2)),(Q(0),Q(0)))),Q(1))
        one=JointInstrument((((Q(1,2),Q(1,2)),),),Q(1))
        combined=direct_sum_instruments((swap,),(one,))
        self.assertEqual(predictive_partition(combined),((0,1,2),))
        # Same accessible future laws, not same source carrier or history.
        self.assertEqual(combined[0].n,3)

    def test_proper_holdout_score_distinguishes_models_with_same_fixed_belief(self):
        truth=(Q(3,4),Q(1,4))
        rival=(Q(1,2),Q(1,2))
        self.assertEqual(brier_excess(rival,truth),Q(1,8))
        self.assertEqual(brier_excess(truth,truth),Q(0))
        self.assertEqual(brier_excess(rival,truth),sum(((a-b)**2 for a,b in zip(rival,truth)),Q(0)))
        self.assertEqual(brier_loss(truth,0),Q(1,8))
        self.assertEqual(brier_loss(truth,1),Q(9,8))
        with self.assertRaises(ValueError):
            brier_loss((Q(1),Q(1)),1)

    def test_same_belief_fixed_point_not_predictive_equivalence(self):
        P=((Q(1,2),Q(1,2)),(Q(1,2),Q(1,2)))
        a=instrument_from_post_likelihood(P,
          ((Q(1,2),Q(1,2)),(Q(1,2),Q(1,2))),Q(1))
        b=instrument_from_post_likelihood(P,
          ((Q(3,4),Q(1,4)),(Q(3,4),Q(1,4))),Q(1))
        c=direct_sum_instruments((a,),(b,))
        self.assertEqual(predictive_partition(c),((0,1),(2,3)))

    def test_cross_model_prior_equivalence_is_exact_future_law_not_identity(self):
        swap=JointInstrument((((Q(0),Q(0)),(Q(1,2),Q(1,2))),
                              ((Q(1,2),Q(1,2)),(Q(0),Q(0)))),Q(1))
        single=JointInstrument((((Q(1,2),Q(1,2)),),),Q(1))
        for prior in ((Q(0),Q(1)),(Q(1,3),Q(2,3)),(Q(1),Q(0))):
            self.assertTrue(predictively_equivalent_priors((swap,),(single,),prior,(Q(1),)))
        # An equivalent predictive model need not describe the true source:
        self.assertNotEqual(swap.n,single.n)

    def test_cross_model_fixed_point_equality_not_sufficient(self):
        P=((Q(1,2),Q(1,2)),(Q(1,2),Q(1,2)))
        a=instrument_from_post_likelihood(P,
          ((Q(1,2),Q(1,2)),(Q(1,2),Q(1,2))),Q(1))
        b=instrument_from_post_likelihood(P,
          ((Q(3,4),Q(1,4)),(Q(3,4),Q(1,4))),Q(1))
        self.assertFalse(predictively_equivalent_priors((a,),(b,),
                          (Q(1,2),Q(1,2)),(Q(1,2),Q(1,2))))

    def test_predictive_equivalence_requires_shared_cost_action_contract(self):
        a=reset_and_read_old(Q(1))
        b=reset_and_read_old(Q(2))
        with self.assertRaises(ValueError):
            direct_sum_instruments((a,),(b,))
        c=JointInstrument((((Q(1),), (Q(0),)),((Q(1),),(Q(0),))),Q(1))
        with self.assertRaises(ValueError):
            direct_sum_instruments((a,),(c,))

    def test_source_model_does_not_fix_resource_cost(self):
        a=reset_and_read_old(Q(1,8));b=reset_and_read_old(Q(3,4))
        self.assertEqual(a.joint,b.joint)
        self.assertNotEqual(a.cost,b.cost)


if __name__=='__main__':
    unittest.main(verbosity=2)
