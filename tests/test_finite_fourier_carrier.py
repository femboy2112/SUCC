"""Independent rational cyclotomic character-source verification."""
import unittest
from fractions import Fraction as F
from itertools import product
from math import gcd
from observational_succ.diagonal_adele_zeta import DiagonalSourceError,prime
from observational_succ.finite_fourier_carrier import (
    CyclotomicElement,cyclotomic_polynomial,exact_dft,exact_idft,
    shift_function,dilate_function,fourier_covariance_receipt,
)

class ExactFiniteFourier(unittest.TestCase):
    def test_exact_cyclotomic_basis_examples(self):
        self.assertEqual(cyclotomic_polynomial(1),(F(-1),F(1)))
        self.assertEqual(cyclotomic_polynomial(4),(F(1),F(0),F(1)))
        self.assertEqual(cyclotomic_polynomial(6),(F(1),F(-1),F(1)))
        self.assertEqual(cyclotomic_polynomial(8),(F(1),F(0),F(0),F(0),F(1)))

    def test_all_finite_character_orthogonality(self):
        for n in range(2,13):
            for k in range(n):
                v=CyclotomicElement.scalar(n,0)
                for x in range(n):
                    v=v+CyclotomicElement.root(n,k*x)
                self.assertEqual(v,CyclotomicElement.scalar(n,n if k==0 else 0))

    def test_dft_exact_inverse_multiple_rational_sources(self):
        for n in range(2,12):
            for base in range(3):
                values=tuple(F((x*x+base*x-2)%7, x+1) for x in range(n))
                inverted=exact_idft(exact_dft(values))
                self.assertEqual(inverted,tuple(CyclotomicElement.scalar(n,q) for q in values))

    def test_succ_and_fucc_commuting_dual_squares(self):
        for n in range(2,11):
            f=tuple(F(2*x+1,x+1) for x in range(n))
            for m in range(2,n+3):
                if gcd(m,n)!=1:continue
                for d in (-1,0,1):
                    report=fourier_covariance_receipt(f,d,m)
                    self.assertTrue(report['exact_inverse'])
                    self.assertTrue(report['shift_fourier_square'])
                    self.assertTrue(report['fucc_dual_frequency_square'])
                    self.assertFalse(report['physical_carrier_authenticated'])

    def test_nonunit_dilation_not_permutation(self):
        with self.assertRaises(DiagonalSourceError):
            dilate_function((1,2,3,4),2)

    def test_fake_euler_source_may_pass_behavior_but_not_signature(self):
        f=(1,3,5,7,9)
        self.assertTrue(fourier_covariance_receipt(f,1,6)['fucc_dual_frequency_square'])
        with self.assertRaises(DiagonalSourceError):
            fourier_covariance_receipt(f,1,6,require_prime=True)
        self.assertTrue(fourier_covariance_receipt(f,1,2,require_prime=True)['prime_source_attested'])

    def test_missing_fractional_sources_fail(self):
        with self.assertRaises(DiagonalSourceError):
            exact_dft([1.1,2])

if __name__=='__main__':unittest.main()
