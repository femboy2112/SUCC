"""Exact rational fourth-derivative, positive e^3 and Xi Simpson error tests."""
import unittest
from fractions import Fraction as Q
from observational_succ.theta_complex_simpson_bounds import (
    SimpsonBoundError, e3_positive_witness, theta_d4_uniform_majorant,
    simpson_component_bound, theta_t8_analytic_tail,
    original_xi_complex_remainder
)

class ComplexThetaErrorTests(unittest.TestCase):
    def test_e3_rational_positive(self):
        self.assertEqual(e3_positive_witness(),Q(41,4480))

    def test_derivative_4_majorant_strict(self):
        self.assertEqual(theta_d4_uniform_majorant(),Q(8119566336,2395975))
        self.assertLess(theta_d4_uniform_majorant(),3500)

    def test_even_grid_and_monotone(self):
        x=[simpson_component_bound(m) for m in (128,256,512,1024,2048)]
        self.assertTrue(all(a==16*b for a,b in zip(x,x[1:])))

    def test_strict_2048_target_bound(self):
        self.assertLess(original_xi_complex_remainder(2048),Q(1,100000))
        self.assertGreater(original_xi_complex_remainder(2048),0)

    def test_missing_nodes_never_claimed(self):
        for M in (0,1,3,11,-2,512.0):
            with self.assertRaises(SimpsonBoundError):
                original_xi_complex_remainder(M)

    def test_theta_t8_tail_positive(self):
        t=theta_t8_analytic_tail()
        self.assertLess(t,Q(1,10000000000))
        self.assertGreater(t,0)

if __name__=='__main__':
    unittest.main()
