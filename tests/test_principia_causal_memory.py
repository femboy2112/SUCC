import unittest
from dataclasses import replace
from observational_succ.principia_causal_memory import (
    CausalSourceError, Step, CausalMemory, Policy, carrier, passport,
    initial_memory, verify_memory, step_memory, response_paths,
    joint_potential_outcomes, reachable_atoms, future_quotient,
    verify_future_quotient, shortest_distinguishing_path, strong_future_null,
    find_target_policy, verify_target_policy, gaussian_theta_null_carrier,
)


def silent_preparation():
    """Load reads zero and doesn't remove a world, but enables read later."""
    states = ('s0', 's1', 'l0', 'l1', 'read0', 'read1')
    return carrier(
        'silent-preparation-source', ('w0', 'w1'), states,
        ('noop', 'read', 'load'), ('s0', 's1'),
        ('0', '0', '0', '0', '0', '1'), ('alpha', 'beta'),
        (
            states,
            ('read0', 'read0', 'read0', 'read1', 'read0', 'read1'),
            ('l0', 'l1', 'l0', 'l1', 'read0', 'read1'),
        ), costs=(0, 1, 0),
    )


def cross_action_source(with_reset=True):
    """Two hidden causal coupling types have identical one-action marginals."""
    worlds = ('C0', 'C1', 'A0', 'A1')
    states = tuple(f'{stage}{w}' for stage in ('i','a','b') for w in worlds)
    lookup = {(stage,w):states[4*i+j] for i,stage in enumerate(('i','a','b'))
              for j,w in enumerate(worlds)}
    actions = ('a','b','reset') if with_reset else ('a','b')
    outputs = []
    for stage in ('i','a','b'):
        for w in worlds:
            bit=int(w[1]);mode=int(w[0]=='A')
            outputs.append('0' if stage=='i' else str(bit if stage=='a' else bit^mode))
    moves = []
    for action in actions:
        row=[]
        for stage in ('i','a','b'):
            for w in worlds:
                if action=='reset':nextstage='i'
                elif stage!='i':nextstage=stage  # destructive: can only reset to probe again
                else:nextstage=action
                row.append(lookup[(nextstage,w)])
        moves.append(tuple(row))
    return carrier('joint-coupling-with-reset' if with_reset else 'joint-coupling-no-reset',
                   worlds, states, actions, tuple(lookup[('i',w)] for w in worlds),
                   outputs, tuple(w[0] for w in worlds), tuple(moves))


