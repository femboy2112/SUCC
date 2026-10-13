"""Exact independent-sampling and history-internalization adversaries."""
import unittest
from fractions import Fraction as F
from itertools import product
from observational_succ.carrier_statistical_limit import (
    StatisticalFrontierError, ExperimentPair, OperationalKernel,
    rational_bernoulli_tree,
)


class StatisticalBoundaryTests(unittest.TestCase):
    def test_identical_experiment_laws_permanent_statistical_alias(self):
        p=ExperimentPair("same world",("0","1"),(F(2,3),F(1,3)),(F(2,3),F(1,3)))
        self.assertEqual(p.total_variation,0)
        self.assertEqual(p.equal_prior_risk,F(1,2))
        for n in (1,2,3,4,5):
            self.assertEqual(p.independent_product_risk(n),F(1,2))
        self.assertTrue(p.invariant_forever_under_iid())

    def test_one_noisy_report_never_proves_certain_ontology(self):
        p=ExperimentPair("two hypotheses",(0,1),(F(3,4),F(1,4)),(F(1,4),F(3,4)))
        self.assertEqual(p.total_variation,F(1,2))
        self.assertEqual(p.equal_prior_risk,F(1,4))
        errors=[p.independent_product_risk(n) for n in range(1,8)]
        self.assertEqual(errors[0],F(1,4))
        self.assertTrue(all(e>0 for e in errors))
        self.assertTrue(all(b<=a for a,b in zip(errors,errors[1:])))
        self.assertLessEqual(p.iid_chebyshev_error_upper(1000),F(1,250))
        self.assertFalse(p.certainty_possible)

    def test_disjoint_support_immediate_zero_error(self):
        p=ExperimentPair("certain",(0,1),(1,0),(0,1))
        self.assertTrue(p.certainty_possible)
        self.assertEqual(p.equal_prior_risk,0)
        self.assertEqual(p.independent_product_risk(4),0)

    def test_exhaustive_small_rational_le_cam_identity(self):
        for q in range(2,5):
            for w in product(range(3),repeat=q):
                if not sum(w):continue
                for z in product(range(3),repeat=q):
                    if not sum(z):continue
                    p=ExperimentPair("controlled",tuple(range(q)),
                        tuple(F(x,sum(w)) for x in w),tuple(F(x,sum(z)) for x in z))
                    self.assertEqual(2*p.equal_prior_risk,1-p.total_variation)
                    self.assertEqual(p.certainty_possible,
                                     all(a*b==0 for a,b in zip(p.internal,p.external)))

    def test_omega_confidence_is_not_finite_certainty(self):
        p=ExperimentPair("iid",(0,1),(F(3,4),F(1,4)),(F(1,4),F(3,4)))
        self.assertTrue(all(p.independent_product_risk(n)>0 for n in range(1,9)))
        self.assertLess(p.iid_chebyshev_error_upper(10000),F(1,100))
        # Does not grant an actual limit observation as one machine operation.

    def test_history_based_internalization_all_adaptive_policies(self):
        for horizon in (1,2,3):
            kernel=rational_bernoulli_tree(horizon)
            simulator=kernel.internal_realization()
            # Enumerate all policies for small tree only at horizon <=2.
            if horizon<=2:
                histories={():None}
                for a in kernel.actions:
                    for o in kernel.outcomes:
                        histories[((a,o),)]=None
                hs=tuple(h for h in histories if len(h)<horizon)
                policies=(dict(zip(hs, choices)) for choices in product(kernel.actions,repeat=len(hs)))
            else:
                policy={history:("LEFT" if len(history)%2==0 else "RIGHT")
                        for history,a in kernel.rows if a=="LEFT"}
                policies=(policy,)
            for policy in policies:
                self.assertEqual(kernel.policy_distribution(policy),simulator.run_policy(policy))

    def test_adaptive_source_has_real_action_effect(self):
        k=rational_bernoulli_tree(2)
        left=k.rows[(),"LEFT"]
        right=k.rows[(),"RIGHT"]
        self.assertNotEqual(left,right)
        pol_l={h:"LEFT" for h,a in k.rows if a=="LEFT"}
        pol_r={h:"RIGHT" for h,a in k.rows if a=="LEFT"}
        self.assertNotEqual(k.policy_distribution(pol_l),k.policy_distribution(pol_r))
        self.assertEqual(k.internal_realization().run_policy(pol_l),k.policy_distribution(pol_l))

    def test_observer_postprocessing_cannot_improve_ontology_discrimination(self):
        p=ExperimentPair('source',(0,1,2),(F(1,2),F(1,2),0),
                         (0,F(1,2),F(1,2)))
        changed=p.push(('public_zero','public_one'),
                       ((F(1),F(0)),(F(1,2),F(1,2)),(F(0),F(1))),name='coarse')
        self.assertLessEqual(changed.total_variation,p.total_variation)
        self.assertGreaterEqual(changed.equal_prior_risk,p.equal_prior_risk)
        erased=p.push(('constant',),((F(1),),(F(1),),(F(1),)),name='erase')
        self.assertEqual(erased.total_variation,0)
        self.assertEqual(erased.equal_prior_risk,F(1,2))
        with self.assertRaises(StatisticalFrontierError):
            p.push(('x','y'),((1,0),),name='broken')

    def test_internal_history_simulator_state_cost_is_nonzero(self):
        for n in (1,2,3):
            k=rational_bernoulli_tree(n)
            cost=k.internal_history_state_bound()
            self.assertEqual(cost['reachable_internal_states'],
                             sum(4**j for j in range(n+1)))
            self.assertEqual(cost['worst_case_state_upper'],
                             sum(4**j for j in range(n+1)))
            self.assertTrue(cost['nonzero_resource_cost'])
            self.assertFalse(cost['physical_ontology_authenticated'])

    def test_noncausal_missing_branch_refused(self):
        k=rational_bernoulli_tree(1)
        with self.assertRaises(StatisticalFrontierError):
            OperationalKernel("x",k.actions,k.outcomes,1,{((),"LEFT"):(F(1,2),F(1,2))})
        with self.assertRaises(StatisticalFrontierError):
            OperationalKernel("x",k.actions,k.outcomes,1,{**k.rows,((('LEFT',0),),"RIGHT"):(1,0)})

    def test_physical_source_authentication_not_inferred_from_kernel(self):
        k=rational_bernoulli_tree(2)
        sim=k.internal_realization()
        self.assertEqual(sim.source.source_id,k.source_id)
        # Names are declarations; adding ontology labels changes no rows.
        self.assertNotIn("outside",repr(sim.transition((),"LEFT")))

    def test_exact_probability_contracts_and_caps(self):
        with self.assertRaises(StatisticalFrontierError):
            ExperimentPair("x",(0,1),(0.5,0.5),(F(1,2),F(1,2)))
        p=ExperimentPair("x",(0,1),(F(1,2),F(1,2)),(F(1,2),F(1,2)))
        with self.assertRaises(StatisticalFrontierError):
            p.independent_product_risk(40)
        with self.assertRaises(StatisticalFrontierError):
            p.iid_chebyshev_error_upper(10)
        with self.assertRaises(StatisticalFrontierError):
            rational_bernoulli_tree(9)

if __name__=="__main__":unittest.main()
