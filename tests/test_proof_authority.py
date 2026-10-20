"""Proof Forge III, Part II: the four-level trusted proof-authority kernel.

Covers every required failure control -- a fake theorem name, a valid theorem
with an invalid source map, a finite Gram that must not certify a global kernel,
a wrong-quantifier transport, an alternative normalization -- plus the acceptance
criterion (metadata cannot elevate itself to authority) and the two-theorem reuse
(Schur negative-witness at Level B; Mason-Stothers -> polynomial Fermat at C/D)."""
import os
import unittest

import sympy as sp

from observational_succ.proof_authority import (
    INAPPLICABLE,
    REFUTED,
    VERIFIED,
    Claim,
    FormalTheorem,
    LocalCertificate,
    ProofAuthorityError,
    SourceRealization,
    load_receipt,
    registered_checkers,
    transport_respects_quantifiers,
)

_RECEIPT_PATH = os.path.join(os.path.dirname(__file__), "..",
                             "formal", "mathlib_bridge", "axiom_audit.json")
from observational_succ.proof_contracts import ProofContract, Quantifier

_V414 = "leanprover/lean4:v4.14.0"
_REV = "4bbdccd9e825cf9b2c5d1e5e5d6f1a1b2c3d4e5f"
_RECEIPT = {
    "build_succeeded": True,
    "toolchain": _V414,
    "manifest_rev": _REV,
    "theorems": {
        "succ_mason_stothers_charZero": {
            "axioms": ["propext", "Classical.choice", "Quot.sound"]},
        "polynomial_fermat": {
            "axioms": ["propext", "Classical.choice", "Quot.sound"]},
    },
}


def _ms_theorem(name="succ_mason_stothers_charZero"):
    return FormalTheorem(name=name, toolchain=_V414, manifest_rev=_REV,
                         allowed_axioms=("propext", "Classical.choice", "Quot.sound"))


class TestLevelB(unittest.TestCase):
    def test_negative_vector_certificate_verified(self):
        # Reuse of the exact Schur kernel: an exact v with v^T M v < 0.
        M = sp.Matrix([[1, -5000], [-5000, 24999999]])
        cert = LocalCertificate("negative_vector",
                                {"matrix": M, "vector": sp.Matrix([5000, 1])},
                                scope="finite")
        claim = Claim("M_not_psd", "M is indefinite", required_level="B", scope="finite")
        self.assertEqual(claim.discharge(cert).status, VERIFIED)

    def test_finite_schur_positivity_genuine_vs_trap(self):
        A, B, D = sp.Matrix([[1]]), sp.Matrix([[2]]), sp.Matrix([[100]])
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
        good = LocalCertificate("finite_schur_positivity",
                                {"matrix": M, "n_A": 1}, scope="finite")
        claim = Claim("block_positive", "M>=0 (finite block positivity)",
                      required_level="B", scope="finite")
        self.assertEqual(claim.discharge(good).status, VERIFIED)
        # the diag(1,-1) trap: high block not PSD -> checker fails -> REFUTED
        trap = LocalCertificate("finite_schur_positivity",
                                {"matrix": sp.Matrix([[1, 0], [0, -1]]), "n_A": 1},
                                scope="finite")
        self.assertEqual(claim.discharge(trap).status, REFUTED)

    def test_finite_schur_positivity_ignores_caller_source_flag(self):
        # A self-asserted source_form_identified flag must NOT change the MATH
        # verdict (it is simply ignored); and a Level-B cert cannot reach a
        # source/global claim regardless.
        Mbad = sp.Matrix([[1, 0], [0, -1]])   # not PSD
        cert = LocalCertificate("finite_schur_positivity",
                                {"matrix": Mbad, "n_A": 1,
                                 "source_form_identified": True}, scope="finite")
        self.assertEqual(
            Claim("x", "finite", required_level="B", scope="finite")
            .discharge(cert).status, REFUTED)              # flag can't rescue non-PSD
        Mgood = sp.Matrix([[2, 1], [1, 2]])
        cert2 = LocalCertificate("finite_schur_positivity",
                                 {"matrix": Mgood, "n_A": 1,
                                  "source_form_identified": True}, scope="finite")
        # even flagged "source", it can only discharge a FINITE Level-B claim ...
        self.assertEqual(
            Claim("x", "finite", required_level="B", scope="finite")
            .discharge(cert2).status, VERIFIED)
        # ... never a Level-D source claim (level gating)
        self.assertEqual(
            Claim("src", "source", required_level="D", scope="global")
            .discharge(cert2).status, INAPPLICABLE)

    def test_casus_irreducibilis_block_is_a_verdict_not_a_crash(self):
        # Amber #3: a rational M whose high block has irrational (casus
        # irreducibilis) eigenvalues must yield a verdict, never a raw TypeError.
        M = sp.Matrix([[sp.Rational(-2, 3), -1, sp.Rational(2, 3), -1],
                       [-1, 5, sp.Rational(7, 3), sp.Rational(-5, 3)],
                       [sp.Rational(2, 3), sp.Rational(7, 3), sp.Rational(49, 36),
                        sp.Rational(-5, 6)],
                       [-1, sp.Rational(-5, 3), sp.Rational(-5, 6),
                        sp.Rational(11, 9)]])
        cert = LocalCertificate("finite_schur_positivity",
                                {"matrix": M, "n_A": 1}, scope="finite")
        v = Claim("x", "finite", required_level="B", scope="finite").discharge(cert)
        self.assertIn(v.status, (VERIFIED, REFUTED, INAPPLICABLE, "UNKNOWN"))

    def test_unknown_checker_rejected_at_construction(self):
        with self.assertRaises(ProofAuthorityError):
            LocalCertificate("totally_made_up", {"x": 1})

    def test_float_data_rejected_by_reused_exact_guard(self):
        cert = LocalCertificate("psd_matrix",
                                {"matrix": sp.Matrix([[1.0, 0.0], [0.0, 2.0]])})
        claim = Claim("psd", "PSD", required_level="B", scope="finite")
        # the exact-input guard (quantitative_rigidity) fires inside verify
        self.assertEqual(claim.discharge(cert).status, REFUTED)