class CausalMemoryTests(unittest.TestCase):
    def test_same_zero_memory_distinct_causal_coupling(self):
        c=silent_preparation()
        m=initial_memory(c,'0')
        prepared=step_memory(c,m,'load','0')
        self.assertEqual({w for w,_ in m.coupling},{w for w,_ in prepared.coupling})
        self.assertNotEqual(m.coupling,prepared.coupling)
        self.assertEqual(prepared.steps,(Step('load','0'),))
        self.assertEqual({p[2] for p in response_paths(c,m,('read',))},{('0',)})
        self.assertEqual({p[2] for p in response_paths(c,prepared,('read',))},{('0',),('1',)})

    def test_sham_vs_silent_instrument_preparation(self):
        c=silent_preparation()
        m=initial_memory(c,'0')
        self.assertTrue(strong_future_null(c,m,'noop'))
        self.assertFalse(strong_future_null(c,m,'load'))
        self.assertFalse(strong_future_null(c,m,'read'))
        prepared=step_memory(c,m,'load','0')
        self.assertEqual(len(prepared.coupling),len(m.coupling))
        self.assertTrue(strong_future_null(c,prepared,'noop'))

    def test_policy_requires_real_preparation(self):
        c=silent_preparation()
        m=initial_memory(c,'0')
        self.assertIsNone(find_target_policy(c,m,1))
        policy=find_target_policy(c,m,2)
        self.assertIsNotNone(policy)
        self.assertEqual(policy.action,'load')
        self.assertEqual(verify_target_policy(c,m,policy,max_depth=2),2)
        self.assertIsNone(find_target_policy(c,m,5,allowed=('noop','read')))

    def test_target_can_be_identified_after_actual_observations(self):
        c=silent_preparation()
        m=initial_memory(c,'0')
        m=step_memory(c,m,'load','0')
        m=step_memory(c,m,'read','1')
        self.assertEqual(m.coupling,(('w1','read1'),))
        self.assertEqual(find_target_policy(c,m,0),Policy(None,'beta'))

    def test_forged_memory_and_source_mutant_refused(self):
        c=silent_preparation()
        m=initial_memory(c,'0')
        with self.assertRaises(CausalSourceError):verify_memory(c,replace(m,coupling=(('w0','s0'),)))
        with self.assertRaises(CausalSourceError):verify_memory(c,replace(m,source='fake'))
        changed=replace(c,outputs=('0','0','0','0','1','1'))
        with self.assertRaises(CausalSourceError):verify_memory(changed,m)
        with self.assertRaises(CausalSourceError):step_memory(c,m,'read','1')

    def test_future_quotient_independently_verified(self):
        for c in (silent_preparation(),cross_action_source()):
            with self.subTest(name=c.name):
                q=future_quotient(c)
                self.assertEqual(verify_future_quotient(c,q),q)
                self.assertLessEqual(len(q.dimensions),len(q.atoms))
                self.assertEqual(q.dimensions[-1],len(set(q.colors)))

    def test_minimality_has_finite_witness(self):
        c=silent_preparation()
        q=verify_future_quotient(c,future_quotient(c))
        for i,a in enumerate(q.atoms):
            for j in range(i+1,len(q.atoms)):
                b=q.atoms[j]
                word=shortest_distinguishing_path(c,a,b)
                if q.colors[i]==q.colors[j]:
                    self.assertIsNone(word)
                else:
                    self.assertIsNotNone(word)
                    self.assertLessEqual(len(word),len(q.atoms)-1)

    def test_forged_behavior_class_and_history_rejected(self):
        c=silent_preparation()
        q=future_quotient(c)
        with self.assertRaises(CausalSourceError):verify_future_quotient(c,replace(q,colors=tuple(0 for _ in q.colors)))
        with self.assertRaises(CausalSourceError):verify_future_quotient(c,replace(q,dimensions=(1,)))
        with self.assertRaises(CausalSourceError):verify_future_quotient(replace(c,costs=(1,1,0)),q)

    def test_same_individual_observation_marginals_different_coupling(self):
        c=cross_action_source()
        m=initial_memory(c,'0')
        joint=joint_potential_outcomes(c,m,(('a',),('b',)))
        for i in (0,1):
            marginals={j[2][i] for j in joint if j[1]=='C'}
            mutant={j[2][i] for j in joint if j[1]=='A'}
            self.assertEqual(marginals,mutant)
            self.assertEqual(marginals,{('0',),('1',)})
        self.assertEqual({j[2] for j in joint if j[1]=='C'},
                         {(('0',),('0',)),(('1',),('1',))})
        self.assertEqual({j[2] for j in joint if j[1]=='A'},
                         {(('0',),('1',)),(('1',),('0',))})

    def test_reset_makes_causal_coupling_operationally_discriminable(self):
        c=cross_action_source(with_reset=True)
        m=initial_memory(c,'0')
        self.assertIsNone(find_target_policy(c,m,2))
        policy=find_target_policy(c,m,3)
        self.assertIsNotNone(policy)
        self.assertEqual(verify_target_policy(c,m,policy,max_depth=3),3)
        self.assertEqual({p[2] for p in response_paths(c,m,('a','reset','b'))},
                         {('0','0','0'),('0','0','1'),('1','0','0'),('1','0','1')})

    def test_no_reset_leaves_operational_access_gap(self):
        c=cross_action_source(with_reset=False)
        m=initial_memory(c,'0')
        self.assertIsNone(find_target_policy(c,m,5))
        # Mathematical counterfactual joint still differs by source, but cannot be sampled jointly.
        self.assertEqual(len(joint_potential_outcomes(c,m,(('a',),('b',)))),4)

    def test_wrong_policy_detected_by_exhaustive_replay(self):
        c=silent_preparation()
        m=initial_memory(c,'0')
        p=Policy('load',None,(('0',Policy('read',None,(('0',Policy(None,'alpha')),('1',Policy(None,'alpha'))))),))
        with self.assertRaises(CausalSourceError):verify_target_policy(c,m,p,max_depth=2)

    def test_memory_disclosure_is_not_source_contact(self):
        c=silent_preparation()
        m=initial_memory(c,'0')
        self.assertEqual(len(m.coupling),2)  # candidate models, no empirical source bit
        self.assertEqual({t for _,t,_ in response_paths(c,m,())},{'alpha','beta'})

    def test_authentic_gaussian_two_kinds_of_zero(self):
        c=gaussian_theta_null_carrier()
        m=initial_memory(c,'0')
        self.assertEqual(len(m.coupling),2)
        self.assertEqual({p[2] for p in response_paths(c,m,('repeat',))},{('0',)})
        self.assertEqual({p[2] for p in response_paths(c,m,('lift',))},{('-16',),('0',)})
        self.assertTrue(strong_future_null(c,m,'repeat'))
        self.assertFalse(strong_future_null(c,m,'lift'))
        policy=find_target_policy(c,m,1)
        self.assertIsNotNone(policy)
        self.assertEqual(verify_target_policy(c,m,policy,max_depth=1),1)
        self.assertEqual(step_memory(c,m,'lift','-16').coupling,
                         (('norm2-rotation','n2-jet4'),))
        self.assertEqual(verify_future_quotient(c,future_quotient(c)).source,passport(c))

    def test_forged_branch_rejected_even_when_unreachable(self):
        c=silent_preparation()
        m=initial_memory(c,'0')
        real=find_target_policy(c,m,2)
        fake=replace(real,branches=real.branches+(('fake',Policy(None,'alpha')),))
        with self.assertRaises(CausalSourceError):verify_target_policy(c,m,fake,max_depth=2)

    def test_illegal_coupling_and_cost(self):
        c=silent_preparation()
        with self.assertRaises(CausalSourceError):carrier('bad',('w',),('q',),('a',),('q',),('0',),('x',),(('bad',),))
        with self.assertRaises(CausalSourceError):carrier('bad',('w',),('q',),('a',),('q',),('0',),('x',),(('q',),),costs=(-1,))


if __name__=='__main__':unittest.main()
