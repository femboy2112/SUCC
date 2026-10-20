"""Part VIII: witness-carrying proof contracts actually carry authority.

These tests wire the new proof_contracts machinery to a REAL theorem (the finite
Schur theorem from quantitative_rigidity) and to a REAL invalid transport (Gemini
1.1), demonstrating that (a) a certificate must re-verify by exact recomputation,
(b) a bare source-authenticity boolean is rejected, and (c) an invalid transport is
rejected rather than asserted.
"""
import random
import unittest

import sympy as sp

from observational_succ.proof_contracts import (
    CarryingContract,
    CheckedCertificate,
    ProofContract,
    ProofContractError,
    ProofTransport,
    Quantifier,
    SourceRealizationWitness,
    TheoremReference,
    UndischargedAssumption,
)
from observational_succ.quantitative_rigidity import (
    Rat,
    conservative_surrogate,
    finite_schur_certificate,
    is_positive_definite,
    is_positive_semidefinite,
    schur_complement,
)


def _random_pd(n, rng):
    """A random exact PD matrix: L L^T + I with small-rational L."""
    L = sp.Matrix(n, n, lambda i, j: Rat(rng.randint(-2, 2)))
    return L * L.T + sp.eye(n)


def _finite_schur_equivalence_corpus(trials=40, seed=20261020):
    """Recompute, exactly, the finite Schur equivalence M>=0 <=> (A-BD^{-1}B^T)>=0
    on a seeded corpus with D>0. Returns True iff it holds on every sample."""
    rng = random.Random(seed)
    for _ in range(trials):
        nA = rng.randint(1, 2)
        nD = rng.randint(1, 2)
        A = sp.Matrix(nA, nA, lambda i, j: Rat(rng.randint(-2, 2)))
        A = (A + A.T) / 2
        B = sp.Matrix(nA, nD, lambda i, j: Rat(rng.randint(-2, 2)))
        D = _random_pd(nD, rng)
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
        cert = finite_schur_certificate(M, nA)
        if not cert.equivalence_holds:
            return (False, M.tolist())          # a counterexample would surface here
    return True


class TestCheckedCertificate(unittest.TestCase):
    def test_finite_schur_certificate_reverifies(self):
        cert = CheckedCertificate(
            name="finite_schur_equivalence",
            check=_finite_schur_equivalence_corpus,
            description="M>=0 <=> Schur complement >=0 on a seeded exact corpus (D>0)",
        )
        self.assertTrue(cert.verify())

    def test_truthy_but_not_True_is_rejected(self):
        # a check that returns a truthy non-True value must NOT pass as proof
        bad = CheckedCertificate(name="sloppy", check=lambda: [1, 2, 3])
        with self.assertRaises(ProofContractError):
            bad.verify()
        bad2 = CheckedCertificate(name="sloppy2", check=lambda: 1)  # int 1, not True
        with self.assertRaises(ProofContractError):
            bad2.verify()


class TestSourceRealizationWitness(unittest.TestCase):
    def test_bare_boolean_authenticity_rejected(self):
        w = SourceRealizationWitness(object_name="fake_weil_form", authentic=True)
        with self.assertRaises(ProofContractError):
            w.verify()   # authentic=True with no identification map -> rejected

    def test_authenticity_with_verifying_identification_ok(self):
        w = SourceRealizationWitness(
            object_name="genuine_source",
            authentic=True,
            identification=lambda: True,    # a real identification that recomputes True
        )
        self.assertTrue(w.verify())

    def test_synthetic_proxy_ok_when_not_claiming_authenticity(self):
        w = SourceRealizationWitness(object_name="aux_gram", authentic=False,
                                     note="synthetic positive covariance, not the Weil form")
        self.assertTrue(w.verify())


class TestInvalidTransportRejected(unittest.TestCase):
    def test_restricted_coercivity_transport_is_rejected(self):
        # Gemini 1.1 as a transport: "restricted-coercivity surrogate PSD" =>
        # "inverse-response (true Schur) PSD". On the 1.1 witness the premise holds
        # but the conclusion fails, so the implication is FALSE and must be rejected.
        A = sp.Matrix([[2]])
        B = sp.Matrix([[1, 0]])
        D = sp.Matrix([[1, Rat(9, 10)], [Rat(9, 10), 1]])
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))

        def implication_holds():
            premise = is_positive_semidefinite(conservative_surrogate(M, 1, kappa=1))
            conclusion = is_positive_semidefinite(schur_complement(M, 1))
            return (not premise) or conclusion   # premise => conclusion

        bad_transport = ProofTransport(
            source="restricted_coercivity_surrogate_PSD",
            target="inverse_response_PSD",
            witness_check=implication_holds,
        )
        with self.assertRaises(ProofContractError):
            bad_transport.verify()

    def test_valid_transport_accepted(self):
        # a genuinely valid transport: true Schur PSD => M PSD on a PD-D example
        A = sp.Matrix([[2]])
        B = sp.Matrix([[1, 1]])
        D = 2 * sp.eye(2)
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))

        def implication_holds():
            premise = is_positive_semidefinite(schur_complement(M, 1))
            conclusion = is_positive_semidefinite(M)
            return (not premise) or conclusion

        good = ProofTransport(source="schur_PSD", target="M_PSD",
                              witness_check=implication_holds)
        self.assertTrue(good.verify())


class TestCarryingContract(unittest.TestCase):
    def test_classical_needs_backing(self):
        contract = ProofContract(
            name="finite_schur_theorem",
            statement="M=[[A,B],[B^T,D]], D>0: M>=0 <=> A-BD^{-1}B^T>=0",
            prefix=[Quantifier("forall", "M", "sym block matrices with D>0")],
            hypotheses=["D positive definite", "M symmetric"],
            constant_dependencies={},
            finite_to_infinite="finite dimensional; no finite->infinite step",
            source_authentic=False,
            method="exact Schur complement + square completion",
            status="CLASSICAL",
        )
        # CLASSICAL with NO backing -> rejected
        with self.assertRaises(ProofContractError):
            CarryingContract(contract=contract)
        # CLASSICAL with a checked certificate -> accepted and verifies
        carrying = CarryingContract(
            contract=contract,
            certificates=[CheckedCertificate("finite_schur_equivalence",
                                             _finite_schur_equivalence_corpus)],
            theorem_refs=[TheoremReference(
                name="Schur complement theorem",
                system="classical (Haynsworth); exact sympy oracle in-repo",
            )],
            undischarged=[],
        )
        rec = carrying.verify()
        self.assertIn("finite_schur_equivalence", rec["certificates_verified"])
        self.assertEqual(rec["status"], "CLASSICAL")

    def test_source_authentic_requires_witness(self):
        contract = ProofContract(
            name="bogus_source_claim",
            statement="this form IS the completed signed Weil form",
            prefix=[Quantifier("forall", "f", "test functions")],
            hypotheses=[],
            constant_dependencies={},
            finite_to_infinite="n/a",
            source_authentic=True,              # claims authenticity ...
            method="assertion",
            status="HYPOTHESIS",
        )
        with self.assertRaises(ProofContractError):
            CarryingContract(contract=contract)  # ... but no SourceRealizationWitness

    def test_theorem_reference_axiom_audit(self):
        ref = TheoremReference(
            name="Polynomial.abc", system="mathlib4",
            axioms=("propext", "Classical.choice", "Quot.sound"),
        )
        self.assertTrue(ref.uses_only(["propext", "Classical.choice", "Quot.sound"]))
        self.assertFalse(ref.uses_only(["propext", "Quot.sound"]))  # choice present


if __name__ == "__main__":
    unittest.main()
