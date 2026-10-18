"""Independent rational probes for original BDC weighted memory and RN transport."""
import unittest
from fractions import Fraction as F

from observational_succ.weighted_clock_cocycle import (
    ClockDensityError, clock_phase, memory_weight_bounds,
    approximate_weight, ratio_square_interval,
    finite_grid_cocycle, finite_cocycle_composition,
    cut_jump_and_unweighted_shift_lower, periodic_ghost_mutant,
)


class WeightedClockCocycleTests(unittest.TestCase):
    def test_real_positive_backward_memory_interval_and_depth_refinement(self):
        for L in (2,3,6,10):
            for u in (F(0),F(1,2),F(1),F(3,2),F(L-1,2)):
                if not 0<=u<L:continue
                a=memory_weight_bounds(u,L,8)
                b=memory_weight_bounds(u,L,22)
                self.assertLessEqual(a["lower"],b["lower"])
                self.assertLessEqual(b["upper"],a["upper"])
                self.assertGreater(b["lower"],0)
                # Independent deeper prefix guaranteed to lie inside
                # the stated interval even with omitted positive tail.
                deeper=approximate_weight(u,L,200)
                self.assertLessEqual(a["lower"],deeper)
                self.assertLessEqual(deeper,a["upper"])
                self.assertFalse(a["normalized_clock_Haar_equal_to_memory"])

    def test_ratio_interval_source_bounded_by_high_depth_independent_series(self):
        for L in (2,3,6,10):
            for u,a in ((F(1,2),1),(F(3,2),1),(F(0),-1),
                        (F(L-1,2),F(1,2))):
                if not 0<=u<L:continue
                r=ratio_square_interval(L,u,a,J=15)
                v=clock_phase(u-a,L)
                # A RATIO of two truncated positive series is NOT
                # necessarily an enclosure of the ratio of their full
                # limits. Compare independently enclosed ratios instead.
                fine=ratio_square_interval(L,u,a,J=300)
                self.assertLessEqual(r["RN_cocycle_square_lower"],
                                     fine["RN_cocycle_square_lower"])
                self.assertGreaterEqual(r["RN_cocycle_square_upper"],
                                        fine["RN_cocycle_square_upper"])
                self.assertLessEqual(fine["RN_cocycle_square_lower"],
                                     fine["RN_cocycle_square_upper"])
                self.assertTrue(r["unitary_in_original_weighted_L2"])
                self.assertFalse(r["original_Haar_shift_without_cocycle_unitary"])

    def test_discrete_exact_weighted_isometry_for_every_vector(self):
        for L,resolution,J,shift in ((2,2,15,2),(3,2,9,1),
                                     (6,1,12,1),(5,3,8,3),(4,2,10,-1)):
            r=finite_grid_cocycle(L,resolution,J,shift)
            weights=r["source_weight_prefixes"]
            factors=r["RN_amplitude_squares"]
            size=len(weights)
            self.assertEqual(len(factors),size)
            # Direct independent norm computation in the actual
            # weighted source norm. Square-root coefficients are not
            # rational, so compare the exact norm-squared algebra.
            for seed in (0,1,7):
                vec=tuple(F(((i+3*seed)%7)-3,5) for i in range(size))
                original=sum(weights[i]*vec[i]*vec[i] for i in range(size))
                transformed=sum(weights[i]*factors[i]*
                                vec[(i-shift)%size]**2 for i in range(size))
                self.assertEqual(transformed,original)
            self.assertTrue(r["weighted_norms_preserved_by_cocycle"])
            self.assertFalse(r["finite_prefix_represents_exact_integrated_memory"])
            self.assertFalse(r["naive_clock_shift_weight_preserving"])

    def test_direct_finite_cocycle_composition_and_reciprocal_orientation(self):
        for L in (2,3,5,8):
            for u,a,b in ((F(1,2),1,-1),(F(3,2),F(1,2),1),
                          (F(0),-1,F(1,2))):
                r=finite_cocycle_composition(L,u,a,b,J=15)
                self.assertEqual(r["cocycle_a_sq"]*r["cocycle_b_after_a_sq"],
                                 r["composed_sq"])
                self.assertTrue(r["exact_pure_coboundary_at_every_positive_weight"])
                self.assertFalse(r["change_to_uniform_measure_is_source_free"])
                inverse=finite_cocycle_composition(L,u,a,-a,J=15)
                self.assertEqual(inverse["composed_sq"],1)

    def test_cut_density_jump_gives_L_squared_failure_for_naive_translation(self):
        for L in (2,3,5,10,50,100,500):
            r=cut_jump_and_unweighted_shift_lower(L)
            self.assertEqual(r["source_density_ratio_strict_lower"],F(2*L*L,9))
            self.assertEqual(r["near_cut_right_jump_exact"],1)
            self.assertFalse(r["uniformly_bounded_naive_shift_as_L_grows"])
            # Lower bound on the true ratio using an independent
            # rational series enclosure, not only the theorem metadata.
            before=memory_weight_bounds(F(1,2),L,30)
            after=memory_weight_bounds(F(3,2),L,30)
            self.assertGreater(after["lower"]/before["upper"],
                               r["source_density_ratio_strict_lower"])
            self.assertTrue(r["corrected_density_cocycle_translation_is_unitary"])

    def test_unobserved_periodic_ghost_changes_source_probability(self):
        for L in (2,3,6,30):
            genuine=periodic_ghost_mutant(L,0)
            mutant=periodic_ghost_mutant(L,F(1,5))
            self.assertTrue(genuine["decay_at_infinity_retained"])
            self.assertFalse(mutant["decay_at_infinity_retained"])
            self.assertTrue(mutant["shift_law_unchanged"])
            self.assertEqual(mutant["integrated_source_mass_added"],F(L,5))
            self.assertFalse(mutant["same_declared_backward_probability_measure"])

    def test_source_domain_types_and_periodic_ghost_controls(self):
        for L in (0,1,True,F(6)):
            with self.assertRaises(ClockDensityError):
                memory_weight_bounds(F(1,2),L,8)
        for u in (F(-1,2),F(6),True,0.1):
            with self.assertRaises(ClockDensityError):
                memory_weight_bounds(u,6,8)
        for J in (0,True,1.2,1001):
            with self.assertRaises(ClockDensityError):
                approximate_weight(0,3,J)
        with self.assertRaises(ClockDensityError):
            finite_grid_cocycle(6,0,4,1)
        with self.assertRaises(ClockDensityError):
            finite_grid_cocycle(20,8,4,1)
        with self.assertRaises(ClockDensityError):
            finite_grid_cocycle(2,2,4,F(1,2))
        with self.assertRaises(ClockDensityError):
            periodic_ghost_mutant(2,0.2)
        self.assertEqual(clock_phase(F(-1,2),3),F(5,2))


if __name__=="__main__":
    unittest.main()
