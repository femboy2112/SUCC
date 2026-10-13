"""Likelihood ratio optional stopping: exact null path enumeration."""
import unittest
from fractions import Fraction as Q
from observational_succ.contextual_heuristics import ModelProbe,HeuristicError
from observational_succ.heuristic_evidence_martingales import (
    lr_step,replay_lr,adaptive_crossing_probability,
)


class AnytimeLikelihoodTests(unittest.TestCase):
    def setUp(self):
        self.p=ModelProbe("sensor","c",("up","down"),
                          {"H0":(Q(1,2),Q(1,2)),"H1":(Q(3,4),Q(1,4))})
        self.q=ModelProbe("mirror","c",("up","down"),
                          {"H0":(Q(1,4),Q(3,4)),"H1":(Q(1,2),Q(1,2))})

    def test_exact_bayes_factor_multiplicative(self):
        self.assertEqual(lr_step(1,self.p,"up",null="H0",alternative="H1"),Q(3,2))
        self.assertEqual(lr_step(Q(3,2),self.p,"down",null="H0",alternative="H1"),Q(3,4))

    def test_wealth_is_exact_null_martingale(self):
        for probe in (self.p,self.q):
            for start in (Q(1),Q(7,3),Q(1,19)):
                average=sum((probe.law("H0")[i]*lr_step(start,probe,y,
                              null="H0",alternative="H1")
                              for i,y in enumerate(probe.outcomes)),Q(0))
                self.assertEqual(average,start)

    def test_adaptive_policy_optional_stopping_bound(self):
        def policy(history):
            return self.p if (not history or history[-1][1]=="up") else self.q
        for depth in range(0,10):
            for alpha in (Q(1,2),Q(1,4),Q(1,10)):
                result=adaptive_crossing_probability(policy,depth,null="H0",
                                                      alternative="H1",alpha=alpha)
                self.assertLessEqual(result["null_cross_probability"],alpha)
                self.assertEqual(result["upper_bound"],alpha)
                self.assertFalse(result["physical_null_law_authenticated"])

    def test_null_does_not_require_posterior_or_prior(self):
        r=replay_lr(((self.p,"up"),(self.p,"up"),(self.p,"up")),
                    null="H0",alternative="H1",alpha=Q(1,5))
        self.assertEqual(r.wealth,Q(27,8))
        self.assertFalse(r.crosses)
        r2=replay_lr(((self.p,"up"),)*5,null="H0",alternative="H1",
                     alpha=Q(1,10))
        self.assertFalse(r2.crosses)

    def test_reject_unlicensed_zero_null_probabilities(self):
        bad=ModelProbe("b","c",("a","b"),{"H0":(1,0),"H1":(0,1)})
        with self.assertRaisesRegex(HeuristicError,"full null support"):
            lr_step(1,bad,"a",null="H0",alternative="H1")

    def test_invalid_horizon_or_alpha_rejected(self):
        with self.assertRaises(HeuristicError):
            adaptive_crossing_probability(lambda _:self.p,13,null="H0",alternative="H1")
        with self.assertRaises(HeuristicError):
            adaptive_crossing_probability(lambda _:self.p,3,null="H0",alternative="H1",alpha=1)

    def test_unbounded_horizon_is_not_claimed_by_finite_enumeration(self):
        r=adaptive_crossing_probability(lambda _:self.p,8,null="H0",alternative="H1",alpha=Q(1,5))
        self.assertGreater(r["tree_nodes"],1)
        self.assertTrue(r["valid_with_predictable_adaptive_probes"])
        self.assertLessEqual(r["null_cross_probability"],Q(1,5))

if __name__=="__main__":unittest.main()

class NoisyLimitTests(unittest.TestCase):
    def test_exact_exponential_underdetermination_bounds(self):
        from observational_succ.heuristic_evidence_martingales import noisy_limit_witness
        for n in (0,2,10,20,100):
            r=noisy_limit_witness(Q(3,4),n)
            self.assertEqual(r["bhattacharyya_coefficient_squared"],Q(3,4))
            self.assertEqual(r["wrong_majority_posterior_probability_upper"],Q(3,4)**(n//2))
            self.assertFalse(r["any_finite_trial_deductive_certainty"])
        self.assertLess(noisy_limit_witness(Q(3,4),100)["wrong_majority_posterior_probability_upper"],Q(1,10000))

    def test_requires_real_statistical_separability(self):
        from observational_succ.heuristic_evidence_martingales import noisy_limit_witness
        for p,n in ((Q(1,2),2),(Q(1),2),(Q(3,4),3)):
            with self.assertRaises(HeuristicError):noisy_limit_witness(p,n)
