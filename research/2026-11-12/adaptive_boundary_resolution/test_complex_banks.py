"""Exact calibration and hostile controls; no fitted asymptotic tests."""

from fractions import Fraction as F
import unittest

from complex_banks import (
    Bank, Gaussian, I, ONE, ZERO, bank_response, canonical_bank,
    control_report, cumulative_bank, damped_minorant, finite_prefix_impostor,
    omega_sieve, source_cumulative_direct, source_cumulative_triangle,
    source_response, twist_bank, two_node_minorant,
)


def trial_omega(value):
    answer, divisor = 0, 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            answer += 1
            value //= divisor
        divisor += 1
    return answer + int(value > 1)


class ExactArithmeticTests(unittest.TestCase):
    def test_gaussian_arithmetic_and_phase_are_exact(self):
        self.assertEqual([I**k for k in range(5)], [ONE, I, -ONE, -I, ONE])
        z = Gaussian(F(3, 5), F(4, 5))
        self.assertEqual(z * z.conjugate(), ONE)
        self.assertEqual(z / z, ONE)
        self.assertEqual((z + I) * (z - I), z**2 + ONE)

    def test_inexact_and_oracle_inputs_are_rejected(self):
        for bad in (0.5, True, "1/2", complex(0, 1)):
            with self.assertRaises(ValueError):
                Gaussian(bad)
        for bad_node in (0, Gaussian(2), Gaussian(1, 1)):
            with self.assertRaises(ValueError):
                source_response(bad_node, 3)
        with self.assertRaises(ValueError):
            Bank(((ZERO, ONE),))

    def test_bank_pairing_normalization_and_distinctness(self):
        with self.assertRaises(ValueError):
            Bank(((I, ONE),))
        with self.assertRaises(ValueError):
            Bank(((ONE, Gaussian(2)),))
        with self.assertRaises(ValueError):
            Bank(((ONE, Gaussian(F(1, 2))), (ONE, Gaussian(F(1, 2)))))
        bank = canonical_bank(((ONE, 2), (ONE, -1)))
        self.assertEqual(bank.terms, ((ONE, ONE),))
        # Normalization alone deliberately does not imply the sign condition.
        self.assertEqual(bank.first_positive_grade(1), 1)

    def test_sieve_matches_independent_trial_division(self):
        omega = omega_sieve(512)
        self.assertEqual(omega[1], 0)
        self.assertEqual(tuple(omega[1:]), tuple(trial_omega(n) for n in range(1, 513)))


