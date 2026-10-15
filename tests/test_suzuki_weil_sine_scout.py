"""Smoke regressions for numerically scouting the genuine Weil integral.

These are floating-point diagnostics, NEVER spectral proof certificates.
"""
import unittest
import math
from scripts.suzuki_weil_sine_scout import simpson,source_prime_jets,sine_result


class SuzukiSineScoutTests(unittest.TestCase):
    def test_basic_quadrature_independent_calibration(self):
        self.assertAlmostEqual(simpson(lambda t:t*t,0,1,256),1/3,places=12)
        self.assertAlmostEqual(simpson(lambda t:math.sin(t),0,math.pi,512),2,places=8)

    def test_correct_prime_onset_and_no_composite_6(self):
        self.assertEqual(source_prime_jets(0.1),[])
        self.assertEqual([x[0] for x in source_prime_jets(.42)],[2])
        self.assertNotIn(6,[x[0] for x in source_prime_jets(1.0)])
        self.assertIn(4,[x[0] for x in source_prime_jets(1.0)])

    def test_numerical_diagnostics_not_promoted_to_form_positivity(self):
        c=sine_result(3*math.log(2)/5,1)
        self.assertLess(c['rayleigh'],0.05)
        self.assertGreater(c['rayleigh'],0)
        self.assertFalse(c['qualified'])
        self.assertFalse(c['RH_proved'])
        self.assertEqual(c['prime_jets'],[2])


if __name__=='__main__':unittest.main()
