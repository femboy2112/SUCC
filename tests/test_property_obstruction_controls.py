"""Exact source-blindness adversarial controls: finitely positive does not imply global PSD."""
from fractions import Fraction as Q
import unittest

from observational_succ.property_obstruction_controls import (
    PropertyObstructionError, quadratic_value, invisible_negative_direction,
)


class PositivityBlindspotTests(unittest.TestCase):
    def test_every_finite_horizon_admits_hidden_negative_unit(self):
        for K in (1,2,3,5,13,31,100):
            for M in (K+1, K+5):
                result = invisible_negative_direction(K,M)
                self.assertTrue(result["observed_corners_identical"])
                self.assertEqual(result["positive_form_value_at_unseen_unit"],"1")
                self.assertEqual(result["negative_form_value_at_unseen_unit"],"-1")
                self.assertFalse(result["source_attested"])
                self.assertFalse(result["RH_proved"])

    def test_two_forms_agree_on_every_observed_rational_probe(self):
        for K in range(1,15):
            M = K+2
            for j in range(K):
                v=tuple(Q((i-j)*(i+2),i+3) for i in range(K))
                self.assertEqual(quadratic_value(v),quadratic_value(v,M))

    def test_real_rational_negative_direction_and_positivity(self):
        v=(Q(1,2),Q(-3,4),Q(7,6))
        self.assertEqual(quadratic_value(v,10),quadratic_value(v))
        self.assertEqual(quadratic_value(v,2),
                         quadratic_value(v)-2*Q(3,4)**2)

    def test_invalid_access_is_not_a_valid_positivity_probe(self):
        with self.assertRaises(PropertyObstructionError):
            invisible_negative_direction(3,3)
        with self.assertRaises(PropertyObstructionError):
            invisible_negative_direction(0)
        with self.assertRaises(PropertyObstructionError):
            quadratic_value((1,0.5),2)
        with self.assertRaises(PropertyObstructionError):
            quadratic_value((Q(1),),0)


if __name__=="__main__":
    unittest.main()