class TestFiniteGramDoesNotCertifyGlobalKernel(unittest.TestCase):
    def test_scope_mismatch_is_inapplicable(self):
        G = sp.Matrix([[2, 1], [1, 2]])          # a perfectly PSD finite Gram
        cert = LocalCertificate("finite_gram_psd", {"gram": G}, scope="finite")
        global_claim = Claim("global_kernel_psd", "K(s,t) is a PSD kernel on all R",
                             required_level="B", scope="global")
        v = global_claim.discharge(cert)
        self.assertEqual(v.status, INAPPLICABLE)       # finite positivity != global
        # ... while it DOES discharge the honest finite claim
        finite_claim = Claim("finite_gram", "this finite Gram is PSD",
                             required_level="B", scope="finite")
        self.assertEqual(finite_claim.discharge(cert).status, VERIFIED)


class TestLevelCFormalTheorem(unittest.TestCase):
    def test_valid_theorem_verified_against_receipt(self):
        thm = _ms_theorem()
        claim = Claim("mason_stothers", "polynomial abc", required_level="C",
                      scope="global")
        self.assertEqual(claim.discharge(thm, receipt=_RECEIPT).status, VERIFIED)

    def test_fake_theorem_name_rejected(self):
        fake = _ms_theorem(name="succ_proves_riemann_hypothesis")
        claim = Claim("rh", "RH", required_level="C", scope="global")
        self.assertEqual(claim.discharge(fake, receipt=_RECEIPT).status, REFUTED)

    def test_name_without_receipt_is_not_a_theorem(self):
        thm = _ms_theorem()
        claim = Claim("mason_stothers", "polynomial abc", required_level="C",
                      scope="global")
        self.assertEqual(claim.discharge(thm).status, REFUTED)  # no receipt supplied

    def test_axiom_envelope_enforced(self):
        bad_receipt = {
            "build_succeeded": True, "toolchain": _V414, "manifest_rev": _REV,
            "theorems": {"succ_mason_stothers_charZero": {"axioms": ["sorryAx"]}}}
        thm = _ms_theorem()
        claim = Claim("ms", "abc", required_level="C", scope="global")
        self.assertEqual(claim.discharge(thm, receipt=bad_receipt).status, REFUTED)


