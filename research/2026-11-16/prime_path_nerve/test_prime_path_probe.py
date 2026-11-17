"""Isolated standard-library research tests, no repository import required."""
import unittest
from fractions import Fraction
from math import gcd, prod
from prime_path_probe import (primes_through,sieve,signed_faces,simplex_euler_char,
  mobius,ramanujan,negative_odd_residue,negative_odd_factor,finite_euler_minus_one,is_new_prime,full_demo)

class PrimePathChecks(unittest.TestCase):
    def test_complete_exact_suite(self):
        self.assertEqual(full_demo(),'exact certificates passed')
    def test_prime_source_validation(self):
        for bad in ((2,2),(2,6),(1,2),(4,)):
            with self.assertRaises(ValueError):
                sieve(bad,11)
    def test_boolean_nerve_49_121(self):
        self.assertEqual(sieve((2,3,5),49),1)
        self.assertEqual(sieve((2,3,5,7),49),0)
        self.assertTrue(is_new_prime(7))
        self.assertFalse(is_new_prime(49))
        self.assertFalse(is_new_prime(121))
    def test_euler_char(self):
        self.assertEqual(simplex_euler_char((2,3,5),7),0)
        self.assertEqual(simplex_euler_char((2,3,5),6),1)
        self.assertEqual(signed_faces((2,3,5),6),0)
    def test_exact_minus_one_2357(self):
        primes=(2,3,5,7)
        self.assertEqual(finite_euler_minus_one(primes),Fraction(1,48))
        self.assertEqual(negative_odd_residue(primes,1),-4)
        self.assertEqual(negative_odd_residue(primes,1)*finite_euler_minus_one(primes),Fraction(-1,12))
    def test_prime_character(self):
        self.assertEqual(ramanujan(30,1),-1)
        self.assertEqual(ramanujan(30,0),8)
        self.assertEqual(ramanujan(30,6),-2)
    def test_full_point_limit(self):
        # With the prime inventory growing, only n=1 survives eventually.
        for n in range(2,150):
            self.assertEqual(sieve(primes_through(n),n),0)
        self.assertEqual(sieve(primes_through(149),1),1)
    def test_new_prime_composite_six_not_extra_atom(self):
        for n in range(1,150):
            sel=sieve((2,3),n)
            self.assertEqual(sel,sel*(1-int(n%6==0)))
    def test_even_zeta_values(self):
        self.assertEqual(negative_odd_residue((),1),Fraction(-1,12))
        self.assertEqual(negative_odd_residue((),2),Fraction(1,120))
        self.assertEqual(negative_odd_residue((),3),Fraction(-1,252))

if __name__=='__main__':
    unittest.main(verbosity=2)
