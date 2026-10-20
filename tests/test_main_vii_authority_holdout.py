"""A separately authored data-boundary holdout for proposition-bound authority.

No catalogue or checker registration is changed. This is not an adversarial
Python-code sandbox test; monkeypatching installed trusted code is out of scope.
"""
from dataclasses import FrozenInstanceError
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import unittest

from observational_succ import proof_authority as pa


class AuthorityHoldout(unittest.TestCase):
    def claim(self, proposition):
        return pa.Claim("independent holdout",proposition,"B",scope="finite")

    def test_exact_two_by_two_minors_oracle(self):
        # Independent necessary-and-sufficient 2x2 principal-minor criterion.
        for a,b,d in product(range(-2,3),repeat=3):
            matrix = [[a,b],[b,d]]
            expected = a >= 0 and d >= 0 and a*d-b*b >= 0
            certificate = pa.LocalCertificate("psd_matrix",{"matrix":matrix})
            verdict = self.claim(pa.MatrixProposition("psd",matrix)).discharge(certificate)
            self.assertEqual(verdict.status == pa.VERIFIED,expected,(matrix,verdict))

    def test_matrix_and_predicate_are_part_of_the_proposition(self):
        certificate = pa.LocalCertificate("psd_matrix",{"matrix":[[1]]})
        for proposition in ("The Riemann hypothesis is true.",
                            pa.MatrixProposition("psd",[[-1]]),
                            pa.MatrixProposition("psd",[[1,0],[0,1]]),
                            pa.MatrixProposition("not_psd",[[1]])):
            self.assertNotEqual(self.claim(proposition).discharge(certificate).status,pa.VERIFIED)
        self.assertEqual(self.claim(certificate.proposition).discharge(certificate).status,pa.VERIFIED)

    def test_negative_witness_cannot_move_between_matrices(self):
        certificate = pa.LocalCertificate("negative_vector",{
            "matrix":[[1,2],[2,1]],"vector":[[1],[-1]]})
        self.assertEqual(self.claim(certificate.proposition).discharge(certificate).status,pa.VERIFIED)
        for matrix in ([[1]],[[1,0],[0,1]],[[2,2],[2,2]]):
            verdict = self.claim(pa.MatrixProposition("not_psd",matrix)).discharge(certificate)
            self.assertNotEqual(verdict.status,pa.VERIFIED)

    def test_input_mutation_does_not_move_the_certificate(self):
        original = [[1]]
        data = {"matrix":original}
        certificate = pa.LocalCertificate("psd_matrix",data)
        original[0][0] = -1
        data["matrix"] = [[-2]]
        self.assertEqual(certificate.proposition,pa.MatrixProposition("psd",[[1]]))
        self.assertEqual(self.claim(certificate.proposition).discharge(certificate).status,pa.VERIFIED)
        with self.assertRaises(TypeError):
            certificate.data["matrix"] = ((-1,),)
        with self.assertRaises(FrozenInstanceError):
            certificate.scope = "global"

    def test_rational_data_domain_and_scope(self):
        for value in (True,False,1.0,"1",float("nan")):
            with self.assertRaises(pa.ProofAuthorityError):
                pa.LocalCertificate("psd_matrix",{"matrix":[[value]]})
        certificate = pa.LocalCertificate("psd_matrix",{"matrix":[[Fraction(1,3)]]})
        self.assertEqual(self.claim(certificate.proposition).discharge(certificate).status,pa.VERIFIED)
        with self.assertRaises(pa.ProofAuthorityError):
            pa.LocalCertificate("psd_matrix",{"matrix":[[1]]},scope="global")

    def test_subclass_cannot_override_the_installed_verifier(self):
        class Fake(pa.LocalCertificate):
            def verify(self):
                return True
        forged = Fake("psd_matrix",{"matrix":[[-1]]})
        self.assertNotEqual(self.claim(forged.proposition).discharge(forged).status,pa.VERIFIED)

    def test_forged_formal_json_and_unrelated_english_claim(self):
        theorem = pa.FormalTheorem("polynomial_fermat","fake-toolchain","fake-revision")
        receipt = {"build_succeeded":True,"toolchain":"fake-toolchain",
                   "mathlib_rev":"fake-revision","manifest_rev":"fake-revision",
                   "theorems":{"polynomial_fermat":{"axioms":[]}}}
        for proposition in ("The Riemann hypothesis is true.",theorem.proposition):
            claim = pa.Claim("formal holdout",proposition,"C",scope="global")
            self.assertNotEqual(claim.discharge(theorem,receipt=receipt).status,pa.VERIFIED)
        with self.assertRaises(pa.ProofAuthorityError):
            pa.FormalTheorem.from_receipt("polynomial_fermat",receipt)

    def test_actual_historical_receipt_cannot_authorize_rh(self):
        # This is the real archived receipt, not a synthetic successful JSON.
        root = Path(pa.__file__).resolve().parents[1]
        receipt = json.loads((root/"formal/mathlib_bridge/axiom_audit.json").read_text())
        theorem = pa.FormalTheorem("polynomial_fermat",receipt["toolchain"],
                                  receipt["manifest_rev"])
        claim = pa.Claim("mandatory unrelated theorem control",
                         "The Riemann hypothesis is true.","C",scope="global")
        self.assertNotEqual(claim.discharge(theorem,receipt=receipt).status,pa.VERIFIED)

    def test_registration_is_closed_to_caller_callbacks(self):
        for register in (pa.register_checker,pa.register_source_map):
            with self.assertRaises(pa.ProofAuthorityError):
                register("adversary",lambda _data: True)


if __name__ == "__main__":
    unittest.main()
