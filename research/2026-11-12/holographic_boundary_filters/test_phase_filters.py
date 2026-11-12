"""Exact hostile controls for finite target and phase certificates."""

from fractions import Fraction as F
from itertools import product
import unittest

from phase_filters import (
    approximate_target_certificate,
    control_report,
    cyclic_convolution,
    cyclic_correlation,
    cyclic_triple,
    cyclotomic_conjugate,
    cyclotomic_multiply,
    cyclotomic_polynomial,
    exact_bispectrum,
    exact_fourier,
    exact_power,
    exact_triple_fourier,
    nullspace,
    observations,
    shift,
    solve_linear,
    support_relation_rank,
    target_identifiability,
)


class TargetCertificateTests(unittest.TestCase):
    def test_exact_target_in_span(self):
        filters = [[1, 1, 1, 1], [0, 0, 1, 1]]
        target = [-1, -1, 2, 2]
        cert = target_identifiability(filters, target)
        self.assertTrue(cert["identified"])
        self.assertEqual(cert["coefficients"], (F(-1), F(3)))

    def test_annihilator_gives_two_actual_probabilities(self):
        filters = [[1, 1, 1, 1], [0, 0, 1, 1]]
        target = [0, 1, 0, 1]
        cert = target_identifiability(filters, target)
        self.assertFalse(cert["identified"])
        p, q = cert["positive_law"], cert["negative_law"]
        self.assertEqual(sum(p), 1)
        self.assertEqual(sum(q), 1)
        self.assertGreaterEqual(min(p + q), 0)
        self.assertEqual(observations(filters, p), observations(filters, q))
        self.assertEqual(abs(cert["target_gap"]), 1)

    def test_sharp_diameter_in_four_atom_control(self):
        filters = [[1, 1, 1, 1], [0, 0, 1, 1]]
        cert = approximate_target_certificate(
            filters, [0, 1, 0, 1], [F(1, 2), 0], [1, F(1, 2)], [0, 0]
        )
        # A constant half approximates this target within 1/2.  The preceding
        # exact indistinguishable pair attains diameter 1, proving sharpness.
        self.assertEqual(cert["radius"], F(1, 2))
        self.assertEqual(cert["center"], F(1, 2))

    def test_noisy_dual_certificate_pays_coefficient_cost(self):
        filters = [[1, 1, 1, 1], [0, 0, 1, 1]]
        target = [-1, -1, 2, 2]
        cert = approximate_target_certificate(
            filters, target, [-1, 3], [1, F(51, 100)], [0, F(1, 100)]
        )
        self.assertEqual(cert["radius"], F(3, 100))
        self.assertEqual(cert["coefficient_l1"], 4)
        self.assertLessEqual(abs(F(1, 2) - cert["center"]), cert["radius"])

    def test_redundant_rows_do_not_create_information(self):
        cert = target_identifiability(
            [[1, 1, 1], [0, 1, 1], [0, 2, 2]], [0, 0, 1]
        )
        self.assertFalse(cert["identified"])

    def test_exact_solver_rejects_inconsistent_mutant(self):
        self.assertIsNone(solve_linear([[1], [1]], [0, 1]))
        self.assertEqual(solve_linear([[1, 1], [2, 2]], [1, 2]), (F(1), F(0)))

    def test_nullspace_is_verified_directly(self):
        matrix = [[1, 1, 1, 1], [0, 1, 2, 3], [0, 2, 4, 6]]
        basis = nullspace(matrix)
        self.assertEqual(len(basis), 2)
        for vector in basis:
            self.assertEqual(observations(matrix, vector), (0, 0, 0))

    def test_invalid_mass_contract_and_errors_rejected(self):
        with self.assertRaises(ValueError):
            target_identifiability([[1, 0]], [0, 1])
        with self.assertRaises(ValueError):
            approximate_target_certificate([[1, 1]], [1, 0], [1], [1], [-1])

    def test_exact_input_contract_rejects_float_bool_and_string(self):
        for bad in (0.5, True, "1/2"):
            with self.subTest(value=bad, function="target_identifiability"):
                with self.assertRaises(ValueError):
                    target_identifiability([[1, 1]], [bad, 0])
                with self.assertRaises(ValueError):
                    target_identifiability([[1, 1], [bad, 0]], [0, 1])
            approximate_mutants = (
                ([[1, bad]], [F(1, 2)] * 2, [F(1, 2)], [1], [0]),
                ([[1, 1]], [bad, F(1, 2)], [F(1, 2)], [1], [0]),
                ([[1, 1]], [F(1, 2)] * 2, [bad], [1], [0]),
                ([[1, 1]], [F(1, 2)] * 2, [F(1, 2)], [bad], [0]),
                ([[1, 1]], [F(1, 2)] * 2, [F(1, 2)], [1], [bad]),
            )
            for index, args in enumerate(approximate_mutants):
                with self.subTest(value=bad, function="approximate_target_certificate", argument=index):
                    with self.assertRaises(ValueError):
                        approximate_target_certificate(*args)
            for function in (exact_fourier, cyclic_triple):
                with self.subTest(value=bad, function=function.__name__):
                    with self.assertRaises(ValueError):
                        function((F(1, 2), bad))

        # Valid exact rational values continue to satisfy the public contract.
        identified = target_identifiability(
            [[F(1), F(1)]], [F(1, 2), F(1, 2)]
        )
        self.assertEqual(identified["coefficients"], (F(1, 2),))
        approximate = approximate_target_certificate(
            [[F(1), F(1)]], [F(1, 2)] * 2,
            [F(1, 2)], [F(1)], [F(0)],
        )
        self.assertEqual((approximate["center"], approximate["radius"]), (F(1, 2), F(0)))
        self.assertEqual(exact_fourier((F(1, 2), F(1, 2))), ((F(1),), (F(0),)))
        self.assertEqual(cyclic_triple((F(1, 2), F(1, 2))), ((F(1, 4),) * 2,) * 2)


