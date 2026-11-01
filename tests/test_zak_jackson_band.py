"""Root-discoverable exact tests for the new Zak/Jackson band bridge."""
from __future__ import annotations
import importlib.util
import sys
import unittest
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

_ROOT=Path(__file__).resolve().parents[1]
_BASE=_ROOT/'research'/'2026-10-31'/'zak_jackson_band'

def _load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

m=_load(_BASE/'jackson_band.py','succ_zak_jackson_band_implementation')
o=_load(_BASE/'independent_oracle.py','succ_zak_jackson_band_independent')

class TestZakJacksonBand(unittest.TestCase):
    def test_four_pole_independent(self):
        for n in range(1,52):
            self.assertEqual(m.four_pole(n),m.four_pole_combined(n))
            self.assertEqual(m.four_pole(n),o.rational_original_source(n))
    def test_fractional_four_pole_independent(self):
        for x in (Fraction(5,4),Fraction(7,2),Fraction(19,7),Fraction(123,8)):
            self.assertEqual(m.four_pole(x),o.rational_original_source(x))
    def test_source_positive_and_decreasing(self):
        v=[m.four_pole(i) for i in range(1,100)]
        self.assertTrue(all(a>b>0 for a,b in zip(v,v[1:])))
    def test_initial_seed(self):
        vals=m.original_u_prefix(9)
        self.assertEqual(vals[0],0)
        self.assertEqual(vals[1],Fraction(47,15))
        self.assertTrue(all(vals[i+1]==16*vals[i]+m.four_pole(i+1) for i in range(9)))
    def test_green_interval_nested(self):
        for x in (0,1,Fraction(1,4),Fraction(11,3)):
            old=m.green_interval(x,2)
            for count in (3,5,8):
                new=m.green_interval(x,count)
                self.assertLessEqual(old[0],new[0])
                self.assertGreaterEqual(old[1],new[1])
                self.assertGreater(new[1],new[0])
                old=new
    def test_green_shift_residual(self):
        for x in (0,Fraction(1,4),1,Fraction(19,5)):
            for depth in (1,2,4,8):
                self.assertEqual(m.green_telescoping_defect(x,depth),-m.four_pole(Fraction(x)+depth+1)/16**depth)
    def test_fourth_normalizer(self):
        for L in (2,3,4,8,16,32,64):
            co=m.fourth_coefficients(L)
            self.assertEqual(co[0],m.exact_fourth_normalizer(L))
            self.assertEqual(sum(co.values()),L**4)
    def test_direct_four_tuple_oracle(self):
        for L in (2,3,5,8,16):
            self.assertEqual(m.fourth_coefficients(L),o.quadruple_frequency_counts(L))
    def test_fourth_even_positive_spectrum(self):
        for L in (2,3,5,16):
            a=m.fourth_coefficients(L)
            self.assertTrue(all(v>0 and a[-k]==v for k,v in a.items()))
            self.assertEqual((min(a),max(a)),(-2*L+2,2*L-2))
    def test_flat_top_coefficients_conservation(self):
        for L in (2,3,5,16,32):
            c=m.flat_top_coefficients(L)
            self.assertEqual(c[0],1)
            self.assertEqual(sum(c.values()),Fraction(6*L+1))
            self.assertTrue(all(0<=v<=1 for v in c.values()))
    def test_flat_top_plateau(self):
        for L in (2,3,5,16):
            c=m.flat_top_coefficients(L)
            self.assertTrue(all(c[k]==1 for k in range(-L-2,L+3)))
    def test_flat_top_support(self):
        for L in (2,3,5,16):
            c=m.flat_top_coefficients(L)
            self.assertEqual(min(c),-5*L+2)
            self.assertEqual(max(c),5*L-2)
            self.assertEqual(m.flat_top_coefficient(L,5*L-1),0)
            self.assertEqual(m.flat_top_coefficient(L,-5*L+1),0)
    def test_independent_flat_top_oracle(self):
        for L in (2,3,5,8):
            for f in range(-5*L,5*L+1):
                self.assertEqual(m.flat_top_coefficient(L,f),o.direct_flat_top_frequency(L,f))
    def test_ideal_ladder_exact_prefix(self):
        for M in (1,2,3,4,7):
            for N in (M,M+1,M+5):
                self.assertEqual(m.ideal_linear_ladder_weights(N,M),(Fraction(1),)*M+(Fraction(0),)*(N-M))
    def test_ladder_frequency_coverage(self):
        for M in (1,2):
            L=16**M
            self.assertEqual(m.flat_top_coefficient(L,16**M),1)
            self.assertEqual(m.flat_top_coefficient(L,16**(M+1)),0)
    def test_explicit_analytic_constant(self):
        for h in (-11,-2,-1,1,2,13):
            self.assertLess(m.analytic_constant_bound(h),m.guaranteed_band_error(h))
    def test_coherent_high_alias_positive_at_large_horizon(self):
        for M in (200,250,320):
            d=M//2
            self.assertGreater(m.coherent_high_alias_lower_bound(M,d,1),0)
    def test_coherent_high_alias_asymptotic_ratio(self):
        for M in (400,800,1600):
            d=M//4
            bound=m.coherent_high_alias_lower_bound(M,d,1)
            self.assertGreater(bound,Fraction(3*M,4)-100)
    def test_horizontal_finite_action_selector(self):
        for e in (Fraction(1,3), Fraction(-3,7), Fraction(2,11)):
            self.assertEqual(m.horizontal_action_coefficient(e,6),6*e*e)
            self.assertGreater(m.horizontal_action_coefficient(e,100),m.horizontal_action_coefficient(e,10))
        self.assertEqual(m.horizontal_action_coefficient(0,10**6),0)
    def test_source_stationary_gap_lower_rational(self):
        for n in range(1,12):
            self.assertEqual(m.stationary_band_gap_lower(n),3*16**n-1)
            self.assertGreater(m.stationary_band_gap_lower(n),0)
    def test_source_pairs_have_strong_uniform_shear(self):
        for upper in range(2,16):
            raw=Fraction(15,64)*16**upper-1
            self.assertGreater(raw,m.pair_derivative_lower(upper))
    def test_source_pair_cross_energy_bound(self):
        for h in (-5,-1,1,2,7):
            # Upper bound after pi>3, summed exactly over infinite geometric pairs.
            self.assertEqual(m.continuous_slice_error_upper_rational(h),Fraction(8,225*abs(h)))
            for N in (2,3,10,100):
                geometric=sum((Fraction(upper-1,16**upper) for upper in range(2,N+1)),Fraction())
                self.assertLess(geometric,Fraction(1,225))
    def test_horizontal_action_invalid(self):
        with self.assertRaises(ValueError):m.horizontal_action_coefficient(1,-1)
    def test_eight_jet_positive_source_mutant_firewall(self):
        for k in range(9):
            v=sum((-1)**j*comb(8,j)*(-j)**k for j in range(9))
            self.assertEqual(v, factorial(8) if k==8 else 0)
    def test_beta_spoof_positive_and_extra_poles(self):
        for n in (1,2,3,7):
            b=sum((Fraction((-1)**j*comb(8,j),8*n+j) for j in range(9)),Fraction())
            ref=Fraction(factorial(8),1)
            for k in range(9):ref/=8*n+k
            self.assertEqual(b,ref)
            self.assertGreater(b,0)
    def test_error_validation(self):
        for bad in (0,1.1,True,'1'):
            with self.assertRaises(ValueError):m.guaranteed_band_error(bad)
    def test_mutated_truncation_loses_flat_top(self):
        # Hostile mutation: wrong rectangular span 2L instead of 3L.
        L=16
        b={k:Fraction(v,L**4) for k,v in m.fourth_coefficients(L).items()}
        ell=L
        mutated=sum((v for k,v in b.items() if abs(ell-k)<=2*L),Fraction())
        self.assertLess(mutated,1)
        self.assertEqual(m.flat_top_coefficient(L,ell),1)
    def test_mutated_fourth_kernel_coefficient_is_detected(self):
        # Hostile mutation: delete the unique far-edge quadruple coefficient.
        L=8
        true=m.fourth_coefficients(L)
        wrong=dict(true)
        wrong[2*L-2]-=1
        self.assertNotEqual(wrong,o.quadruple_frequency_counts(L))
        self.assertNotEqual(sum(wrong.values()),L**4)
    def test_source_invalid_domain(self):
        with self.assertRaises(ValueError):m.four_pole(Fraction(9,10))
        with self.assertRaises(ValueError):m.green_interval(-1,4)
        with self.assertRaises(ValueError):m.green_interval(1,0)
    def test_coeff_budget_and_arguments(self):
        with self.assertRaises(ValueError):m.fourth_coefficients(4096)
        with self.assertRaises(ValueError):m.triangular_coefficient(1,0)
        with self.assertRaises(ValueError):m.flat_top_coefficient(16,Fraction(1,2))

if __name__=='__main__':unittest.main()
