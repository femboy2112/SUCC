"""Exact finite source witnesses and rigorous analytic chi4 mutation controls."""
from dataclasses import FrozenInstanceError
from fractions import Fraction as Q
import unittest

from observational_succ.source_character_interaction import (
    character_four, gauss_sum_four, local_chi4_euler,
)
from observational_succ.tate_schwartz_functor import critical_mellin_character
from observational_succ.tate_chi4 import (
    Chi4SourceError, Chi4TateSource, two_adic_hecke, diagonal_hecke_receipt,
    ramified_test, ramified_fourier, ramified_fourier_closed,
    ramified_mellin_mass, source_fourier_multiplier,
    logarithmic_source_tape, validate_coefficient_tape,
    theta_tail_bound, theta_interval, theta_functional_probe,
    completed_theta_error, arithmetic_mutation_receipts,
)


class Chi4TateTests(unittest.TestCase):
    def test_source_descriptor_retains_original_atom_provenance(self):
        source = Chi4TateSource("declared-arithmetic-source", 9)
        self.assertEqual((source.conductor, source.parity, source.root_number), (4, 1, 1))
        for coefficient, ball in source.two_adic_atoms():
            self.assertEqual((ball.source_id, ball.epoch), (source.source_id, 9))
            self.assertEqual(ball.contains(1)-ball.contains(3), coefficient)
        with self.assertRaises(FrozenInstanceError):
            source.epoch = 10
        receipt = source.local_mellin_receipt(2, (2, 3, 5))
        self.assertEqual(receipt["finite_places"], ((2, Q(1)), (3, Q(9, 10)), (5, Q(25, 24))))
        self.assertFalse(receipt["finite_product_is_all_places"])

    def test_rational_hecke_diagonal_including_negative_valuations(self):
        for a in range(-25, 26):
            if not a:
                continue
            for b in range(1, 21):
                self.assertEqual(diagonal_hecke_receipt(Q(a, b))["diagonal_product"], 1)

    def test_two_adic_character_is_not_zero_at_uniformizer(self):
        self.assertEqual(character_four(2), 0)
        self.assertEqual(two_adic_hecke(2), 1)
        self.assertEqual(two_adic_hecke(-1), -1)
        for a in (Q(1, 6), Q(-5, 16), Q(18), Q(7, 5)):
            for b in (Q(3), Q(-8, 7), Q(5, 11)):
                self.assertEqual(two_adic_hecke(a*b), two_adic_hecke(a)*two_adic_hecke(b))

    def test_ramified_test_support_and_values(self):
        for n in range(-30, 31):
            self.assertEqual(ramified_test(n), character_four(n))
        self.assertEqual(ramified_test(Q(1, 3)), -1)
        self.assertEqual(ramified_test(Q(1, 2)), 0)

    def test_ramified_multiplicative_haar_mass_exact(self):
        self.assertEqual(ramified_mellin_mass(), Q(1))
        self.assertEqual(sum((Q(1, 4)*ramified_test(a)*two_adic_hecke(a)
                              for a in (1, 3)), Q(0)), Q(1, 2))

    def test_independent_atom_fourier_matches_conductor_formula(self):
        for numerator in range(-19, 20):
            for denominator in (1, 2, 3, 4, 5, 8, 12, 20, 32):
                xi = Q(numerator, denominator)
                for sign in (-1, 1):
                    self.assertEqual(ramified_fourier(xi, sign), ramified_fourier_closed(xi, sign))

    def test_ramified_fourier_support_is_exactly_valuation_minus_two(self):
        for numerator in (1, 3, 5, 7):
            self.assertNotEqual(ramified_fourier(Q(numerator, 4)), (0, 0))
        for xi in (0, 1, 2, Q(1, 2), Q(1, 8), Q(3, 16)):
            self.assertEqual(ramified_fourier(xi), (0, 0))

    def test_single_phase_flip_breaks_global_scalar_both_flips_preserve(self):
        self.assertEqual(source_fourier_multiplier(1, -1), 1)
        self.assertEqual(source_fourier_multiplier(-1, 1), 1)
        self.assertEqual(source_fourier_multiplier(1, 1), -1)
        self.assertEqual(source_fourier_multiplier(-1, -1), -1)
        self.assertEqual(ramified_fourier(Q(1, 4)), (Q(0), Q(-1, 2)))

    def test_gauss_sum_and_odd_real_phase_agree(self):
        gauss = gauss_sum_four()
        self.assertEqual((gauss["gauss_sum_real"], gauss["gauss_sum_imag"]), (0, 2))
        # tau/(i*sqrt(4)) = (2i)/(2i) = 1, exactly.
        self.assertEqual(gauss["normalized_root_number"], "1")
        self.assertEqual(source_fourier_multiplier(), 1)

    def test_signed_prime_power_tape_and_fake_composite_rejection(self):
        tape = {n: (p, sign) for n, p, sign in logarithmic_source_tape(81)}
        self.assertEqual(tape[3], (3, -1))
        self.assertEqual(tape[9], (3, 1))
        self.assertEqual(tape[27], (3, -1))
        self.assertEqual(tape[81], (3, 1))
        self.assertEqual(tape[8], (2, 0))
        self.assertNotIn(6, tape)
        self.assertNotIn(15, tape)

    def test_non_euler_prime_square_has_finite_coherence_witness(self):
        actual = tuple(character_four(n) for n in range(1, 13))
        good = validate_coefficient_tape(actual)
        self.assertIsNone(good["first_source_mismatch"])
        self.assertIsNone(good["multiplicativity_witness"])
        mutant = list(actual); mutant[8] = -1
        bad = validate_coefficient_tape(tuple(mutant))
        self.assertEqual(bad["first_source_mismatch"], (9, -1, 1))
        self.assertEqual(bad["multiplicativity_witness"], (3, 3, -1, 1))

    def test_completely_multiplicative_counterfeit_still_fails_source(self):
        result = validate_coefficient_tape((1,)*12)
        self.assertIsNone(result["multiplicativity_witness"])
        self.assertEqual(result["first_source_mismatch"], (2, 1, 0))
        self.assertFalse(result["global_source_certified"])

    def test_zero_tape_fails_unit_without_false_multiplicativity_witness(self):
        result = validate_coefficient_tape((0,)*12)
        self.assertIsNone(result["multiplicativity_witness"])
        self.assertEqual(result["unit_normalization_witness"], (1, 0, 1))
        self.assertEqual(result["first_source_mismatch"], (1, 0, 1))

    def test_omitted_places_are_visible_without_zeros(self):
        # Removing chi_2 makes the diagonal -1 character equal -1.
        self.assertEqual(diagonal_hecke_receipt(-1)["real_sign_character"], -1)
        self.assertNotEqual(Q(local_chi4_euler(3, 2, 1)["full"]), 1)
        self.assertEqual(Q(local_chi4_euler(3, 2, 1)["full"]), Q(9, 10))

    def test_conductor_and_parity_finite_witnesses(self):
        self.assertEqual(1 % 2, 3 % 2)
        self.assertNotEqual(character_four(1), character_four(3))
        self.assertEqual(character_four(1)+character_four(-1), 0)
        self.assertEqual(character_four(1)-character_four(-1), 2)

    def test_zero_modes_forbid_zeta_pole_import(self):
        self.assertEqual(ramified_test(0), 0)
        self.assertEqual(ramified_fourier(0), (0, 0))

    def test_half_density_mutation_is_exact_log_clock_drift(self):
        self.assertTrue(critical_mellin_character(Q(1, 2))["is_critical_fourier"])
        self.assertEqual(critical_mellin_character(Q(1, 2), Q(1, 8))["real_exponent_in_log_clock"], Q(1, 8))

    def test_theta_bounds_shrink_and_certify_nonzero(self):
        self.assertTrue(0 < theta_tail_bound(1, 5) < theta_tail_bound(1, 3))
        enclosure = theta_interval(1, 5)
        self.assertTrue(Q(9, 10) < enclosure.lo < enclosure.hi < Q(92, 100))

    def test_analytic_conductor_and_root_mutations_are_rigorously_separated(self):
        good = theta_functional_probe()
        self.assertFalse(good["rigorously_disjoint"])
        self.assertFalse(good["identity_proved_by_probe"])
        for mutant in (theta_functional_probe(conductor=1), theta_functional_probe(root=-1)):
            self.assertTrue(mutant["rigorously_disjoint"])
            self.assertFalse(mutant["zero_positions_used"])

    def test_completed_theta_strip_error_improves(self):
        for derivative in range(3):
            self.assertTrue(0 < completed_theta_error(-2, 3, 4, 18, derivative)
                            < completed_theta_error(-2, 3, 2, 6, derivative))

    def test_receipts_preserve_no_grh_and_non_euler_witness(self):
        result = arithmetic_mutation_receipts()
        self.assertFalse(result["GRH_proved"])
        self.assertFalse(result["fake_six_logjet_present_in_authentic_source"])
        self.assertEqual(result["fake_six_tape"]["multiplicativity_witness"], (2, 3, 1, 0))

    def test_domain_errors_are_explicit(self):
        for call in (lambda: Chi4TateSource(""), lambda: Chi4TateSource("source", True),
                     lambda: two_adic_hecke(0), lambda: ramified_test(0.25),
                     lambda: ramified_fourier(1, 0), lambda: theta_tail_bound(Q(1, 10), 1),
                     lambda: theta_functional_probe(2), lambda: completed_theta_error(3, 2, 4, 18)):
            with self.assertRaises(Chi4SourceError):
                call()


if __name__ == "__main__":
    unittest.main()
