"""Independent finite enumerations for selection/observable information."""
import itertools
import unittest
from fractions import Fraction as Q

from observational_succ.path_likelihood import (
    path_likelihood_certificate, inverse_phase_certificate,
    authentic_inverse_window, smooth_selector_obstruction,
    adaptive_coboundary_control,
)
from observational_succ.lambda_source_duality import original_history


class SignedInnovation(unittest.TestCase):
    def test_signed_terms_cancel_while_energies_remain(self):
        words = tuple(itertools.product((0, 1), repeat=2))
        p = dict.fromkeys(words, Q(1, 4))
        q = {(0, 0): Q(1)}
        f = dict(zip(words, map(Q, (0, 2, -1, -1))))
        cert = path_likelihood_certificate(p, q, f)
        self.assertEqual(tuple(row.signed_pairing for row in cert.innovations), (1, -1))
        self.assertEqual(cert.signed_difference, 0)
        self.assertEqual(cert.chi_square, 3)
        self.assertTrue(all(row.observable_increment_square > 0 for row in cert.innovations))
        reflected = path_likelihood_certificate(p, q, {w: -v for w, v in f.items()})
        self.assertEqual(tuple(r.signed_pairing for r in reflected.innovations), (-1, 1))
        self.assertEqual(tuple(r.observable_increment_square for r in cert.innovations),
                         tuple(r.observable_increment_square for r in reflected.innovations))

    def test_nonuniform_laws_and_fresh_ternary_paths(self):
        words = tuple(itertools.product(range(3), repeat=3))
        pweights = [i+1 for i in range(len(words))]
        qweights = [(i*7+11) % 19 for i in range(len(words))]
        p = {w: Q(a, sum(pweights)) for w, a in zip(words, pweights)}
        q = {w: Q(a, sum(qweights)) for w, a in zip(words, qweights)}
        f = {w: Q((i*i+5*i) % 23-11, i+1) for i, w in enumerate(words)}
        cert = path_likelihood_certificate(p, q, f)
        direct = sum(((q[w]-p[w])*f[w] for w in words), Q())
        self.assertEqual(cert.signed_difference, direct)
        self.assertEqual(sum((r.likelihood_increment_square for r in cert.innovations), Q()),
                         sum(((q[w]-p[w])**2/p[w] for w in words), Q()))

    def test_null_selection_and_constant_observation(self):
        p = {(0,): Q(2, 7), (1,): Q(5, 7)}
        cert = path_likelihood_certificate(p, p, {(0,): Q(3), (1,): Q(-8)})
        self.assertEqual(cert.chi_square, 0)
        self.assertEqual(cert.signed_difference, 0)
        cert = path_likelihood_certificate(p, {(1,): Q(1)}, dict.fromkeys(p, Q(9)))
        self.assertEqual(cert.observable_variance, 0)
        self.assertEqual(cert.signed_difference, 0)

    def test_zero_depth(self):
        cert = path_likelihood_certificate({(): Q(1)}, {(): Q(1)}, {(): Q(17)})
        self.assertEqual(cert.innovations, ())
        self.assertEqual(cert.selected_expectation, 17)

    def test_absolute_continuity_and_data_mutations_rejected(self):
        p = {(0,): Q(1)}
        for q, f in [({(1,): Q(1)}, {(0,): Q()}),
                     ({(0,): Q(2)}, {(0,): Q()}),
                     ({(0,): Q(1)}, {}),
                     ({(0,): Q(1)}, {(0,): 0.5})]:
            with self.assertRaises(ValueError):
                path_likelihood_certificate(p, q, f)
        with self.assertRaises(ValueError):
            path_likelihood_certificate({(0,): Q(1, 2), (0, 1): Q(1, 2)},
                                        {(0,): Q(1)}, {(0,): Q(), (0, 1): Q()})


