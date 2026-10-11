"""Independent exact witnesses, mutants and finite holdouts for SUCC transport.

The mathematical universality is supplied by proofs in the dossier.
Exhaustive finite tests calibrate the code and discover counterexamples;
they do not elevate the physical or analytic hypotheses.
"""
import random
import unittest
from itertools import product

from observational_succ.precision_transport import (
    TransportError, PrecisionFrame, ClaimContext, TransportVerdict,
    nonzero_valuation, minimum_full_resolution, minimum_claim_resolution,
    certify_transport, compose_full_lifts, certify_intervention,
    precision_transport_demo,
)


def _context(p, r, claims, suffix="A"):
    return ClaimContext.from_mapping(
        p, r, claims, source_id="source-" + suffix,
        basis_id="declared-basis-v1", claim_id="finite-claim")


def _naive_factorization(table, p, r, d, s):
    """Totally independent finite group-by-output oracle."""
    grouped = {}
    for x, claim in table.items():
        grouped.setdefault((d * x) % (p ** s), set()).add(claim)
    return all(len(labels) == 1 for labels in grouped.values())


def _naive_threshold(table, p, r, d):
    """Find the least precision by search rather than by v_p pair formula."""
    if len(set(table.values())) == 1:
        return 1
    if d == 0:
        return None
    for s in range(1, r + nonzero_valuation(d, p) + 1):
        if _naive_factorization(table, p, r, d, s):
            return s
    raise AssertionError("A full faithful lift must preserve any source claim")


