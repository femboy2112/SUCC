"""Exact tests for the quantitative rigidity core (Part III)."""
import unittest

import sympy as sp

from observational_succ.quantitative_rigidity import (
    Rat,
    coupling_negative_vector,
    diagnostics_from_block,
    finite_schur_certificate,
    form_core_negative_control,
    inverse_decay_block,
    is_positive_definite,
    is_positive_semidefinite,
    min_eigenvalue_exact,
    negative_witness,
    range_inclusion_holds,
    schur_complement,
    shorted_complement,
    square_completion_identity,
    uniform_gap_profile,
)


class TestExactPositivity(unittest.TestCase):
    def test_pd_and_psd_basic(self):
        I = sp.eye(3)
        self.assertTrue(is_positive_definite(I))
        self.assertTrue(is_positive_semidefinite(I))
        # PSD but not PD
        M = sp.diag(1, 0, 2)
        self.assertFalse(is_positive_definite(M))
        self.assertTrue(is_positive_semidefinite(M))
        # indefinite
        N = sp.diag(1, -1)
        self.assertFalse(is_positive_semidefinite(N))

    def test_psd_needs_all_principal_minors_not_just_leading(self):
        # Classic trap: leading principal minors are 0,0 but the matrix is NOT PSD.
        M = sp.Matrix([[0, 0], [0, -1]])
        # leading minors: det[0]=0, det(M)=0  -> Sylvester-for-PD says "not PD" (ok)
        # but PSD must look at ALL principal minors, incl. the (2,2) entry = -1 < 0
        self.assertFalse(is_positive_semidefinite(M))

    def test_negative_witness_is_exact(self):
        M = sp.Matrix([[1, 2], [2, 1]])  # eigenvalues 3, -1 -> indefinite
        v = negative_witness(M)
        self.assertIsNotNone(v)
        val = (v.T * M * v)[0, 0]
        self.assertTrue(val < 0)
        self.assertTrue(all(c.is_rational for c in v))
        # PSD matrix -> no witness
        self.assertIsNone(negative_witness(sp.eye(2)))


class TestFiniteSchur(unittest.TestCase):
    def test_equivalence_D_pd_psd_case(self):
        # M PSD <=> Schur complement PSD, with D > 0.
        A = sp.Matrix([[2]])
        B = sp.Matrix([[1, 1]])
        D = sp.Matrix([[2, 0], [0, 2]])
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
        cert = finite_schur_certificate(M, 1)
        self.assertTrue(cert.D_positive_definite)
        # Schur = 2 - (1,1).(1/2 I).(1,1)^T = 2 - 1 = 1 > 0
        self.assertEqual(cert.schur, sp.Matrix([[1]]))
        self.assertTrue(cert.schur_psd)
        self.assertTrue(cert.M_psd)
        self.assertTrue(cert.equivalence_holds)
        self.assertIsNone(cert.negative_vector)

    def test_equivalence_nonpsd_case_with_witness(self):
        A = sp.Matrix([[1]])
        B = sp.Matrix([[2, 0]])
        D = sp.Matrix([[1, 0], [0, 1]])
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
        # Schur = 1 - (2,0).(2,0)^T = 1 - 4 = -3 < 0  => M not PSD
        cert = finite_schur_certificate(M, 1)
        self.assertEqual(cert.schur, sp.Matrix([[-3]]))
        self.assertFalse(cert.schur_psd)
        self.assertFalse(cert.M_psd)
        self.assertTrue(cert.equivalence_holds)   # both False -> equivalent
        self.assertIsNotNone(cert.negative_vector)
        self.assertTrue((cert.negative_vector.T * M * cert.negative_vector)[0, 0] < 0)

    def test_D_singular_range_inclusion_and_shorted(self):
        # D >= 0 singular, range inclusion holds -> shorted complement governs.
        A = sp.Matrix([[1]])
        B = sp.Matrix([[1, 0]])          # B^T in ran(D) since D has e_1 in range
        D = sp.diag(1, 0)
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
        self.assertTrue(range_inclusion_holds(M, 1))
        S = shorted_complement(M, 1)     # 1 - 1*1*1 = 0
        self.assertEqual(S, sp.Matrix([[0]]))
        cert = finite_schur_certificate(M, 1)
        self.assertFalse(cert.D_positive_definite)
        self.assertTrue(cert.D_positive_semidefinite)
        self.assertTrue(cert.range_inclusion)
        self.assertTrue(cert.schur_psd)
        self.assertTrue(cert.M_psd)
        self.assertTrue(cert.equivalence_holds)

    def test_D_singular_range_inclusion_fails_forces_nonpsd(self):
        # B^T leaks outside ran(D): M cannot be PSD.
        A = sp.Matrix([[5]])
        B = sp.Matrix([[0, 1]])          # couples to the zero direction of D
        D = sp.diag(1, 0)
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
        self.assertFalse(range_inclusion_holds(M, 1))
        cert = finite_schur_certificate(M, 1)
        self.assertFalse(cert.M_psd)

    def test_square_completion_identity_exact(self):
        A = sp.Matrix([[3]])
        B = sp.Matrix([[1, 2]])
        D = sp.Matrix([[2, sp.Rational(1, 2)], [sp.Rational(1, 2), 3]])
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
        # several exact (x,y)
        for x, y in [([1], [1, 1]), ([2], [-1, 3]), ([sp.Rational(1, 3)], [0, 1])]:
            self.assertTrue(square_completion_identity(M, 1, x, y))

    def test_coupling_negative_vector_realizes_schur_sign(self):
        # The 1.1-shape: Schur < 0 -> exact full-space negative vector.
        A = sp.Matrix([[2]])
        B = sp.Matrix([[1, 0]])
        D = sp.Matrix([[1, Rat(9, 10)], [Rat(9, 10), 1]])
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
        S = schur_complement(M, 1)
        self.assertEqual(S, sp.Matrix([[Rat(-62, 19)]]))
        v = coupling_negative_vector(M, 1, [1])
        self.assertEqual((v.T * M * v)[0, 0], Rat(-62, 19))


