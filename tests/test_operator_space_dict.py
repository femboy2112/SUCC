"""Exact tests for operator_space_dict (Proof Forge III, Lane C).

Every assertion is exact (sympy.Rational). A float is never a certificate. The
witnesses are generic exact linear algebra; none is a signed-Weil positivity claim.
"""
import unittest

import sympy as sp

from observational_succ.operator_space_dict import (
    absolute_gap_holds,
    k_relative_gap_holds,
    gap_notion_witness,
    gapless_profile,
    k_relative_misread_as_absolute,
    transport_defect_diagnostics,
)
from observational_succ.quantitative_rigidity import quad

Rat = sp.Rational


class TestGapNotionsAreDistinct(unittest.TestCase):
    def test_absolute_vs_k_relative_predicates_disagree(self):
        D = sp.diag(1, Rat(1, 10))
        # absolute gap at kappa=1 fails; at kappa=1/10 holds (min eig = 1/10)
        self.assertFalse(absolute_gap_holds(D, Rat(1)))
        self.assertTrue(absolute_gap_holds(D, Rat(1, 10)))
        # K-relative gap with K=D at kappa=1 holds (D - D = 0 is PSD)
        self.assertTrue(k_relative_gap_holds(D, D, Rat(1)))
        # but K-relative at kappa=2 fails (D - 2D = -D not PSD)
        self.assertFalse(k_relative_gap_holds(D, D, Rat(2)))

    def test_gapless_family_loses_absolute_gap_keeps_k_relative(self):
        for N in (2, 3, 8, 32):
            w = gap_notion_witness(N)
            self.assertEqual(w.absolute_min_eig, Rat(1, N))   # -> 0
            self.assertFalse(w.absolute_gap_at_1)             # no uniform absolute gap
            self.assertTrue(w.k_relative_gap_at_1_with_K_eq_D)  # uniform K-relative gap

    def test_gapless_profile_tends_to_zero(self):
        prof = dict(gapless_profile([1, 2, 4, 16, 64]))
        self.assertEqual(prof[1], Rat(1, 1))
        self.assertEqual(prof[64], Rat(1, 64))
        # strictly decreasing to 0
        vals = [prof[N] for N in (1, 2, 4, 16, 64)]
        self.assertEqual(vals, sorted(vals, reverse=True))
        self.assertTrue(all(v > 0 for v in vals))


class TestTransportDefect(unittest.TestCase):
    def setUp(self):
        self.w = k_relative_misread_as_absolute()

    def test_premises_true_k_relative_false_absolute(self):
        # the HONEST premise holds; the ILLEGAL substitution does not
        self.assertTrue(self.w.D_has_k_relative_gap)
        self.assertFalse(self.w.D_has_absolute_gap)

    def test_sign_flip_is_real(self):
        # absolute surrogate certifies POSITIVE; true Schur is NEGATIVE
        self.assertEqual(self.w.absolute_surrogate, sp.Matrix([[1]]))
        self.assertEqual(self.w.true_schur, sp.Matrix([[-8]]))
        self.assertTrue(self.w.absolute_surrogate_psd)
        self.assertFalse(self.w.true_schur_psd)
        self.assertTrue(self.w.sign_flips)

    def test_negative_vector_is_exact_and_negative(self):
        v = self.w.negative_vector_of_M
        self.assertTrue(quad(self.w.M, v) < 0)
        self.assertFalse(v.atoms(sp.Float))   # exact, no floats

    def test_coupling_vector_realizes_schur_value(self):
        v = self.w.coupling_vector
        # v = (x; -D^{-1} B^* x) realizes v^T M v = <S x, x> = -8 for x = (1)
        self.assertEqual(quad(self.w.M, v), Rat(-8))


class TestDiagnosticsNotFooled(unittest.TestCase):
    def test_status_is_refuted_not_verified(self):
        diag = transport_defect_diagnostics()
        # true Schur not PSD  -> REFUTED; source not identified anyway
        self.assertFalse(diag.schur_complement_psd)
        self.assertFalse(diag.source_form_identified)
        self.assertEqual(diag.certificate_status(), "REFUTED")
        self.assertFalse(diag.is_genuine_certificate())
        # the absolute surrogate being PSD plays NO role in the verdict
        self.assertTrue(diag.sufficient_surrogate_psd)


if __name__ == "__main__":
    unittest.main()
