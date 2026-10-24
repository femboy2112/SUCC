"""Hostile exact regression for minimal first carry and BBP Green no-go claims."""
import unittest
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import comb
from observational_succ.minimal_circle_carry import (
    exact_origin_moment,independent_origin_moment,first_carry_excess,
    first_carry_witness,no_carry_high_moment_bound,
    needed_alias_free_frame_labels,sufficient_grid_for_2k_moment,
    haar_bad_frame_upper,authentic_bbp_forcing,finite_green_section,
    finite_green_residual,finite_green_l1_control,
    finite_green_l2_ratio_squared,rational_nonnormal_green_tail,
    rational_nonnormal_forcing,zero_action_circle_origins,zero_chord_step)
from observational_succ.minimal_green_obstruction import (
    finite_intertwiner_obstruction,target_cycle_order,
    finite_green_iterate_norm_squared,rational_orbit_eventually_fixed,
    finite_stable_source_vs_circle)

class MomentFirstCarry(unittest.TestCase):
    def test_no_carry_moments_match_independent_phases(self):
        for base in (2,3,4,16):
            for N in (1,2,3,4,5):
                for k in sorted({0,1,2,base-1,base}):
                    lhs=exact_origin_moment(base,N,k)
                    rhs=independent_origin_moment(N,k)
                    self.assertEqual(lhs,rhs,(base,N,k))
                    self.assertLessEqual(lhs,no_carry_high_moment_bound(base,N,k))

    def test_first_carry_excess_full_arithmetic(self):
        for base in (2,3,4,6,16):
            for N in (1,2,3,4,5):
                lhs=exact_origin_moment(base,N,base+1)
                baseline=independent_origin_moment(N,base+1)
                self.assertEqual(lhs-baseline,first_carry_excess(base,N))
                if N>=3:
                    self.assertGreater(lhs,baseline)
        self.assertEqual(first_carry_excess(16,3),34)
        self.assertEqual(first_carry_excess(16,4),646)
        self.assertEqual(first_carry_excess(16,5),1836)

    def test_independent_ordered_tuple_oracle(self):
        for base,N,k in ((2,3,3),(2,4,3),(3,4,4),(4,4,5)):
            values=Counter(sum(base**j for j in t)
                           for t in product(range(N),repeat=k))
            self.assertEqual(sum(z*z for z in values.values()),
                             exact_origin_moment(base,N,k))

    def test_first_carry_relation_and_wide_gap(self):
        for base in (2,3,16):
            for earliest in (0,1,3):
                for gap in (2,3,5):
                    a,c=first_carry_witness(base,earliest,gap)
                    self.assertNotEqual(a,c)
                    self.assertEqual(sum(a),base+1)
                    self.assertEqual(sum(c),base+1)
        with self.assertRaises(ValueError):
            first_carry_witness(16,0,1)

    def test_finite_origin_frame_resources(self):
        for base,N,k in ((2,4,2),(3,3,3),(16,3,4),(16,4,5)):
            m=k*base**(N-1)+1
            self.assertTrue(sufficient_grid_for_2k_moment(base,N,k,m))
            self.assertEqual(exact_origin_moment(base,N,k,modulus=m),
                             exact_origin_moment(base,N,k))
            self.assertLessEqual(needed_alias_free_frame_labels(base,N,k),m)
        self.assertGreater(exact_origin_moment(16,3,1,modulus=15),
                           exact_origin_moment(16,3,1))
        self.assertEqual(needed_alias_free_frame_labels(16,100,16),
                         14980162794189827475)
        with self.assertRaises(ValueError):
            needed_alias_free_frame_labels(16,3,17)

    def test_high_moment_exception_bound_is_ensemble_only(self):
        k,prob=haar_bad_frame_upper(16,100,Q(1,2))
        self.assertEqual(k,16)
        self.assertLess(prob,Q(1,10**6))
        self.assertEqual(haar_bad_frame_upper(16,1,Q(1,2))[1],1)
        with self.assertRaises(ValueError):
            haar_bad_frame_upper(16,100,0)

    def test_source_blind_minimal_geometric_action_is_nonnormal(self):
        for base in (2,3,16):
            m=zero_action_circle_origins(base)
            self.assertEqual(len(m),base-1)
            self.assertTrue(all(zero_chord_step(base,x) for x in m))
            self.assertFalse(zero_chord_step(base,Q(1,base)))
        self.assertEqual(zero_action_circle_origins(16)[-1],Q(14,15))

    def test_source_guard_and_computational_cap(self):
        with self.assertRaises(ValueError):
            exact_origin_moment(1,3,1)
        with self.assertRaises(ValueError):
            exact_origin_moment(16,8,17,max_states=100)
        with self.assertRaises(ValueError):
            no_carry_high_moment_bound(16,3,17)