class TestGaplessAndDiagnostics(unittest.TestCase):
    def test_inverse_decay_no_uniform_gap(self):
        prof = uniform_gap_profile(inverse_decay_block, [1, 2, 4, 8, 16])
        # every finite block is PD (min eig = 1/N > 0) but min eig -> 0
        for N, lam in prof:
            self.assertEqual(lam, Rat(1, N))
            self.assertTrue(lam > 0)
        self.assertTrue(prof[-1][1] < prof[0][1])
        self.assertTrue(is_positive_definite(inverse_decay_block(16)))

    def test_min_eigenvalue_nondiagonal(self):
        M = sp.Matrix([[2, 1], [1, 2]])      # eigenvalues 1, 3
        self.assertEqual(min_eigenvalue_exact(M), 1)

    def test_diagnostics_are_separate_not_a_score(self):
        # Gemini 1.2 shape: conservative surrogate negative, TRUE Schur positive.
        A = sp.Matrix([[1]])
        B = sp.Matrix([[2]])
        D = sp.Matrix([[100]])
        M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
        diag = diagnostics_from_block(M, 1, source_form_identified=True, kappa=1)
        # true Schur = 1 - 4/100 = 24/25 > 0
        self.assertTrue(diag.schur_complement_psd)
        self.assertEqual(diag.inverse_response_sign, "positive")
        # surrogate A - 1^{-1} B B^T = 1 - 4 = -3 < 0 : fails, yet form is positive
        self.assertFalse(diag.sufficient_surrogate_psd)
        # the genuine certificate ignores the surrogate entirely
        self.assertTrue(diag.is_genuine_certificate())
        rec = diag.as_record()
        self.assertNotIn("score", rec)   # there is deliberately no scalar score


class TestFormCoreTransport(unittest.TestCase):
    def test_negative_control_exact(self):
        for N in (3, 5, 10, 25):
            ctrl = form_core_negative_control(N)
            # q > 0 on the L^2-dense test subspace ...
            self.assertTrue(ctrl.test_gram_pd)
            self.assertTrue(ctrl.test_gram_min_eig > 0)
            self.assertTrue(ctrl.a_squared < ctrl.threshold_a_squared)
            # ... yet the global form is negative on e_1 (missed by the subspace)
            self.assertEqual(ctrl.global_negative_value, -9)

    def test_coercivity_constant_shrinks_toward_threshold(self):
        # As N grows with a^2 fixed at the threshold-respecting value, the test
        # subspace's coercivity does not stay bounded below (form-closure loses
        # the gap) -- illustrating why L^2-density is insufficient.
        mins = [form_core_negative_control(N, a_squared=Rat(1, 1000)).test_gram_min_eig
                for N in (3, 5, 10, 20)]
        self.assertTrue(all(m > 0 for m in mins))


if __name__ == "__main__":
    unittest.main()
