"""Hostile exact tests for source-faithful bidirectional chronological transport."""
import unittest
from fractions import Fraction as Q
from itertools import permutations

from observational_succ.bidirectional_source_histories import (
    LabelledMarkovSource,SourcePath,HistoryTransportError,affine_backward,
    endpoint_marginal,bicausal_observation_quotient,distinguishable_order_budget,
    lift_field_growth_source,
)


def two_state_source():
    levels=tuple(('A','B') for _ in range(6))
    layers=[]
    for t in range(5):
        stay=Q(t+1,t+3)
        flip=Q(2,t+3)
        layers.append({x:(('hold',x,stay),('flip','B' if x=='A' else 'A',flip))
                       for x in ('A','B')})
    return LabelledMarkovSource(levels,tuple(layers))


def fork_and_merge():
    return LabelledMarkovSource(
        (('root',),('middle',),('end',)),
        ({'root':(('e', 'middle',Q(1,3)),('f','middle',Q(2,3)))},
         {'middle':(('finish','end',Q(1)),)}))


class ChronologicalSemigroupTests(unittest.TestCase):
    def test_no_truncation_affine_full_history(self):
        c=two_state_source()
        r=c.affine_braid(2,2,'A')
        self.assertEqual(r['S_then_Vp_schedule'],(2,3,6))
        self.assertEqual(r['Vp_then_Sp_schedule'],(2,4,5,6))
        self.assertEqual(r['S_then_Vp_paths'],r['Vp_then_Sp_paths'])
        self.assertEqual(sum(r['S_then_Vp_paths'].values(),Q()),Q(1))
        self.assertEqual(len(r['S_then_Vp_paths']),16)
        self.assertEqual(set(p.end_clock for p in r['S_then_Vp_paths']),{6})
        self.assertEqual(set(len(p.labels) for p in r['S_then_Vp_paths']),{4})

    def test_pathwise_full_tape_braid_all_primes_and_starts(self):
        # Every complete recorded tape represents one *realized* history.
        for p,n in ((2,1),(2,2),(3,1),(3,2),(5,1)):
            end=p*(n+1)
            states=tuple(('x',j) for j in range(1,end+1))
            labels=tuple(f'event-{j}' for j in range(1,end))
            full=SourcePath(1,states,labels)
            left=affine_backward(affine_backward(full,p,0),1,1)
            right=full
            for _ in range(p):
                right=affine_backward(right,1,1)
            right=affine_backward(right,p,0)
            self.assertEqual(left,right)
            self.assertEqual(left.end_clock,n)
            self.assertEqual(left.labels,labels[:n-1])

    def test_backward_only_on_correct_prime_image(self):
        p=SourcePath(1,tuple(range(1,8)),tuple(str(j) for j in range(1,7)))
        self.assertIsNone(affine_backward(p,2,0))
        self.assertEqual(affine_backward(p,1,1).end_clock,6)
        self.assertEqual(affine_backward(p,3,1).end_clock,2)
        self.assertIsNone(affine_backward(SourcePath(3,(10,),()),1,1))

    def test_middle_path_not_same_as_complete_ledger(self):
        c=two_state_source()
        left=(2,3,6)
        right=(2,4,5,6)
        self.assertNotEqual(left,right)
        self.assertEqual(c.route('A',left),c.route('A',right))
        self.assertTrue(any(x.states[1]!=x.states[2] for x in c.route('A',left)))

    def test_grouping_law_on_all_source_states(self):
        c=two_state_source()
        for initial in c.levels[0]:
            full=c.segment(1,6,initial)
            for split in range(2,6):
                pre=c.segment(1,split,initial)
                self.assertEqual(c.extend(pre,split,6),full)

    def test_parallel_channel_histories_survive_state_collapse(self):
        c=fork_and_merge()
        d=c.segment(1,3,'root')
        self.assertEqual(len(d),2)
        self.assertEqual(set(p.states for p in d),{('root','middle','end')})
        self.assertEqual(set(p.labels for p in d),{('e','finish'),('f','finish')})
        self.assertEqual(endpoint_marginal(d),{'end':Q(1)})
        self.assertEqual(set(d.values()),{Q(1,3),Q(2,3)})

    def test_source_labelled_reverse_step_retains_parallel_channels(self):
        c=fork_and_merge()
        r=c.backwards_events({'root':Q(1)})
        self.assertEqual({(x,label):p for x,label,p in r[0]['middle']},
                         {('root','e'):Q(1,3),('root','f'):Q(2,3)})
        for path,prob in c.segment(1,3,'root').items():
            receipt=c.pathwise_balance(path,{'root':Q(1)})
            self.assertTrue(receipt['equal'])
            self.assertEqual(receipt['forward'],prob)

    def test_source_reverse_every_realized_path(self):
        c=two_state_source()
        prior={'A':Q(1,3),'B':Q(2,3)}
        for x in c.levels[0]:
            for path,prob in c.segment(1,6,x).items():
                r=c.pathwise_balance(path,prior)
                self.assertTrue(r['equal'])
                self.assertEqual(r['forward'],prob*prior[x])

    def test_posterior_is_mixture_not_unique_reverse(self):
        c=fork_and_merge()
        post=c.posterior_paths(1,3,{'root':Q(1)},'end')
        self.assertEqual(len(post),2)
        self.assertEqual(sorted(post.values()),[Q(1,3),Q(2,3)])
        self.assertEqual(sum(post.values(),Q()),Q(1))
        with self.assertRaises(HistoryTransportError):
            c.posterior_paths(1,2,{'root':Q(1)},'end')

    def test_path_isometry_gram_exact_and_no_false_recovery(self):
        c=two_state_source()
        self.assertEqual(c.path_isometry_gram(1,6),((Q(1),Q()),(Q(),Q(1))))
        d=fork_and_merge()
        self.assertEqual(d.path_isometry_gram(1,3),((Q(1),),))
        self.assertEqual(len(d.segment(1,3,'root')),2)

    def test_unbiased_source_and_mutated_label_cannot_alias(self):
        c=fork_and_merge()
        d=c.segment(1,3,'root')
        q=list(d)
        mutated=SourcePath(q[0].start_clock,q[0].states,('mutant','finish'))
        self.assertNotIn(mutated,d)
        self.assertEqual(mutated.states,q[0].states)

    def test_path_history_lower_bound_not_endpoint_count(self):
        self.assertEqual(distinguishable_order_budget(0)['minimal_binary_bits'],0)
        self.assertEqual(distinguishable_order_budget(3)['ordered_histories'],6)
        self.assertEqual(distinguishable_order_budget(4)['minimal_binary_bits'],5)
        labels=('a','b','c','d')
        self.assertEqual(len(set(permutations(labels))),24)


