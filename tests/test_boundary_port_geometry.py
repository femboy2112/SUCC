"""Exact source/port naturality and future-safe tomography hostile regressions."""
from fractions import Fraction as Q
from itertools import permutations, product
import unittest

from observational_succ.boundary_port_geometry import (
    Network, PortFrame, PortSourceError, action_descent, diamond,
    diamond_bridge_inverse, diamond_contact_response, future_safe_partition,
    two_contact_gain_inverse, hidden_contact_defect,
)
from observational_succ.dynamic_boundary_inverse import RCNetwork


PORTS=(('L','u'),('u','v'),('v','R'),('L','R'))
WEIGHTS=(Q(1),Q(7),Q(2),Q(3))


def independent_parent_response(net):
    """Use earlier repository's distinct RCNetwork/Schur code as second oracle."""
    aggregate={}
    for a,b,g in net.edges:
        k=tuple(sorted((a,b)))
        aggregate[k]=aggregate.get(k,Q())+g
    supplied=tuple((a,b,g) for (a,b),g in sorted(aggregate.items()))
    return RCNetwork('source-check', net.vertices, net.boundary, supplied).response(0)


class PortFrameTheoremTests(unittest.TestCase):
    def test_exact_anchor_and_known_initial_response(self):
        base=diamond()
        self.assertEqual(base.dt_n(),((Q(1),Q(-1)),(Q(-1),Q(1))))
        self.assertEqual(base.dt_n(),independent_parent_response(base))
        with self.assertRaises(PortSourceError):
            Network(('L','u'),('L',),(('u','u',Q(1)),))
        with self.assertRaises(PortSourceError):
            Network(('L','u'),('L',),())
        with self.assertRaises(PortSourceError):
            diamond(Q(-1))
        with self.assertRaises(PortSourceError):
            base.add(('u','v'),0)

    def test_every_individual_port_update_is_exact_and_monotone(self):
        base=diamond()
        F=PortFrame.from_network(base,PORTS)
        for k,g in enumerate(WEIGHTS):
            actual=base.add(PORTS[k],g)
            updated=F.update(k,g)
            new=PortFrame.from_network(actual,PORTS)
            self.assertEqual(updated,new)
            self.assertEqual(updated.Lambda,independent_parent_response(actual))
            for u in ((Q(1),Q()),(Q(),Q(1)),(Q(2),Q(-3))):
                before=sum(u[i]*F.Lambda[i][j]*u[j] for i in range(2) for j in range(2))
                after=sum(u[i]*updated.Lambda[i][j]*u[j] for i in range(2) for j in range(2))
                self.assertGreaterEqual(after,before)

    def test_all_24_permutations_rebuild_same_complete_response_jet(self):
        base=diamond()
        start=PortFrame.from_network(base,PORTS)
        target=base
        for i in range(len(PORTS)):
            target=target.add(PORTS[i],WEIGHTS[i])
        true=PortFrame.from_network(target,PORTS)
        self.assertEqual(true.Lambda,independent_parent_response(target))
        for order in permutations(range(4)):
            F=start; net=base
            for k in order:
                F=F.update(k,WEIGHTS[k])
                net=net.add(PORTS[k],WEIGHTS[k])
                self.assertEqual(F,PortFrame.from_network(net,PORTS))
                self.assertEqual(F.Lambda,independent_parent_response(net))
            self.assertEqual(F,true)

    def test_repeated_source_port_is_additive(self):
        base=diamond()
        F=PortFrame.from_network(base,PORTS)
        for a,b in ((Q(1),Q(2)),(Q(3,7),Q(11,13))):
            left=F.update(1,a).update(1,b)
            right=F.update(1,a+b)
            self.assertEqual(left,right)
            self.assertEqual(left,PortFrame.from_network(base.add(PORTS[1],a+b),PORTS))

    def test_recorded_forward_backward_frames_reconstruct_all_path_histories(self):
        start=PortFrame.from_network(diamond(),PORTS)
        for order in permutations(range(4)):
            state=start
            record=[]
            for idx in order:
                state=state.update(idx,WEIGHTS[idx])
                record.append((idx,WEIGHTS[idx]))
            for idx,g in reversed(record):
                state=state.reverse_recorded_update(idx,g)
            self.assertEqual(state,start)
        after=start.update(1,Q(7))
        self.assertEqual(after.Lambda,start.Lambda)
        self.assertNotEqual(after.R,start.R)
        self.assertEqual(after.reverse_recorded_update(1,Q(7)),start)
        self.assertNotEqual(after.reverse_recorded_update(1,Q(6)),start)
        with self.assertRaises(PortSourceError):after.reverse_recorded_update(1,Q(0))
        with self.assertRaises(PortSourceError):after.reverse_recorded_update(1,Q(100))

    def test_source_orientation_is_a_gauge_not_new_physics(self):
        base=diamond(Q(7))
        F=PortFrame.from_network(base,PORTS)
        flip=F.reorient(1)
        ports2=tuple((b,a) if i==1 else (a,b) for i,(a,b) in enumerate(PORTS))
        self.assertEqual(flip,PortFrame.from_network(base,ports2))
        self.assertEqual(flip.Lambda,F.Lambda)
        self.assertEqual(flip.update(1,Q(3)).Lambda,F.update(1,Q(3)).Lambda)
        self.assertEqual(flip.reorient(1),F)

    def test_reject_bad_port_and_float_mutations(self):
        base=diamond()
        for ps in ((), (('L','L'),), (('L','ghost'),)):
            with self.assertRaises(PortSourceError):PortFrame.from_network(base,ps)
        F=PortFrame.from_network(base,PORTS)
        for v in (0,True,0.2,Q(-1)):
            with self.assertRaises(PortSourceError):F.update(0,v)
        with self.assertRaises(PortSourceError):F.update(len(PORTS),Q(1))
        with self.assertRaises(PortSourceError):F.reorient(-1)


