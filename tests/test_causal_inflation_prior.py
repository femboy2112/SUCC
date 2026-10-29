"""Calibrated exact tests of declared prior, causal inflation, source controls."""
import math
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.causal_inflation_prior import (
    BinaryTreePrior, PriorInflationError, finite_inflation_scale,
    discrete_conformal_budget, oily_parameters, oily_matrix_power,
    linear_branch_energy, oily_critical_energy_closed, ks_signal_to_noise,
    normalized_census_variance, correlated_remote_update, golden_lucas_scale,
    embedded_causal_tree, original_deflated_oily_L,
    oily_preobservation_unnormalized, oily_postobservation_unnormalized,
    oily_frontier_event_likelihood,uniform_L_event_probability,
    max_entropy_vacancy_double_imbalance,bayesian_wavefront_message,
)


class SourcePriorTests(unittest.TestCase):
    def setUp(self):
        self.p = BinaryTreePrior(2,F(1,2))

    def test_transition_mass_and_correlation(self):
        self.assertEqual(self.p.p_same,F(3,4))
        self.assertEqual(self.p.p_flip,F(1,4))
        for parent in (-1,1):
            self.assertEqual(sum(self.p.transition(parent,c) for c in (-1,1)),1)
            self.assertEqual(sum(c*self.p.transition(parent,c) for c in (-1,1)),F(parent,2))

    def test_root_prior_distinct_same_causal_structure(self):
        equal = BinaryTreePrior(1,F(1,2),F(1,2))
        skew = BinaryTreePrior(1,F(1,2),F(3,4))
        self.assertEqual(equal.posterior_root((1,),1),F(3,4))
        self.assertEqual(skew.posterior_root((1,),1),F(9,10))

    def test_root_posterior_sufficiency(self):
        self.assertEqual(self.p.posterior_root((1,1),1),F(9,10))
        self.assertEqual(self.p.posterior_root((1,-1),1),F(1,2))
        self.assertEqual(self.p.posterior_root((-1,-1),1),F(1,10))

    def test_two_depth_exact_cylinder_mass(self):
        p = self.p
        for depth in (0,1):
            total = sum((p.finite_cylinder(tuple(spins),depth)
                         for spins in product((-1,1), repeat=sum(2**k for k in range(depth+1)))),F())
            self.assertEqual(total,1)

    def test_projective_consistency_all_second_layer_extensions(self):
        p=self.p
        for prefix in product((-1,1), repeat=3):
            mass=p.finite_cylinder(prefix,1)
            extended=sum((p.finite_cylinder(prefix+kids,2)
                         for kids in product((-1,1),repeat=4)),F())
            self.assertEqual(mass,extended)

    def test_likelihoods_normalize_exactly(self):
        for depth in (1,2,3):
            lp_total=F(0); lm_total=F(0)
            for leaves in product((-1,1),repeat=2**depth):
                lp,lm=self.p.leaf_likelihoods(leaves,depth)
                lp_total+=lp;lm_total+=lm
            self.assertEqual((lp_total,lm_total),(F(1),F(1)))

    def test_exhaustive_accuracy_diminishes_for_frontier_only(self):
        stats=[self.p.level_statistics(depth) for depth in (1,2,3)]
        self.assertTrue(stats[0]['accuracy_exact'] >= stats[1]['accuracy_exact'] >= stats[2]['accuracy_exact'] >= F(1,2))
        self.assertTrue(stats[0]['mutual_info_bits'] >= stats[1]['mutual_info_bits'] >= stats[2]['mutual_info_bits'] >0)

    def test_independent_frontier_erases_root(self):
        p=BinaryTreePrior(2,F(0))
        s=p.level_statistics(2)
        self.assertEqual(s['accuracy_exact'],F(1,2))
        self.assertAlmostEqual(s['mutual_info_bits'],0,places=12)

    def test_perfect_source_preserves_root(self):
        p=BinaryTreePrior(2,F(1))
        self.assertEqual(p.posterior_root((1,)*4,2),1)
        self.assertEqual(p.posterior_root((-1,)*4,2),0)
        with self.assertRaises(PriorInflationError):
            p.posterior_root((1,1,1,-1),2)
        s=p.level_statistics(2)
        self.assertEqual(s['accuracy_exact'],F(1))
        self.assertAlmostEqual(s['mutual_info_bits'],1,places=12)

    def test_prior_point_masses(self):
        p=BinaryTreePrior(1,F(1,2),F(1))
        self.assertEqual(p.posterior_root((-1,),1),F(1))
        self.assertEqual(p.finite_cylinder((1,-1),1),F(1,4))

    def test_exact_nonlinear_bayes_wavefront_messages(self):
        self.assertEqual(bayesian_wavefront_message(F(1,2),(F(1),F(1))),F(4,5))
        self.assertEqual(bayesian_wavefront_message(F(1,2),(F(1),F(-1))),0)
        self.assertEqual(bayesian_wavefront_message(F(1,2),(F(0),F(0))),0)
        self.assertEqual(bayesian_wavefront_message(F(0),(F(1),F(1))),0)

    def test_message_identity_matches_exact_tree_likelihood(self):
        model=BinaryTreePrior(2,F(1,2))
        for leaves in product((-1,1),repeat=4):
            # At depth 2, the two child messages are built from disjoint
            # causal observations of each two-leaf subtree.
            m=[]
            for i in (0,2):
                posterior=model.posterior_root(leaves[i:i+2],1)
                m.append(2*posterior-1)
            direct=model.posterior_root(leaves,2)
            self.assertEqual(bayesian_wavefront_message(F(1,2),tuple(m)),2*direct-1)

    def test_message_requires_consistent_causal_evidence(self):
        with self.assertRaises(PriorInflationError):bayesian_wavefront_message(F(1),[1,-1])
        with self.assertRaises(PriorInflationError):bayesian_wavefront_message(F(1,2),[])
        with self.assertRaises(PriorInflationError):bayesian_wavefront_message(F(1,2),[2])

    def test_bad_source_labels_are_rejected(self):
        for args in ((0,F(1,2)),(2,F(5,4)),(2,F(-1,5))):
            with self.assertRaises(PriorInflationError): BinaryTreePrior(*args)
        with self.assertRaises(PriorInflationError): BinaryTreePrior(2,F(1,2),source_id="")
        with self.assertRaises(PriorInflationError): self.p.finite_cylinder((1,),1)
        with self.assertRaises(PriorInflationError): self.p.posterior_root((1,),1)
        with self.assertRaises(PriorInflationError): self.p.transition(0,1)

    def test_exhaustive_budget(self):
        with self.assertRaises(PriorInflationError): self.p.level_statistics(4)


