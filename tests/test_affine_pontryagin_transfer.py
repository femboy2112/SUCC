"""Exact source-preserving arithmetic transfer and affine chronology controls."""
import unittest
from fractions import Fraction as F
from observational_succ.affine_pontryagin_transfer import (
    RationalCharacterAlgebra as A, AffineSourceWord as W, TransferContractError,
    exact_transfer_relations, history_loss_witness, verify_dual_word_composition,
)


class ExactTransferTests(unittest.TestCase):
    def test_rho_preimages_classical(self):
        e=A.basis(F(1,2))
        self.assertEqual(e.rho(2), A(((F(1,4),F(1,2)),(F(3,4),F(1,2)))))
        self.assertEqual(A.basis().rho(2).terms, ((F(0),F(1,2)),(F(1,2),F(1,2))))

    def test_full_relations_many(self):
        for m,n in ((2,3),(3,4),(2,7)):
            for r in (F(0),F(1,5),F(-7,12)):
                for s in (F(1,3),F(5,14)):
                    d=exact_transfer_relations(r,s,n,m)
                    checked=('multiplicative','semigroup','inverse','projection',
                             'idempotent','nonunital','adjoint_n')
                    self.assertTrue(all(v for k,v in d.items() if k.endswith(checked)),d)

    def test_positive_haar_nonnegative_for_square(self):
        e=A(((F(0),F(2)),(F(1,3),F(-1)),(F(2,3),F(-1))))
        self.assertEqual(e.multiply(e).haar(),F(6))

    def test_source_epochs_not_glued(self):
        with self.assertRaises(TransferContractError):
            A.basis(F(1,3),epoch=0).multiply(A.basis(F(1,3),epoch=1))
        with self.assertRaises(TransferContractError):
            W((("S",1),),source_id='S1').then(W((("V",2),),source_id='S2'))

    def test_adversarial_inputs(self):
        for bad in (True,2.,0,-2,257):
            with self.assertRaises(TransferContractError): A.basis().rho(bad)
        for bad in (('V',6),('V',1),('S',2),('V',True),('Q',3)):
            with self.assertRaises(TransferContractError): W((bad,))

    def test_nonunital_and_projection(self):
        for n in (2,3,5):
            ep=A.basis().rho(n)
            self.assertNotEqual(ep,A.basis())
            self.assertEqual(ep.multiply(ep),ep)
            self.assertEqual(ep.haar(),F(1,n))
            self.assertEqual(A.basis(F(1,7)).sigma(n).rho(n),
                             A.basis(F(1,7)).multiply(ep))

    def test_history_collision_and_word_duality(self):
        for p in (2,3,5):
            witness=history_loss_witness(p)
            self.assertTrue(witness['equal_affine_endpoints'])
            self.assertNotEqual(witness['left_steps'],witness['right_steps'])
            self.assertFalse(witness['endpoint_decoder_of_event_count_exists'])
        w1=W((("S",1),("V",2)))
        w2=W((("V",3),("S",1)))
        for r in (F(0),F(1,5),F(7,12)):
            self.assertTrue(verify_dual_word_composition(w1,w2,r))
            a,b=w1.then(w2).normal_form()
            self.assertEqual(w1.then(w2).dual_character(r),(a*r%1,b*r%1))


if __name__=='__main__':
    unittest.main()
