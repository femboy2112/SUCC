"""Live cross-authentication against Coherent Main X's two original BBP carriers.

No independent surrogate arithmetic source and no pi numeric oracle used here.
This integration module requires the full SUCC package and runs in hosted CI.
"""
from __future__ import annotations

import unittest
from fractions import Fraction as Q

from observational_succ import bbp_natural_carrier as NC
from observational_succ import integer_bbp_carrier as IC
from observational_succ.vacuum_parameter_bbp import (
    forcing, source_orbit, selected_hex_digit, source_tail_bracket,
    krylov_certificate, certified_hex_prefix,
)


class AuthenticatedFourPolePassports(unittest.TestCase):
    def test_all_forcing_sources_are_exact_same_rational(self):
        for n in range(1,61):
            fresh=forcing(n)
            a,b=IC.forcing_pair(n)
            self.assertEqual(fresh,Q(a,b))
            self.assertEqual(fresh,NC.exact_forcing(n))
            self.assertEqual(fresh,Q(NC.forcing_numerator(n),
                                     NC.forcing_denominator(n)))

    def test_moment_recursion_has_original_unwrapped_integer_lifts(self):
        states=IC.source_states(36)
        for n in range(37):
            expected=source_orbit(n)
            self.assertEqual(expected,NC.orbit_state(n).rational)
            self.assertEqual(expected,Q(states[n].numerator,states[n].conductor))

    def test_selected_decimal_to_hex_carrier_readouts_preserved(self):
        for n in range(1,35):
            d=selected_hex_digit(n)
            self.assertIsNotNone(d)
            # Natural carrier alpha=pi/16 digit index n-1 matches our n-th pi digit.
            if n>=2:
                alternate=NC.certified_hex_digit(n-1)
                self.assertIsNotNone(alternate)
                self.assertEqual(d,alternate[0])
            lo,hi=source_tail_bracket(n)
            self.assertGreater(lo,0)
            self.assertLess(lo,hi)

    def test_eight_krylov_moments_authentic_normality_firewall(self):
        certificate=krylov_certificate(8)
        self.assertEqual(certificate.moments_used,17)
        self.assertEqual(certified_hex_prefix(8,23),
                         '3.243F6A8885A308D313198A2')
        self.assertLess(certificate.upper-certificate.lower,Q(1,16**23))


if __name__=='__main__':unittest.main()
