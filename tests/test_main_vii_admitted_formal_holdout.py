"""Independent holdout against the actually admitted Lean build.

This test does not register checkers, patch a catalogue, or manufacture a
positive receipt. Missing real admission fails this gate rather than skipping.
"""
from copy import deepcopy
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import unittest

from observational_succ import proof_authority as pa


class AdmittedFormalHoldout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(pa.__file__).resolve().parents[1]
        cls.receipt = json.loads((cls.root/
            "formal/kernel_audit/admitted/kernel-attestation.json").read_text())
        cls.fermat = pa.FormalTheorem.from_receipt(
            "SUCC.MasonStothersBridge.polynomial_fermat",cls.receipt)
        cls.mason = pa.FormalTheorem.from_receipt(
            "SUCC.MasonStothersBridge.succ_mason_stothers_charZero",cls.receipt)

    def claim(self,proposition):
        return pa.Claim("independent actual-kernel holdout",proposition,"C",scope="global")

    def test_admitted_exact_polynomial_and_schur_propositions(self):
        self.assertGreaterEqual(len(self.receipt["theorem_exports"]),10)
        for name,entry in self.receipt["theorem_exports"].items():
            theorem = pa.FormalTheorem.from_receipt(name,self.receipt)
            self.assertEqual(self.claim(theorem.proposition).discharge(
                theorem,receipt=self.receipt).status,pa.VERIFIED,name)
            self.assertEqual(hashlib.sha256(entry["type_expr"].encode()).hexdigest(),
                             entry["type_sha256"])
            self.assertTrue(set(entry["axioms"]) <= {"propext","Classical.choice","Quot.sound"})

    def test_actual_receipt_cannot_certify_rh_or_exchange_theorems(self):
        self.assertNotEqual(self.fermat.proposition,self.mason.proposition)
        for theorem in (self.fermat,self.mason):
            verdict = self.claim("The Riemann hypothesis is true.").discharge(
                theorem,receipt=self.receipt)
            self.assertNotEqual(verdict.status,pa.VERIFIED)
        for claim_theorem,evidence in ((self.mason,self.fermat),(self.fermat,self.mason)):
            verdict = self.claim(claim_theorem.proposition).discharge(evidence,receipt=self.receipt)
            self.assertEqual(verdict.status,pa.INAPPLICABLE)

    def test_claim_cannot_change_the_proved_type(self):
        altered = replace(self.fermat.proposition,type_expr="The Riemann hypothesis is true.")
        self.assertEqual(self.claim(altered).discharge(self.fermat,
            receipt=self.receipt).status,pa.INAPPLICABLE)
        # Even if the forged evidence and claim agree with each other, their
        # proposition must still agree with the actual kernel's declaration.
        for evidence in (replace(self.fermat,type_expr="False"),
                         replace(self.fermat,name=self.mason.name),
                         replace(self.fermat,toolchain="forged"),
                         replace(self.fermat,manifest_rev="0"*40),
                         replace(self.fermat,environment_sha256="0"*64)):
            verdict = self.claim(evidence.proposition).discharge(evidence,receipt=self.receipt)
            self.assertNotEqual(verdict.status,pa.VERIFIED)

    def test_unqualified_name_is_not_a_canonical_reference(self):
        with self.assertRaises(pa.ProofAuthorityError):
            pa.FormalTheorem.from_receipt("polynomial_fermat",self.receipt)

    def test_changed_receipt_data_does_not_inherit_admission(self):
        for field,value in (("type_expr","False"),("axioms",["sorryAx"]),
                            ("universe_parameters",["unproved_new_universe"])):
            receipt = deepcopy(self.receipt)
            receipt["theorem_exports"][self.fermat.name][field] = value
            if field == "type_expr":
                receipt["theorem_exports"][self.fermat.name]["type_sha256"] = \
                    hashlib.sha256(value.encode()).hexdigest()
            with self.assertRaises(pa.ProofAuthorityError):
                pa.FormalTheorem.from_receipt(self.fermat.name,receipt)
        receipt = deepcopy(self.receipt)
        receipt["build"]["git_commit"] = "0"*40
        with self.assertRaises(pa.ProofAuthorityError):
            pa.FormalTheorem.from_receipt(self.fermat.name,receipt)

    def test_all_checked_source_hashes_match_actual_installed_files(self):
        for relative,expected in self.receipt["source_hashes"].items():
            path = (self.root/relative).resolve()
            self.assertTrue(path.is_relative_to(self.root))
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),expected,relative)


if __name__ == "__main__":
    unittest.main()