class PrecisionTransportArithmeticTests(unittest.TestCase):
    def test_canonical_resolution_is_necessary_for_representative_independence(self):
        for p in (2, 3, 5, 7):
            for r in range(1, 4):
                for d in (-25, -10, -5, -1, 1, 2, 5, 10, 25):
                    v = nonzero_valuation(d, p)
                    s = r + v
                    frame = PrecisionFrame(p, r, d, s)
                    self.assertTrue(frame.full_clock_faithful)
                    self.assertEqual(frame.debt, v)
                    for x in (0, 1, (p ** r) - 1):
                        self.assertEqual((d * x) % (p ** s),
                                         (d * (x + p ** r)) % (p ** s))
                        self.assertNotEqual((d * x) % (p ** (s + 1)),
                                            (d * (x + p ** r)) % (p ** (s + 1)))
                    with self.assertRaises(TransportError):
                        PrecisionFrame(p, r, d, s + 1)

    def test_exact_kernel_fibers_image_and_cardinality_independent_enumeration(self):
        for p in (2, 3, 5):
            for r in range(1, 4):
                for d in (-10, -5, -2, -1, 0, 1, 2, 5, 10):
                    upper = r + (nonzero_valuation(d, p) if d else 2)
                    for s in range(1, upper + 1):
                        frame = PrecisionFrame(p, r, d, s)
                        outputs = [frame.observe(x) for x in range(p ** r)]
                        fibers = {}
                        for x, y in enumerate(outputs):
                            fibers.setdefault(y, set()).add(x)
                        self.assertEqual(len(fibers), frame.image_size)
                        self.assertTrue(all(
                            len(xs) == frame.fiber_size for xs in fibers.values()))
                        for x in range(p ** r):
                            for z in range(p ** r):
                                same_output = outputs[x] == outputs[z]
                                same_prefix = (x - z) % (p ** frame.observed_digits) == 0
                                self.assertEqual(same_output, same_prefix)

    def test_source_is_injective_only_at_full_precision_in_unrestricted_clock(self):
        for p, r, d in ((2, 4, 4), (3, 3, 9), (5, 2, -10),
                        (5, 3, 125), (7, 2, 1)):
            s = minimum_full_resolution(p, r, d)
            exact = PrecisionFrame(p, r, d, s)
            self.assertTrue(exact.full_clock_faithful)
            self.assertEqual(exact.image_size, p ** r)
            self.assertEqual(exact.fiber_size, 1)
            for x in range(p ** r):
                y = exact.observe(x)
                self.assertEqual(exact.full_decode(y), x)
                self.assertEqual(y % (p ** exact.debt), 0)
            with self.assertRaises(TransportError):
                exact.full_decode(1) if exact.debt else exact.full_decode(p ** s)
            for t in range(1, s):
                truncated = PrecisionFrame(p, r, d, t)
                self.assertFalse(truncated.full_clock_faithful)
                with self.assertRaises(TransportError):
                    truncated.full_decode(truncated.observe(0))

    def test_linear_meta_succ_crosses_nonunit_without_information_annihilation(self):
        # Same SUCC jet (0,1,4) -> (1,5,4) at p=5, mod 25.
        before = PrecisionFrame(5, 2, 1, 2)
        fixed_precision_after = PrecisionFrame(5, 2, 5, 2)
        compensated_after = PrecisionFrame(5, 2, 5, 3)
        self.assertEqual((before.image_size, fixed_precision_after.image_size),
                         (25, 5))
        self.assertEqual(compensated_after.image_size, 25)
        self.assertEqual(compensated_after.debt, 1)
        self.assertEqual(compensated_after.full_decode(
            compensated_after.observe(19)), 19)
        self.assertEqual(fixed_precision_after.observe(1),
                         fixed_precision_after.observe(6))
        self.assertNotEqual(compensated_after.observe(1),
                            compensated_after.observe(6))

    def test_zero_step_is_genuine_full_source_erasure_in_this_channel(self):
        self.assertIsNone(minimum_full_resolution(5, 2, 0))
        for s in (1, 2, 3, 9):
            frame = PrecisionFrame(5, 2, 0, s)
            self.assertEqual(frame.image_size, 1)
            self.assertEqual(frame.fiber_size, 25)
            self.assertEqual({frame.observe(x) for x in range(25)}, {0})
            with self.assertRaises(TransportError):
                frame.full_decode(0)

    def test_full_lift_functorial_composition_and_associativity_controls(self):
        for p, r, ds in (
            (2, 3, (4, -6, 3)),
            (3, 2, (9, 6, -3)),
            (5, 2, (5, -10, 25)),
            (7, 2, (2, -7, 14)),
        ):
            d, e, f = ds
            first_two = compose_full_lifts(p, r, d, e)
            last_two = compose_full_lifts(p, r, d * e, f)
            total = compose_full_lifts(p, r, d, e * f)
            self.assertEqual(last_two.composite.s, total.composite.s)
            self.assertEqual(total.composite.debt,
                             sum(nonzero_valuation(a, p) for a in ds))
            for x in range(p ** r):
                self.assertEqual(first_two.apply(x), (d * e * x) %
                                 (p ** first_two.composite.s))
                y1 = first_two.first.observe(x)
                y2 = first_two.second.observe(y1)
                final = PrecisionFrame(p, first_two.second.s, f,
                                       total.composite.s).observe(y2)
                self.assertEqual(final, last_two.apply(x))
                self.assertEqual(final, total.apply(x))
                self.assertEqual(total.composite.full_decode(final), x)

    def test_wrong_place_boolean_and_noncanonical_representatives_rejected(self):
        for args in ((6, 2, 1, 2), (1, 2, 1, 2), (True, 2, 1, 2),
                     (5, 0, 1, 1), (5, 2, True, 2), (5, 2, 1, 0)):
            with self.assertRaises(TransportError):
                PrecisionFrame(*args)
        frame = PrecisionFrame(5, 2, 5, 3)
        for x in (-1, 25, 26, 1.0, True):
            with self.assertRaises(TransportError):
                frame.observe(x)
        for y in (-1, 125, 2.5, True):
            with self.assertRaises(TransportError):
                frame.full_decode(y)


