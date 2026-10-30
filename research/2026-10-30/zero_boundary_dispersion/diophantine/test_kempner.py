import unittest
from fractions import Fraction as Q
from kempner_calibration import fold,euclidean

class KempnerTests(unittest.TestCase):
    def test_initial_fold(self):
        self.assertEqual(fold(16,2),[0,15,18,16,15])
    def test_independent_euclidean(self):
        for u in (3,16,19):
            for v in (2,5,8):
                s=sum((Q(1,u**(2**j)) for j in range(v+1)),Q(0))
                self.assertEqual(fold(u,v),euclidean(s.numerator,s.denominator))
    def test_bounded_partial_quotient_alphabet(self):
        a=fold(16,10)
        self.assertEqual(set(a[1:]),{14,15,16,18})
        self.assertEqual(a[-1],15)
    def test_no_zero_partial_quotients_in_declared_domain(self):
        for u in (3,4,16):
            self.assertTrue(all(x>0 for x in fold(u,7)[1:]))
        with self.assertRaises(ValueError):fold(2,7)

if __name__=='__main__':unittest.main(verbosity=2)
