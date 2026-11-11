"""Independent rational, boundary, mutation and signed-cancellation checks."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
import unittest
from unittest.mock import patch

from observational_succ.duck_bbp import tail_interval
from observational_succ.recursive_haar_pinbed import (
    canonical_law, digit_averaging_law, interval_w1, interval_w1_haar,
)
from observational_succ.zero_anchored_haar import (
    bernstein_vector, certified_haar_defect, certified_pascal_characters,
    certified_phase_grid, contraction_residual, finite_verdict,
    grid_haar_defect, pascal_haar_upper, signed_block_overlap, verify_phase_grid,
    contraction_error_floor, orbit_defect_floor, _source_integer_enclosure,
)


class SourcePhaseTests(unittest.TestCase):
    def test_bulk_enclosure_contains_independent_rational_tail_interval(self):
        c = certified_phase_grid(0, 9, depth=5, guard=6)
        a, b = tail_interval(0, c.horizon)
        self.assertLessEqual(F(c.integer_lower, 16**c.horizon), a)
        self.assertGreaterEqual(F(c.integer_upper, 16**c.horizon), b)
        self.assertTrue(verify_phase_grid(c))

    def test_integer_digit_and_known_initial_fraction_digits_have_correct_clock(self):
        c = certified_phase_grid(0, 12, depth=4)
        self.assertEqual(''.join(format(k//16**3, 'X') for k in c.points),
                         '3243F6A8885A')
        shifted = certified_phase_grid(1, 11, depth=4)
        self.assertEqual(c.points[1:], shifted.points)

    def test_separate_horizons_preserve_refined_phase_cells(self):
        a = certified_phase_grid(7, 23, depth=4)
        b = certified_phase_grid(7, 23, depth=7)
        self.assertEqual(a.points, tuple(x//16**3 for x in b.points))

    def test_mutated_payloads_fail_source_reconstruction(self):
        c = certified_phase_grid(0, 8)
        mutations = [replace(c, start=1), replace(c, horizon=c.horizon+1),
                     replace(c, integer_lower=c.integer_lower+1),
                     replace(c, integer_upper=c.integer_upper-1),
                     replace(c, points=(c.points[0]+1,)+c.points[1:]),
                     replace(c, horizon=float(c.horizon)),
                     replace(c, integer_lower=F(c.integer_lower)),
                     replace(c, points=tuple(F(k) for k in c.points))]
        for wrong in mutations:
            self.assertFalse(verify_phase_grid(wrong))
            with self.assertRaises(ValueError):
                certified_haar_defect(wrong)

    def test_invalid_exact_inputs(self):
        for start, count, depth, guard in [(-1,2,3,4),(0,0,3,4),(True,2,3,4),
                                          (0,2,0,4),(0,2,3,False),(0,2.0,3,4)]:
            with self.assertRaises(ValueError):
                certified_phase_grid(start, count, depth=depth, guard=guard)

    def test_observation_window_is_checked(self):
        c = certified_phase_grid(0, 8)
        for offset, count in [(8,1),(-1,1),(0,9),(0,0),(True,1)]:
            with self.assertRaises(ValueError):
                certified_haar_defect(c, offset, count)

    def test_source_primitive_mutation_is_rejected(self):
        _source_integer_enclosure.cache_clear()
        with patch('observational_succ.zero_anchored_haar.forcing', return_value=F(0)):
            with self.assertRaisesRegex(ValueError, 'four-pole'):
                certified_phase_grid(0,9)
        _source_integer_enclosure.cache_clear()


class IndependentWassersteinTests(unittest.TestCase):
    def test_grid_algorithm_matches_general_fraction_cdf_implementation(self):
        for points in product((0,1,7,15,16,31), repeat=3):
            law = canonical_law(tuple(F(k,32) for k in points))
            expected = interval_w1(law, digit_averaging_law(law))
            self.assertEqual(grid_haar_defect(points,32), expected)

    def test_constant_control_and_uniform_digit_grid(self):
        self.assertEqual(grid_haar_defect((0,)*13, 16), F(15,32))
        self.assertEqual(grid_haar_defect(tuple(range(16)),16), 0)
        law = canonical_law(tuple(F(k,16) for k in range(16)))
        self.assertEqual(interval_w1_haar(law),F(1,32))

    def test_exact_signed_overlap_matches_concatenated_law(self):
        for early, late in [((0,0),(0,0)),((0,0),(15,15)),
                            ((1,7,13),(2,8,14)),((1,1,15),(0,7,9))]:
            result = signed_block_overlap(early,late,16)
            self.assertEqual(result.combined, grid_haar_defect(early+late,16))
            self.assertEqual(result.combined,
                             (result.early+result.late)/2-result.overlap)
            self.assertGreaterEqual(result.overlap,0)
        self.assertEqual(signed_block_overlap((0,),(0,),16).overlap,0)
        self.assertGreater(signed_block_overlap((0,),(15,),16).overlap,0)

    def test_certified_defect_contains_finer_independent_observation(self):
        coarse = certified_phase_grid(0,32,depth=3)
        fine = certified_phase_grid(0,32,depth=9)
        d = certified_haar_defect(coarse)
        better = certified_haar_defect(fine)
        self.assertLessEqual(d.lower,better.lower)
        self.assertGreaterEqual(d.upper,better.upper)

    def test_residual_endpoints_are_outward(self):
        c = certified_phase_grid(0,32)
        big, small = certified_haar_defect(c), certified_haar_defect(c,0,16)
        lo,hi = contraction_residual(big,small,F(1,2),F(1,100))
        center = big.approximation-small.approximation/2-F(1,100)
        self.assertLessEqual(lo,center)
        self.assertGreaterEqual(hi,center)
        self.assertEqual(finite_verdict((F(-1),F(0))), 'CERTIFIED_FINITE_PASS')
        self.assertEqual(finite_verdict((F(1),F(2))), 'CERTIFIED_FINITE_FAIL')
        self.assertEqual(finite_verdict((F(-1),F(1))), 'UNRESOLVED_PRECISION')
        for invalid in ((0.0,1.0),(False,True),(F(1),F(0))):
            with self.assertRaises(ValueError):
                finite_verdict(invalid)

    def test_no_invalid_grid_is_coerced(self):
        for points,q in [((),16),((16,),16),((True,),16),((F(1,2),),16),((0,),17)]:
            with self.assertRaises(ValueError):
                grid_haar_defect(points,q)

    def test_finite_sample_floor_for_independently_generated_rational_orbits(self):
        for start in (F(),F(1,17),F(2,3),F(1,255),F(31,97)):
            phases = []
            x = start
            for n in range(1,33):
                phases.append(x)
                law = canonical_law(tuple(phases))
                self.assertGreaterEqual(interval_w1(law,digit_averaging_law(law)),
                                        orbit_defect_floor(n))
                x = (16*x) % 1
        self.assertEqual(contraction_error_floor(F(1,16)),F(77,512))
        self.assertGreater(F(77,512),F(2,15))
        self.assertEqual(contraction_error_floor(F(1,2)),0)


class PascalTests(unittest.TestCase):
    def test_partition_pascal_recursion_and_exact_moments(self):
        for m in range(9):
            for y in (F(),F(1,7),F(1,2),F(1)):
                row = bernstein_vector(m,y)
                self.assertEqual(sum(row,F()),1)
                self.assertTrue(all(x>=0 for x in row))
                if m:
                    old = (F(),)+bernstein_vector(m-1,y)+(F(),)
                    for j in range(m+1):
                        self.assertEqual(row[j], (1-y)*old[j+1]+y*old[j])

    def test_parity_is_exact_digit_character_not_circle_character(self):
        c = certified_phase_grid(0,33,depth=6)
        chars = certified_pascal_characters(c,0,(8,))
        expected = sum((-1)**(k//16**5) for k in c.points[:-1])
        self.assertEqual(chars[0].coefficients,(F(expected,32),)+(F(),)*7)
        self.assertEqual(chars[0].modulus_error,0)

    def test_all_character_components_sum_to_degree_zero(self):
        c = certified_phase_grid(3,18,depth=5)
        zero = certified_pascal_characters(c,0)
        higher = certified_pascal_characters(c,3)
        for h in range(1,16):
            row = [x for x in higher if x.frequency==h]
            self.assertEqual(tuple(sum((x.coefficients[k] for x in row),F())
                                   for k in range(8)),zero[h-1].coefficients)

    def test_full_pascal_certificate_bound_and_missing_components(self):
        c = certified_phase_grid(0,17,depth=6)
        bound = pascal_haar_upper(c,1)
        law = canonical_law(tuple(F(k,c.denominator) for k in c.points[:-1]))
        self.assertLessEqual(interval_w1_haar(law)+c.point_error,bound)
        with self.assertRaises(ValueError):
            pascal_haar_upper(replace(c,points=(0,)*c.count),1)

    def test_certification_cannot_skip_authentication_or_detach_observations(self):
        c = certified_phase_grid(0,17,depth=6)
        fake = replace(c, points=tuple((j%16)*16**5 for j in range(17)))
        with self.assertRaises(ValueError):
            certified_pascal_characters(fake,1)
        with self.assertRaises(TypeError):
            certified_pascal_characters(fake,1,verify=False)
        with self.assertRaises(TypeError):
            certified_haar_defect(fake,verify=False)
        with self.assertRaises(ValueError):
            pascal_haar_upper(certified_pascal_characters(c,1),1)

    def test_rejects_wrong_character_and_unsupported_degree(self):
        c = certified_phase_grid(0,5)
        for hs in ((0,),(16,),(True,),(8,8)):
            with self.assertRaises(ValueError):
                certified_pascal_characters(c,1,hs)
        with self.assertRaises(ValueError):
            pascal_haar_upper(c,2)
        with self.assertRaises(ValueError):
            replace(certified_pascal_characters(c,1)[0],modulus_error=F(-1))


if __name__ == '__main__':
    unittest.main()
