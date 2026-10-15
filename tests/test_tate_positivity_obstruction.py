"""Independent rational controls for the scoped Tate positivity obstruction."""
from fractions import Fraction as F
import unittest

from observational_succ.tate_positivity_obstruction import (
    dilation_polynomial, normalized_multiplier, normalized_source_operator,
    odd_test_moments, positivity_obstruction_certificate, relative_gaussian_mellin,
)


def even_beta_integral(power_x: int, power_one_minus_x2: int) -> F:
    """Integral [-1,1] x^(2m)(1-x^2)^k dx by beta recurrence.

    Independent of production polynomial expansion/antiderivatives.
    Start at k=0; B(a,k+1)/B(a,k)=k/(a+k).
    """
    a = F(power_x, 2)+F(1, 2)
    result = 1/a
    for k in range(1, power_one_minus_x2+1):
        result *= k/(a+k)
    return result


class TatePositivityObstructionTests(unittest.TestCase):
    def test_operator_reconstructs_normalized_source(self):
        self.assertEqual(dilation_polynomial((1,)), (F(1, 2), F(-2)))
        self.assertEqual(normalized_source_operator((1,)), (1, -32, F(64, 3)))
        p = (F(1),)
        for _ in range(7):
            p = normalized_source_operator(p)
            self.assertEqual(p[0], 1)
            self.assertEqual(relative_gaussian_mellin(p, 1), 1)

    def test_mellin_intertwining_on_nontrivial_polynomials_and_parameters(self):
        for p in ((1,), (0, 1), (3, -2, 7), (F(1, 7), 0, -5, F(2, 3))):
            for s in (F(1, 5), F(1, 2), 1, 2, F(13, 3)):
                base = relative_gaussian_mellin(p, s)
                self.assertEqual(relative_gaussian_mellin(dilation_polynomial(p), s),
                                 (F(1, 2)-s)*base)
                self.assertEqual(relative_gaussian_mellin(normalized_source_operator(p), s),
                                 normalized_multiplier(s)*base)

    def test_normalization_symmetry_and_source_discriminator(self):
        for s in (F(-7, 3), 0, F(1, 4), F(1, 2), 1, 2, F(19, 5)):
            self.assertEqual(normalized_multiplier(s), normalized_multiplier(1-s))
        self.assertEqual(normalized_multiplier(0), 1)
        self.assertEqual(normalized_multiplier(1), 1)
        self.assertEqual(normalized_multiplier(F(1, 4)), 0)
        self.assertEqual(normalized_multiplier(F(3, 4)), 0)
        self.assertEqual(normalized_multiplier(2), F(35, 3))
        self.assertLess(positivity_obstruction_certificate()["first_iterate_ratio_at_u_1"], 0)

    def test_rational_moments_by_independent_beta_recurrence(self):
        r = odd_test_moments()
        self.assertEqual(r["positive_half_first_moment"], even_beta_integral(2, 3)/2)
        self.assertEqual(r["positive_half_first_moment"], F(16, 315))
        self.assertEqual(r["l2_squared"], even_beta_integral(2, 6))
        self.assertEqual(r["l2_squared"], F(2048, 45045))
        # f'=(1-x^2)^2(1-7x^2), so (f')^2=(1-x^2)^4(1-14x^2+49x^4).
        beta_derivative = (even_beta_integral(0, 4)-14*even_beta_integral(2, 4)
                           +49*even_beta_integral(4, 4))
        self.assertEqual(r["derivative_l2_squared"], beta_derivative)
        self.assertEqual(beta_derivative, F(3072, 5005))

    def test_complete_countermodel_bound_is_strictly_negative(self):
        r = positivity_obstruction_certificate()
        self.assertEqual(r["transform_at_quarter_lower_bound"], F(8, 315))
        self.assertEqual(r["added_divisor_form_upper_bound"], -F(128, 99225))
        self.assertEqual(r["coarse_modified_strict_upper_bound"], -F(127388, 99225))
        self.assertLess(r["modified_complete_form_strict_upper_bound"],
                        r["coarse_modified_strict_upper_bound"])
        self.assertTrue(r["modified_complete_form_negative"])
        self.assertFalse(r["canonical_weil_positivity_proved"])
        self.assertFalse(r["actual_zeta_zero_positions_used"])
        self.assertFalse(r["RH_proved"])

    def test_small_multiplicity_bound_does_not_claim_sign(self):
        r = positivity_obstruction_certificate(1)
        self.assertLess(r["added_divisor_form_upper_bound"], 0)
        self.assertGreater(r["modified_complete_form_strict_upper_bound"], 0)
        self.assertFalse(r["modified_complete_form_negative"])

    def test_mutation_of_positive_multiplier_coefficient_is_detected(self):
        # A dropped normalization constant destroys the source moment at s=1.
        mutant = (F(0), F(-32), F(64, 3))
        self.assertNotEqual(relative_gaussian_mellin(mutant, 1), 1)
        # Reversing the divisor sign would fail this explicit negative receipt.
        r = positivity_obstruction_certificate()
        positive_mutation = (r["canonical_complete_form_strict_upper_bound"]
                             - r["multiplicity"]*r["added_divisor_form_upper_bound"])
        self.assertGreater(positive_mutation, 0)

    def test_invalid_exact_or_domain_inputs_fail_closed(self):
        for bad in (True, 0, -1, 1.5, 1_000_001):
            with self.assertRaises(ValueError):
                positivity_obstruction_certificate(bad)
        for bad in (0, -1, 0.5, True):
            with self.assertRaises(ValueError):
                relative_gaussian_mellin((1,), bad)
        with self.assertRaises(ValueError):
            normalized_source_operator((1.0,))


if __name__ == "__main__":
    unittest.main()
