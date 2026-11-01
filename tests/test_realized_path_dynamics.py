"""Exact tests for the new positive history dynamics and original BBP source firewall."""
from __future__ import annotations
import unittest,importlib.util,sys
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/'research'/'2026-10-31'/'realized_path_dynamics'
def load(name,filename):
    spec=importlib.util.spec_from_file_location(name,ROOT/filename)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod
m=load('realized_path_20261031_main','realized_path.py')
o=load('realized_path_20261031_oracle','independent_oracle.py')

class RealizedPathTest(unittest.TestCase):
    def setUp(self):self.model=m.history_model()

    def test_path_count(self):self.assertEqual(len(self.model.enumerate_paths()),5)
    def test_prior_normalization(self):self.assertEqual(sum((p.prior for p in self.model.enumerate_paths()),F()),1)
    def test_path_prior_independent(self):
        self.assertEqual({p.labels:p.prior for p in self.model.enumerate_paths()},o.directed_reference_path_weights())
    def test_reference_source_support(self):
        self.assertEqual({p.endpoint for p in self.model.enumerate_paths()},{'T','X','Y'})
    def test_same_observed_state(self):self.assertEqual(m.observed_position('A'),m.observed_position('B'))
    def test_different_future_support(self):
        self.assertEqual(m.deconditioned_future_support(self.model,('A',)),frozenset({'T','X'}))
        self.assertEqual(m.deconditioned_future_support(self.model,('B',)),frozenset({'T','X','Y'}))
    def test_different_terminal_probabilities_before_tilt(self):
        self.assertEqual(sum((p.prior for p in self.model.enumerate_paths() if p.labels==('A','hit')),F()),F(3,8))
        self.assertEqual(sum((p.prior for p in self.model.enumerate_paths() if p.labels==('B','hit')),F()),F(1,8))
    def test_target_desirability(self):
        d=self.model.desirability()
        self.assertEqual(d[2],{'T':F(1),'X':F(),'Y':F()})
        self.assertEqual(d[1]['A'],F(3,4));self.assertEqual(d[1]['B'],F(1,16))
        self.assertEqual(d[0]['root'],F(13,32))
    def test_terminal_conditioned_gibbs(self):
        q=self.model.tilted_paths();self.assertEqual(sum(q.values(),F()),F(1))
        self.assertEqual({p.labels:w for p,w in q.items() if w},o.target_gibbs_weights(F(1,2)))
    def test_optimal_first_transition(self):self.assertEqual(self.model.optimal_transition(0,'root'),{'A':F(12,13),'B':F(1,13)})
    def test_optimal_post_A(self):self.assertEqual(self.model.optimal_transition(1,'A'),{'hit':F(1),'miss':F()})
    def test_optimal_post_B(self):self.assertEqual(self.model.optimal_transition(1,'B'),{'hit':F(1),'miss':F(),'sidetrack':F()})
    def test_path_gibbs_ratio(self):self.assertTrue(m.posterior_partition_identity(self.model))
    def test_prefix_normalization_A(self):
        prob,q=self.model.condition(('A',))
        self.assertEqual(prob,F(12,13));self.assertEqual(sum(q.values(),F()),1)
        self.assertEqual({p.labels:w for p,w in q.items() if w},{('A','hit'):F(1)})
    def test_prefix_normalization_B(self):
        prob,q=self.model.condition(('B',));self.assertEqual(prob,F(1,13))
        self.assertEqual({p.labels:w for p,w in q.items() if w},{('B','hit'):F(1)})
    def test_prefix_information_ratio_A(self):
        mass,_=self.model.condition(('A',));self.assertEqual(1/mass,F(13,12))
    def test_prefix_information_ratio_B(self):
        mass,_=self.model.condition(('B',));self.assertEqual(1/mass,F(13))
    def test_condition_full_path(self):
        prob,q=self.model.condition(('A','hit'))
        self.assertEqual(prob,F(12,13));self.assertEqual(sum(q.values(),F()),1)
    def test_condition_zero_probability_rejected(self):
        with self.assertRaises(ValueError):self.model.condition(('A','miss'))
    def test_empty_prefix_returns_original(self):
        mass,q=self.model.condition(())
        self.assertEqual(mass,1);self.assertEqual(q,self.model.tilted_paths())
    def test_no_legal_prefix_rejected(self):
        with self.assertRaises(ValueError):self.model.condition(('not-realized',))
    def test_zero_temperature_geodesic(self):
        self.assertEqual(m.zero_temperature_branch(F(1)),F(3,4))
        self.assertEqual(m.zero_temperature_branch(F(1,2)),F(12,13))
        self.assertEqual(m.zero_temperature_branch(F(1,1000)),F(3000000,3000001))
        self.assertGreater(m.zero_temperature_branch(F(1,1000)),m.zero_temperature_branch(F(1,2)))
    def test_tie_not_forced_unique(self):
        # At lambda=1, costs do not change reference target-conditioned odds: 3:1, not a deterministic geodesic.
        self.assertEqual(self.model.optimal_transition(0,'root',F(1))['A'],F(3,4))
    def test_positive_entropy_future_can_rise(self):
        before,after=m.entropy_future_counterexample();self.assertEqual(before,F(5,2))
        self.assertEqual(after,3);self.assertGreater(F(after),before)
    def test_missing_terminal(self):
        with self.assertRaises(ValueError):m.PathModel('root',self.model.layers,frozenset({'unreachable'}))
    def test_unnormalized_transition_rejected(self):
        broken=({'root':(m.Edge('bad','A',F(1,3)),)},)+self.model.layers[1:]
        with self.assertRaises(ValueError):m.PathModel('root',broken,frozenset({'T'}))
    def test_duplicate_action_labels_rejected(self):
        broken=({'root':(m.Edge('foo','A',F(1,2)),m.Edge('foo','B',F(1,2)))},)+self.model.layers[1:]
        with self.assertRaises(ValueError):m.PathModel('root',broken,frozenset({'T'}))
    def test_negative_cost_rejected(self):
        with self.assertRaises(ValueError):m.Edge('bad','X',F(1),-1)
    def test_float_prior_rejected(self):
        with self.assertRaises(ValueError):m.Edge('bad','X',.5)
    def test_invalid_lambda_rejected(self):
        for lam in (F(0),F(2),.5):
            with self.assertRaises(ValueError):self.model.desirability(lam)
    def test_zero_desirability_history_rejected(self):
        with self.assertRaises(ValueError):self.model.optimal_transition(1,'X')
    def test_original_four_pole_full_source(self):
        for n in range(1,60):self.assertEqual(m.original_source(n),o.source_combined(n))
    def test_original_noncommutative_matrix(self):
        self.assertEqual(m.source_commutator(),F(12301,273))
        self.assertEqual(m.source_commutator(),o.two_step_affine_difference())
    def test_original_order_matches_state(self):
        a=m.matmul(m.source_step(2),m.source_step(1))
        self.assertEqual(a[0][1],m.original_state(2))
        self.assertNotEqual(a,m.matmul(m.source_step(1),m.source_step(2)))
    def test_BBP_matrix_convolution(self):
        for n in range(0,25):self.assertEqual(m.original_state(n),o.state_convolution(n))
    def test_BBP_action_canonical(self):
        for n in range(0,25):
            self.assertEqual(m.original_action(n),o.action_convolution(n))
            self.assertEqual(m.original_action(n),m.symplectic_source_action(n))
    def test_BBP_seedblind_action_increments(self):
        # Two initial seeds can have same source/action increment but different action baseline.
        for n in range(1,10):
            self.assertEqual(m.original_action(n)-m.original_action(n-1),o.source_combined(n)/16**n)
    def test_source_rejects_negative_index(self):
        for n in (0,-1,1.5,'1'):
            with self.assertRaises(ValueError):m.original_source(n)
    def test_operator_integral_exact_factorization(self):
        one=((F(1,2),0,m.source_step(1)),(F(1,2),1,m.IDENTITY))
        two=((F(1,2),1,m.source_step(2)),(F(1,2),0,m.IDENTITY))
        actual,factor=m.finite_operator_path_integral((one,two))
        self.assertEqual(actual,factor)
    def test_operator_integral_order_matters(self):
        one=((F(1,2),0,m.source_step(1)),(F(1,2),0,m.IDENTITY))
        two=((F(1,2),0,m.source_step(2)),(F(1,2),0,m.IDENTITY))
        a,_=m.finite_operator_path_integral((one,two))
        b,_=m.finite_operator_path_integral((two,one))
        self.assertNotEqual(a,b)
    def test_naive_marginal_factor_fails_for_memory(self):
        direct,naive=m.dependent_path_integral()
        self.assertNotEqual(direct,naive)
    def test_matrix_product_associativity(self):
        a=m.source_step(1);b=m.source_step(2);c=m.source_step(3)
        self.assertEqual(m.matmul(a,m.matmul(b,c)),m.matmul(m.matmul(a,b),c))
    def test_matrix_source_first_zero(self):self.assertEqual(m.source_product(0),m.IDENTITY)
    def test_matrix_action_original_first(self):self.assertEqual(m.source_product(1)[0][1],F(47,15))
    def test_entropy_does_not_fix_signed_cancellation(self):self.assertEqual(m.phase_model_counterexample(),(F(1),F()))
    def test_full_path_zero_entropy_under_determinism(self):
        # Exactly one original BBP path exists once source, zero seed, and horizon are fixed.
        self.assertEqual(len({tuple(m.original_source(n) for n in range(1,N+1)) for N in (5,)}),1)
    def test_affine_momentum_frame(self):
        for n in range(1,12):
            xn=m.original_state(n);pn=F(1,16**n)
            self.assertEqual(xn*pn,m.original_action(n))

