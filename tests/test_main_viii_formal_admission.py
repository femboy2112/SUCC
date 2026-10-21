"""Installed Main VIII authority gate: real slope admission, no mocked catalogue.

Before the coordinator admits the actual three-project build the positive gate
must fail. A research receipt is never silently promoted by this test.
"""
from copy import deepcopy
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import unittest

from observational_succ import proof_authority as pa

ROOT = Path(pa.__file__).resolve().parents[1]
SLOPES = tuple("ObservationalSUCC.PrimitiveSlope." + name for name in (
    "determinant_divisibility_int", "nat_dvd_int_cast", "determinant_divisibility",
    "reduced_pair_injective", "primitive_triple_determinant_ne_zero", "modulus_le_natAbs",
    "primitive_determinant_gap", "nonprimitive_control", "noncoprime_moduli_control"))


class MainVIIIFormalAdmission(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((ROOT / "formal/kernel_audit/admitted/kernel-attestation.json").read_text())
        self.historical = json.loads((ROOT /
            "formal/slope_rigidity/receipts/kernel-observation-39508738928.json").read_text())

    def test_nineteen_actual_declarations_include_all_nine_slopes(self):
        self.assertEqual(len(self.record["theorem_exports"]), 19)
        for name in SLOPES:
            theorem = pa.FormalTheorem.from_receipt(name, self.record)
            claim = pa.Claim("exact universal slope theorem", theorem.proposition, "C", scope="global")
            self.assertEqual(claim.discharge(theorem, receipt=self.record).status, pa.VERIFIED)
            # Rebuilding changes the source environment, not the theorem type.
            self.assertEqual(self.record["theorem_exports"][name], self.historical["theorem_exports"][name])

    def test_historical_research_observation_cannot_self_admit(self):
        self.assertEqual(self.historical["status"], "KERNEL_CHECKED_NOT_AUTHORITY_ADMITTED")
        for name in SLOPES:
            with self.assertRaises(pa.ProofAuthorityError):
                pa.FormalTheorem.from_receipt(name, self.historical)

    def test_slope_cannot_certify_endpoint_or_unrelated_proposition(self):
        theorem = pa.FormalTheorem.from_receipt(SLOPES[6], self.record)
        for proposition in ("The Riemann hypothesis is true.", "The weighted abc moment is quadratic at t=2/3.",
                            replace(theorem.proposition, type_expr="False")):
            claim = pa.Claim("unproved transport", proposition, "C", scope="global")
            self.assertEqual(claim.discharge(theorem, receipt=self.record).status, pa.INAPPLICABLE)
        forged = deepcopy(self.record)
        entry = forged["theorem_exports"][theorem.name]
        entry["type_expr"] = "False"
        entry["type_sha256"] = hashlib.sha256(b"False").hexdigest()
        with self.assertRaises(pa.ProofAuthorityError):
            pa.FormalTheorem.from_receipt(theorem.name, forged)


if __name__ == "__main__":
    unittest.main()
