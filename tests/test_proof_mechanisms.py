"""Tests for the proof-mechanism audit transducers (M1, M2, M8).

These test the META tools, using exact arithmetic only. They assert the
audit behaviour, not any mathematical theorem about pi/RH.
"""
import unittest

from fractions import Fraction as F

from observational_succ.proof_mechanisms import (
    MechanismError, criterion_audit, exact_countermodel, threshold_bisect,
    threshold_report,
)


class TestExactCountermodel(unittest.TestCase):
    """M2: a refutation must carry an exact negative margin."""

    def test_refutes_when_negative(self):
        cm = exact_countermodel(
            claim="L2 projection onto P<=3 is derivative-contractive",
            witness="h = P5(2t) - P3(2t)",
            membership="h(+-1/2)=0 and h in H^1(-1/2,1/2)",
            violation=F(36) - F(60),          # ||h'||^2 - ||(Q4h)'||^2
            source_witness=(36,60),
            membership_checker=lambda w: w == (36,60),
        )
        self.assertTrue(cm.refutes)
        self.assertEqual(cm.violation, F(-24))
        self.assertIn("REFUTES", cm.report())

    def test_does_not_promote_a_non_refutation(self):
        cm = exact_countermodel("x", "y", "z", F(0))
        self.assertFalse(cm.refutes)
        self.assertIn("does NOT refute", cm.report())

    def test_negative_margin_without_verified_membership_refuses(self):
        cm=exact_countermodel("arbitrary universal", "untyped witness",
                             "membership claimed by author",F(-1))
        self.assertFalse(cm.refutes)
        self.assertTrue(cm.negative_margin)
        self.assertIn("UNVERIFIED MEMBERSHIP",cm.report())

    def test_rejects_float(self):
        with self.assertRaises(MechanismError):
            exact_countermodel("x", "y", "z", 0.5)


class TestThresholdBisect(unittest.TestCase):
    """M8: exact flip value, no floats."""

    def test_recovers_a_known_rational_threshold(self):
        # predicate: p < 3/8  -> flip at exactly 3/8
        thr = threshold_bisect(lambda p: p < F(3, 8), -1, 1, direction="<", steps=80)
        self.assertLessEqual(abs(thr - F(3, 8)), F(1, 2**70))

    def test_report_reports_distance(self):
        # conclusion holds for p < 6.015e-7; available is 121/32
        target = F(363594907672565835, 604462909807314587353088)
        rep = threshold_report(lambda p: p < target, 0, 1,
                               available=F(121, 32), direction="<", steps=64)
        self.assertFalse(rep.exact)
        self.assertLessEqual(rep.lower, target)
        self.assertGreaterEqual(rep.upper, target)
        self.assertGreater(rep.ratio, 6_000_000)   # ~6.29e6
        self.assertLess(rep.ratio, 7_000_000)
        self.assertIn("distance ratio", rep.report())

    def test_exact_arithmetic_is_not_exact_real_threshold(self):
        from observational_succ.proof_mechanisms import threshold_bisect_interval
        low,high=threshold_bisect_interval(lambda p:p*p<F(2),0,2,
                                            direction="<",steps=80)
        self.assertLess(low*low,2)
        self.assertGreaterEqual(high*high,2)
        self.assertGreater(high,low)

    def test_requires_separating_bracket(self):
        with self.assertRaises(MechanismError):
            threshold_bisect(lambda p: True, 0, 1)


class TestCriterionAudit(unittest.TestCase):
    """M1: catch tautologies, hollowness and genericity."""

    def test_flags_tautology(self):
        a = criterion_audit("target", "premise", generic_in_x=False,
                            premise_equivalent_to_target=True, falsifier_named=True)
        self.assertIn("TAUTOLOGY", a.verdict)

    def test_flags_generic(self):
        a = criterion_audit("pi normal base 16", "carry sum -> 0",
                            generic_in_x=True,
                            premise_equivalent_to_target=False,
                            falsifier_named=True)
        self.assertIn("GENERIC", a.verdict)

    def test_flags_hollow(self):
        a = criterion_audit("t", "p", generic_in_x=False,
                            premise_equivalent_to_target=False,
                            falsifier_named=False)
        self.assertIn("HOLLOW", a.verdict)

    def test_ok_case(self):
        a = criterion_audit("t", "p", generic_in_x=False,
                            premise_equivalent_to_target=False,
                            falsifier_named=True)
        self.assertTrue(a.verdict.startswith("OK"))

    def test_flags_transient_feature(self):
        # the four-pole lesson: a feature killed by one step of the dynamics
        # cannot control recurrent statistics
        a = criterion_audit("pi normal base 16", "pole structure controls carry sum",
                            generic_in_x=False,
                            premise_equivalent_to_target=False,
                            falsifier_named=True,
                            structural_feature_killed_in_one_step=True)
        self.assertIn("TRANSIENT_QUOTIENT_WARNING", a.verdict)

    def test_flags_non_faithful(self):
        a = criterion_audit("t", "p", generic_in_x=False,
                            premise_equivalent_to_target=False,
                            falsifier_named=True,
                            failure_observable_at_target=False)
        self.assertIn("TARGET_TEST_INCOMPLETE", a.verdict)

    def test_faithful_specific_is_ok(self):
        a = criterion_audit("t", "p", generic_in_x=False,
                            premise_equivalent_to_target=False,
                            falsifier_named=True,
                            failure_observable_at_target=True)
        self.assertTrue(a.verdict.startswith("OK"))



if __name__ == "__main__":
    unittest.main()