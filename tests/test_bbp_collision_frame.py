"""Authentic source oracles, finite clock enumeration and hostile frame controls."""
import cmath
import math
import unittest
from collections import Counter
from fractions import Fraction as Q

from observational_succ.bbp_collision_frame import (
    MAX_ECHO_CLOCK, MAX_PROBABILITY_INDEX, MAX_SHELL,
    PopulationFrameCertificate, echo_readout_error_pi_units,
    fejer_clock_pmf, fejer_population_certificate,
    gamma_clock_pmf, gamma_clock_tail, gamma_population_certificate,
    matched_echo_coefficients, matched_echo_record,
    recommended_fejer_width, recommended_gamma_scale,
    smallest_gram_eigenvalue_upper, source_phase_error_pi_units,
    source_spacing_certificate,
)
from observational_succ.bbp_echo_delay_transport import division_by_characteristic, exact_window


def four_poles(n):
    return Q(4, 8 * n - 7) - Q(2, 8 * n - 4) - Q(1, 8 * n - 3) - Q(1, 8 * n - 2)


def original_states(last):
    states = [Q(0)]
    for n in range(1, last + 1):
        states.append(16 * states[-1] + four_poles(n))
    return states


def phase(turns):
    # Never cast a giant unwrapped source state directly to float.
    return cmath.exp(2j * math.pi * float(turns % 1))


def finite_readout_energy(nodes, coefficients, width, offset=0):
    count = len(nodes)
    return sum(float(fejer_clock_pmf(width, k, offset)) *
               abs(sum(c * phase(k * g) for c, g in zip(coefficients, nodes)) / count) ** 2
               for k in range(offset + 1, offset + 2 * width))


class AuthenticEchoTests(unittest.TestCase):
    def test_fixed_target_echo_against_independent_four_pole_replay(self):
        states = original_states(74)
        for n in (0, 1, 7, 23, 73):
            for h, k in ((1, 0), (-3, 17), (7, -101), (1, 10 ** 6), (0, 13)):
                record = matched_echo_record(n, h, k)
                self.assertEqual(record.state, states[n])
                self.assertEqual(record.next_state, states[n + 1])
                self.assertEqual(record.source_node, four_poles(n + 1))
                self.assertEqual(record.phase_turns, h * states[n] + k * four_poles(n + 1))
                self.assertEqual(record.phase_mod_one, record.phase_turns % 1)
                self.assertEqual(division_by_characteristic(record.coefficients), (h, (k,)))
                self.assertEqual(record.retains_nonzero_carrier, h != 0)

    def test_seed_erasure_mutation_does_not_retain_target(self):
        n, k, seed = 11, 71, Q(1, 7)
        states = original_states(n + 1)
        shifted = (states[n] + 16 ** n * seed, states[n + 1] + 16 ** (n + 1) * seed)
        for h in (0, 1, -5):
            a, b = matched_echo_coefficients(h, k)
            original = a * states[n] + b * states[n + 1]
            other = a * shifted[0] + b * shifted[1]
            self.assertEqual(other - original, h * 16 ** n * seed)
        self.assertEqual(division_by_characteristic((-16 * k, k))[0], 0)
        self.assertEqual(division_by_characteristic((1 - 16 * k, k))[0], 1)

    def test_source_sensitivity_scales_with_intensity(self):
        g, error = four_poles(12), Q(1, 10 ** 7)
        for k in (0, 1, -127, 10 ** 5):
            budget = source_phase_error_pi_units(k, error)
            self.assertEqual(budget, 2 * abs(k) * error)
            self.assertLessEqual(abs(phase(k * (g + error)) - phase(k * g)),
                                 math.pi * float(budget) + 1e-12)

    def test_raw_state_error_accounts_for_both_large_taps(self):
        h, k, first, second = 3, 123, Q(1, 1000), Q(1, 2000)
        a, b = matched_echo_coefficients(h, k)
        budget = echo_readout_error_pi_units(h, k, first, second)
        # Opposite error directions attain the triangle bound in this case.
        perturbation = a * (-first) + b * second
        self.assertEqual(budget, 2 * abs(perturbation))
        self.assertGreater(budget, 2 * abs(h) * first)


