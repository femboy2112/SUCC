"""Exact controls for the manuscript, including false stronger conjectures."""
import itertools
import unittest
from fractions import Fraction as Q

from observational_succ.principia_observatoris import (
    ContractError, LinearModel, matrix, multiply, transpose, identity, inverse,
    row_basis, right_inverse, subtract, difference_model, linear_separator,
    predictive_completion, quotient_defect, word_defect, bbp_forcing,
    bbp_hankel_ldl, bbp_rank_predictor, bbp_rank_error_bound,
)


class PrincipiaContractTests(unittest.TestCase):
    def test_inexact_and_malformed_inputs_rejected(self):
        for bad in ([[1.0]], [[True]], [[1], [1, 2]], [[]], []):
            with self.subTest(bad=bad), self.assertRaises(ContractError):
                matrix(bad)
        with self.assertRaises(ContractError):
            inverse([[1, 2], [2, 4]])
        with self.assertRaises(ContractError):
            right_inverse([[1, 0], [2, 0]])
        with self.assertRaises(ContractError):
            multiply([[1, 0]], [[1]])
        with self.assertRaises(ContractError):
            LinearModel("", (), ((1,),), ((1,),))
        with self.assertRaises(ContractError):
            LinearModel("bad", (((1,),),), ((1,), (2,)), ((1, 1),))

    def test_matrix_inverse_pivot_and_rank(self):
        a = matrix([[0, 2], [3, 4]])
        self.assertEqual(multiply(a, inverse(a)), identity(2))
        self.assertEqual(row_basis([[0, 0], [2, 4], [-3, -6]]), ((Q(1), Q(2)),))


class PrincipiaHorizonTests(unittest.TestCase):
    def test_sharp_two_realization_horizon(self):
        left = LinearModel("left", (((0, 0), (0, 1)),), ((1,), (1,)), ((Q(-1, 6), Q(1, 2)),))
        right = LinearModel("right", (((2, 0), (0, 3)),), ((1,), (1,)), ((Q(1, 2), Q(-1, 6)),))
        delta = difference_model(left, right)
        for k in range(3):
            self.assertEqual(delta.response((0,)*k), ((Q(0),),))
        self.assertEqual(delta.response((0,)*3), ((Q(1),),))
        self.assertEqual(linear_separator(delta)["word"], (0, 0, 0))

    def test_shortest_separator_on_switched_holdouts(self):
        # Unrelated integer actions, including cancellation and singular systems.
        for values in itertools.product((-1, 0, 1), repeat=4):
            a = (values[:2], values[2:])
            model = LinearModel("holdout", (a, ((0, 1), (-1, 0))), ((1,), (2,)), ((2, -1),))
            result = linear_separator(model)
            brute = [w for k in range(2) for w in itertools.product(range(2), repeat=k)
                     if any(x for row in model.response(w) for x in row)]
            if brute:
                self.assertEqual(result["status"], "DISTINGUISHED")
                self.assertEqual(len(result["word"]), len(brute[0]))
            else:
                self.assertEqual(result["status"], "ZERO_ON_ALL_WORDS")

    def test_initial_rank_and_zero_input(self):
        model = LinearModel("no input", (((1, 2), (3, 4)),), ((0,), (0,)), ((1, 1),))
        self.assertEqual(linear_separator(model)["reachable_rank"], 0)
        model = LinearModel("full bank", (((1, 2), (3, 4)),), identity(2), ((0, 1),))
        self.assertEqual(linear_separator(model)["word"], ())

    def test_signed_cancellation_does_not_erase_paths(self):
        a = ((0, 0, 0, 0), (1, 0, 0, 0), (1, 0, 0, 0), (0, 1, -1, 0))
        model = LinearModel("cancel", (a,), ((1,), (0,), (0,), (0,)), ((0, 0, 0, 1),))
        self.assertEqual(linear_separator(model)["status"], "ZERO_ON_ALL_WORDS")
        self.assertEqual(a[3][1]*a[1][0], 1)
        self.assertEqual(a[3][2]*a[2][0], -1)
        broken = [list(r) for r in a]
        broken[3][2] = 0
        altered = LinearModel("one path", (broken,), model.initial, model.readout)
        self.assertEqual(linear_separator(altered)["word"], (0, 0))

    def test_empty_alphabet_and_bad_word(self):
        model = LinearModel("static", (), ((1,),), ((0,),))
        self.assertEqual(linear_separator(model)["status"], "ZERO_ON_ALL_WORDS")
        for word in ((0,), (True,), (-1,)):
            with self.assertRaises(ContractError):
                model.response(word)


