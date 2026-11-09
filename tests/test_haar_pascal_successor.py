"""Signed Pascal higher differences: source, spectrum and hostile controls."""
import unittest
from math import comb
from observational_succ.haar_successor_junction import signed_junction, source_certified_digits
from observational_succ.haar_pascal_successor import pascal_successor_energy

class HaarPascalTests(unittest.TestCase):
    def test_pascal_successor_binomial_impulse(self):
        # Single occupied child has pulse (1,-m,...), squared norm C(2m,m).
        for m in range(1,6):
            self.assertEqual(pascal_successor_energy([0]*70,64,0,m),16*comb(2*m,m))

    def test_pascal_successor_upper_h8_exact(self):
        digits=[d for d in range(16) for _ in range(5 if d%2==0 else 3)]+[0]
        detail=signed_junction(digits,64,0)['low_energy']
        for m in range(1,5):
            self.assertEqual(pascal_successor_energy(digits,64,0,m),4**m*detail)

    def test_pascal_first_order_exact_original_source(self):
        digits,_,_=source_certified_digits(16,69)
        for j in range(3):
            z=signed_junction(digits,64,j)
            self.assertEqual(pascal_successor_energy(digits,64,j,1),z['successor_energy'])
            self.assertGreaterEqual(20**3*pascal_successor_energy(digits,64,j,3),3**3*z['low_energy'])

if __name__=='__main__': unittest.main()
