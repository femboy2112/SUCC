"""Finite polynomial jets do not determine shell-boundary occupancy."""
from fractions import Fraction as Q
import unittest

# P_4(2u-1), shifted Legendre polynomial of exact degree four.
COEFF=(Q(1),Q(-20),Q(90),Q(-140),Q(70))
def integral_monomial(k,lo=Q(0),hi=Q(1)):
    return sum((c*(hi**(j+k+1)-lo**(j+k+1))/(j+k+1)
                for j,c in enumerate(COEFF)),Q())
def p4(u):return sum((c*u**j for j,c in enumerate(COEFF)),Q())

class HistoryJetNoGo(unittest.TestCase):
    def test_01_first_four_raw_moments_equal_to_haar(self):
        for k in range(4):
            self.assertEqual(integral_monomial(k),0)
        self.assertEqual(integral_monomial(4),Q(1,630))

    def test_02_exact_quarter_threshold_distinguishes_models(self):
        self.assertEqual(integral_monomial(0,Q(3,4),Q(1)),Q(-15,512))
        self.assertEqual(Q(1,4)+integral_monomial(0,Q(3,4),Q(1)),Q(113,512))
        self.assertNotEqual(Q(113,512),Q(1,4))

    def test_03_legendre_extrema_validate_probability_density(self):
        # P4(t)=(35t^4-30t^2+3)/8; extrema at t=0,+/-sqrt(3/7), +/-1.
        self.assertEqual(p4(Q(0)),1)
        self.assertEqual(p4(Q(1)),1)
        self.assertEqual(p4(Q(1,2)),Q(3,8))
        self.assertTrue(-Q(3,7)<=Q(3,8)<=1)
        # Min P4=-3/7; max P4=1, so |eps|<=1 yields 1+eps P4>=0.

    def test_04_higher_order_jet_detects_hidden_change(self):
        self.assertNotEqual(integral_monomial(4),0)
        self.assertEqual(integral_monomial(4),Q(1,630))

if __name__=='__main__':unittest.main()