class PrincipiaDefectTests(unittest.TestCase):
    def test_unavoidable_hidden_response_and_exact_repair(self):
        p, a = ((1, 0),), ((0, 1), (0, 0))
        result = quotient_defect(p, a)
        self.assertFalse(result["descends"])
        self.assertEqual(result["defect"], matrix([[0, 1]]))
        self.assertEqual(result["predictor"], matrix([[0]]))
        # Indistinguishable states have opposite unit outputs; all predictors
        # at their common observation 0 have worst error at least 1.
        for guess in (Q(-3), Q(-1, 3), Q(0), Q(7, 5)):
            self.assertGreaterEqual(max(abs(1-guess), abs(-1-guess)), 1)
        completion = predictive_completion(p, (a,))
        self.assertEqual(completion["added_coordinates"], 1)
        self.assertEqual(completion["ranks"], (1, 2))
        self.assertEqual(completion["basis"], identity(2))

    def test_descended_and_oblique_observers(self):
        self.assertTrue(quotient_defect([[1, 0]], [[2, 0], [0, 3]])["descends"])
        result = quotient_defect([[1, 1]], [[1, 0], [0, 2]])
        self.assertEqual(result["predictor"], ((Q(3, 2),),))
        self.assertEqual(result["defect"], ((Q(-1, 2), Q(1, 2)),))
        hidden = result["hidden_projector"]
        self.assertEqual(multiply(hidden, hidden), hidden)
        self.assertEqual(transpose(hidden), hidden)

    def test_completion_is_minimal_invariant_span_on_holdout(self):
        a = matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
        b = matrix([[1, 0, 0], [0, -2, 0], [0, 0, 3]])
        result = predictive_completion([[1, 0, 0]], (a, b))
        self.assertEqual(result["ranks"], (1, 2, 3))
        q = result["basis"]
        for source, effective in zip((a, b), result["actions"]):
            self.assertEqual(multiply(q, source), multiply(effective, q))
        zero = predictive_completion([[0, 0, 0]], (a, b))
        self.assertEqual((zero["basis"], zero["added_coordinates"]), ((), 0))

    def test_word_transport_order_and_cancellation(self):
        p = ((1, 2),)
        source = (((1, 2), (0, 1)), ((0, 1), (-1, 0)))
        target = (((2,),), ((-1,),))
        for n in range(5):
            for word in itertools.product(range(2), repeat=n):
                result = word_defect(p, source, target, word)
                self.assertEqual(result["direct"], result["telescoped"])

    def test_descent_is_coordinate_invariant(self):
        p, a = matrix([[1, 0]]), matrix([[0, 1], [0, 0]])
        s, t = matrix([[1, 2], [0, 3]]), matrix([[7]])
        p2 = multiply(multiply(t, p), inverse(s))
        a2 = multiply(multiply(s, a), inverse(s))
        self.assertEqual(quotient_defect(p, a)["descends"], quotient_defect(p2, a2)["descends"])
        # Norm values are not compared without transporting the Hilbert metrics.


class PrincipiaArithmeticTests(unittest.TestCase):
    def test_original_forcing_identity_and_positive_hankel(self):
        for n in (1, 2, 17, 41):
            alternate = Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(bbp_forcing(n), alternate)
            for size in range(1, 6):
                result = bbp_hankel_ldl(n, size)
                d = matrix([[result["diagonal"][i] if i == j else 0
                             for j in range(size)] for i in range(size)])
                self.assertEqual(multiply(multiply(result["lower"], d), transpose(result["lower"])), result["matrix"])

    def test_sharp_forcing_discrimination_and_fitted_mutant(self):
        for start in (1, 3, 29):
            for dimension in range(1, 5):
                fitted = bbp_rank_predictor(start, dimension)
                model = fitted["model"]
                for k in range(2*dimension):
                    self.assertEqual(model.response((0,)*k)[0][0], bbp_forcing(start+k))
                self.assertGreater(fitted["next_error"], 0)
                self.assertGreater(bbp_rank_error_bound(start, dimension), 0)
                self.assertLessEqual(bbp_rank_error_bound(start, dimension), fitted["next_error"])
                self.assertNotEqual(model.response((0,)*(2*dimension))[0][0], bbp_forcing(start+2*dimension))

    def test_reject_invalid_bbp_index(self):
        for n in (0, -1, True, 1.0):
            with self.assertRaises(ContractError):
                bbp_forcing(n)
            with self.assertRaises(ContractError):
                bbp_hankel_ldl(n, 1)
            with self.assertRaises(ContractError):
                bbp_rank_predictor(1, n)


if __name__ == "__main__":
    unittest.main()
