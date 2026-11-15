"""Independent exact source and endpoint controls for causal inverse kernels."""

from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.bbp_causal_inverse import (
    CausalInverseKernel,
    MAX_INVERSE_ORDER,
    MAX_JET_ORDER,
    inverse_kernel,
    source_laplace,
)


def four_poles(a):
    return Q(4, 1) / a - Q(2, 1) / (a + 3) - Q(1, 1) / (a + 4) - Q(1, 1) / (a + 5)


def polynomial_product(left, right):
    return tuple(sum((left[j] * right[k-j]
                      for j in range(len(left)) if 0 <= k-j < len(right)), Q(0))
                 for k in range(len(left) + len(right) - 1))


def source_jet(last_order, first_weight=4):
    return tuple(sum((weight * (-rate)**k
                      for rate, weight in ((0, first_weight), (3, -2), (4, -1), (5, -1))))
                 for k in range(last_order + 1))


def convolution_jet(left, right):
    count = min(len(left), len(right))
    return (Q(0),) + tuple(
        sum((left[j] * right[n-1-j] for j in range(n)), Q(0))
        for n in range(1, count)
    )


def source_power_jet(order, last_order):
    base = source_jet(last_order)
    result = base
    for _ in range(order - 1):
        result = convolution_jet(result, base)
    return result


