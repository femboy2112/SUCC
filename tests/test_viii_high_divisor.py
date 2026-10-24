"""Exact independent controls; the universal conic proof is in its dossier."""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
import unittest

from observational_succ.viii_high_divisor import (
    CofactorSelection, ConicSeed, catalog_growth_budget, conic_selections,
    integer_weight, ris, source_selections,
)


def independent_radical(n):
    return product_value(p for p in range(2,n+1)
                         if n%p == 0 and all(p%d for d in range(2,isqrt(p)+1)))


def product_value(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def brute_sources(seed, X):
    """Additive triangle census, independent of the production conic slices."""
    answer = set()
    for c in range(2,int(X)+1):
        for a in range(1,c):
            b = c-a
            if gcd(a,b) != 1:
                continue
            roots = []
            for value,cofactor in zip((a,b,c),(seed.u,seed.v,seed.w)):
                if value%cofactor:
                    break
                root = isqrt(value//cofactor)
                if root*root*cofactor != value:
                    break
                roots.append(root)
            if len(roots) == 3:
                answer.add((a,b,c))
    return answer


class ConicIncidenceTests(unittest.TestCase):
    def test_expansion_retains_all_selections_and_exact_weights(self):
        cases = 0
        for c in range(2,41):
            for a in range(1,c):
                if gcd(a,c) != 1:
                    continue
                records = source_selections(a,c-a)
                self.assertEqual(len(records),len(set(records)))
                for record in records:
                    u,v,w = record.cofactors
                    self.assertEqual(record.d*u+record.e*v,record.f*w)
                    self.assertEqual(record.D*record.U,a*(c-a)*c)
                    self.assertEqual(gcd(record.d,record.e)*gcd(record.d,record.f)*gcd(record.e,record.f),1)
                    self.assertLessEqual(4*record.D*record.U,c**3)
                    if record.D > c*c:
                        self.assertLess(4*record.U,c)
                for t in (0,1,2):
                    exact = sum(integer_weight(r.d,t)*integer_weight(r.e,t)*integer_weight(r.f,t)
                                for r in records)
                    self.assertEqual(exact,ris(a*(c-a)*c)**t)
                cases += 1
        self.assertGreater(cases,400)
        self.assertEqual(len(source_selections(8,1)),6)

    def test_ris_has_independent_small_integer_check(self):
        for n in range(1,201):
            self.assertEqual(ris(n),n//independent_radical(n))

    def test_quadratic_identity_and_bounded_cancellation(self):
        seeds = (ConicSeed(1,1,1,3,4,5),ConicSeed(1,1,2,1,1,1),
                 ConicSeed(2,3,5,1,1,1),ConicSeed(4,1,5,1,1,1),
                 ConicSeed(3,4,7,1,1,1),ConicSeed(1,1,1,6,8,10))
        count = 0
        for seed in seeds:
            for n,m in product(range(-20,21),repeat=2):
                if gcd(n,m) != 1:
                    continue
                x,y,z = seed.parameter_image(n,m)
                self.assertEqual(seed.u*x*x+seed.v*y*y,seed.w*z*z)
                self.assertGreater(z,0)
                cancellation = gcd(gcd(x,y),z)
                self.assertEqual(seed.cancellation_multiple%cancellation,0)
                count += 1
        self.assertEqual(count,6144)

    def test_parametrization_coverage_by_inverse_rational_direction(self):
        for seed in (ConicSeed(1,1,1,3,4,5),ConicSeed(1,1,2,1,1,1),
                     ConicSeed(4,1,5,1,1,1)):
            for record in conic_selections(seed,10000):
                r,s,z = record.square_roots
                n,m = r*seed.z0-seed.r0*z,s*seed.z0-seed.s0*z
                h = gcd(n,m)
                if h == 0:
                    continue  # The explicitly excepted base point.
                raw = seed.parameter_image(n//h,m//h)
                g = gcd(gcd(raw[0],raw[1]),raw[2])
                self.assertEqual(tuple(q//g for q in raw),(r,s,z))

    def test_conic_census_against_independent_additive_census(self):
        for seed in (ConicSeed(1,1,1,3,4,5),ConicSeed(1,1,2,1,1,1),
                     ConicSeed(2,3,5,1,1,1),ConicSeed(4,1,5,1,1,1)):
            for X in (2,40,Fraction(201,2),400):
                records = conic_selections(seed,X)
                self.assertEqual({(r.a,r.b,r.c) for r in records},brute_sources(seed,X))
                self.assertLessEqual(len(records)**2,seed.count_coefficient_squared*X)

    def test_source_primitivity_is_not_root_primitivity(self):
        # 4*1^2+1*4^2=5*2^2, primitive roots but nonprimitive source.
        self.assertEqual(gcd(gcd(1,4),2),1)
        with self.assertRaises(ValueError):
            CofactorSelection(4,16,20,1,16,4)
        self.assertNotIn((4,16,20),{(r.a,r.b,r.c) for r in
                         conic_selections(ConicSeed(4,1,5,1,1,1),20)})

    def test_primitive_root_theorem_also_covers_nonprimitive_sources(self):
        seed = ConicSeed(4,1,5,1,1,1)
        count = 0
        for z in range(1,31):
            for r in range(1,isqrt((5*z*z-1)//4)+1):
                s = isqrt(5*z*z-4*r*r)
                if 4*r*r+s*s != 5*z*z or gcd(gcd(r,s),z) != 1:
                    continue
                count += 1
                n,m = r-z,s-z
                h = gcd(n,m)
                if h:
                    raw = seed.parameter_image(n//h,m//h)
                    g = gcd(gcd(raw[0],raw[1]),raw[2])
                    self.assertEqual(tuple(q//g for q in raw),(r,s,z))
        self.assertGreater(count,len(conic_selections(seed,4500)))
        self.assertLessEqual(count**2,seed.count_coefficient_squared*4500)

    def test_balanced_high_divisor_source_and_actual_weight(self):
        record = CofactorSelection(49,289,338,49,289,169)
        self.assertEqual(record.cofactors,(1,1,2))
        self.assertEqual(record.D,2393209)
        self.assertGreater(record.D,338**2)
        self.assertEqual(ris(7*17*13),1)
        self.assertEqual(ris(record.a*record.b*record.c),1547)
        self.assertEqual(integer_weight(49,1)*integer_weight(289,1)*integer_weight(169,1),1152)
        self.assertIn(record,conic_selections(ConicSeed(1,1,2,1,1,1),338))

    def test_deep_prime_square_root_majorant_requires_depth_factor(self):
        self.assertEqual(integer_weight(81,1),18)
        self.assertGreater(integer_weight(81,1),isqrt(81))
        for r in range(1,150):
            for t in (0,1,2):
                self.assertLessEqual(integer_weight(r*r,t),(r*ris(r))**t)
        # Powerful does not mean square; the conic sector never covers 8.
        record = CofactorSelection(8,1,9,8,1,9)
        self.assertIsNone(record.square_roots)

    def test_growth_exponents_and_dyadic_saving_are_exact(self):
        t,kappa,theta = Fraction(5,7),Fraction(1,2),Fraction(1,100)
        selected = catalog_growth_budget(t,kappa,theta)
        source = catalog_growth_budget(t,kappa,theta,source_moment=True)
        self.assertEqual(selected.exponent,Fraction(1367,700))
        self.assertEqual(selected.saving,Fraction(33,700))
        self.assertEqual(source.exponent,Fraction(691,350))
        self.assertEqual(source.saving,Fraction(9,350))
        self.assertEqual(source.coefficient,23)
        self.assertGreater(source.t,Fraction(2,3))
        self.assertLess(catalog_growth_budget(1,kappa,theta).saving,0)

    def test_immutable_strict_inputs(self):
        for bad in (True,1.0,Fraction(3,2),0):
            with self.assertRaises(ValueError):
                ConicSeed(bad,1,2,1,1,1)
        with self.assertRaises(ValueError):
            ConicSeed(1,1,1,1,1,1)
        seed = ConicSeed(1,1,2,1,1,1)
        with self.assertRaises(AttributeError):
            seed.w = 1
        for direction in ((0,0),(2,2),(True,1),(1.0,1)):
            with self.assertRaises(ValueError):
                seed.parameter_image(*direction)
        for bad in (True,2.0,Fraction(3,2)):
            with self.assertRaises(ValueError):
                conic_selections(seed,bad)
        for bad in (True,0.5,Fraction(8,7)):
            with self.assertRaises(ValueError):
                catalog_growth_budget(bad,0,0)


if __name__ == "__main__":
    unittest.main()