class IndependentTopologyHoldout(unittest.TestCase):
    def test_asymmetric_three_electrode_six_vertex_holdout(self):
        # Chosen independently of the symmetric diamond derivation. Three
        # electrodes, three hidden nodes and five distinct source ports.
        base=Network(
            ('A','B','C','u','v','w'),('A','B','C'),
            (('A','u',Q(2)),('u','B',Q(3)),('B','v',Q(5,2)),
             ('v','C',Q(7,3)),('u','v',Q(1,5)),('v','w',Q(4)),
             ('w','A',Q(11,4)),('A','C',Q(3,7))),
        )
        ports=(('A','v'),('u','w'),('B','C'),('w','C'),('u','v'))
        strengths=(Q(1,3),Q(2,5),Q(4),Q(1,7),Q(13,11))
        F0=PortFrame.from_network(base,ports)
        self.assertEqual(F0.Lambda,independent_parent_response(base))
        checked=0
        for order in permutations(range(5)):
            net=base; F=F0
            for k in order:
                net=net.add(ports[k],strengths[k]);F=F.update(k,strengths[k])
                self.assertEqual(F,PortFrame.from_network(net,ports))
                self.assertEqual(F.Lambda,independent_parent_response(net))
                checked+=1
            for k in reversed(order):
                F=F.reverse_recorded_update(k,strengths[k])
            self.assertEqual(F,F0)
        self.assertEqual(checked,600)