class SourceSpacingTests(unittest.TestCase):
    def test_sharp_spacing_bounds_all_pairs_and_new_holdouts(self):
        for b in (2, 3, 5, 11, 31, 101, 1009):
            certificate = source_spacing_certificate(b)
            expected = four_poles(2 * b - 1) - four_poles(2 * b)
            self.assertEqual(certificate.minimum_gap, expected)
            self.assertLessEqual(certificate.gap_lower, expected)
            self.assertLessEqual(expected, certificate.gap_upper)
            self.assertEqual(certificate.span, four_poles(b + 1) - four_poles(2 * b))
            self.assertLess(certificate.span, certificate.span_upper)
            self.assertLess(certificate.span_upper, Q(1, 2))
            if b <= 31:
                nodes = [four_poles(n + 1) for n in range(b, 2 * b)]
                gaps = [nodes[i] - nodes[i + 1] for i in range(b - 1)]
                self.assertEqual(min(gaps), expected)
                self.assertTrue(all(x > y for x, y in zip(gaps, gaps[1:])))
                for i in range(b):
                    for j in range(i + 1, b):
                        self.assertGreaterEqual(nodes[i] - nodes[j], (j - i) * certificate.gap_lower)

    def test_channel_deletion_breaks_authentic_cubic_gap_bound(self):
        b = 101
        certificate = source_spacing_certificate(b)
        # Deleting the last negative pole leaves an O(1/n) source.
        def deleted(n):
            return four_poles(n) + Q(1, 8 * n - 2)
        wrong_gap = deleted(2 * b - 1) - deleted(2 * b)
        self.assertGreater(wrong_gap, certificate.gap_upper)
        self.assertNotEqual(wrong_gap, certificate.minimum_gap)

    def test_recommended_scales_have_cubic_size_and_quarter_deviation(self):
        for b in (2, 3, 17, 257, 4099):
            source = source_spacing_certificate(b)
            scale = recommended_gamma_scale(b)
            width = recommended_fejer_width(b)
            self.assertGreaterEqual(scale * source.gap_lower, 1)
            self.assertLess((scale - 1) * source.gap_lower, 1)
            self.assertGreaterEqual(width * source.gap_lower, 2)
            self.assertLess((width - 1) * source.gap_lower, 2)
            for cert in (gamma_population_certificate(b, scale), fejer_population_certificate(b, width)):
                self.assertTrue(cert.stable)
                self.assertLessEqual(cert.deviation_upper, Q(1, 4))
                self.assertLessEqual(cert.condition_number_squared_upper, Q(5, 3))
                self.assertLessEqual(cert.mean_recovery_squared_gain, Q(4 * b, 3))


class ClockLawTests(unittest.TestCase):
    def test_gamma_pmf_matches_two_geometric_convolution(self):
        for scale in (Q(0), Q(1, 3), Q(1), Q(7, 2)):
            ratio = scale / (1 + scale)
            for k in range(15):
                convolution = sum(((1 - ratio) * ratio ** j *
                                   (1 - ratio) * ratio ** (k - j) for j in range(k + 1)), Q(0))
                self.assertEqual(gamma_clock_pmf(scale, k), convolution)

    def test_gamma_tail_exactly_completes_finite_mass(self):
        for scale in (Q(0), Q(1, 5), Q(1), Q(11)):
            for cutoff in (0, 1, 5, 20):
                mass = sum((gamma_clock_pmf(scale, k) for k in range(cutoff + 1)), Q(0))
                self.assertEqual(mass + gamma_clock_tail(scale, cutoff), 1)
        self.assertEqual(gamma_clock_pmf(0, 0), 1)
        self.assertEqual(gamma_clock_pmf(0, 1), 0)

    def test_fejer_clock_matches_explicit_independent_pair_enumeration(self):
        for width in (1, 2, 3, 7):
            for offset in (0, 13):
                counts = Counter(offset + 1 + u + v for u in range(width) for v in range(width))
                for k in range(offset - 1, offset + 2 * width + 2):
                    self.assertEqual(fejer_clock_pmf(width, k, offset), Q(counts[k], width * width))
                mean = sum((Q(k * count, width * width) for k, count in counts.items()), Q(0))
                variance = sum((Q(count, width * width) * (k - mean) ** 2 for k, count in counts.items()), Q(0))
                cert = fejer_population_certificate(2, width, offset)
                self.assertEqual(mean, cert.frequency_mean)
                self.assertEqual(variance, cert.frequency_variance)

    def test_gamma_character_against_truncated_probability_law(self):
        scale, cutoff = Q(1, 3), 48
        for delta in (Q(0), Q(1, 13), Q(-2, 7), four_poles(3) - four_poles(4)):
            finite = sum(float(gamma_clock_pmf(scale, k)) * phase(k * delta) for k in range(cutoff + 1))
            closed = (1 + float(scale) * (1 - phase(delta))) ** -2
            self.assertLessEqual(abs(finite - closed), float(gamma_clock_tail(scale, cutoff)) + 1e-14)


