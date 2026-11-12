"""Exact positive, negative, order, phase, closure and conditioning controls."""
from fractions import Fraction as F
from itertools import product
import unittest

from boundary_realization import (
    BoundaryCertificate, C, adjoint, basis_column, boundary_tables, identity,
    inverse, is_zero, matrix, multiply, pauli_pair, psd, subtract,
    word_return, word_state,
)


def all_words(alphabet, maximum):
    for length in range(maximum + 1):
        yield from product(alphabet, repeat=length)


class OrderedBoundaryTests(unittest.TestCase):
    def test_exact_number_guards(self):
        for bad in (0.1, True, 1j):
            with self.assertRaises(TypeError):
                C(bad)
        self.assertEqual(C(F(2, 3), F(1, 7)) / C(F(2, 3), F(1, 7)), C(1))

    def test_complex_gram_uses_adjoint(self):
        # V=[e0, i e0+e1], so the two off-diagonal entries must be conjugates.
        a = matrix([[C(0, 1), 0], [1, 0]])
        filters = {"a": a, "x": pauli_pair()["x"]}
        state, words = basis_column(2, 0), ((), ("a",))
        g, h, q = boundary_tables(filters, state, words)
        self.assertEqual(g, matrix([[1, C(0, 1)], [C(0, -1), 2]]))
        self.assertTrue(psd(g, strict=True))
        cert = BoundaryCertificate(words, g, h, q)
        self.assertTrue(cert.closed)
        for word in all_words(tuple(filters), 5):
            self.assertEqual(cert.return_value(word), word_return(filters, word, state))

    def test_exact_closed_pauli_reconstruction(self):
        filters, state, words = pauli_pair(), basis_column(2, 0), ((), ("x",))
        cert = BoundaryCertificate(words, *boundary_tables(filters, state, words))
        self.assertTrue(cert.closed)
        self.assertEqual(cert.g, identity(2))
        self.assertEqual(cert.m, filters)
        for word in all_words(tuple(filters), 7):
            self.assertEqual(cert.return_value(word), word_return(filters, word, state))

    def test_all_word_intensities_alias_but_phase_separates(self):
        state, plus, minus = basis_column(2, 0), pauli_pair(1), pauli_pair(-1)
        for word in all_words(("x", "y"), 7):
            a, b = word_return(plus, word, state), word_return(minus, word, state)
            self.assertEqual(a.abs2(), b.abs2())
            expected = a * (-1 if word.count("y") % 2 else 1)
            self.assertEqual(b, expected)
        for name in ("x", "y"):
            for k in range(9):
                self.assertEqual(word_return(plus, (name,) * k, state),
                                 word_return(minus, (name,) * k, state))
        self.assertEqual(word_return(plus, ("y", "x"), state), C(0, 1))
        self.assertEqual(word_return(minus, ("y", "x"), state), C(0, -1))

    def test_order_mutation_changes_signed_response(self):
        filters, state = pauli_pair(), basis_column(2, 0)
        self.assertEqual(word_return(filters, ("x", "y"), state), C(0, -1))
        self.assertEqual(word_return(filters, ("y", "x"), state), C(0, 1))
        self.assertNotEqual(word_return(filters, ("x", "y"), state),
                            word_return(filters, ("y", "x"), state))

    def test_transpose_mutation_falsely_reports_leakage(self):
        h = pauli_pair()["y"]
        transpose = tuple(tuple(row[j] for row in h) for j in range(2))
        correct = subtract(identity(2), multiply(adjoint(h), h))
        mutant = subtract(identity(2), multiply(transpose, h))
        self.assertTrue(is_zero(correct))
        self.assertEqual(mutant, matrix([[2, 0], [0, 2]]))

    def test_hidden_direct_summand_is_not_identified(self):
        small = pauli_pair()
        hidden = {}
        for name, hidden_value in (("x", 2), ("y", 3)):
            a = small[name]
            hidden[name] = matrix([[a[0][0], a[0][1], 0],
                                   [a[1][0], a[1][1], 0], [0, 0, hidden_value]])
        words = ((), ("x",))
        small_tables = boundary_tables(small, basis_column(2, 0), words)
        big_tables = boundary_tables(hidden, basis_column(3, 0), words)
        self.assertEqual(small_tables, big_tables)
        self.assertTrue(BoundaryCertificate(words, *big_tables).closed)
        for word in all_words(("x", "y"), 6):
            self.assertEqual(word_return(small, word, basis_column(2, 0)),
                             word_return(hidden, word, basis_column(3, 0)))

    def test_nonclosure_has_positive_residual(self):
        # Only e0 is observed; X exits to e1, and a second X returns.
        filters, state, words = {"x": pauli_pair()["x"]}, basis_column(2, 0), ((),)
        cert = BoundaryCertificate(words, *boundary_tables(filters, state, words))
        self.assertFalse(cert.closed)
        self.assertEqual(cert.residual["x"], matrix([[1]]))
        self.assertEqual(cert.return_value(("x", "x")), C(0))
        self.assertEqual(word_return(filters, ("x", "x"), state), C(1))

    def test_missing_generator_closure_is_not_enough(self):
        # Identity alone closes the line, but adding X exposes the missing sector.
        state, words = basis_column(2, 0), ((),)
        id_only = BoundaryCertificate(words, *boundary_tables({"i": identity(2)}, state, words))
        full = BoundaryCertificate(words, *boundary_tables(
            {"i": identity(2), "x": pauli_pair()["x"]}, state, words))
        self.assertTrue(id_only.closed)
        self.assertFalse(full.closed)

    def test_invalid_gram_and_shift_controls(self):
        with self.assertRaises(ValueError):
            BoundaryCertificate(((),), [[0]], {"x": [[0]]}, {"x": [[0]]})
        with self.assertRaises(ValueError):
            BoundaryCertificate(((),), [[1]], {"x": [[1]]}, {"x": [[0]]})
        with self.assertRaises(ValueError):
            BoundaryCertificate(((),), [[1]], {"x": [[0]]}, {"y": [[1]]})
        g, h, q = boundary_tables(pauli_pair(), basis_column(2, 0), ((), ("x",)))
        with self.assertRaises(ValueError):
            BoundaryCertificate(((), ("y",)), g, h, q)

    def test_psd_singular_zero_pivot_guard(self):
        self.assertTrue(psd(matrix([[0, 0], [0, 1]])))
        self.assertFalse(psd(matrix([[0, 1], [1, 1]])))
        self.assertFalse(psd(matrix([[1, C(0, 1)], [C(0, 1), 1]])))
        self.assertFalse(psd(matrix([[1, 0], [0, -1]])))

    def test_metric_conditioning_cannot_be_dropped(self):
        # V=[e0, eps e1], A e1=e2: raw R->0 but normalized defect is exactly 1.
        for denominator in (3, 7, 101):
            epsilon = F(1, denominator)
            filters = {
                "b": matrix([[0, 0, 0], [epsilon, 0, 0], [0, 0, 0]]),
                "a": matrix([[0, 0, 0], [0, 0, 0], [0, 1, 0]]),
            }
            words, state = ((), ("b",)), basis_column(3, 0)
            cert = BoundaryCertificate(words, *boundary_tables(filters, state, words))
            self.assertEqual(cert.g, matrix([[1, 0], [0, epsilon**2]]))
            self.assertEqual(cert.residual["a"], matrix([[0, 0], [0, epsilon**2]]))
            self.assertEqual(cert.defect_trace["a"], F(1))

    def test_approximate_closure_bound_on_rational_rotations(self):
        # Independent exact ambient word evaluation versus the scalar compression.
        # Both actual generators are rotations, hence ambient contractions.
        for u in (F(1, 5), F(1, 2), F(2, 3)):
            c, s = (1-u*u)/(1+u*u), 2*u/(1+u*u)
            filters = {"r": matrix([[c, -s], [s, c]]),
                       "l": matrix([[c, s], [-s, c]])}
            state, words = basis_column(2, 0), ((),)
            cert = BoundaryCertificate(words, *boundary_tables(filters, state, words))
            self.assertEqual(cert.defect_trace["r"], s*s)
            for word in all_words(("r", "l"), 6):
                actual = word_state(filters, word, state)
                predicted = matrix([[cert.return_value(word)], [0]])
                error = subtract(actual, predicted)
                error2 = multiply(adjoint(error), error)[0][0]
                self.assertFalse(error2.im)
                self.assertLessEqual(error2.re, cert.conditional_word_error_squared_bound(word))

    def test_inverse_nonorthogonal_complex_gram(self):
        g = matrix([[1, C(0, 1)], [C(0, -1), 2]])
        self.assertEqual(multiply(g, inverse(g)), identity(2))
        self.assertEqual(multiply(inverse(g), g), identity(2))


if __name__ == "__main__":
    unittest.main()