class BidirectionalQuotientTests(unittest.TestCase):
    def test_backward_refines_when_forward_does_not(self):
        # Both terminal states have the SAME response observation. Their
        # distinct past source laws force the strict bicausal split.
        c=LabelledMarkovSource(
            (('x1','x2'),('y1','y2')),
            ({'x1':(('a','y1',Q(3,4)),('b','y2',Q(1,4))),
              'x2':(('c','y1',Q(1,4)),('d','y2',Q(3,4)))},))
        obs=({'x1':'left','x2':'right'},{'y1':'same','y2':'same'})
        r=bicausal_observation_quotient(c,{'x1':Q(1,2),'x2':Q(1,2)},obs)
        self.assertEqual(r['initial_partitions'][1],(0,0))
        self.assertEqual(r['partitions'][1],(0,1))
        self.assertEqual(r['source_backward'][0]['y1']['x1'],Q(3,4))
        self.assertEqual(r['source_backward'][0]['y2']['x1'],Q(1,4))
        self.assertEqual(r['strict_rounds'],1)

    def test_future_prediction_refines_indistinguishable_source(self):
        c=LabelledMarkovSource(
            (('x1','x2'),('y1','y2')),
            ({'x1':(('one','y1',Q(1)),),
              'x2':(('two','y2',Q(1)),)},))
        r=bicausal_observation_quotient(c,{'x1':Q(1,2),'x2':Q(1,2)},
                    ({'x1':'same','x2':'same'},{'y1':'C1','y2':'C2'}))
        self.assertEqual(r['partitions'][0],(0,1))
        self.assertEqual(r['partitions'][1],(0,1))

    def test_symmetric_source_quotient_stays_coarse(self):
        c=two_state_source()
        obs=tuple({x:'measurement' for x in level} for level in c.levels)
        r=bicausal_observation_quotient(c,{'A':Q(1,2),'B':Q(1,2)},obs)
        self.assertEqual(r['strict_rounds'],0)
        self.assertEqual(r['partitions'],tuple((0,0) for _ in c.levels))

    def test_initial_source_law_can_change_backward_partition(self):
        c=LabelledMarkovSource(
            (('x1','x2'),('y1','y2')),
            ({'x1':(('1','y1',Q(3,4)),('2','y2',Q(1,4))),
              'x2':(('1','y1',Q(1,4)),('2','y2',Q(3,4)))},))
        obs=({'x1':0,'x2':1},{'y1':0,'y2':0})
        for p in (Q(1,2),Q(1,3),Q(9,10)):
            r=bicausal_observation_quotient(c,{'x1':p,'x2':1-p},obs)
            self.assertNotEqual(r['source_backward'][0]['y1']['x1'],
                                r['source_backward'][0]['y2']['x1'])
            self.assertEqual(r['partitions'][1],(0,1))

    def test_observer_compression_is_not_history_faithful(self):
        c=fork_and_merge()
        obs=({'root':'root'},{'middle':'middle'},{'end':'end'})
        r=bicausal_observation_quotient(c,{'root':Q(1)},obs)
        self.assertEqual(r['strict_rounds'],0)
        self.assertEqual(len(c.segment(1,3,'root')),2)
        self.assertEqual(len(endpoint_marginal(c.segment(1,3,'root'))),1)

    def test_adversarial_unsupported_source_rejected(self):
        c=LabelledMarkovSource(
            (('a','b'),('z',)),({'a':(('a','z',Q(1)),),
                               'b':(('b','z',Q(1)),)},))
        with self.assertRaises(HistoryTransportError):
            bicausal_observation_quotient(c,{'a':Q(1),'b':Q()},
                                        ({'a':0,'b':0},{'z':0}))


