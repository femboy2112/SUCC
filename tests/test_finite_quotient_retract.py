"""Exact finite retraction/projection gates and adversarial mutants."""
import random
import unittest
from fractions import Fraction as Q

from observational_succ.finite_quotient_retract import (
    FiniteQuotientRetract, QuotientRetractError,
)


class FiniteQuotientRetractTests(unittest.TestCase):
    def test_universal_algebra_specimens_and_energy(self):
        rng = random.Random(100715)
        for n in range(2, 9):
            for k in (2, 3, 4):
                R = FiniteQuotientRetract(n*k, n)
                for _ in range(10):
                    f = tuple(Q(rng.randint(-7, 7), rng.randint(1, 7)) for _ in range(n))
                    g = tuple(Q(rng.randint(-7, 7), rng.randint(1, 7)) for _ in range(n*k))
                    self.assertEqual(R.average(R.pullback(f)), f)
                    self.assertEqual(R.pushforward(R.pullback(f)), tuple(k*x for x in f))
                    self.assertEqual(R.project(R.project(g)), R.project(g))
                    x = R.exact_instance(g)
                    self.assertEqual(x["projected_energy"] + x["unseen_energy"], x["total_energy"])
                    self.assertGreaterEqual(x["unseen_energy"], 0)
                    self.assertFalse(x["proves_universal_law_by_enumeration"])

    def test_dual_injection_composes_and_wrong_direction_fails(self):
        A, B, C = (FiniteQuotientRetract(6, 3),
                   FiniteQuotientRetract(12, 6),
                   FiniteQuotientRetract(12, 3))
        for i in range(-10, 11):
            self.assertEqual(B.dual_injection(A.dual_injection(i)), C.dual_injection(i))
        self.assertEqual(FiniteQuotientRetract(4, 2).dual_injection(1), 2)
        self.assertNotEqual(FiniteQuotientRetract(4, 2).dual_injection(1), 1)

    def test_nontrivial_idempotent_and_wrong_normalization_mutant(self):
        R = FiniteQuotientRetract(4, 2)
        g = (Q(1), Q(0), Q(0), Q(0))
        p = R.project(g)
        self.assertNotEqual(p, g)
        self.assertEqual(R.project(p), p)
        self.assertNotEqual(R.pullback(R.pushforward(g)), p)  # forget 1/k
        self.assertEqual(R.exact_instance(g)["unseen_energy"], Q(1, 2))

    def test_fourier_pullback_on_exact_cyclotomic_clock(self):
        for n,k in ((2,2), (2,3), (3,2), (3,3), (4,2), (5,2)):
            R = FiniteQuotientRetract(n*k,n)
            for f in (tuple(range(n)), tuple((-1)**i for i in range(n))):
                receipt = R.fourier_instance(f)
                self.assertTrue(receipt["exact_finite_fourier_instance"])
                self.assertEqual(receipt["dual_injection"], tuple(k*i for i in range(n)))
                self.assertFalse(receipt["proves_global_adelic_theorem"])

    def test_hostile_input_and_source_identity(self):
        for m,n in ((4,4),(5,2),(2,3),(101,2),(4,1),(True,2)):
            with self.assertRaises(QuotientRetractError):
                FiniteQuotientRetract(m,n)
        for src,epoch in (("",0),("same",-1),("same",True)):
            with self.assertRaises(QuotientRetractError):
                FiniteQuotientRetract(4,2,src,epoch)
        R = FiniteQuotientRetract(4,2,"real",7)
        R.assert_source("real",7)
        for src,epoch in (("fake",7),("real",8)):
            with self.assertRaises(QuotientRetractError):
                R.assert_source(src,epoch)
        for bad in ((1,2), (1,True,2,3), (1,2,3,4.0)):
            with self.assertRaises(QuotientRetractError):
                R.exact_instance(bad)
        with self.assertRaises(QuotientRetractError):
            R.dual_injection(1.0)


if __name__ == "__main__":
    unittest.main()
