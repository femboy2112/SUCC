from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
from random import Random
import unittest
from observational_succ.source_aware_amalgamation import (
    Context, Marginal, CouplingError, markov_amalgamate, separator_bayes_square,
    credal_target_interval, StochasticAction, Hypothesis, CausalReceipt,
    EvolvingEvidence, FreshEvidenceContract, bridge_population,
)
from observational_succ.relational_model_genetics import Capsule, Port, pullback

CTX=Context('joint-source',0,'same-units')

def parents():
    rows=tuple(product((0,1),repeat=2))
    return (Marginal(CTX,('a','y'),rows,(Q(3,8),Q(1,8),Q(1,8),Q(3,8))),
            Marginal(CTX,('y','b'),rows,(Q(1,4),)*4))


def source_models(noise=False):
    identity=((Q(1),Q(0)),(Q(0),Q(1)))
    emit=((Q(3,4),Q(1,4)),(Q(1,4),Q(3,4))) if noise else identity
    sense=StochasticAction('sense',('0','1'),identity,emit)
    erase=StochasticAction('erase',('0','1'),((Q(1),Q(0)),)*2,identity)
    flip=StochasticAction('flip',('0','1'),((Q(0),Q(1)),(Q(1),Q(0))),identity)
    return (Hypothesis('m', (Q(1,2),Q(1,2)),(sense,erase,flip),('0','1')),)


def event(n,act='sense',out='0'):
    return CausalReceipt('event'+str(n),n,CTX,act,out)


