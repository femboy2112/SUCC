"""Scoped finite/source table and higher-order interaction regression controls."""
import unittest
from itertools import product, combinations

from observational_succ.recursive_model_interactions import (
    SourceCarrier, ModelInteractionError, leaf, join, project, closure,
    global_fiber, min_unsat_cores, sound_for_declared_truth,
    available_information_signature, distinguishable_pairs,
)

class RecursiveModelTests(unittest.TestCase):
    def setUp(self):
        self.c=SourceCarrier('math-X',4,'(a,b,c)',('a','b','c'),tuple(product('01',repeat=3)))
        self.ab=leaf(self.c,'AB=',('a','b'),(('0','0'),('1','1')))
        self.bc=leaf(self.c,'BC=',('b','c'),(('0','0'),('1','1')))
        self.acneq=leaf(self.c,'AC!=',('a','c'),(('0','1'),('1','0')))

    def test_level2_exposes_nonlocal_constraint(self):
        m=join(self.c,self.ab,self.bc)
        self.assertEqual(m.level,1)
        self.assertEqual(project(self.c,m,('a','c')).allowed,frozenset((('0','0'),('1','1'))))
        self.assertEqual(len(global_fiber(self.c,(self.ab,))),4)
        self.assertEqual(len(global_fiber(self.c,(self.ab,self.bc))),2)
        self.assertEqual(m.support,frozenset(('AB=','BC=')))
        self.assertTrue(len(closure(self.c,(self.ab,self.bc),depth=2))>2)

    def test_meta_cycle_obstruction_pairwise_ghost(self):
        for pair in combinations((self.ab,self.bc,self.acneq),2):
            self.assertTrue(global_fiber(self.c,pair))
        self.assertEqual(global_fiber(self.c,(self.ab,self.bc,self.acneq)),())
        self.assertEqual(min_unsat_cores(self.c,(self.ab,self.bc,self.acneq)),
                         (frozenset(('AB=','BC=','AC!=')),))

    def test_soundness_conditional_not_automatic(self):
        m=join(self.c,self.ab,self.bc)
        self.assertTrue(sound_for_declared_truth(self.c,m,('1','1','1')))
        self.assertFalse(sound_for_declared_truth(self.c,m,('1','0','1')))
        with self.assertRaises(ModelInteractionError):
            sound_for_declared_truth(self.c,m,('2','2','2'))

    def test_join_algebra(self):
        a,b,c=self.ab,self.bc,self.acneq
        for x,y in ((a,b),(b,c),(a,c)):
            self.assertEqual(join(self.c,x,y).allowed,join(self.c,y,x).allowed)
            self.assertEqual(join(self.c,x,x).allowed,x.allowed)
        left=join(self.c,join(self.c,a,b),c)
        right=join(self.c,a,join(self.c,b,c))
        self.assertEqual((left.scope,left.allowed),(right.scope,right.allowed))
        self.assertFalse(left.allowed)

    def test_no_free_bit_data_processing(self):
        reports=available_information_signature(
            self.c,tuple(tuple(w[i] for w in self.c.worlds) for i in (0,1)))
        before=distinguishable_pairs(reports)
        for fn in (
            lambda u:u[0],lambda u:u[0]==u[1],
            lambda u:(u,u[::-1]),lambda u:(u[0]+u[1])*2
        ):
            augmented=tuple((r,fn(r)) for r in reports)
            self.assertEqual(distinguishable_pairs(augmented),before)
            for i,j in combinations(range(len(reports)),2):
                if reports[i]==reports[j]:self.assertEqual(fn(reports[i]),fn(reports[j]))

    def test_provenance_ablation(self):
        allroots=(self.ab,self.bc,self.acneq)
        for r in allroots:
            self.assertTrue(global_fiber(self.c,tuple(x for x in allroots if x!=r)))
        self.assertFalse(global_fiber(self.c,allroots))

    def test_source_epoch_basis_mutants(self):
        for c in (
          SourceCarrier('other',4,'(a,b,c)',self.c.variables,self.c.worlds),
          SourceCarrier('math-X',5,'(a,b,c)',self.c.variables,self.c.worlds),
          SourceCarrier('math-X',4,'(c,b,a)',self.c.variables,self.c.worlds)
        ):
            with self.assertRaises(ModelInteractionError):join(c,self.ab,self.bc)
        with self.assertRaises(ModelInteractionError):
            leaf(self.c,'fake',('a','c'),(('2','2'),))
        with self.assertRaises(ModelInteractionError):
            leaf(self.c,'rev',('c','a'),(('1','1'),))

    def test_source_table_relative_join_prohibits_ghost(self):
        c=SourceCarrier('x',0,'v',('a','b'),(('0','0'),('1','1')))
        ab=leaf(c,'all',('a','b'),(('0','0'),('1','1')))
        self.assertEqual(global_fiber(c,(ab,)),c.worlds)
        self.assertEqual(join(c,ab,ab).allowed,ab.allowed)

    def test_projection_wrong_scope(self):
        with self.assertRaises(ModelInteractionError):
            project(self.c,self.ab,('a','c'))

    def test_empty_relation_retains_contradiction(self):
        all3=join(self.c,join(self.c,self.ab,self.bc),self.acneq)
        self.assertEqual(all3.allowed,frozenset())
        self.assertEqual(all3.support,frozenset(('AB=','BC=','AC!=')))
        self.assertEqual(global_fiber(self.c,(all3,)),())

    def test_root_legal_vs_truth_law(self):
        actual=('1','0','0')
        self.assertTrue(sound_for_declared_truth(self.c,self.bc,actual))
        self.assertFalse(sound_for_declared_truth(self.c,self.ab,actual))
        self.assertFalse(sound_for_declared_truth(self.c,join(self.c,self.ab,self.bc),actual))

if __name__=='__main__':
    unittest.main()
