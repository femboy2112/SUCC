"""Fourteen-plus exact local tests for the source-selected 2×3 joint clock.

Only mathematical finite controls; analytic solenoid and no-go theorems
are paper-level. No pi normality or RH is asserted.
"""
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1] /
  "research" / "2026-10-31" / "two_three_joint_carrier"))
from two_three_carrier import (
 bbp_r,original_states,two_mod_states,rational_mod_two,three_clock,
 clock_period,clock_modulus,joint_clock_counts,local_character_histogram,
 hats,empirical_hats,tripling_refine_hat,tripling_carry,
 certified_selected_tripling_carry,tripling_hat_defect,
 tripling_transport_certificate,v_p_rational,rational_circle_phase,
 periodic_character_control)

class TwoThreeCarrierTests(unittest.TestCase):
    def test_01_source_exact_four_poles_and_modular_lift(self):
        for n in range(1,70):
            self.assertEqual(bbp_r(n),
                 Fraction(4,8*n-7)-Fraction(2,8*n-4)
                 -Fraction(1,8*n-3)-Fraction(1,8*n-2))
            self.assertEqual(bbp_r(n).denominator%2,1)
        exact=original_states(60)
        for a in (4,8,10):
            self.assertEqual(two_mod_states(60,a),
                tuple(rational_mod_two(x,a) for x in exact))

    def test_02_selected_two_adic_isometry_finite_holdout(self):
        states=original_states(65)
        def v2(n):
            v=0
            while n%2==0:n//=2;v+=1
            return v
        for i in range(65):
            for j in range(i+1,65):
                self.assertEqual(v_p_rational(states[j]-states[i],2),v2(j-i))

    def test_03_three_adic_lte_and_primitive_time_clock(self):
        for b in range(1,7):
            L=clock_period(b)
            self.assertEqual(three_clock(L,b),1)
            self.assertEqual({three_clock(n,b) for n in range(L)},
                {u for u in range(1,3**b) if u%3==1})
        for n in range(1,128):
            self.assertEqual(v_p_rational(Fraction(16**n-1),3),
                             1+v_p_rational(Fraction(n),3))

    def test_04_joint_crt_every_fiber_exact_once(self):
        for a,b in ((4,1),(4,2),(4,3),(8,2)):
            for start in (0,17):
                z=joint_clock_counts(a,b,start)
                self.assertTrue(z['all_equal'])
                self.assertEqual(z['expected_cells'],z['period'])
                self.assertEqual(set(z['counts'].values()),{1})

    def test_05_any_horizon_has_floor_ceil_exact_product_counts(self):
        a,b=4,3
        z=joint_clock_counts(a,b)
        M=z['period']
        for N in (1,11,M-1,M,M+3,2*M+19):
            states=two_mod_states(N,a)
            cnt=Counter((states[t],three_clock(t,b)) for t in range(N))
            self.assertTrue(all(cnt.get(pair,0) in (N//M,N//M+1)
                 for pair in z['counts']))

    def test_06_exact_local_product_character_orthogonality(self):
        for a,b in ((4,2),(4,3),(8,2)):
            for r,s in ((0,0),(1,0),(0,1),(1,1),(2,2),(8,1)):
                x=local_character_histogram(a,b,r,s)
                self.assertTrue(x['uniform_roots'])
                self.assertTrue(x['zero_mean'])

    def test_07_rational_tripling_digit_carry(self):
        for q in (16,48,256):
            for d in (5,17,31,127):
                for n in range(-80,81,13):
                    left,c,right=tripling_carry(Fraction(n,d),q)
                    self.assertIn(c,(0,1,2))
                    self.assertEqual(right,(3*left+c)%q)

    def test_08_exact_threefold_hat_refinement(self):
        for q in (16,256):
            for x in (Fraction(0),Fraction(1,31),Fraction(-7,18),
                       Fraction(2048,2053),Fraction(371,191)):
                self.assertTrue(tripling_refine_hat(x,q))

    def test_09_certified_original_pi_selected_real_carries(self):
        digits="243f6a8885a308d313"
        for n in range(1,18):
            r=certified_selected_tripling_carry(n,16,65)
            self.assertEqual(r['digit'],int(digits[n-1],16))
            self.assertEqual(r['tripled_digit'],
                             (3*r['digit']+r['carry'])%16)
        for n in range(1,19):
            r=certified_selected_tripling_carry(n,256,65)
            self.assertLess(r['strict_width'],Fraction(1,1000000))

    def test_10_actual_source_to_completed_tripling_budget(self):
        for N,q in ((16,16),(64,16),(128,16),(20,256)):
            r=tripling_transport_certificate(N,q,24)
            self.assertLessEqual(r['observed'],r['certified_bound'])
            self.assertLess(r['certified_bound'],r['universal_upper'])
            self.assertLess(r['missing_tail_upper'],Fraction(1,1000))

    def test_11_source_3adic_poles_not_clock_units(self):
        seq=original_states(9)
        self.assertEqual(v_p_rational(seq[1],3),-1)
        self.assertEqual(v_p_rational(seq[2],3),-2)
        self.assertEqual(v_p_rational(seq[7],3),-3)
        self.assertEqual(three_clock(2,2)%3,1)

    def test_12_infinite_circle_dual_finite_subgroup_is_not_the_circle(self):
        for N in (2,3,6,48):
            self.assertEqual(rational_circle_phase(0,N,Fraction(1)),
                             rational_circle_phase(N,N,Fraction(1)))
            self.assertNotEqual(rational_circle_phase(0,N,Fraction(1,2)),
                                rational_circle_phase(N,N,Fraction(1,2)))

    def test_13_periodic_factors_and_prime_five_obstruction(self):
        self.assertTrue(periodic_character_control(Fraction(1,17),2))
        self.assertFalse(periodic_character_control(Fraction(1,17),1))
        self.assertTrue(periodic_character_control(Fraction(1,16**3-1),3))
        self.assertTrue(periodic_character_control(Fraction(1,16**5-1),5))
        self.assertFalse(any(clock_modulus(a,b)%5==0
                             for a in range(1,6) for b in range(1,6)))

    def test_14_tripling_invariance_not_automatic_or_haar(self):
        x=Fraction(1,5)
        self.assertEqual(16*x%1,x)
        self.assertNotEqual(3*x%1,x)
        self.assertNotEqual(hats(x,16),hats(3*x,16))
        self.assertEqual(hats(0,16),hats(3*0,16))
        self.assertEqual(sum(abs(v-Fraction(1,16))
                    for v in empirical_hats([0]*20,16)),2-Fraction(2,16))

    def test_15_sparse_irrational_has_zero_digit_frequency(self):
        # This exact finite control illustrates the paper proof:
        # alpha=sum_(j>=1)16^(-2^j) is irrational, nonnormal;
        # Vinogradov still proves p*alpha uniformly distributed mod 1.
        for k in range(5,12):
            N=2**k
            occupied=sum(1 for j in range(1,k+1) if 2**j<=N)
            self.assertEqual(occupied,k)
            self.assertLess(Fraction(occupied,N),Fraction(1,5))


class IndependentBackwardSourceTests(unittest.TestCase):
    def test_16_backward_green_matches_original_zero_selected_forward(self):
        from two_three_carrier import independent_backward_f2_residue
        for a in (4,8,12,16):
            forward=two_mod_states(100,a)
            self.assertEqual(independent_backward_f2_residue(0,a),0)
            for t in range(101):
                self.assertEqual(independent_backward_f2_residue(t,a),forward[t])


class ExceptionalBorelSourceTests(unittest.TestCase):
    def test_17_measurable_null_orbit_decoder_source_faithful(self):
        from two_three_carrier import exceptional_integer_orbit_phase
        for a in (Fraction(1,17), Fraction(3,7), Fraction(47,15)):
            self.assertEqual(exceptional_integer_orbit_phase(0,a),a%1)
            for n in range(-20,20):
                self.assertEqual((16*exceptional_integer_orbit_phase(n,a))%1,
                    exceptional_integer_orbit_phase(n+1,a))


class DualSpectralCarrierTests(unittest.TestCase):
    def test_18_exact_rank_two_spectral_actions_and_sparse_density(self):
        from two_three_carrier import solenoid_dual_shift,semigroup_16_3_below
        for x in (Fraction(1),Fraction(1,6),Fraction(-5,72)):
            for a,b in ((-3,5),(0,0),(2,-4),(7,3)):
                self.assertEqual(
                    solenoid_dual_shift(solenoid_dual_shift(x,a,0),0,b),
                    solenoid_dual_shift(solenoid_dual_shift(x,0,b),a,0))
        with self.assertRaises(ValueError):
            solenoid_dual_shift(Fraction(1,5),1,1)
        for X in (16,100,1000,100000,100000000):
            vals=semigroup_16_3_below(X)
            self.assertEqual(len(vals),len(set(vals)))
            self.assertEqual(vals[0],1)
            self.assertTrue(all(v<=X for v in vals))
            import math
            bound=(int(math.log(X,16))+1)*(int(math.log(X,3))+1)
            self.assertLessEqual(len(vals),bound)
        self.assertLess(len(semigroup_16_3_below(100000000)),1000)

if __name__=="__main__":
    unittest.main()