class PrecisionTransportProofTests(unittest.TestCase):
    def test_five_adic_low_digit_survives_and_high_digit_needs_repair(self):
        low = _context(5, 2, {x: str(x % 5) for x in range(25)})
        high = _context(5, 2, {x: str(x // 5) for x in range(25)})
        truncated = PrecisionFrame(5, 2, 5, 2)
        full = PrecisionFrame(5, 2, 5, 3)
        good = certify_transport(low, truncated)
        bad = certify_transport(high, truncated)
        repaired = certify_transport(high, full)
        self.assertEqual(low.separation_depth(), 1)
        self.assertEqual(high.separation_depth(), 2)
        self.assertEqual(minimum_claim_resolution(low, 5), 2)
        self.assertEqual(minimum_claim_resolution(high, 5), 3)
        self.assertTrue(good.valid)
        self.assertFalse(bad.valid)
        self.assertIsNotNone(bad.collision)
        x, y = bad.collision
        self.assertEqual(truncated.observe(x), truncated.observe(y))
        self.assertNotEqual(dict(high.claims)[x], dict(high.claims)[y])
        self.assertTrue(repaired.valid)
        for a, label in high.claims:
            self.assertEqual(repaired.decode(full.observe(a), high), label)
        for a, label in low.claims:
            self.assertEqual(good.decode(truncated.observe(a), low), label)

    def test_complete_binary_claim_tables_against_independent_truth_oracle(self):
        # All 2^8 Boolean predicates on the entire 2^3 clock.
        for bits in product(("0", "1"), repeat=8):
            table = dict(enumerate(bits))
            context = _context(2, 3, table)
            for d in (-4, -2, -1, 0, 1, 2, 4):
                expected = _naive_threshold(table, 2, 3, d)
                self.assertEqual(minimum_claim_resolution(context, d), expected)
                max_s = 3 + (nonzero_valuation(d, 2) if d else 1)
                for s in range(1, max_s + 1):
                    verdict = certify_transport(context, PrecisionFrame(2, 3, d, s))
                    self.assertEqual(verdict.valid,
                                     _naive_factorization(table, 2, 3, d, s))
                    self.assertEqual(verdict.valid,
                                     expected is not None and s >= expected)
                    if not verdict.valid:
                        a, b = verdict.collision
                        self.assertNotEqual(table[a], table[b])
                        self.assertEqual((d * a) % (2 ** s), (d * b) % (2 ** s))

    def test_seeded_unfitted_source_subsets_and_multilabel_holdouts(self):
        rng = random.Random(918271)
        for case in range(100):
            p = rng.choice((2, 3, 5))
            r = rng.choice((1, 2, 3))
            x_values = rng.sample(range(p ** r), k=min(p ** r, rng.randint(1, 12)))
            table = {x: str(rng.randrange(4)) for x in x_values}
            context = _context(p, r, table, suffix=str(case))
            d = rng.choice((-25, -10, -5, -1, 0, 1, 2, 5, 10, 25))
            expected = _naive_threshold(table, p, r, d)
            self.assertEqual(minimum_claim_resolution(context, d), expected)
            max_s = r + (nonzero_valuation(d, p) if d else 2)
            for s in range(1, max_s + 1):
                frame = PrecisionFrame(p, r, d, s)
                verdict = certify_transport(context, frame)
                self.assertEqual(verdict.valid,
                                 _naive_factorization(table, p, r, d, s))
                if verdict.valid:
                    for x, value in table.items():
                        self.assertEqual(verdict.decode(frame.observe(x), context),
                                         value)

    def test_source_context_change_and_stale_basis_cannot_reuse_decoder(self):
        context = _context(5, 2, {1: "same", 6: "same"}, "narrow")
        frame = PrecisionFrame(5, 2, 5, 2)
        cert = certify_transport(context, frame)
        self.assertTrue(cert.valid)
        self.assertEqual(cert.decode(5, context), "same")
        expanded = _context(5, 2, {1: "same", 6: "same", 11: "other"},
                            "expanded")
        self.assertFalse(certify_transport(expanded, frame).valid)
        with self.assertRaises(TransportError):
            cert.decode(5, expanded)
        same_data_new_basis = ClaimContext.from_mapping(
            5, 2, {1: "same", 6: "same"}, source_id="source-narrow",
            basis_id="reindexed-basis", claim_id="finite-claim")
        with self.assertRaises(TransportError):
            cert.decode(5, same_data_new_basis)
        same_data_new_claim = ClaimContext.from_mapping(
            5, 2, {1: "same", 6: "same"}, source_id="source-narrow",
            basis_id="declared-basis-v1", claim_id="another-statement")
        with self.assertRaises(TransportError):
            cert.decode(5, same_data_new_claim)
        with self.assertRaises(TransportError):
            cert.decode(0, context)

    def test_constant_claim_can_survive_zero_or_nonunit_step(self):
        constant = _context(5, 2, {x: "Q" for x in range(25)})
        nonconstant = _context(5, 2, {0: "Q", 1: "R"})
        self.assertEqual(constant.separation_depth(), 0)
        self.assertEqual(minimum_claim_resolution(constant, 0), 1)
        self.assertIsNone(minimum_claim_resolution(nonconstant, 0))
        for s in (1, 2, 5):
            frame = PrecisionFrame(5, 2, 0, s)
            self.assertTrue(certify_transport(constant, frame).valid)
            self.assertFalse(certify_transport(nonconstant, frame).valid)

    def test_source_intervention_semantic_and_observation_gates_are_distinct(self):
        before = _context(5, 2, {x: str(x % 5) for x in range(25)}, "old")
        after = _context(5, 2, {x: str(x % 5) for x in range(25)}, "new")
        frame = PrecisionFrame(5, 2, 5, 2)
        valid = certify_intervention(
            before, after, {x: (x + 5) % 25 for x in range(25)}, frame)
        self.assertTrue(valid.valid)
        self.assertEqual(valid.status, "source-and-observation-preserved")
        self.assertIsNotNone(valid.transport)
        # A source-preserving identity intervention but insufficient output.
        before_high = _context(
            5, 2, {x: str(x // 5) for x in range(25)}, "old-high")
        after_high = _context(
            5, 2, {x: str(x // 5) for x in range(25)}, "new-high")
        observed_bad = certify_intervention(
            before_high, after_high, {x: x for x in range(25)}, frame)
        self.assertEqual(observed_bad.status, "post-source-observation-collision")
        self.assertIsNotNone(observed_bad.observation_conflict)
        repaired = certify_intervention(
            before_high, after_high, {x: x for x in range(25)},
            PrecisionFrame(5, 2, 5, 3))
        self.assertTrue(repaired.valid)
        # Destructive intervention changes the original target law: no
        # resolution, including a full injective output, repairs semantics.
        reset_source = _context(
            5, 2, {x: str(x // 5) for x in range(5)}, "reset")
        changed = certify_intervention(
            before_high, reset_source, {x: x % 5 for x in range(25)},
            PrecisionFrame(5, 2, 5, 3))
        self.assertEqual(changed.status, "source-truth-changed")
        self.assertIsNotNone(changed.semantic_conflict)
        self.assertFalse(changed.valid)

    def test_malformed_source_and_unjustified_interventions_rejected(self):
        with self.assertRaises(TransportError):
            ClaimContext(5, 2, ((6, "a"), (1, "b")), "s", "b", "c")
        with self.assertRaises(TransportError):
            ClaimContext(5, 2, ((1, "a"), (1, "b")), "s", "b", "c")
        with self.assertRaises(TransportError):
            _context(6, 2, {0: "p"})
        with self.assertRaises(TransportError):
            _context(5, 2, {25: "out"})
        context = _context(5, 2, {1: "a", 2: "b"})
        for h in ({1: 1}, {1: 1, 2: 25}, {1: 1, 2: True}):
            with self.assertRaises(TransportError):
                certify_intervention(context, context, h,
                                     PrecisionFrame(5, 2, 1, 2))
        with self.assertRaises(TransportError):
            certify_transport(context, PrecisionFrame(3, 2, 1, 2))

    def test_machine_receipt_has_full_negative_claim_firewall(self):
        x = precision_transport_demo()
        self.assertEqual(x["status"], "SOURCE_RELATIVE_PRECISION_TRANSPORT_EXACT")
        self.assertEqual((x["coarse_image_size"],
                          x["source_repair_output_precision"]), (5, 3))
        self.assertEqual(x["high_digit_claim_minimum_precision"], 3)
        self.assertFalse(x["high_digit_claim_at_coarse_precision"])
        self.assertTrue(x["high_digit_claim_after_repair"])
        self.assertTrue(x["source_preserving_intervention"])
        self.assertEqual(x["destructive_intervention_status"],
                         "source-truth-changed")
        self.assertFalse(x["extra_precision_repairs_destructive_source_change"])
        self.assertFalse(x["zero_step_has_finite_full_repair"])
        self.assertFalse(x["finite_source_table_authenticates_physical_truth"])
        self.assertFalse(x["RH_Gamma_or_Weil_theorem_claimed"])


if __name__ == "__main__":
    unittest.main()