class HiddenBridgeTomography(unittest.TestCase):
    def test_hidden_bridge_does_not_change_present_boundary(self):
        no,yes=diamond(Q(0)),diamond(Q(7))
        self.assertEqual(no.dt_n(),yes.dt_n())
        f0=PortFrame.from_network(no,PORTS)
        f7=PortFrame.from_network(yes,PORTS)
        self.assertEqual(f0.W,f7.W)
        self.assertNotEqual(f0.R,f7.R)
        self.assertEqual(f0.R[0][0],Q(1,2))
        self.assertEqual(f7.R[0][0],Q(9,32))
        self.assertEqual(f0.W[0][0],Q(1,2))
        self.assertEqual(f7.W[0][0],Q(1,2))
        self.assertEqual(f0.update(1,Q(7)),f7)

    def test_one_contact_measures_hidden_conductance_exactly(self):
        for a,g in product((Q(1,3),Q(1),Q(2),Q(17,5)),(Q(0),Q(1),Q(7),Q(23,3))):
            c=diamond_contact_response(a,g)
            self.assertEqual(c,diamond(g).add(PORTS[0],a).dt_n()[0][0])
            self.assertEqual(g,diamond_bridge_inverse(a,c))
        self.assertEqual(diamond_contact_response(1,0),Q(7,6))
        self.assertEqual(diamond_contact_response(1,7),Q(49,41))
        self.assertEqual(diamond_bridge_inverse(1,Q(49,41)),Q(7))

    def test_response_difference_exact_stability_identity(self):
        for a,g,h in product((Q(1),Q(2),Q(1,4)),(Q(0),Q(2),Q(7)),(Q(9),Q(22))):
            c=lambda x:diamond_contact_response(a,x)
            d=lambda x:(a+4)*x+2*a+4
            self.assertEqual(c(h)-c(g),a*a*(h-g)/(d(h)*d(g)))
        self.assertEqual(diamond_contact_response(0,0),diamond_contact_response(0,7))
        with self.assertRaises(PortSourceError):diamond_bridge_inverse(0,Q(1))
        with self.assertRaises(PortSourceError):diamond_bridge_inverse(1,Q(6,5))
        with self.assertRaises(PortSourceError):diamond_bridge_inverse(1,Q(99))

    def test_two_strength_contacts_reconstruct_hidden_green_kernel(self):
        for g,r_expected in ((Q(),Q(1,2)),(Q(7),Q(9,32)),(Q(11),Q(13,48))):
            d1=diamond_contact_response(1,g)-1
            d2=diamond_contact_response(2,g)-1
            A,r=two_contact_gain_inverse(1,d1,2,d2)
            self.assertEqual(A,Q(1,4))
            self.assertEqual(r,r_expected)
        with self.assertRaises(PortSourceError):two_contact_gain_inverse(1,Q(0),2,Q(1,2))
        with self.assertRaises(PortSourceError):two_contact_gain_inverse(1,Q(1,2),1,Q(1,3))

    def test_hidden_change_first_appears_in_third_order_mixed_susceptibility(self):
        frame=PortFrame.from_network(diamond(),PORTS)
        for z,a in product((Q(1,3),Q(7),Q(11)),(Q(1,3),Q(1),Q(2))):
            info=hidden_contact_defect(frame,1,0,z,a)
            self.assertEqual(info['observed_exact_defect'],info['source_formula'])
            self.assertEqual(info['observed_exact_defect'][0][0],
                             diamond_contact_response(a,z)-diamond_contact_response(a,0))
            self.assertEqual(info['cubic_coefficient'][0][0],Q(1,16))
            self.assertEqual(info['mixed_third_derivative_at_zero'][0][0],Q(1,8))
            self.assertEqual(info['first_hidden_variation_at_zero'][0][0],Q())
            self.assertEqual(info['mixed_second_at_zero'][0][0],Q())
        with self.assertRaises(PortSourceError):
            hidden_contact_defect(frame,0,1,Q(1),Q(1))

    def test_wrong_source_label_changes_prediction(self):
        frame=PortFrame.from_network(diamond(),PORTS)
        true=frame.update(0,Q(1)).Lambda
        fake=frame.update(1,Q(1)).Lambda
        self.assertNotEqual(true,fake)
        self.assertEqual(fake,frame.Lambda)


