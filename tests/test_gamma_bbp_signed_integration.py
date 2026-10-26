"""Source passport checks against both Main X BBP arithmetic interfaces.

Local standalone test fixtures for those interfaces are labelled shims;
final authority requires this suite on GitHub's real complete repository.
"""
from __future__ import annotations

import unittest
from fractions import Fraction as Q
from observational_succ import bbp_natural_carrier as NC
from observational_succ import integer_bbp_carrier as IC
from observational_succ.gamma_bbp_signed_coherence import (
    authentic_orbit_rational, finite_twisted_coboundary,
    green_tail_interval, moment_anchor, signed_moment_crossing,
)
from observational_succ.zero_one_gamma_bridge import authentic_bbp_forcing


class LiveSourcePassportTests(unittest.TestCase):
    def test_independent_integer_and_natural_four_pole_coefficients(self):
        for n in range(1,90):
            a,b=IC.forcing_pair(n)
            expected=Q(a,b)
            self.assertEqual(expected,NC.exact_forcing(n))
            self.assertEqual(expected,authentic_bbp_forcing(n))
            self.assertEqual(expected,Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2))

    def test_signed_coherence_uses_actual_time_index_not_shifted_index(self):
        for n in (0,1,2,4,12,35):
            self.assertEqual(finite_twisted_coboundary(n,7)[2],
                             NC.exact_forcing(n+1))
            self.assertNotEqual(authentic_bbp_forcing(n+1),authentic_bbp_forcing(n+2))

    def test_true_reference_relative_sign_control(self):
        a=moment_anchor(0,terms=35)
        self.assertEqual(a.b_moment,NC.exact_forcing(1))
        self.assertGreater(signed_moment_crossing(0,1,terms=35).determinant.lower,0)
        self.assertGreater(green_tail_interval(1,12).lower,0)


if __name__=='__main__':unittest.main()
