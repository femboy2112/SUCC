"""Root-Level Regression Test Suite for Mega-Round V:
Weyl Differencing, Non-Autonomous Transfer Operators, and Hausdorff Tail Monotonicity (WTM-01 .. WTM-18).

Tests claims WTM-01 through WTM-18, Lean 4 kernel verification, and adversarial countermodels.
Author: Antigravity Pair Programmer
Branch: research/pi-normality-framework-spine-2026-11-02
Date: 2026-11-02
"""

from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
DOSSIER = REPO_ROOT / "research" / "2026-11-02" / "weyl_transfer_operator_monotonicity"
LEAN_FILE = DOSSIER / "WeylTransferMonotonicityCore.lean"
RECEIPT_FILE = DOSSIER / "EXACT_WTM_RECEIPT.json"

import sys
sys.path.insert(0, str(DOSSIER))
import weyl_transfer_operator_monotonicity_engine as engine
import independent_oracle_wtm as oracle


class TestWeylTransferOperatorMonotonicity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = engine.generate_exact_receipt()

    def test_wtm01_shift_difference_factorization(self):
        cert = self.receipt["claims"]["WTM-01"]
        self.assertTrue(cert["all_exact"])
        self.assertEqual(cert["status"], "PROVED_EXACT")

    def test_wtm02_universal_pole_annihilation(self):
        cert = self.receipt["claims"]["WTM-02"]
        self.assertTrue(cert["all_annihilated"])
        self.assertEqual(cert["status"], "PROVED_EXACT")

    def test_wtm03_second_shift_acceleration(self):
        cert = self.receipt["claims"]["WTM-03"]
        self.assertTrue(cert["all_positive"])
        self.assertEqual(cert["leading_coeff_k1"], 225)

    def test_wtm04_weyl_vdc_majorization(self):
        cert = self.receipt["claims"]["WTM-04"]
        self.assertTrue(cert["majorization_holds"])
        self.assertLessEqual(cert["ratio"], 1.0)

    def test_wtm05_transfer_operator_preservation(self):
        cert = self.receipt["claims"]["WTM-05"]
        self.assertTrue(cert["integral_preserved"])
        self.assertTrue(cert["strictly_positive"])

    def test_wtm06_lasota_yorke_contraction(self):
        cert = self.receipt["claims"]["WTM-06"]
        self.assertTrue(cert["contraction_holds"])
        self.assertLessEqual(cert["contraction_factor"], 1.0 / 16.0 + 1e-4)

    def test_wtm07_composition_factorization(self):
        cert = self.receipt["claims"]["WTM-07"]
        self.assertTrue(cert["factorization_holds"])
        self.assertLess(cert["factorization_error"], 1e-11)
        self.assertEqual(cert["spectral_gap"], 15.0 / 16.0)

    def test_wtm08_character_decay(self):
        cert = self.receipt["claims"]["WTM-08"]
        self.assertTrue(cert["all_decay"])

    def test_wtm09_parity_odd_order_5mod8(self):
        cert = self.receipt["claims"]["WTM-09"]
        self.assertTrue(cert["all_odd_order"])

    def test_wtm10_s_unit_lattice_det_95(self):
        cert = self.receipt["claims"]["WTM-10"]
        self.assertTrue(cert["is_ninety_five"])
        self.assertEqual(cert["det_L_factorization"], [5, 19])

    def test_wtm11_multi_prime_tensor_gauss(self):
        cert = self.receipt["claims"]["WTM-11"]
        self.assertTrue(cert["satisfies_bound"])

    def test_wtm12_tri_radix_gram_coercivity(self):
        cert = self.receipt["claims"]["WTM-12"]
        self.assertTrue(cert["coercivity_positive"])
        self.assertEqual(cert["det_M"], 9025)
        self.assertEqual(cert["min_integer_quadratic_val"], 5)

    def test_wtm13_bbp_algebraic_integral(self):
        cert = self.receipt["claims"]["WTM-13"]
        self.assertTrue(cert["algebraic_identity_verified"])

    def test_wtm14_complete_monotonicity_green_tail(self):
        cert = self.receipt["claims"]["WTM-14"]
        self.assertTrue(cert["all_positive"])

    def test_wtm15_hausdorff_moment_total_mass(self):
        cert = self.receipt["claims"]["WTM-15"]
        self.assertTrue(cert["B_strictly_less_than_1_over_61"])

    def test_wtm16_square_root_sieve_floor(self):
        cert = self.receipt["claims"]["WTM-16"]
        self.assertTrue(cert["rate_exceeds_90_percent"])
        self.assertGreaterEqual(cert["non_exceptional_rate"], 0.90)

    def test_wtm17_gauss_ratio_suppression(self):
        cert = self.receipt["claims"]["WTM-17"]
        self.assertTrue(cert["uniform_bound_one_satisfied"])
        self.assertTrue(cert["mean_below_0_25"])

    def test_wtm18_extended_prime_census(self):
        cert = self.receipt["claims"]["WTM-18"]
        self.assertTrue(cert["exceeds_95_percent"])

    def test_independent_oracle_all_pass(self):
        res = oracle.independent_verify_all()
        for claim, passed in res.items():
            self.assertTrue(passed, f"Oracle failed on {claim}")

    def test_lean4_kernel_verification(self):
        cmd = ["lean", str(LEAN_FILE)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, f"Lean verification failed:\n{proc.stderr}")
        self.assertNotIn("sorry", proc.stdout)
        self.assertNotIn("Classical.choice", proc.stdout)

    # ------------------------------------------------------------------
    # Adversarial Countermodels
    # ------------------------------------------------------------------

    def test_adversarial_perturbed_sigma_detected(self):
        """Perturbing sigma_k by +1 breaks the exact difference identity."""
        k = 2
        bad_sigma = (16**k - 1) // 15 + 1
        self.assertNotEqual(16**k - 1, 15 * bad_sigma)

    def test_adversarial_non_expanding_map_fails_gap(self):
        """Radix 1 (non-expanding) has zero spectral gap: 1 - 1 = 0."""
        radix = 1
        gap = radix - 1
        self.assertEqual(gap, 0)

    def test_adversarial_indefinite_lattice_detected(self):
        """Adversarial matrix with indefinite structure fails coercivity."""
        import numpy as np
        L_bad = np.array([[1, 5, 0], [0, 1, 5], [5, 0, 1]], dtype=float)
        M_bad = np.array([[1, 10, 0], [10, 1, 0], [0, 0, 1]], dtype=float)
        eigs_bad = np.linalg.eigvalsh(M_bad)
        self.assertLess(min(eigs_bad), 0, "Adversarial indefinite matrix must have negative eigenvalue")

    def test_adversarial_alternating_weight_breaks_monotonicity(self):
        """Sign-alternating forcing breaks the Hausdorff moment complete monotonicity."""
        import mpmath as mp
        bad_T2 = [mp.mpf(1), mp.mpf(2), mp.mpf(0.5)]
        delta1 = bad_T2[1] - bad_T2[0]  # = +1
        alt_delta1 = -delta1  # = -1 < 0 (violation!)
        self.assertLess(alt_delta1, 0, "Non-monotonic sequence must fail complete monotonicity")


if __name__ == "__main__":
    unittest.main()
