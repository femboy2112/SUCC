"""Scoped exact finite regression; no inference about pi normality."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import unittest
from fractions import Fraction as F
from math import comb, factorial, gcd
import opposing_observers as o

class SourceTests(unittest.TestCase):
    def test_four_poles_and_source(self):
        self.assertEqual(o.bbp_forcing(1),F(47,15))
        for n in (1,2,3,37,61,97):
            self.assertEqual(o.bbp_forcing(n), sum((F(v,8*n-7+d) for d,v in o.POLES),F()))
            self.assertTrue(o.bbp_forcing(n)>0)
    def test_identity_pair_normalization(self):
        for a in (F(1),F(4),F(9),F(67),F(23,8)):
            for rho in (F(0),F(1,7),F(1,2),F(3,4)):
                t=a*rho
                self.assertEqual(o.disagreement_moment(a,t,0),1)
                self.assertEqual(o.product_normalizer(a,t)*o.hellinger_squared(a,t),1)
    def test_independent_first_two_moments(self):
        for a in (F(1),F(13),F(71)):
            for t in (F(0),a/4,a/2):
                m=o.source_mean(a+t)-o.source_mean(a-t)
                self.assertEqual(o.disagreement_moment(a,t,1),m)
                v1= -o.R_prime(a+t)/o.R(a+t)
                v2= -o.R_prime(a-t)/o.R(a-t)
                self.assertEqual(v1-v2,m)
                self.assertGreater(o.disagreement_moment(a,t,2)-m*m,0)
    def test_overlap_brackets(self):
        for a in (F(1),F(2),F(9),F(123),F(999)):
            for rho in (F(1,17),F(1,3),F(7,11),F(9,10)):
                t=a*rho; L,U=o.overlap_bounds_squared(a,t)
                self.assertLess(L,o.hellinger_squared(a,t));self.assertLess(o.hellinger_squared(a,t),U)
    def test_moment_symmetry(self):
        for a in (F(1),F(9),F(51)):
            for m in (1,3,5): self.assertEqual(o.disagreement_moment(a,0,m),0)
        self.assertEqual(o.disagreement_moment(F(9),F(4),1)<0,True)
    def test_seed_formal_phase_aliases(self):
        for n in range(1,8):
            for a in (8*n-7,(8*n-7)*F(3,2)):
                zero=o.signed_phase_readout_formal(n,a)
                self.assertEqual(zero,o.signed_phase_readout_formal(n,a,-1))
                self.assertEqual(zero,o.signed_phase_readout_formal(n,a,-16))
    def test_paired_pascal_instrument(self):
        for n in range(1,21):
            a=F(8*n-7)
            for u in (F(0),a/3):
                for c in (a+u,a-u):
                    weights=o.grade_probabilities(n,c)
                    self.assertEqual(sum(weights),1)
                    self.assertTrue(all(w>0 for w in weights))
                    self.assertEqual(sum((j*w for j,w in enumerate(weights)),F()),o.grade_mean(n,c))
    def test_exact_directional_source_score(self):
        for n in range(1,12):
            a=F(8*n-7)
            q=o.grade_derivative(n,a)
            self.assertEqual(sum(q,F()),0)
            score=o.directional_phase_score_formal(n,a)
            self.assertEqual(sum(score.values(),F()),0)
            self.assertEqual(score,o.directional_phase_score_formal(n,a,-1))
        self.assertNotEqual(o.directional_phase_score_formal(1,F(1)),{})

    def test_n1_noncentral_character(self):
        n=1;a=F(1);t=F(1,3)
        plus=o.signed_phase_readout_formal(n,a+t)
        minus=o.signed_phase_readout_formal(n,a-t)
        self.assertNotEqual(plus,minus)
        self.assertEqual(sum(plus.values()),sum(minus.values()))
        self.assertEqual(sum(plus.values()),1)
    def test_input_validation(self):
        for fn in (lambda:o.R(0),lambda:o.R(1.0),lambda:o.validate(1,1),
                   lambda:o.validate(0,0),lambda:o.validate(1,-1),
                   lambda:o.disagreement_moment(1,0,-1),lambda:o.grade_probabilities(-1,1),
                   lambda:o.bbp_history(-1),lambda:o.signed_phase_readout_formal(1,1,frequency=0)):
            with self.assertRaises(ValueError):fn()
    def test_source_clock_seed(self):
        h=o.bbp_history(15)
        self.assertEqual(h[0],0)
        for n in range(1,16):self.assertEqual(h[n]-16*h[n-1],o.bbp_forcing(n))

if __name__=='__main__':unittest.main(verbosity=2)
