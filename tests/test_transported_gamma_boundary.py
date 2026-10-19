"""Exact form/values distinction for the true Gamma/prime source."""
import unittest
from fractions import Fraction as F
from observational_succ.transported_gamma_boundary import (
    TransportError, exact_rank, finite_boundary_control,
    original_source_transport_contract,
)


class FormTransportVersusValueCommutation(unittest.TestCase):
    def test_independent_sizes_and_rational_exponent_controls(self):
        for n,k in ((9,6),(11,7),(13,9),(15,10),(17,12)):
            for q in (F(1,2),F(2,3)):
                c=finite_boundary_control(n,k,q)
                self.assertTrue(c["unrestricted_form_covariant"])
                self.assertTrue(c["exterior_leakage_identity"])
                self.assertFalse(c["same_window_commuting"])
                self.assertEqual((c["rank_four_boundary"],
                                  c["even_parity_rank"],c["odd_parity_rank"]),
                                 (4,2,2))
    def test_no_false_complete_gamma_or_suzuki_promotion(self):
        c=finite_boundary_control()
        self.assertFalse(c["full_gamma_tower_rank_four_proved"])
        self.assertFalse(c["source_S4_positive_proved"])
        self.assertFalse(c["RH_proved"])

    def test_exact_rank_oracle_against_direct_rational_matrices(self):
        self.assertEqual(exact_rank(((F(1),F(2)),(F(2),F(4)))),1)
        self.assertEqual(exact_rank(((F(1),F(2)),(F(2),F(1)))),2)
        self.assertEqual(exact_rank(((F(0),F(0)),(F(0),F(0)))),0)

    def test_invalid_geometry_parameter_or_kernel_rejected(self):
        for n,k,q in ((8,5,F(1,2)),(13,6,F(1,2)),
                      (13,12,F(1,2)),(13,9,F(0)),(13,9,F(1)),
                      (13,9,F(-1,2)),(13,9,0.5),
                      (True,9,F(1,2)),(13,9,True)):
            with self.assertRaises(TransportError):
                finite_boundary_control(n,k,q)

    def test_original_signed_suzuki_source_hypotheses(self):
        try:
            import observational_succ.tate_suzuki_shorting
        except ImportError:
            self.skipTest("frozen signed Suzuki source unavailable")
        c=original_source_transport_contract()
        self.assertEqual(c["source_git_blob"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(c["prime_wavefront"],((2,2),))
        self.assertEqual(c["single_rung_continuum_boundary_rank"],4)
        self.assertEqual(c["single_rung_each_parity_rank"],2)
        self.assertFalse(c["whole_gamma_tower_rank_four_proved"])


if __name__=="__main__":
    unittest.main()
