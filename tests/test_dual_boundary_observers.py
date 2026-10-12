"""Exact dual E-boundary falsifiers: source, common factor, flux and infinity."""
import sys
import unittest
from fractions import Fraction as F
from itertools import product
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.dual_boundary_observers import (
    DualBoundaryError, DualFiniteTower, TwoSidedHarmonicCarrier,
    two_port_carrier, unit_path_two_port, symmetric_binary_chain_end_correlation)
from observational_succ.shared_carrier_descent import SharedCarrierGraph


def bits():
    states=tuple(product(range(2),repeat=2))
    return DualFiniteTower('same-carrier',0,states,(F(1,4),)*4,
        (((0,)*4),tuple(s[0] for s in states)),
        (((0,)*4),tuple(s[1] for s in states)))


def half_graph(tag,edges,outer,iface=('m',),version=0,vertices=None):
    vertices=vertices or tuple(dict.fromkeys(x for a,b,_ in edges for x in (a,b)))
    return SharedCarrierGraph(tag,version,vertices,tuple(outer)+tuple(iface),tuple(edges))


class DualObserverTests(unittest.TestCase):
    def test_same_source_does_not_force_correlated_outcomes(self):
        t=bits()
        left=t.observations('left');right=t.observations('right')
        ea=sum((p*F(int(x)) for p,x in zip(t.prior,left)),F(0))
        eb=sum((p*F(int(x)) for p,x in zip(t.prior,right)),F(0))
        eab=sum((p*F(int(a))*F(int(b)) for p,a,b in zip(t.prior,left,right)),F(0))
        self.assertEqual(eab-ea*eb,F(0))
        self.assertEqual(t.common_factor()['component_count'],1)

    def test_two_incomplete_observers_jointly_prove_xor(self):
        t=bits()
        target=tuple(a^b for a,b in t.states)
        self.assertFalse(t.claim_factors(target,'left')['factors'])
        self.assertFalse(t.claim_factors(target,'right')['factors'])
        self.assertTrue(t.claim_factors(target,'joint')['factors'])
        self.assertEqual(t.conditional_expectation(target,'left'),(F(1,2),)*4)
        self.assertEqual(t.conditional_expectation(target,'right'),(F(1,2),)*4)
        self.assertEqual(t.conditional_expectation(target,'joint'),target)

    def test_trivial_first_level_and_nontrivial_completion_are_distinct(self):
        t=bits()
        report=t.common_factor(0,0)
        self.assertEqual(report['component_count'],1)
        self.assertEqual(report['exact_common_witness_covariance'],0)
        self.assertEqual(t.common_factor()['component_count'],1)

    def test_shared_nonconstant_bit_gives_positive_exact_witness_variance(self):
        states=tuple(product(range(2),repeat=3))
        t=DualFiniteTower('one-carrier',4,states,(F(1,8),)*8,
            ((('base',)*8),tuple((k,a) for k,a,b in states)),
            ((('base',)*8),tuple((k,b) for k,a,b in states)))
        c=t.common_factor()
        self.assertEqual(c['component_count'],2)
        self.assertEqual(c['common_component_masses'],(F(1,2),F(1,2)))
        self.assertEqual(c['exact_common_witness_covariance'],F(1,4))
        self.assertTrue(t.claim_factors(tuple(k for k,a,b in states),'left')['factors'])
        self.assertTrue(t.claim_factors(tuple(k for k,a,b in states),'right')['factors'])
        self.assertFalse(t.claim_factors(tuple(a for k,a,b in states),'right')['factors'])

    def test_asymmetric_source_priors_are_exact(self):
        states=(0,1,2)
        t=DualFiniteTower('weighted',0,states,(F(1,2),F(1,3),F(1,6)),
                          ((0,0,1),),((0,1,1),))
        self.assertEqual(t.common_factor()['component_count'],1)
        self.assertEqual(t.conditional_expectation((0,3,0),'left'),(F(6,5),F(6,5),F(0)))

    def test_conditional_expectation_orders_fail_to_commute(self):
        t=DualFiniteTower('three-source',1,(0,1,2),(F(1,3),)*3,
                          ((0,0,1),),((0,1,1),))
        x=(F(0),F(1),F(2))
        right_then_left=t.conditional_expectation(
            t.conditional_expectation(x,'right'),'left')
        left_then_right=t.conditional_expectation(
            t.conditional_expectation(x,'left'),'right')
        self.assertEqual(right_then_left,(F(3,4),F(3,4),F(3,2)))
        self.assertEqual(left_then_right,(F(1,2),F(5,4),F(5,4)))
        self.assertNotEqual(right_then_left,left_then_right)
        self.assertEqual(t.conditional_expectation(x,'joint'),x)

    def test_dual_projection_correlation_is_exact_not_heuristic(self):
        t=bits()
        parity=tuple(a^b for a,b in t.states)
        report=t.correlation_receipt(parity)
        self.assertEqual(report['target_variance'],F(1,4))
        self.assertEqual(report['left_l2_error_squared'],F(1,4))
        self.assertEqual(report['right_l2_error_squared'],F(1,4))
        self.assertEqual(report['estimate_covariance'],F(0))
        self.assertFalse(report['strict_correlation_certified'])

    def test_two_limits_to_common_target_certify_positive_correlation(self):
        states=tuple(product(range(2),repeat=3))
        t=DualFiniteTower('one',0,states,(F(1,8),)*8,
            (((0,)*8),tuple(k for k,a,b in states)),
            (((0,)*8),tuple(k for k,a,b in states)))
        target=tuple(k for k,a,b in states)
        self.assertFalse(t.correlation_receipt(target,0,0)['strict_correlation_certified'])
        final=t.correlation_receipt(target,1,1)
        self.assertEqual(final['estimate_covariance'],F(1,4))
        self.assertEqual(final['covariance_guaranteed_lower'],F(1,4))
        self.assertTrue(final['strict_correlation_certified'])

    def test_finite_shared_carrier_projections_may_anticorrelate(self):
        t=DualFiniteTower('one',0,(0,1,2),(F(1,3),)*3,
             ((0,0,1),),((0,1,1),))
        report=t.correlation_receipt((0,1,0))
        self.assertEqual(report['estimate_covariance'],-F(1,36))
        self.assertFalse(report['strict_correlation_certified'])

    def test_witness_is_maximal_common_deterministic_factor(self):
        t=bits()
        self.assertEqual(len(set(t.common_factor()['states_to_component'])),1)
        states=tuple(product(range(3),range(2),range(2)))
        tower=DualFiniteTower('three-cells',1,states,(F(1,len(states)),)*len(states),
                 (tuple((k,a) for k,a,b in states),),
                 (tuple((k,b) for k,a,b in states),))
        self.assertEqual(tower.common_factor()['component_count'],3)

    def test_forged_nonrefining_level_rejected(self):
        with self.assertRaisesRegex(DualBoundaryError,'forgot'):
            DualFiniteTower('one',0,(0,1,2,3),(F(1,4),)*4,
                ((0,0,1,1),(0,1,0,0)),((0,0,0,0),))

    def test_unobserved_level_forgery_and_invalid_prior_rejected(self):
        t=bits()
        with self.assertRaises(DualBoundaryError):t.common_factor(9,0)
        with self.assertRaises(DualBoundaryError):t.conditional_expectation((1,),side='joint')
        with self.assertRaises(DualBoundaryError):t.claim_factors((0,1,0,1),'outside')
        with self.assertRaises(DualBoundaryError):
            DualFiniteTower('one',0,(0,1),(F(1),F(0)),((0,1),),((0,1),))
        with self.assertRaises(DualBoundaryError):
            DualFiniteTower('one',0,(0,1),(0.5,0.5),((0,1),),((0,1),))

    def test_cumulative_towers_never_lose_a_common_factor(self):
        states=tuple(product(range(2),repeat=3))
        t=DualFiniteTower('same',2,states,(F(1,8),)*8,
             ((0,)*8, tuple(s[0] for s in states),tuple((s[0],s[1]) for s in states)),
             ((0,)*8, tuple(s[2] for s in states),tuple((s[0],s[2]) for s in states)))
        levels=[t.common_factor(i,i)['component_count'] for i in range(3)]
        self.assertEqual(levels,[1,1,2])


