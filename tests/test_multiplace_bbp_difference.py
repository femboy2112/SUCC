"""Finite original-source tests for the three-place BBP resolvent and pole spectrum.

Quantified infinite claims are paper proofs in the research dossier; these
integer/Fraction tests calibrate genuine finite arithmetic only.
"""
import sys
import unittest
from fractions import Fraction as F
from math import comb, gcd
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1] /
    "research" / "2026-10-31" / "multiplace_bbp_difference"))

from multiplace_difference import (
    POLES,valuation,bbp_source,original_denominator,
    positive_moment_polynomial,source_arch_moment,
    source_two_point_arch,source_moment_coefficient,
    pole_depth_three,pole_depth_profile,truncated_mean_pole_depth,
    resolvent_certificate,exact_pole_slope,small_shift_valuation,
    joint_dyadic_pole_classes,prime_exposure,real_positive_tail_limit,
)


class MultiplaceBBPDifferenceTests(unittest.TestCase):
    def test_01_original_four_poles_and_positive_factorization(self):
        for y in range(-50,80):
            self.assertEqual(
                bbp_source(y),
                F(120*y*y-89*y+16,original_denominator(y)))
        for j in range(0,101):
            t=F(j,100)
            self.assertEqual(positive_moment_polynomial(t),
                             4-2*t**3-t**4-t**5)
            self.assertGreaterEqual(positive_moment_polynomial(t),0)

    def test_02_exact_archimedean_moment(self):
        for y in range(1,85):
            self.assertEqual(source_arch_moment(y),bbp_source(y))
            self.assertGreater(bbp_source(y),0)
        for x in range(1,16):
            for y in range(x+1,32):
                self.assertEqual(source_two_point_arch(x,y),
                                 bbp_source(x)-bbp_source(y))
                self.assertGreater(source_two_point_arch(x,y),0)

    def test_03_exact_complete_monotonicity(self):
        for y in range(1,14):
            for k in range(0,9):
                diff=sum(((-1)**j*comb(k,j)*bbp_source(y+j)
                           for j in range(k+1)),F(0))
                self.assertGreater(diff,0)

    def test_04_gamma_moments_positive_and_original_C0(self):
        for y in range(1,80):
            self.assertEqual(source_moment_coefficient(y,0),bbp_source(y))
            for j in range(0,12):
                self.assertGreater(source_moment_coefficient(y,j),0)

    def test_05_three_place_exact_remainder_and_norm_budgets(self):
        for m in range(2,9):
            y=1+6**m
            for J in (1,2,3,4,5,8):
                z=resolvent_certificate(y,6**m,J)
                self.assertEqual(z["exact"],z["prefix"]+z["remainder"])
                self.assertLess(abs(z["remainder"]),z["real_error_upper"])
                self.assertGreaterEqual(valuation(z["remainder"],2),
                                        z["v2_remainder_lower"])
                self.assertGreaterEqual(valuation(z["remainder"],3),
                                        z["v3_remainder_lower"])
                self.assertEqual(z["v2_exact"],m)
                self.assertEqual(z["v3_exact"],m-2)

    def test_06_three_place_resolvent_other_source_points(self):
        for m in (3,4,5,6):
            h=6**m
            for x in range(1,23):
                y=x+h
                if m<=pole_depth_three(y):
                    continue
                for J in (1,3,6):
                    z=resolvent_certificate(y,h,J)
                    self.assertEqual(z["exact"],bbp_source(x)-bbp_source(y))
                    self.assertGreaterEqual(valuation(z["remainder"],2),
                                            z["v2_remainder_lower"])
                    self.assertGreaterEqual(valuation(z["remainder"],3),
                                            z["v3_remainder_lower"])

    def test_07_exact_prime_three_slope_and_prime_two_slope(self):
        for y in range(-400,401):
            d=pole_depth_three(y)
            self.assertEqual(valuation(exact_pole_slope(y),3),-2*d)
            self.assertEqual(valuation(exact_pole_slope(y),2),0)

    def test_08_exact_improved_prime_three_difference(self):
        for y in range(-37,38):
            for m in range(pole_depth_three(y)+1,
                           min(pole_depth_three(y)+4,9)):
                z=small_shift_valuation(y,m)
                self.assertEqual(z["v2_exact"],m)
                self.assertEqual(z["v3_exact"],m-2*z["pole_depth"])
                self.assertEqual(z["v3_formula"],z["v3_exact"])

    def test_09_previous_denominator_pole_bound_was_not_sharp(self):
        for y in (2,5,8,11,14,16):
            d=pole_depth_three(y)
            dprod=valuation(original_denominator(y),3)
            self.assertGreater(dprod,d)
            m=dprod+2
            z=small_shift_valuation(y,m)
            self.assertGreater(z["v3_exact"],m-2*dprod)

    def test_10_exact_prime_three_pole_classes(self):
        for k in range(1,9):
            z=pole_depth_profile(k)
            self.assertEqual(len(z["roots"]),3 if k==1 else 4)
            self.assertEqual(z["tail_fraction"],
                    F(1) if k==1 else F(4,3**k))
            direct={y for y in range(3**k)
                    if pole_depth_three(y)>=k}
            self.assertEqual(direct,set(z["roots"]))

    def test_11_exact_average_pole_depth(self):
        for K in range(1,8):
            depths=[min(pole_depth_three(y),K)
                    for y in range(3**K)]
            self.assertEqual(F(sum(depths),len(depths)),
                             truncated_mean_pole_depth(K))
        self.assertEqual(truncated_mean_pole_depth(1),1)
        self.assertEqual(truncated_mean_pole_depth(2),F(13,9))

    def test_12_source_2adic_residues_independent_of_3adic_pole_depth(self):
        for a,K in ((2,2),(4,2),(4,3),(5,3),(4,4)):
            z=joint_dyadic_pole_classes(a,K)
            self.assertTrue(z["factorizes"])
            self.assertEqual(sum(z["counts"].values()),z["period"])
            self.assertEqual(sum(z["depth_counts"].values()),3**K)

    def test_13_exact_bad_pole_fraction_and_good_source_precision(self):
        for m in range(2,7):
            z=pole_depth_profile(m)
            self.assertEqual(z["tail_fraction"],F(4,3**m))
            self.assertEqual(1-z["tail_fraction"],1-F(4,3**m))
            for y in range(1,200):
                if pole_depth_three(y)<m:
                    self.assertEqual(small_shift_valuation(y,m)
                                     ["v3_exact"],m-2*pole_depth_three(y))

    def test_14_external_prime_denominator_growth(self):
        prev=F(0)
        for m in range(2,10):
            z=prime_exposure(m)
            self.assertTrue(F(3)<z["delta"]<F(47,15))
            self.assertGreater(z["delta"],prev)
            self.assertEqual(gcd(z["denominator"],6),1)
            self.assertEqual(z["v2"],m)
            self.assertEqual(z["v3"],m-2)
            self.assertGreater(z["denominator"],z["denominator_lower_bound"])
            prev=z["delta"]

    def test_15_same_rational_has_three_distinct_limit_signatures(self):
        for m in range(2,10):
            z=prime_exposure(m)
            self.assertEqual(real_positive_tail_limit(m),z["delta"])
            self.assertLess(F(0),F(47,15)-z["delta"])
            self.assertLess(F(47,15)-z["delta"],F(1,6**m))
            self.assertGreaterEqual(z["v2"],m)
            self.assertGreaterEqual(z["v3"],m-2)

    def test_16_convergence_is_broken_if_a_pole_is_3adically_close(self):
        for y in range(1,100):
            d=pole_depth_three(y)
            if d<1:continue
            h=6**d
            if y<=h:continue
            with self.assertRaises(ValueError):
                resolvent_certificate(y,h,4)

    def test_17_rational_Cj_leading_source_is_not_a_separate_positive_model(self):
        for y in range(1,31):
            c=source_moment_coefficient(y,1)
            self.assertEqual(-8*c,exact_pole_slope(y))
            self.assertLess(exact_pole_slope(y),0)
            self.assertEqual(valuation(c,2),-3)
            self.assertEqual(valuation(c,3),-2*pole_depth_three(y))


if __name__=="__main__":
    unittest.main()