class RealDtNIntegrationTests(unittest.TestCase):
    def diamond(self):
        from observational_succ.growing_dtn_history import ConductiveState
        return ConductiveState(('L','R','u','v'),('L','R'),(
            ('L','u',Q(1)),('u','R',Q(1)),
            ('L','v',Q(1)),('v','R',Q(1))))

    def test_hidden_material_edge_forces_future_safe_split(self):
        bare=self.diamond()
        hidden=bare.with_edge('u','v',Q(7))
        self.assertEqual(bare.response(),hidden.response())
        x=bare.with_edge('L','u',1)
        y=hidden.with_edge('L','u',1)
        c=LabelledMarkovSource(((bare,hidden),(x,y)),
            ({bare:(('probe_L_u',x,Q(1)),),
              hidden:(('probe_L_u',y,Q(1)),)},))
        r=bicausal_observation_quotient(c,
            {bare:Q(1,2),hidden:Q(1,2)},
            ({bare:bare.response(),hidden:hidden.response()},
             {x:x.response(),y:y.response()}))
        self.assertEqual(r['initial_partitions'][0],(0,0))
        self.assertEqual(r['partitions'][0],(0,1))
        self.assertEqual(x.energy((0,1)),Q(7,6))
        self.assertEqual(y.energy((0,1)),Q(49,41))

    def test_field_guided_material_probabilities_are_not_exchangeable(self):
        c=lift_field_growth_source(self.diamond(),
                    {'a':('L','u',Q(1)),'b':('u','v',Q(1))},2,Q(1,3))
        paths=c.segment(1,3,frozenset())
        self.assertEqual(len(paths),2)
        weights={path.labels:mass for path,mass in paths.items()}
        self.assertEqual(weights[('a','b')],Q(7,11))
        self.assertEqual(weights[('b','a')],Q(4,11))
        self.assertNotEqual(weights[('a','b')],weights[('b','a')])
        self.assertEqual(len(endpoint_marginal(paths)),1)
        self.assertEqual(c.posterior_paths(1,3,{frozenset():Q(1)},
                                          frozenset({'a','b'})),paths)
        for path,mass in paths.items():
            self.assertEqual(c.pathwise_balance(path,{frozenset():Q(1)})['forward'],mass)

    def test_physical_five_edge_affine_braid_keeps_all_24_paths(self):
        base=self.diamond()
        candidates={'a':('L','u',Q(1)),'b':('u','v',Q(1)),
                    'c':('L','R',Q(1,2)),
                    'd':('R','v',Q(1,3)),'e':('L','v',Q(2,3))}
        c=lift_field_growth_source(base,candidates,5,Q(1,3))
        result=c.affine_braid(2,2,frozenset({'a'}))
        left=result['S_then_Vp_paths']
        right=result['Vp_then_Sp_paths']
        self.assertEqual(left,right)
        self.assertEqual(len(left),24) # four remaining labels: 4! orders
        self.assertEqual(sum(left.values(),Q()),Q(1))
        self.assertEqual(len(endpoint_marginal(left)),1)
        self.assertEqual({len(set(path.labels)) for path in left},{4})

