"""Exact tests for the Mason-Stothers proof certificate.

Two independent routes per the Proof Forge discipline: the symbolic certificate
(sympy over an exact field) is the proof oracle; these tests are the adversarial
computational check against the exact statement, including hostile controls.
"""
import unittest

import sympy as sp

from observational_succ.mason_stothers import (
    MasonStothersError,
    mason_stothers_certificate,
    wronskian,
    poly_radical,
    integer_transfer_obstruction,
)

x = sp.Symbol("x")


class TestMasonStothersValid(unittest.TestCase):
    def test_x3_plus_1_tight(self):
        # A=x^3, B=1, C=x^3+1 : bound is tight (equality)
        cert = mason_stothers_certificate(x**3, 1)
        self.assertTrue(cert.verified)
        self.assertFalse(cert.W_is_zero)
        self.assertTrue(cert.wronskian_forms_agree)
        self.assertTrue(cert.divisibility_holds)
        self.assertTrue(cert.bound_holds)
        self.assertEqual(cert.max_deg, 3)
        self.assertEqual(cert.deg_rad_ABC, 4)   # x * (x+1) * (x^2-x+1)
        self.assertEqual(cert.bound_rhs, 3)

    def test_square_plus_linear(self):
        # A=x^2, B=2x+1, C=(x+1)^2
        cert = mason_stothers_certificate(x**2, 2*x + 1)
        self.assertTrue(cert.verified)
        self.assertEqual(cert.max_deg, 2)
        self.assertEqual(cert.bound_rhs, 2)     # rad = x(x+1/2)(x+1), deg 3

    def test_higher_degree_coprime(self):
        # A=x^5, B=1 -> C=x^5+1 ; bound tight at deg 5 <= 6-1
        cert = mason_stothers_certificate(x**5, 1)
        self.assertTrue(cert.verified)
        self.assertEqual(cert.max_deg, 5)
        self.assertLessEqual(cert.max_deg, cert.bound_rhs)

    def test_davenport_tight(self):
        # Davenport-style: A=(x+1)^2, B=-4x, C=(x-1)^2 ; bound tight (max=2=rhs)
        cert = mason_stothers_certificate((x + 1)**2, -4*x, (x - 1)**2)
        self.assertTrue(cert.verified, cert.as_record())
        self.assertTrue(cert.divisibility_holds)
        self.assertEqual(cert.max_deg, 2)
        self.assertEqual(cert.deg_rad_ABC, 3)        # x(x+1)(x-1)
        self.assertEqual(cert.max_deg, cert.bound_rhs)  # tight

    def test_strictly_non_tight(self):
        # A=(x-1)(x-2), B=(x-3)(x-4), C=2(x^2-5x+7) [irreducible] : all squarefree
        # coprime, so deg rad(ABC)=6, max deg=2 -> bound STRICT (2 < 5).
        A = (x - 1)*(x - 2)
        B = (x - 3)*(x - 4)
        cert = mason_stothers_certificate(A, B)
        self.assertTrue(cert.verified, cert.as_record())
        self.assertTrue(cert.divisibility_holds, "M | W must hold on strict cases")
        self.assertEqual(cert.max_deg, 2)
        self.assertEqual(cert.deg_rad_ABC, 6)
        self.assertEqual(cert.bound_rhs, 5)
        self.assertLess(cert.max_deg, cert.bound_rhs)   # STRICT, not tight

    def test_wronskian_forms_all_equal_up_to_sign(self):
        A = sp.Poly(x**3, x, domain=sp.QQ)
        B = sp.Poly(sp.Integer(1), x, domain=sp.QQ)
        C = sp.Poly(x**3 + 1, x, domain=sp.QQ)
        self.assertTrue((wronskian(A, B) - wronskian(A, C)).is_zero)
        self.assertTrue((wronskian(A, B) + wronskian(B, C)).is_zero)


class TestMasonStothersCounterexamples(unittest.TestCase):
    def test_char_p_collapse(self):
        # A=x^5, B=1, C=x^5+1 over GF(5): freshman's dream, W == 0
        cert = mason_stothers_certificate(x**5, 1, domain=sp.GF(5),
                                          require_hypotheses=False)
        self.assertTrue(cert.W_is_zero)
        self.assertFalse(cert.verified)
        self.assertIn("collapse", cert.note.lower() + "x")  # note set
        # true radical of x^5*(x+1)^5 over GF(5) is x(x+1), deg 2 (factor_list,
        # NOT the gcd-squarefree shortcut which is wrong when P'==0)
        self.assertEqual(cert.deg_rad_ABC, 2)
        self.assertEqual(cert.bound_rhs, 1)
        # the bound it WOULD claim (deg 5 <= 1) is violated -> W=0 is why
        self.assertEqual(cert.max_deg, 5)
        self.assertGreater(cert.max_deg, cert.bound_rhs)

    def test_coprimality_failure_rejected(self):
        # A=x, B=x -> not coprime; require_hypotheses=True must raise
        with self.assertRaises(MasonStothersError):
            mason_stothers_certificate(x, x, 2*x)
        cert = mason_stothers_certificate(x, x, 2*x, require_hypotheses=False)
        self.assertFalse(cert.hypotheses_ok)
        self.assertFalse(cert.verified)

    def test_all_constant_rejected(self):
        with self.assertRaises(MasonStothersError):
            mason_stothers_certificate(sp.Integer(1), sp.Integer(1))

    def test_sum_mismatch_rejected(self):
        with self.assertRaises(MasonStothersError):
            mason_stothers_certificate(x**2, 1, x**3)  # A+B != C


class TestRadical(unittest.TestCase):
    def test_radical_of_square(self):
        P = sp.Poly((x + 1)**2 * (x - 2), x, domain=sp.QQ)
        rad, deg = poly_radical(P, x, sp.QQ)
        self.assertEqual(deg, 2)                # (x+1)(x-2)
        self.assertTrue(rad.is_monic)

    def test_radical_squarefree_identity(self):
        P = sp.Poly(x * (x + 1) * (x - 1), x, domain=sp.QQ)
        rad, deg = poly_radical(P, x, sp.QQ)
        self.assertEqual(deg, 3)


class TestIntegerObstruction(unittest.TestCase):
    def test_obstruction_is_honest(self):
        obs = integer_transfer_obstruction()
        self.assertIn("OPEN", obs["claim_status"])
        self.assertIn("derivation", obs["obstruction_1_no_derivation"].lower())
        # no claim of an integer abc proof anywhere
        blob = " ".join(obs.values()).lower()
        self.assertNotIn("we prove abc", blob)
        self.assertNotIn("abc is proved", blob)


if __name__ == "__main__":
    unittest.main()
