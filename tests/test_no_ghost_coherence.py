"""Exact lawful stochastic calibration and hostile certificate mutations."""
import unittest
from dataclasses import replace
from fractions import Fraction
from itertools import permutations, product

from observational_succ.no_ghost_coherence import (
    CNOT_RELABEL, TOKEN_SWAP, CarrierPoint, CoherenceError, CoherenceFailure,
    FairTokenCarrier, adjacent_compare, check_pair_table, compare_path,
    find_braid_failure, verify_coherence_failure, verify_pair_family,
)


class NoGhostPrivateCoherence(unittest.TestCase):
    def setUp(self):
        self.model = FairTokenCarrier()

    def test_actual_branch_kernel_and_one_use_enabledness(self):
        state = CarrierPoint(1, frozenset())
        branches = self.model.branches(state, "a")
        self.assertEqual(tuple(s.probability for s in branches), (Fraction(1, 2),) * 2)
        self.assertEqual(tuple(s.private_bit for s in branches), (0, 1))
        self.assertEqual(branches[0].after, branches[1].after)
        with self.assertRaises(CoherenceError):
            self.model.branches(branches[0].after, "a")
        with self.assertRaises(CoherenceError):
            self.model.history(0, ("a", "b"), (0, True))

    def test_each_schedule_is_lawful_with_complete_unit_mass_per_source(self):
        for schedule in permutations(self.model.events):
            histories = self.model.full_histories(schedule)
            for original in self.model.originals:
                fiber = [h for h in histories if h.original == original]
                self.assertEqual(len(fiber), 8)
                self.assertEqual(sum(h.weight for h in fiber), 1)
                self.assertTrue(all(self.model.check(h) for h in fiber))
                self.assertEqual({h.endpoint for h in fiber},
                                 {CarrierPoint(original, frozenset(self.model.events))})

    def test_pair_lawfulness_and_scope_of_branch_identity(self):
        self.assertTrue(check_pair_table(CNOT_RELABEL))
        self.assertTrue(verify_pair_family(self.model, CNOT_RELABEL))
        self.assertTrue(verify_pair_family(self.model, TOKEN_SWAP, preserve_event_tokens=True))
        self.assertFalse(verify_pair_family(self.model, CNOT_RELABEL, preserve_event_tokens=True))

    def test_requested_calibration_is_a_typed_lawful_example(self):
        h = self.model.history(0, ("a", "b", "c"), (0, 1, 0))
        left = compare_path(self.model, h, (0, 1, 0), CNOT_RELABEL)
        right = compare_path(self.model, h, (1, 0, 1), CNOT_RELABEL)
        self.assertEqual(left.schedule, ("c", "b", "a"))
        self.assertEqual(left.schedule, right.schedule)
        self.assertEqual(left.bits, (0, 1, 1))
        self.assertEqual(right.bits, (0, 1, 0))
        self.assertNotEqual(left, right)

    def test_certificate_and_hostile_mutations(self):
        cert = find_braid_failure(self.model)
        self.assertIsInstance(cert, CoherenceFailure)
        self.assertTrue(verify_coherence_failure(self.model, cert))
        self.assertFalse(verify_coherence_failure(self.model, replace(cert, right_bits=cert.left_bits)))
        self.assertFalse(verify_coherence_failure(self.model, replace(cert, final_schedule=("a", "b", "c"))))
        self.assertFalse(verify_coherence_failure(self.model, replace(cert, pair_table=TOKEN_SWAP)))
        self.assertFalse(verify_coherence_failure(self.model, replace(cert, left_path=(0,))))
        self.assertFalse(verify_coherence_failure(self.model, replace(
            cert, initial=replace(cert.initial, source_id="different-source"))))
        bad_table = ((0, 0), (0, 0), (1, 0), (1, 1))
        self.assertFalse(verify_pair_family(self.model, bad_table))
        self.assertFalse(verify_coherence_failure(self.model, replace(cert, pair_table=bad_table)))

    def test_coherent_alternative_exists_and_preserves_every_branch_value(self):
        self.assertIsNone(find_braid_failure(self.model, TOKEN_SWAP))
        for schedule in permutations(self.model.events):
            for bits in product((0, 1), repeat=3):
                h = self.model.history(0, schedule, bits)
                left = compare_path(self.model, h, (0, 1, 0), TOKEN_SWAP)
                right = compare_path(self.model, h, (1, 0, 1), TOKEN_SWAP)
                self.assertEqual(left, right)
                self.assertEqual(left.event_tokens, h.event_tokens)

    def test_disjoint_square_and_backtracking_are_not_the_missing_axiom(self):
        model = FairTokenCarrier(events=("a", "b", "c", "d"))
        for bits in product((0, 1), repeat=4):
            h = model.history(1, model.events, bits)
            self.assertEqual(compare_path(model, h, (0, 2), CNOT_RELABEL),
                             compare_path(model, h, (2, 0), CNOT_RELABEL))
            self.assertEqual(compare_path(model, h, (0, 0), CNOT_RELABEL), h)


if __name__ == "__main__":
    unittest.main()
