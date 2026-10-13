import unittest
from dataclasses import replace

from observational_succ.swarm_completion import PartialEvidence
from observational_succ.swarm_x11_proof_limits import (
    Certificate, CertificationContext, CertificationError, LicensedRule, LicensedStage,
    all_binary_evidence, certify_finite_source, derive, finite_ideals,
    first_zero_parity_witnesses, observation_atom, verify_certificate,
)


class ProofLimitTests(unittest.TestCase):
    def setUp(self):
        self.context = CertificationContext("source", "basis")
        self.rules = (
            LicensedRule("combine", (observation_atom(3, 1), observation_atom(101, 0)), "claim"),
            LicensedRule("continue", ("claim",), "conclusion"),
        )
        self.stage = LicensedStage(self.context, PartialEvidence(((3, 1), (101, 0))),
                                   frozenset(("combine", "continue")))

    def test_licensed_multistep_support_and_replay(self):
        proof = derive(self.stage, self.rules, "conclusion")
        self.assertIsNotNone(proof)
        self.assertEqual(len(proof.steps), 2)
        self.assertTrue(verify_certificate(proof, self.stage, self.rules))
        extension = replace(self.stage, evidence=PartialEvidence(((3, 1), (52, 1), (101, 0))))
        self.assertTrue(verify_certificate(proof, extension, self.rules))

    def test_receipt_cannot_authorize_missing_evidence_or_license(self):
        proof = derive(self.stage, self.rules, "conclusion")
        for evidence in (PartialEvidence(((3, 1),)), PartialEvidence(((101, 0),))):
            weaker = replace(self.stage, evidence=evidence)
            self.assertIsNone(derive(weaker, self.rules, "conclusion"))
            self.assertFalse(verify_certificate(proof, weaker, self.rules))
        for licenses in (frozenset(("combine",)), frozenset(("continue",))):
            weaker = replace(self.stage, licenses=licenses)
            self.assertIsNone(derive(weaker, self.rules, "conclusion"))
            self.assertFalse(verify_certificate(proof, weaker, self.rules))

    def test_source_and_basis_changes_need_transport(self):
        proof = derive(self.stage, self.rules, "conclusion")
        for context in (CertificationContext("other", "basis"), CertificationContext("source", "other")):
            other = replace(self.stage, context=context)
            self.assertFalse(verify_certificate(proof, other, self.rules))
            with self.assertRaises(CertificationError):
                self.stage.join(other)

    def test_forged_inference_and_unlicensed_zero_arity_rule_fail(self):
        forged = Certificate(self.stage, "conclusion", (("conclusion", "continue", ()),))
        self.assertFalse(verify_certificate(forged, self.stage, self.rules))
        axiom = (LicensedRule("axiom", (), "new-commitment"),)
        self.assertIsNone(derive(self.stage, axiom, "new-commitment"))
        licensed = replace(self.stage, licenses=self.stage.licenses | {"axiom"})
        self.assertIsNotNone(derive(licensed, axiom, "new-commitment"))

    def test_directedness_is_essential_for_closure_union_law(self):
        left = replace(self.stage, evidence=PartialEvidence(((3, 1),)))
        right = replace(self.stage, evidence=PartialEvidence(((101, 0),)))
        self.assertIsNone(derive(left, self.rules, "conclusion"))
        self.assertIsNone(derive(right, self.rules, "conclusion"))
        self.assertIsNotNone(derive(left.join(right), self.rules, "conclusion"))
        self.assertFalse(left.extends(right) or right.extends(left))

    def test_undefined_and_empty_source_fiber_are_distinct(self):
        sources = (PartialEvidence(((3, 0), (101, 1))), PartialEvidence(((3, 1), (101, 0))))
        positive = frozenset((sources[0],))
        self.assertIsNone(certify_finite_source(PartialEvidence(()), sources, positive))
        self.assertEqual(certify_finite_source(PartialEvidence(((3, 0),)), sources, positive), 1)
        self.assertEqual(certify_finite_source(PartialEvidence(((101, 0),)), sources, positive), 0)
        with self.assertRaises(CertificationError):
            certify_finite_source(PartialEvidence(((3, 0), (101, 0))), sources, positive)

    def test_scattered_partial_maps_and_ideal_representation(self):
        basis = all_binary_evidence((4, 500))
        ideals = finite_ideals(basis)
        self.assertEqual(len(basis), 9)
        self.assertEqual(len(ideals), 9)
        for ideal in ideals:
            maximum = next(p for p in ideal if all(p.extends(q) for q in ideal))
            self.assertEqual(ideal, frozenset(p for p in basis if maximum.extends(p)))

    def test_arbitrary_finite_all_one_support_has_opposite_future_answers(self):
        for addresses in ((), (9,), (1, 24, 700), (0, 4, 99, 104)):
            even, odd = first_zero_parity_witnesses(addresses)
            self.assertEqual((even % 2, odd % 2), (0, 1))
            self.assertTrue(all(n < min(even, odd) for n in addresses))

    def test_syntactic_finite_support_is_not_semantic_soundness(self):
        bad = (LicensedRule("bad", (observation_atom(3, 1),), "contradicts-declared-source"),)
        licensed = replace(self.stage, licenses=frozenset(("bad",)))
        proof = derive(licensed, bad, "contradicts-declared-source")
        self.assertIsNotNone(proof)
        self.assertTrue(verify_certificate(proof, licensed, bad))

    def test_exact_probe_against_independent_oracles(self):
        from scripts.swarm_x11_proof_limits_probe import run_probe
        result = run_probe()
        self.assertEqual(result["finite_stage_count"], 648)
        self.assertEqual(result["comparable_stage_pairs"], 16875)
        self.assertEqual(result["scattered_phantom_supports_with_opposite_answers"], 154)


if __name__ == "__main__":
    unittest.main()