if __name__=='__main__':unittest.main()

class HamiltonianPathTest(unittest.TestCase):
    def test_idempotent_generator_many(self):
        for i in range(1,14):
            g=m.normalized_generator(i)
            self.assertEqual(m.matmul(g,g),g)
            self.assertEqual(m.matadd(m.IDENTITY,m.matscale(g,F(15))),m.source_step(i))
    def test_generator_right_zero_band(self):
        for i in range(1,7):
            for j in range(1,7):
                self.assertEqual(m.matmul(m.normalized_generator(i),m.normalized_generator(j)),m.normalized_generator(j))
    def test_generator_noncommutes(self):
        self.assertNotEqual(m.normalized_generator(1),m.normalized_generator(2))
        self.assertEqual(m.generator_commutator(1,2),F(106,819)/15-F(47,15)/15)
    def test_commutator_recovers_affine_order(self):
        for i in range(1,6):
            for j in range(1,6):
                x=m.matmul(m.source_step(j),m.source_step(i))
                y=m.matmul(m.source_step(i),m.source_step(j))
                self.assertEqual(x[0][1]-y[0][1],F(225)*(-m.generator_commutator(i,j)))
    def test_flow_end_time_matches_original_affine(self):
        for n in range(1,16):
            for x,p in ((F(),F(1)),(F(3,5),F(7,9)),(F(-2,3),F(11,6))):
                xn,pn=m.symplectic_segment(n,x,p,4)
                self.assertEqual(xn,F(16)*x+m.original_source(n))
                self.assertEqual(pn,p/16)
    def test_flow_semigroup_half_times(self):
        for n in range(1,18):
            x,p=F(2,3),F(5,7)
            midx,midp=m.symplectic_segment(n,x,p,2)
            self.assertEqual(m.symplectic_segment(n,midx,midp,2),m.symplectic_segment(n,x,p,4))
    def test_flow_semigroup_quarter_step(self):
        for n in range(1,11):
            x,p=F(2),F(3)
            midx,midp=m.symplectic_segment(n,x,p,1)
            midx,midp=m.symplectic_segment(n,midx,midp,1)
            midx,midp=m.symplectic_segment(n,midx,midp,1)
            midx,midp=m.symplectic_segment(n,midx,midp,1)
            self.assertEqual((midx,midp),m.symplectic_segment(n,x,p,4))
    def test_Hamiltonian_source_increment_as_pairing(self):
        for n in range(1,20):
            p0=F(1,16**(n-1))
            x0=m.original_state(n-1)
            xn,pn=m.symplectic_segment(n,x0,p0,4)
            self.assertEqual(xn*pn-x0*p0,m.original_source(n)/16**n)
    def test_inside_segment_pairing(self):
        for n in range(1,11):
            x0,p0=F(1,3),F(5,7)
            for k in range(5):
                x,p=m.symplectic_segment(n,x0,p0,k)
                z=F(2**k)
                self.assertEqual(x*p-x0*p0,p0*m.original_source(n)*F(z-1,z*15))
    def test_micro_histories_end_same(self):
        for n in range(1,10):
            a,b=m.micro_paths_same_endpoint(n,F(n,17))
            self.assertEqual(a[1],b[1]);self.assertNotEqual(a[0],b[0])
    def test_microhistories_same_endpoint_phase(self):
        # Every endpoint-dependent source character is identical, despite distinct microhistories.
        for n in range(1,10):
            a,b=m.micro_paths_same_endpoint(n,F(7,11))
            self.assertEqual(a[-1]-b[-1],0)
    def test_microhistories_same_canonical_action(self):
        for n in range(1,8):
            x=m.original_state(n-1)
            aa,bb=m.micro_paths_same_endpoint(n,x)
            self.assertEqual(aa[1]/16**n,bb[1]/16**n)
    def test_flow_wrong_input_rejected(self):
        for k in (-1,5,1.0):
            with self.assertRaises(ValueError):m.symplectic_segment(1,F(1),F(1),k)
    def test_micro_wrong_input_rejected(self):
        with self.assertRaises(ValueError):m.micro_paths_same_endpoint(1,0.0)

