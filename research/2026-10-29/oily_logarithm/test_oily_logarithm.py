"""Finite exact falsification tests for SUCC Oily logarithm model."""
import unittest
from fractions import Fraction as Q
from itertools import product
from math import gcd, comb
import oily_logarithm as m

class OilyLogFiniteTests(unittest.TestCase):
    def test_original_four_pole_passport_and_seed(self):
        self.assertEqual(m.source_r(1),Q(47,15))
        self.assertEqual(m.bbp_history(0), (Q(0),))
        for n in (1,2,3,11,37):
            self.assertEqual(m.source_r(n), Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2))
            hist=m.bbp_history(n)
            self.assertEqual(hist[n]-16*hist[n-1], m.source_r(n))

    def test_scaled_source_moments_positive_and_gamma(self):
        for a,k in product((Q(1),Q(5),Q(37),Q(777)),range(7)):
            actual=m.source_scaled_moment(a,k)
            self.assertGreater(actual, 0)
            direct=Q(a**k)*__import__('math').factorial(k)*sum((Q(c,(a+d)**(k+1)) for d,c in m.POLES),Q())/m.source_R(a)
            self.assertEqual(actual,direct)

    def test_fourier_exact_symmetry_and_unit_value(self):
        for a,z in product((Q(1),Q(3),Q(8),Q(125),Q(987)),(Q(-3),Q(-1),Q(0),Q(1),Q(3),Q(2,7))):
            re,im=m.source_normalized_fourier(a,z)
            conjugate=m.source_normalized_fourier(a,-z)
            self.assertEqual((re,-im),conjugate)
            self.assertGreater(re*re+im*im,0)
            self.assertLessEqual(re*re+im*im,1)
            if z==0:self.assertEqual((re,im),(Q(1),Q()))
            if z==1:
                self.assertGreater(re,0)
                self.assertGreater(im,0)
                self.assertGreater(re*re+im*im,Q(1,4))

    def test_logarithmic_inversion_oily_twist(self):
        for a in (Q(1,7),Q(1),Q(2),Q(4),Q(9),Q(37),Q(16),Q(222)):
            ratio=m.source_inversion_ratio(a)
            exp=m.oily_inversion_exponential(a)
            self.assertEqual(ratio, (a/4)**3*exp)
            self.assertEqual(exp*m.oily_inversion_exponential(Q(16)/a), 1)
            self.assertEqual(exp-1, (a*a-16)/((3*a+16)*(5*a+16)))
            self.assertEqual(m.oily_inversion_tanh_half(a),
                             (exp-1)/(exp+1))
            self.assertLess(exp,Q(16,15))
            self.assertGreater(exp,Q(15,16))
            if a==4:self.assertEqual(exp,1)
            elif a>4:self.assertGreater(exp,1)
            else:self.assertLess(exp,1)

    def test_source_mirror_amplitude_and_phase(self):
        for a,t in ((Q(1),Q(1,3)),(Q(9),Q(2)),(Q(73),Q(13)),(Q(613),Q(19))):
            aff=m.mirror_source_density_product_ratio(a,t)
            self.assertEqual(aff*m.source_R(a+t)*m.source_R(a-t),m.source_R(a)**2)
            self.assertGreater(aff,0)
            self.assertLessEqual(aff,1)
            for n,s,h in product((0,1,2,8), (Q(0),Q(-1),Q(1,15),Q(7,24)), (1,3,-5)):
                self.assertEqual(m.mirror_phase_product_residue(n,s,h),0)
                plus=m.bbp_history(n,s)[n]
                minus=m.bbp_history(n,-s)[n]
                self.assertEqual((h*(plus-minus))%1, (2*h*16**n*s)%1)

    def test_literal_branch_cocycle_complete(self):
        for seed in (Q(),Q(-1),Q(-16),Q(1,15),Q(1,256),Q(7,24),Q(-13,29)):
            residues,carries=m.literal_carries(55,seed)
            self.assertEqual(len(carries),56)
            for k in range(1,56):
                self.assertEqual(16*residues[k-1]+m.source_r(k)-residues[k],carries[k])
                self.assertEqual(carries[k].denominator,1) if isinstance(carries[k],Q) else self.assertIsInstance(carries[k],int)

    def test_seed_offset_inertial_exact_differential(self):
        for seed,n in product((Q(-16),Q(-1),Q(0),Q(1,3),Q(1,15),Q(1,256)),(0,1,2,3,37,61)):
            history=m.bbp_history(n,seed)
            zero=m.bbp_history(n)
            self.assertEqual(history[n]-zero[n],16**n*seed)
            for k in range(1,n+1):
                self.assertEqual(history[k]/16**k-history[k-1]/16**(k-1),m.source_r(k)/16**k)

    def test_late_seed_phase_aliases(self):
        for n in range(8):
            self.assertEqual(m.seed_phase_shift(Q(-1),n),0)
            self.assertEqual(m.seed_phase_shift(Q(-16),n),0)
            self.assertEqual(m.seed_phase_shift(Q(1,15),n), Q(16**n,15)%1)
        self.assertNotEqual(m.seed_phase_shift(Q(1,256),1),0)
        self.assertEqual(m.seed_phase_shift(Q(1,256),2),0)

    def test_mirrored_branch_ternary_shape_and_q3_inversion(self):
        for x in (Q(),Q(1,15),Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(14,15),Q(63,64)):
            probs=m.mirrored_branch_probabilities(x)
            self.assertEqual(sum(probs.values(),Q()),1)
            self.assertTrue(all(z>=0 for z in probs.values()))
            re,imcoef=m.mirrored_branch_q3_character(x)
            self.assertEqual(re,1-Q(3,2)*abs(1-2*x))
            self.assertEqual(imcoef,(1-2*x)/2)
            self.assertEqual(Q(1,2)-imcoef,x)
            # Unlike q=3, the q=2 character loses orientation (x vs 1-x).
            q2=probs[0]-probs[-1]-probs[1]
            self.assertEqual(q2,1-2*abs(1-2*x))
        with self.assertRaises(ValueError):m.mirrored_branch_probabilities(1)

    def test_semantic_branch_actual_original_and_counterseed_controls(self):
        for n,seed,delta in product((0,1,2,3,7,13),
                                   (Q(),Q(1,7),Q(1,15),Q(-1),Q(1,256)),
                                   (Q(),Q(1,11),Q(7,33),Q(3,8),Q(31,48))):
            J=m.mirrored_branch_disagreement(n,seed,delta)
            x=m.bbp_history(n,seed)[n]%1
            theta=(16**n*delta)%1
            predicted=int(theta>x)-int(theta>=1-x)
            self.assertEqual(J,predicted)
        x1=m.bbp_history(1)[1]%1
        self.assertEqual(x1,Q(2,15))
        self.assertEqual(m.mirrored_branch_q3_character(x1),(Q(-1,10),Q(11,30)))
        for n in (1,2,3,7):
            # For the advanced seed -pi/16 the exact true state is -T_n;
            # approximate it with an explicit rational negative tail control,
            # without inserting a nonrational value into the exact arithmetic API.
            source_tail_upper=Q(1,(8*n+1)**2)
            x=1-source_tail_upper
            self.assertEqual(m.mirrored_branch_q3_character(x)[1],source_tail_upper-Q(1,2))

    def test_pascal_normalization_and_signed_log_linear_coefficient(self):
        for n in (0,1,2,5,11,22):
            a=Q(8*n-7) if n else Q(1)
            weights=m.grade_weights(n,a)
            self.assertEqual(sum(weights,Q()),1)
            self.assertTrue(all(w>0 for w in weights))
            deriv=m.score_weights(n,a)
            self.assertEqual(sum(deriv,Q()),0)
            readout=m.signed_pascal_log_derivative_group(n,a,seed=Q(1,15))
            self.assertEqual(sum(readout.values(),Q()),1)
            score=m.signed_pascal_log_cross_group(n,a,seed=Q(1,15))
            self.assertEqual(sum(score.values(),Q()),0)

    def test_phase_and_source_do_not_belong_to_same_type(self):
        for n in (1,3,7):
            a=8*n-7
            q=m.grade_weights(n,a)
            self.assertNotEqual(q, tuple(Q(1,n+1) for _ in range(n+1)))
            # The positive source never depends on seed, but signed phases do.
            self.assertEqual(q,m.grade_weights(n,a))
            z=m.signed_pascal_log_derivative_group(n,a,seed=Q())
            mutant=m.signed_pascal_log_derivative_group(n,a,seed=Q(1,7))
            self.assertNotEqual(z,mutant)

    def test_errors_and_bad_source_rejected(self):
        calls=(lambda:m.source_R(0),lambda:m.source_r(0),lambda:m.oily_inversion_exponential(0),
               lambda:m.source_normalized_fourier(0,1),
               lambda:m.source_normalized_fourier(1,0.5),
               lambda:m.source_scaled_moment(1,-1),
               lambda:m.bbp_history(-1),lambda:m.seed_phase_shift(Q(1,3),-1),
               lambda:m.literal_carries(-1),
               lambda:m.mirror_source_density_product_ratio(Q(1),Q(2)),
               lambda:m.grade_weights(-1,Q(1)),
               lambda:m.score_weights(1,Q(0)),
               lambda:m.signed_pascal_log_derivative_group(1,1,h=0))
        for call in calls:
            with self.subTest(call=call),self.assertRaises(ValueError):call()

if __name__ == '__main__': unittest.main(verbosity=2)