class ComplexBankControls(unittest.TestCase):
    def test_twisted_minorant_has_exact_all_residue_formula(self):
        for radius, inner in ((F(1), F(1, 2)), (F(1, 2), F(1, 4))):
            bank = twist_bank(two_node_minorant(radius, inner))
            self.assertEqual(bank.evaluate(0), 1)
            for h in range(1, 65):
                base = (radius * inner**h - inner * radius**h) / (radius - inner)
                cosine = (1, 0, -1, 0)[h % 4]
                self.assertEqual(bank.evaluate(h), base * (2 - cosine))
                self.assertLessEqual(bank.evaluate(h), 0)

    def test_outer_phase_mean_and_energy_have_correct_sign(self):
        bank = twist_bank(two_node_minorant())
        dominant = bank.dominant_circle()
        self.assertEqual(dominant["radius_squared"], 1)
        self.assertEqual(dominant["positive_real_coefficient"], -2)
        self.assertEqual(dominant["energy"], F(9, 2))
        periodic = [sum((b * z**h for z, b in dominant["terms"]), ZERO).real
                    for h in range(4)]
        self.assertEqual(sum(periodic) / 4, -2)
        self.assertEqual(sum(value**2 for value in periodic) / 4, F(9, 2))

    def test_prefix_impostor_fails_after_three_passing_grades(self):
        bank = finite_prefix_impostor()
        self.assertEqual(bank.evaluate(0), 1)
        self.assertEqual([bank.evaluate(h) for h in range(1, 4)], [F(-1, 3)] * 3)
        self.assertIsNone(bank.first_positive_grade(3))
        self.assertEqual(bank.first_positive_grade(4), 4)
        self.assertEqual(bank.evaluate(4), 1)
        self.assertEqual(bank.dominant_circle()["positive_real_coefficient"], 0)

    def test_phase_imbalance_mutation_is_rejected(self):
        with self.assertRaises(ValueError):
            Bank(((I, Gaussian(F(1, 2))), (-I, Gaussian(F(1, 3))),
                  (Gaussian(F(1, 2)), Gaussian(F(1, 6)))))

    def test_true_minorant_cumulative_sign_changes_after_positive_prefix(self):
        bank = twist_bank(two_node_minorant())
        self.assertEqual([bank_response(bank, n) for n in range(2, 7)],
                         [F(1), F(1), F(-1, 2), F(-1), F(-2)])
        self.assertEqual([cumulative_bank(bank, n) for n in range(2, 7)],
                         [F(1), F(2), F(3, 2), F(1, 2), F(-3, 2)])

    def test_cutoff_frozen_bank_matches_finite_prime_pair_counts(self):
        cutoff = 16
        bank = twist_bank(damped_minorant(8))
        # floor(log2(cutoff^2))-2=6, so every encountered positive grade
        # lies among the explicitly annihilated grades 1,...,7.
        self.assertEqual(bank.evaluate(0), 1)
        for h in range(1, 8):
            self.assertEqual(bank.evaluate(h), 0)
        for n in range(2, cutoff + 1):
            direct_primes = sum(trial_omega(n + a) == trial_omega(n - a) == 1
                                for a in range(n - 1))
            self.assertEqual(bank_response(bank, n), direct_primes)


class SourceTriangleControls(unittest.TestCase):
    def test_endpoint_and_diagonal_normalizations(self):
        for z in (Gaussian(F(1, 2)), I, -ONE, ONE):
            self.assertEqual(source_response(z, 2), ONE)
            self.assertEqual(source_cumulative_direct(z, 3), Gaussian(2) + z)
            self.assertEqual(source_cumulative_triangle(z, 3), Gaussian(2) + z)

    def test_complex_triangle_equals_direct_midpoint_sum(self):
        for z in (Gaussian(F(1, 2)), Gaussian(0, F(1, 2)),
                  Gaussian(F(3, 5), F(4, 5)), -ONE, ONE):
            for cutoff in (2, 3, 4, 7, 16):
                self.assertEqual(source_cumulative_direct(z, cutoff),
                                 source_cumulative_triangle(z, cutoff))

    def test_response_linear_combination_equals_grade_evaluation(self):
        bank = twist_bank(two_node_minorant(F(1, 2), F(1, 4)))
        for n in range(2, 17):
            mixed = sum((b * source_response(z, n) for z, b in bank.terms), ZERO)
            self.assertEqual(mixed, Gaussian(bank_response(bank, n)))

    def test_algebraic_diagonal_cannot_be_replaced_by_modulus(self):
        # At cutoff 4 the diagonal weights are 1,1,i, giving 1, not 3.
        actual_diagonal = ONE**2 + ONE**2 + I**2
        wrong_diagonal = ONE + ONE + ONE
        self.assertEqual(actual_diagonal, ONE)
        self.assertNotEqual(actual_diagonal, wrong_diagonal)
        self.assertEqual((wrong_diagonal - actual_diagonal) / 2, ONE)

    def test_unweighted_endpoint_matches_exact_pair_count(self):
        for cutoff in (2, 3, 8, 16):
            self.assertEqual(source_cumulative_triangle(ONE, cutoff),
                             Gaussian(cutoff * (cutoff - 1) // 2))

    def test_report_discloses_finite_scope(self):
        report = control_report()
        self.assertIn("no numerical asymptotic inference", report["scope"])
        self.assertEqual(report["impostor_first_positive_grade"], 4)
        self.assertEqual(report["true_minorant_cumulative_2_through_6"][-1], "-3/2")


if __name__ == "__main__":
    unittest.main()
