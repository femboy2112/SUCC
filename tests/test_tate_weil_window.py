"""Exact, source-specific finite-support Weil-wavefront test contracts."""
import unittest
from fractions import Fraction as F

from observational_succ.tate_weil_window import (
    CompactWeilSourceWindow, WeilWindowError, support_cofinality_receipt,
    invisible_prime_window,
)
from observational_succ.completed_weil_transport import von_mangoldt_labels


class SourceWindowTests(unittest.TestCase):
    def test_exact_integer_cutoff_and_true_prime_powers(self):
        for a,L,N in ((F(1, 10),1,3), (F(1, 2),1,3),
                      (F(3, 4),2,9), (F(1),2,9),
                      (F(5, 4),3,27), (F(3, 2),3,27),
                      (F(2),4,81), (F(5, 2),5,243)):
            r = CompactWeilSourceWindow(a).certificate()
            self.assertEqual(r["ceil_2a"], L)
            self.assertEqual(r["strict_integer_cutoff"], N)
            self.assertEqual(r["included_genuine_prime_power_labels"],
                             von_mangoldt_labels(N-1))
            self.assertTrue(r["support_bounded_without_exp_floats"])
            self.assertFalse(r["full_Weil_form_proved_PSD"])

    def test_fake_composite_six_rejected_even_when_below_cutoff(self):
        r = CompactWeilSourceWindow(1).certificate()
        values = [n for n,p in r["included_genuine_prime_power_labels"]]
        self.assertIn(2, values)
        self.assertIn(3, values)
        self.assertIn(4, values)
        self.assertIn(5, values)
        self.assertIn(7, values)
        self.assertIn(8, values)
        self.assertNotIn(6, values)
        self.assertEqual(r["source_specific"],
                         "actual von Mangoldt coefficients; no fake 6")

    def test_compact_window_cannot_read_late_true_prime(self):
        cases = ((F(1, 2),3), (F(1),11), (F(3, 2),29),
                 (F(2),83), (F(5, 2),251))
        for a,p in cases:
            r = invisible_prime_window(p,a)
            self.assertTrue(r["outside_compact_source_window_proved"])
            self.assertGreaterEqual(p,r["integer_cutoff"])
        # Nearer prime is not automatically declared invisible from a
        # sufficient conservative bound; returning False is UNKNOWN.
        self.assertFalse(invisible_prime_window(5, 1)["outside_compact_source_window_proved"])

    def test_support_exhaustion_remains_infinite_proof_obligation(self):
        for k in (1, 2, 10, 100, 1000):
            r = support_cofinality_receipt(k)
            self.assertEqual(r["larger_half_support"] - r["half_support"], F(1, 2))
            self.assertTrue(r["nested"])
            self.assertFalse(r["observed_finitely_many_levels_prove_global_positive"])

    def test_wrong_type_and_missing_source_rejected(self):
        for value in (F(0), -1, 0.3, True):
            with self.assertRaises((WeilWindowError, ValueError)):
                CompactWeilSourceWindow(value)
        with self.assertRaises(WeilWindowError):
            CompactWeilSourceWindow(6).certificate()
        for p in (1, 4, 6, 9, 15, True):
            with self.assertRaises(WeilWindowError):
                invisible_prime_window(p, F(1))
        with self.assertRaises(WeilWindowError):
            support_cofinality_receipt(0)


if __name__ == "__main__":
    unittest.main()