class IdempotentPathSumTests(unittest.TestCase):
    def test_exact_band_expansion_all_horizons(self):
        for n in range(0,35):self.assertEqual(m.ordered_band_expansion(n),m.source_product(n))
    def test_subset_enumeration_independent(self):
        for n in range(0,11):self.assertEqual(m.subset_band_expansion(n),m.ordered_band_expansion(n))
    def test_original_state_from_band(self):
        for n in range(0,24):self.assertEqual(m.ordered_band_expansion(n)[0][1],m.original_state(n))
    def test_band_weight_sum_top_left(self):
        for n in range(1,25):
            self.assertEqual(1+sum(15*16**(n-j) for j in range(1,n+1)),16**n)
    def test_band_early_source_coefficient(self):
        for n in range(1,14):
            coeff=15*16**(n-1)
            self.assertGreater(coeff,0)
    def test_tied_geodesic_stays_nondeterministic(self):
        model=m.tied_geodesic_model()
        for d in (F(1),F(1,2),F(1,100000)):
            self.assertEqual(model.optimal_transition(0,'root',d),{'first':F(1,2),'second':F(1,2)})
    def test_invalid_subset_budget(self):
        for n in (-1,15):
            with self.assertRaises(ValueError):m.subset_band_expansion(n)

class TelescopingSelectionTests(unittest.TestCase):
    def test_product_doob_equal_enumerated_posterior(self):
        model=m.history_model()
        q=model.tilted_paths()
        for path,weight in q.items():
            self.assertEqual(m.doob_path_weight(model,path.labels),weight)
    def test_doob_zero_path(self):
        model=m.history_model()
        self.assertEqual(m.doob_path_weight(model,('A','miss')),0)
        self.assertEqual(m.doob_path_weight(model,('B','sidetrack')),0)
    def test_doob_all_lambda_values(self):
        for lam in (F(1),F(1,2),F(1,3),F(1,128)):
            model=m.history_model()
            for path,q in model.tilted_paths(lam).items():
                self.assertEqual(m.doob_path_weight(model,path.labels,lam),q)
    def test_doob_bad_path_rejected(self):
        with self.assertRaises(ValueError):m.doob_path_weight(m.history_model(),('Z','hit'))
    def test_time_index_entropy_does_not_force_cancel(self):
        for n in (2,4,16,128):
            horizon,alternate=m.time_entropy_only_no_go(n)
            self.assertEqual(horizon,n);self.assertEqual(alternate,0)
            self.assertEqual(sum((F(1) for _ in range(n)),F())/n,1)
    def test_time_entropy_bad_scope(self):
        for n in (0,1,3,-2,2.0):
            with self.assertRaises(ValueError):m.time_entropy_only_no_go(n)