class EvolvingAmalgamationTests(unittest.TestCase):
    def test_categorical_joint_preserves_both_marginals(self):
        a,b=parents();m=markov_amalgamate(a,b,assume_conditional_independence=True)
        self.assertEqual(m.project(a.variables),a.project(a.variables))
        self.assertEqual(m.project(b.variables),b.project(b.variables))
        self.assertEqual(sum(m.weights),1)

    def test_parent_pullback_support_agrees_with_probability_glue(self):
        a,b=parents();ports=lambda vs:tuple(Port(v,('0','1')) for v in vs)
        capsule=lambda name,m:Capsule(name,'typed',CTX.source,CTX.version,CTX.basis,ports(m.variables),
            tuple(tuple(map(str,r)) for r,p in zip(m.rows,m.weights) if p))
        rel=pullback(capsule('a',a),capsule('b',b)).merged
        m=markov_amalgamate(a,b,assume_conditional_independence=True)
        self.assertEqual(set(rel.rows),{tuple(map(str,r)) for r,p in zip(m.rows,m.weights) if p})

    def test_no_free_independence(self):
        with self.assertRaisesRegex(CouplingError,'Marginals'):markov_amalgamate(*parents())

    def test_inconsistent_overlap_and_source_are_rejected(self):
        a,b=parents()
        wrong=replace(b,weights=(Q(1,2),Q(0),Q(1,2),Q(0)))
        # y margins still 1/2; choose an actual mismatch instead.
        wrong=replace(b,weights=(Q(3,4),Q(0),Q(1,4),Q(0)))
        with self.assertRaisesRegex(CouplingError,'marginal'):markov_amalgamate(a,wrong,assume_conditional_independence=True)
        with self.assertRaisesRegex(CouplingError,'source'):markov_amalgamate(a,replace(b,context=Context('other',0,'same-units')),assume_conditional_independence=True)

    def test_separator_evidence_counted_once(self):
        a,b=parents();r=separator_bayes_square(a,b,{(0,):Q(1,4),(1,):Q(3,4)})
        self.assertEqual(r['posterior'].project(('y',)),{(0,):Q(1,4),(1,):Q(3,4)})
        # Dividing by the OLD separator after both updates gives likelihood^2.
        a2=a.condition({(0,):Q(1,4),(1,):Q(3,4)},('y',));b2=b.condition({(0,):Q(1,4),(1,):Q(3,4)},('y',))
        old=a.project(('y',));aa=a2.project(('y',));bb=b2.project(('y',))
        fake={y:aa[y]*bb[y]/old[y] for y in old};z=sum(fake.values())
        self.assertEqual(fake[(1,)]/z,Q(9,10))

    def test_gluing_associative_on_declared_markov_chain(self):
        a,b=parents();c=Marginal(CTX,('b','c'),tuple(product((0,1),repeat=2)),(Q(1,4),)*4)
        l=markov_amalgamate(markov_amalgamate(a,b,assume_conditional_independence=True),c,assume_conditional_independence=True)
        r=markov_amalgamate(a,markov_amalgamate(b,c,assume_conditional_independence=True),assume_conditional_independence=True)
        self.assertEqual(l.project(l.variables),r.project(l.variables))

    def test_zero_separator_mass_safe(self):
        a=Marginal(CTX,('a','y'),((0,0),(1,1)),(Q(1),Q(0)))
        b=Marginal(CTX,('y','b'),((0,0),(1,1)),(Q(1),Q(0)))
        self.assertEqual(markov_amalgamate(a,b,assume_conditional_independence=True).weights,(Q(1),))

    def test_credal_ambiguity_is_retained(self):
        rows=tuple(product((0,1),repeat=2))
        positive=Marginal(CTX,('a','b'),rows,(Q(1,2),Q(0),Q(0),Q(1,2)))
        negative=Marginal(CTX,('a','b'),rows,(Q(0),Q(1,2),Q(1,2),Q(0)))
        self.assertEqual(positive.project(('a',)),negative.project(('a',)))
        self.assertEqual(credal_target_interval((positive,negative),lambda r:r['a']==r['b']),(0,1))

    def test_random_source_marginal_gluing(self):
        rng=Random(74741)
        for _ in range(150):
            sy=[rng.randrange(1,8) for _ in range(3)];zy=sum(sy)
            pa=[];pb=[]
            for y in range(3):
                ra=[rng.randrange(1,8) for _ in range(2)];rb=[rng.randrange(1,8) for _ in range(2)]
                pa.extend(Q(sy[y],zy)*Q(v,sum(ra)) for v in ra)
                pb.extend(Q(sy[y],zy)*Q(v,sum(rb)) for v in rb)
            a=Marginal(CTX,('y','a'),tuple(product(range(3),range(2))),tuple(pa))
            b=Marginal(CTX,('y','b'),tuple(product(range(3),range(2))),tuple(pb))
            m=markov_amalgamate(a,b,assume_conditional_independence=True)
            self.assertEqual(m.project(a.variables),a.project(a.variables))
            separator_bayes_square(a,b,{(y,):Q(y+1,4) for y in range(3)})

    def test_delayed_noncommuting_receipts_use_causal_not_arrival_order(self):
        e=EvolvingEvidence(CTX,source_models(),(Q(1),))
        later=event(1,'flip','1');early=event(0,'erase','0')
        r=e.receive(later);self.assertEqual(r['applied'],0);self.assertEqual(r['buffered'],1)
        r=e.receive(early);self.assertEqual(r['applied'],2)
        self.assertEqual(r['original_target'],{'0':Q(1,2),'1':Q(1,2)})
        self.assertEqual({current for _,_,current in e.joint},{1})

    def test_destructive_current_measurement_does_not_rewrite_original_truth(self):
        e=EvolvingEvidence(CTX,source_models(),(Q(1),))
        e.receive(event(0,'erase','0'));r=e.receive(event(1,'sense','0'))
        self.assertEqual(r['original_target'],{'0':Q(1,2),'1':Q(1,2)})
        self.assertIn('NOT_A_FORMAL',r['status'])

    def test_repeated_event_is_not_new_evidence(self):
        e=EvolvingEvidence(CTX,source_models(noise=True),(Q(1),))
        a=event(0);r=e.receive(a);before=dict(e.joint)
        self.assertEqual(e.receive(a),r);self.assertEqual(e.joint,before)
        self.assertEqual(len(e.applied),1)

    def test_distinct_noisy_events_condition_on_one_shared_state(self):
        e=EvolvingEvidence(CTX,source_models(noise=True),(Q(1),))
        e.receive(event(0));r=e.receive(event(1))
        self.assertEqual(r['original_target']['0'],Q(9,10))
        self.assertEqual(e.predictive_probabilities,[Q(1,2),Q(5,8)])

    def test_repeat_exact_latent_read_has_unit_predictive_likelihood(self):
        e=EvolvingEvidence(CTX,source_models(),(Q(1),))
        e.receive(event(0));e.receive(event(1))
        self.assertEqual(e.predictive_probabilities,[Q(1,2),Q(1)])

    def test_conflicting_or_stale_receipts_rejected(self):
        e=EvolvingEvidence(CTX,source_models(),(Q(1),));a=event(0);e.receive(a)
        with self.assertRaises(CouplingError):e.receive(replace(a,outcome='1'))
        with self.assertRaises(CouplingError):e.receive(replace(a,event_id='new'))
        with self.assertRaises(CouplingError):e.receive(replace(event(1),context=Context('joint-source',1,'same-units')))

    def test_impossible_evidence_is_transactional_model_misspecification(self):
        e=EvolvingEvidence(CTX,source_models(),(Q(1),));e.receive(event(0,'erase','0'))
        before=dict(e.joint)
        with self.assertRaisesRegex(CouplingError,'MISSPECIFIED'):e.receive(event(1,'sense','1'))
        self.assertEqual(e.joint,before);self.assertEqual(len(e.applied),1)

    def test_fitting_data_is_not_heldout_evidence(self):
        gate=FreshEvidenceContract('new-model',CTX,frozenset({'event0'}))
        self.assertTrue(gate.validate_test((event(1),)))
        with self.assertRaisesRegex(CouplingError,'leakage'):gate.validate_test((event(0),))

    def test_probabilistic_evolutionary_bridge_adapter(self):
        dom=('0','1','2'); cod=('cold','warm','hot')
        maps=(cod,('warm','hot','cold'),('hot','cold','warm'))
        engine=bridge_population(CTX,dom,cod,maps,(Q(1,3),)*3,error_rate=Q(1,5))
        record=CausalReceipt('fresh',0,CTX,'query:0','cold')
        result=engine.receive(record)
        self.assertEqual(result['model_posterior'],{'bridge:0':Q(4,5),'bridge:1':Q(1,10),'bridge:2':Q(1,10)})
        self.assertFalse(result['model_class_exhaustive'])
        self.assertIn('NOT_A_FORMAL',result['status'])

    def test_noisy_bridge_never_becomes_exact_by_repeated_likelihood(self):
        dom=('0','1');cod=('cold','warm')
        engine=bridge_population(CTX,dom,cod,(cod,tuple(reversed(cod))),(Q(1,2),)*2,error_rate=Q(1,4))
        for i in range(5):engine.receive(CausalReceipt('e'+str(i),i,CTX,'query:0','cold'))
        posterior=engine.summary()['model_posterior']
        self.assertEqual(posterior['bridge:0'],Q(243,244))
        self.assertGreater(posterior['bridge:1'],0)

    def test_stochastic_marginal_fusion_can_reveal_hidden_correlation(self):
        rows=tuple(product((0,1),repeat=2))
        a=Marginal(CTX,('x','y'),rows,(Q(1,2),Q(0),Q(0),Q(1,2)))
        b=Marginal(CTX,('x','y'),rows,(Q(0),Q(1,2),Q(1,2),Q(0)))
        for variable in ('x','y'):self.assertEqual(a.project((variable,)),b.project((variable,)))
        self.assertNotEqual(a.project(('x','y')),b.project(('x','y')))

    def test_invalid_probability_tables_fail(self):
        with self.assertRaises(CouplingError):Marginal(CTX,('x',),((0,),(1,)),(0.5,0.5))
        with self.assertRaises(CouplingError):StochasticAction('a',('0','1'),((Q(1),Q(1)),)*2,((Q(1),Q(0)),)*2)

if __name__=='__main__':unittest.main()
