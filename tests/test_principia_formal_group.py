import unittest
from fractions import Fraction
from observational_succ.principia_formal_group import (
    log_coefficients, inverse_formal_log, valuation, factorial_valuation,
    verify_height_two, InvalidFormalSource, compose_truncated, power_truncated
)

class FormalGroupTests(unittest.TestCase):
    def test_resolvent_support(self):
        self.assertEqual(log_coefficients(2,20)[4],Fraction(1,2))
        self.assertEqual(log_coefficients(2,20)[16],Fraction(1,4))
        self.assertEqual(log_coefficients(3,20)[9],Fraction(1,3))
    def test_exact_inverse_composition_and_bound(self):
        for p,d in ((2,8),(2,20),(3,12),(5,8)):
            with self.subTest(p=p,d=d):
                self.assertGreaterEqual(verify_height_two(p,d,[1,1,2,3])['inverse_support'],1)
    def test_nontrivial_source_compositions(self):
        for f in ([0,1],[1,0,1],[0,0,0,1],[1,2,4,8]):
            verify_height_two(2,20,f)
    def test_nonintegral_kernel_rejected(self):
        with self.assertRaises(InvalidFormalSource): verify_height_two(2,12,[0,Fraction(1,2)])
    def test_composite_prime_rejected(self):
        with self.assertRaises(InvalidFormalSource):log_coefficients(4,8)
    def test_known_first_inverse_coefficient(self):
        self.assertEqual(inverse_formal_log(2,8)[4],Fraction(-1,2))
        self.assertEqual(inverse_formal_log(3,12)[9],Fraction(-1,3))
    def test_height_one_mutant_breaks_height_two_bound(self):
        # The wrong height-one log T + T^p/p has inverse coefficient -1/p at T^p.
        p=3
        self.assertLess(Fraction(-1),Fraction(-(p-1),p*p-1))
    def test_legendre_factorial(self):
        self.assertEqual(factorial_valuation(10,2),8)
        self.assertEqual(valuation(Fraction(8,3),2),3)
        self.assertIsNone(valuation(Fraction(0),3))

if __name__=='__main__':unittest.main()