class HorizonTests(unittest.TestCase):
    def test_infinite_two_scale_conformal_reach_is_finite(self):
        for n in range(31):
            self.assertEqual(discrete_conformal_budget(2,n),2*(1-F(1,2**n)))
        self.assertTrue(discrete_conformal_budget(2,30)<2)

    def test_finite_inflation_does_not_make_event_horizon(self):
        self.assertEqual(finite_inflation_scale(2,100,end=3),8)
        self.assertEqual(discrete_conformal_budget(2,3,end=3),F(7,4))
        self.assertEqual(discrete_conformal_budget(2,11,end=3),F(11,4))
        self.assertTrue(discrete_conformal_budget(2,1000,end=3)>100)

    def test_multiple_rate_horizon(self):
        for g in (2,3,5):
            for n in range(1,11):
                cur=discrete_conformal_budget(g,n)
                delta=cur-discrete_conformal_budget(g,n-1)
                self.assertEqual(delta,F(1,g**(n-1)))

    def test_pisot_lucas_integer_inflation_shadow(self):
        self.assertEqual([golden_lucas_scale(n) for n in range(10)],
                         [2,1,3,4,7,11,18,29,47,76])
        for n in range(2,30):
            self.assertEqual(golden_lucas_scale(n+1),golden_lucas_scale(n)+golden_lucas_scale(n-1))
        with self.assertRaises(PriorInflationError):golden_lucas_scale(-1)

    def test_exact_embedded_causal_tree_never_sends_superluminal_signal(self):
        for branching in (2,3,5):
            levels=embedded_causal_tree(branching,4,2)
            self.assertEqual(tuple(len(x) for x in levels),tuple(branching**n for n in range(5)))
            for n in range(4):
                for k,pos in enumerate(levels[n+1]):
                    parent=levels[n][k//branching]
                    self.assertLessEqual(abs(pos-parent),F(1,2**n))

    def test_embedded_separation_can_be_superluminal_globally(self):
        levels=embedded_causal_tree(2,5,2)
        dist=2**5*(levels[5][-1]-levels[5][0])
        self.assertGreater(dist,1)
        self.assertEqual(dist,F(31))

    def test_inflation_geometry_validation(self):
        for fn,args in ((finite_inflation_scale,(1,4)),(discrete_conformal_budget,(1,4)),(finite_inflation_scale,(2,-1)),(discrete_conformal_budget,(2,-1))):
            with self.assertRaises(PriorInflationError):fn(*args)


class OilyControls(unittest.TestCase):
    def test_exact_authentic_oily_parameters_and_packet(self):
        for x in (F(),F(1,8),F(1,2),F(3,4),F(1)):
            u,v=oily_parameters(x)
            self.assertEqual(u+v,x)
            self.assertEqual(u-v,x*(1-x))
            self.assertTrue(F(0)<=v<=u<=F(1,2))
            for n in range(1,9):
                m=oily_matrix_power(x,n)
                self.assertEqual(m[0][1],sum(u**k*v**(n-1-k) for k in range(n)))

    def test_critical_jordan_growth(self):
        for n in range(17):
            m=oily_matrix_power(1,n)
            self.assertEqual(m[0][0],F(1,2**n))
            self.assertEqual(m[1][1],F(1,2**n))
            self.assertEqual(m[0][1],F(n,2**(n-1)) if n else F(0))
            for b in (2,3,4,5):
                self.assertEqual(linear_branch_energy(b,n),oily_critical_energy_closed(b,n))

    def test_binary_replication_cannot_preserve_oily_linear_energy(self):
        es=[linear_branch_energy(2,n) for n in range(6,31)]
        self.assertTrue(all(x>y for x,y in zip(es,es[1:])))
        self.assertLess(es[-1],F(1,1000))

    def test_critical_four_branch_jordan_distinction(self):
        self.assertEqual(oily_critical_energy_closed(4,6),146)
        self.assertGreater(oily_critical_energy_closed(5,11),oily_critical_energy_closed(4,11))

    def test_exact_bayes_prior_to_original_oily_posterior(self):
        for x in (F(0),F(1,10),F(1,2),F(4,5),F(1)):
            L=original_deflated_oily_L(x)
            self.assertGreater(L,0)
            self.assertEqual(oily_frontier_event_likelihood(x),1-x)
            for a in (0,1,2,8,24):
                prior=oily_preobservation_unnormalized(x,a)
                after=oily_postobservation_unnormalized(x,a)
                self.assertEqual(after,prior*(1-x))
                u,v=oily_parameters(x)
                authentic=(F(1-x,4)/(1-u)/(1-v))*x**a
                self.assertEqual(after,authentic)

    def test_max_entropy_vacancy_and_double_occupancy_signed_difference(self):
        for x in (F(0),F(1,8),F(1,2),F(3,4),F(1)):
            self.assertEqual(max_entropy_vacancy_double_imbalance(x),1-x)
            self.assertEqual(max_entropy_vacancy_double_imbalance(x),oily_frontier_event_likelihood(x))

    def test_no_fixed_binary_microevent_has_likelihood_one_minus_x(self):
        from itertools import product
        possible=[]
        for chosen in product((0,1),repeat=4):
            a00,a01,a10,a11=chosen
            def P(p):
                return a00*(1-p)**2+(a01+a10)*p*(1-p)+a11*p*p
            # A degree-2 polynomial equal to 1-2p on an interval must agree
            # at three distinct points; no deterministic two-bit event can.
            matches=all(P(p)==1-2*p for p in (F(0),F(1,4),F(1,2)))
            if matches:possible.append(chosen)
        self.assertEqual(possible,[])

    def test_calibrated_finite_event_probability(self):
        for a in range(25):
            self.assertEqual(uniform_L_event_probability(a),F(1,a+2))
            self.assertLessEqual(uniform_L_event_probability(a),F(1,2))

    def test_max_entropy_two_bit_rates_do_not_force_noisy_channel(self):
        self.assertEqual(oily_parameters(1),(F(1,2),F(1,2)))
        # Same emitter occupancy with distinct independent sensor fidelities.
        self.assertNotEqual(ks_signal_to_noise(2,F(1,2)),ks_signal_to_noise(2,F(3,4)))


class BroadcastThresholdTests(unittest.TestCase):
    def test_two_branch_half_correlation_below_ks(self):
        self.assertEqual(ks_signal_to_noise(2,F(1,2)),F(1,2))
        self.assertGreater(ks_signal_to_noise(5,F(1,2)),1)

    def test_exact_census_variance_formula_and_threshold(self):
        self.assertEqual(normalized_census_variance(2,F(1,2),0),0)
        self.assertEqual(normalized_census_variance(2,F(1,2),1),F(3,2))
        self.assertEqual(normalized_census_variance(5,F(1,2),1),F(3,5))
        a=[normalized_census_variance(2,F(1,2),j) for j in (1,2,3,4)]
        self.assertTrue(all(x<y for x,y in zip(a,a[1:])))
        bound=(1-F(1,4))/(ks_signal_to_noise(5,F(1,2))-1)
        self.assertLess(normalized_census_variance(5,F(1,2),20),bound)

    def test_variance_exact_against_exhaustive_tree(self):
        model=BinaryTreePrior(2,F(1,2),F(1))
        for depth in (1,2):
            verts=sum(2**j for j in range(depth+1))
            N=2**depth
            mean=F(0); second=F(0)
            for children in product((-1,1), repeat=verts-1):
                nodes=(1,)+children
                prob=model.finite_cylinder(nodes,depth)
                s=sum(nodes[-N:])/F((2*model.theta)**depth)
                mean+=prob*s;second+=prob*s*s
            self.assertEqual(mean,1)
            self.assertEqual(second-1,normalized_census_variance(2,F(1,2),depth))

    def test_normalized_census_requires_nonzero_channel(self):
        with self.assertRaises(PriorInflationError):normalized_census_variance(2,0,3)

    def test_transient_inflation_returns_to_subcritical_deep_frontier(self):
        # Uniform binary noise and b=2 after the finite inflation phase:
        # each future layer increases the variance lower-bound contribution.
        g=ks_signal_to_noise(2,F(1,2))
        self.assertLess(g,1)
        self.assertGreater(normalized_census_variance(2,F(1,2),25),normalized_census_variance(2,F(1,2),5))


class PreexistingCorrelationTests(unittest.TestCase):
    def test_bayes_update_without_remote_signal(self):
        self.assertEqual(correlated_remote_update(F(1,2),1),F(5,8))
        self.assertEqual(correlated_remote_update(F(1,2),-1),F(3,8))
        self.assertEqual((correlated_remote_update(F(1,2),1)+correlated_remote_update(F(1,2),-1))/2,F(1,2))

    def test_independent_and_perfect_latent_controls(self):
        self.assertEqual(correlated_remote_update(0,1),F(1,2))
        self.assertEqual(correlated_remote_update(1,1),F(1))
        self.assertEqual(correlated_remote_update(1,-1),F(0))


if __name__ == "__main__":
    unittest.main()
