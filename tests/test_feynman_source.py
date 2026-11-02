"""Root-discoverable exact-arithmetic tests for rigorous SUCC finite Feynman lift."""
from __future__ import annotations
import importlib.util
from pathlib import Path
from fractions import Fraction as F
import unittest

ROOT=Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'feynman_source_paths'

def read_module(name, filename):
    spec=importlib.util.spec_from_file_location(name,ROOT/filename)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

m=read_module('feynman_source_exact_20261101','feynman_source.py')
o=read_module('feynman_source_oracle_20261101','independent_oracle.py')

class SourceTests(unittest.TestCase):
    def test_source_first(self): self.assertEqual(m.source(1),F(47,15))
    def test_source_second(self): self.assertEqual(m.source(2),F(106,819))
    def test_combined_source_many(self):
        for n in range(1,160):self.assertEqual(m.source(n),o.source(n))
    def test_positive_source(self):
        for n in range(1,125):self.assertGreater(m.source(n),0)
    def test_strict_decrease(self):
        for n in range(1,100):self.assertGreater(m.source(n),m.source(n+1))
    def test_all_original_denominators_odd(self):
        for n in range(1,101):self.assertTrue(m.source(n).denominator%2)
    def test_nonzero_seed_type_reject(self):
        with self.assertRaises(ValueError):m.orbit(1,0)
    def test_invalid_source_index(self):
        for n in (0,-1,F(1,2)):
            with self.assertRaises(ValueError):m.source(n)
    def test_zero_seed(self):self.assertEqual(m.orbit(0),0)
    def test_forward_recurrence(self):
        for n in range(1,18):self.assertEqual(m.orbit(n),16*m.orbit(n-1)+m.source(n))
    def test_affine_matrix_two_implementations(self):
        for n in range(0,24):self.assertEqual(m.affine_product(n),o.matrix_product(n))
    def test_matrix_translation_selected(self):
        for n in range(0,20):self.assertEqual(m.affine_product(n)[1],m.orbit(n))
    def test_seed_covariance(self):
        for n in range(0,12):self.assertEqual(m.orbit(n,F(2,5)),m.orbit(n)+16**n*F(2,5))
    def test_action_reconstructs(self):
        for n in range(0,24):self.assertEqual(m.weighted_action(n),m.orbit(n)/16**n)
    def test_action_increments(self):
        for n in range(1,23):self.assertEqual(m.weighted_action(n)-m.weighted_action(n-1),m.source(n)/16**n)
    def test_first_two_ordering_defect(self): self.assertEqual(m.two_order_offset(),F(12301,273))
    def test_wrong_order_defect_sign(self):
        a,b=m.source(1),m.source(2)
        d21=16*a+b;d12=16*b+a
        self.assertEqual(d21-d12,m.two_order_offset())
        self.assertNotEqual(d21,d12)

