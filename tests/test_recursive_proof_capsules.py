"""Evidence-carrying models of model interactions; exact source/domain negative gates."""
import unittest
from itertools import product
from fractions import Fraction as Q

from observational_succ.recursive_model_interactions import SourceCarrier,leaf
from observational_succ.recursive_proof_capsules import (
    Capsule, ProofCapsuleError, relation_capsule, obstruction_capsule,
    schur_capsule, contour_capsule, combine_verified, ask_global_weil_positivity
)

class MetaProofTests(unittest.TestCase):
    def setUp(self):
        self.carrier=SourceCarrier('X',0,'abc',('a','b','c'),tuple(product('01',repeat=3)))
        self.a=leaf(self.carrier,'AB',('a','b'),(('0','0'),('1','1')))
        self.b=leaf(self.carrier,'BC',('b','c'),(('0','0'),('1','1')))
        self.c=leaf(self.carrier,'AC_NOT',('a','c'),(('0','1'),('1','0')))

    def test_new_constraint_with_exact_source_support(self):
        m=relation_capsule(self.carrier,(self.a,self.b),('a','c'))
        self.assertEqual(m.conclusion,(('0','0'),('1','1')))
        self.assertEqual(m.premises,frozenset(('AB','BC')))
        self.assertFalse(m.rh_proved)

    def test_missing_dependency_changes_truth(self):
        m=relation_capsule(self.carrier,(self.a,),('a','c'))
        self.assertNotEqual(m.conclusion,(('0','0'),('1','1')))

    def test_meta_obstruction_source_witness(self):
        m=obstruction_capsule(self.carrier,(self.a,self.b,self.c))
        self.assertEqual(m.conclusion,(('AB','AC_NOT','BC'),))
        with self.assertRaises(ProofCapsuleError):
            obstruction_capsule(self.carrier,(self.a,self.b))

    def test_signed_operator_is_not_weil(self):
        c=schur_capsule(((1,),),((2,),),((1,),))
        self.assertEqual(c.conclusion,('NOT_PSD',(('-3',),)))
        self.assertNotEqual(c.source,'AUTHENTIC_Q_XI_COMPLETED_THETA')
        with self.assertRaises(ProofCapsuleError):
            ask_global_weil_positivity((c,))

    def test_cross_source_rejects_false_inference(self):
        finite=relation_capsule(self.carrier,(self.a,self.b),('a','c'))
        schur=schur_capsule(((1,),),((1,),),((1,),))
        with self.assertRaises(ProofCapsuleError):
            combine_verified(finite,schur)

    def test_same_source_repetition_is_not_independence(self):
        a=relation_capsule(self.carrier,(self.a,self.b),('a','c'))
        b=relation_capsule(self.carrier,(self.a,self.b),('a','c'))
        c=combine_verified(a,b)
        self.assertEqual(c.premises,a.premises)
        self.assertEqual(c.conclusion,a.conclusion)
        self.assertEqual(len(c.parent_capsules),2*len(a.parent_capsules))

    def test_untyped_rh_rejected(self):
        with self.assertRaises(ProofCapsuleError):
            Capsule('CONTOUR_ZERO_COUNT','zeta','all complex',
                    ('all positive',),frozenset(),(), 'PROVED',True)

    def test_original_xi_meta_capsule_cannot_prove_weil(self):
        from observational_succ.theta_taylor_jets import jets
        data=jets(degree=20,modes=3,T=8,cells=1536)
        c=contour_capsule(data,Q(3),Q(11,2),13)
        self.assertEqual(c.conclusion,(0,))
        self.assertEqual(c.status,'PROVED_MATHEMATICAL_SOURCE_BOUNDED_DOMAIN')
        with self.assertRaises(ProofCapsuleError):
            ask_global_weil_positivity((c,))

if __name__=='__main__':
    unittest.main()
