"""Exact research regression for source-tail/frequency visibility, no pi oracle."""
from pathlib import Path
import importlib.util
from fractions import Fraction as Q
import unittest

SCRIPT=Path(__file__).resolve().parents[1] / 'research/2026-11-04/analytic_exile/analytic_exile.py'
sp=importlib.util.spec_from_file_location('succc_analytic_exile',SCRIPT)
m=importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)

class SourceExileTests(unittest.TestCase):
    def test_original_four_poles(self):
        self.assertEqual(m.authentic_r(1),Q(47,15))
        self.assertEqual(m.authentic_r(2), Q(4,9)-Q(2,12)-Q(1,13)-Q(1,14))

    def test_source_positive_cap(self):
        for n in (1,2,3,7,41,97,193,385):
            self.assertTrue(Q(0)<m.authentic_r(n)<m.positive_source_cap(n))

    def test_source_two_arithmetic_oracles(self):
        for A in (40,96,160):
            x=m.original_phases(2*A)
            y=m.modular_original_phases(2*A)
            self.assertEqual(x,y)
            self.assertTrue(all(z.denominator%2==1 for z in x))

    def test_exact_ladder_lifts(self):
        x=m.original_phases(2*96)
        for A in (40,96):
            for h in (1,3,5):
                for j in range(4):
                    self.assertTrue(m.ward_ladder_bound(A,h,j)>=0)
                    # Exact original recurrence proving the Ward step before complex chord.
                    for n in (A,A+1,2*A-1):
                        left=16**(j+1)*h*x[n]
                        right=16**j*h*(x[n+1]-m.authentic_r(n+1))
                        self.assertEqual((left-right)%1,0)

    def test_ward_zero_depth(self):
        self.assertEqual(m.ward_ladder_bound(96,3,0),0)

    def test_ward_concrete_visibility_is_conditional(self):
        z=m.ward_visibility_certificate(A=512,q=512,h=1,epsilon=Q(1,10))
        self.assertTrue(z['useful'])
        self.assertEqual(z['L'],2)
        self.assertGreater(z['conditional_J_minus_one_lower'],0)
        self.assertFalse(z['source_normality_proved'])

    def test_ward_premise_can_fail(self):
        z=m.ward_visibility_certificate(A=8,q=512,h=1,epsilon=Q(1,10))
        self.assertFalse(z['useful'])

    def test_weighted_tail_uniform_bound(self):
        for q in (2,8,16,32,257):
            x=m.weighted_fourier_tail_upper(q,q*q)
            self.assertLessEqual(x,Q(2,9))

    def test_completion_epoch_uniform(self):
        for A in (40,96,160):
            self.assertLess(m.completion_epoch_coeff_upper(A,5),Q(1,100))
            self.assertGreater(m.completion_band_square_energy_upper(A,5),0)

    def test_prefix_shadow_source_only(self):
        for A in (40,96,160):
            for h in (1,3,5):
                self.assertLess(m.finite_prefix_shadow_error(A,h),Q(1,10**4))

    def test_champernowne_truncations_terminate(self):
        for M in (1,4,17,40):
            x=m.champernowne16_prefix(M)
            self.assertEqual((16**M*x)%1,0)
            self.assertEqual((16**(M+7)*x)%1,0)

    def test_champernowne_matching_finite_history(self):
        M=17
        x=m.champernowne16_prefix(M)
        xx=m.champernowne16_prefix(2*M)
        self.assertLess(xx-x,Q(1,16**M))
        for n in range(0,M-1):
            self.assertLess((16**n*(xx-x)),Q(1,16**(M-n)))

    def test_false_uniform_equal_branch_control(self):
        for q in (2,8,16,256):
            self.assertEqual(m.coherent_fixed_point(q),q)

    def test_triangle_source_exact(self):
        # Original source selected rational phases only, at a small development resolution.
        for A in (8,16,24):
            x=m.original_phases(2*A)
            energy=m.triangle_energy(x[A:2*A],8)
            self.assertTrue(Q(1)<=energy<=8)

    def test_gamma2_negative_binomial_tail_exact(self):
        for r in (Q(1,2),Q(3,4),Q(7,8),Q(31,32)):
            for last in (0,1,3,8,17):
                self.assertEqual(m.nb2_partial_mass(r,last)+m.nb2_tail_mass(r,last),1)

    def test_exact_abel_cesaro_gamma2_mixture(self):
        src=tuple(m.authentic_r(n) for n in range(1,14))
        for series in (src, (Q(1),)*8, (Q(1),Q(-1),Q(1),Q(-1))):
            for r in (Q(1,2),Q(7,8),Q(31,32)):
                out=m.abel_cesaro_finite_identity(series,r)
                self.assertEqual(out['abel_mean'],out['mixture_total'])

    def test_growing_boundary_ghost_analytic_pole(self):
        for M in (1,3,8,32):
            for z in (Q(1,2),Q(7,8),Q(31,32),Q(127,128)):
                out=m.boundary_ghost(M,z)
                self.assertTrue(out['exact_equal_to_z_power_M'])
                self.assertEqual((1-z)*out['function'],z**M)
                self.assertEqual(out['fixed_M_boundary_residue'],1)
                self.assertEqual(m.unit_phase_boundary_difference(M,z),-2*out['function'])

    def test_gamma2_mean_and_euler_scale(self):
        for r in (Q(0),Q(1,2),Q(3,4),Q(31,32)):
            self.assertEqual(m.gamma2_scaled_mean(r),1+r)
        # As r approaches 1, its scaled NB2 mean approaches Gamma(2)'s mean 2.
        self.assertLess(2-m.gamma2_scaled_mean(Q(127,128)),Q(1,100))

    def test_actual_green_tail_abel_residue_vanishes(self):
        for h in (1,3,5,17):
            earlier=m.gamma_tail_abel_boundary_upper(h,Q(7,8))
            later=m.gamma_tail_abel_boundary_upper(h,Q(127,128))
            self.assertLess(later,earlier)
            self.assertGreaterEqual(later,0)

    def test_source_analytic_ward_forcing_budget(self):
        source_sum=sum((m.authentic_r(n) for n in range(1,320)),Q(0))
        self.assertLess(source_sum,4)
        for h in (1,3,5):
            first=m.analytic_ward_source_error_bound(h,Q(3,4))
            second=m.analytic_ward_source_error_bound(h,Q(127,128))
            self.assertLess(second,first)
            self.assertGreaterEqual(second,0)

    def test_bad_inputs(self):
        with self.assertRaises(ValueError):m.authentic_r(0)
        with self.assertRaises(ValueError):m.ward_ladder_bound(0,1,3)
        with self.assertRaises(ValueError):m.band_depth(8,0)
        with self.assertRaises(ValueError):m.weighted_fourier_tail_upper(1,1)

if __name__=='__main__':unittest.main()