class GreenMinimalPath(unittest.TestCase):
    def test_authentic_rational_bbp_residual(self):
        for n in (0,1,2,10,50):
            for K in (1,2,3,8):
                residual=finite_green_residual(n,K)
                self.assertEqual(residual,-authentic_bbp_forcing(n+K+1)/16**K)
                self.assertLess(residual,0)
        self.assertEqual(authentic_bbp_forcing(1),Q(47,15))

    def test_finite_source_l1_l2_sharpness(self):
        for base in (2,3,16):
            for N in (1,2,8,64):
                source=[Q(1,j+1) for j in range(N)]
                x,y,z=finite_green_l1_control(source,base)
                self.assertTrue(all(v>=0 for v in z))
                self.assertLess(y,x/(base-1))
            self.assertLess(finite_green_l2_ratio_squared(10,base),
                            Q(1,(base-1)**2))
            self.assertLess(finite_green_l2_ratio_squared(100,base),
                            Q(1,(base-1)**2))
            self.assertGreater(finite_green_l2_ratio_squared(100,base),
                               finite_green_l2_ratio_squared(10,base))
        with self.assertRaises(ValueError):
            finite_green_l1_control([-1,2])

    def test_same_minimal_energy_principle_can_select_fixed_circle(self):
        for n in range(1,50):
            self.assertGreater(rational_nonnormal_forcing(n),0)
            self.assertEqual(rational_nonnormal_forcing(n),
                16*rational_nonnormal_green_tail(n-1)-rational_nonnormal_green_tail(n))
        self.assertEqual(rational_nonnormal_green_tail(0),Q(1,2))
        self.assertEqual((16*rational_nonnormal_green_tail(0))%1,0)

class HilbertTimeNoGo(unittest.TestCase):
    def test_exact_permutation_isometry_vs_source_contraction(self):
        for p in ((0,),(1,2,0),(1,0,3,2),(1,2,3,0)):
            L,factors=finite_intertwiner_obstruction((Q(1,2),Q(15,16),0),p)
            self.assertEqual(L,target_cycle_order(p))
            self.assertEqual(factors[0],1-Q(1,2)**L)
            self.assertTrue(all(z>0 for z in factors))
        with self.assertRaises(ValueError):
            finite_intertwiner_obstruction((Q(1,2),Q(1)),(1,0))
        with self.assertRaises(ValueError):
            finite_intertwiner_obstruction((Q(1,2),),(1,1))

    def test_strong_not_uniform_decay(self):
        for n in (1,2,10,30):
            eps=Q(1,2**(n+10))
            self.assertGreater(
                finite_green_iterate_norm_squared((1-eps,),(1,),n),Q(1,2))
            self.assertLess(
                finite_green_iterate_norm_squared((Q(1,2),),(1,),n),1)

    def test_rational_preperiodic_controls_not_pi(self):
        self.assertEqual(rational_orbit_eventually_fixed(16,Q(1,16),5),1)
        self.assertEqual(rational_orbit_eventually_fixed(16,Q(1,3),5),0)
        self.assertIsNone(rational_orbit_eventually_fixed(16,Q(1,7),5))
        self.assertEqual(rational_orbit_eventually_fixed(2,Q(1,8),5),3)

    def test_small_decaying_source_can_have_nondecaying_circle_phase(self):
        pts=finite_stable_source_vs_circle(16,Q(1,2),Q(1,3),12)
        self.assertEqual(pts[-1][0],Q(1,2048))
        self.assertTrue(all(phase==Q(1,3) for _,phase in pts))
        with self.assertRaises(ValueError):
            finite_stable_source_vs_circle(16,Q(1),Q(1,3),10)

if __name__=="__main__":
    unittest.main()