class PopulationFrameTests(unittest.TestCase):
    def test_fejer_energy_bounds_for_authentic_and_hostile_carriers(self):
        for b in (2, 3):
            width = recommended_fejer_width(b)
            certificate = fejer_population_certificate(b, width)
            nodes = [four_poles(n + 1) for n in range(b, 2 * b)]
            states = original_states(2 * b)
            vectors = ([1 + 0j] * b,
                       [phase(states[n]) for n in range(b, 2 * b)],
                       [(-1) ** n for n in range(b)],
                       [1 + 0j] + [0j] * (b - 1))
            lower, upper = certificate.eigenvalue_interval
            for coefficients in vectors:
                energy = finite_readout_energy(nodes, coefficients, width)
                norm2 = sum(abs(c) ** 2 for c in coefficients)
                self.assertGreaterEqual(energy + 1e-11, float(lower) * norm2 / b ** 2)
                self.assertLessEqual(energy, float(upper) * norm2 / b ** 2 + 1e-11)

    def test_locked_carrier_has_small_energy_but_unit_target_mean(self):
        b = 3
        certificate = fejer_population_certificate(b, recommended_fejer_width(b))
        nodes = [four_poles(n + 1) for n in range(b, 2 * b)]
        locked = [1 + 0j] * b
        energy = finite_readout_energy(nodes, locked, certificate.scale)
        self.assertEqual(sum(locked) / b, 1)
        self.assertLessEqual(energy, float(certificate.unit_phase_energy_interval[1]) + 1e-11)
        self.assertLess(certificate.unit_phase_energy_interval[1], 1)
        # Same forcing, a DIFFERENT rational seed selected by a finite future
        # boundary.  This approximates the coherent counterseed; it is not U_0=0.
        window = exact_window(2 * b + 16)
        counterseed = -window.tails[0]
        self.assertNotEqual(counterseed, 0)
        shifted = [window.states[n] + 16 ** n * counterseed for n in range(b, 2 * b)]
        self.assertEqual(shifted, [-window.tails[n] for n in range(b, 2 * b)])
        coherent = [phase(value) for value in shifted]
        self.assertGreater((sum(coherent) / b).real, 0.999)
        coherent_energy = finite_readout_energy(nodes, coherent, certificate.scale)
        self.assertLessEqual(coherent_energy, float(certificate.unit_phase_energy_interval[1]) + 1e-11)

    def test_oriented_residual_recovers_escape_not_difference_of_energies(self):
        b = 3
        certificate = fejer_population_certificate(b, recommended_fejer_width(b))
        nodes = [four_poles(n + 1) for n in range(b, 2 * b)]
        states = original_states(2 * b)
        carrier = [phase(states[n]) for n in range(b, 2 * b)]
        residual = [z - 1 for z in carrier]
        residual_energy = finite_readout_energy(nodes, residual, certificate.scale)
        escape = sum(1 - z.real for z in carrier) / b
        low, high = certificate.oriented_escape_multipliers
        self.assertGreaterEqual(escape + 1e-11, float(low) * residual_energy)
        self.assertLessEqual(escape, float(high) * residual_energy + 1e-11)
        self.assertGreater(residual_energy, 0)
        # Global phase inversion preserves every raw |F|^2, but changes escape.
        inverted = [-z for z in carrier]
        self.assertAlmostEqual(finite_readout_energy(nodes, carrier, certificate.scale),
                               finite_readout_energy(nodes, inverted, certificate.scale))
        self.assertNotAlmostEqual(escape, sum(1 - z.real for z in inverted) / b)

    def test_gamma_gram_row_bound_from_independent_closed_form(self):
        for b in (2, 5, 13):
            scale = recommended_gamma_scale(b)
            certificate = gamma_population_certificate(b, scale)
            nodes = [four_poles(n + 1) for n in range(b, 2 * b)]
            for n, g in enumerate(nodes):
                row = sum(abs((1 + scale * (1 - phase(other - g))) ** -2)
                          for m, other in enumerate(nodes) if m != n)
                self.assertLessEqual(row, float(certificate.deviation_upper) + 1e-11)

    def test_frequency_translation_changes_orientation_not_conditioning(self):
        nodes = [four_poles(3), four_poles(4)]
        width = 3
        values = []
        for offset in (0, 10 ** 6):
            gram12 = sum(float(fejer_clock_pmf(width, k, offset)) * phase(k * (nodes[1] - nodes[0]))
                         for k in range(offset + 1, offset + 2 * width))
            values.append(gram12)
            cert = fejer_population_certificate(2, width, offset)
            actual_smallest = 1 - abs(gram12)
            self.assertLessEqual(actual_smallest,
                                 float(smallest_gram_eigenvalue_upper(2, cert.frequency_variance)) + 1e-12)
        self.assertAlmostEqual(abs(values[0]), abs(values[1]))
        self.assertGreater(abs(values[0] - values[1]), 1e-3)

    def test_subcubic_clock_spread_has_unresolved_adjacent_columns(self):
        previous = Q(1)
        for b in (8, 16, 32, 64, 128):
            cert = gamma_population_certificate(b, b * b)
            upper = smallest_gram_eigenvalue_upper(b, cert.frequency_variance)
            self.assertLess(upper, previous)
            self.assertLess(upper, Q(1, b * b))
            self.assertFalse(cert.stable)
            previous = upper
        self.assertEqual(smallest_gram_eigenvalue_upper(3, 0), 0)

    def test_unresolved_certificates_do_not_offer_inverse_gains(self):
        for cert in (gamma_population_certificate(7, 1), fejer_population_certificate(7, 1)):
            self.assertFalse(cert.stable)
            self.assertEqual(cert.eigenvalue_interval[0], 0)
            for name in ("condition_number_squared_upper", "coefficient_recovery_squared_gain",
                         "mean_recovery_squared_gain", "oriented_escape_multipliers"):
                with self.assertRaisesRegex(ValueError, "does not certify"):
                    getattr(cert, name)


