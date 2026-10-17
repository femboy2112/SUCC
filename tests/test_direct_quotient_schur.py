"""Exact mathematical quotient and operator tests, not original-source sign claims."""
import unittest
from fractions import Fraction as F
from observational_succ.direct_quotient_schur import (
    DirectQuotientError, projected_step_gram, certified_projector_first_upper,
    exact_finite_operator_schur, exact_psd, rank_one_coercivity_gain,
)


class DirectQuotientMath(unittest.TestCase):
    def test_constant_and_linear_project_to_zero(self):
        rows=[]
        for c in range(12):
            x=F(-1,2)+F(2*c+1,24)
            rows.append((F(1),x))
        g=projected_step_gram(rows)['projected_gram']
        self.assertEqual(g[0][0],0)
        self.assertEqual(g[0][1],0)
        self.assertGreater(g[1][1],0)

    def test_positive_gram_and_normalization(self):
        rows=[(F(1),F(2),F(0),F(3))]*8
        self.assertTrue(exact_psd(projected_step_gram(rows)['projected_gram']))
        self.assertEqual(projected_step_gram(rows)['projected_gram'][0][0],0)

    def test_parity_sensitive_direct_quotient_errors(self):
        pts=[((F(1),F(1)),(F(q,12),F(q,12)),(F(0),F(0)),(F(0),F(0))) for q in range(1,9)]
        e=certified_projector_first_upper(pts,(F(0),F(1,3),F(0),F(0)),(F(0),)*4)
        self.assertTrue(exact_psd(e['quotient_loewner_upper']))
        self.assertEqual(e['quotient_loewner_upper'][0][1],0)
        self.assertEqual(e['error_l2_column_upper'][0],0)
        self.assertEqual(e['error_gram_operator_diagonal_upper'][2],0)

    def test_exact_cancellation_of_large_polynomial_component(self):
        rows=[(F((i-4)**2),F(0),F(0),F(0)) for i in range(8)]
        boosted=[(row[0]+10**12,)+row[1:] for row in rows]
        self.assertEqual(projected_step_gram(rows)["projected_gram"],
                         projected_step_gram(boosted)["projected_gram"])
        self.assertNotEqual(projected_step_gram(rows)["unprojected_gram"],
                            projected_step_gram(boosted)["unprojected_gram"])

    def test_uncertainty_not_discarded(self):
        pts=[((F(0),F(1,10)),(F(0),F(0)),(F(0),F(0)),(F(0),F(0)))]*4
        e=certified_projector_first_upper(pts,(F(1),F(0),F(0),F(0)),(F(0),)*4)
        self.assertGreater(e['error_squared_cell_bounds'][0],0)
        self.assertGreater(e['quotient_loewner_upper'][0][0],0)

    def test_float_bool_negative_and_invalid_contracts(self):
        for bad in (0.1,True,F(-1)):
            with self.assertRaises(DirectQuotientError):
                certified_projector_first_upper([((0,0),)*4],(0,)*4,(bad,0,0,0))
        with self.assertRaises(DirectQuotientError):
            projected_step_gram([(1,2),(3,)])


class OperatorComparison(unittest.TestCase):
    def test_exact_operator_rank_one_improvement(self):
        A=((F(3),F(1,2)),(F(1,2),F(2)))
        B=((F(1),F(2)),(F(2),F(1)))
        K=((F(1),F(0)),(F(0),F(2)))
        C=((F(3,2),F(0)),(F(0),F(2)))
        D=((F(2),F(0)),(F(0),F(3)))
        U=((F(0),F(0)),(F(0),F(0)))
        r=exact_finite_operator_schur(A,B,D,C,U)
        self.assertTrue(exact_psd(tuple(tuple(r['actual'][i][j]-r['lower'][i][j]
                                            for j in range(2)) for i in range(2))))
        self.assertFalse(r['original_source_identified'])
        q=rank_one_coercivity_gain(K,(1,0),kappa=1,delta=F(1,2))
        self.assertEqual(q['gain_coefficient'],F(1,3))
        self.assertFalse(q['source_D_ge_comparator_proved'])

    def test_wrong_order_rejected(self):
        with self.assertRaises(DirectQuotientError):
            exact_finite_operator_schur(((2,),),((1,),),((F(1,3),),),((1,),),((0,),))

    def test_response_identity_and_schur_independence(self):
        A=((F(3),),);B=((F(1),),);D=((F(2),),);C=((F(1),),)
        r0=exact_finite_operator_schur(A,B,D,C,((F(0),),))
        r1=exact_finite_operator_schur(A,B,D,C,((F(1,2),),))
        self.assertEqual(r0['actual'],r1['actual'])
        self.assertEqual(r1['actual'],r1['lower'])
        self.assertNotEqual(r0['lower'],r1['lower'])


if __name__=='__main__':
    unittest.main()
