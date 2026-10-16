from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from observational_succ.source_proof_certificate import audit_capsules, evidence_file, CapsuleError


class CapsuleTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "proof.txt").write_text("Explicit finite model, not a Lean proof.\n")
        self.c = dict(claim_id="finite", authority="EXACT_FINITE_CHECK",
                      statement="The specified finite identity holds.", source="Fin 2",
                      operations_relations="identity map", target_carrier="Fin 2",
                      observation_morphisms="identity", topology_measure="discrete counting",
                      universal_property="identity factorization", comparison_maps="identity",
                      source_identity="declared model", source_epoch=0, hypotheses=[], dependencies=[],
                      scope="FINITE_INSTANCE", conclusion_mode="INSTANCE_ONLY",
                      evidence=[evidence_file(self.root, "proof.txt", "FINITE_RECEIPT")],
                      access={x: "explicit model" for x in (
                          "permitted_observations", "constructible_witness", "oracle",
                          "probe_discrimination", "proof_theory", "execution_cost")},
                      adversarial={x: "explicit negative test" for x in (
                          "domain_tests", "negative_examples", "source_mutations", "replay")})

    def test_hash_audit_issues_no_truth_authority(self):
        r = audit_capsules([self.c], self.root)
        self.assertEqual(r["theorems_proved_by_this_audit"], [])
        self.assertIsNone(r["claims"][0]["semantic_authority_issued"])
        (self.root / "proof.txt").write_text("altered proof")
        with self.assertRaises(CapsuleError):
            audit_capsules([self.c], self.root)

    def test_no_finite_to_global_or_lean_laundering(self):
        for change in ({"scope": "UNIVERSAL"}, {"authority": "LEAN_KERNEL_PROVED"},
                       {"authority": "UNVERIFIED"}, {"authority": "PYTHON_PROVED"}):
            with self.assertRaises(CapsuleError):
                audit_capsules([dict(self.c, **change)], self.root)

    def test_missing_or_circular_premises(self):
        for deps in (["missing"], ["finite"]):
            with self.assertRaises(CapsuleError):
                audit_capsules([dict(self.c, dependencies=deps)], self.root)

    def test_conditional_retains_open_premise(self):
        unresolved = dict(self.c, claim_id="open", authority="UNVERIFIED",
                          conclusion_mode="OPEN_TARGET")
        conditional = dict(self.c, authority="PAPER_PROVED", scope="UNIVERSAL",
                           conclusion_mode="THEOREM_UNDER_HYPOTHESES", dependencies=["open"])
        with self.assertRaises(CapsuleError):
            audit_capsules([unresolved, conditional], self.root)
        conditional["hypotheses"] = ["ASSUME:open"]
        r = audit_capsules([unresolved, conditional], self.root)
        self.assertEqual(r["claims"][-1]["open_dependencies"], ["open"])
        self.assertEqual(r["claims"][-1]["retained_hypotheses"], ["ASSUME:open"])

    def test_path_escape_or_unsafe_epoch(self):
        bad = deepcopy(self.c)
        bad["evidence"][0]["path"] = "../outside.txt"
        with self.assertRaises(CapsuleError):
            audit_capsules([bad], self.root)
        with self.assertRaises(CapsuleError):
            audit_capsules([dict(self.c, source_epoch=True)], self.root)

    def test_transitive_premise_laundering_is_rejected(self):
        for authority, mode, scope in (("UNVERIFIED", "OPEN_TARGET", "UNIVERSAL"),
                                       ("REFUTED", "COUNTEREXAMPLE", "UNIVERSAL"),
                                       ("TESTED_MODEL", "INSTANCE_ONLY", "NUMERICAL_MODEL")):
            u = dict(self.c, claim_id="U", authority=authority, conclusion_mode=mode, scope=scope)
            b = dict(self.c, claim_id="B", authority="PAPER_PROVED", scope="UNIVERSAL",
                     conclusion_mode="THEOREM_UNDER_HYPOTHESES", dependencies=["U"],
                     hypotheses=["ASSUME:U"])
            consumer = dict(b, claim_id="C", dependencies=["B"], hypotheses=[])
            with self.assertRaises(CapsuleError):
                audit_capsules([u, b, consumer], self.root)
            consumer["hypotheses"] = ["ASSUME:U"]
            r = audit_capsules([u, b, consumer], self.root)
            self.assertEqual(r["claims"][-1]["open_dependencies"], ["U"])
            self.assertEqual(r["claims"][-1]["retained_hypotheses"], ["ASSUME:U"])

    def test_open_target_cannot_wear_a_proof_label(self):
        for authority in ("PAPER_PROVED", "LEAN_KERNEL_PROVED", "CLASSICAL_IMPORTED"):
            with self.assertRaises(CapsuleError):
                audit_capsules([dict(self.c, authority=authority, conclusion_mode="OPEN_TARGET")], self.root)

    def test_ordinary_hypotheses_survive_every_edge(self):
        parent = dict(self.c, claim_id="parent", authority="PAPER_PROVED", scope="UNIVERSAL",
                      conclusion_mode="THEOREM_UNDER_HYPOTHESES", hypotheses=["A is bounded"])
        child = dict(parent, claim_id="child", hypotheses=[], dependencies=["parent"])
        r = audit_capsules([parent, child], self.root)
        self.assertEqual(r["claims"][-1]["retained_hypotheses"], ["A is bounded"])


if __name__ == "__main__":
    unittest.main()
