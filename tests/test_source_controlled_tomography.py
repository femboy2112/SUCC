"""Exact tests for source-controlled arithmetic tomography (SCO-01..04)."""
import unittest
from fractions import Fraction as Q
from math import log

from observational_succ import source_controlled_tomography as sct
from observational_succ.reality_pin_arithmetic import arithmetic_matrix_interval


class TestForwardModel(unittest.TestCase):
    def test_named_entries(self):
        for sigma in (2, 3, 4):
            for lam in (1, 2, Q(1, 3)):
                self.assertEqual(sct.k_off_diagonal(2, 3, lam, sigma), Q(lam))
                self.assertEqual(sct.k_off_diagonal(1, 3, lam, sigma), Q(1, 3 ** sigma))
                self.assertEqual(sct.k_off_diagonal(1, 5, lam, sigma), Q(1, 5 ** sigma))

    def test_cross_check_reality_pin_matrix(self):
        # independent second route: the exact off-diagonals of P_n K P_n
        lam, sigma, n = 1, 2, 7
        lower, _ = arithmetic_matrix_interval(n, lam, sigma)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    self.assertEqual(sct.k_off_diagonal(i, j, lam, sigma),
                                     lower[i - 1][j - 1])

    def test_mixed_channel_entry(self):
        # <1|K|2> = lambda (S) + 2^{-sigma} (V_2)
        self.assertEqual(sct.k_off_diagonal(1, 2, 1, 2), Q(1) + Q(1, 4))


class TestSCO01Identification(unittest.TestCase):
    def test_round_trip_float(self):
        for sigma in (2, 3, 4):
            for lam in (1.0, 2.0, 0.5):
                rec = sct.verify_identification_exact(lam, sigma)
                self.assertAlmostEqual(rec.sigma, sigma, places=9)
                self.assertAlmostEqual(rec.lam, lam, places=9)
                self.assertAlmostEqual(rec.gain, 1.0, places=9)

    def test_sigma_interval_contains_truth(self):
        # sigma = 2 exactly: q13 = 1/9, q15 = 1/25, ratio 25/9 = (5/3)^2
        lo, hi = sct.identify_sigma_interval(Q(1, 9), Q(1, 25))
        self.assertLessEqual(lo, 2)
        self.assertLessEqual(2, hi)
        self.assertLess(hi - lo, Q(1, 1000))

    def test_sigma_interval_requires_positive_sigma(self):
        with self.assertRaises(sct.TomographyError):
            sct.identify_sigma_interval(Q(1, 25), Q(1, 9))  # q13 < q15


class TestSCO02Stability(unittest.TestCase):
    def test_bound_dominates_empirical_deviation(self):
        sigma = 3
        q13 = 1 / 3 ** sigma
        q15 = 1 / 5 ** sigma
        for eta in (Q(1, 100), Q(1, 20), Q(1, 10)):
            bound = sct.sigma_error_bound(eta)
            e = float(eta)
            # worst-case: q13 up, q15 down (and the reverse)
            worst = 0.0
            for s13, s15 in ((1 + e, 1 - e), (1 - e, 1 + e)):
                sig = log((q13 * s13) / (q15 * s15)) / log(5 / 3)
                worst = max(worst, abs(sig - sigma))
            self.assertLessEqual(worst, float(bound) + 1e-12)

    def test_zero_error_zero_bound(self):
        self.assertEqual(sct.sigma_error_bound(0), 0)

    def test_gain_cancels(self):
        self.assertTrue(sct.gain_cancels(1 / 9, 1 / 25, scale=7.3))


class TestSCO03Authentication(unittest.TestCase):
    def test_v6_invisible_to_coprime_probes(self):
        self.assertTrue(sct.counterfeit_invisible(6, [(2, 3), (1, 3), (1, 5)]))

    def test_v6_detected_by_its_support(self):
        self.assertFalse(sct.counterfeit_invisible(6, [(1, 6)]))

    def test_minimal_separating_entry(self):
        entry, weight = sct.minimal_separating_entry(6, sigma=2)
        self.assertEqual(entry, (1, 6))
        self.assertEqual(weight, Q(1, 36))

    def test_dirichlet_log_witness(self):
        self.assertEqual(sct.dirichlet_log_witness(1), 0)   # genuine zeta a(6)=1
        self.assertEqual(sct.dirichlet_log_witness(2), 1)   # counterfeit a(6)=2

    def test_open_world_statement_present(self):
        self.assertIn("complexity", sct.no_fixed_probe_set_suffices_open_world())


class TestSCO04Firewall(unittest.TestCase):
    def test_ladder_level1_only(self):
        ladder = sct.access_ladder()
        self.assertEqual(ladder[0][0], 1)
        self.assertTrue(ladder[0][2])                 # level 1 satisfied
        self.assertFalse(any(level[2] for level in ladder[1:]))

    def test_assert_mathematical_only(self):
        self.assertTrue(sct.assert_mathematical_only(1))
        for bad in (2, 3, 4, 5):
            with self.assertRaises(sct.TomographyError):
                sct.assert_mathematical_only(bad)


if __name__ == "__main__":
    unittest.main()
