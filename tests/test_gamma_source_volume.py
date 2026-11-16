"""Exact source and hostile controls for the Gamma source-volume interface."""
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial, prod
import unittest

from observational_succ.gamma_source_volume import (
    AffinePiDeterminant,
    fractional_grade_prefactor,
    fractional_grade_prefix,
    integer_grade_pgf,
    integer_grade_prefix,
    integer_grade_probability,
    shared_redrawn_grade,
    source_depth_ratio,
    source_hankel_certificate,
    source_hankel_determinant,
    source_moment_pi_coefficient,
)
from observational_succ.wavefront_oracle_two_stage import SourceGeometry, equal_stage_critical_grade


def compositions(total, length):
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(total + 1):
        for rest in compositions(total - first, length - 1):
            yield (first,) + rest


def enumerated_integer_grade(x, depth, grade):
    """Independent oracle: enumerate counts in 2*depth geometric stages."""
    u, v = x - x * x / 2, x * x / 2
    parameters = (u, v) * depth
    return sum((prod(((1 - theta) * theta**count
                      for theta, count in zip(parameters, allocation)), start=Q(1))
                for allocation in compositions(grade, len(parameters))), Q(0))


def multinomial_moment_coefficient(n):
    """Independent polynomial integral via multinomial, not polynomial products."""
    k = n - 1
    result = Q(0)
    for r1 in range(k + 1):
        for r3 in range(k - r1 + 1):
            for r4 in range(k - r1 - r3 + 1):
                r0 = k - r1 - r3 - r4
                multiplicity = Q(factorial(k), factorial(r0) * factorial(r1)
                                 * factorial(r3) * factorial(r4))
                coefficient = multiplicity * (-1)**r1 * Q(1, 2)**r3 * Q(-1, 4)**r4
                degree = r1 + 3 * r3 + 4 * r4
                result += coefficient / ((degree + 1) * (degree + 2))
    return 4 * result


def permutation_determinant(matrix):
    result = Q(0)
    for permutation in permutations(range(len(matrix))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(matrix)) for j in range(i + 1, len(matrix)))
        result += (-1)**inversions * prod((matrix[i][permutation[i]]
                                          for i in range(len(matrix))), start=Q(1))
    return result


