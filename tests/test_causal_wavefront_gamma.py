"""Adversarial exact controls for causal-horizon / gamma conjecture."""
from __future__ import annotations
import unittest
from fractions import Fraction as F
from math import log

from observational_succ.causal_wavefront_gamma import (
    Event,can_signal,frontier_event,max_speed_one_behind,harmonic,
    near_null_lag_discrete,near_null_lag_continuous,sampled_clock_gap,
    standard_binary_entropy,uniform_frontier_residual_bound,
    original_oily_L_at,original_oily_R_at,
    finite_beta_jet_kl,gamma_jet_symmetric_divergence,
    pell_boost_certificate,pell_lorentz_null_identity,
)

GAMMA = .5772156649015328606  # numerical oracle, NOT a proof of gamma

class CausalWavefrontTests(unittest.TestCase):
    def test_one_behind_cannot_observe_current_front(self):
        for t in range(1,30):
            observer=max_speed_one_behind(t)
            self.assertFalse(can_signal(frontier_event(t),observer))
            self.assertTrue(can_signal(frontier_event(t-1),observer))
            self.assertFalse(can_signal(frontier_event(t+1),observer))

    def test_exact_finite_speed_obstruction(self):
        for t in range(1,30):
            observer=max_speed_one_behind(t)
            self.assertEqual(observer.position,t-1)
            self.assertEqual(frontier_event(t).position-observer.position,1)
            # Keeping this gap requires null-speed displacement +1 every step.
            if t>1:
                self.assertEqual(observer.position-max_speed_one_behind(t-1).position,1)

    def test_lagged_information_not_necessarily_uncertain(self):
        # Deterministic frontier bit B_t=B_(t-1) is predictable from the past.
        self.assertEqual(standard_binary_entropy(F(0)),0)
        self.assertEqual(standard_binary_entropy(F(1)),0)
        # Fresh fair bit is provably independent of the entire previous history.
        self.assertEqual(standard_binary_entropy(F(1,2)),1)
        # Nonuniversal biased innovations give intermediate residual entropy.
        self.assertGreater(standard_binary_entropy(F(1,4)),0)
        self.assertLess(standard_binary_entropy(F(1,4)),1)

    def test_information_budget_lower_bound(self):
        self.assertEqual(uniform_frontier_residual_bound(8,3),5)
        self.assertEqual(uniform_frontier_residual_bound(8,8),0)
        self.assertEqual(uniform_frontier_residual_bound(8,12),0)
        with self.assertRaises(ValueError):uniform_frontier_residual_bound(-1,5)

class HarmonicPursuitTests(unittest.TestCase):
    def test_same_initial_position_and_valid_speed(self):
        for a in (F(1,4),F(1,2),F(1)):
            self.assertEqual(near_null_lag_discrete(0,a),1)
            self.assertEqual(near_null_lag_continuous(0,a),1)
            for n in range(1,25):
                d=near_null_lag_discrete(n,a)-near_null_lag_discrete(n-1,a)
                self.assertEqual(d,a/F(n))
                self.assertLessEqual(0,F(1)-a/F(n))
                self.assertLess(F(1)-a/F(n),1)

    def test_euler_gamma_limit_and_nonuniversality(self):
        for a in (F(1),F(1,2),F(1,4)):
            x=sampled_clock_gap(4000,a)
            self.assertGreater(x,0)
            self.assertLess(abs(x-float(a)*GAMMA),.0003)
        self.assertLess(sampled_clock_gap(1000,F(1,2)),sampled_clock_gap(1000,F(1)))

    def test_exact_clock_is_sampling_defect_not_curvature(self):
        for n in (1,2,3,8,17):
            self.assertEqual(near_null_lag_discrete(n,F(1))-1,harmonic(n))
            self.assertAlmostEqual(near_null_lag_continuous(n,F(1))-1,log(n+1),places=13)

    def test_shifted_clock_changes_constant(self):
        # Even the same discrete H_n compared to log(n), not log(n+1),
        # differs by log(1+1/n) at finite n.
        for n in (2,3,8,32):
            self.assertAlmostEqual((float(harmonic(n))-log(n))-
                sampled_clock_gap(n),log(1+1/n),places=13)

class OilyBoundaryKLTests(unittest.TestCase):
    def test_source_kernel_exact_simple_zero(self):
        self.assertEqual(original_oily_L_at(F(1)),1)
        self.assertEqual(original_oily_R_at(F(1)),0)
        for x in (F(0),F(1,5),F(1,2),F(3,4),F(7,8)):
            self.assertEqual(original_oily_R_at(x),(1-x)*original_oily_L_at(x))
            self.assertGreater(original_oily_L_at(x),0)

    def test_two_KL_limits_and_exact_jeffreys(self):
        for a in (0,1,2,8,32,128,1024):
            d01,d10,J=finite_beta_jet_kl(a)
            self.assertGreater(d01,0)
            self.assertGreater(d10,0)
            self.assertEqual(J,F(a+1,a+2))
            self.assertAlmostEqual(d01+d10,float(J),places=12)
        d01,d10,_=finite_beta_jet_kl(1024)
        self.assertLess(abs(d01-GAMMA),0.002)
        self.assertLess(abs(d10-(1-GAMMA)),0.002)

    def test_all_consecutive_gamma_shape_jeffreys(self):
        for k in (1,2,3,5,11,101):
            self.assertEqual(gamma_jet_symmetric_divergence(k),F(1,k))

    def test_baseline_is_declared_not_authentic_second_source(self):
        self.assertNotEqual(original_oily_L_at(F(1,2)),original_oily_R_at(F(1,2)))
        self.assertEqual(original_oily_L_at(F(1)),1)

class PisotNullFrames(unittest.TestCase):
    def test_exact_pisot_boost_identity(self):
        for m in range(1,30):
            c2,s2,v2=pell_boost_certificate(m)
            self.assertEqual(c2-s2,1)
            self.assertTrue(pell_lorentz_null_identity(m))
            self.assertGreater(v2,0)
            self.assertLess(v2,1)
        self.assertEqual(pell_boost_certificate(1),(F(5,4),F(1,4),F(1,5)))
        self.assertEqual(pell_boost_certificate(2),(F(2),F(1),F(1,2)))

if __name__=='__main__':unittest.main()
