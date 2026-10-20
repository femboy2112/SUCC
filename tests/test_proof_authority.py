"""Permanent negative controls for exact proposition-bound authority.

Synthetic success receipts used by the historical tests were themselves an
unsafe assumption. They now serve as hostile inputs, never as formal proofs.
"""
from dataclasses import FrozenInstanceError, replace
from fractions import Fraction
from pathlib import Path
import json
import unittest
import sympy as sp

from observational_succ.proof_authority import (
    Claim, FormalProposition, FormalTheorem, LocalCertificate, MatrixProposition,
    SourceRealization, ProofAuthorityError, VERIFIED, REFUTED, INAPPLICABLE,
    load_receipt, register_checker, register_source_map, registered_checkers,
    transport_respects_quantifiers,
)
from observational_succ.proof_contracts import ProofContract, Quantifier

ROOT = Path(__file__).resolve().parents[1]


class TestFiniteAuthority(unittest.TestCase):
    def test_positive_exact_psd_binding(self):
        for matrix in ([[1]], [[2, 1], [1, 2]], [[1, 1], [1, 1]]):
            cert = LocalCertificate("psd_matrix", {"matrix": matrix})
            claim = Claim("exact PSD", MatrixProposition("psd", matrix), "B")
            self.assertEqual(claim.discharge(cert).status, VERIFIED)

    def test_wrong_matrix_and_predicate_rejected(self):
        cert = LocalCertificate("psd_matrix", {"matrix": [[1]]})
        for proposition in (MatrixProposition("psd", [[-1]]),
                            MatrixProposition("not_psd", [[1]]),
                            MatrixProposition("psd", [[2]]),
                            "The Riemann hypothesis is true."):
            self.assertEqual(Claim("unrelated", proposition, "B").discharge(cert).status, INAPPLICABLE)

    def test_negative_witness_binds_exact_matrix(self):
        matrix = [[0, 1], [1, 0]]
        cert = LocalCertificate("negative_vector", {"matrix": matrix, "vector": [[1], [-1]]})
        self.assertEqual(Claim("negative", cert.proposition, "B").discharge(cert).status, VERIFIED)
        wrong = MatrixProposition("not_psd", [[0, 2], [2, 0]])
        self.assertEqual(Claim("other", wrong, "B").discharge(cert).status, INAPPLICABLE)
        bad = LocalCertificate("negative_vector", {"matrix": [[1]], "vector": [[1]]})
        self.assertEqual(Claim("false witness", bad.proposition, "B").discharge(bad).status, REFUTED)

    def test_bad_psd_certificate_recomputed(self):
        cert = LocalCertificate("psd_matrix", {"matrix": [[1, 2], [2, 1]]})
        self.assertEqual(Claim("bad PSD", cert.proposition, "B").discharge(cert).status, REFUTED)

    def test_exact_gram_and_schur(self):
        for cert in (LocalCertificate("finite_gram_psd", {"gram": [[1, 1], [1, 1]]}),
                     LocalCertificate("finite_schur_positivity", {"matrix": [[2, 1], [1, 2]], "n_A": 1})):
            self.assertEqual(Claim("finite", cert.proposition, "B").discharge(cert).status, VERIFIED)
            self.assertEqual(Claim("global", cert.proposition, "B", scope="global").discharge(cert).status, INAPPLICABLE)

    def test_global_self_label_rejected(self):
        with self.assertRaises(ProofAuthorityError):
            LocalCertificate("psd_matrix", {"matrix": [[1]]}, scope="global")

    def test_immutable_deep_snapshot(self):
        matrix = [[1]]
        data = {"matrix": matrix}
        cert = LocalCertificate("psd_matrix", data)
        claim = Claim("PSD", cert.proposition, "B")
        matrix[0][0] = -1
        self.assertEqual(claim.discharge(cert).status, VERIFIED)
        with self.assertRaises(TypeError):
            cert.data["matrix"] = ((-1,),)
        with self.assertRaises(FrozenInstanceError):
            claim.statement = "RH"

    def test_closed_registry_and_subclass(self):
        self.assertIn("psd_matrix", registered_checkers())
        for register in (register_checker, register_source_map):
            with self.assertRaises(ProofAuthorityError):
                register("caller", lambda *_: True)
        class Forged(LocalCertificate):
            def verify(self):
                return True
        forged = Forged("psd_matrix", {"matrix": [[-1]]})
        self.assertEqual(Claim("forgery", forged.proposition, "B").discharge(forged).status, REFUTED)
        self.assertEqual(Claim("callback", "RH", "C").discharge(lambda: True).status, REFUTED)

    def test_rational_domain_and_partition_guards(self):
        for entry in (True, 1.0, "1", sp.sqrt(2)):
            with self.assertRaises(ProofAuthorityError):
                LocalCertificate("psd_matrix", {"matrix": [[entry]]})
        cert = LocalCertificate("psd_matrix", {"matrix": [[Fraction(1, 3)]]})
        self.assertTrue(cert.verify())
        for size in (True, 1.0, Fraction(3, 2), 0, 2):
            with self.assertRaises(ProofAuthorityError):
                LocalCertificate("finite_schur_positivity", {"matrix": [[1, 0], [0, 1]], "n_A": size})
        with self.assertRaises(ProofAuthorityError):
            LocalCertificate("psd_matrix", {"matrix": [[1, 2], [0, 1]]})

    def test_normalization_and_level(self):
        cert = LocalCertificate("psd_matrix", {"matrix": [[1]]}, normalization="primitive")
        self.assertEqual(Claim("norm", cert.proposition, "B", normalization="derivative").discharge(cert).status, INAPPLICABLE)
        self.assertEqual(Claim("source", cert.proposition, "D").discharge(cert).status, INAPPLICABLE)