class TwoSidedCarrierTests(unittest.TestCase):
    def two_edge(self,wl=1,wr=1):
        left=half_graph('shared',(('L','m',F(wl)),),('L',))
        right=half_graph('shared',(('m','R',F(wr)),),('R',))
        return TwoSidedHarmonicCarrier(left,right,('L',),('R',),('m',))

    def test_meeting_in_middle_requires_matching_flux(self):
        tower=self.two_edge()
        left=tower.left.complete_harmonic({'L':F(0),'m':F(0)})
        right=tower.right.complete_harmonic({'m':F(0),'R':F(1)})
        self.assertEqual(tower.left.flux(left)['m'],0)
        self.assertEqual(tower.right.flux(right)['m'],-1)
        self.assertNotEqual(tower.left.flux(left)['m']+tower.right.flux(right)['m'],0)
        result=tower.interface_solution({'L':0},{'R':1})
        self.assertEqual(result['interface'],{'m':F(1,2)})
        self.assertEqual(result['global_energy'],F(1,4))
        self.assertEqual(result['interface_flux_residual'],{'m':0})

    def test_asymmetric_conductance_moves_meeting_point(self):
        tower=self.two_edge(2,1)
        result=tower.interface_solution({'L':0},{'R':1})
        self.assertEqual(result['interface'],{'m':F(1,3)})
        self.assertEqual(result['global_energy'],F(1,3))

    def test_four_edge_chain_assembles_from_own_half_fields(self):
        l=half_graph('one',((0,1,F(1)),(1,2,F(1))),(0,),(2,))
        r=half_graph('one',((2,3,F(1)),(3,4,F(1))),(4,),(2,))
        tower=TwoSidedHarmonicCarrier(l,r,(0,),(4,),(2,))
        done=tower.interface_solution({0:F(0)},{4:F(1)})
        self.assertEqual(done['interface'],{2:F(1,2)})
        self.assertEqual(done['source_field'],{0:F(0),1:F(1,4),2:F(1,2),3:F(3,4),4:F(1)})
        self.assertEqual(done['global_energy'],F(1,8))
        self.assertEqual(two_port_carrier(tower.merged_graph(),(0,),(4,))['effective_conductance'],F(1,4))

    def test_multi_point_interface_solved_simultaneously(self):
        l=half_graph('one',(('L','m0',F(1)),('L','m1',F(1)),('m0','m1',F(2))),('L',),('m0','m1'))
        r=half_graph('one',(('m0','R',F(1)),('m1','R',F(1))),('R',),('m0','m1'))
        t=TwoSidedHarmonicCarrier(l,r,('L',),('R',),('m0','m1'))
        report=t.interface_solution({'L':0},{'R':1})
        self.assertEqual(report['interface'],{'m0':F(1,2),'m1':F(1,2)})
        self.assertEqual(report['global_energy'],F(1,2))

    def test_wrong_source_carrier_or_version_rejected(self):
        l=half_graph('source-a',(('L','m',F(1)),),('L',))
        r=half_graph('source-b',(('m','R',F(1)),),('R',))
        with self.assertRaisesRegex(DualBoundaryError,'Different original'):
            TwoSidedHarmonicCarrier(l,r,('L',),('R',),('m',))
        r=half_graph('source-a',(('m','R',F(1)),),('R',),version=1)
        with self.assertRaises(DualBoundaryError):
            TwoSidedHarmonicCarrier(l,r,('L',),('R',),('m',))

    def test_hidden_overlap_rejected(self):
        l=half_graph('one',(('L','m',F(1)),('L','shared',F(1))),('L',))
        r=half_graph('one',(('m','R',F(1)),('shared','R',F(1))),('R',))
        with self.assertRaisesRegex(DualBoundaryError,'Hidden vertex'):
            TwoSidedHarmonicCarrier(l,r,('L',),('R',),('m',))

    def test_edge_double_ownership_rejected(self):
        l=half_graph('one',(('L','m',F(1)),('m','n',F(1))),('L',),('m','n'))
        r=half_graph('one',(('m','n',F(1)),('n','R',F(1))),('R',),('m','n'))
        with self.assertRaisesRegex(DualBoundaryError,'edge cannot'):
            TwoSidedHarmonicCarrier(l,r,('L',),('R',),('m','n'))

    def test_incomplete_outer_receipts_rejected(self):
        t=self.two_edge()
        with self.assertRaises(DualBoundaryError):t.interface_solution({}, {'R':1})
        with self.assertRaises(DualBoundaryError):t.interface_solution({'L':0}, {'R':1,'extra':0})

    def test_one_connected_stochastic_carrier_ends_decorrelate(self):
        for n in range(1,15):
            report=symmetric_binary_chain_end_correlation(n,F(1,4))
            self.assertEqual(report['endpoint_covariance'],F(1,2**n))
            self.assertTrue(report['both_marginals_symmetric'])
        self.assertEqual(symmetric_binary_chain_end_correlation(1,F(1,2))['endpoint_covariance'],0)
        self.assertEqual(symmetric_binary_chain_end_correlation(3,F(0))['endpoint_covariance'],1)
        with self.assertRaises(DualBoundaryError):
            symmetric_binary_chain_end_correlation(-1,F(1,4))
        with self.assertRaises(DualBoundaryError):
            symmetric_binary_chain_end_correlation(2,F(3,2))

    def test_unit_path_two_port_decay_at_large_distance(self):
        for n in range(1,17):
            receipt=unit_path_two_port(n)
            self.assertEqual(receipt['effective_conductance'],F(1,n))
            self.assertEqual(receipt['energy_for_unit_jump'],F(1,2*n))
        self.assertGreater(unit_path_two_port(2)['effective_conductance'],unit_path_two_port(16)['effective_conductance'])

    def test_disconnected_same_carrier_can_have_zero_cross_transfer(self):
        source=SharedCarrierGraph('one',1,('L','R'),('L','R'),())
        result=two_port_carrier(source,('L',),('R',))
        self.assertEqual(result['effective_conductance'],0)
        self.assertFalse(result['strictly_coupled'])

    def test_reject_invalid_two_port_partition(self):
        graph=self.two_edge().merged_graph()
        for left,right in (((),('R',)),(('L',),()),(('L',),('L',)),(('L',),('not-boundary',))):
            with self.assertRaises(DualBoundaryError):two_port_carrier(graph,left,right)

    def test_exact_independent_direct_reconstruction_random_paths(self):
        # Exhaustive nonnegative boundary values and varied integer conductances.
        for wl,wr in product((1,2,3,5),repeat=2):
            for bl,br in product((F(-1),F(0),F(1)),repeat=2):
                t=self.two_edge(wl,wr)
                receipt=t.interface_solution({'L':bl},{'R':br})
                expect=(F(wl)*bl+F(wr)*br)/(wl+wr)
                self.assertEqual(receipt['interface']['m'],expect)
                self.assertEqual(receipt['global_energy'],
                                 F(wl*wr,2*(wl+wr))*(bl-br)**2)


if __name__=='__main__':unittest.main()
