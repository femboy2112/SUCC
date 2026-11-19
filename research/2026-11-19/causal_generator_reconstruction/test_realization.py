"""Exact controls for conditional response-table reconstruction."""
from fractions import Fraction as F
from itertools import product
import unittest

from realization import (
    Realization, add_models, affine_row_lift, delayed_spike_model, enumerate_path_response,
    fibonacci_model, inverse, matrix, missing_from_one_history, multiply,
    probe_bank, reconstruct_from_table, verify_linear_function_closure,
)


class RealizationTests(unittest.TestCase):
    def setUp(self):
        self.fib = fibonacci_model()
        self.p = self.q = ((), ("a",))
        self.bank = probe_bank(self.p, self.q, ("a",))
        self.table = {w: self.fib.response(w) for w in self.bank}

    def test_fibonacci_four_responses_and_fresh_lengths(self):
        self.assertEqual([len(w) for w in self.bank], [0, 1, 2, 3])
        self.assertEqual([self.table[w] for w in self.bank], [1, 1, 2, 3])
        got = reconstruct_from_table(self.table, self.p, self.q, ("a",),
                                     assumed_global_rank_at_most=2)
        self.assertEqual(got.model.transitions["a"], matrix(((0, 1), (1, 1))))
        self.assertEqual(got.model.alpha, (1, 0))
        self.assertEqual(got.model.beta, (1, 1))
        for n in (4, 5, 10, 17, 29, 47, 83):
            self.assertEqual(got.model.response(("a",)*n), self.fib.response(("a",)*n))

    def test_table_does_not_certify_its_global_rank(self):
        got = reconstruct_from_table(self.table, self.p, self.q, ("a",))
        self.assertEqual(got.claim, "FINITE_DATA_CANDIDATE_ONLY")
        self.assertIsNone(got.assumed_global_rank_at_most)
        for bad in (1, 3, True):
            with self.assertRaises(ValueError):
                reconstruct_from_table(self.table, self.p, self.q, ("a",),
                                       assumed_global_rank_at_most=bad)

    def test_noncommuting_word_reconstruction_and_path_oracle(self):
        model = Realization((1, 0), {
            "a": ((1, 1), (0, 1)), "b": ((1, 0), (1, 1))}, (0, 1))
        p, q = ((), ("a",)), ((), ("a",))
        bank = probe_bank(p, q, ("a", "b"))
        table = {w: model.response(w) for w in bank}
        got = reconstruct_from_table(table, p, q, ("a", "b"),
                                     assumed_global_rank_at_most=2)
        for n in range(7):
            for w in product(("a", "b"), repeat=n):
                self.assertEqual(got.model.response(w), model.response(w))
                if n <= 4:
                    self.assertEqual(got.model.response(w), enumerate_path_response(model, w))
        self.assertNotEqual(model.response(("a", "b", "a")),
                            model.response(("b", "a", "a")))

    def test_order_mutation_is_detected_outside_single_letter_powers(self):
        model = Realization((1, 0), {
            "a": ((1, 1), (0, 1)), "b": ((1, 0), (1, 1))}, (1, 0))
        self.assertEqual(model.response(("a",)*4), model.response(tuple(reversed(("a",)*4))))
        self.assertNotEqual(model.response(("a", "b")), model.response(("b", "a")))

    def test_missing_shift_probe_is_not_silently_filled(self):
        table = dict(self.table)
        del table[("a",)*3]
        with self.assertRaises(ValueError):
            reconstruct_from_table(table, self.p, self.q, ("a",))

    def test_singular_block_rejected(self):
        with self.assertRaises(ValueError):
            reconstruct_from_table({w: 1 for w in self.bank}, self.p, self.q, ("a",))

    def test_delayed_hidden_state_matches_training_and_fails_holdout(self):
        delayed = add_models(self.fib, delayed_spike_model(12))
        table = {w: delayed.response(w) for w in self.bank}
        got = reconstruct_from_table(table, self.p, self.q, ("a",))
        for n in range(12):
            self.assertEqual(got.model.response(("a",)*n), delayed.response(("a",)*n))
        self.assertEqual(delayed.response(("a",)*12)-got.model.response(("a",)*12), 1)
        table[("a",)*12] = delayed.response(("a",)*12)
        with self.assertRaises(ValueError):
            reconstruct_from_table(table, self.p, self.q, ("a",))

    def test_delayed_spike_antidiagonal_full_rank(self):
        for delay in (0, 1, 4, 7):
            model = delayed_spike_model(delay)
            h = matrix([[model.response(("a",)*(i+j)) for j in range(delay+1)]
                        for i in range(delay+1)])
            self.assertEqual(multiply(h, h), matrix([[int(i == j) for j in range(delay+1)]
                                                     for i in range(delay+1)]))
            self.assertEqual(inverse(h), h)

    def test_similarity_does_not_determine_graph_support(self):
        diag = Realization((1, 1), {"a": ((1, 0), (0, 2))}, (1, 1))
        tri = diag.changed_basis(((1, -1), (0, 1)))
        self.assertEqual(tri.transitions["a"], matrix(((1, 1), (0, 2))))
        self.assertEqual(tri.alpha, (1, 0))
        self.assertEqual(tri.beta, (2, 1))
        for n in range(20):
            self.assertEqual(diag.response(("a",)*n), tri.response(("a",)*n))
        self.assertNotEqual(diag.transitions["a"], tri.transitions["a"])

    def test_hidden_direct_summand_cannot_be_inferred(self):
        visible = Realization((1, 1), {"a": ((1, 0), (0, 2))}, (1, 1))
        hidden = Realization((0,), {"a": ((7,),)}, (0,))
        enlarged = add_models(visible, hidden)
        for n in range(20):
            self.assertEqual(visible.response(("a",)*n), enlarged.response(("a",)*n))
        self.assertEqual(sum(enlarged.transitions["a"][i][i] for i in range(3)), 10)
        self.assertEqual(sum(visible.transitions["a"][i][i] for i in range(2)), 3)

    def test_one_history_access_differs_from_reset_queries(self):
        bank = ((), ("a",), ("b",), ("a", "b"))
        self.assertEqual(missing_from_one_history(bank, ("a", "b")), (("b",),))
        self.assertEqual(missing_from_one_history(self.bank, ("a",)*3), ())

    def test_symbolic_function_closure_all_state_identity(self):
        sources = {"a": ((1, 1, 0), (0, 1, 0), (0, 0, 7)),
                   "b": ((1, 0, 0), (1, 1, 0), (0, 0, 9))}
        features = ((1, 0), (0, 1), (0, 0))
        reduced = {"a": ((1, 1), (0, 1)), "b": ((1, 0), (1, 1))}
        self.assertTrue(verify_linear_function_closure(sources, features, reduced,
                                                      (1, 0, 0), (1, 0)))
        sources["b"] = ((1, 0, 0), (1, 1, 0), (1, 0, 9))
        self.assertFalse(verify_linear_function_closure(sources, features, reduced,
                                                       (1, 0, 0), (1, 0)))

    def test_closure_requires_target_in_the_observed_span(self):
        self.assertFalse(verify_linear_function_closure(
            {"a": ((1, 0), (0, 2))}, ((1,), (0,)), {"a": ((1,),)}, (0, 1), (0,)))

    def test_affine_anchor_repairs_derivative_only_prediction(self):
        lifted = affine_row_lift(((1,),), (1,))
        translated = Realization((0, 1), {"a": lifted}, (1, 0))
        derivative_only = Realization((0,), {"a": ((1,),)}, (1,))
        for n in range(20):
            self.assertEqual(translated.response(("a",)*n), n)
        self.assertNotEqual(translated.response(("a",)), derivative_only.response(("a",)))
        with self.assertRaises(ValueError):
            affine_row_lift(((1, 0), (0, 1)), (1,))

    def test_exact_arithmetic_and_shapes_are_enforced(self):
        with self.assertRaises(TypeError):
            Realization((1.0,), {"a": ((1,),)}, (1,))
        with self.assertRaises(TypeError):
            Realization((True,), {"a": ((1,),)}, (1,))
        with self.assertRaises(ValueError):
            self.fib.changed_basis(((1,),))
        with self.assertRaises(ValueError):
            probe_bank(((), ("a",)), ((),), ("a",))
        with self.assertRaises(ValueError):
            probe_bank(((), ("x",)), ((), ("a",)), ("a",))


if __name__ == "__main__":
    unittest.main(verbosity=2)
