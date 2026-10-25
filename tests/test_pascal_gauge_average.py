"""Exact randomized-selector / single-selector separation tests."""
from __future__ import annotations

from fractions import Fraction as Q
import unittest
from observational_succ.pascal_gauge_average import (
    haar_initial_selector_expectation,finite_grid_initial_selector_probe,order16,
)
from observational_succ.pi_dyadic_prime_transfer import dyadic_carry_branch_certificate


class GaugeAverageTests(unittest.TestCase):
    def test_exact_Haar_mean_and_diagonal_correction(self):
        for D in (1,2,3,8,35):
            for tau in (Q(1,4),Q(1,16),Q(1,64)):
                row=haar_initial_selector_expectation(D,tau)
                self.assertEqual(16*Q(row['mean_zero'])-Q(row['mean_Q0']),15*D)
                self.assertEqual(row['mean_primitive_shells'],[D,2*D,4*D,8*D])
                self.assertEqual(row['mean_nonempty_walsh_moment'],D)

    def test_initial_grid_exact_source_rational(self):
        for q in (41,97):
            self.assertGreater(order16(q),2)
            for tau in (Q(1,4),Q(1,16)):
                result=finite_grid_initial_selector_probe(9,(6,7,8),q,tau)
                self.assertLessEqual(Q(result['finite_grid_absolute_error']),Q(result['proved_grid_error_upper']))
                self.assertEqual(result['Haar_signed_excess'],45)

    def test_hard_scope_and_grid_no_go(self):
        with self.assertRaises(ValueError):
            finite_grid_initial_selector_probe(9,(6,7,8),3,Q(1,4))
        with self.assertRaises(ValueError):
            finite_grid_initial_selector_probe(9,(6,7,8),17,Q(1,4))
        with self.assertRaises(ValueError):
            haar_initial_selector_expectation(0,Q(1,4))
        # The actual selected source can be far from the Haar mean; ensemble
        # statements must never silently assert selected <= average.
        r=dyadic_carry_branch_certificate(41,Q(1,16))
        selected=16*r['zero_centered_branch']-sum(r['branch_histogram'])
        self.assertNotEqual(selected,15*r['window_length'])


if __name__=='__main__':
    unittest.main()
