"""Exact calibration and hostile controls for the two-wire source instrument."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.twisted_pair_transport import (
    antiphase_certificate, apply_wire_orientation, bbp_synchronous_pair,
    circle_distance, gaussian, gaussian_conjugate, gaussian_norm_squared,
    gaussian_product, path_transport, quadratic_sum, quadrature_mismatch_energy,
    quarter_turn_phase, rational_phase, recover_signal, sharp_antiphase_cycle,
    signed_lag_correlation, transported_lag_correlation,
    transported_quadratic_sum, verify_bbp_path, wire_twists,
)


class ExactInputDomain(unittest.TestCase):
    def test_exact_gaussian_and_phase_arithmetic(self):
        z = gaussian(Q(3, 5), Q(4, 5))
        self.assertEqual(gaussian_product(z, gaussian_conjugate(z)), (Q(1), Q()))
        self.assertEqual(gaussian_norm_squared(z), 1)
        self.assertEqual(rational_phase(Q(-9, 4)), Q(3, 4))
        self.assertEqual(circle_distance(Q(-7, 4), Q(1, 2)), Q(1, 4))
        self.assertEqual(quarter_turn_phase(Q(-1, 4)), gaussian(0, -1))
        self.assertEqual(quarter_turn_phase(7), gaussian(1))

    def test_inexact_and_aliased_numeric_types_are_rejected(self):
        for bad in (True, False, 0.0, 0.5, "1/2", complex(1, 0)):
            with self.subTest(bad=bad):
                for function in (rational_phase, circle_distance,
                                 quarter_turn_phase, gaussian):
                    with self.assertRaises(ValueError):
                        function(bad)
                with self.assertRaises(ValueError):
                    gaussian_product((bad, 0), (1, 0))
        for bad in ((1,), (1, 2, 3), [1, 0], 1):
            with self.assertRaises(ValueError):
                quadratic_sum((bad,))
        with self.assertRaises(ValueError):
            quarter_turn_phase(Q(1, 3))

    def test_integer_and_wire_domain_guards(self):
        for bad in (True, 1.0, 0, 2):
            with self.assertRaises(ValueError):
                wire_twists((1, bad))
        for bad in (True, 0.0, -1):
            with self.assertRaises(ValueError):
                signed_lag_correlation(((1, 0),), bad)
            with self.assertRaises(ValueError):
                path_transport((1,), bad, 0)
            with self.assertRaises(ValueError):
                bbp_synchronous_pair(bad, 0)
        for bad in (True, 16.0, 1, -2, 3):
            with self.assertRaises(ValueError):
                antiphase_certificate(bad, Q(1, 2))
            with self.assertRaises(ValueError):
                sharp_antiphase_cycle(bad)
        for bad in (True, 1.0):
            with self.assertRaises(ValueError):
                antiphase_certificate(16, 0, bad)


class SignedWireTransport(unittest.TestCase):
    def test_exhaustive_short_wire_paths_and_signed_correlations(self):
        roots = tuple(quarter_turn_phase(Q(k, 4)) for k in range(4))
        checks = 0
        mutation_failures = 0
        for signal in product(roots, repeat=4):
            for signs in product((-1, 1), repeat=4):
                edges = wire_twists(signs)
                observed = apply_wire_orientation(signal, signs)
                self.assertEqual(recover_signal(observed, edges, signs[0]), signal)
                self.assertEqual(transported_quadratic_sum(observed, edges),
                                 quadratic_sum(signal))
                for lag in (1, 2, 3):
                    expected = signed_lag_correlation(signal, lag)
                    self.assertEqual(transported_lag_correlation(observed, edges, lag),
                                     expected)
                    mutation_failures += signed_lag_correlation(observed, lag) != expected
                    checks += 1
        self.assertEqual(checks, 12288)
        self.assertEqual(mutation_failures, 8064)

    def test_unknown_initial_wire_only_changes_global_sign(self):
        signal = ((Q(3, 5), Q(4, 5)), (1, -2), (0, Q(7, 3)))
        signs = (-1, 1, -1)
        observed = apply_wire_orientation(signal, signs)
        edges = wire_twists(signs)
        self.assertEqual(recover_signal(observed, edges),
                         tuple((-Q(a), -Q(b)) for a, b in signal))
        self.assertEqual(transported_quadratic_sum(observed, edges),
                         quadratic_sum(signal))
        self.assertEqual(wire_twists(signs), wire_twists(tuple(-x for x in signs)))
        for i in range(3):
            for j in range(3):
                self.assertEqual(path_transport(edges, i, j), signs[i] * signs[j])

    def test_discarded_and_corrupted_transport_fake_cancellation(self):
        signal = ((1, 0),) * 6
        observed = apply_wire_orientation(signal, (1, -1, 1, -1, 1, -1))
        edges = (-1,) * 5
        self.assertEqual(quadratic_sum(observed), 0)
        self.assertEqual(transported_quadratic_sum(observed, edges), 36)
        self.assertEqual(transported_lag_correlation(observed, edges, 1), (5, 0))
        self.assertEqual(signed_lag_correlation(observed, 1), (-5, 0))
        self.assertNotEqual(transported_quadratic_sum(observed, (1,) * 5), 36)
        with self.assertRaises(ValueError):
            transported_quadratic_sum(observed, ())
        with self.assertRaises(ValueError):
            transported_lag_correlation(observed, edges[:-1], 1)

    def test_quadratic_sum_matches_independent_all_pair_expansion(self):
        samples = ((Q(2, 3), Q(1, 5)), (Q(-3, 7), Q(2, 11)), (1, -4))
        signs = (-1, 1, 1)
        observed = apply_wire_orientation(samples, signs)
        edges = wire_twists(signs)
        real = imag = Q()
        for i, (a, b) in enumerate(observed):
            for j, (c, d) in enumerate(observed):
                p = signs[i] * signs[j]
                real += p * (a * c + b * d)
                imag += p * (b * c - a * d)
        self.assertEqual(imag, 0)
        self.assertEqual(real, transported_quadratic_sum(observed, edges))
        self.assertEqual(real, quadratic_sum(samples))

    def test_empty_singleton_and_lag_boundaries(self):
        self.assertEqual(wire_twists(()), ())
        self.assertEqual(recover_signal((), ()), ())
        self.assertEqual(transported_quadratic_sum((), ()), 0)
        self.assertEqual(transported_lag_correlation((), (), 0), (0, 0))
        self.assertEqual(path_transport((), 0, 0), 1)
        self.assertEqual(transported_lag_correlation(((2, 3),), (), 0), (13, 0))
        self.assertEqual(transported_lag_correlation(((2, 3),), (), 1), (0, 0))
        self.assertEqual(transported_lag_correlation(((2, 3),), (), 8), (0, 0))
        with self.assertRaises(ValueError):
            path_transport((), 0, 1)
        with self.assertRaises(ValueError):
            apply_wire_orientation(((1, 0),), ())
        with self.assertRaises(ValueError):
            recover_signal((), (1,))
        with self.assertRaises(ValueError):
            recover_signal(((1, 0),), (), True)


class AntiphaseSourceObstruction(unittest.TestCase):
    def test_sharp_even_radix_bound_and_equality_cycles(self):
        for base in (2, 4, 6, 16, 32):
            first, second = sharp_antiphase_cycle(base)
            self.assertEqual((base * first) % 1, second)
            self.assertEqual((base * second) % 1, first)
            for phase in (first, second):
                cert = antiphase_certificate(base, phase)
                self.assertTrue(cert.bound_verified)
                self.assertTrue(cert.attains_bound)
                self.assertEqual(cert.lower_bound, Q(1, 2 * (base + 1)))
            for denominator in (7, 19, 101):
                for numerator in range(denominator):
                    self.assertTrue(antiphase_certificate(
                        base, Q(numerator, denominator)).bound_verified)
        self.assertEqual(sharp_antiphase_cycle(16), (Q(9, 17), Q(8, 17)))

    def test_antiphase_collapses_and_odd_radix_control_survives(self):
        cert = antiphase_certificate(16, Q(1, 2))
        self.assertEqual(cert.first_error, 0)
        self.assertEqual(cert.next_error, Q(1, 2))
        self.assertEqual(cert.next_difference, 0)
        for base in (3, 5, 17):
            self.assertEqual((base * Q(1, 2)) % 1, Q(1, 2))

    def test_forcing_difference_pays_for_persistent_antiphase(self):
        cert = antiphase_certificate(16, Q(1, 2), forcing_difference=Q(1, 2))
        self.assertEqual(cert.first_error, 0)
        self.assertEqual(cert.next_error, 0)
        self.assertEqual(cert.forcing_error, Q(1, 2))
        self.assertEqual(cert.lower_bound, 0)
        for delta in (Q(1, 3), Q(4, 7), Q(9, 17)):
            for eta in (Q(-1, 13), Q(), Q(3, 10), Q(1, 2)):
                for h in (-7, 0, 1, 4):
                    cert = antiphase_certificate(16, delta, h, eta)
                    self.assertEqual(cert.next_difference, (16 * delta + eta) % 1)
                    self.assertTrue(cert.bound_verified)

    def test_authentic_bbp_path_and_literal_carries_independently(self):
        pair = bbp_synchronous_pair(24, Q(9, 17))
        expected = Q()
        expected_control = Q(9, 17)
        for n in range(1, 25):
            r = Q(4, 8 * n - 7) - Q(2, 8 * n - 4)
            r -= Q(1, 8 * n - 3) + Q(1, 8 * n - 2)
            self.assertEqual(pair.source[n - 1], r)
            lift = 16 * expected + r
            other_lift = 16 * expected_control + r
            self.assertEqual(pair.selected_carries[n - 1], lift // 1)
            self.assertEqual(pair.control_carries[n - 1], other_lift // 1)
            expected, expected_control = lift % 1, other_lift % 1
            self.assertEqual(pair.selected[n], expected)
            self.assertEqual(pair.control[n], expected_control)
            self.assertEqual(pair.differences[n], (Q(9, 17) * pow(16, n, 17)) % 1)
        self.assertTrue(verify_bbp_path(pair.selected))
        self.assertTrue(verify_bbp_path(pair.control, Q(9, 17)))
        self.assertFalse(verify_bbp_path(pair.control))

    def test_actual_source_halfturn_coalescence_and_mutation_rejection(self):
        pair = bbp_synchronous_pair(8, Q(1, 2))
        self.assertEqual(pair.differences, (Q(1, 2),) + (Q(),) * 8)
        self.assertEqual(pair.selected[1:], pair.control[1:])
        self.assertEqual(pair.control_carries[0] - pair.selected_carries[0], 8)
        mutated = list(pair.selected)
        mutated[4] = (mutated[4] + Q(1, 1000)) % 1
        self.assertFalse(verify_bbp_path(mutated))
        self.assertFalse(verify_bbp_path(()))
        self.assertFalse(verify_bbp_path((0, 1)))
        with self.assertRaises(ValueError):
            verify_bbp_path((0, 0.0))
        empty = bbp_synchronous_pair(0, 0)
        self.assertEqual(empty.selected, (Q(),))
        self.assertEqual(empty.selected_carries, ())


class QuadratureAgreement(unittest.TestCase):
    def test_two_positive_energies_recover_signed_mean(self):
        local = ((Q(3, 5), Q(4, 5)), (0, 1), (1, 0), (-1, 0))
        complement = ((0, 1), (Q(5, 13), Q(-12, 13)), (-1, 0), (0, -1))
        products = [gaussian_product(u, v) for u, v in zip(local, complement)]
        real = sum(value[0] for value in products) / 4
        imag = sum(value[1] for value in products) / 4
        e0 = quadrature_mismatch_energy(local, complement, 0)
        e1 = quadrature_mismatch_energy(local, complement, 1)
        self.assertEqual(1 - e0 / 2, real)
        self.assertEqual(1 - e1 / 2, imag)
        self.assertEqual(quadrature_mismatch_energy(local, complement, 2), 2 + 2 * real)
        self.assertEqual(quadrature_mismatch_energy(local, complement, 3), 2 + 2 * imag)

    def test_perfect_phase_agreement_means_maximal_coherence(self):
        local = ((Q(3, 5), Q(4, 5)), (0, 1), (-1, 0))
        complement = tuple(gaussian_conjugate(value) for value in local)
        self.assertEqual(quadrature_mismatch_energy(local, complement, 0), 0)
        self.assertEqual(quadratic_sum(tuple(gaussian_product(u, v)
                                            for u, v in zip(local, complement))), 9)
        self.assertEqual(quadrature_mismatch_energy(local, complement, 1), 2)

    def test_quadrature_domain_guards(self):
        for bad in (-1, 4, True, 1.0):
            with self.assertRaises(ValueError):
                quadrature_mismatch_energy(((1, 0),), ((1, 0),), bad)
        for first, second in (((), ()), (((1, 0),), ()), (((2, 0),), ((1, 0),))):
            with self.assertRaises(ValueError):
                quadrature_mismatch_energy(first, second, 0)


if __name__ == "__main__":
    unittest.main()
