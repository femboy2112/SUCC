"""Exact finite mini-carrier proofs, ghost controls, and source-closure tests."""
import unittest
from itertools import permutations
from observational_succ.miniature_carrier import (
    Carrier, Mini, MiniatureContractError, compile_factor, compile_subcarrier,
    compile_dual_product, future_partition, dark_target_witness,
)


def clock4(read='parity', actions=('inc',), preparations=('0',)):
    states = tuple(str(j) for j in range(4))
    mapping = {'inc': {str(j): str((j+1) % 4) for j in range(4)},
               'jump2': {str(j): str((j+2) % 4) for j in range(4)}}
    reports = {s: str(int(s)%2 if read == 'parity' else int(s)//2) for s in states}
    return Carrier(states, {a: mapping[a] for a in actions}, reports, preparations, 'physical-clock-v1')


def bitflip(source='physical-clock-v1'):
    return Mini(('0','1'), {'flip': {'0':'1','1':'0'}},
                {'0':'0','1':'1'}, '0', source)


def paired_system(correlated=False, leaky=False):
    states = ('00', '11') if correlated else ('00','01','10','11')
    actions = {
        'L': {c: ('1' if c[0]=='0' else '0') +
             (('1' if c[1]=='0' else '0') if leaky or correlated else c[1])
             for c in states},
        'R': {c: c[0]+('1' if c[1]=='0' else '0') for c in states},
    }
    if correlated:
        # Only simultaneous flips are lawful; both single-factors survive.
        actions['R'] = actions['L'].copy()
    return Carrier(states, actions, {c:c for c in states}, ('00',), 'joint')


def bit(source='joint'):
    return Mini(('0','1'), {'flip':{'0':'1','1':'0'}},
                {'0':'0','1':'1'}, '0', source)


def hidden_source_carrier(with_copy=False):
    states=tuple(f's{s}m{m}' for s in '01' for m in '01')
    acts={
        'flip': {c: c[:3]+('1' if c[-1]=='0' else '0') for c in states},
        'reset':{c:c[:3]+'0' for c in states},
    }
    if with_copy:
        acts['copy_source_to_memory']={c:c[:3]+c[1] for c in states}
    return Carrier(states, acts, {c:c[-1] for c in states},
                   ('s0m0','s1m0'), 'hidden-bit-v1')


class MiniatureCarrierTests(unittest.TestCase):
    def test_lawful_virtual_quotient_without_action_section(self):
        p=clock4()
        m=bitflip()
        dec={str(j):str(j%2) for j in range(4)}
        r=compile_factor(p,m,dec,{'flip':('inc',)})
        self.assertTrue(r['certified'])
        self.assertEqual(r['realization'], 'lawful_behavioral_factor')
        self.assertFalse(r['new_physical_instrument_created'])
        self.assertEqual(r['common_source_squares_checked'],4)
        r2=compile_subcarrier(p,m,{'0':'0','1':'1'}, {'flip':('inc',)})
        self.assertFalse(r2['certified'])
        self.assertEqual(r2['reason'],'noncommuting_carrier_square')

    def test_every_possible_clock_section_is_impossible(self):
        p=clock4(preparations=('0','1','2','3'))
        m=bitflip()
        reasons=set()
        for e0,e1 in permutations(p.states,2):
            c=compile_subcarrier(p,m,{'0':e0,'1':e1},{'flip':('inc',)})
            self.assertFalse(c['certified'])
            reasons.add(c['reason'])
        self.assertTrue(reasons <= {'wrong_source_report','noncommuting_carrier_square'})
        self.assertIn('noncommuting_carrier_square',reasons)

    def test_literal_two_state_invariant_subcarrier_with_macro(self):
        p=clock4(read='high',actions=('inc','jump2'))
        m=bitflip()
        r=compile_subcarrier(p,m,{'0':'0','1':'2'},{'flip':('inc','inc')},budget=2)
        self.assertTrue(r['certified'])
        self.assertTrue(r['strict_inside'])
        self.assertEqual(r['maximum_macro_cost'],2)
        self.assertFalse(r['literal_inclusion'])
        self.assertFalse(compile_subcarrier(p,m,{'0':'0','1':'2'},
                                            {'flip':('inc',)})['certified'])
        with self.assertRaises(MiniatureContractError):
            compile_subcarrier(p,m,{'0':'0','1':'2'},
                               {'flip':('inc','inc')},budget=1)

    def test_missing_preparation_is_not_a_ghost_state(self):
        p=clock4(read='high',actions=('jump2',),preparations=('1',))
        m=bitflip()
        c=compile_subcarrier(p,m,{'0':'0','1':'2'}, {'flip':('jump2',)})
        self.assertEqual(c['reason'],'unavailable_initial_preparation')

    def test_unsafe_actions_cannot_be_compiled(self):
        p=Carrier(('0','1'), {'one_use':{'0':'1','1':None}},
                  {'0':'0','1':'1'}, ('0',), 'fail')
        m=bitflip('fail')
        c=compile_subcarrier(p,m,{'0':'0','1':'1'}, {'flip':('one_use',)})
        self.assertEqual(c['reason'],'unsafe_or_unperformed_primitive')
        self.assertEqual(c['witness']['mini_state'],'1')

    def test_two_individually_valid_minis_cannot_fake_unrealizable_joint_source(self):
        p=paired_system(correlated=True)
        m=bit()
        la={c:c[0] for c in p.states}
        ra={c:c[1] for c in p.states}
        self.assertTrue(compile_factor(p,m,la,{'flip':('L',)}, public_map={'00':'0','11':'1'})['certified'])
        self.assertTrue(compile_factor(p,m,ra,{'flip':('R',)}, public_map={'00':'0','11':'1'})['certified'])
        d=compile_dual_product(p,m,m,la,ra,('L',),('R',),
                               {c:(c[0],c[1]) for c in p.reports.values()})
        self.assertFalse(d['certified'])
        self.assertEqual(d['reason'],'ghost_joint_states')
        self.assertEqual(d['witness']['missing_pairs'],[('0','1'),('1','0')])

    def test_product_really_lives_in_parent_and_actions_do_not_interfere(self):
        p=paired_system()
        m=bit()
        la={c:c[0] for c in p.states}
        ra={c:c[1] for c in p.states}
        d=compile_dual_product(p,m,m,la,ra,('L',),('R',),
                               {c:(c[0],c[1]) for c in p.reports.values()})
        self.assertTrue(d['certified'])
        self.assertEqual(d['product_states'],4)
        self.assertTrue(d['observable_actions_commute'])
        self.assertFalse(d['physical_actions_proved_commuting'])

    def test_cross_channel_interference_forces_refusal(self):
        p=paired_system(leaky=True)
        m=bit()
        la={c:c[0] for c in p.states}
        ra={c:c[1] for c in p.states}
        d=compile_dual_product(p,m,m,la,ra,('L',),('R',),
                               {c:(c[0],c[1]) for c in p.reports.values()})
        self.assertFalse(d['certified'])
        self.assertEqual(d['reason'],'cross_observer_interference')

    def test_forged_public_observation_fails(self):
        p=paired_system()
        m=bit()
        la={c:c[0] for c in p.states}
        ra={c:c[1] for c in p.states}
        report={c:(c[0],c[1]) for c in p.reports.values()}
        report['01']=('0','0')
        self.assertEqual(compile_dual_product(p,m,m,la,ra,('L',),('R',),report)['reason'],
                         'unjustified_joint_observation')

    def test_bureaucracy_can_minimize_complete_declared_carrier(self):
        p=clock4()
        r=future_partition(p)
        self.assertEqual(r['final_model_states'],2)
        self.assertEqual(r['stages'],[2,2])
        self.assertTrue(r['verified'])
        self.assertTrue(compile_factor(p,r['mini'],r['decoder'],{'inc':('inc',)})['certified'])
        p2=clock4(read='high')
        r2=future_partition(p2)
        self.assertEqual(r2['final_model_states'],4)
        self.assertEqual(r2['stages'][0],2)
        self.assertEqual(r2['stages'][-1],4)

    def test_original_hidden_source_cannot_be_measured_by_model_alone(self):
        p=hidden_source_carrier()
        target={c:c[1] for c in p.states}
        r=dark_target_witness(p,target)
        self.assertFalse(r['certified'])
        self.assertEqual(r['reason'],'target_not_in_parent_observation_closure')
        s,t=r['witness']['source_pair']
        self.assertNotEqual(target[s],target[t])
        self.assertEqual(p.reports[s],p.reports[t])

    def test_authentic_new_source_coupling_changes_tool_closure(self):
        p=hidden_source_carrier(with_copy=True)
        target={c:c[1] for c in p.states}
        r=dark_target_witness(p,target)
        self.assertTrue(r['certified'])
        self.assertTrue(r['existing_actions_sufficient_in_ideal_closure'])
        # The newly declared action is a premise, not inferred physical apparatus.
        self.assertFalse(r['source_authenticated_externally'])

    def test_source_version_and_incomplete_tables_are_refused(self):
        p=clock4()
        m=bitflip('other-source')
        with self.assertRaises(MiniatureContractError):
            compile_factor(p,m,{str(j):str(j%2) for j in range(4)},{'flip':('inc',)})
        with self.assertRaises(MiniatureContractError):
            Carrier(('0','1'), {'bad': {'0':'1'}}, {'0':'0','1':'1'}, ('0',),'x')
        with self.assertRaises(MiniatureContractError):
            compile_factor(p,bitflip(),{str(j):str(j%2) for j in range(4)},
                           {'flip':('not-a-physical-tool',)})


if __name__ == '__main__':
    unittest.main()


class NestedMiniatureTests(unittest.TestCase):
    def test_nested_compilation_and_exact_source_cost(self):
        from observational_succ.miniature_carrier import compile_nested_factor
        states=tuple(str(i) for i in range(8))
        parent=Carrier(states, {'tick':{str(i):str((i+1)%8) for i in range(8)}},
                       {str(i):str((i//2)%2) for i in range(8)},
                       ('0',),'nest')
        mid=Mini(tuple(str(i) for i in range(4)),
                 {'step':{str(i):str((i+1)%4) for i in range(4)}},
                 {str(i):str(i%2) for i in range(4)}, '0','nest')
        child=Mini(('0','1'),{'flip':{'0':'1','1':'0'}},
                   {'0':'0','1':'1'},'0','nest')
        one={str(i):str(i//2) for i in range(8)}
        two={str(i):str(i%2) for i in range(4)}
        proof=compile_nested_factor(parent,mid,child,one,two,
                           {'step':('tick','tick')},
                           {'flip':('step','step','step')},budget=6)
        self.assertTrue(proof['certified'])
        self.assertEqual(proof['effective_parent_step_cost'],6)
        self.assertEqual(proof['effective_parent_action_words']['flip'],['tick']*6)
        self.assertTrue(proof['all_three_carrier_squares_verified'])
        self.assertFalse(proof['no_physical_speedup_implied'] is False)
        self.assertEqual(len(proof['expanded_parent_history']),8)

    def test_nested_bureaucracy_refuses_insufficient_budget(self):
        from observational_succ.miniature_carrier import compile_nested_factor
        states=tuple(str(i) for i in range(8))
        parent=Carrier(states, {'tick':{str(i):str((i+1)%8) for i in range(8)}},
                       {str(i):str((i//2)%2) for i in range(8)},('0',),'nest')
        mid=Mini(tuple(str(i) for i in range(4)),
                 {'step':{str(i):str((i+1)%4) for i in range(4)}},
                 {str(i):str(i%2) for i in range(4)}, '0','nest')
        child=Mini(('0','1'),{'flip':{'0':'1','1':'0'}},
                   {'0':'0','1':'1'},'0','nest')
        proof=compile_nested_factor(parent,mid,child,
                 {str(i):str(i//2) for i in range(8)},
                 {str(i):str(i%2) for i in range(4)},
                 {'step':('tick','tick')}, {'flip':('step','step','step')}, budget=5)
        self.assertFalse(proof['certified'])
        self.assertIn(proof['reason'], ('uncertified_intermediate_to_child',
                                         'composite_exceeds_parent_resource_budget'))


class IndependentMiniOracleTests(unittest.TestCase):
    def test_all_future_equivalence_against_pair_bfs_random_holdout(self):
        # Different algorithm from partition-refinement: BFS in the product
        # graph of ordered source-state pairs; exhaustive and source-complete.
        import random
        rng=random.Random(20131013)
        for n in (2,3,4,5):
            st=tuple(str(i) for i in range(n))
            for _ in range(90):
                acts={a:{c:rng.choice(st) for c in st} for a in ('A','B')}
                outputs={c:str(rng.randint(0,2)) for c in st}
                p=Carrier(st,acts,outputs,st,'random-finite')
                r=future_partition(p)
                self.assertTrue(r['verified'])
                self.assertTrue(r['carrier_realization_certified'])
                for i,c in enumerate(st):
                    for d in st[i+1:]:
                        queue=[(c,d)]
                        visited=set()
                        distinguished=False
                        for x,y in queue:
                            if (x,y) in visited:
                                continue
                            visited.add((x,y))
                            if outputs[x]!=outputs[y]:
                                distinguished=True
                                break
                            for act in acts:
                                pair=(acts[act][x],acts[act][y])
                                if pair not in visited:
                                    queue.append(pair)
                        self.assertEqual(r['decoder'][c]!=r['decoder'][d],
                                         distinguished)

    def test_abstract_minimum_exists_but_physical_state_unreachable(self):
        p=Carrier(('a','b'),{'idle':{'a':'a','b':'b'}},
                  {'a':'0','b':'1'},('a',),'one-preparation')
        r=future_partition(p)
        self.assertTrue(r['verified'])
        self.assertEqual(r['final_model_states'],2)
        self.assertFalse(r['carrier_realization_certified'])
        self.assertEqual(r['carrier_realization_obstruction'],'unreachable_mini_state')

    def test_unprepared_joint_cartesian_states_are_ghosts(self):
        states=('00','01','10','11')
        p=Carrier(states,{'idle':{c:c for c in states}},
                  {c:c for c in states},('00',),'joint')
        m=bit()
        d=compile_dual_product(p,m,m,{c:c[0] for c in states},
                       {c:c[1] for c in states},(),(),
                       {c:(c[0],c[1]) for c in states})
        self.assertEqual(d['reason'],'joint_states_not_constructible_from_preparation')
        self.assertEqual(d['witness']['unreachable_pairs'],
                         [('0','1'),('1','0'),('1','1')])


class ClockFamilyTheoremTests(unittest.TestCase):
    def test_proper_cyclic_successor_factors_never_split(self):
        from observational_succ.miniature_carrier import cyclic_successor_factor
        for m, n in ((4,2),(6,2),(6,3),(8,4),(9,3),(12,4),(20,5)):
            r=cyclic_successor_factor(m,n)
            self.assertTrue(r['surjective_successor_factor_exists'])
            self.assertTrue(r['proper_factor_is_nonsplit'])
            self.assertFalse(r['equivariant_subcarrier_section_exists'])
        for m,n in ((6,4),(10,3),(7,2)):
            self.assertFalse(cyclic_successor_factor(m,n)['surjective_successor_factor_exists'])
        for n in (2,3,7):
            self.assertTrue(cyclic_successor_factor(n,n)['equivariant_subcarrier_section_exists'])
