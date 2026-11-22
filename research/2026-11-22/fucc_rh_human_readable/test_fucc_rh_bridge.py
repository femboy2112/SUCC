import unittest
from fractions import Fraction
from math import factorial
from fucc_rh_bridge import (
    factorize,fucc_euler_log_coefficients,fucc_log_commutator_coefficients,
    riesz_log_prime_coeffs,inverse_height_two_log,poly_pow,poly_mul,
    lagrange_U_power_coefficient,padic_valuation_fraction,valuation_factorial,
    local_model_derivative,local_model_lower_bound,
    fucc_mahler_resolvent_coefficients,fucc_mahler_resolvent_norm_sq,
    fucc_mahler_residual_coefficients)

class FUCCTest(unittest.TestCase):
    def test_euler_prime_powers(self):
        self.assertEqual(fucc_euler_log_coefficients(16),
           {2:1,3:1,4:Fraction(1,2),5:1,7:1,8:Fraction(1,3),9:Fraction(1,2),11:1,13:1,16:Fraction(1,4)})
        self.assertNotIn(6,fucc_log_commutator_coefficients(100))
    def test_primes_with_log_coeff(self):
        for X in range(1,83):
            for n,p in fucc_log_commutator_coefficients(X).items():
                self.assertEqual(factorize(n),{p:next(iter(factorize(n).values()))})
    def test_Riesz_X16(self):
        self.assertEqual(riesz_log_prime_coeffs(16)[2],
           Fraction(16,2)-1+Fraction(16,4)-1+Fraction(16,8)-1+Fraction(16,16)-1)
        self.assertEqual(riesz_log_prime_coeffs(16)[3],Fraction(16,3)-1+Fraction(16,9)-1)
    def test_Euler_slope(self):
        self.assertEqual(valuation_factorial(27,3),13)
        self.assertEqual(valuation_factorial(16,2),15)
    def test_Lagrange_independence(self):
        for p,N in [(2,23),(3,29),(5,29)]:
            U=inverse_height_two_log(p,N)
            for a in range(1,N+1):
                self.assertEqual(U[a],lagrange_U_power_coefficient(p,a,1),(p,a))
            for m in (1,2,3):
                w=poly_pow(U,m,N)
                for a in range(m,N+1):
                    self.assertEqual(w[a],lagrange_U_power_coefficient(p,a,m),(p,a,m))
    def test_valuation_bound(self):
        for p,N in [(2,28),(3,30),(5,30)]:
            for a in range(1,N+1):
                z=local_model_derivative(p,a,[1,2,-3,1])
                v=padic_valuation_fraction(z,p)
                self.assertTrue(v is None or v>=local_model_lower_bound(p,a),(p,a,z))
    def test_valuation_mutant(self):
        for p,N in [(2,16),(3,20)]:
            for a in range(1,N+1):
                z=local_model_derivative(p,a,[2,0,0,-7,8,5])
                v=padic_valuation_fraction(z,p)
                self.assertTrue(v is None or v>=local_model_lower_bound(p,a),(p,a,z))
    def test_valuation_gamma_not_relevant(self):
        self.assertEqual(padic_valuation_fraction(Fraction(1,3),3),-1)
        self.assertIsNone(padic_valuation_fraction(Fraction(0),3))
    def test_fucc_shift_no_coefficient_divisibility(self):
        # V_p^k|1> = |p^k>, coefficient 1. No positive p-adic valuation.
        for p in (2,3,5):
            for k in range(1,9):
                self.assertEqual(padic_valuation_fraction(Fraction(1),p),0)
                self.assertEqual(factorize(p**k),{p:k})
    def test_fucc_resolvent_exact_series(self):
        for p in [2,3,5,7]:
            for terms in [1,2,3,5]:
                coeff=fucc_mahler_resolvent_coefficients(p,terms)
                self.assertEqual(coeff,{p**(2*j):Fraction(1,p**j) for j in range(terms)})
                self.assertEqual(fucc_mahler_residual_coefficients(p,terms),{1:Fraction(1)})
            self.assertEqual(fucc_mahler_resolvent_norm_sq(p),Fraction(p*p,p*p-1))
    def test_fucc_resolvent_matches_formal_log(self):
        for p in [2,3,5]:
            n=28
            coeff=fucc_mahler_resolvent_coefficients(p,4)
            U=inverse_height_two_log(p,n)
            # From l(U)=U+sum p^(-j)U^(p^(2j))=z, direct coefficient identity.
            series=U.copy()
            for exponent,c in coeff.items():
                if exponent>1 and exponent<=n:
                    x=poly_pow(U,exponent,n)
                    series=[a+c*b for a,b in zip(series,x)]
            self.assertEqual(series,[Fraction(0),Fraction(1)]+[Fraction(0)]*(n-1))
    def test_hadamard_capacity_example(self):
        a,b,c,d=4,1,1,4
        det=a*d-b*c
        self.assertEqual(det,15)
        self.assertLessEqual(det*det,(a*a+b*b)*(c*c+d*d))
        self.assertEqual(factorize(det),{3:1,5:1})

if __name__=='__main__':unittest.main()