class ExactFourierTests(unittest.TestCase):
    def test_cyclotomic_moduli_against_known_polynomials(self):
        self.assertEqual(cyclotomic_polynomial(3), (1, 1, 1))
        self.assertEqual(cyclotomic_polynomial(6), (1, -1, 1))
        self.assertEqual(cyclotomic_polynomial(12), (1, 0, -1, 0, 1))

    def test_conjugation_is_involution_and_preserves_norm(self):
        for q in (3, 6, 12):
            for value in exact_fourier(tuple(range(q))):
                conjugate = cyclotomic_conjugate(value, q)
                self.assertEqual(cyclotomic_conjugate(conjugate, q), value)
                norm = cyclotomic_multiply(value, conjugate, q)
                self.assertEqual(cyclotomic_conjugate(norm, q), norm)

    def test_power_is_independent_transform_of_autocorrelation(self):
        for signal in ((2, -1, 4), (28, 21, 7, 0, 7, 21), tuple(range(12))):
            self.assertEqual(exact_power(signal), exact_fourier(cyclic_correlation(signal)))

    def test_bispectrum_matches_direct_double_transform_of_triples(self):
        for signal in ((2, -1, 4), (28, 21, 7, 0, 7, 21), tuple(range(12))):
            self.assertEqual(exact_bispectrum(signal), exact_triple_fourier(signal))

    def test_sign_mutation_is_detected(self):
        signal = (1, 0, 2, 3, 0)
        spectrum = exact_bispectrum(signal)
        # Reflection conjugates the bispectrum; omitting conjugation is not
        # harmless for this asymmetric control.
        reflected = (signal[0],) + tuple(reversed(signal[1:]))
        self.assertNotEqual(spectrum, exact_bispectrum(reflected))