class TestLevelDSourceRealization(unittest.TestCase):
    def _real(self, source_poly):
        x = sp.Symbol("x")
        return SourceRealization(
            theorem=_ms_theorem(), math_object="theorem polys", source_object="SUCC polys",
            map_type="polynomial_identity",
            data={"gen": x, "theorem_poly": x ** 2 + 1, "source_poly": source_poly})

    def test_valid_source_realization_verified(self):
        x = sp.Symbol("x")
        claim = Claim("source_id", "the theorem is about the SUCC object",
                      required_level="D", scope="global")
        self.assertEqual(claim.discharge(self._real(x ** 2 + 1), receipt=_RECEIPT).status,
                         VERIFIED)

    def test_valid_theorem_wrong_source_map_refuted(self):
        x = sp.Symbol("x")
        claim = Claim("source_id", "the theorem is about the SUCC object",
                      required_level="D", scope="global")
        v = claim.discharge(self._real(x ** 2 + 2), receipt=_RECEIPT)
        self.assertEqual(v.status, REFUTED)   # right theorem, wrong object

    def test_level_c_does_not_imply_level_d(self):
        # A Level C theorem offered where Level D is required: not a source cert.
        claim = Claim("source_id", "source realization", required_level="D",
                      scope="global")
        v = claim.discharge(_ms_theorem(), receipt=_RECEIPT)
        self.assertEqual(v.status, INAPPLICABLE)

    def test_level_d_satisfies_level_c_requirement(self):
        x = sp.Symbol("x")
        claim = Claim("formal", "a formal theorem", required_level="C", scope="global")
        self.assertEqual(claim.discharge(self._real(x ** 2 + 1), receipt=_RECEIPT).status,
                         VERIFIED)


class TestNormalizationControl(unittest.TestCase):
    def test_alternative_normalization_does_not_certify(self):
        thm = FormalTheorem(name="succ_mason_stothers_charZero", toolchain=_V414,
                            manifest_rev=_REV,
                            allowed_axioms=("propext", "Classical.choice", "Quot.sound"),
                            normalization="A+B=C")
        claim = Claim("abc_half_density", "abc in half-density normalization",
                      required_level="C", scope="global",
                      normalization="a+b+c=0, half-density")
        self.assertEqual(claim.discharge(thm, receipt=_RECEIPT).status, INAPPLICABLE)


class TestMetadataCannotElevate(unittest.TestCase):
    def test_raw_callback_is_not_evidence(self):
        claim = Claim("x", "anything", required_level="B", scope="finite")
        self.assertEqual(claim.discharge(lambda: True).status, REFUTED)

    def test_bare_value_is_not_evidence(self):
        claim = Claim("x", "anything", required_level="B", scope="finite")
        self.assertEqual(claim.discharge("a string claiming to be a proof").status, REFUTED)

    def test_forged_duck_typed_object_is_rejected(self):
        # A hand-forged look-alike with the right attributes must NOT discharge:
        # authority is by registered artifact type, not object shape.
        class Forged:
            level = "D"
            scope = "global"
            normalization = ""

            def verify(self, **kwargs):
                return True

        claim = Claim("x", "forged source realization", required_level="D",
                      scope="global")
        self.assertEqual(claim.discharge(Forged()).status, REFUTED)


