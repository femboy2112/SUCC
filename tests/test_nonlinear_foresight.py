"""Exact finite controls for a declared source; no infinite inference by scan."""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.nonlinear_foresight import (
    bounded_pair_error_bound,
    future_error_bound,
    in_bounded_image,
    in_source_image,
    in_three_report_image,
    jump_descriptor,
    jump_report,
    jump_report_counted,
    monomial_in_polynomial_stage,
    satisfies_report_relation,
    source_reports,
    validate_reports,
)


def sequential_report(x, y, n):
    """Independent trajectory oracle: walk the source one step at a time."""
    for _ in range(n):
        x *= y
    return x


class NonlinearForesightTests(unittest.TestCase):
    def test_initial_report_and_singular_zero(self):
        self.assertEqual(jump_report(Q(2, 3), Q(-7, 5), 0), Q(2, 3))
        for n in (0, 1, 2, 17, 10**9):
            receipt = jump_report_counted(0, 0, n)
            self.assertEqual(receipt.value, 0)
            self.assertEqual((receipt.multiplications, receipt.divisions), (0, 0))
        self.assertEqual(jump_descriptor(0, 0), (0, 0))

    def test_off_image_reports_are_rejected_even_at_zero_horizon(self):
        for b in (Q(-1), Q(1), Q(1, 7)):
            self.assertFalse(in_source_image(0, b))
            self.assertFalse(in_bounded_image(0, b, 100))
            with self.assertRaises(ValueError):
                validate_reports(0, b)
            with self.assertRaises(ValueError):
                jump_descriptor(0, b)
            for n in (0, 1, 7):
                with self.assertRaises(ValueError):
                    jump_report(0, b, n)

    def test_exact_input_types_fail_closed(self):
        for invalid in (0.5, True, "1/2", complex(1)):
            for call in (
                lambda: source_reports(invalid, 1),
                lambda: validate_reports(1, invalid),
                lambda: in_source_image(invalid, 1),
                lambda: jump_report(1, invalid, 2),
                lambda: future_error_bound(2, invalid, 0, 0),
                lambda: future_error_bound(2, 1, invalid, 0),
            ):
                with self.assertRaises(TypeError):
                    call()
        self.assertEqual(validate_reports(2, 3), (Q(2), Q(3)))

    def test_horizon_and_monomial_indices_fail_closed(self):
        for invalid in (-1, True, Q(2), 2.0, "2"):
            for call in (
                lambda: jump_report(1, 2, invalid),
                lambda: future_error_bound(invalid, 1, 0, 0),
                lambda: bounded_pair_error_bound(1, 1, 1, 1, invalid, 1),
                lambda: monomial_in_polynomial_stage(1, 1, invalid),
            ):
                with self.assertRaises(ValueError):
                    call()

    def test_jump_matches_direct_source_trajectory(self):
        xs = (Q(-2), Q(-1, 2), Q(0), Q(1, 3), Q(1), Q(2))
        ys = (Q(-3, 2), Q(-1), Q(0), Q(1, 2), Q(1), Q(2))
        for x, y, n in product(xs, ys, range(18)):
            a, b = source_reports(x, y)
            self.assertEqual(jump_report(a, b, n), sequential_report(x, y, n))

    def test_descriptor_descent_and_entry_into_singular_branch(self):
        for x, y in product((Q(-2), Q(0), Q(2, 3)), (Q(-1), Q(0), Q(5, 2))):
            self.assertEqual(jump_descriptor(*source_reports(x, y)),
                             source_reports(x * y, y))
        self.assertEqual(jump_descriptor(7, 0), (0, 0))
        self.assertEqual(jump_report(7, 0, 0), 7)
        self.assertEqual(jump_report(7, 0, 12), 0)

    def test_counted_binary_arithmetic_matches_declared_algorithm(self):
        for n in range(1, 129):
            receipt = jump_report_counted(Q(-2, 3), Q(5, 7), n)
            self.assertEqual(receipt.multiplications,
                             n.bit_length() - 1 + n.bit_count() + 1)
            self.assertLessEqual(receipt.multiplications, 2 * n.bit_length())
            self.assertEqual(receipt.divisions, 1)
            self.assertEqual(receipt.value, sequential_report(Q(-2, 3), Q(-15, 14), n))
        receipt = jump_report_counted(2, 3, 0)
        self.assertEqual((receipt.value, receipt.multiplications, receipt.divisions),
                         (Q(2), 0, 0))

    def test_polynomial_monomial_criterion_against_product_enumeration(self):
        for depth in range(7):
            for r in range(5):
                # Independently enumerate products of r generators x*y**j.
                realized_y_degrees = {sum(choices)
                                      for choices in product(range(depth + 1), repeat=r)}
                for s in range(4 * depth + 3):
                    self.assertEqual(monomial_in_polynomial_stage(r, s, depth),
                                     s in realized_y_degrees)

    def test_next_observable_is_absent_from_each_polynomial_stage(self):
        for depth in range(64):
            self.assertTrue(monomial_in_polynomial_stage(1, depth, depth))
            self.assertFalse(monomial_in_polynomial_stage(1, depth + 1, depth))
        self.assertTrue(monomial_in_polynomial_stage(0, 0, 0))
        self.assertFalse(monomial_in_polynomial_stage(0, 1, 100))

    def test_polynomial_relation_alone_admits_false_future(self):
        self.assertTrue(satisfies_report_relation(0, 0, 1))
        self.assertFalse(in_three_report_image(0, 0, 1))
        self.assertEqual(jump_report(0, 0, 2), 0)
        self.assertTrue(in_three_report_image(0, 0, 0))
        for x, y in product((Q(-3), Q(0), Q(5, 7)), (Q(-1, 2), Q(0), Q(3))):
            self.assertTrue(in_three_report_image(x, x * y, x * y * y))
        self.assertFalse(in_three_report_image(1, 2, 5))

    def test_unbounded_source_has_small_reports_and_unit_future(self):
        for n, k in product(range(2, 10), range(2, 20)):
            epsilon = Q(1, k)
            a, b = epsilon**n, epsilon ** (n - 1)
            self.assertEqual(source_reports(epsilon**n, 1 / epsilon), (a, b))
            self.assertEqual(jump_report(a, b, n), 1)
            self.assertLessEqual(abs(a), epsilon)
            self.assertLessEqual(abs(b), epsilon)
            self.assertEqual(jump_report(0, 0, n), 0)

    def test_source_bound_and_coordinate_errors_are_validated(self):
        self.assertTrue(in_bounded_image(0, 0, 0))
        self.assertTrue(in_bounded_image(-2, 3, Q(3, 2)))
        self.assertFalse(in_bounded_image(-2, 3, 1))
        with self.assertRaises(ValueError):
            bounded_pair_error_bound(1, 2, 1, 1, 3, 1)
        with self.assertRaises(ValueError):
            bounded_pair_error_bound(0, 1, 1, 1, 3, 2)
        for args in ((2, -1, 0, 0), (2, 1, -1, 0), (2, 1, 0, -1)):
            with self.assertRaises(ValueError):
                future_error_bound(*args)
        with self.assertRaises(ValueError):
            in_bounded_image(0, 0, -1)

    def test_bounded_noise_inequality_across_both_signs_and_origin(self):
        xs = (Q(-2), Q(-1, 2), Q(0), Q(1, 3), Q(2))
        ys = (Q(-2), Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1), Q(2))
        for bound in (Q(0), Q(1, 2), Q(1), Q(2)):
            states = [(x, y) for x, y in product(xs, ys) if abs(y) <= bound]
            for (x, y), (u, v), n in product(states, states, range(9)):
                a, b = source_reports(x, y)
                c, d = source_reports(u, v)
                actual = abs(sequential_report(x, y, n) - sequential_report(u, v, n))
                certified = bounded_pair_error_bound(a, b, c, d, n, bound)
                self.assertLessEqual(actual, certified)

    def test_initial_horizons_and_zero_source_bound(self):
        self.assertEqual(future_error_bound(0, 2, Q(1, 7), Q(2, 9)), Q(1, 7))
        self.assertEqual(future_error_bound(1, 2, Q(1, 7), Q(2, 9)), Q(2, 9))
        for n in range(2, 12):
            self.assertEqual(future_error_bound(n, 0, 1, 1), 0)

    def test_small_report_error_can_grow_at_increasing_horizons(self):
        for k in range(2, 33):
            epsilon = Q(1, k)
            self.assertTrue(in_bounded_image(1, 1 - epsilon, 1))
            actual = jump_report(1, 1, k) - jump_report(1, 1 - epsilon, k)
            self.assertGreaterEqual(actual, Q(1, 2))
            self.assertLessEqual(actual, bounded_pair_error_bound(1, 1, 1, 1 - epsilon, k, 1))

    def test_output_bit_growth_is_separate_from_field_operation_count(self):
        for n in (1, 2, 7, 32, 127, 256):
            receipt = jump_report_counted(1, 2, n)
            self.assertEqual(receipt.value, 2**n)
            self.assertEqual(receipt.value.numerator.bit_length(), n + 1)
            self.assertEqual(receipt.value.denominator, 1)
            if n >= 32:
                self.assertLess(receipt.multiplications, n)


if __name__ == "__main__":
    unittest.main(verbosity=2)