class CausalInverseTests(unittest.TestCase):
    def test_source_symbol_matches_literal_four_poles(self):
        for a in (Q(1, 7), Q(1), Q(9), Q(25), Q(51, 2)):
            self.assertEqual(source_laplace(a), four_poles(a))
        self.assertEqual(source_laplace(1), Q(47, 15))

    def test_first_inverse_has_exact_boundary_and_regular_parts(self):
        kernel = inverse_kernel()
        self.assertEqual(kernel.delta_polynomial,
                         (Q(-164, 3375), Q(59, 225), Q(1, 15)))
        self.assertEqual(kernel.remainder_numerator,
                         (Q(39360, 3375), Q(9944, 3375)))
        self.assertEqual(kernel.remainder_denominator, (Q(240), Q(121), Q(15)))
        self.assertEqual(kernel.remainder_jet(1),
                         (Q(9944, 50625), Q(-612824, 759375)))

    def test_zero_order_is_delta_and_has_no_regular_part(self):
        kernel = inverse_kernel(0)
        self.assertEqual(kernel.delta_polynomial, (Q(1),))
        self.assertEqual(kernel.remainder_numerator, (Q(0),))
        self.assertEqual(kernel.remainder_denominator, (Q(1),))
        self.assertEqual(kernel.remainder_jet(8), (Q(0),) * 9)
        self.assertEqual(kernel.laplace(0), 1)

    def test_symbol_reciprocal_at_independent_rational_arguments(self):
        for order, a in product(range(MAX_INVERSE_ORDER + 1),
                                (Q(1, 9), Q(2, 3), Q(1), Q(9), Q(73))):
            self.assertEqual(inverse_kernel(order).laplace(a) * four_poles(a)**order, 1)
        for order in range(1, MAX_INVERSE_ORDER + 1):
            self.assertEqual(inverse_kernel(order).laplace(0), 0)

    def test_polynomial_identity_uses_original_pole_product(self):
        for order in range(MAX_INVERSE_ORDER + 1):
            expected = (Q(1),)
            for _ in range(order):
                for offset in (0, 3, 4, 5):
                    expected = polynomial_product(expected, (Q(offset), Q(1)))
            kernel = inverse_kernel(order)
            expanded = list(polynomial_product(kernel.delta_polynomial,
                                               kernel.remainder_denominator))
            for i, value in enumerate(kernel.remainder_numerator):
                expanded[i] += value
            self.assertEqual(tuple(expanded), expected)

    def test_highest_delta_order_is_twice_inverse_depth(self):
        for order in range(MAX_INVERSE_ORDER + 1):
            kernel = inverse_kernel(order)
            self.assertEqual(len(kernel.delta_polynomial), 2 * order + 1)
            self.assertEqual(kernel.delta_polynomial[-1], Q(1, 15**order))

    def test_inverse_cascade_and_unit(self):
        for m, n in product(range(5), repeat=2):
            left, right = inverse_kernel(m), inverse_kernel(n)
            self.assertEqual(left.convolve(right), inverse_kernel(m + n))
            self.assertEqual(left.convolve(right), right.convolve(left))
        a, b, c = (inverse_kernel(k) for k in (1, 2, 3))
        self.assertEqual(a.convolve(b).convolve(c), a.convolve(b.convolve(c)))

    def test_actual_source_convolution_cancels_boundary_and_regular_jets(self):
        for order in range(1, 5):
            kernel = inverse_kernel(order)
            q_jet = source_power_jet(order, 2 * order + 18)
            regular_jet = kernel.remainder_jet(18)
            delta = kernel.delta_polynomial
            boundary = tuple(sum((delta[k] * q_jet[k-1-j]
                                  for k in range(j + 1, len(delta))), Q(0))
                             for j in range(2 * order))
            self.assertEqual(boundary, (Q(1),) + (Q(0),) * (2 * order - 1))
            convolution = convolution_jet(q_jet, regular_jet)
            for n in range(19):
                smooth = sum((coefficient * q_jet[n+k]
                              for k, coefficient in enumerate(delta)), Q(0))
                self.assertEqual(smooth + convolution[n], 0)

    def test_regular_remainder_obeys_its_rational_ode(self):
        for order in range(1, 5):
            kernel = inverse_kernel(order)
            jet = kernel.remainder_jet(24)
            denominator = kernel.remainder_denominator
            for n in range(25 - len(denominator)):
                self.assertEqual(sum((coefficient * jet[n+j]
                                      for j, coefficient in enumerate(denominator)), Q(0)), 0)

    def test_delta_action_retains_distributional_derivative_signs(self):
        kernel = inverse_kernel()
        endpoint = (Q(2), Q(3), Q(5))
        expected = Q(-164, 3375) * 2 - Q(59, 225) * 3 + Q(1, 15) * 5
        self.assertEqual(kernel.singular_pairing(endpoint), expected)
        wrong = sum((a*b for a, b in zip(kernel.delta_polynomial, endpoint)), Q(0))
        self.assertNotEqual(expected, wrong)

    def test_omitted_boundary_or_remainder_fails(self):
        kernel = inverse_kernel()
        q_jet = source_jet(5)
        # The boundary delta comes from delta'' convolved with H*q.
        self.assertEqual(kernel.delta_polynomial[2] * q_jet[1], 1)
        self.assertNotEqual(Q(0) * q_jet[1], 1)
        # Dropping the smooth remainder leaves a nonzero second endpoint jet.
        residue = sum((coefficient * q_jet[2+k]
                       for k, coefficient in enumerate(kernel.delta_polynomial)), Q(0))
        self.assertNotEqual(residue, 0)
        # A changed first source pole creates an unwanted delta' at the boundary.
        mutant = source_jet(2, first_weight=5)
        self.assertNotEqual(kernel.delta_polynomial[2] * mutant[0], 0)

    def test_source_passport_rejects_tampered_decomposition(self):
        kernel = inverse_kernel()
        with self.assertRaises(ValueError):
            replace(kernel, delta_polynomial=(Q(-164, 3375), Q(-59, 225), Q(1, 15)))
        with self.assertRaises(ValueError):
            replace(kernel, remainder_numerator=(Q(0),))
        with self.assertRaises(ValueError):
            replace(kernel, remainder_denominator=(Q(240), Q(122), Q(15)))

    def test_exact_inputs_and_budgets(self):
        for bad in (True, 1.0, Q(1), -1, MAX_INVERSE_ORDER + 1):
            with self.assertRaises(ValueError):
                inverse_kernel(bad)
        for bad in (True, 0.5, "1"):
            with self.assertRaises(TypeError):
                source_laplace(bad)
            with self.assertRaises(TypeError):
                inverse_kernel().laplace(bad)
        for bad in (0, -1):
            with self.assertRaises(ValueError):
                source_laplace(bad)
        with self.assertRaises(ValueError):
            inverse_kernel().laplace(-1)
        for bad in (True, 1.0, -1, MAX_JET_ORDER + 1):
            with self.assertRaises(ValueError):
                inverse_kernel().remainder_jet(bad)
        with self.assertRaises(ValueError):
            inverse_kernel(MAX_INVERSE_ORDER).convolve(inverse_kernel(1))
        with self.assertRaises(TypeError):
            inverse_kernel().convolve(1)
        with self.assertRaises(ValueError):
            inverse_kernel().singular_pairing((Q(1),))
        with self.assertRaises(TypeError):
            inverse_kernel().singular_pairing((Q(1), 0.5, Q(2)))

    def test_dataclass_field_types_are_guarded(self):
        kernel = inverse_kernel()
        with self.assertRaises(TypeError):
            replace(kernel, delta_polynomial=(Q(-164, 3375), 0.5, Q(1, 15)))
        with self.assertRaises(TypeError):
            replace(kernel, delta_polynomial=[])
        with self.assertRaises(ValueError):
            CausalInverseKernel(0, (Q(1),), (Q(1),), (Q(1),))


if __name__ == "__main__":
    unittest.main()
