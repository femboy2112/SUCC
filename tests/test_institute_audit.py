from copy import deepcopy
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import unittest

from observational_succ.institute_audit import audit_registry
from observational_succ.source_proof_certificate import CapsuleError, evidence_file


class InstituteAuditTests(unittest.TestCase):
    def setUp(self):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        def git(*args):
            return subprocess.check_output(["git", *args], cwd=self.root,
                                           stderr=subprocess.DEVNULL, text=True).strip()
        git("init", "--quiet")
        (self.root/"proof.txt").write_text("Test fixture only. This is not a proof.\n")
        (self.root/"lean-toolchain").write_text("leanprover/lean4:v4.14.0\n")
        git("add", ".")
        git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
            "commit", "--quiet", "-m", "fixture")
        c = dict(claim_id="A", authority="PAPER_PROVED", statement="Fixture statement",
                 source="S", operations_relations="f", target_carrier="C",
                 observation_morphisms="q", topology_measure="discrete",
                 universal_property="factorization", comparison_maps="identity",
                 source_identity="declared fixture", source_epoch=0,
                 hypotheses=["H"], dependencies=[], scope="UNIVERSAL",
                 conclusion_mode="THEOREM_UNDER_HYPOTHESES",
                 evidence=[evidence_file(self.root, "proof.txt", "PAPER_PROOF")],
                 access={k:"fixture" for k in ("permitted_observations", "constructible_witness",
                         "oracle", "probe_discrimination", "proof_theory", "execution_cost")},
                 adversarial={k:"fixture" for k in ("domain_tests", "negative_examples",
                               "source_mutations", "replay")},
                 signature=dict(source="S", carrier="C", topology="discrete"),
                 quantifiers="all fixture objects", prior_art="fixture", novelty="none",
                 next_discriminator="mutation", independent_check="fixture", proof_debt=[],
                 git_sources=[dict(commit=git("rev-parse", "HEAD"), path="proof.txt",
                                   blob=git("rev-parse", "HEAD:proof.txt"))])
        self.registry = dict(schema="SUCC_INSTITUTE_v1", claims=[c], transports=[])
        self.c = c

    def audit(self):
        return audit_registry(self.registry, self.root)

    def child(self):
        c = deepcopy(self.c)
        c.update(claim_id="B", dependencies=["A"])
        self.registry["claims"].append(c)
        return c

    def test_audit_does_not_prove_fixture(self):
        result = self.audit()
        self.assertEqual(result["theorems_proved_by_this_audit"], [])
        self.assertFalse(result["physical_source_authentication"])

    def test_missing_inherited_hypothesis_rejected(self):
        self.child()["hypotheses"] = []
        with self.assertRaisesRegex(CapsuleError, "hypothesis laundering"):
            self.audit()

    def test_each_type_dimension_requires_comparison(self):
        child = self.child()
        for field in ("source", "carrier", "topology"):
            original = child["signature"][field]
            child["signature"][field] = "changed"
            with self.assertRaisesRegex(CapsuleError, "comparison map"):
                self.audit()
            child["signature"][field] = original

    def test_explicit_reviewed_transport_and_drift(self):
        c = self.child()
        c["signature"]["topology"] = "completion"
        edge = dict(**{"from":"A", "to":"B"}, input=deepcopy(self.c["signature"]),
                    output=deepcopy(c["signature"]), authority="PAPER_PROVED",
                    obligation="continuity and density", evidence=c["evidence"][0])
        self.registry["transports"].append(edge)
        self.audit()
        edge["output"]["topology"] = "weak completion"
        with self.assertRaisesRegex(CapsuleError, "signature drift"):
            self.audit()

    def test_wrong_git_blob_and_missing_commit(self):
        source = self.c["git_sources"][0]
        old = source["blob"]
        source["blob"] = "0"*40
        with self.assertRaisesRegex(CapsuleError, "identity mismatch"):
            self.audit()
        source["blob"] = old
        source["commit"] = "0"*40
        with self.assertRaisesRegex(CapsuleError, "Missing pinned"):
            self.audit()

    def test_no_finite_to_infinite_promotion(self):
        self.c["authority"] = "EXACT_FINITE_CHECK"
        self.c["conclusion_mode"] = "INSTANCE_ONLY"
        with self.assertRaises(CapsuleError):
            self.audit()

    def test_tree_hash_cannot_impersonate_source_commit(self):
        source = self.c["git_sources"][0]
        source["commit"] = subprocess.check_output(
            ["git", "rev-parse", "HEAD^{tree}"], cwd=self.root, text=True).strip()
        with self.assertRaisesRegex(CapsuleError, "commit object"):
            self.audit()

    def test_conditional_debt_must_be_explicit(self):
        self.c.update(authority="UNVERIFIED", conclusion_mode="OPEN_TARGET")
        child = self.child()
        child.update(authority="PAPER_PROVED", conclusion_mode="THEOREM_UNDER_HYPOTHESES",
                     hypotheses=["H", "ASSUME:A"])
        with self.assertRaisesRegex(CapsuleError, "proof debt"):
            self.audit()
        child["proof_debt"] = ["A"]
        self.audit()

    def test_stale_ci(self):
        self.c["ci"] = dict(checked_head="a"*40, claim_head="b"*40, conclusion="success")
        with self.assertRaisesRegex(CapsuleError, "Stale"):
            self.audit()

    def kernel_fixture(self):
        # Forged by design: demonstrates that integrity does not attest execution.
        # The production CI runs the fixed compiler separately.
        (self.root/"Proof.lean").write_text("theorem fixture : True := True.intro\n")
        src = evidence_file(self.root, "Proof.lean", "LEAN_SOURCE")
        ax = dict(toolchain="leanprover/lean4:v4.14.0", declarations={"fixture":[]})
        receipt = dict(ax, source_sha256=src["sha256"], exit_code=0, negative_control_exit_code=1)
        (self.root/"axioms.json").write_text(json.dumps(ax))
        (self.root/"receipt.json").write_text(json.dumps(receipt))
        self.c.update(authority="LEAN_KERNEL_PROVED", kernel_declarations=["fixture"],
                      evidence=[src, evidence_file(self.root, "axioms.json", "AXIOM_MANIFEST"),
                                evidence_file(self.root, "receipt.json", "LEAN_RECEIPT")])

    def test_rehashed_source_cannot_reuse_stale_execution(self):
        self.kernel_fixture()
        self.audit()
        (self.root/"Proof.lean").write_text("theorem fixture : False := by sorry\n")
        self.c["evidence"][0] = evidence_file(self.root, "Proof.lean", "LEAN_SOURCE")
        with self.assertRaisesRegex(CapsuleError, "Stale Lean"):
            self.audit()

    def test_kernel_cannot_import_paper_authority(self):
        paper = deepcopy(self.c)
        paper["claim_id"] = "paper"
        self.kernel_fixture()
        self.c["dependencies"] = ["paper"]
        self.registry["claims"].append(paper)
        with self.assertRaisesRegex(CapsuleError, "kernel authority"):
            self.audit()


if __name__ == "__main__":
    unittest.main()
