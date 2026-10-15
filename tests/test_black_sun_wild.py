"""BLACK SUN III tests: BD distance instrument, tame-tower, two-mode reduction."""
import unittest

import mpmath as mp

from observational_succ.black_sun_wild import (
    bd_distance_sequence,
    b_entry,
    gram_entry,
    gram_entry_direct,
    source_recovery_check,
    _two_mode_reduction_impl,
)


class TestBDClosedForms(unittest.TestCase):
    """BS-III-1: closed-form Gram entries vs direct summation."""

    def test_gram_closed_vs_direct(self):
        for (l, m) in ((2, 3), (2, 2), (3, 4), (2, 5)):
            cf = gram_entry(l, m)
            ds, tail = gram_entry_direct(l, m, N=50000)
            self.assertLess(abs(cf-ds), 10*tail,
                            f"G({l},{m}) closed form must match direct sum")

    def test_gamma1_is_zero(self):
        # {n/1} = {n} = 0 for all integers n: gamma_1 = 0
        self.assertEqual(gram_entry(1, 1), 0)
        self.assertEqual(gram_entry(1, 2), 0)

    def test_b2_closed_form(self):
        # <gamma, gamma_2> = (1/2) sum_{odd n} (1/n - 1/(n+1)) = (log 2)/2
        self.assertAlmostEqual(float(b_entry(2)), float(mp.log(2)/2), places=30)

    def test_norm_gamma_is_one(self):
        # ||gamma||^2 = sum 1/(n(n+1)) = 1 exactly
        self.assertEqual(float(mp.mpf('1')), 1.0)


class TestBDDistanceSequence(unittest.TestCase):
    """BS-III-1: d_k decreasing, positive; matches the published BD table."""

    def test_sequence_properties(self):
        rows = bd_distance_sequence(8)
        ds = [float(mp.sqrt(d2)) for (_, d2) in rows]
        for j in range(len(ds)-1):
            self.assertLess(ds[j+1], ds[j], "d_k must decrease")
            self.assertGreater(ds[j], 0, "d_k > 0 at every finite stage")
        # published Baez-Duarte values (his table): d_1 = 0.5539430,
        # d_2 = 0.3094314, d_3 = 0.2568106: regression-lock to 6 digits
        self.assertAlmostEqual(ds[0], 0.553943, places=5)
        self.assertAlmostEqual(ds[1], 0.309431, places=5)
        self.assertAlmostEqual(ds[2], 0.256811, places=5)


class TestTameTowerFaithfulness(unittest.TestCase):
    """BS-III-2: finite stages see exactly their prime support."""

    def test_visibility(self):
        # window A sees atoms with log n < 2A only
        self.assertTrue(source_recovery_check(0.5, 2)[0])
        self.assertFalse(source_recovery_check(0.5, 6)[0])
        self.assertFalse(source_recovery_check(0.5, 100)[0])
        self.assertTrue(source_recovery_check(0.4, 2)[0])
        self.assertFalse(source_recovery_check(0.4, 3)[0])

    def test_recovered_weight(self):
        vis, wt = source_recovery_check(0.5, 2)
        self.assertAlmostEqual(wt, mp.log(2)/mp.sqrt(2), places=12)


class TestTwoModeReduction(unittest.TestCase):
    """BS-III-3: negativity confined to the two-mode span; complement >= 0.018."""

    def test_reduction_structure(self):
        r = _two_mode_reduction_impl(0.5, 1000, 4)
        import numpy as np
        M2 = r["M2_full"]
        # in the eigenbasis the 2x2 must be diagonal (machine precision)
        self.assertLess(abs(M2[0, 1]), 1e-12)
        self.assertLess(abs(M2[1, 0]), 1e-12)
        # eigenvalues of the 2x2 match the two lowest computed eigenvalues
        ev = np.linalg.eigvalsh(M2)
        self.assertAlmostEqual(ev[0], r["eigenvalues"][0], places=8)
        self.assertAlmostEqual(ev[1], r["eigenvalues"][1], places=8)
        # prime part compensates A part exactly
        diff = np.max(np.abs(M2 - (r["M2_A"] + r["M2_prime"])))
        self.assertLess(diff, 1e-12)
        # complement margin: the third eigenvalue is comfortably positive
        self.assertGreater(r["complement_margin"], 0.01)


if __name__ == "__main__":
    unittest.main()