from fractions import Fraction as Q
from math import pi,sin,cos
import unittest

from observational_succ.pi_succ_character_intervals import (
    machin_pi_interval,characteristic_interval,fourier_squared_interval,
    magnitude_decimal_bounds,
)
from observational_succ.pi_succ_lag_bridge import source_circle_prefix

class SpectralFiniteCertificates(unittest.TestCase):
    def test_pi_machin_enclosure_and_monotonicity(self):
        a,b=machin_pi_interval(12)
        c,d=machin_pi_interval(16)
        self.assertTrue(a<c<d<b)
        import mpmath as mp
        with mp.workdps(100):
            self.assertTrue(mp.mpf(c.numerator)/c.denominator < mp.pi
                            < mp.mpf(d.numerator)/d.denominator) # diagnostic, NOT proof

    def test_trigonometric_exact_root_controls(self):
        pr=machin_pi_interval(20)
        for x,re,im in ((Q(),1,0),(Q(1,4),0,1),
                        (Q(1,2),-1,0),(Q(3,4),0,-1)):
            clo,chi,slo,shi=characteristic_interval(x,pr,16)
            self.assertTrue(clo<=re<=chi)
            self.assertTrue(slo<=im<=shi)

    def test_independent_double_angle_oracle_inside_enclosures(self):
        # Diagnostic comparisons only; actual certificate is rational.
        pr=machin_pi_interval(20)
        for den in (7,11,16,31):
            for j in range(den):
                z=Q(j,den)
                a,b,c,d=characteristic_interval(z,pr,14)
                self.assertLess(float(a)-1e-12,cos(2*pi*float(z)))
                self.assertGreater(float(b)+1e-12,cos(2*pi*float(z)))
                self.assertLess(float(c)-1e-12,sin(2*pi*float(z)))
                self.assertGreater(float(d)+1e-12,sin(2*pi*float(z)))

    def test_actual_selected_lag_fourier_certificate_small_window(self):
        phases=source_circle_prefix(80)
        lo,hi=fourier_squared_interval(phases[32:48],15,order=12)
        self.assertTrue(Q()<lo<hi<1)
        bounds=magnitude_decimal_bounds((lo,hi))
        self.assertLess(float(bounds[0]),float(bounds[1]))

    def test_rational_nonnormal_source_refuses(self):
        x=(Q(1,15),)*12
        a,b=fourier_squared_interval(x,15)
        self.assertTrue(a>Q(99,100))
        self.assertEqual(b,1)

    def test_reject_malformed(self):
        with self.assertRaises(ValueError):machin_pi_interval(0)
        with self.assertRaises(ValueError):fourier_squared_interval((),1)
        with self.assertRaises(ValueError):characteristic_interval(Q(1,7),(Q(0),Q(1)))

if __name__=='__main__':unittest.main()
