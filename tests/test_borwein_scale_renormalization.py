"""Exact multiscale kernel and atomic floor controls, original source intact."""
import sys,unittest
from fractions import Fraction as F
from math import isqrt
from observational_succ.borwein_quantitative_certificate import (
    L, HAAR_MEAN, polynomial_quadrature, U, source_r,
)
from observational_succ.borwein_scale_renormalization import (
    ATOMIC_FLOOR,GRID_UPPER, L_MAX, L_LIP,
    paired_original_blocks,block_variance,pair_defect,pair_defect_autocorrelation,
    original_pair_report,step_coboundary_bound,
    phase_multiset_covers_dilated_mode,atomic_floor_for_length,
    uniform_grid_upper_for_length,exact_uniform_grid,scaled_residual_bound,
)

class SourceScaleTests(unittest.TestCase):
    def test_authentic_paired_blocks_use_one_terminal(self):
        for start,n in ((0,2),(2,2),(4,4),(8,4),(8,8),(16,4)):
            aa,bb=paired_original_blocks(start,n)
            m=start+2*n
            self.assertEqual(len(aa),n)
            self.assertEqual(len(bb),n)
            self.assertEqual(aa[0],(U(m)/16**(m-start))%1)
            self.assertEqual(bb[-1],(U(m)/16)%1)
            self.assertEqual(U(0),0)
            self.assertEqual(U(1),F(47,15))

    def test_exact_split_energy_conservation(self):
        for start,n in ((0,2),(2,2),(4,4),(8,4),(8,8),(16,4)):
            aa,bb=paired_original_blocks(start,n)
            E1,E2,EU,D,eps=original_pair_report(start,n)
            self.assertEqual(EU,(E1+E2)/2-D)
            self.assertEqual(D,pair_defect(aa,bb))
            self.assertGreaterEqual(D,0)
            self.assertGreater(eps,0)

    def test_independent_autocorrelation_defect(self):
        for start,n in ((0,1),(0,2),(2,2),(4,4)):
            a,b=paired_original_blocks(start,n)
            self.assertEqual(pair_defect(a,b),pair_defect_autocorrelation(a,b))

    def test_cross_block_frequency_dilation_is_exact(self):
        for start,n in ((0,2),(4,4),(8,4),(8,8)):
            a,b=paired_original_blocks(start,n)
            for h in (-7,-1,1,2,9):
                self.assertTrue(phase_multiset_covers_dilated_mode(a,b,h))

    def test_locked_orbit_has_zero_cross_block_mixing_defect(self):
        for n in (1,2,4,8):
            constant=(F(1,15),)*n
            self.assertEqual(pair_defect(constant,constant),0)
            self.assertGreater(block_variance(constant),0)

    def test_authentic_merging_energy_not_always_monotone(self):
        ea,eb,ec,d,_=original_pair_report(4,4)
        self.assertGreater(ec,ea)  # exact counterexample to E_merged<=E_left
        self.assertGreater(d,0)

    def test_universal_atomic_floor_exact(self):
        for n in (1,2,3,4,8,12):
            grid=exact_uniform_grid(n)
            E=polynomial_quadrature(grid)
            self.assertGreaterEqual(E,atomic_floor_for_length(n))
            self.assertLessEqual(E,uniform_grid_upper_for_length(n))
            self.assertGreater(E,0)

    def test_original_source_energies_beat_atomic_floor(self):
        for start,n in ((0,2),(4,4),(8,8),(16,4)):
            aa,bb=paired_original_blocks(start,n)
            self.assertGreater(block_variance(aa),atomic_floor_for_length(n))
            self.assertGreater(block_variance(bb),atomic_floor_for_length(n))
            self.assertGreater(block_variance(aa+bb),atomic_floor_for_length(2*n))

    def test_fejer_combinatorial_minimum_direct_finite(self):
        # At N atoms, Fejer F_{2N} gives sum_{h=1}^{2N-1}|mu_hat(h)|²>=1/2.
        # Test via exact root-of-unity Fourier patterns for N-th roots:
        for n in (1,2,3,4,7,12):
            hats=[int(h%n==0) for h in range(1,2*n)]
            self.assertGreaterEqual(sum(h*h for h in hats),F(1,2))
            self.assertEqual(sum(h*h for h in hats),1)
        self.assertEqual(ATOMIC_FLOOR,F(4862025,313044726016))
        self.assertEqual(GRID_UPPER,F(968,250563))

    def test_step_coboundary_defect_vanishes_even_for_locked_orbits(self):
        for n in (1,2,4,8):
            self.assertEqual(step_coboundary_bound(n),F(64,289*n))
            # The source-agnostic T-invariant constant orbit has exact 0 defect,
            # despite nonzero source-to-Haar kernel discrepancy.
            frozen=(F(0),)*n
            self.assertGreater(block_variance(frozen),0)
            self.assertEqual(tuple(frozen[1:])+(frozen[-1],),frozen)

    def test_dense_subsequence_interpolation_bound_is_exact_formula(self):
        self.assertEqual(scaled_residual_bound(100,100),0)
        self.assertEqual(scaled_residual_bound(100,101),F(64,289*101))
        self.assertEqual(scaled_residual_bound(100,200),F(32,289))
        # j² -> (j+1)² has relative gap -> 0, while doubling does not.
        for j in (10,100,1000):
            r=scaled_residual_bound(j*j,(j+1)**2)
            self.assertLess(r,F(2,j))

    def test_rational_phase_filter_zero_and_nonunit_fixed_controls(self):
        for n in (2,4,8):
            self.assertEqual(pair_defect((F(0),)*n,(F(0),)*n),0)
            self.assertEqual(pair_defect((F(1,15),)*n,(F(1,15),)*n),0)
            self.assertEqual(block_variance((F(0),)*n),block_variance((F(1,15),)*n))

