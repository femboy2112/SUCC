"""Root-Level Regression Test Suite for Pi Normality Framework Spine (PNS-01 .. PNS-18).

Tests claims PNS-01 through PNS-18, Lean 4 kernel verification, and adversarial countermodels.
Author: Antigravity Pair Programmer.
Branch: research/pi-normality-framework-spine-2026-11-02.
"""
from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
DOSSIER = REPO_ROOT / "research" / "2026-11-02" / "pi_normality_framework_spine"
LEAN_FILE = DOSSIER / "PiNormalitySpineCore.lean"
RECEIPT_FILE = DOSSIER / "EXACT_SPINE_RECEIPT.json"

import sys
sys.path.insert(0, str(DOSSIER))
import pi_normality_spine_engine as engine
import independent_oracle_spine as oracle


class TestPiNormalityFrameworkSpineMegaRound(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = engine.generate_exact_receipt()

    def test_pns01_two_prime_plancherel(self):
        cert = self.receipt["claims"]["PNS-01"]
        self.assertTrue(cert["exact_match"])
        self.assertLess(cert["plancherel_error"], 1e-12)

    def test_pns02_two_prime_pole_annihilation(self):
        cert = self.receipt["claims"]["PNS-02"]
        self.assertTrue(cert["both_poles_annihilated"])
        self.assertEqual(cert["max_fractional_discrepancy"], "0")

    def test_pns03_coprime_order_gauss_factorization(self):
        cert = self.receipt["claims"]["PNS-03"]
        self.assertTrue(cert["factors_identically"])
        self.assertTrue(cert["satisfies_sqrt_bound"])
        self.assertLess(cert["factorization_error"], 1e-12)

    def test_pns04_non_coprime_index_bound(self):
        cert = self.receipt["claims"]["PNS-04"]
        self.assertTrue(cert["satisfies_index_bound"])
        self.assertLessEqual(cert["G_pq_norm"], cert["bound_d_sqrt_pq"])

    def test_pns05_hex_to_binary_cocycle(self):
        cert = self.receipt["claims"]["PNS-05"]
        self.assertTrue(cert["all_reconstructed"])
        self.assertEqual(cert["checks_count"], 12)

    def test_pns06_walsh_nilpotent_shift(self):
        cert = self.receipt["claims"]["PNS-06"]
        self.assertTrue(cert["all_zero"])
        self.assertEqual(cert["index_of_nilpotence"], 4)

    def test_pns07_carry_correlation_decay(self):
        cert = self.receipt["claims"]["PNS-07"]
        self.assertTrue(cert["bounded_correlation"])
        self.assertEqual(len(cert["lag_correlations"]), 4)

    def test_pns08_centered_spill_variance(self):
        cert = self.receipt["claims"]["PNS-08"]
        self.assertTrue(cert["reduction_is_two"])
        self.assertEqual(cert["variance_reduction_ratio"], 2.0)

    def test_pns09_tri_radix_lagrange(self):
        cert = self.receipt["claims"]["PNS-09"]
        self.assertTrue(cert["is_ninety_five_squared"])
        self.assertTrue(cert["det_strictly_positive"])
        self.assertEqual(cert["det_M"], 9025)

    def test_pns10_tri_radix_spectrum(self):
        cert = self.receipt["claims"]["PNS-10"]
        self.assertTrue(cert["all_strictly_positive"])
        self.assertGreater(cert["min_eigenvalue"], 3.0)

    def test_pns11_tri_radix_incommensurability(self):
        cert = self.receipt["claims"]["PNS-11"]
        self.assertTrue(cert["is_coprime"])
        self.assertEqual(cert["gcd_15_2_1"], 1)

    def test_pns12_baker_effective_bound(self):
        cert = self.receipt["claims"]["PNS-12"]
        self.assertTrue(cert["strictly_positive"])
        self.assertGreater(cert["minimum_log_gap_n_lt_20"], 0.0)

    def test_pns13_pade_two_two_denominator(self):
        cert = self.receipt["claims"]["PNS-13"]
        self.assertTrue(cert["at_n_1_is_119_squared"])
        self.assertTrue(cert["all_strictly_positive"])
        self.assertEqual(cert["at_n_1"], 14161)

    def test_pns14_third_difference_bbp_orbit(self):
        cert = self.receipt["claims"]["PNS-14"]
        self.assertTrue(cert["all_strictly_positive"])
        self.assertTrue(cert["lead_is_15_cubed"])
        self.assertEqual(cert["lead_coefficient"], 3375)

    def test_pns15_counterseed_distance_divergence(self):
        cert = self.receipt["claims"]["PNS-15"]
        self.assertTrue(cert["strictly_growing"])
        self.assertEqual(cert["amplification_rates_k_1_to_5"], [15, 225, 3375, 50625, 759375])

    def test_pns16_aurifeuillian_quartic_splitting(self):
        cert = self.receipt["claims"]["PNS-16"]
        self.assertTrue(cert["all_products_match"])
        self.assertTrue(cert["all_gcds_one"])

    def test_pns17_exceptional_sieve_orders(self):
        cert = self.receipt["claims"]["PNS-17"]
        self.assertTrue(cert["all_tight"])

    def test_pns18_large_order_census_20k(self):
        cert = self.receipt["claims"]["PNS-18"]
        self.assertTrue(cert["census_exceeds_94_pct"])
        self.assertGreater(cert["total_primes_1_mod_4"], 1000)
        self.assertGreater(cert["primes_L_gt_sqrt_p"], 1000)

    def test_saved_receipt_and_oracle_validation(self):
        self.assertTrue(RECEIPT_FILE.exists())
        ok = oracle.check_receipt(RECEIPT_FILE)
        self.assertTrue(ok)

    def test_adversarial_countermodels(self):
        adv = oracle.run_adversarial_countermodels()
        for name, passed in adv.items():
            self.assertTrue(passed, f"Countermodel {name} failed")

    def test_lean4_kernel_verification(self):
        self.assertTrue(LEAN_FILE.exists())
        cmd = ["/usr/bin/lean", str(LEAN_FILE)]
        res = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, f"Lean compile failed: {res.stderr}")
        self.assertNotIn("sorryAx", res.stdout)
        self.assertNotIn("Classical.choice", res.stdout)
        output_lines = [l for l in res.stdout.strip().split("\n") if l.startswith("'ObservationalSUCC")]
        self.assertEqual(len(output_lines), 18)


if __name__ == "__main__":
    unittest.main()
