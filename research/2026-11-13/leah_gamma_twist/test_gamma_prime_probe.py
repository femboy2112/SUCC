"""Meaningful exact controls declared in GAMMA_PRIME.md before execution."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import unittest

SPEC = importlib.util.spec_from_file_location("leah_gamma_prime_probe", Path(__file__).with_name("gamma_prime_probe.py"))
gp = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gp)


class GammaPrimeControls(unittest.TestCase):
    def test_independent_four_poles_and_combined_formula(self):
        for n in range(1, 129):
            self.assertEqual(gp.forcing(n), gp.combined_forcing(n))

    def test_beta_tail_enclosure_against_independent_series(self):
        for n in range(1, 129):
            lo, hi = gp.tail_beta_interval(n)
            a, b = gp.tail_series_interval(n)
            self.assertLessEqual(lo, a)
            self.assertLessEqual(b, hi)

    def test_declared_fixed_lag_holdouts(self):
        for n in gp.HOLDOUTS:
            for c in gp.stencils():
                data = gp.lag_tail_certificate(n, c)
                self.assertTrue(data["rational_recurrence_identity"])

    def test_polynomial_factorization_and_seed_retention(self):
        for q, c in enumerate(gp.stencils()[:4]):
            order, s = gp.split_one_root(c)
            self.assertEqual((order, s), (q, (-16, 1)))
            self.assertEqual(gp.poly_eval(c, 16), 0)
        self.assertEqual(gp.poly_eval((-1, 1), 16), 15)
        self.assertEqual(gp.poly_eval((1, 0, 1), 16), 257)

    def test_declared_state_energy_branch_and_projection_bounds(self):
        for a in gp.HOLDOUTS:
            data = gp.state_energy_certificate(a, a)
            lo, hi = data["energy_interval"]
            self.assertGreater(lo, 0)
            self.assertLessEqual(lo, hi)
            self.assertLessEqual(hi, data["coherent_energy_upper"])
            self.assertEqual(data["completed_counterseed_energy"], 0)

    def test_frequency_sign_symmetry_and_branch_guard(self):
        self.assertEqual(gp.state_energy_certificate(137, 137, -1)["energy_interval"],
                         gp.state_energy_certificate(137, 137, 1)["energy_interval"])
        with self.assertRaises(ValueError):
            gp.state_energy_certificate(1, 2, 10**6)

    def test_declared_old_cofactor_shadows_and_prime_passports(self):
        for a in gp.OLD_CLOCK_HOLDOUTS:
            data = gp.old_cofactor_shadow(a)
            self.assertTrue(data["seed_is_nonzero_rational"])
            self.assertTrue(data["preserved_newborn_primes"])
            self.assertFalse(data["zero_anchor_preserved"])
            # A radius certificate may honestly be inconclusive at a small A.
            self.assertEqual(data["short_arc_certified"], data["radius_bound"] < Q(1, 4))

    def test_declared_gamma_forcing_clock_vs_accumulated_clock(self):
        for p in gp.PRIME_HOLDOUTS:
            data = gp.prime_gamma_clock(p)
            self.assertEqual(data["forcing_coset_candidates"], 1)
            self.assertGreater(data["state_coset_capacity_on_same_window"], 1)
            self.assertEqual(data["newborn_residue"], 4)
            self.assertTrue(data["full_old_cofactor_reconstruction"])
            self.assertFalse(data["state_is_claimed_inside_forcing_window"])

    def test_half_open_coset_endpoint_convention(self):
        self.assertEqual(gp.coset_count(Q(0), Q(1), Q(0), 1), 1)
        self.assertEqual(gp.coset_count(Q(1, 3), Q(2, 3), Q(1, 3), 3), 1)
        self.assertEqual(gp.coset_count(Q(-2, 3), Q(0), Q(0), 3), 2)
        self.assertEqual(gp.coset_count(Q(0), Q(0), Q(0), 3), 0)

    def test_rational_alias_separates_R0_from_normality(self):
        data = gp.rational_alias_control()
        self.assertGreater(data["R0_gap_interval"][0], 0)
        self.assertEqual(data["frequency_15_energy"], 0)
        self.assertFalse(data["normal"])

    def test_residue_mutation_changes_tail_order_and_fails_authentic_identity(self):
        for n in gp.HOLDOUTS:
            data = gp.mutation_control(n)
            self.assertEqual(data["total_residue"], 1)
            self.assertTrue(data["authentic_identity_rejected"])

    def test_chronological_gamma_product_keeps_required_weights(self):
        for n in (2, 3, 7, 16):
            data = gp.exact_product_control(n)
            self.assertTrue(data["weighted_log_derivative_is_U"])
            self.assertFalse(data["ordinary_gamma_log_derivative_is_U"])

    def test_exact_input_rejection(self):
        for bad in (True, 3.0, "3"):
            with self.assertRaises(ValueError):
                gp.forcing(bad)
            with self.assertRaises(ValueError):
                gp.polynomial((1, bad))
        with self.assertRaises(ValueError):
            gp.polynomial((0, 0))

    def test_outward_decimal_rounding_including_negative_values(self):
        d = gp.decimal_interval(Q(-1, 3), Q(1, 3), 6)
        self.assertEqual((d["lower"], d["upper"]), ("-0.333334", "0.333334"))


if __name__ == "__main__":
    unittest.main()
