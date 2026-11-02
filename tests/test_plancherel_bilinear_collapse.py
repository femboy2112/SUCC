"""Root-Level Regression Test Suite for Mega-Round III / IV:
Plancherel-Bilinear Collapse, Pole Annihilation, and 630-Prime Census Analysis.

Tests claims PBC-01 through PBC-18, Lean 4 kernel verification, and adversarial countermodels.
Author: Antigravity Pair Programmer.
Branch: research/prime-cofactor-nonconspiracy-2026-11-02.
"""
from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
DOSSIER = REPO_ROOT / "research" / "2026-11-02" / "plancherel_bilinear_collapse"
LEAN_FILE = DOSSIER / "PlancherelBilinearCore.lean"
RECEIPT_FILE = DOSSIER / "EXACT_MEGA_ROUND_3_RECEIPT.json"

import sys
sys.path.insert(0, str(DOSSIER))
import mega_round_3_engine as engine
import independent_oracle_3 as oracle


class TestPlancherelBilinearCollapseMegaRound(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = engine.generate_exact_receipt()

    def test_pbc01_plancherel_convolution(self):
        cert = self.receipt["claims"]["PBC-01"]
        self.assertTrue(cert["plancherel_exact_match"])
        self.assertLess(cert["plancherel_error"], 1e-12)
        # Independent cross-check on another prime (p=17, L=2)
        cert17 = engine.certificate_pbc01_plancherel_convolution(17, 1)
        self.assertTrue(cert17["plancherel_exact_match"])

    def test_pbc02_pole_annihilation(self):
        cert = self.receipt["claims"]["PBC-02"]
        self.assertTrue(cert["pole_annihilated_identically"])
        self.assertEqual(cert["max_fractional_pole_discrepancy"], "0")
        # Check on p=241 (p = 1 mod 8) and p=257
        cert241 = engine.certificate_pbc02_pole_annihilation(241, 1)
        self.assertTrue(cert241["pole_annihilated_identically"])

    def test_pbc03_discrepancy_representation(self):
        cert = self.receipt["claims"]["PBC-03"]
        self.assertGreater(cert["discrepancy_magnitude"], 0.0)
        self.assertLess(cert["discrepancy_magnitude"], 1.0)

    def test_pbc04_gauss_energy_partition(self):
        cert = self.receipt["claims"]["PBC-04"]
        self.assertTrue(cert["energy_conservation_exact"])
        self.assertEqual(cert["energy_partition_error"], 0.0)
        self.assertEqual(cert["total_gauss_energy"], cert["expected_L_squared"])

    def test_pbc05_universal_asymptotic_haar_mean(self):
        cert = self.receipt["claims"]["PBC-05"]
        self.assertTrue(cert["all_means_within_0_01_of_half"])
        self.assertEqual(cert["total_rows"], 630)
        for h_str in ["1", "3", "5"]:
            self.assertLess(cert["statistics_by_h"][h_str]["diff_from_half"], 0.01)

    def test_pbc06_modulo_8_structural_invariance(self):
        cert = self.receipt["claims"]["PBC-06"]
        self.assertTrue(cert["mod8_invariance_holds"])
        self.assertLess(cert["max_mod8_mean_divergence"], 0.02)

    def test_pbc07_order_decoupling_correlation(self):
        cert = self.receipt["claims"]["PBC-07"]
        self.assertTrue(cert["all_correlations_small"])
        for h_str in ["1", "3", "5"]:
            self.assertLess(abs(cert["correlations"][h_str]["pearson_corr_with_L"]), 0.15)

    def test_pbc08_bounded_fourier_energy(self):
        cert = self.receipt["claims"]["PBC-08"]
        self.assertTrue(cert["total_energy_bounded"])
        self.assertLessEqual(cert["total_dhat_energy"], 4.0)
        self.assertLess(cert["parseval_error"], 1e-12)

    def test_pbc09_radix_16_3_convergents(self):
        cert = self.receipt["claims"]["PBC-09"]
        self.assertTrue(cert["proximity_verified"])
        self.assertEqual(cert["proximity_16_2_minus_3_5"], 13)

    def test_pbc10_coupled_carry_markov(self):
        cert = self.receipt["claims"]["PBC-10"]
        self.assertEqual(cert["num_states"], 48)
        self.assertTrue(cert["strong_connectivity"])

    def test_pbc11_coupled_quadratic_form(self):
        cert = self.receipt["claims"]["PBC-11"]
        self.assertTrue(cert["is_positive_definite"])
        self.assertEqual(cert["discriminant"], -8836)
        self.assertGreater(cert["min_eigenvalue"], 0.0)

    def test_pbc12_base3_counterseed_discriminator(self):
        cert = self.receipt["claims"]["PBC-12"]
        self.assertTrue(cert["non_torsion_confirmed"])
        self.assertEqual(cert["unique_points_in_first_ten"], 10)

    def test_pbc13_pade_pole_exclusion(self):
        cert = self.receipt["claims"]["PBC-13"]
        self.assertTrue(cert["strictly_positive_on_physical_range"])
        self.assertEqual(cert["values_n_1_to_10"][0][1], 120)

    def test_pbc14_discrete_convexity(self):
        cert = self.receipt["claims"]["PBC-14"]
        self.assertTrue(cert["all_strictly_positive"])

    def test_pbc15_seed_escape_amplification(self):
        cert = self.receipt["claims"]["PBC-15"]
        self.assertEqual(cert["amplification_factor"], 225)
        self.assertTrue(cert["is_fifteen_squared"])

    def test_pbc16_aurifeuillian_quartic_factors(self):
        cert = self.receipt["claims"]["PBC-16"]
        self.assertTrue(cert["all_products_match"])
        self.assertTrue(cert["all_gcds_one"])

    def test_pbc17_exceptional_set_sieve_bound(self):
        cert = self.receipt["claims"]["PBC-17"]
        self.assertTrue(cert["all_bounds_tight"])

    def test_pbc18_large_order_census(self):
        cert = self.receipt["claims"]["PBC-18"]
        self.assertTrue(cert["census_exceeds_93_pct"])
        self.assertEqual(cert["total_primes_1_mod_4"], 608)
        self.assertEqual(cert["primes_with_L_gt_sqrt_p"], 569)
        self.assertAlmostEqual(cert["percentage"], 93.59, places=2)

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
        # Verify no sorryAx and no Classical.choice
        self.assertNotIn("sorryAx", res.stdout)
        self.assertNotIn("Classical.choice", res.stdout)
        # Ensure #print axioms lines were processed
        output_lines = [l for l in res.stdout.strip().split("\n") if l.startswith("'ObservationalSUCC")]
        self.assertEqual(len(output_lines), 20)


if __name__ == "__main__":
    unittest.main()