class FresnelAndStationarityTests(unittest.TestCase):
    def test_variance_first(self):self.assertEqual(m.variance_clock(1),1)
    def test_variance_closed_vs_recursive(self):
        for n in range(1,40):self.assertEqual(m.variance_clock(n),m.variance_clock_recursive(n))
    def test_variance_closed_vs_independent(self):
        for n in range(1,15):self.assertEqual(m.variance_clock(n),o.aggregate_variance(n))
    def test_variance_recursion(self):
        for n in range(2,14):self.assertEqual(m.variance_clock(n),256*m.variance_clock(n-1)+1)
    def test_gaussian_heat_covariance(self):
        for n in range(1,11):
            for e in [F(1,12),F(1,1024),F(7,3)]:
                self.assertEqual(o.path_gaussian_covariance(n,e),e*m.variance_clock(n))
    def test_stationary_path_independent_equations(self):
        for n in range(1,9):
            for e in [F(1,16),F(1,2),F(3,2)]:
                for d in [F(0),F(1,7),F(-3,5)]:
                    x0=F(2,7);final=16**n*x0+m.orbit(n)+d
                    x,p=m.stationary_path(n,x0,final,e)
                    self.assertTrue(o.assert_stationarity(n,x,p,e))
                    self.assertEqual(x[-1],final)
    def test_stationary_path_honest_zero_displacement(self):
        for n in range(1,12):
            x,p=m.stationary_path(n,F(0),m.orbit(n),F(1,8))
            self.assertEqual(p,(F(0),)*n)
            self.assertEqual(x,tuple(m.orbit(j) for j in range(n+1)))
    def test_stationary_action_quadratic(self):
        for n in range(1,12):
            for e in [F(1,16),F(3,7)]:
                x0=F(-1,5);delta=F(11,13)
                xf=16**n*x0+m.orbit(n)+delta
                self.assertEqual(m.stationary_action(n,x0,xf,e),delta*delta/(2*e*m.variance_clock(n)))
    def test_no_finite_eps_zero_stationary_boundary(self):
        with self.assertRaises(ValueError):m.stationary_path(1,F(0),F(0),F(0))
    def test_fresnel_fourier_quadratic_exponent(self):
        for n in range(1,8):
            v=m.exact_fourier_fresnel_phase(n,F(3,11),F(1,29),F(2,3))
            self.assertEqual(v,-F(1,29)*F(2,3)*F(9,121)*o.aggregate_variance(n)/2)
    def test_fresnel_phase_even_in_k(self):
        for n in range(1,7):
            self.assertEqual(m.exact_fourier_fresnel_phase(n,F(2,3),F(1,17)),m.exact_fourier_fresnel_phase(n,F(-2,3),F(1,17)))
    def test_nonnegative_bandwidth(self):
        with self.assertRaises(ValueError):m.bandlimited_error_bound(1,F(1,10),F(1),F(-1))
    def test_uniform_bandlimited_bound_all_horizons(self):
        for n in range(1,64):
            for eps in [F(1,16),F(2),F(1,1000)]:
                for k in [F(1),F(7,5)]:
                    self.assertLess(m.bandlimited_error_bound(n,eps,F(1),k),m.uniform_bandlimited_bound(eps,F(1),k))
    def test_uniform_bound_constant_510(self):
        self.assertEqual(m.uniform_bandlimited_bound(F(2,3),F(5,7),F(11,4)),F(2,3)*F(5,7)*F(121,16)/510)
    def test_bandlimited_zero_epsilon(self):
        self.assertEqual(m.bandlimited_error_bound(7,F(0),F(1),F(3)),0)
    def test_relative_covariance_exact(self):
        for n in range(1,24):
            self.assertEqual(F(m.variance_clock(n),16**(2*n)),(1-F(1,16**(2*n)))/255)
    def test_pi_character_observer_exponent_growth(self):
        for n in range(1,11):
            self.assertEqual(m.gaussian_phase_attenuation_exponent(n,1,F(1,16**n)),-2)
            self.assertEqual(m.gaussian_phase_attenuation_exponent(n,1,F(1)),F(-2*16**(2*n)))
    def test_squeezed_seed_precision(self):
        for n in range(1,20):
            x=m.gaussian_phase_attenuation_exponent(n,3,F(1,16**n*n))
            self.assertEqual(x,-F(18,n*n))
    def test_coherent_q_fifths_modulus(self):
        for n in range(1,30):self.assertEqual(F(16**n,5)%1,F(1,5))
    def test_counterfeit_tail_bound(self):
        for n in range(1,31):
            t=sum((m.source(n+j)/16**j for j in range(1,55)),F(0))
            self.assertLess(t,m.source_tail_bound(n))
    def test_counterfeit_finite_phase_near_one_fifth(self):
        for n in range(1,20):
            q=m.counterfeit_point_mod_one(n,27)
            self.assertLess(q,F(1,5))
            self.assertGreater(q,F(1,5)-m.source_tail_bound(n))
    def test_heat_point_regulator_character_coefficient(self):
        for n in range(1,9):
            e=F(1,4096);hbar=F(7,9)
            self.assertEqual(m.heat_point_character_attenuation_exponent(n,3,e,hbar),
                             -F(18)*e*hbar*o.aggregate_variance(n))
    def test_heat_point_regulator_requires_exponential_resolution(self):
        # Choose eps=16^(-2n): point attenuation approaches a nonzero constant,
        # unlike the true seed delta limit; exact coefficient tends -2/255.
        for n in range(1,12):
            v=m.heat_point_character_attenuation_exponent(n,1,F(1,16**(2*n)))
            self.assertEqual(v,-2*(1-F(1,16**(2*n)))/255)
            self.assertLess(v,0)
    def test_heat_versus_unitary_banded_resolution_distinction(self):
        # For FIXED eps, the L2 band-limited unitary bound is O(eps)
        # while the separate point-heat attenuation coefficient diverges.
        for n in range(2,12):
            self.assertLess(m.bandlimited_error_bound(n,F(1,1000),F(1),F(1)),F(1,510000))
            self.assertLess(m.heat_point_character_attenuation_exponent(n,1,F(1,1000)),
                            m.heat_point_character_attenuation_exponent(n-1,1,F(1,1000)))
    def test_heat_invalid_regulator(self):
        with self.assertRaises(ValueError):
            m.heat_point_character_attenuation_exponent(2,1,F(-1,10))

    def test_two_order_overlap_coefficient(self):
        delta=m.two_order_offset();sig=F(3,16)
        self.assertEqual(m.two_order_gaussian_overlap_exponent(sig),-delta*delta/(8*256**2*sig*sig))
    def test_two_order_overlap_strict_negative(self):
        for s in [F(1,10),F(1),F(7)]:self.assertLess(m.two_order_gaussian_overlap_exponent(s),0)
    def test_two_order_p_phase(self):
        self.assertEqual(m.two_order_momentum_phase_coefficient(F(1),F(1)),-F(12301,273*256))
    def test_two_order_zero_momentum_no_phase(self):
        self.assertEqual(m.two_order_momentum_phase_coefficient(F(0)),0)
    def test_full_real_line_unitarity_jacobian(self):
        # |det dy/dx| = 16^N and half-density squared = 16^-N.
        for n in range(1,30):self.assertEqual(F(16**n)*F(1,16**n),1)
    def test_quarter_step_exact_source_flow(self):
        # Four substeps: time 1/4 has 16^(1/4)=2.
        for n in range(1,16):
            b=m.source(n);c=b/15;x=F(7,9);p=F(3,13)
            for _ in range(4):
                x=2*x+c
                p/=2
            self.assertEqual(x,16*F(7,9)+b)
            self.assertEqual(p,F(3,13)/16)

if __name__=='__main__':unittest.main()