class InputFirewallTests(unittest.TestCase):
    def test_duplicate_channel_and_wrong_norm_rejected(self):
        with self.assertRaises(HistoryTransportError):
            LabelledMarkovSource((('x',),('y',)),
                ({'x':(('e','y',Q(1,2)),('e','y',Q(1,2)))},))
        with self.assertRaises(HistoryTransportError):
            LabelledMarkovSource((('x',),('y',)),
                ({'x':(('e','y',Q(1,3)),)},))
        with self.assertRaises(HistoryTransportError):
            LabelledMarkovSource((('x',),('y',)),
                ({'x':(('e','y',0.5),)},))

    def test_malformed_clock_and_fake_composites(self):
        c=two_state_source()
        with self.assertRaises(HistoryTransportError):c.affine_braid(2,4,'A')
        with self.assertRaises(HistoryTransportError):c.affine_braid(2,3,'A')
        with self.assertRaises(HistoryTransportError):c.affine_braid(True,2,'A')
        with self.assertRaises(HistoryTransportError):c.route('A',(2,2,6))

    def test_invalid_source_event_or_probability_rejected(self):
        with self.assertRaises(HistoryTransportError):
            SourcePath(1,('x','y'),())
        with self.assertRaises(HistoryTransportError):
            SourcePath(1,('x','y'),('',))
        with self.assertRaises(HistoryTransportError):
            LabelledMarkovSource((('x',),('y',)),
                                 ({'x':(('e','other',Q(1)),)},))
        with self.assertRaises(HistoryTransportError):
            LabelledMarkovSource((('x',),('y',)),
                                 ({'x':(('e','y',Q(-1)),)},))

    def test_invalid_prior_and_path_extension_rejected(self):
        c=two_state_source()
        with self.assertRaises(HistoryTransportError):c.marginals({'A':Q(1)})
        with self.assertRaises(HistoryTransportError):c.marginals({'A':Q(2),'B':Q(-1)})
        with self.assertRaises(HistoryTransportError):
            c.extend({SourcePath(1,('A',),()):Q(1)},2,3)
        with self.assertRaises(HistoryTransportError):
            c.segment(6,7,'A')
        with self.assertRaises(HistoryTransportError):
            bicausal_observation_quotient(c,{'A':Q(1,2),'B':Q(1,2)},
                                          ({'A':0},)*6)

if __name__=='__main__':unittest.main()
