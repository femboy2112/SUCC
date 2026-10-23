"""Exact hostile controls; finite cases corroborate, not prove, paper theorems."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product

from observational_succ.boundary_realization_selection import (
    BoundarySourceError, FiniteNetwork, boundary_response, matmul,
)
from observational_succ.reality_pin_selection import (
    PinContractError, PinPlan, Prediction, glue, identify, pullback, rc_plan,
    refine_equal_series, schur, separation_witnesses, series_rc, series_rc_box,
    synthetic_rc_receipt, transpose, schur_perturbation_bound,
)


class RealityPinSelectionTests(unittest.TestCase):
    def test_finite_separation_is_strict(self):
        p = PinPlan("s", ("x",), (Prediction("a", "a", (0,), (0,)),
                                     Prediction("b", "b", (2,), (0,))), (1,))
        self.assertEqual(separation_witnesses(p), (("a", "b", ()),))
        self.assertEqual(len(identify(p, "s", p.digest(), {"x": 1})["models"]), 2)
        q = replace(p, instrument_errors=(Q(999, 1000),))
        self.assertEqual(separation_witnesses(q), (("a", "b", ("x",)),))

    def test_vector_probe_and_unequal_theory_errors(self):
        p = PinPlan("s", ("x", "y"),
                    (Prediction("a", "a", (0, 0), (1, Q(1, 10))),
                     Prediction("b", "b", (0, 2), (1, Q(1, 5)))), (1, Q(1, 10)))
        self.assertEqual(separation_witnesses(p), (("a", "b", ("y",)),))
        self.assertEqual(identify(p, "s", p.digest(), {"y": Q(1, 10)})["models"], ("a",))

    def test_same_gauge_does_not_make_extra_physical_models(self):
        p = PinPlan("s", ("x",), (Prediction("a", "g", (1,), (0,)),
                                    Prediction("copy", "g", (1,), (0,))), (0,))
        result = identify(p, "s", p.digest(), {"x": 1})
        self.assertEqual(result["models"], ("a", "copy"))
        self.assertTrue(result["unique_within_family"])
        self.assertFalse(result["physical_authentication"])

    def test_source_commitment_and_language_fail_closed(self):
        p = rc_plan()
        for source, commitment, readings in (("other", p.digest(), {"dc": 1}),
                                             (p.source_id, "bad", {"dc": 1}),
                                             (p.source_id, p.digest(), {"unknown": 1})):
            with self.assertRaises(PinContractError):
                identify(p, source, commitment, readings)
        mutated = replace(p, predictions=(Prediction("postfit", "postfit", (1, 1, 1), (0, 0, 0)),))
        with self.assertRaises(PinContractError):
            identify(mutated, mutated.source_id, p.digest(), {"dc": 1})

    def test_noisy_out_of_family_data_returns_empty(self):
        p = rc_plan()
        self.assertTrue(identify(p, p.source_id, p.digest(), {"dc": 20})["empty_fiber"])

    def test_continuous_tolerances_all_corners_and_fresh_interiors(self):
        interval = (Q(99, 100), Q(101, 100))
        for s in (0, 1, 3, Q(7, 4)):
            lower, upper = series_rc_box(interval, interval, interval, s)
            for values in product((interval[0], Q(1), Q(2001, 2000), interval[1]), repeat=3):
                actual = series_rc(*values, s)
                self.assertLessEqual(lower, actual)
                self.assertLessEqual(actual, upper)

    def test_rc_against_independent_full_graph_assembly(self):
        for a, b, c, s in product((Q(1), Q(3, 2)), (Q(2), Q(5, 4)), (Q(1), Q(7, 3)), (0, 1, 3)):
            network = FiniteNetwork(3, (0, 2), ((0, 1, a), (1, 2, b)), ((1, c),))
            self.assertEqual(series_rc(a, b, c, s), boundary_response(network, s)[0][0])

    def test_synthetic_calibration_and_unspent_holdout(self):
        receipt = synthetic_rc_receipt()
        self.assertFalse(receipt["physical_measurements_performed"])
        self.assertEqual(len(receipt["dc_selection"]["models"]), 2)
        self.assertEqual(receipt["calibration_selection"]["models"], ("series-capacitor",))
        self.assertEqual(receipt["heldout_selection"]["models"], ("series-capacitor",))
        self.assertFalse(receipt["heldout_selection"]["unique_gauge_within_family"])
        self.assertEqual(receipt["heldout_selection"]["identification_scope"], "topology_family")
        p = rc_plan()
        self.assertEqual(identify(p, p.source_id, p.digest(), {"holdout-laplace-3": Q(1, 2)})["models"], ("direct",))

    def test_restricted_family_false_uniqueness(self):
        p = rc_plan()
        narrow = replace(p, predictions=(p.predictions[0],))
        self.assertTrue(identify(narrow, narrow.source_id, narrow.digest(), {"dc": Q(1, 2)})["unique_within_family"])
        self.assertFalse(identify(p, p.source_id, p.digest(), {"dc": Q(1, 2)})["unique_within_family"])

    def test_constructive_refinement_contains_truth_and_rate(self):
        truth = Q(31, 23)
        for r in range(1, 9):
            eps = Q(1, 2**r)
            reading = series_rc(truth, truth, 1, 2) + eps / 3
            leaves = refine_equal_series((1, 2), reading, eps, 2, r)
            self.assertTrue(any(a <= truth <= b for a, b in leaves))
            self.assertLessEqual(leaves[-1][1] - leaves[0][0], 6 * eps)

    def test_nonvanishing_error_does_not_force_unique_limit(self):
        reading = series_rc(Q(3, 2), Q(3, 2), 1, 1)
        leaves = refine_equal_series((1, 2), reading, Q(1, 10), 1, 8)
        self.assertGreater(leaves[-1][1] - leaves[0][0], Q(1, 10))

    def test_exact_rejects_float_and_invalid_budgets(self):
        with self.assertRaises(BoundarySourceError):
            series_rc(1.0, 1, 1, 1)
        with self.assertRaises(PinContractError):
            Prediction("a", "a", (1,), (-1,))


class BoundaryCompositionTests(unittest.TestCase):
    def test_nested_elimination_order(self):
        L = ((5, -1, -2, 0), (-1, 6, -1, -1), (-2, -1, 7, -2), (0, -1, -2, 8))
        direct = schur(L, (0, 3))
        self.assertEqual(direct, schur(schur(L, (0, 2, 3)), (0, 2)))
        self.assertEqual(direct, schur(schur(L, (0, 1, 3)), (0, 2)))

    def test_interior_congruence_naturality(self):
        L = ((4, -1, 1, 0), (-1, 5, 0, -1), (1, 0, 3, 1), (0, -1, 1, 4))
        U = ((2, 1), (0, 1))
        T = ((0, -1), (1, 0))
        block = ((0, -1, 0, 0), (1, 0, 0, 0), (0, 0, 2, 1), (0, 0, 0, 1))
        self.assertEqual(schur(pullback(L, block), (0, 1)), pullback(schur(L, (0, 1)), T))

    def test_gluing_matches_independent_full_operator(self):
        L1 = ((4, 0, -1), (0, 5, -2), (-1, -2, 4))
        L2 = ((6, -1, -2), (-1, 7, -1), (-2, -1, 5))
        identity, swap = ((1, 0), (0, 1)), ((0, 1), (1, 0))
        expected = glue((schur(L1, (0, 1)), schur(L2, (0, 1))), (identity, swap))
        # Assemble directly in [shared port 0, shared port 1, private 1, private 2].
        A = [[Q(0) for _ in range(4)] for _ in range(4)]
        for L, placement in ((L1, (0, 1, 2)), (L2, (1, 0, 3))):
            for i in range(3):
                for j in range(3):
                    A[placement[i]][placement[j]] += L[i][j]
        self.assertEqual(expected, schur(A, (0, 1)))

    def test_wrong_orientation_is_detectable(self):
        L = ((2, -1), (-1, 3))
        correct = pullback(L, ((1, 0), (0, 1)))
        reversed_second = pullback(L, ((1, 0), (0, -1)))
        self.assertNotEqual(correct, reversed_second)
        self.assertEqual(reversed_second, ((2, 1), (1, 3)))

    def test_identical_total_has_nonunique_decompositions(self):
        identity = ((1, 0), (0, 1))
        L = ((2, -1), (-1, 2))
        half = tuple(tuple(v / Q(2) for v in row) for row in L)
        self.assertEqual(glue((half, half), (identity, identity)), L)
        self.assertEqual(glue((L,), (identity,)), L)

    def test_singular_elimination_and_bad_ports_fail(self):
        with self.assertRaises(BoundarySourceError):
            schur(((1, 0), (0, 0)), (0,))
        with self.assertRaises(PinContractError):
            schur(((1, 0), (0, 1)), (0, 0))

    def test_quantified_schur_perturbation(self):
        L = ((10, 3, 4), (3, 4, 0), (4, 0, 5))
        other = ((Q(51, 5), Q(33, 10), Q(22, 5)),
                 (Q(33, 10), Q(39, 10), 0), (Q(22, 5), 0, Q(51, 10)))
        observed = abs(schur(L, (0,))[0][0] - schur(other, (0,))[0][0])
        bound = schur_perturbation_bound(4, 5, Q(1, 10), Q(1, 2), Q(1, 5))
        self.assertLessEqual(observed, bound)
        with self.assertRaises(PinContractError):
            schur_perturbation_bound(1, 1, 1, 0, 0)


if __name__ == "__main__":
    unittest.main()
