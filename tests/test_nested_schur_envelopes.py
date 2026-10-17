import unittest
from fractions import Fraction as F
from observational_succ.nested_schur_envelopes import (
    NestedShortError, short_to_low, monotone_nested_short_bounds,sign_switch_countermodel,
)

class NestedTests(unittest.TestCase):
    def test_monotone_diagonal(self):
        lower=((F(1),0,0),(0,F(1),0),(0,0,F(1)))
        upper=((F(2),0,0),(0,F(2),0),(0,0,F(3)))
        r=monotone_nested_short_bounds(lower,upper,1)
        self.assertEqual(r['low_short_lower'],((F(1),),))
        self.assertEqual(r['low_short_upper'],((F(2),),))
        self.assertFalse(r['original_source_identified'])

    def test_nonlinear_coupling(self):
        lower=((F(2),F(1)),(F(1),F(2)))
        upper=((F(3),F(1)),(F(1),F(3)))
        r=monotone_nested_short_bounds(lower,upper,1)
        self.assertEqual(r['low_short_lower'],((F(3,2),),))
        self.assertEqual(r['low_short_upper'],((F(8,3),),))

    def test_strictly_positive_discarded_middle_required(self):
        lower=((0,1),(1,-1));upper=((0,1),(1,1))
        with self.assertRaises(NestedShortError):
            monotone_nested_short_bounds(lower,upper,1)
        v=sign_switch_countermodel()
        self.assertTrue(v['U_minus_L_PSD'])
        self.assertTrue(v['short_order_reversed'])
        self.assertEqual(v['short_lower'],((F(1),),))
        self.assertEqual(v['short_upper'],((F(-1),),))

    def test_malformed_order(self):
        with self.assertRaises(NestedShortError):
            monotone_nested_short_bounds(((2,0),(0,2)),((1,0),(0,1)),1)

    def test_singular_middle_rejected(self):
        with self.assertRaises(NestedShortError):
            monotone_nested_short_bounds(((1,0),(0,0)),((1,0),(0,1)),1)

    def test_schur_preserves_rationals(self):
        self.assertEqual(short_to_low(((3,2),(2,5)),1),((F(11,5),),))

    def test_reject_float_or_bool(self):
        with self.assertRaises(NestedShortError):
            monotone_nested_short_bounds(((1.,0),(0,1)),((2,0),(0,2)),1)
        with self.assertRaises(NestedShortError):
            monotone_nested_short_bounds(((True,0),(0,1)),((2,0),(0,2)),1)

if __name__=='__main__':unittest.main()