class ActionTiltFirewallTest(unittest.TestCase):
    def test_original_source_decay_bound(self):
        for j in range(2,160):
            self.assertLess(m.original_source(j),F(15,64*(j-1)**2))
    def test_action_defect_mass_uniform(self):
        for j in (2,3,5,10,50,120,250):
            self.assertGreater(m.finite_action_tail_mass(j),0)
            self.assertLess(m.finite_action_tail_mass(j),F(1,1024))
    def test_action_tail_mass_monotone(self):
        self.assertLess(m.finite_action_tail_mass(10),m.finite_action_tail_mass(11))
    def test_rational_tilt_positivity(self):
        for n in (1,2,5,10,16):
            w=m.rational_action_tilt_weights(n)
            self.assertEqual(len(w),n)
            self.assertTrue(all(0<x<=1 for x in w))
    def test_weighted_constant_char_same(self):
        for n in (2,5,12):
            w=m.rational_action_tilt_weights(n)
            self.assertEqual(m.weighted_mean_real((F(1),)*n,w),1)
    def test_weighted_alternating_rational_character(self):
        for n in (2,4,8,12,16):
            w=m.rational_action_tilt_weights(n)
            z=tuple(F((-1)**j) for j in range(n))
            self.assertLessEqual(abs(m.weighted_mean_real(z,w)),F(1))
    def test_weighted_source_time_tilt_not_randomness(self):
        w=m.rational_action_tilt_weights(12)
        self.assertLess(w[-1],w[0]) # increasing canonical action => inverse weights decline
    def test_action_tilt_bad_inputs(self):
        for n in (0,-1,1.0):
            with self.assertRaises(ValueError):m.rational_action_tilt_weights(n)
    def test_mean_bad_lengths(self):
        with self.assertRaises(ValueError):m.weighted_mean_real((F(1),),(F(1),F(2)))
