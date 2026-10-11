"""Exact finite positive and adversarial controls for ideal-frame SUCC.

These tests do NOT execute omega or test the all-orders flat-function theorem.
The latter is a mathematical proof in the accompanying research note.
"""
import unittest
from fractions import Fraction as Q
from math import factorial

from observational_succ.ideal_frames import (
    IdealFrameError,
    IdealJetFrame,
    PolynomialSource,
    analytic_finite_stage_adversary,
    divergent_analytic_jet_prefix,
    finite_probe_equivalent,
)


class IdealFramesTests(unittest.TestCase):
    def test_finite_polynomial_reconstruction_is_conditional_and_exact(self):
        src = PolynomialSource((Q(3), Q(-2), Q(1, 2)))
        f0 = IdealJetFrame.initial(src)
        self.assertEqual(f0.observed_jet, (Q(3),))
        self.assertTrue(f0.compatible(src))
        with self.assertRaises(IdealFrameError):
            f0.reconstruct_under_degree_assumption(2)
        f1 = f0.succ(src)
        f2 = f1.succ(src)
        self.assertEqual(f2.observed_jet, (Q(3), Q(-2), Q(1)))
        fit = f2.reconstruct_under_degree_assumption(2)
        self.assertEqual(fit, src)
        for x in (Q(-3), Q(-1, 2), Q(0), Q(7, 3)):
            self.assertEqual(fit.value(x), src.value(x))

    def test_every_finite_analytic_jet_still_has_a_distinct_adversary(self):
        for n in range(22):
            a, b = analytic_finite_stage_adversary(n)
            self.assertTrue(finite_probe_equivalent(a, b, n))
            self.assertFalse(finite_probe_equivalent(a, b, n + 1))
            self.assertNotEqual(a.value(1), b.value(1))

    def test_wrong_degree_model_can_appear_complete_early(self):
        src = PolynomialSource((Q(0), Q(0), Q(0), Q(0), Q(1)))
        f = IdealJetFrame.initial(src)
        self.assertEqual(f.reconstruct_under_degree_assumption(0).value(1), 0)
        # This is a CONDITIONAL fit, demonstrably wrong for the real source.
        self.assertEqual(src.value(1), 1)
        for _ in range(4):
            f = f.succ(src)
        self.assertEqual(f.horizon, 4)
        with self.assertRaises(IdealFrameError):
            f.reconstruct_under_degree_assumption(0)

    def test_causal_journal_cannot_rewrite_prior_outcomes(self):
        src = PolynomialSource((Q(5), Q(2)))
        frame = IdealJetFrame.initial(src)
        with self.assertRaises(IdealFrameError):
            frame.succ(PolynomialSource((Q(6), Q(2))))
        later = frame.succ(src)
        self.assertEqual(later.observed_jet[:1], frame.observed_jet)
        self.assertTrue(later.compatible(src))
        self.assertFalse(later.compatible(PolynomialSource((Q(5), Q(3)))))

    def test_finite_analytic_realizability_does_not_imply_limit(self):
        old = ()
        for n in range(18):
            prefix = divergent_analytic_jet_prefix(n)
            self.assertEqual(prefix[:n], old)
            self.assertEqual(prefix[-1], factorial(n))
            # Every finite prefix is the coefficients of an actual polynomial.
            finite_witness = PolynomialSource(prefix)
            self.assertEqual(finite_witness.coefficients, prefix)
            if n:
                self.assertEqual(prefix[-1] / prefix[-2], n)
            old = prefix
        # Radius zero is proved by the unbounded coefficient ratios,
        # not by pretending that this finite test executed an infinite series.

    def test_bad_probe_types_and_bounds_are_rejected(self):
        src = PolynomialSource((1,))
        with self.assertRaises(IdealFrameError):
            PolynomialSource((0.1,))
        with self.assertRaises(IdealFrameError):
            PolynomialSource(())
        with self.assertRaises(IdealFrameError):
            src.jet(True)
        with self.assertRaises(IdealFrameError):
            divergent_analytic_jet_prefix(-1)
        with self.assertRaises(IdealFrameError):
            analytic_finite_stage_adversary(63)
        with self.assertRaises(IdealFrameError):
            IdealJetFrame(1, (Q(0),))
        with self.assertRaises(IdealFrameError):
            IdealJetFrame(0, (0.0,))


if __name__ == "__main__":
    unittest.main()
