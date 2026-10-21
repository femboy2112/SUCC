"""Hostile exact tests for the dimension-indexed exterior/cofactor research."""
import unittest
from fractions import Fraction
from itertools import product
from math import comb, factorial, gcd, lcm

from observational_succ.exterior_cofactor_ascent import (
    ExteriorAscentError, cofactor_certificate, determinant,
    exterior_certificate, rank_drop_family, residue_simplex_count,
    simplex_error_bound, simplex_relative_bound,
    unrestricted_simplex_count, weighted_infinite_count,
)


class TestSimplexHierarchy(unittest.TestCase):
    def test_unrestricted_stars_bars(self):
        for m in range(1,7):
            for X in range(18):
                self.assertEqual(unrestricted_simplex_count(m,X),
                                 comb(X,m) if X>=m else 0)
                self.assertEqual(residue_simplex_count(m,1,X,[(0,)*m]),
                                 unrestricted_simplex_count(m,X))

    def test_independent_residue_oracle(self):
        for m in range(1,4):
            for W in range(1,4):
                rows=list(product(range(W),repeat=m))
                for X in range(0,16):
                    counts={r:0 for r in rows}
                    for xs in product(range(1,X+1),repeat=m):
                        if sum(xs)<=X:
                            counts[tuple(v%W for v in xs)]+=1
                    for r in rows:
                        got=residue_simplex_count(m,W,X,[r])
                        self.assertEqual(got,counts[r])
                        mean=Fraction(X,W)**m/factorial(m)
                        self.assertLessEqual(abs(got-mean),
                                             simplex_error_bound(m,W,X,1))

    def test_dimension_uniformity_and_guards(self):
        for m in (1,2,3,6,9):
            X=1000*m*m
            rel=simplex_relative_bound(m,1,X)
            ratio=Fraction(unrestricted_simplex_count(m,X)*factorial(m),X**m)
            self.assertLessEqual(1-ratio,rel)
            self.assertLess(rel,Fraction(1,20))
        with self.assertRaises(ExteriorAscentError):
            residue_simplex_count(2,3,12,[(0,0),(0,0)])
        with self.assertRaises(ExteriorAscentError):
            residue_simplex_count(2,3,12.0,[(0,0)])
        with self.assertRaises(ExteriorAscentError):
            residue_simplex_count(2,3,12,[(0,3)])
        with self.assertRaises(ExteriorAscentError):
            simplex_relative_bound(2,3,0)


class TestCofactorExterior(unittest.TestCase):
    def test_determinants_against_direct_formula(self):
        for a,b,c,d in product(range(-2,3),repeat=4):
            self.assertEqual(determinant(((a,b),(c,d))),a*d-b*c)
        self.assertEqual(determinant(((1,0,0),(0,1,0),(0,0,1))),1)
        self.assertEqual(determinant(((1,2,3),(4,5,6),(7,8,9))),0)

    def test_high_D_m2_singleton_and_cofactors(self):
        ds=(9,16,25)
        example=cofactor_certificate(ds,(1,1,1),25)
        self.assertEqual(example["D"],3600)
        self.assertTrue(example["high_divisor"])
        cert=exterior_certificate(ds,((9,16,25),(18,32,50)),50)
        self.assertEqual(cert["determinant"],0)
        self.assertTrue(cert["rank_drop_forced"])
        with self.assertRaises(ExteriorAscentError):
            exterior_certificate((2,2,1),((2,2,4),(4,4,8)),8)

    def test_high_D_three_summands_not_singleton(self):
        fam=rank_drop_family(1001,3)
        self.assertEqual(fam["D"],6037084083030)
        self.assertEqual(fam["X"],9015)
        self.assertEqual(fam["count"],2)
        self.assertGreater(fam["D"],fam["X"]**3)
        n=1001
        third=(n,4*(n+1),2*(2*n+1),3*(3*n+2))
        cert=exterior_certificate(fam["moduli"],(*fam["points"],third),fam["X"])
        self.assertEqual(cert["determinant"],0)
        self.assertTrue(cert["rank_drop_forced"])
        self.assertEqual(gcd(gcd(third[0],third[1]),third[2]),1)

    def test_unbounded_high_D_multiplicity(self):
        for K in (3,4,6,9):
            oddpart=lcm(*range(1,K))
            while oddpart%2==0:
                oddpart//=2
            n=oddpart
            while n <= 12*K**3:
                n+=2*oddpart
            fam=rank_drop_family(n,K)
            self.assertEqual(fam["count"],K-1)
            self.assertGreater(fam["D"],fam["X"]**3)

    def test_primitive_is_not_pairwise_in_dimension_three(self):
        xs=(6,10,15)
        self.assertEqual(gcd(gcd(xs[0],xs[1]),xs[2]),1)
        self.assertGreater(gcd(xs[0],xs[1]),1)

    def test_local_primitive_vs_pairwise_clock(self):
        from observational_succ.exterior_cofactor_ascent import local_prime_clock_factors
        from itertools import product
        for m in range(2,6):
            for p in (2,3,5):
                vals = list(product(range(p), repeat=m))
                exact_primitive = Fraction(sum(any(x != 0 for x in v) for v in vals),p**m)
                exact_pairwise = Fraction(sum(sum(x == 0 for x in v) <= 1 for v in vals),p**m)
                got=local_prime_clock_factors(m,p)
                self.assertEqual(got["primitive_gcd"],exact_primitive)
                self.assertEqual(got["pairwise_summands"],exact_pairwise)
        self.assertEqual(local_prime_clock_factors(3,2),
                         {"primitive_gcd":Fraction(7,8),"pairwise_summands":Fraction(1,2)})
        with self.assertRaises(ExteriorAscentError):
            local_prime_clock_factors(3,4)

    def test_locally_finite_infinite_weighted_carrier(self):
        # Sum of partition numbers p(0)+...+p(X), not a literal X^infinity.
        known=(1,2,4,7,12,19,30,45,67,97,139)
        for X,count in enumerate(known):
            self.assertEqual(weighted_infinite_count(X,range(1,X+1)),count)


if __name__ == "__main__":
    unittest.main()