class InverseResolution(unittest.TestCase):
    def test_projection_against_independent_cyclotomic_enumeration(self):
        for depth in (1, 3, 6):
            size = 2**depth
            for h in (-17, -8, -3, 0, 1, 2, 4, 8, 16, 32):
                for selected in {0, 1, size//2, size-1}:
                    cert = inverse_phase_certificate(2, depth, h, selected, Q(7, 15))
                    for row in cert['levels']:
                        level = row['level']; residue = selected % (2**level)
                        population = [j for j in range(size) if j % (2**level) == residue]
                        powers = [(h*j) % size for j in population]
                        if len(set(powers)) == 1:
                            expected = (Q(h)*Q(7, 15)/size + Q(powers[0], size)) % 1
                            self.assertEqual(row['conditional_phase'], expected)
                        else:
                            # Phi_(2^depth)(z)=z^(size/2)+1; evaluate the
                            # enumerated numerator in that exact quotient.
                            remainder = [0]*(size//2)
                            for exponent in powers:
                                remainder[exponent % (size//2)] += 1 if exponent < size//2 else -1
                            self.assertEqual(remainder, [0]*(size//2))
                            self.assertIsNone(row['conditional_phase'])

    def test_binary_and_hex_revelation_have_declared_order(self):
        for h, binary_level in ((1, 12), (2, 11), (4, 10), (8, 9), (16, 8), (256, 4)):
            binary = inverse_phase_certificate(2, 12, h, 1907)
            hexadecimal = inverse_phase_certificate(16, 3, h, 1907)
            self.assertEqual(binary['first_observable_level'], binary_level)
            self.assertEqual(hexadecimal['first_observable_level'], (binary_level+3)//4)
            self.assertEqual(sum(row['signed_pairing_amplitude'] for row in binary['levels']), 1)
            self.assertEqual(binary['selected_phase'], hexadecimal['selected_phase'])

    def test_constant_fiber_modes_have_no_new_observable_information(self):
        for h in (0, 256, -512):
            cert = inverse_phase_certificate(16, 2, h, 73, Q(4, 7))
            self.assertIsNone(cert['first_observable_level'])
            self.assertEqual(cert['initial_phase_amplitude'], 1)
            self.assertTrue(all(row['conditional_phase'] is not None for row in cert['levels']))
            self.assertEqual(sum(row['signed_pairing_amplitude'] for row in cert['levels']), 0)

    def test_large_fiber_is_not_enumerated(self):
        cert = inverse_phase_certificate(16, 128, 8, 17, Q(1, 3))
        self.assertEqual(len(cert['levels']), 129)
        self.assertEqual(cert['fiber_size'], 2**512)
        self.assertEqual(cert['selected_chi_square'], 2**512-1)
        self.assertEqual(cert['selected_path_reference_probability'], Q(1, 2**512))

    def test_source_windows_use_original_four_poles_and_zero_seed(self):
        states = original_history(64)
        for start, steps in ((0, 1), (1, 3), (7, 5), (31, 9)):
            forcing = Q()
            for n in range(start+1, start+steps+1):
                forcing = 16*forcing + Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            for h in (1, 2, 8, 16, 257):
                cert = authentic_inverse_window(states, start, steps, h, binary=True)
                self.assertEqual(cert['macro_forcing'], forcing)
                u = Q() if start == 0 else states[start-1]
                self.assertEqual(cert['selected_phase'], (h*u) % 1)
                self.assertEqual(cert['source_selected_state'].denominator % 2, 1)
        mutant = (states[0]+1,)+states[1:]
        with self.assertRaises(ValueError):
            authentic_inverse_window(mutant, 1, 3, 1)

    def test_bad_resolution_inputs_rejected(self):
        for args in [(1, 2, 1, 0), (2, -1, 1, 0), (2, 2, 1.0, 0), (2, 2, 1, 4)]:
            with self.assertRaises(ValueError):
                inverse_phase_certificate(*args)


class SmoothAndAdaptiveControls(unittest.TestCase):
    def test_all_labels_are_near_zero_with_quantified_budget(self):
        cert = smooth_selector_obstruction(1009, 3, Q(2))
        self.assertEqual(cert['selected_digits'], tuple(range(16)))
        self.assertGreater(cert['finite_error_lower'], Q(99, 100))
        for j, tail in enumerate(cert['tails']):
            predecessor = (tail+j)/16
            self.assertEqual(predecessor.denominator % 2, 1)
            self.assertLessEqual(tail, Q(16, cert['conductor']))

    def test_continuous_exception_and_invalid_regularizer_rejected(self):
        for h, bound in ((0, Q()), (16, Q(1)), (1, Q(-1)), (1, 0.5)):
            with self.assertRaises(ValueError):
                smooth_selector_obstruction(7, h, bound)

    def test_local_phase_losses_fail_to_multiply_by_path_enumeration(self):
        p = Q(3, 4)
        for n in range(1, 9):
            actual = Q()
            for word in itertools.product((1, -1), repeat=n):
                probability, product_phase, previous = Q(1), 1, 1
                for sign in word:
                    probability *= p if sign == 1 else 1-p
                    product_phase *= previous*sign
                    previous = sign
                actual += probability*product_phase
            cert = adaptive_coboundary_control(n, p)
            self.assertEqual(actual, Q(1, 2))
            self.assertEqual(cert['actual_product_expectation'], actual)
            self.assertEqual(cert['local_conditional_modulus'], Q(1, 2))
            self.assertFalse(cert['universal_local_modulus_product_bound_valid'])
            self.assertEqual(cert['instance_violates_modulus_product_bound'], n > 1)
            if n > 1:
                self.assertGreater(abs(actual), cert['false_product_of_local_moduli'])

    def test_twisted_unit_eigenvector_and_null_bias(self):
        for p in (Q(1, 3), Q(1, 2), Q(7, 8)):
            cert = adaptive_coboundary_control(19, p)
            matrix = cert['twisted_kernel']; vector = cert['unit_eigenvector']
            self.assertEqual(tuple(sum((a*b for a, b in zip(row, vector)), Q()) for row in matrix), vector)
            self.assertTrue(all(v > 0 for row in cert['reference_kernel'] for v in row))
            self.assertEqual(cert['actual_product_expectation'], 2*p-1)
            self.assertEqual(cert['instance_violates_modulus_product_bound'], p != Q(1, 2))


if __name__ == '__main__':
    unittest.main()
