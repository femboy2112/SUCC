"""Exact tests for the Scott cofinal-schedule theorem (Front D)."""
import unittest

from observational_succ import scott_cofinal_schedule as scf


class CofinalScheduleTests(unittest.TestCase):
    def test_canonical_seam_schedule_is_cofinal(self):
        r = scf.verify_cofinality_theorem()
        self.assertTrue(r['seam_schedule_cofinal'])

    def test_diagonal_schedule_not_cofinal(self):
        r = scf.verify_cofinality_theorem()
        self.assertTrue(r['diagonal_schedule_L_bounded'])
        self.assertTrue(r['diagonal_NOT_cofinal'])

    def test_both_coordinates_unbounded_required(self):
        # Cofinal requires BOTH n and L unbounded.
        ns, Ls = scf.seam_schedule(20)
        self.assertEqual(len(ns), len(Ls))
        self.assertTrue(max(ns) >= 20 and max(Ls) >= 20)
        ns2, Ls2 = scf.diagonal_schedule(20)
        self.assertEqual(max(Ls2), 2)  # L frozen at 2


if __name__ == '__main__':
    unittest.main()
