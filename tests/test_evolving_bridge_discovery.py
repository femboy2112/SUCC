from dataclasses import replace
from math import factorial
from random import Random
import unittest
from observational_succ.relational_model_genetics import Capsule, Port, PairedSourceTable, GeneticsError, project
from observational_succ.evolutionary_bridge_search import ternary_fusion_demo
from observational_succ.evolving_bridge_search import evolve_with_obstructions
from observational_succ.evolving_observer_categories import (
    Action,Readout,FiniteDynamics,PartialTransitionTable,SynthesisError,
)
from observational_succ.obstruction_discovery_lab import discovery_case, hidden_carrier, mine_generic_laws
from observational_succ.evolving_observer_categories import discover_representation


def fusion_source(n,seed=2718,*,partial=None):
    rng=Random(seed);vals=list(range(n));rng.shuffle(vals)
    numeric=tuple(map(str,range(n)));labels=tuple('label'+str(i) for i in vals)
    left=Capsule('clock','clock','fusion',0,'v',
        (Port('x',numeric),Port('y',numeric)),tuple((str(i),str((i+1)%n)) for i in range(n)))
    right=Capsule('thermal','thermal','fusion',0,'v',
        (Port('t',labels),Port('z',numeric)),tuple((labels[i],str((i-1)%n)) for i in range(n)))
    events=tuple(('s'+str(i),str(i),labels[i]) for i in range(n))
    table=PairedSourceTable('fusion',0,'v',Port('y',numeric),Port('t',labels),
        events if partial is None else events[:partial],partial is None)
    return left,right,table


class EvolvingBridgeDiscoveryTests(unittest.TestCase):
    def test_previous_genetic_failures_are_real_regression_cases(self):
        failed=[i for i in range(20) if not ternary_fusion_demo(i)['genetic_succeeded']]
        self.assertEqual(failed,[0,11,13])

    def test_counterexample_evolution_removes_old_local_optima(self):
        a,b,s=fusion_source(3)
        for seed in range(20):
            r=evolve_with_obstructions(a,b,s,seed=seed)
            self.assertTrue(r.complete_declared_source)
            self.assertLessEqual(len(r.proposals),3)
            self.assertFalse(r.full_permutation_enumeration_used)
            self.assertEqual(project(r.child,('x','z')),(('0','0'),('1','1'),('2','2')))

    def test_larger_alignment_without_factorial_oracle(self):
        for n in (4,5,7):
            a,b,s=fusion_source(n)
            for seed in range(20):
                r=evolve_with_obstructions(a,b,s,seed=seed)
                self.assertLessEqual(len(r.proposals),n)
                self.assertEqual(len(r.exclusions),len({x.left_value for x in r.exclusions}))
                self.assertEqual(r.remaining_bijections,1)
                self.assertEqual(project(r.child,('x','z')),tuple((str(i),str(i)) for i in range(n)))

    def test_every_later_child_preserves_each_exclusion(self):
        a,b,s=fusion_source(7);r=evolve_with_obstructions(a,b,s,seed=99)
        for i,w in enumerate(r.exclusions):
            k=s.left_port.domain.index(w.left_value)
            self.assertTrue(all(p[k]==w.required_right for p in r.proposals[i+1:]))

    def test_partial_source_does_not_become_complete_by_genetic_confidence(self):
        a,b,s=fusion_source(5,partial=2)
        r=evolve_with_obstructions(a,b,s)
        self.assertFalse(r.complete_declared_source)
        self.assertEqual(r.remaining_bijections,6)
        self.assertFalse(r.bridge.complete_source_class)

    def test_forged_complete_table_rejected(self):
        a,b,s=fusion_source(5,partial=2)
        with self.assertRaisesRegex(GeneticsError,'Completeness'):
            evolve_with_obstructions(a,b,replace(s,complete_source_class=True))

    def test_false_joint_source_or_changed_basis_rejected(self):
        a,b,s=fusion_source(3)
        with self.assertRaises(GeneticsError):evolve_with_obstructions(replace(a,epoch=1),b,s)
        with self.assertRaises(GeneticsError):evolve_with_obstructions(a,replace(b,basis='changed'),s)

    def test_partial_table_keeps_unobserved_entries_open(self):
        p=PartialTransitionTable('x',0,'v',2,('a',),(Readout('r',(0,1)),),(('a',0,0),))
        identity=FiniteDynamics('x',0,'v',(Action('a',(0,1)),),p.readouts)
        erase=FiniteDynamics('x',0,'v',(Action('a',(0,0)),),p.readouts)
        self.assertTrue(p.compatible(identity));self.assertTrue(p.compatible(erase))
        self.assertEqual(p.remaining_completions(),2)
        self.assertEqual(p.next_unobserved_query(),('a',1))
        with self.assertRaisesRegex(SynthesisError,'PARTIAL_SOURCE'):p.completion()

    def test_new_observation_discriminates_previous_candidates(self):
        p=PartialTransitionTable('x',0,'v',2,('a',),(Readout('r',(0,1)),),(('a',0,0),('a',1,1)))
        self.assertEqual(p.remaining_completions(),1)
        s=p.completion();self.assertEqual(s.actions[0].after,(0,1))
        self.assertFalse(p.compatible(replace(s,actions=(Action('a',(0,0)),))))

    def test_partial_contradictory_receipt_not_ignored(self):
        with self.assertRaises(SynthesisError):
            PartialTransitionTable('x',0,'v',2,('a',),(Readout('r',(0,1)),),(('a',0,0),('a',0,1)))

    def test_calibration_unknown_invariant(self):
        r=discovery_case(3,271828)
        self.assertEqual((r['source_states'],r['discovered_states']), (27,9))
        self.assertEqual(r['fiber_sizes'],[3])
        self.assertTrue(r['generic_discovered_laws']['central_commutator'])
        self.assertFalse(r['generic_discovered_laws']['commutator_is_identity'])
        self.assertEqual(r['generic_discovered_laws']['size'],27)
        self.assertEqual(r['generic_discovered_laws']['orders'],[3,3,3])

    def test_precommitted_holdout_p5(self):
        r=discovery_case(5,314159)
        self.assertEqual((r['source_states'],r['discovered_states']),(125,25))
        self.assertEqual(r['generic_discovered_laws']['size'],125)
        self.assertEqual(r['generic_discovered_laws']['orders'],[5,5,5])
        self.assertEqual(r['fresh_word_checks'],36)
        self.assertTrue(r['generic_discovered_laws']['normal_form_unique'])

    def test_precommitted_holdout_p7(self):
        r=discovery_case(7,161803)
        self.assertEqual((r['source_states'],r['discovered_states']),(343,49))
        self.assertEqual(r['generic_discovered_laws']['size'],343)
        self.assertEqual(r['generic_discovered_laws']['center_size'],7)
        self.assertEqual(r['generic_discovered_laws']['orders'],[7,7,7])
        self.assertTrue(r['changed_toolkit_rejected'])
        self.assertEqual(r['expanded_toolkit_states'],343)

    def test_bare_noncommuting_actions_do_not_make_false_group(self):
        s=FiniteDynamics('erase',0,'v',(Action('erase',(0,0)),),(Readout('r',(0,1)),))
        self.assertFalse(mine_generic_laws(discover_representation(s))['group'])

if __name__=='__main__':unittest.main()