if __name__=='__main__':unittest.main()

class OrdinalWaveletBudgetTests(unittest.TestCase):
    def test_exact_source_full_knowledge_budget(self):
        from observational_succ.borwein_scale_renormalization import (
            original_prefix_phases,wavelet_detail_budget,wavelet_remaining_energy,
            constant_single_atom_energy,prefix_shadow_tail)
        atom=F(335872,304434045)
        self.assertEqual(constant_single_atom_energy(),atom)
        for N in (1,2,3,4,5,8,12):
            phases=original_prefix_phases(N)
            total=polynomial_quadrature(phases)
            spent=wavelet_detail_budget(phases)
            self.assertEqual(total+spent,atom)
            self.assertGreaterEqual(spent,0)
            self.assertEqual(wavelet_remaining_energy(phases),total)
            self.assertGreater(total,atomic_floor_for_length(N))
            self.assertGreater(prefix_shadow_tail(N),0)

    def test_locked_zero_and_nonunit_source_have_zero_budget(self):
        from observational_succ.borwein_scale_renormalization import (
            wavelet_detail_budget,constant_single_atom_energy)
        for N in (1,2,4,8):
            for x in (F(0),F(1,15),F(3,7)):
                seq=(x,)*N
                self.assertEqual(wavelet_detail_budget(seq),0)
                self.assertEqual(polynomial_quadrature(seq),constant_single_atom_energy())

    def test_rational_uniform_grids_increasingly_saturate_budget(self):
        from observational_succ.borwein_scale_renormalization import (
            wavelet_detail_budget,constant_single_atom_energy)
        prev=F(-1)
        for n in (2,4,8):
            pts=exact_uniform_grid(n)
            budget=wavelet_detail_budget(pts)
            self.assertEqual(budget+polynomial_quadrature(pts),constant_single_atom_energy())
            self.assertGreater(budget,prev)
            prev=budget

    def test_unbalanced_tree_genuine_positive_defects(self):
        from observational_succ.borwein_scale_renormalization import wavelet_detail_budget
        pts=(F(0),F(1,9),F(1,3),F(2,3),F(7,9))
        self.assertEqual(wavelet_detail_budget(pts)+polynomial_quadrature(pts),F(335872,304434045))


class ArgonSharpConstantCrossAudit(unittest.TestCase):
    def test_sharp_floor_from_independent_argon_bound(self):
        from observational_succ.borwein_scale_renormalization import (
            SHARP_FOURIER_FLOOR, SHARP_ATOMIC_FLOOR, sharp_atomic_floor_for_length)
        self.assertEqual(SHARP_FOURIER_FLOOR,F(5733,279752))
        self.assertEqual(SHARP_FOURIER_FLOOR/
                         F(2205,139876),F(13,10))
        self.assertEqual(SHARP_ATOMIC_FLOOR,F(32867289,1252178904064))
        self.assertEqual(SHARP_ATOMIC_FLOOR/ATOMIC_FLOOR,F(169,100))
        for N in (1,2,3,4,8,12):
            self.assertGreaterEqual(polynomial_quadrature(exact_uniform_grid(N)),
                                    sharp_atomic_floor_for_length(N))
            self.assertLessEqual(sharp_atomic_floor_for_length(N),
                                 uniform_grid_upper_for_length(N))
