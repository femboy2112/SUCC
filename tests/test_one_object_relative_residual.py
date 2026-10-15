"""Exact residual Schur theorem with full finite inverse as hostile independent oracle."""
import unittest
from fractions import Fraction as F
from observational_succ import one_object_relative_residual as r

def diag(values):
    return tuple(tuple(F(values[i]) if i==j else F() for j in range(len(values)))
                 for i in range(len(values)))

class RelativeShortingTests(unittest.TestCase):
    def setUp(self):
        self.K=diag((1,F(1,4),F(1,9)))
        self.D=diag((2,F(1,4),F(1,9)))
        self.B=((F(1),),(F(1,4),),(F(1,9),))

    def test_complete_two_sided_source_matrix_order(self):
        for seen in ((),(0,),(0,1),(0,1,2)):
            z=r.finite_relative_short(((F(9,10),),),self.D,self.B,self.K,1,seen)
            self.assertTrue(r.psd(r.add(z.true_response,z.lower_response,-1)))
            self.assertTrue(r.psd(r.add(z.upper_response,z.true_response,-1)))
            self.assertFalse(z.authentic_suzuki_source)
            self.assertFalse(z.rh_proved)
        self.assertEqual(z.true_response,((F(31,36),),))

    def test_adding_a_high_response_can_convert_inconclusive_to_positive(self):
        A=((F(9,10),),)
        first=r.finite_relative_short(A,self.D,self.B,self.K,1)
        improved=r.finite_relative_short(A,self.D,self.B,self.K,1,(0,))
        self.assertFalse(first.whole_space_positive_from_lower_schur)
        self.assertTrue(improved.whole_space_positive_from_lower_schur)
        self.assertEqual(improved.upper_response,improved.true_response)
        self.assertEqual(improved.lower_response,((F(1,2),),))
        self.assertEqual(improved.upper_response,((F(31,36),),))

    def test_genuine_finite_negative_test_requires_source_response(self):
        A=((F(4,5),),)
        before=r.finite_relative_short(A,self.D,self.B,self.K,1)
        after=r.finite_relative_short(A,self.D,self.B,self.K,1,(0,1,2))
        self.assertIsNone(before.exact_finite_negative_witness)
        self.assertIsNotNone(after.exact_finite_negative_witness)
        self.assertFalse(after.whole_space_positive_from_lower_schur)
        self.assertLess(r.quadratic(r.add(A,after.true_response,-1),
                                   after.exact_finite_negative_witness),0)

    def test_full_finite_inverse_matches_correct_variational_response(self):
        A=((F(1),),)
        z=r.finite_relative_short(A,self.D,self.B,self.K,1,(0,1,2))
        self.assertEqual(z.residual,r.zero(3,1))
        self.assertEqual(z.lower_response,z.true_response)
        self.assertEqual(z.upper_response,z.true_response)
        self.assertEqual(z.Y,((F(1,2),),(F(1),),(F(1),)))

    def test_wrong_fixed_identity_gap_refused(self):
        K=diag((1,F(1,100)))
        D=diag((1,F(1,100)))
        B=((F(1),),(F(1,10),))
        good=r.finite_relative_short(((F(3),),),D,B,K,1)
        self.assertEqual(good.true_response,((F(2),),))
        self.assertTrue(good.whole_space_positive_from_lower_schur)
        with self.assertRaises(r.ResidualSourceError):
            r.finite_relative_short(((F(3),),),D,B,r.eye(2),1)

    def test_exact_non_diagonal_positive_neumann_relative_metric(self):
        D=((F(2),F(1)),(F(1),F(3)))
        K=r.eye(2)
        B=((F(1),F(2)),(F(3),F(-1)))
        A=((F(20),F(0)),(F(0),F(20)))
        for seen in ((),(0,),(1,),(0,1)):
            out=r.finite_relative_short(A,D,B,K,1,seen)
            self.assertTrue(r.psd(r.add(out.true_response,out.lower_response,-1)))
            self.assertTrue(r.psd(r.add(out.upper_response,out.true_response,-1)))

    def test_exact_singular_low_psd_is_accepted_as_psd(self):
        self.assertTrue(r.psd(((F(0),F()),(F(),F(1)))))
        self.assertFalse(r.pd(((F(0),F()),(F(),F(1)))))
        self.assertFalse(r.psd(((F(0),F(1)),(F(1),F(0)))))

    def test_no_false_certificates_from_invalid_high_source(self):
        for fn in (
            lambda:r.finite_relative_short(((1,),),((0,),),((1,),),((1,),),1),
            lambda:r.finite_relative_short(((1,),),((1,),),((1,),),((1,),),2),
            lambda:r.finite_relative_short(((1,),),((1,),),((1,),),((0,),),1),
            lambda:r.finite_relative_short(((1,),),((1,),),((1,),),((1,),),0),
            lambda:r.finite_relative_short(((1,),),((1,),),((1,),),((1,),),1,(1,)),
            lambda:r.finite_relative_short(((1,),),((1,),),((1,),),((1,),),1,(0,0)),
        ):
            with self.assertRaises(r.ResidualSourceError):fn()

    def test_no_float_alias_even_when_numeric_values_equal(self):
        with self.assertRaises(r.ResidualSourceError):
            r.finite_relative_short(((1.0,),),((1,),),((1,),),((1,),),1)
        with self.assertRaises(r.ResidualSourceError):
            r.finite_relative_short(((1,),),((1,),),((1,),),((1,),),1.0)

    def test_parity_splits_even_odd_without_mixed_residual(self):
        D=diag((2,3));K=r.eye(2)
        B=((F(1),F()),(F(),F(2)))
        A=diag((2,2))
        out=r.finite_relative_short(A,D,B,K,1,(0,))
        self.assertEqual(out.residual[0],(F(),F()))
        self.assertEqual(out.residual[1],(F(),F(2)))
        for M in (out.lower_response,out.upper_response,out.true_response):
            self.assertEqual(M[0][1],0)

class InfiniteToyObstructionTests(unittest.TestCase):
    def test_compact_high_inverse_can_be_unbounded_but_short_response_finite(self):
        for n in (1,2,4,8,16,64,512):
            receipt=r.finite_residual_approaching_zero(n)
            self.assertFalse(receipt["infinite_high_inverse_vector_in_l2"])
            self.assertTrue(receipt["finite_scalar_zero_shift_response"])
            self.assertLessEqual(receipt["residual_H1_squared_upper"],F(1,n))
            self.assertFalse(receipt["authentic_weil"])

    def test_absence_of_H1_cross_regularization_is_a_real_obstruction(self):
        for n in (1,2,10,100):
            out=r.missing_H1_obstruction(n)
            self.assertEqual(out["finite_response"],F(n))
            self.assertFalse(out["bounded_zero_shift_response"])
            self.assertFalse(out["authentic_weil"])

if __name__=="__main__":
    unittest.main()
