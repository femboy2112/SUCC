"""Historical F01-F04 are negative controls, not assertions that bugs persist."""
from dataclasses import FrozenInstanceError
import unittest
from observational_succ.proof_contracts import (
    CarryingContract, CheckedCertificate, ProofContract, ProofContractError,
    Quantifier, SourceRealizationWitness, TheoremReference,
)


def contract(**updates):
    args = dict(name="research", statement="RH", prefix=[], hypotheses=[],
                constant_dependencies={}, finite_to_infinite="none supplied",
                source_authentic=False, method="metadata", status="UNVERIFIED")
    args.update(updates)
    return ProofContract(**args)


class TestLegacyAuthorityBoundaries(unittest.TestCase):
    def test_contradictory_source_flags_rejected(self):
        with self.assertRaises(ProofContractError):
            CarryingContract(contract(source_authentic=True), source_witness=
                             SourceRealizationWitness("source", authentic=False))

    def test_contract_status_cannot_be_mutated(self):
        c = contract()
        with self.assertRaises(FrozenInstanceError):
            c.status = "PROVED LOCAL"

    def test_nested_metadata_is_snapshotted(self):
        dependencies = {"C": ["N"]}
        prefix = [Quantifier("forall", "N", "N"), Quantifier("exists", "C", "R", ["N"])]
        c = contract(prefix=prefix, constant_dependencies=dependencies)
        prefix.clear()
        dependencies["C"].clear()
        self.assertFalse(c.is_uniform_in("C", "N"))
        self.assertEqual(c.constant_dependencies["C"], ("N",))
        with self.assertRaises(TypeError):
            c.constant_dependencies["C"] = ()

    def test_conflicting_dependencies_and_duplicate_names_rejected(self):
        for prefix, dependencies in (
            ([Quantifier("forall", "N", "N"), Quantifier("exists", "C", "R", ["N"])], {"C": []}),
            ([Quantifier("exists", "C", "R"), Quantifier("forall", "N", "N")], {"C": ["N"]}),
            ([Quantifier("forall", "N", "N"), Quantifier("forall", "N", "N")], {}),
        ):
            with self.assertRaises(ProofContractError):
                contract(prefix=prefix, constant_dependencies=dependencies)

    def test_unrelated_theorem_reference_is_metadata_only(self):
        bundle = CarryingContract(contract(status="PROVED LOCAL"),
                                  theorem_refs=[TheoremReference("Polynomial.abc", "mathlib")])
        record = bundle.verify()
        self.assertEqual(record["status"], "UNVERIFIED")
        self.assertEqual(record["claimed_status"], "PROVED LOCAL")
        self.assertEqual(record["authority"], "NON_AUTHORITATIVE_RESEARCH_METADATA")
        self.assertFalse(record["source_authentic"])

    def test_lambda_true_diagnostic_never_proves_RH(self):
        bundle = CarryingContract(contract(status="PROVED LOCAL"),
                                  certificates=[CheckedCertificate("true", lambda: True)])
        self.assertEqual(bundle.verify()["status"], "UNVERIFIED")

    def test_ducktyped_source_verifier_rejected(self):
        class Pretender:
            def verify(self, **kwargs):
                return True
        witness = SourceRealizationWitness("original source", authentic=True, realization=Pretender())
        with self.assertRaises(ProofContractError):
            witness.verify()

    def test_research_record_separates_claim_from_authority(self):
        record = contract(status="CLASSICAL", source_authentic=True).as_record()
        self.assertEqual(record["status"], "UNVERIFIED")
        self.assertEqual(record["claimed_status"], "CLASSICAL")
        self.assertFalse(record["source_authentic"])
        self.assertTrue(record["claimed_source_authentic"])


if __name__ == "__main__":
    unittest.main()
