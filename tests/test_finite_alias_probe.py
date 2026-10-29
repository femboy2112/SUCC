import sys, unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research/2026-10-29/golden_gamma_farey_twist'))
import finite_alias_probe as a

class TestFiniteIndistinguishability(unittest.TestCase):
    def test_binary_small(self):
        for k in range(1,5):
            w=a.de_bruijn(2,k)
            self.assertTrue(a.exact_uniform_upto(w,2,k))
            self.assertEqual(len(a.circular_histogram(w,k+1)),2**k)  # fewer than 2**(k+1)
    def test_hexadecimal_depth_one_to_three(self):
        for k in (1,2,3):
            w=a.de_bruijn(16,k)
            self.assertTrue(a.exact_uniform_upto(w,16,k))
            self.assertEqual(len(w),16**k)
            self.assertEqual(len(a.circular_histogram(w,k+1)),16**k)
    def test_periodic_rational_bad_global(self):
        w=a.de_bruijn(16,2)
        x=a.rational_periodic_number(w,16)
        self.assertIsInstance(x,Fraction)
        self.assertGreater(x,0)
        self.assertLess(x,1)
        self.assertTrue(a.exact_uniform_upto(w,16,2))
        self.assertLess(len(a.circular_histogram(w,3)),16**3)
    def test_fourier_lower_modes_exactly_blind(self):
        for q in (7,17,65,257):
            self.assertTrue(all(a.finite_frequency_uniform(q,h)==0 for h in range(1,q)))
            self.assertEqual(a.finite_frequency_uniform(q,q),1)
    def test_negative_and_bad_inputs(self):
        with self.assertRaises(ValueError):a.de_bruijn(1,2)
        with self.assertRaises(ValueError):a.de_bruijn(16,6)
        with self.assertRaises(ValueError):a.rational_periodic_number([0,16],16)

if __name__=='__main__':unittest.main()
