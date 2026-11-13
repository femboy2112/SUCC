"""Calibrated rational tests for the Yang--Mills/SUCC comparison slice."""

from fractions import Fraction as F
import unittest

from observational_succ.ym_phase_transport import (
    affine_residual,
    check_affine_phases,
    common_phase_comparison,
    contraction_factor,
    phase_diameter_bound,
    target_reader,
    target_stability_bound,
    weighted_sup,
)


class CommonExpansionTests(unittest.TestCase):
    def test_opposite_remainders_need_factor_two(self):
        result = common_phase_comparison((2, -3), F(29, 4), (2, -1),
                                         F(-9, 4), (2, 2), F(1, 4))
        self.assertEqual(result["difference_defect"], F(1, 2))
        self.assertEqual(result["difference_budget"], F(1, 2))

    def test_zero_remainders_do_not_identify_phases(self):
        result = common_phase_comparison((1,), 1, (1,), -1, (-1,), 0)
        self.assertEqual(result["difference_defect"], 0)
        self.assertNotEqual(1, -1)

    def test_phase_dependent_coefficients_cannot_be_substituted(self):
        # Left: 1 = 1*1. Right: 2 = 2*1. Each is exact separately;
        # pretending that their coefficient is the same is rejected.
        with self.assertRaises(ValueError):
            common_phase_comparison((1,), 1, (1,), 2, (1,), 0)

    def test_mutated_residual_budget_is_rejected(self):
        with self.assertRaises(ValueError):
            common_phase_comparison((1,), F(5, 4), (1,), 1, (1,), F(1, 5))

    def test_signed_channel_cancellation_is_preserved(self):
        result = common_phase_comparison((3, -3), 0, (5, 5), 0, (7, 7), 0)
        self.assertEqual(result["difference_defect"], 0)

    def test_unfitted_rational_pairs(self):
        for denominator in (7, 19, 53):
            coefficients = (F(2, denominator), -F(5, denominator + 2))
            left, right = (F(7, 3), F(-11, 4)), (F(-17, 6), F(13, 5))
            lbase = sum(c * x for c, x in zip(coefficients, left))
            rbase = sum(c * x for c, x in zip(coefficients, right))
            epsilon = F(1, denominator ** 2)
            result = common_phase_comparison(coefficients, lbase + epsilon, left,
                                             rbase - epsilon, right, epsilon)
            self.assertEqual(abs(result["difference_defect"]), 2 * epsilon)


class ContractionTests(unittest.TestCase):
    def test_sharp_scalar_diameter(self):
        result = check_affine_phases(((F(1, 2),),), (1,), (0,),
                                    ((F(1, 3),), (-F(1, 3),)), F(1, 6))
        self.assertEqual(result["observed_diameter"], F(2, 3))
        self.assertEqual(result["diameter_bound"], F(2, 3))

    def test_weighted_certificate_when_unweighted_rows_exceed_one(self):
        operator = ((0, 2), (F(1, 8), 0))
        self.assertEqual(contraction_factor(operator, (1, 1)), 2)
        self.assertEqual(contraction_factor(operator, (4, 1)), F(1, 2))
        result = check_affine_phases(operator, (4, 1), (0, 0),
                                    ((4, 1), (-4, -1)), F(1, 2))
        self.assertEqual(result["observed_diameter"], 2)
        self.assertEqual(result["diameter_bound"], 2)

    def test_signed_row_sum_mutation_fails(self):
        operator = ((1, -1), (0, 0))
        self.assertEqual(sum(operator[0]), 0)
        self.assertEqual(contraction_factor(operator, (1, 1)), 2)
        with self.assertRaises(ValueError):
            phase_diameter_bound(operator, (1, 1), F(1, 100))

    def test_same_bias_is_required(self):
        with self.assertRaises(ValueError):
            check_affine_phases(((0,),), (1,), (1,), ((1,), (2,)), 0)

    def test_identity_has_no_contraction_margin(self):
        with self.assertRaises(ValueError):
            phase_diameter_bound(((1,),), (1,), 0)

    def test_small_error_with_closing_margin_keeps_unit_diameter(self):
        for n in (2, 7, 41, 1009, 100003):
            result = check_affine_phases(((1 - F(1, n),),), (1,), (0,),
                                        ((F(1, 2),), (-F(1, 2),)), F(1, 2*n))
            self.assertEqual(result["observed_diameter"], 1)
            self.assertEqual(result["diameter_bound"], 1)

    def test_fixed_margin_gives_vanishing_bound(self):
        self.assertEqual(phase_diameter_bound(((F(3, 4),),), (1,), F(1, 10000)),
                         F(1, 1250))

    def test_known_affine_fixed_point(self):
        self.assertEqual(affine_residual(((F(1, 3),),), (2,), (3,)), (0,))
        result = check_affine_phases(((F(1, 3),),), (1,), (2,), ((3,), (3,)), 0)
        self.assertEqual(result["observed_diameter"], 0)

    def test_domain_mutations(self):
        for bad in (0.5, True, "1/2"):
            with self.assertRaises(TypeError):
                contraction_factor(((bad,),), (1,))
        for bad_weights in ((0,), (-1,), (1, 2)):
            with self.assertRaises(ValueError):
                contraction_factor(((0,),), bad_weights)
        with self.assertRaises(ValueError):
            weighted_sup((), ())
        with self.assertRaises(ValueError):
            contraction_factor(((1, 2),), (1,))
        with self.assertRaises(ValueError):
            check_affine_phases(((0,),), (1,), (0,), (), 0)
        with self.assertRaises(ValueError):
            phase_diameter_bound(((0,),), (1,), -1)


