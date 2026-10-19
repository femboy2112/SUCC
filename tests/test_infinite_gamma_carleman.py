"""Exact rational infinite Gamma tower controls and frozen original-source tests."""
import unittest
from fractions import Fraction as F
from observational_succ.infinite_gamma_carleman import (
    GammaTowerError, alpha, finite_geometric, gamma_spacing_coefficient,
    exp_negative_interval, analytic_gamma_kernel_window,
    dyadic_nonnorm_witness, sqrt_lower, h01_tail_bound,
    original_source_infinite_gamma_contract, comparison_prime_threshold_packet,
    lawful_tent_domain_obstruction,
)


class ExactOriginalGammaTower(unittest.TestCase):
    def test_actual_real_gamma_spacing_not_fake_rung_density(self):
        self.assertEqual([alpha(j) for j in range(5)],
                         [F(1,2),F(5,2),F(9,2),F(13,2),F(17,2)])
        self.assertEqual(gamma_spacing_coefficient(2),F(1,2))
        self.assertEqual(alpha(12)-alpha(11),2)
        self.assertNotEqual(gamma_spacing_coefficient(4),F(1,2))

    def test_direct_finite_geometric_against_closed_formula(self):
        for q in (F(1,2),F(2,3),F(31,32),F(7,13)):
            for n in (0,1,2,3,8,32,64):
                self.assertTrue(finite_geometric(q,n)["exact_equal"])

    def test_original_infinite_series_against_independent_finite_rungs(self):
        for J,s in ((1,F(1,4)),(4,F(1,16)),(8,F(1,32)),
                    (16,F(1,64)),(64,F(1,256))):
            r=analytic_gamma_kernel_window(s,J)
            self.assertLess(F(r["infinite_exact_series_lower"]),
                            F(r["infinite_exact_series_upper"]))
            self.assertGreater(F(r["tail_lower"]),0)
            self.assertGreaterEqual(F(r["infinite_exact_series_lower"]),
                                    F(1,2)/s-F(1,4))
            self.assertLessEqual(F(r["infinite_exact_series_upper"]),
                                 F(1,2)/s+1)
        lo,hi=exp_negative_interval(F(1,8))
        self.assertTrue(0<lo<hi<1)

    def test_uniform_nonnorm_convergence_counterpacket(self):
        for J in (1,2,8,16,64,189,1024,10**6):
            w=dyadic_nonnorm_witness(J)
            self.assertGreaterEqual(F(w["tail_cross_block_lower"]),F(3,32))
            self.assertLess(2*F(w["corner_interval_delta"]),F(1,4))
            self.assertTrue(w["operator_norm_convergence_refuted"])
            self.assertFalse(w["RH_proved"])

    def test_comparison_prime_threshold_noncompact_jump(self):
        for b in (F(3,4),F(999,1000),F(999999,1000000)):
            for J in (8,64,189):
                w=comparison_prime_threshold_packet(b,J)
                self.assertTrue(w["nontrivial_edges"])
                self.assertGreaterEqual(F(w["nonnorm_rational_floor"]),F(3,32))
                self.assertEqual(w["limit_boundary_essential_norm"],
                                 "pi/2 (PAPER theorem)")
                self.assertTrue(w["comparison_not_original_log2"])
        for b in (F(1),F(11,10),F(5,4)):
            w=comparison_prime_threshold_packet(b,64)
            self.assertFalse(w["nontrivial_edges"])
            self.assertEqual(w["limit_boundary_essential_norm"],"0")
            self.assertTrue(w["compressed_prime_shift_zero"])
        with self.assertRaises(GammaTowerError):
            comparison_prime_threshold_packet(F(1,2),64)

    def test_rational_sqrt_bounds_and_H01_rate(self):
        for q in (F(1,2),F(7,5),F(128),F(757,2)):
            self.assertLessEqual(sqrt_lower(q)**2,q)
        n=(8,16,64,128,189,512,1024)
        rates=[F(h01_tail_bound(J)["two_sided_H01_commutator_error_upper"])
               for J in n]
        self.assertEqual(rates,sorted(rates,reverse=True))
        self.assertLess(rates[-1],rates[0])
        self.assertFalse(h01_tail_bound(64)["source_S4_positive_proved"])

    def test_bad_geometry_and_fake_numerics_rejected(self):
        for bad in (True,0,-2,2.3,"9"):
            with self.assertRaises(GammaTowerError):
                dyadic_nonnorm_witness(bad)
        for bad in (1.0,True,F(0),F(1),F(-1,2)):
            with self.assertRaises(GammaTowerError):
                finite_geometric(bad,3)
        for bad in (F(-1), F(2), 1.5, True):
            with self.assertRaises(GammaTowerError):
                exp_negative_interval(bad)
        with self.assertRaises(GammaTowerError):
            analytic_gamma_kernel_window(F(1,2),64)
        for bad in (0,True,0.5,-3):
            with self.assertRaises(GammaTowerError):
                h01_tail_bound(bad)

    def test_lawful_H01_high_modes_refute_K_relative_shortcut(self):
        for n in (3,8,32,128,4096):
            z=lawful_tent_domain_obstruction(n)
            self.assertEqual(F(z["derivative_to_L2_ratio_squared"]),3*n*n)
            self.assertTrue(z["uniform_H01_to_L2_inverse_control_refuted"])
            self.assertFalse(z["RH_proved"])
        with self.assertRaises(GammaTowerError):
            lawful_tent_domain_obstruction(2)

    def test_original_signed_source_SHA_genuine_prime_and_gamma(self):
        try:
            import observational_succ.tate_suzuki_shorting
        except ImportError:
            self.skipTest("frozen source absent; hosted CI must not skip")
        x=original_source_infinite_gamma_contract()
        self.assertEqual(x["source_git_blob"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(x["true_prime_power"],((2,2),))
        self.assertEqual(x["true_alpha_j"],"(4j+1)/2")
        self.assertFalse(x["source_S4_positive_proved"])
        self.assertFalse(x["RH_proved"])


if __name__=="__main__":
    unittest.main()