class PhaseControlsTests(unittest.TestCase):
    def test_homometric_boundary_alias_hides_sum_positivity(self):
        a = tuple(int(x in {0, 1, 4, 6}) for x in range(12))
        b = tuple(int(x in {0, 1, 3, 7}) for x in range(12))
        self.assertEqual(cyclic_correlation(a), cyclic_correlation(b))
        self.assertEqual(exact_power(a), exact_power(b))
        self.assertEqual((cyclic_convolution(a)[3], cyclic_convolution(b)[3]), (0, 2))
        self.assertEqual((cyclic_convolution(a)[5], cyclic_convolution(b)[5]), (2, 0))
        self.assertNotEqual(cyclic_triple(a), cyclic_triple(b))
        self.assertNotEqual(exact_bispectrum(a), exact_bispectrum(b))

    def test_support_zero_alias_survives_every_triple(self):
        f, g = (28, 21, 7, 0, 7, 21), (16, 3, 1, 12, 25, 27)
        self.assertEqual(sum(f), sum(g))
        self.assertEqual(cyclic_correlation(f), cyclic_correlation(g))
        self.assertEqual(cyclic_triple(f), cyclic_triple(g))
        self.assertEqual(exact_bispectrum(f), exact_bispectrum(g))
        self.assertNotIn(g, [shift(f, s) for s in range(6)])
        support = tuple(h for h, value in enumerate(exact_fourier(f)) if any(value))
        self.assertEqual(support, (0, 1, 5))
        self.assertEqual(support_relation_rank(support, 6), 2)

    def test_full_support_finite_exhaustive_calibration(self):
        classes = {}
        included = 0
        for signal in product(range(2), repeat=5):
            if not all(any(value) for value in exact_fourier(signal)):
                continue
            included += 1
            key = cyclic_triple(signal)
            if key in classes:
                self.assertIn(signal, [shift(classes[key], s) for s in range(5)])
            else:
                classes[key] = signal
        self.assertEqual(included, 30)

    def test_full_relation_rank_can_hide_extra_finite_torsion(self):
        q = 21
        support = (0, 1, 2, 4, 8, 11, 16)
        exponents_mod_63 = {0: 0, 1: 1, 2: 2, 4: 4, 8: 8, 11: 32, 16: 16}
        triangles = {
            (h, k, (h + k) % q)
            for h in support for k in support
            if h and k and (h + k) % q in support
        }
        self.assertEqual(triangles, {
            (1, 1, 2), (2, 2, 4), (4, 4, 8),
            (8, 8, 16), (16, 16, 11), (11, 11, 1),
        })
        self.assertEqual(support_relation_rank(support, q), len(support))
        # Integer exponents encode exact roots of unity. Every observed
        # bispectrum phase relation is satisfied modulo 63.
        for h in support:
            for k in support:
                s = (h + k) % q
                if s in support:
                    self.assertEqual(
                        (exponents_mod_63[h] + exponents_mod_63[k]
                         - exponents_mod_63[s]) % 63, 0
                    )
        # A translation on Z/21 has frequency-one exponent divisible by
        # three when represented among the 63rd roots of unity.
        self.assertTrue(all((1 - 3*s) % 63 != 0 for s in range(q)))
        self.assertNotEqual((q * exponents_mod_63[1]) % 63, 0)

    def test_near_haar_scaling_exact_at_two_scales(self):
        u, v = (14, -7, -7), (2, 11, -13)
        for epsilon in (F(1, 100), F(1, 1000)):
            p = tuple(F(1, 3) + epsilon * a for a in u)
            q = tuple(F(1, 3) + epsilon * a for a in v)
            self.assertEqual(sum(p), 1)
            self.assertEqual(sum(q), 1)
            self.assertGreater(min(p + q), 0)
            self.assertTrue(all(any(a) for a in exact_fourier(p)))
            self.assertTrue(all(any(a) for a in exact_fourier(q)))
            self.assertEqual(cyclic_correlation(p), cyclic_correlation(q))
            self.assertEqual(exact_power(p), exact_power(q))
            distance = min(
                sum(abs(a - b) for a, b in zip(p, shift(q, s)))
                for s in range(3)
            )
            self.assertEqual(distance, 18 * epsilon)
            cp, cq = cyclic_triple(p), cyclic_triple(q)
            difference = max(abs(cp[s][t] - cq[s][t]) for s in range(3) for t in range(3))
            self.assertEqual(difference, 3078 * epsilon ** 3)

    def test_phase_report_has_expected_scopes_and_witnesses(self):
        report = control_report()
        self.assertEqual(report["homometric"]["sum_at_3"], [0, 2])
        self.assertEqual(report["support_zero"]["translations"], [])
        self.assertEqual(report["near_haar"]["maximum_triple_difference_coefficient"], 3078)
        self.assertIn("no asymptotic", report["scope"])


if __name__ == "__main__":
    unittest.main()
