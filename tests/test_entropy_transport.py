"""Countermodels and exact structural gates for finite entropy transport.

Floating entropy assertions calibrate diagnostics. The universal claims
are proved in the research note; these tests do not certify real logs.
"""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.entropy_transport import (
    EntropyTransportError, FiniteLaw, entropy, conditional_entropy,
    mutual_information, require_determined, conditionally_independent,
    shared_conditioning_identity, reversible_information_transport,
    conditional_continuity, block_transport, sharp_mod5_law,
    entropy_transport_probe,
)


class EntropyTransportTests(unittest.TestCase):
    def test_source_dependent_translation_needs_both_bits(self):
        law = sharp_mod5_law()
        for (x, s, xp, w), mass in law.atoms:
            self.assertEqual(mass, F(1, 4))
            self.assertEqual((x+s) % 5, xp)
            self.assertNotEqual(x, 0)
            self.assertNotEqual(xp, 0)
        require_determined(law, ("S",), ("X",))
        require_determined(law, ("X",), ("S", "W"))
        self.assertTrue(conditionally_independent(law, ("XP", "W")))
        r = reversible_information_transport(law, old_target=("X",),
            new_target=("XP",), word=("W",), update=("S",))
        self.assertAlmostEqual(r["loss_bits"], 2)
        self.assertAlmostEqual(r["identity_loss_bits"], 2)
        self.assertAlmostEqual(entropy(law, ("S",)), 1)
        self.assertAlmostEqual(r["new_word_information_bits"], 0)

    def test_exogenous_update_one_bit_bound_and_receiver_known_update(self):
        law = FiniteLaw(("X", "S", "XP", "W"), tuple(
            ((x, s, x ^ s, x), F(1, 4)) for x, s in product(range(2), repeat=2)),
            "exogenous-one-time-pad")
        self.assertTrue(conditionally_independent(law, ("X", "S")))
        r = reversible_information_transport(law, old_target=("X",),
            new_target=("XP",), word=("W",), update=("S",))
        self.assertAlmostEqual(r["sender_revelation_bits"], 0)
        self.assertAlmostEqual(r["loss_bits"], 1)
        known = reversible_information_transport(law, old_target=("X",),
            new_target=("XP",), word=("W",), update=("S",), receiver=("S",))
        self.assertAlmostEqual(known["loss_bits"], 0)
        self.assertAlmostEqual(known["two_update_entropy_bound_bits"], 0)

    def test_noninvertible_frame_mutation_is_rejected(self):
        broken = FiniteLaw(("X", "S", "XP", "W"),
            (((0, 0, 0, 0), F(1, 2)), ((1, 0, 0, 1), F(1, 2))), "erasure")
        with self.assertRaisesRegex(EntropyTransportError, "not determined"):
            reversible_information_transport(broken, old_target=("X",),
                new_target=("XP",), word=("W",), update=("S",))

    def test_repeated_coordinates_cannot_supply_fresh_joint_entropy(self):
        names = tuple(f"X{i}" for i in range(8))
        law = FiniteLaw(names + ("U",), tuple(
            (((b,) * 9), F(1, 2)) for b in range(2)), "one-bit-repeated-eight-times")
        self.assertFalse(conditionally_independent(law, names))
        self.assertAlmostEqual(entropy(law, names), 1)
        r = shared_conditioning_identity(law, names, ("U",),
                                        alphabet_sizes={x: 2 for x in names})
        self.assertAlmostEqual(r["joint_deficit_bits"], 7)
        self.assertAlmostEqual(r["shared_update_entropy_bits"], 1)
        self.assertAlmostEqual(r["sum_conditional_deficits_bits"], 8)
        self.assertAlmostEqual(r["identity_rhs_bits"], 8)

    def test_parity_update_creates_conditional_dependence_instead_of_marginal_debt(self):
        law = FiniteLaw(("X", "Y", "U"), tuple(
            ((x, y, x ^ y), F(1, 4)) for x, y in product(range(2), repeat=2)),
            "parity-side-information")
        self.assertTrue(conditionally_independent(law, ("X", "Y")))
        self.assertFalse(conditionally_independent(law, ("X", "Y"), ("U",)))
        r = shared_conditioning_identity(law, ("X", "Y"), ("U",),
                                        alphabet_sizes={"X": 2, "Y": 2})
        self.assertAlmostEqual(r["update_information_bits"], 1)
        self.assertAlmostEqual(r["conditional_total_correlation_bits"], 1)
        self.assertAlmostEqual(r["sum_conditional_deficits_bits"], 0)
        self.assertAlmostEqual(r["identity_rhs_bits"], 0)

    def test_receiver_context_must_condition_initial_entropy_too(self):
        law = FiniteLaw(("X", "U", "R"),
            (((0, 0, 0), F(1, 2)), ((1, 1, 1), F(1, 2))), "known-source")
        r = shared_conditioning_identity(law, ("X",), ("U",),
                                        alphabet_sizes={"X": 2}, receiver=("R",))
        self.assertAlmostEqual(r["shared_update_entropy_bits"], 0)
        self.assertAlmostEqual(r["joint_deficit_bits"], 1)
        self.assertAlmostEqual(r["sum_conditional_deficits_bits"], 1)
        self.assertAlmostEqual(entropy(law, ("X",)), 1)
        self.assertAlmostEqual(conditional_entropy(law, ("X",), ("R",)), 0)

    def test_continuity_does_not_scale_with_observer_alphabet(self):
        reports = []
        for n in (1, 37):
            p = FiniteLaw(("A", "R"), tuple(((0, i), F(1, n)) for i in range(n)),
                          "same-channel-source")
            q = FiniteLaw(("A", "R"), tuple(
                ((a, i), F(3 if a == 0 else 1, 4*n))
                for i in range(n) for a in range(2)), "same-channel-source")
            report = conditional_continuity(p, q, ("A",), ("R",), alphabet_size=2)
            self.assertEqual(report["total_variation"], F(1, 4))
            self.assertLess(report["entropy_difference_bits"], report["continuity_bound_bits"])
            reports.append(report)
        self.assertAlmostEqual(reports[0]["continuity_bound_bits"], reports[1]["continuity_bound_bits"])
        self.assertAlmostEqual(reports[0]["entropy_difference_bits"], reports[1]["entropy_difference_bits"])

    def test_continuity_endpoint_and_source_drift_gates(self):
        p = FiniteLaw(("A", "R"), (((0, 0), 1),), "source")
        q = FiniteLaw(("A", "R"), (((0, 1), F(1, 2)), ((1, 1), F(1, 2))), "source")
        report = conditional_continuity(p, q, ("A",), ("R",), alphabet_size=2)
        self.assertEqual(report["total_variation"], 1)
        self.assertAlmostEqual(report["entropy_difference_bits"], 1)
        self.assertAlmostEqual(report["continuity_bound_bits"], 1)
        stale = FiniteLaw(q.variables, q.atoms, "different-source")
        with self.assertRaisesRegex(EntropyTransportError, "source"):
            conditional_continuity(p, stale, ("A",), ("R",), alphabet_size=2)
        tiny = F(1, 2**80)
        almost_disjoint = FiniteLaw(("A", "R"),
            (((0, 0), tiny), ((1, 1), 1-tiny)), "source")
        rounded = conditional_continuity(p, almost_disjoint, ("A",), ("R",),
                                         alphabet_size=2)
        self.assertEqual(rounded["total_variation"], 1-tiny)
        self.assertGreaterEqual(rounded["continuity_bound_bits"], 1)

    def test_moving_states_update_from_preceding_increment_without_new_cost(self):
        law = FiniteLaw(("Q0", "A", "B", "Q1"), tuple(
            ((q, a, b, q ^ a), F(1, 8)) for q, a, b in product(range(2), repeat=3)),
            "additive-observer")
        r = block_transport(law, blocks=(("A",), ("B",)),
                            states=(("Q0",), ("Q1",)), initial=("Q0",))
        self.assertAlmostEqual(r["word_entropy_bits"], 2)
        self.assertAlmostEqual(r["local_block_entropy_sum_bits"], 2)
        self.assertAlmostEqual(r["shared_update_entropy_bits"], 0)

    def test_one_shared_update_for_both_blocks_and_unpaid_mutation(self):
        law = FiniteLaw(("A", "B", "U"),
            (((0, 0, 0), F(1, 2)), ((1, 1, 1), F(1, 2))), "shared-bit")
        r = block_transport(law, blocks=(("A",), ("B",)),
                            states=(("U",), ("U",)), initial=(), update=("U",))
        self.assertAlmostEqual(r["word_entropy_bits"], 1)
        self.assertAlmostEqual(r["local_block_entropy_sum_bits"], 0)
        self.assertAlmostEqual(r["shared_update_entropy_bits"], 1)
        self.assertAlmostEqual(r["entropy_bound_bits"], 1)
        with self.assertRaisesRegex(EntropyTransportError, "not determined"):
            block_transport(law, blocks=(("A",), ("B",)),
                            states=(("U",), ("U",)), initial=())

    def test_noncommon_law_can_overcharge_nested_rates(self):
        law = FiniteLaw(("A", "B", "Q1", "Q2", "Q1_NEXT"), tuple(
            ((a, b, a, (a, b), 0), F(1, 4)) for a, b in product(range(2), repeat=2)),
            "unsmoothed-two-letter-control")
        require_determined(law, ("Q1_NEXT",), ("Q1", "A"))
        charge = mutual_information(law, ("Q1",), ("A",))
        charge += mutual_information(law, ("Q2",), ("A", "B"), ("Q1",)) / 2
        self.assertAlmostEqual(charge, 1.5)  # larger than one-bit letter capacity

    def test_exact_probability_validation_and_scope_receipt(self):
        for atoms in ((((0,), 0.5), ((1,), 0.5)),
                      (((0,), F(2)), ((1,), F(-1))),
                      (((0,), F(1, 3)),)):
            with self.assertRaises(EntropyTransportError):
                FiniteLaw(("X",), atoms, "invalid")
        with self.assertRaises(EntropyTransportError):
            FiniteLaw(("X", "X"), (((0, 0), 1),), "duplicate-names")
        receipt = entropy_transport_probe()
        self.assertFalse(receipt["formal_proof_or_interval_certificate"])
        self.assertFalse(receipt["repeated_facts_are_independent"])
        self.assertTrue(receipt["uncharged_update_rejected"])


if __name__ == "__main__":
    unittest.main()
