"""Independent finite identities and mutations, not an all-n numerical proof."""
import unittest
from fractions import Fraction
from math import comb, log
from finite_source_triangle import (R,r,word_weight,q,next_probabilities,
 triangle_row,shifted_triangle_row,harmonic,harmonic_from_paths,
 harmonic_from_source,bbp_harmonic,gamma_matched_harmonic,
 bbp_state,fractional,literal_carry,two_step_carry,graded_selected_points)


class TriangleExact(unittest.TestCase):
    def test_source_pasport(self):
        for n in range(1,16):
            a=8*n-7
            self.assertEqual(r(n),4/Fraction(a)-2/Fraction(a+3)-1/Fraction(a+4)-1/Fraction(a+5))
            self.assertGreater(r(n),0)

    def test_exact_row_superposition(self):
        for a in [1,9,17,25,41]:
            for m in range(0,8):
                row=triangle_row(a,m)
                self.assertEqual(row,tuple(q(a,m,j) for j in range(m+1)))
                self.assertEqual(sum(row),1)
                self.assertTrue(all(v>0 for v in row))
                for j in range(m+1):
                    self.assertEqual(q(a,m,j),comb(m,j)*word_weight(a,m,j))
                    fail,success=next_probabilities(a,m,j)
                    self.assertEqual(fail+success,1)
                    self.assertTrue(0<fail<1 and 0<success<1)

    def test_source_shift_triangle(self):
        for a in [1,9,17,25]:
            for m in range(0,8):
                row=shifted_triangle_row(a,m)
                self.assertEqual(row,tuple(q(a,m,j) for j in range(m+1)))

    def test_pascal_path_exchangeability_and_posterior(self):
        # Two paths 01 and 10 must lead to the identical endpoint posterior.
        for a in [1,9,17,33]:
            fail,_=next_probabilities(a,0,0)
            _,s01=next_probabilities(a,1,0)
            _,s1=next_probabilities(a,0,0)
            f10,_=next_probabilities(a,1,1)
            self.assertEqual(fail*s01,s1*f10)
            self.assertEqual(fail*s01,word_weight(a,2,1))

    def test_harmonic_two_paths(self):
        for a in [1,9,17,25]:
            for m in range(0,10):
                self.assertEqual(harmonic_from_paths(a,m),harmonic_from_source(a,m))
                if m:
                    difference=harmonic_from_source(a,m)-harmonic_from_source(a,m-1)
                    self.assertEqual(difference,(1-R(a+8*m)/R(a))/m)

    def test_selected_seed_not_created_by_sensor(self):
        # Same forcing, different deterministic s. Sensor q has no seed argument.
        for n in range(1,10):
            a=8*n-7
            self.assertEqual(sum(q(a,n,j) for j in range(n+1)),1)
            self.assertTrue(0<q(a,n,0)<1)

    def test_exact_circle_carry_cocycle_and_selected_sensor(self):
        for seed in (Fraction(0),Fraction(1,7),Fraction(-1,5),Fraction(13,16)):
            for n in range(1,18):
                self.assertEqual(two_step_carry(n,seed),
                                 16*literal_carry(n,seed)+literal_carry(n+1,seed))
                x=fractional(bbp_state(n,seed))
                self.assertTrue(0 <= x < 1)
            for n in range(1,8):
                marked=graded_selected_points(n,seed)
                self.assertEqual(sum(weight for _,weight,_,_ in marked),1)
                for j,weight,phase,carry in marked:
                    self.assertEqual(weight,q(8*n-7,n,j))
                    self.assertEqual(phase,fractional(bbp_state(n+j,seed)))
                    self.assertEqual(carry,literal_carry(n+j,seed))

    def test_finite_first_jet_calibration_only(self):
        target=0.5+log(2)
        # Scope: finite observations numerically consistent with paper asymptotics.
        for n in (60,120,240):
            original=float(bbp_harmonic(n))
            fake=float(gamma_matched_harmonic(n))
            self.assertLess(abs(n*(original-target)+49/320),0.02)
            self.assertLess(abs(n*(fake-target)-1/32),0.02)
            self.assertLess(abs(n*(original-fake)+59/320),0.02)

if __name__=='__main__':
    unittest.main()
