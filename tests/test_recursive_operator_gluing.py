"""Finite exact Schur source-coupling certificates and compact-gap adversarial tests."""
import unittest
from fractions import Fraction as Q
from observational_succ.recursive_operator_gluing import (
    CouplingError, certify_schur, psd, principal_minors
)

class SchurTests(unittest.TestCase):
    def test_sources_positive_global_negative(self):
        c=certify_schur(((1,),),((2,),),((1,),))
        self.assertTrue(c.a_pd and c.b_psd)
        self.assertEqual(c.schur,((Q(-3),),))
        self.assertFalse(c.complete_psd or c.schur_psd)

    def test_mutant_safe_coupling(self):
        c=certify_schur(((1,),),((1,),),((1,),))
        self.assertTrue(c.complete_psd and c.schur_psd)
        self.assertEqual(c.schur,((Q(),),))

    def test_genuine_nontrivial_2x2_blocks(self):
        c=certify_schur(((2,1),(1,2)),((1,0),(0,1)),((2,0),(0,2)))
        self.assertEqual(c.schur,((Q(4,3),Q(1,3)),(Q(1,3),Q(4,3))))
        self.assertTrue(c.schur_psd and c.complete_psd)

    def test_compact_gap_trap_every_n(self):
        for n in (1,2,10,1000000):
            c=certify_schur(((Q(1,n*n),),),((Q(2,n),),),((1,),))
            self.assertFalse(c.complete_psd)
            self.assertEqual(c.schur,((Q(-3),),))

    def test_missing_source_guard(self):
        for A,C,B in (
          (((0,),),((1,),),((1,),)),
          (((1,0),(0,1)),((1,),),((1,),)),
          (((1,),),((1,),),((1,1),(1,1)))
        ):
            with self.assertRaises(CouplingError):certify_schur(A,C,B)

    def test_exact_minor_contradiction(self):
        A=((Q(1),Q(2)),(Q(2),Q(1)))
        self.assertFalse(psd(A))
        self.assertEqual(dict(principal_minors(A))[(0,1)],Q(-3))

    def test_floats_not_proof(self):
        with self.assertRaises(CouplingError):
            certify_schur(((1.0,),),((0,),),((1,),))

if __name__=='__main__':
    unittest.main()
