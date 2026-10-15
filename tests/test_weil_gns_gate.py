"""Independent exact probes separating positive auxiliaries from signed targets."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.weil_gns_gate import (
    FiniteSignedForm, GNSGateError, calibration_pair,
)


class WeilGNSFiniteControls(unittest.TestCase):
    def test_positive_and_rank_deficient_completion(self):
        for matrix in (
            ((1,0),(0,1)),
            ((1,1),(1,1)),
            ((0,0),(0,0)),
            ((2,1),(1,2)),
            ((0,0,0),(0,4,0),(0,0,0)),
        ):
            n=len(matrix)
            f=FiniteSignedForm(tuple("x"+str(i) for i in range(n)),matrix,"toy source")
            r=f.receipt()
            self.assertTrue(r["exact_finite_PSD"])
            self.assertTrue(r["GNS_positive_quotient_available_for_THIS_DECLARED_FORM"])
            self.assertFalse(r["claimed_complete_Weil_distribution_identified"])
            for v in product((-2,-1,0,1,2),repeat=n):
                self.assertGreaterEqual(f.quadratic(tuple(v)),0)

    def test_signed_negative_subspace_is_finite_witness(self):
        matrices=(
            ((1,0),(0,-1)),
            ((1,2),(2,1)),
            ((0,1),(1,0)),
            ((1,1,0),(1,1,0),(0,0,-1)),
        )
        for matrix in matrices:
            n=len(matrix)
            f=FiniteSignedForm(tuple("x"+str(i) for i in range(n)),matrix,"declared signed")
            r=f.receipt()
            self.assertFalse(r["exact_finite_PSD"])
            self.assertIsNotNone(r["first_negative_minor"])
            self.assertLess(r["first_negative_minor"][1],0)
            self.assertFalse(r["RH_proved"])

    def test_all_principal_minors_not_just_diagonal_or_leading(self):
        # Positive diagonal entries alone cannot establish PSD.
        f=FiniteSignedForm(("u","v"),((1,2),(2,1)),"signed")
        r=f.receipt()
        self.assertTrue(all(f.gram[i][i] >= 0 for i in range(2)))
        self.assertFalse(r["exact_finite_PSD"])
        self.assertEqual(f.quadratic((1,-1)),F(-2))

    def test_source_identity_and_wrong_input_rejected(self):
        for matrix in (((1,2),(3,1)),((1,),(2,)),((0.1,),),((True,),)):
            with self.assertRaises(GNSGateError):
                FiniteSignedForm(("x","y") if len(matrix)>1 else ("x",),matrix,"source")
        with self.assertRaises(GNSGateError):
            FiniteSignedForm(("x","x"),((1,0),(0,1)),"source")
        with self.assertRaises(GNSGateError):
            FiniteSignedForm(("x",),((1,),),"")
        with self.assertRaises(GNSGateError):
            FiniteSignedForm(("x",),((1,),),"source").quadratic((F(1),F(2)))

    def test_auxiliary_positive_does_not_identify_signed_Weil(self):
        r=calibration_pair()
        self.assertTrue(r["auxiliary_positive"]["exact_finite_PSD"])
        self.assertFalse(r["signed_countermodel"]["exact_finite_PSD"])
        self.assertFalse(r["positivity_of_auxiliary_implies_original_Weil"])
        self.assertFalse(r["RH_proved"])


if __name__=="__main__":
    unittest.main()