class SourceCategoryTests(unittest.TestCase):
    def setUp(self):
        self.states=('before0','before7','after0','after7')
        self.obs={'before0':Q(1),'before7':Q(1),'after0':Q(7,6),'after7':Q(49,41)}
        self.actions={
            'contact':{'before0':'after0','before7':'after7','after0':'after0','after7':'after7'},
            'idle':{x:x for x in self.states},
        }

    def test_present_boundary_action_not_well_defined(self):
        induced,obstruction=action_descent(self.states,self.obs,self.actions)
        self.assertIsNone(induced)
        self.assertEqual(obstruction[0],'contact')
        self.assertEqual(set(obstruction[1:3]),{'before0','before7'})

    def test_one_future_probe_repairs_the_observational_quotient(self):
        data=future_safe_partition(self.states,self.obs,self.actions)
        self.assertEqual(data['rounds'],1)
        self.assertEqual(data['minimal_observable_state_count'],4)
        self.assertNotEqual(data['classes']['before0'],data['classes']['before7'])
        signals={x:(self.obs[x],self.obs[self.actions['contact'][x]]) for x in self.states}
        induced,obstruction=action_descent(self.states,signals,self.actions)
        self.assertIsNone(obstruction)
        self.assertIsNotNone(induced)

    def test_perfectly_hidden_duplicate_is_not_resolved_by_more_steps(self):
        states=('a','b')
        obs={'a':Q(1),'b':Q(1)}
        actions={'swap':{'a':'b','b':'a'},'idle':{'a':'a','b':'b'}}
        self.assertEqual(future_safe_partition(states,obs,actions)['minimal_observable_state_count'],1)
        self.assertIsNotNone(action_descent(states,obs,actions)[0])

    def test_invalid_unauthenticated_action_rejected(self):
        with self.assertRaises(PortSourceError):
            future_safe_partition(self.states,self.obs,{'contact':{'before0':'after0'}})


class IndependentObjectHoldouts(unittest.TestCase):
    def test_first_level_alias_not_intrinsic_ring_ontology(self):
        # Existing OPIG PR #238 construction, independently recomputed.
        # Z/4 has two outcomes under multiplication by 2; F2[t]/t2 has one.
        integer_ring = {2*x%4 for x in range(4)}
        dual_ring = {(0,0)}  # char 2: 2*(a+bt)=0 for all a,b
        self.assertEqual(len(integer_ring),2)
        self.assertEqual(len(dual_ring),1)
        self.assertEqual({x%2 for x in range(4)},{0,1})

    def test_independent_gauge_marginals_do_not_select_joint_coupling(self):
        n=4
        locked={(x,y):(Q(1,n) if y==x else Q()) for x in range(n) for y in range(n)}
        free={(x,y):Q(1,n*n) for x in range(n) for y in range(n)}
        for x in range(n):
            self.assertEqual(sum(locked[(x,y)] for y in range(n)),Q(1,n))
            self.assertEqual(sum(free[(x,y)] for y in range(n)),Q(1,n))
        self.assertNotEqual(sum(locked[(x,x)] for x in range(n)),
                            sum(free[(x,x)] for x in range(n)))

    def test_product_fiber_singleton_does_not_prove_physical_cross_map(self):
        models=list(product((Q(),Q(7)),('Z4','F2_dual'),('locked','free')))
        # All models fit calibrated present Lambda=1, first-shell F2, Haar marginals.
        self.assertEqual(len(models),8)
        after_contact=[m for m in models if diamond_contact_response(1,m[0])==Q(49,41)]
        after_ring=[m for m in after_contact if (2 if m[1]=='Z4' else 1)==2]
        after_joint=[m for m in after_ring if (Q(1) if m[2]=='locked' else Q(1,4))==1]
        self.assertEqual(len(after_contact),4)
        self.assertEqual(len(after_ring),2)
        self.assertEqual(after_joint,[(Q(7),'Z4','locked')])
        # This singleton is a PRODUCT-model identification, NOT a demonstrated
        # source-natural transformation from a physical discharge to prime clocks.


if __name__ == '__main__':
    unittest.main()
