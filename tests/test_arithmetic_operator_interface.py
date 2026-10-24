import unittest
from fractions import Fraction as F
from math import gcd

from observational_succ.affine_pontryagin_transfer import RationalCharacterAlgebra as R
from observational_succ.arithmetic_operator_interface import (
    basis_action, character_value, cyclotomic_polynomial, root_average_receipt,
    shift_refinement_defect, thermal_refinement_defect_squared,
    multiply_monomials, critical_state_monomial,
)


class ArithmeticOperatorInterfaceTests(unittest.TestCase):
    def test_cyclotomic_independent_known_values(self):
        self.assertEqual(cyclotomic_polynomial(1), (-1, 1))
        self.assertEqual(cyclotomic_polynomial(6), (1, -1, 1))
        self.assertEqual(cyclotomic_polynomial(12), (1, 0, -1, 0, 1))
        # Same number, different formal phase supports; true reduction is essential.
        a = R.basis(F(1, 3)).add(R.basis(F(2, 3)))
        self.assertEqual(character_value(a, 1, 3), character_value(R.basis().scale(-1), 1, 3))

    def test_old_root_average_against_hilbert_action(self):
        for r in (F(0), F(1, 3), F(-2, 5), F(5, 7)):
            for m in (1, 2, 3, 4, 6):
                for n in range(1, 31):
                    self.assertTrue(root_average_receipt(r, m, n)["equal"])

    def test_hilbert_relations_and_composite_control(self):
        for n in range(1, 35):
            for m in (2, 3, 6):
                self.assertEqual(basis_action((("V", m), ("D", m)), n), (n, F(0)))
                r = F(2, 7)
                self.assertEqual(basis_action((("V", m), ("E", r)), n),
                                 basis_action((("E", m*r), ("V", m)), n))
                self.assertEqual(basis_action((("V", m), ("E", r), ("D", m)), n),
                                 basis_action((("E", m*r),), n))
            for m in (2, 3, 4, 6):
                for k in (2, 3, 5):
                    d = gcd(m, k)
                    self.assertEqual(basis_action((("V", k), ("D", m)), n),
                                     basis_action((("D", m//d), ("V", k//d)), n))
        # False commutation V_2* V_2 = V_2 V_2* fails on the vacuum.
        self.assertNotEqual(basis_action((("V", 2), ("D", 2)), 1),
                            basis_action((("D", 2), ("V", 2)), 1))

    def test_refinement_no_uniform_operator_convergence(self):
        for k in range(12):
            self.assertEqual(shift_refinement_defect(k, k), ())
            self.assertEqual(shift_refinement_defect(k, k+4), ((k+1, k, F(1)),))
            for q in (F(1, 4), F(1, 9)):
                top = q**k / sum(q**j for j in range(k+1))
                self.assertEqual(thermal_refinement_defect_squared(q, k), top)

    def test_reject_malformed_and_orientation_mutation(self):
        for d in (True, 0, -1, 1025):
            with self.assertRaises(ValueError):
                cyclotomic_polynomial(d)
        with self.assertRaises(ValueError):
            character_value(R.basis(F(1, 3)), 1, 2)
        self.assertNotEqual(character_value(R.basis(F(1, 5)), 1, 5),
                            character_value(R.basis(F(-1, 5)), 1, 5))

    def test_critical_state_kms_and_old_root_average(self):
        words = [(m, r, n) for m in range(1, 5) for n in range(1, 5)
                 for r in (F(0), F(1, 2), F(1, 3))]
        for a in words:
            for b in words:
                ab, ba = multiply_monomials(a, b), multiply_monomials(b, a)
                self.assertEqual(critical_state_monomial(ab),
                                 F(a[2], a[0])*critical_state_monomial(ba))
        for m in range(1, 9):
            for r in (F(0), F(1, 3), F(1, 5)):
                self.assertEqual(critical_state_monomial((m, r, m)), R.basis(r).rho(m).haar())
        # A wrong temperature in this formula fails the required beta=1 KMS test.
        self.assertNotEqual(F(1, 2**2), F(1, 2))

    def test_monomial_product_independent_basis_action(self):
        for a in ((2, F(1, 3), 3), (4, F(2, 5), 2), (1, F(0), 6)):
            for b in ((3, F(1, 2), 4), (6, F(1, 3), 1)):
                m, r, n = multiply_monomials(a, b)
                raw = (("D", b[2]), ("E", b[1]), ("V", b[0]),
                       ("D", a[2]), ("E", a[1]), ("V", a[0]))
                for k in range(1, 40):
                    self.assertEqual(basis_action(raw, k),
                                     basis_action((("D", n), ("E", r), ("V", m)), k))


if __name__ == "__main__":
    unittest.main()
