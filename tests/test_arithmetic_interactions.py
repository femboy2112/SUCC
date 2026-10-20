"""Exact tests for the additive/multiplicative interaction calculus.

The load-bearing fact: the additive von Mangoldt convolution is NOT the
Dirichlet-series square (-zeta'/zeta)^2; the smallest exact separating witness
is n=5.
"""
import unittest

import sympy as sp

from observational_succ.arithmetic_interactions import (
    additive_convolution,
    dirichlet_convolution,
    von_mangoldt,
    radical_int,
    is_prime_power,
    dgf_coefficient_of_squared_logderiv,
    illegal_interchange_witness,
    goldbach_representation_R_Lambda,
)


class TestConvolutions(unittest.TestCase):
    def test_additive_n5_exact(self):
        # (Lambda *+ Lambda)(5) = Lambda(2)Lambda(3)+Lambda(3)Lambda(2) = 2 log2 log3
        val = additive_convolution(von_mangoldt, von_mangoldt, 5)
        self.assertEqual(sp.simplify(val - 2*sp.log(2)*sp.log(3)), 0)

    def test_dirichlet_n5_zero(self):
        # (Lambda *x Lambda)(5) = 0 (5 prime: only 1*5, Lambda(1)=0)
        val = dirichlet_convolution(von_mangoldt, von_mangoldt, 5)
        self.assertEqual(sp.simplify(val), 0)

    def test_they_coincide_at_small_n_by_accident(self):
        # n=4: both equal log(2)^2 -- coincidence, NOT a general identity
        a4 = additive_convolution(von_mangoldt, von_mangoldt, 4)
        d4 = dirichlet_convolution(von_mangoldt, von_mangoldt, 4)
        self.assertEqual(sp.simplify(a4 - sp.log(2)**2), 0)
        self.assertEqual(sp.simplify(d4 - sp.log(2)**2), 0)

    def test_dgf_coefficient_is_dirichlet_conv(self):
        for n in range(1, 13):
            self.assertEqual(
                sp.simplify(dgf_coefficient_of_squared_logderiv(n)
                            - dirichlet_convolution(von_mangoldt, von_mangoldt, n)),
                0, msg=f"n={n}")

    def test_R_Lambda_is_additive(self):
        self.assertEqual(
            sp.simplify(goldbach_representation_R_Lambda(5) - 2*sp.log(2)*sp.log(3)),
            0)


class TestIllegalInterchange(unittest.TestCase):
    def test_smallest_witness_is_5(self):
        w = illegal_interchange_witness(16)
        self.assertEqual(w.n, 5)
        self.assertFalse(w.equal)
        self.assertEqual(sp.simplify(sp.sympify(w.dirichlet_value)), 0)
        self.assertEqual(
            sp.simplify(sp.sympify(w.additive_value) - 2*sp.log(2)*sp.log(3)), 0)

    def test_receipt_shape(self):
        rec = illegal_interchange_witness(16).as_receipt()
        self.assertEqual(rec["n"], "5")
        self.assertEqual(rec["equal"], "False")


class TestArithmeticHelpers(unittest.TestCase):
    def test_von_mangoldt(self):
        self.assertEqual(von_mangoldt(1), 0)
        self.assertEqual(sp.simplify(von_mangoldt(8) - sp.log(2)), 0)   # 2^3
        self.assertEqual(sp.simplify(von_mangoldt(9) - sp.log(3)), 0)   # 3^2
        self.assertEqual(von_mangoldt(6), 0)                            # composite

    def test_is_prime_power(self):
        self.assertEqual(is_prime_power(8), (True, 2, 3))
        self.assertEqual(is_prime_power(6), (False, 0, 0))
        self.assertEqual(is_prime_power(1), (False, 0, 0))

    def test_radical_int(self):
        self.assertEqual(radical_int(1), 1)
        self.assertEqual(radical_int(12), 6)     # 2^2*3 -> 2*3
        self.assertEqual(radical_int(2**5 * 3**2 * 5), 30)


if __name__ == "__main__":
    unittest.main()