class TargetQuotientTests(unittest.TestCase):
    def test_invisible_resonance_can_remain(self):
        operator = ((1, 0), (0, F(1, 2)))
        self.assertEqual(contraction_factor(operator, (1, 1)), 1)
        result = target_stability_bound(operator, ((0, 1),), F(1, 100))
        self.assertEqual(result["reader"], ((F(0), F(2)),))
        self.assertEqual(result["target_difference_bound"], F(1, 25))
        # The first coordinate can have arbitrary, persistent phase differences.
        left, right = (1000, F(1, 50)), (-1000, -F(1, 50))
        self.assertEqual(affine_residual(operator, (0, 0), left), (0, F(1, 100)))
        self.assertEqual(affine_residual(operator, (0, 0), right), (0, -F(1, 100)))
        self.assertEqual(abs(left[1] - right[1]), result["target_difference_bound"])

    def test_visible_resonance_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "ker"):
            target_reader(((1, 0), (0, F(1, 2))), ((1, 0),))

    def test_oscillating_direction_needs_no_contraction(self):
        self.assertEqual(contraction_factor(((-1,),), (1,)), 1)
        result = target_stability_bound(((-1,),), ((1,),), F(1, 10))
        self.assertEqual(result["reader"], ((F(1, 2),),))
        self.assertEqual(result["target_difference_bound"], F(1, 10))

    def test_quarter_turn_uses_signed_inverse(self):
        result = target_stability_bound(((0, -1), (1, 0)), ((1, 0), (0, 1)), F(1, 20))
        self.assertEqual(result["reader"], ((F(1, 2), -F(1, 2)), (F(1, 2), F(1, 2))))
        self.assertEqual(result["reader_norm"], 1)

    def test_radix_invariance_chain_has_a_visible_boundary_mode(self):
        for depth in (2, 5, 17):
            # x_j=x_(j+1), with last coordinate unconstrained: all constants survive.
            operator = [[F(0) for _ in range(depth)] for _ in range(depth)]
            for row in range(depth - 1):
                operator[row][row + 1] = F(1)
            operator[-1][-1] = F(1)
            target = ((F(1),) + (F(0),) * (depth - 1),)
            with self.assertRaises(ValueError):
                target_reader(operator, target)
            self.assertEqual(affine_residual(operator, (0,) * depth, (1,) * depth),
                             (0,) * depth)
            # Adding the extra boundary estimate changes the hypothesis.
            operator[-1][-1] = F(0)
            result = target_stability_bound(operator, target, F(1, depth ** 2))
            self.assertEqual(result["reader_norm"], depth)
            self.assertEqual(result["target_difference_bound"], F(2, depth))

    def test_closing_margin_is_paid_by_reader_norm(self):
        for n in (2, 13, 1009):
            result = target_stability_bound(((1 - F(1, n),),), ((1,),), F(1, 2*n))
            self.assertEqual(result["reader_norm"], n)
            self.assertEqual(result["target_difference_bound"], 1)

    def test_rectangular_target_and_zero_target(self):
        self.assertEqual(target_reader(((0, 0), (0, 0)), ((1, 2), (3, 4), (5, 6))),
                         ((1, 2), (3, 4), (5, 6)))
        self.assertEqual(target_reader(((1,),), ((0,),)), ((0,),))
        with self.assertRaises(ValueError):
            target_reader(((0,),), ())
        with self.assertRaises(ValueError):
            target_reader(((0,),), ((1, 2),))


if __name__ == "__main__":
    unittest.main()
