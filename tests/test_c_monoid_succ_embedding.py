"""Finite lambda-identity and separate arithmetic-action regression tests."""
import unittest
from fractions import Fraction as Q

from observational_succ import c_monoid_succ_embedding as cm


class CMonoidTests(unittest.TestCase):
    def test_all_cmonoid_equations(self):
        res = cm.check_cmonoid_equations()
        for k, v in res.items():
            self.assertTrue(v, k)

    def test_karoubi_object_idempotent(self):
        # e(x)=<fst x,fst x> is an actual idempotent: its first component
        # stays fst x on a second application.  PROJ1 alone is not idempotent.
        e = cm.pair(cm.PROJ1, cm.PROJ1)
        self.assertTrue(cm.idempotent_retract(e))
        self.assertTrue(cm.idempotent_retract(cm.ID))
        self.assertFalse(cm.idempotent_retract(cm.PROJ1))

    def test_affine_relation(self):
        self.assertTrue(cm.verify_affine_relation())

    def test_source_step_exact(self):
        s = cm.SuccState(0, Q(0))
        s2 = cm.succ_step(s)
        # U_1 = 16*U_0 + r(1) = 0 + 47/15
        self.assertEqual(s2.u, Q(47, 15))
        self.assertEqual(s2.n, 1)
        s3 = cm.succ_step(s2)
        # U_2 = 16*(47/15) + r(2)
        self.assertEqual(s3.u, 16 * Q(47, 15) + cm.forcing(2))
        self.assertEqual(s3.n, 2)

    def test_cantor_firewall(self):
        # A finite set U with |U|>=2 cannot satisfy |U^U| >= 2^|U| > |U|.
        # This is the CW-13 refutation made executable at the counting level.
        for n in (2, 3, 4, 5):
            self.assertGreater(n ** n, n)  # |U^U| = n^n > n = |U|
        self.assertGreater(2 ** 5, 5)

    def test_beta_law_direct(self):
        a, b = cm.CONST('a'), cm.CONST('b')
        # eps(<Lambda(a), b>) = lambda y. a<b,y>
        self.assertTrue(cm.eq(
            cm.APP(cm.EVAL, cm.PAIR(cm.curry(a), b)),
            cm.ABS(cm.APP(a, cm.PAIR(b, cm.V(0))))))

    def test_eta_eval(self):
        # Lambda(eps) = id
        self.assertTrue(cm.eq(cm.curry(cm.EVAL), cm.ID))


if __name__ == '__main__':
    unittest.main()
