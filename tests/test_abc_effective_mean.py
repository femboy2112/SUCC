"""Exact holdouts for the new effective arithmetic theorem; not its proof."""
from fractions import Fraction
from itertools import product
from math import gcd
import unittest

from observational_succ.abc_effective_mean import (
    dyadic_first_moment_lower, effective_constant_budget,
    effective_rate_parameters, euler_constant_power,
    primitive_divisor_budget, primitive_divisor_count_mobius,
    raw_discrepancy_bound, raw_divisor_count,
)
from observational_succ.abc_clock_families import ris
from observational_succ.cloud_abc_correlations import (
    divisors, mobius, powerful, primitive_divisor_count,
)


def brute_count(X, d, e, f, primitive=False):
    """Independent a,b census: no CRT, rows, progressions or Mobius inversion."""
    return sum(
        a % d == 0 and b % e == 0 and (a+b) % f == 0
        and (not primitive or gcd(a, b) == 1)
        for a in range(1, int(X) + 1)
        for b in range(1, int(X) + 1)
        if a+b <= X
    )


MODULI = tuple((d,e,f) for d,e,f in product(range(1, 8), repeat=3)
               if gcd(d,e) == gcd(d,f) == gcd(e,f) == 1)


class EffectiveMeanTests(unittest.TestCase):
    def test_first_moment_dyadic_subexpansion_is_a_genuine_lower_bound(self):
        for X in (2, Fraction(9,2), 9, 18, Fraction(59,2)):
            first_moment = sum(ris(a*(c-a)*c)
                               for c in range(2,int(X)+1)
                               for a in range(1,c) if gcd(a,c)==1)
            lowers = [dyadic_first_moment_lower(X,K) for K in range(2,8)]
            self.assertEqual(lowers,sorted(lowers))
            self.assertLessEqual(lowers[-1],first_moment)
        for K in (True,2.0,Fraction(5,2),1):
            with self.assertRaises(ValueError):
                dyadic_first_moment_lower(8,K)

    def test_explicit_dyadic_family_for_supercritical_moments(self):
        for X in (8,Fraction(17,2),15,16,Fraction(63,2),100):
            a = 2**(int(X).bit_length()-2)
            bs = tuple(range(1,int(X)-a+1,2))
            self.assertGreater(a,Fraction(X)/4)
            self.assertLessEqual(a,Fraction(X)/2)
            self.assertGreaterEqual(len(bs),Fraction(X)/8)
            for b in bs:
                self.assertEqual(gcd(a,b),1)
                self.assertLessEqual(a+b,X)
                self.assertGreater(ris(a*b*(a+b)),Fraction(X)/8)

    def test_raw_rows_against_independent_census_and_boundary_budget(self):
        for X in (0, Fraction(1, 2), 1, 2, Fraction(5, 2), 7, Fraction(33, 4), 19):
            for d,e,f in MODULI:
                with self.subTest(X=X, moduli=(d,e,f)):
                    count = raw_divisor_count(X, d,e,f)
                    self.assertEqual(count, brute_count(X,d,e,f))
                    error = abs(count - Fraction(X)**2 / (2*d*e*f))
                    self.assertLessEqual(error, raw_discrepancy_bound(X,d,e,f))
                    self.assertLessEqual(raw_discrepancy_bound(X,d,e,f),
                                         3 * Fraction(X) / 2)

    def test_full_mobius_inversion_against_gcd_and_old_crt_routes(self):
        for X in (2, 3, Fraction(9, 2), 11, 24):
            for d,e,f in MODULI:
                with self.subTest(X=X, moduli=(d,e,f)):
                    count = primitive_divisor_count_mobius(X,d,e,f)
                    self.assertEqual(count, brute_count(X,d,e,f,True))
                    self.assertEqual(count, primitive_divisor_count(int(X),d,e,f))

    def test_shared_prime_mobius_terms_cannot_be_omitted(self):
        # a=2,b=2 must be removed even though k=2 shares the occupied prime.
        X,d,e,f = 4,2,1,1
        wrong = sum(mobius(k)*raw_divisor_count(Fraction(X,k),d,e,f)
                    for k in range(1,X//2+1) if gcd(k,d*e*f)==1)
        self.assertEqual(wrong, 2)
        self.assertEqual(primitive_divisor_count_mobius(X,d,e,f), 1)

    def test_finite_center_lattice_error_without_irrational_approximation(self):
        for X in (2, Fraction(7,2), 17, Fraction(111,4)):
            for d,e,f in MODULI:
                budget = primitive_divisor_budget(X,d,e,f)
                exact = brute_count(X,d,e,f,True)
                self.assertLessEqual(abs(exact-budget.finite_center),
                                     budget.lattice_error)
                self.assertEqual(budget.normalized_discrepancy,
                                 3*sum((Fraction(1,k) for k in range(1,budget.M+1)),
                                       Fraction())/(2*X) + Fraction(1,2*budget.M))

    def test_sparse_and_huge_moduli_are_absolute_not_relative_bounds(self):
        X,d,e,f = 841,441,400,841
        self.assertEqual(raw_divisor_count(X,d,e,f), 1)
        self.assertEqual(primitive_divisor_count_mobius(X,d,e,f), 1)
        self.assertLess(Fraction(2*X*X,d*e*f), 1)
        d = 10**30+1
        self.assertEqual(raw_divisor_count(10,d,1,1), 0)
        self.assertLessEqual(Fraction(100,2*d), raw_discrepancy_bound(10,d,1,1))

    def test_product_cutoff_gate_on_primitive_triples(self):
        for c in range(2, 45):
            for a in range(1,c):
                b = c-a
                if gcd(a,b)!=1:
                    continue
                H = ris(a*b*c)
                supports = [tuple(d for d in divisors(n) if powerful(d))
                            for n in (a,b,c)]
                for d,e,f in product(*supports):
                    self.assertLessEqual(d*e*f,H*H)
                    self.assertEqual(gcd(d,e)*gcd(d,f)*gcd(e,f),1)

    def test_exact_optimization_parameters(self):
        for t in (0,Fraction(1,3),Fraction(1,2),Fraction(3,5),Fraction(199,300)):
            p = effective_rate_parameters(t)
            self.assertGreater(p.s,p.t)
            self.assertLess(p.s,Fraction(2,3))
            self.assertGreater(p.alpha,p.t)
            self.assertGreater(2*p.alpha-p.t,1)
            self.assertEqual(p.alpha+p.beta,Fraction(5,6))
            self.assertEqual(p.cutoff_power,Fraction(6,5))
            self.assertEqual(p.rate,(2-3*p.t-3*p.h)/5)
            self.assertGreater(p.rate,0)
            self.assertLess(p.rate,(2-3*p.t)/5)

    def test_encoded_constants_are_exact_and_immutable(self):
        budget = effective_constant_budget(Fraction(1,2))
        self.assertIsInstance(budget.euler_power,int)
        self.assertGreater(budget.euler_power,0)
        self.assertIsInstance(budget.constant_upper(),Fraction)
        self.assertGreater(budget.constant_upper(),1)
        with self.assertRaises(AttributeError):
            budget.euler_power=0

    def test_strict_domains_no_bool_float_or_fractional_modulus(self):
        for bad in (True,False,2.0,2.5,-1):
            with self.assertRaises(ValueError):
                raw_divisor_count(bad,1,1,1)
        for bad in (True,1.0,Fraction(3,2),0):
            with self.assertRaises(ValueError):
                raw_divisor_count(10,bad,1,1)
        with self.assertRaises(ValueError):
            raw_divisor_count(10,2,4,1)
        with self.assertRaises(ValueError):
            primitive_divisor_budget(Fraction(3,2),1,1,1)
        for bad in (True,0.5,Fraction(2,3),1):
            with self.assertRaises(ValueError):
                effective_rate_parameters(bad)
        for h in (0,Fraction(1,6),Fraction(1,5)):
            with self.assertRaises(ValueError):
                effective_rate_parameters(Fraction(1,2),h)
        with self.assertRaises(ValueError):
            euler_constant_power(Fraction(1,2),Fraction(3,4))


if __name__ == "__main__":
    unittest.main()
