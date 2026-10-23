"""Exact tests for minimum future-sufficient information (FSO-01, FSO-03, FSO-04)."""
import unittest
from math import log2

from observational_succ import future_sufficient_information as fsi


class TestFSO01(unittest.TestCase):
    def test_closed_form_matches_scan(self):
        for p in range(2, 9):
            for x in range(1, 40):
                for y in range(1, 40):
                    self.assertEqual(fsi.min_separation(x, y, p),
                                     fsi.min_separation_scan(x, y, p))

    def test_sharp_witness_is_p_minus_one(self):
        for p in range(2, 12):
            x, y, length = fsi.sharp_witness(p)
            self.assertEqual((x, y), (1, 2))
            self.assertEqual(length, p - 1)

    def test_identity_collapse_and_sharpness(self):
        for p in range(2, 9):
            cert = fsi.fso01_certificate(p, N=4 * p + 3)
            self.assertTrue(cert.all_distinct_separated)
            self.assertTrue(cert.closed_form_matches_scan)
            self.assertEqual(cert.sharp_bound, p - 1)
            self.assertEqual(cert.max_length_observed, p - 1)
            self.assertEqual(cert.witness_pair, (1, 2))

    def test_different_blocks_separate_at_zero(self):
        # n=2 (block 1) vs n=p+1 (block 2) for p>=2 differ immediately
        for p in range(2, 8):
            self.assertEqual(fsi.min_separation(2, p + 1, p), 0)

    def test_same_value_is_none(self):
        self.assertIsNone(fsi.min_separation(7, 7, 3))


class TestFSO03Certificate(unittest.TestCase):
    def test_minimizer_cross_check_identity(self):
        for p in (2, 3, 5):
            n_blocks, singletons = fsi.confirm_identity_via_minimizer(p, N=4 * p)
            self.assertTrue(singletons)
            self.assertEqual(n_blocks, 4 * p)

    def test_certificate_structure(self):
        cert = fsi.fso03_certificate(5)
        self.assertEqual(cert["available_actions"], ("S",))
        self.assertEqual(cert["refined_future_safe_equivalence"], "identity on N_{>=1}")
        self.assertIn("residue register", cert["retained_information"])
        self.assertEqual(cert["retention_cost_states"], 5)
        self.assertAlmostEqual(cert["retention_cost_bits"], log2(5))
        self.assertEqual(cert["sharp_distinguishing_bound"], 4)
        self.assertEqual(cert["shortest_distinguishing_word"]["length"], 4)
        self.assertEqual(cert["shortest_distinguishing_word"]["pair"], (1, 2))


class TestFSO04ToolkitControls(unittest.TestCase):
    def test_no_action_keeps_quotient_equality(self):
        part = fsi.toolkit_partition(5, N=10, horizon=0)
        self.assertTrue(part.is_quotient_equality)
        self.assertFalse(part.is_identity)
        self.assertEqual(len(part.blocks), 2)        # two quotient blocks

    def test_unrestricted_horizon_gives_identity(self):
        part = fsi.toolkit_partition(5, N=10, horizon=4)   # p-1
        self.assertTrue(part.is_identity)
        self.assertEqual(len(part.blocks), 10)

    def test_intermediate_horizon_strictly_between(self):
        part = fsi.toolkit_partition(5, N=10, horizon=2)
        self.assertFalse(part.is_identity)
        self.assertFalse(part.is_quotient_equality)
        # block 1 {1,2,3,4,5} (residues 0..4) splits as {0,1,2},{3},{4}
        block1 = {b for b in part.blocks if 1 in b}.pop()
        self.assertEqual(block1, (1, 2, 3))
        self.assertEqual(len(part.blocks), 6)        # 3 classes per block x 2

    def test_spectrum_grows_with_toolkit(self):
        spec = fsi.toolkit_spectrum(5, N=10)
        self.assertEqual(len(spec[0].blocks), 2)     # horizon 0
        self.assertEqual(len(spec[1].blocks), 4)     # horizon 1: each block -> {0,1,2,3},{4}
        self.assertEqual(len(spec[4].blocks), 10)    # identity
        # monotone refinement: block count non-decreasing in the toolkit power
        self.assertLessEqual(len(spec[0].blocks), len(spec[1].blocks))
        self.assertLessEqual(len(spec[1].blocks), len(spec[4].blocks))

    def test_p2_spectrum(self):
        spec = fsi.toolkit_spectrum(2, N=8)
        self.assertEqual(set(spec), {0, 1})
        self.assertTrue(spec[0].is_quotient_equality)
        self.assertTrue(spec[1].is_identity)


if __name__ == "__main__":
    unittest.main()
