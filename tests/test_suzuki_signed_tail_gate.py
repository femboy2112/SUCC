import unittest
from fractions import Fraction as F
from observational_succ.suzuki_signed_tail_gate import (
    inverse,schur_scalar,source_positive_tail_lower_bound,
    negative_depth_diagonal,compact_countermodel,receipt,
)


class SignedTailTests(unittest.TestCase):
    def test_exact_inverse(self):
        self.assertEqual(inverse(((2,1),(1,1))),((F(1),F(-1)),(F(-1),F(2))))
    def test_shifted_schur(self):
        self.assertEqual(schur_scalar(1,1,1,1),F(3,2))
    def test_zero_shift_range_obstruction(self):
        self.assertLess(schur_scalar(1,1,0,F(1,128)),0)
        self.assertGreater(schur_scalar(1,1,0,1),0)
    def test_schur_monotone(self):
        vals=[schur_scalar(1,F(1,2),F(1,16),F(1,2**n)) for n in range(1,10)]
        self.assertTrue(all(x>y for x,y in zip(vals,vals[1:])))
    def test_positive_tail_not_symmetric_error(self):
        self.assertEqual(source_positive_tail_lower_bound(1,1,1,1,F(1,10)),F(3,2))
        with self.assertRaises(ValueError):
            source_positive_tail_lower_bound(1,1,1,1,-1)
    def test_hidden_negative_direction(self):
        r=compact_countermodel(5,8,F(1,7))
        self.assertTrue(r["same_observed_compression"])
        self.assertEqual(r["positive_depth"],0)
        self.assertEqual(r["hidden_negative_depth"],F(1,7))
    def test_no_source_sign_claim(self):
        self.assertFalse(receipt()["RH_proved"])
        self.assertFalse(receipt()["source_authentic_Weil_sign_proved"])


if __name__=="__main__":
    unittest.main()
