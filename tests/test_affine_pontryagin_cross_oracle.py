"""Independent exact phase oracle against existing Pontryagin/profinite API."""
import unittest
from fractions import Fraction as F
from observational_succ.affine_pontryagin_transfer import AffineSourceWord,TransferContractError
from observational_succ.pontryagin_source_duality import RationalCircleCharacter
from observational_succ.edge_carrier_reconstruction import ProfiniteProgram

class AffinePontryaginIntegration(unittest.TestCase):
    def test_real_profinite_character_cross_oracle(self):
        word=AffineSourceWord((('S',1),('V',2),('S',1),('V',3)))
        a,b=word.normal_form()
        for r in (F(0),F(1,7),F(5,12),F(-1,13)):
            char=RationalCircleCharacter(r)
            pulled,phase=word.dual_pontryagin_character(char)
            self.assertEqual((pulled.frequency,phase),((a*r)%1,(b*r)%1))
            for x in (ProfiniteProgram.integer(5),ProfiniteProgram.projector(2),
                      ProfiniteProgram.projector(3)):
                y=x.multiply(ProfiniteProgram.integer(a)).add(ProfiniteProgram.integer(b))
                self.assertEqual(char.evaluate(y),(pulled.evaluate(x)+phase)%1)
    def test_source_epoch_mismatch_fail_closed(self):
        w=AffineSourceWord((('S',1),),source_id='S',epoch=3)
        for source,epoch in (('S',4),('T',3)):
            with self.assertRaises(TransferContractError):
                w.dual_pontryagin_character(RationalCircleCharacter(F(1,2),source_id=source,epoch=epoch))

if __name__=='__main__':unittest.main()
