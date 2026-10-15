"""Independent exact integer arithmetic checks for Q(i) -> C completion witness."""
import unittest
from fractions import Fraction as F

from observational_succ.complex_cauchy_edge import (
    GaussianCauchyRoot2, sqrt2_is_not_gaussian_rational,
)
from observational_succ.edge_carrier_reconstruction import (
    EdgeCarrierError, RationalSpan, GaussianRational,
)


class ComplexCauchyEdgeTests(unittest.TestCase):
    def test_exact_root2_qi_enclosure_and_no_float(self):
        point=GaussianCauchyRoot2(RationalSpan(1,3))
        previous=None
        for k in range(0,41):
            r=point.stage(k)
            self.assertTrue(r["strict_positive_enclosure"])
            self.assertLess(r["square_lower"],2)
            self.assertGreater(r["square_upper"],2)
            self.assertLess(r["real_upper"]-r["real_lower"],F(2,10**k))
            self.assertEqual(r["imaginary"],F(1,3))
            self.assertEqual(r["q_i_approximation"].as_pair()[0],r["real_lower"])
            self.assertEqual(r["q_i_approximation"].as_pair()[1],F(1,3))
            if previous is not None:
                self.assertGreaterEqual(r["real_lower"],previous)
            previous=r["real_lower"]

    def test_cauchy_proof_at_far_separated_stages(self):
        point=GaussianCauchyRoot2(RationalSpan(-5,7))
        for coarse in range(0,19):
            for fine in (coarse,coarse+1,coarse+2,coarse+20):
                r=point.cauchy_receipt(fine,coarse)
                self.assertTrue(r["cauchy_rate_proved_by_sqrt2_enclosures"])
                self.assertLess(r["exact_difference"],r["guaranteed_error"])
                self.assertFalse(r["limit_in_Q_i"])

    def test_field_is_truly_larger_than_rational_gaussian_coordinates(self):
        r=sqrt2_is_not_gaussian_rational()
        self.assertTrue(r["target_not_in_Q_i"])
        self.assertTrue(r["computable_cauchy_name_exists"])
        self.assertFalse(r["one_name_generates_every_complex_number"])
        # finite-prefix rational approximation is never exact sqrt(2)
        point=GaussianCauchyRoot2(RationalSpan(0))
        for depth in (0,1,3,5,10):
            z=point.stage(depth)["q_i_approximation"].as_pair()[0]
            self.assertNotEqual(z*z,2)

    def test_wrong_depth_and_nonalgebraic_coercion_rejected(self):
        point=GaussianCauchyRoot2(RationalSpan(0))
        for depth in (-1,True,1.5,101):
            with self.assertRaises(EdgeCarrierError):
                point.stage(depth)
        with self.assertRaises(EdgeCarrierError):
            point.cauchy_receipt(1,2)
        with self.assertRaises(EdgeCarrierError):
            GaussianCauchyRoot2(F(1,3))
        with self.assertRaises(EdgeCarrierError):
            GaussianCauchyRoot2(RationalSpan(1),"")


if __name__ == "__main__":
    unittest.main()