class TestFormalBoundary(unittest.TestCase):
    def setUp(self):
        self.receipt = load_receipt(ROOT / "formal/mathlib_bridge/axiom_audit.json")
        self.theorem = FormalTheorem("polynomial_fermat", self.receipt["toolchain"], self.receipt["manifest_rev"])

    def test_real_historical_receipt_cannot_certify_RH(self):
        claim = Claim("RH", "The Riemann hypothesis is true.", "C", scope="global")
        self.assertEqual(claim.discharge(self.theorem, receipt=self.receipt).status, INAPPLICABLE)

    def test_historical_receipt_has_no_build_authentication(self):
        self.assertFalse(self.theorem.validate_against_receipt(self.receipt))
        with self.assertRaises(ProofAuthorityError):
            self.theorem.verify(receipt=self.receipt)
        with self.assertRaises(ProofAuthorityError):
            FormalTheorem.from_receipt("polynomial_fermat", self.receipt)

    def test_forged_success_json_is_rejected(self):
        forged = {"schema": "succ.lean.kernel.v1", "build_succeeded": True,
                  "toolchain": self.theorem.toolchain, "manifest_rev": self.theorem.manifest_rev,
                  "source_hashes": {"README.md": "0" * 64}, "environment_sha256": "0" * 64,
                  "theorem_exports": {"polynomial_fermat": {"type_expr": "True", "axioms": []}}}
        ref = replace(self.theorem, type_expr="True", environment_sha256="0" * 64)
        self.assertEqual(Claim("fake", ref.proposition, "C", scope="global").discharge(ref, receipt=forged).status, REFUTED)

    def test_formal_reference_binds_every_parameter(self):
        ref = replace(self.theorem, type_expr="forall n, n = n", environment_sha256="a" * 64)
        for prop in (replace(ref.proposition, name="other"),
                     replace(ref.proposition, type_expr="False"),
                     replace(ref.proposition, environment_sha256="b" * 64),
                     replace(ref.proposition, manifest_rev="other"),
                     replace(ref.proposition, toolchain="other")):
            self.assertEqual(Claim("wrong theorem", prop, "C", scope="global").discharge(ref, receipt=self.receipt).status, INAPPLICABLE)

    def test_arbitrary_equal_polynomials_do_not_authenticate_source(self):
        source = SourceRealization(self.theorem, "theorem", "Weil source", "polynomial_identity",
                                   {"gen": sp.Symbol("x"), "theorem_poly": 1, "source_poly": 1})
        self.assertEqual(Claim("source", self.theorem.proposition, "D", scope="global").discharge(source, receipt=self.receipt).status, INAPPLICABLE)
        with self.assertRaises(ProofAuthorityError):
            source.verify(receipt=self.receipt)


class TestQuantifierBoundary(unittest.TestCase):
    def test_pointwise_cannot_be_uniformized(self):
        base = dict(name="bound", statement="...", hypotheses=[], finite_to_infinite="none",
                    source_authentic=False, method="test", status="UNVERIFIED")
        pointwise = ProofContract(prefix=[Quantifier("forall", "N", "N"), Quantifier("exists", "C", "R", ("N",))],
                                  constant_dependencies={"C": ["N"]}, **base)
        uniform = ProofContract(prefix=[Quantifier("exists", "C", "R"), Quantifier("forall", "N", "N")],
                                constant_dependencies={"C": []}, **base)
        self.assertFalse(transport_respects_quantifiers(pointwise, uniform, "C", "N"))
        self.assertTrue(transport_respects_quantifiers(uniform, uniform, "C", "N"))


if __name__ == "__main__":
    unittest.main()