class TestReceiptAxiomHardening(unittest.TestCase):
    def _thm(self):
        return FormalTheorem(name="T", toolchain=_V414, manifest_rev=_REV,
                             allowed_axioms=("propext", "Classical.choice", "Quot.sound"))

    def test_absent_axioms_key_is_rejected(self):
        # A theorem entry with NO axioms key is UNKNOWN, not "axiom-free" -> reject.
        receipt = {"build_succeeded": True, "toolchain": _V414, "manifest_rev": _REV,
                   "theorems": {"T": {}}}
        self.assertFalse(self._thm().validate_against_receipt(receipt))

    def test_sorry_axiom_default_denied_even_if_allowed(self):
        # sorryAx must be rejected regardless of the caller's allowed set.
        ft = FormalTheorem(name="T", toolchain=_V414, manifest_rev=_REV,
                           allowed_axioms=("propext", "sorryAx"))
        receipt = {"build_succeeded": True, "toolchain": _V414, "manifest_rev": _REV,
                   "theorems": {"T": {"axioms": ["propext", "sorryAx"]}}}
        self.assertFalse(ft.validate_against_receipt(receipt))

    def test_native_decide_axiom_default_denied(self):
        ft = FormalTheorem(name="T", toolchain=_V414, manifest_rev=_REV,
                           allowed_axioms=("propext", "Lean.ofReduceBool"))
        receipt = {"build_succeeded": True, "toolchain": _V414, "manifest_rev": _REV,
                   "theorems": {"T": {"axioms": ["Lean.ofReduceBool"]}}}
        self.assertFalse(ft.validate_against_receipt(receipt))


class TestQuantifierTransport(unittest.TestCase):
    def _pointwise(self):
        return ProofContract(
            name="pointwise_bound",
            statement="forall N exists C_N : |S(N)| <= C_N",
            prefix=[Quantifier("forall", "N", "naturals"),
                    Quantifier("exists", "C", "reals", depends_on=["N"])],
            hypotheses=[], constant_dependencies={"C": ["N"]},
            finite_to_infinite="pointwise; no uniform step",
            source_authentic=False, method="per-N estimate", status="PROVED LOCAL")

    def _uniform(self):
        return ProofContract(
            name="uniform_bound",
            statement="exists C forall N : |S(N)| <= C",
            prefix=[Quantifier("exists", "C", "reals"),
                    Quantifier("forall", "N", "naturals")],
            hypotheses=[], constant_dependencies={"C": []},
            finite_to_infinite="claims uniformity",
            source_authentic=False, method="claimed uniform", status="HYPOTHESIS")

    def test_illegal_uniformization_fails(self):
        self.assertFalse(transport_respects_quantifiers(
            self._pointwise(), self._uniform(), "C", "N"))

    def test_legal_transport_when_source_already_uniform(self):
        self.assertTrue(transport_respects_quantifiers(
            self._uniform(), self._uniform(), "C", "N"))


class TestRealReceiptIntegration(unittest.TestCase):
    """End-to-end Part VII -> Part II: the ACTUAL Lean axiom-audit receipt emitted
    by the mathlib bridge build validates through the Level C consumer, using the
    real toolchain/manifest recorded in the file (not a placeholder fixture)."""

    @unittest.skipUnless(os.path.exists(_RECEIPT_PATH), "mathlib bridge receipt absent")
    def test_real_receipt_validates_all_theorems(self):
        r = load_receipt(_RECEIPT_PATH)
        self.assertTrue(r["build_succeeded"])
        allowed = ("propext", "Classical.choice", "Quot.sound")
        self.assertTrue(r["theorems"], "receipt lists no theorems")
        for name in r["theorems"]:
            ft = FormalTheorem(name=name, toolchain=r["toolchain"],
                               manifest_rev=r["manifest_rev"], allowed_axioms=allowed)
            claim = Claim(name, "mathlib bridge theorem", required_level="C",
                          scope="global")
            self.assertEqual(claim.discharge(ft, receipt=r).status, VERIFIED, name)

    @unittest.skipUnless(os.path.exists(_RECEIPT_PATH), "mathlib bridge receipt absent")
    def test_real_receipt_rejects_fabricated_name(self):
        r = load_receipt(_RECEIPT_PATH)
        allowed = ("propext", "Classical.choice", "Quot.sound")
        ft = FormalTheorem(name="succ_proves_riemann_hypothesis",
                           toolchain=r["toolchain"], manifest_rev=r["manifest_rev"],
                           allowed_axioms=allowed)
        claim = Claim("rh", "RH", required_level="C", scope="global")
        self.assertEqual(claim.discharge(ft, receipt=r).status, REFUTED)


class TestRegistry(unittest.TestCase):
    def test_builtin_checkers_present(self):
        for name in ("negative_vector", "psd_matrix", "finite_gram_psd",
                     "finite_schur_positivity"):
            self.assertIn(name, registered_checkers())


if __name__ == "__main__":
    unittest.main()
