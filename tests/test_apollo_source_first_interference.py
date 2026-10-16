"""Exact rational prime shift, Brownian and source-first tests."""
import unittest
from fractions import Fraction as F
from observational_succ.apollo_source_first_interference import (
    PrimeInterferenceError,source_first_prime_interference,
    forced_Brownian_cancellation,exact_anchored_prime_hinge,
    normalized_birth_boundary_wells,finite_feature_graph_criterion)
from observational_succ.apollo_krein_factor import prime_krein_identity

class CanonicalBrownianSource(unittest.TestCase):
    def test_unique_neutral_correction(self):
        a,b,w=F(1,4),F(3,4),F(2,3)
        v=((-F(1,8),0,2,0),(0,F(1,8),1,1))
        r=source_first_prime_interference(a,b,w,v)
        self.assertEqual(r["translated_overlap_real"],0)
        self.assertEqual(r["positive_prime_difference_energy"],
                         r["forced_Brownian_subtraction_energy"])
        self.assertEqual(r["signed_prime_energy"],0)
        self.assertEqual(r["finite_inverse_shift_steps"],1)
        self.assertTrue(r["inverse_reconstruction_exact_on_every_piece"])
        for c in (0,1,2,3):
            x=forced_Brownian_cancellation(a,b,w,c)
            self.assertEqual(x["prebirth_signed_factor_per_w_norm"],2-c)
            self.assertEqual(x["full_old_window_neutral_for_every_test"],c==2)
    def test_old_anchored_source_is_exactly_neutral(self):
        a,b=F(1,4),F(3,4)
        for x in (-a,-a/2,0,a/2,a):
            for y in (-a,-a/2,0,a/2,a):
                z=prime_krein_identity(x,y,b)
                self.assertEqual(z["positive_triangle"],z["negative_brownian"])
                self.assertEqual(z["signed"],0)
    def test_indefinite_source_prime_is_not_entirely_a_negative_well(self):
        d=exact_anchored_prime_hinge(F(1,2),F(3,4),F(2,3))
        self.assertEqual(d["anchored_2x2"],((F(0),F(1,6)),(F(1,6),F(0))))
        self.assertEqual(d["eigenvalues"],(-F(1,6),F(1,6)))
        self.assertFalse(d["RH_proved"])

class InterferenceFamily(unittest.TestCase):
    def test_both_signs_and_zero_from_same_clock(self):
        a,b,w=F(1,2),F(3,4),F(1)
        left=(-a,-F(3,8),2,0)
        for right,signed,positive in (
            ((F(1,4),F(3,8),2,0),-1,1),
            ((F(1,4),F(3,8),-2,0),1,3),
            ((F(1,4),F(3,8),0,2),0,2)):
            z=source_first_prime_interference(a,b,w,(left,right))
            self.assertEqual(z["Brownian_L2_energy"],1)
            self.assertEqual(z["positive_prime_difference_energy"],positive)
            self.assertEqual(z["forced_Brownian_subtraction_energy"],2)
            self.assertEqual(z["signed_prime_energy"],signed)
            self.assertEqual(z["finite_inverse_shift_steps"],2)
            self.assertTrue(z["inverse_reconstruction_exact_on_every_piece"])
            self.assertFalse(z["RH_proved"])
    def test_recovery_arbitrary_piecewise_complex_source(self):
        z=source_first_prime_interference(1,F(1,4),F(7,11),(
            (F(-9,10),F(-4,5),3,1),
            (F(-1,8),F(1,8),-2,4),
            (F(2,5),F(4,5),1,-1)))
        self.assertEqual(z["finite_inverse_shift_steps"],9)
        self.assertTrue(z["positive_feature_determines_Brownian_feature"])
    def test_boundary_layers_do_not_obtain_a_uniform_operator_norm_limit(self):
        for m in (2,3,5,16):
            d=normalized_birth_boundary_wells(m)
            self.assertEqual(d["in_phase_signed_prime_energy"],-1)
            self.assertEqual(d["anti_phase_signed_prime_energy"],1)
            self.assertEqual(d["in_phase_L2_norm_squared"],1)
            self.assertTrue(d["operator_norm_does_not_tend_zero"])
            self.assertFalse(d["RH_proved"])

class FeatureGraphControls(unittest.TestCase):
    def test_determined_negative_is_not_necessarily_contracted(self):
        good=finite_feature_graph_criterion(((2,0),(0,1)),((1,0),(0,1)))
        bad=finite_feature_graph_criterion(((1,0),(0,1)),((2,0),(0,1)))
        self.assertTrue(good["Brownian_or_negative_feature_determined_by_positive"])
        self.assertTrue(bad["Brownian_or_negative_feature_determined_by_positive"])
        self.assertTrue(good["finite_full_source_contraction_condition"])
        self.assertFalse(bad["finite_full_source_contraction_condition"])
    def test_null_direction_cannot_carry_an_unobserved_negative_feature(self):
        a=finite_feature_graph_criterion(((1,0),(0,0)),((0,0),(0,1)))
        b=finite_feature_graph_criterion(((1,0),(0,0)),((F(1,2),0),(0,0)))
        self.assertFalse(a["positive_kernel_null_in_negative_kernel"])
        self.assertTrue(b["positive_kernel_null_in_negative_kernel"])
        self.assertTrue(b["finite_full_source_contraction_condition"])
    def test_bad_source_inputs_are_rejected(self):
        for cells in (
            ((0,1,1,0),(F(1,2),1,1,0)),
            ((0,1,0,0),),((0,1,1.2,0),),()):
            with self.assertRaises(PrimeInterferenceError):
                source_first_prime_interference(1,F(3,4),1,cells)
        with self.assertRaises(PrimeInterferenceError):
            forced_Brownian_cancellation(F(1,2),F(1,2),1)

if __name__=="__main__":
    unittest.main()
