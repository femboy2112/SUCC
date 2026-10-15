"""All-prior rational joint-kernel tests and matched marginal failures."""
import unittest
from fractions import Fraction as Q
from observational_succ.miniature_stochastic import (
    StochasticCarrier, StochasticMini, MiniStochasticError, joint_factor,
    push_row,
)


def systems(mutant=False):
    q=('a','b')
    m=StochasticMini(q, {'coin': {
        'a':(('H','a',Q(1,2)),('T','b',Q(1,2))),
        'b':(('H','b',Q(1,2)),('T','a',Q(1,2)))
    }}, 'a', 'arith-source-v1')
    c=('a0','a1','b0','b1')
    parent_rows={}
    for s in c:
        x,h=s[0],s[1]
        y='a' if x=='b' else 'b'
        row=(('H',x+h,Q(1,2)),('T',y+h,Q(1,2)))
        if mutant and s=='a1':
            row=(('H','b1',Q(1,2)),('T','a1',Q(1,2)))
        parent_rows[s]=row
    p=StochasticCarrier(c, {'coin':parent_rows}, ('a0','a1'), 'arith-source-v1')
    decoder={s:s[0] for s in c}
    return p,m,decoder


class MiniStochasticTests(unittest.TestCase):
    def test_genuine_all_source_conditional_kernel(self):
        p,m,d=systems()
        r=joint_factor(p,m,d,{'coin':'coin'})
        self.assertTrue(r['certified'])
        self.assertEqual(r['source_action_joint_rows_checked'],4)
        self.assertFalse(r['physical_instrument_authenticated'])

    def test_identical_marginals_are_not_joint_source_law(self):
        p,m,d=systems(mutant=True)
        row=p.kernels['coin']['a1']
        actual=push_row(row,d)
        expected=push_row(m.kernels['coin']['a'], {q:q for q in m.states})
        self.assertEqual({z:sum(v for (k, _), v in actual.items() if k==z)
                         for z in ('H','T')},
                         {z:sum(v for (k, _), v in expected.items() if k==z)
                         for z in ('H','T')})
        self.assertEqual({q:sum(v for (_, k), v in actual.items() if k==q)
                          for q in m.states},
                         {q:sum(v for (_, k), v in expected.items() if k==q)
                          for q in m.states})
        r=joint_factor(p,m,d,{'coin':'coin'})
        self.assertEqual(r['reason'],'joint_receipt_state_law_mismatch')
        self.assertEqual(r['witness']['carrier_state'],'a1')

    def test_model_cannot_enable_hidden_source_or_ghost_probability(self):
        p,m,d=systems()
        self.assertEqual(joint_factor(p,m,d,{'coin':'coin'})['certified'],True)
        with self.assertRaises(MiniStochasticError):
            joint_factor(p,m,d,{'coin':'hidden_source_oracle'})
        with self.assertRaises(MiniStochasticError):
            StochasticCarrier(('a',),{'flip':{'a':(('H','a',Q(2,3)),)}},('a',),'x')
        with self.assertRaises(MiniStochasticError):
            StochasticCarrier(('a',),{'flip':{'a':(('H','a',0),('T','a',1))}},('a',),'x')

    def test_cannot_change_source_namespace(self):
        p,m,d=systems()
        mismatched=StochasticMini(m.states,m.kernels,m.initial,'different')
        with self.assertRaises(MiniStochasticError):
            joint_factor(p,mismatched,d,{'coin':'coin'})


if __name__ == '__main__':
    unittest.main()


class StochasticPreparationTests(unittest.TestCase):
    def test_abstract_joint_factor_with_unreachable_mini_state_is_not_realized(self):
        p=StochasticCarrier(('a','b'), {'idle':{
            'a':(('same','a',Q(1)),), 'b':(('same','b',Q(1)),)}},
            ('a',), 'ghost-physical')
        m=StochasticMini(('a','b'), {'idle':{
            'a':(('same','a',Q(1)),), 'b':(('same','b',Q(1)),)}},
            'a', 'ghost-physical')
        result=joint_factor(p,m,{'a':'a','b':'b'},{'idle':'idle'})
        self.assertEqual(result['reason'],'unreachable_mini_state')