class GammaSourceVolumeTests(unittest.TestCase):
    def test_unit_depth_recovers_inherited_authentic_grade_law(self):
        for x, grade in product((Q(0), Q(1, 7), Q(1, 2), Q(9, 10), Q(1)), range(19)):
            self.assertEqual(integer_grade_probability(x, 1, grade),
                             SourceGeometry(x).grade_probability(grade))

    def test_fractional_prefactors_compose_without_rounding_normalization(self):
        for x, alpha, beta in product((Q(0), Q(2, 5), Q(1)),
                                      (Q(0), Q(1, 2), Q(2, 3)),
                                      (Q(1, 3), Q(1, 2), Q(2))):
            left = fractional_grade_prefix(x, alpha, 10)
            right = fractional_grade_prefix(x, beta, 10)
            total = fractional_grade_prefix(x, alpha + beta, 10)
            for n in range(11):
                self.assertEqual(sum((left[j] * right[n - j] for j in range(n + 1)), Q(0)), total[n])
        for grade in range(13):
            self.assertEqual(fractional_grade_prefactor(1, Q(1, 2), grade), Q(1, 2**grade))

    def test_integer_grades_match_explicit_geometric_stage_enumeration(self):
        for x, depth, grade in product((Q(0), Q(2, 5), Q(1)), range(4), range(6)):
            self.assertEqual(integer_grade_probability(x, depth, grade),
                             enumerated_integer_grade(x, depth, grade))

    def test_endpoint_depth_counts_two_loops_per_unit(self):
        for depth, grade in product(range(1, 5), range(14)):
            self.assertEqual(integer_grade_probability(1, depth, grade),
                             equal_stage_critical_grade(2 * depth, grade))

    def test_zero_depth_and_full_pgf_normalization(self):
        for x, depth in product((Q(0), Q(1, 3), Q(1)), range(5)):
            self.assertEqual(integer_grade_pgf(x, depth, 1), 1)
            self.assertEqual(integer_grade_pgf(x, depth, 0), integer_grade_probability(x, depth, 0))
        self.assertEqual(integer_grade_prefix(Q(1, 3), 0, 4), (1, 0, 0, 0, 0))
        self.assertEqual(integer_grade_pgf(1, 1, -1), Q(1, 9))

    def test_source_moments_match_independent_multinomial_integral(self):
        expected = (Q(2), Q(7, 5), Q(2657, 2520), Q(100679, 120120),
                    Q(22645891, 32672640))
        for n, value in enumerate(expected, start=1):
            self.assertEqual(source_moment_pi_coefficient(n), value)
        for n in range(1, 12):
            self.assertEqual(source_moment_pi_coefficient(n), multinomial_moment_coefficient(n))

    def test_finite_program_depth_ratio_despite_unbounded_linear_rank(self):
        self.assertEqual(source_depth_ratio(1), 1)
        self.assertEqual(source_depth_ratio(2), Q(7, 10))
        self.assertEqual(source_depth_ratio(3), Q(2657, 5040))
        for n in range(1, 12):
            # m_1=2/pi and m_n=c_n/pi, tested as a rational identity before division by pi.
            self.assertEqual(2 * source_depth_ratio(n), multinomial_moment_coefficient(n))
        for n in range(1, 17):
            self.assertLessEqual(source_depth_ratio(n), 1)
            self.assertGreaterEqual(source_depth_ratio(n), Q(1, 4**(n-1)))

    def test_explicit_small_hankel_determinants(self):
        det2 = source_hankel_determinant(2)
        self.assertEqual((det2.pi_coefficient, det2.constant, det2.denominator_power),
                         (Q(7, 5), Q(-4), 2))
        det3 = source_hankel_determinant(3)
        self.assertEqual(det3.pi_coefficient, Q(280283645, 4540536000))
        self.assertEqual(det3.constant, Q(-872553024, 4540536000))
        det4 = source_hankel_determinant(4)
        denominator = 1295065442706719523840000
        self.assertEqual(det4.pi_coefficient, Q(117152940838530920085, denominator))
        self.assertEqual(det4.constant, Q(-367695897705032097344, denominator))

    def test_determinants_match_independent_permutation_oracle(self):
        # A rational symbol substitution validates the affine identity; it is not pi.
        p = Q(22, 7)
        for size in range(1, 6):
            matrix = tuple(tuple(Q(1) if i + j == 0 else source_moment_pi_coefficient(i + j) / p
                                 for j in range(size)) for i in range(size))
            determinant = source_hankel_determinant(size)
            self.assertEqual((determinant.pi_coefficient * p + determinant.constant) / p**size,
                             permutation_determinant(matrix))

    def test_original_bbp_enclosures_certify_sizes_one_through_five(self):
        for size in range(1, 6):
            certificate = source_hankel_certificate(size, pi_terms=4)
            self.assertGreater(certificate.pi_lower, 3)
            self.assertLess(certificate.pi_upper, Q(22, 7))
            self.assertTrue(certificate.strict_positive)
            self.assertLessEqual(certificate.lower, certificate.upper)
            midpoint = (certificate.pi_lower + certificate.pi_upper) / 2
            determinant = certificate.determinant
            at_midpoint = ((determinant.pi_coefficient * midpoint + determinant.constant)
                           / midpoint**determinant.denominator_power)
            self.assertLessEqual(certificate.lower, at_midpoint)
            self.assertGreaterEqual(certificate.upper, at_midpoint)

    def test_interval_extension_retains_negative_and_positive_numerators(self):
        determinant = source_hankel_determinant(2)
        low, high = determinant.enclose(2, 4)
        for p in (Q(2), Q(5, 2), Q(3), Q(7, 2), Q(4)):
            value = (determinant.pi_coefficient * p + determinant.constant) / p**2
            self.assertLessEqual(low, value)
            self.assertGreaterEqual(high, value)
        for lo, hi in ((0, 3), (4, 3), (-1, 3)):
            with self.assertRaises(ValueError):
                determinant.enclose(lo, hi)

    def test_retained_and_redrawn_source_are_different_models(self):
        sources = ((Q(0), Q(1, 2)), (Q(1), Q(1, 2)))
        comparison = shared_redrawn_grade(sources, 1, 1, 0)
        self.assertEqual(comparison.shared, Q(17, 32))
        self.assertEqual(comparison.redrawn, Q(25, 64))
        self.assertEqual(comparison.defect, Q(9, 64))
        self.assertNotEqual(comparison.shared, comparison.redrawn)

    def test_single_source_and_zero_depth_have_no_projection_defect(self):
        for x, grade in product((Q(0), Q(1, 3), Q(1)), range(9)):
            comparison = shared_redrawn_grade(((x, Q(1)),), 2, 1, grade)
            self.assertEqual(comparison.defect, 0)
        sources = ((Q(0), Q(1, 3)), (Q(3, 5), Q(2, 3)))
        for grade in range(8):
            self.assertEqual(shared_redrawn_grade(sources, 0, 2, grade).defect, 0)

    def test_invalid_source_mixtures_fail_closed(self):
        for sources in ((), ((0, Q(1, 2)),), ((0, -1), (1, 2)), ((-1, 1),), ((0,),)):
            with self.assertRaises(ValueError):
                shared_redrawn_grade(sources, 1, 1, 0)

    def test_exact_types_and_budgets_fail_closed(self):
        for invalid in (True, 0.5, "1/2"):
            for call in (
                lambda: fractional_grade_prefix(invalid, 1, 0),
                lambda: fractional_grade_prefix(0, invalid, 0),
                lambda: integer_grade_pgf(0, 1, invalid),
                lambda: shared_redrawn_grade(((0, invalid),), 1, 1, 0),
            ):
                with self.assertRaises(TypeError):
                    call()
            with self.assertRaises(TypeError):
                AffinePiDeterminant(invalid, 0, 1)
            with self.assertRaises(TypeError):
                AffinePiDeterminant(1, invalid, 1)
        for call in (
            lambda: fractional_grade_prefix(0, -1, 0),
            lambda: fractional_grade_prefix(0, 1, 129),
            lambda: integer_grade_prefix(0, True, 0),
            lambda: integer_grade_pgf(0, 1, 2),
            lambda: source_moment_pi_coefficient(0),
            lambda: source_moment_pi_coefficient(17),
            lambda: source_depth_ratio(True),
            lambda: source_hankel_determinant(6),
            lambda: source_hankel_certificate(1, 33),
            lambda: shared_redrawn_grade(((0, 1),), 32, 1, 0),
        ):
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main(verbosity=2)