class ExactDomainTests(unittest.TestCase):
    def test_source_clock_and_echo_integer_domains(self):
        for b in (True, 1, 2.0, Q(2), MAX_SHELL + 1):
            with self.assertRaises(ValueError):
                source_spacing_certificate(b)
        for n in (True, -1, 1.0, MAX_ECHO_CLOCK + 1):
            with self.assertRaises(ValueError):
                matched_echo_record(n, 1, 3)
        for h, k in ((True, 1), (1, False), (Q(1), 1), (1, 1.0)):
            with self.assertRaises(ValueError):
                matched_echo_coefficients(h, k)

    def test_probability_and_population_law_domains(self):
        for bad in (True, 0.5, -1, float("nan"), "2"):
            with self.assertRaises(ValueError):
                gamma_clock_pmf(bad, 1)
            with self.assertRaises(ValueError):
                gamma_population_certificate(2, bad)
        with self.assertRaises(ValueError):
            gamma_population_certificate(2, 0)
        for bad in (True, 0, -1, Q(2), 2.0):
            with self.assertRaises(ValueError):
                fejer_population_certificate(2, bad)
        for bad in (True, -1, 1.0, MAX_PROBABILITY_INDEX + 1):
            with self.assertRaises(ValueError):
                gamma_clock_pmf(1, bad)
            with self.assertRaises(ValueError):
                gamma_clock_tail(1, bad)
        for bad in (True, -1, 0.0):
            with self.assertRaises(ValueError):
                fejer_clock_pmf(2, 1, bad)
        with self.assertRaises(ValueError):
            PopulationFrameCertificate(2, "unregistered", 1)

    def test_sensitivity_and_variance_require_nonnegative_exact_inputs(self):
        for bad in (True, -1, 0.1, float("nan")):
            with self.assertRaises(ValueError):
                source_phase_error_pi_units(1, bad)
            with self.assertRaises(ValueError):
                smallest_gram_eigenvalue_upper(2, bad)
            with self.assertRaises(ValueError):
                echo_readout_error_pi_units(1, 3, 0, bad)


if __name__ == "__main__":
    unittest.main()
