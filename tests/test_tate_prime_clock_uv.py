"""Exact and adversarial tests for Tate × APOLLO prime clock UV transducer."""
import unittest
from fractions import Fraction as F

from observational_succ.tate_prime_clock_uv import (
    PrimeClockGateError, shift_path_geometry, exact_two_cell_negative_witness,
    gamma_sparse_lower, genuine_first_prime_sparse_weil_certificate,
    mutated_source_budget,
)
from observational_succ.apollo_krein_factor import (
    brownian_increment_kernel, prime_hinge_kernel,
)


class SharpPrimePathTheorem(unittest.TestCase):
    def test_inactive_boundary_and_activated_two_cell_path(self):
        self.assertEqual(shift_path_geometry(F(1, 2), F(1))[
            "maximum_essential_chain_vertices"], 1)
        for a, b in ((F(1, 2), F(3, 4)), (F(3, 4), F(1))):
            c = shift_path_geometry(a, b)
            self.assertEqual(c["maximum_essential_chain_vertices"], 2)
            self.assertTrue(c["prime_active"])
            self.assertEqual(c["sharp_norm_rational"], 1)
        self.assertEqual(shift_path_geometry(F(5, 4), F(1))[
            "maximum_essential_chain_vertices"], 3)

    def test_rational_negative_path_witness_is_exact_and_attains_bound(self):
        for a, b, weight in (
            (F(1, 2), F(3, 4), F(1)),
            (F(1), F(3, 2), F(1, 3)),
            (F(3, 4), F(1), F(5, 7)),
        ):
            w = exact_two_cell_negative_witness(a, b, weight)
            self.assertEqual(w["brownian_energy"], 2*w["cell_length"])
            self.assertEqual(w["sharp_relative_negative"], -weight)
            self.assertLess(w["original_shape_prime_signed_energy"], 0)
            self.assertTrue(w["synthetic_clock_not_genuine_prime"])
            self.assertFalse(w["RH_proved"])

    def test_first_activation_kernel_itself_is_indefinite(self):
        a, b = F(1, 2), F(3, 4)
        self.assertEqual(prime_hinge_kernel(a, a, b), 0)
        self.assertEqual(prime_hinge_kernel(-a, -a, b), 0)
        self.assertEqual(prime_hinge_kernel(a, -a, b), F(1, 4))
        self.assertEqual(brownian_increment_kernel(a, -a), 0)
        # Signed 2x2 kernel [[0,1/4],[1/4,0]] has eigenvalues +/-1/4.
        self.assertEqual(prime_hinge_kernel(a, -a, b), F(1, 4))

    def test_clock_domain_mutations_fail(self):
        for a, b in ((0,1), (-1,1), (1,0), (True,1),
                     (1,0.75), (F(1, 2), F(2))):
            with self.assertRaises(PrimeClockGateError):
                exact_two_cell_negative_witness(a,b)
        for a,b in ((0,1), (-1,1), (1,0), (True,1), (1,0.5)):
            with self.assertRaises(PrimeClockGateError):
                shift_path_geometry(a,b)


class AuthenticTateGammaUV(unittest.TestCase):
    def test_support_gamma_budget_is_exact_rational_and_infinite_tail_positive(self):
        z = gamma_sparse_lower(16, F(1, 1 << 17))
        self.assertEqual(z["gamma_modes_used"], 65536)
        self.assertEqual(z["gamma_energy_strictly_above"], 6)
        self.assertLess(z["max_schur_ratio"], F(1,2))
        self.assertTrue(z["uncomputed_infinite_gamma_tail_is_positive"])
        self.assertTrue(z["all_smooth_tests_on_any_measurable_support_of_this_size"])
        self.assertFalse(z["RH_proved"])

    def test_gamma_clock_precision_is_not_optional(self):
        for k, mu in ((0, F(1,8)), (True,F(1,8)), (16,F(1,100)),
                      (16,0), (16,0.001), (129,F(1,10**40))):
            with self.assertRaises(PrimeClockGateError):
                gamma_sparse_lower(k,mu)
        self.assertEqual(gamma_sparse_lower(2,F(1,8))[
            "gamma_energy_strictly_above"], F(4,3))

    def test_original_first_prime_window_is_source_authenticated(self):
        c = genuine_first_prime_sparse_weil_certificate()
        self.assertEqual(c["source"], "SHA_PINNED_ORIGINAL_ZETA")
        self.assertEqual(c["actual_prime_power_labels"], (2,))
        self.assertTrue(c["prime_active_at_radius_half"])
        self.assertEqual(c["gamma_clock_modes"], 1<<16)
        self.assertEqual(c["gamma_strict_lower"], 6)
        self.assertEqual(c["completed_real_contact_strict_upper"], F(43,8))
        self.assertEqual(c["first_prime_shift_strict_upper"], F(1,2))
        self.assertEqual(c["negative_pole_strict_upper"], F(1,16))
        self.assertEqual(c["original_completed_Weil_L2_margin_strictly_above"], F(1,16))
        self.assertFalse(c["all_tests_at_radius_half_proved"])
        self.assertFalse(c["all_a_positivity_proved"])
        self.assertFalse(c["RH_proved"])

    def test_uniform_subwindows_and_monotone_support_budget(self):
        for a in (F(1,24), F(1,12), F(1,3), F(1,2)):
            c = genuine_first_prime_sparse_weil_certificate(a, F(1,1<<18))
            self.assertGreaterEqual(c["original_completed_Weil_L2_margin_strictly_above"], F(1,16))
            self.assertTrue(set(c["actual_prime_power_labels"]).issubset({2}))

    def test_source_spoofing_and_unjustified_support_promotion_rejected(self):
        for a,mu in ((F(3,4),F(1,1<<17)),(F(1,2),F(1,100)),
                     (True,F(1,1<<17)),(F(1,2),0),
                     (F(1,2),0.001)):
            with self.assertRaises(PrimeClockGateError):
                genuine_first_prime_sparse_weil_certificate(a,mu)

    def test_fake_source_modifications_withdraw_positive_certificate(self):
        for delta_c, delta_w in ((F(1,2),0),(0,F(1)),
                                 (F(1,16),F(1,16))):
            mutant = mutated_source_budget(delta_c, delta_w)
            self.assertTrue(mutant["negative_mutation_detected"])
            self.assertFalse(mutant["authentic_source"])
            self.assertFalse(mutant["RH_proved"])
        self.assertEqual(mutated_source_budget()["mutant_margin_from_same_conservative_budget"],
                         F(1,16))
        with self.assertRaises(PrimeClockGateError):
            mutated_source_budget(0,0.1)


if __name__ == "__main__":
    unittest.main()
