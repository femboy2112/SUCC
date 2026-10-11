"""Hostile controls for finite Pi1 observational-SUCC and toy kernel probes.

A finite pass is always UNRESOLVED. No test executes an infinite stage,
proves PA consistency, or proves positivity of the arithmetic Weil form.
"""
import unittest

from observational_succ.godel_succ import (
    GodelSuccError, delayed_halt, halted_by, machine_prefix,
    observe_pi1_prefix, rational_kernel, delayed_ramp,
    two_counter_loop, validate_program,
)


class GodelSuccTests(unittest.TestCase):

    def test_delayed_counterexample_and_prefix_indistinguishability(self):
        delayed, loop = delayed_halt(19), two_counter_loop()
        for horizon in (0, 1, 2, 6, 17, 18):
            a, b = machine_prefix(delayed, horizon), machine_prefix(loop, horizon)
            self.assertEqual(a.status, b.status)
            self.assertEqual(a.status, "unresolved")
            self.assertIsNone(a.first_counterexample)
            self.assertFalse(a.universal_claim_proved)
            self.assertFalse(b.universal_claim_proved)
        result = machine_prefix(delayed, 19)
        self.assertEqual(result.status, "refuted")
        self.assertEqual(result.first_counterexample, 19)
        self.assertTrue(halted_by(delayed, 19))
        self.assertFalse(halted_by(delayed, 18))
        self.assertFalse(halted_by(loop, 200))

    def test_immediate_counterexample_detected(self):
        self.assertEqual(machine_prefix((("HALT",),), 0).first_counterexample, 0)
        self.assertEqual(observe_pi1_prefix(lambda n: n != 11, 10).status, "unresolved")
        self.assertEqual(observe_pi1_prefix(lambda n: n != 11, 11).first_counterexample, 11)

    def test_integer_horizons_and_malformed_programs(self):
        for bad in (1.5, -1, True, 100001):
            with self.assertRaises(GodelSuccError):
                observe_pi1_prefix(lambda n: True, bad)
        with self.assertRaises(GodelSuccError):
            observe_pi1_prefix(lambda n: 1, 0)
        with self.assertRaises(GodelSuccError):
            delayed_halt(0)
        for invalid in ((), (("INC", 2, 0),), (("HALT", 0),),
                        (("DECJZ", 0, 7, 0),), (("JUMP", 0),)):
            with self.assertRaises(GodelSuccError):
                validate_program(invalid)

    def test_quantifier_swap_not_uniform(self):
        # For each k some horizon N=k includes k, but N never covers all k.
        for k in range(100):
            self.assertTrue(k <= k)
            self.assertFalse(k + 1 <= k)

    def test_gram_quartic_and_delayed_fake_impulse(self):
        # Positive Psi(t)=t^4 does NOT imply Gram PSD.
        psi = lambda t: t**4
        self.assertEqual(rational_kernel(psi, 1, 1), 2)
        self.assertEqual(rational_kernel(psi, -1, -1), 2)
        self.assertEqual(rational_kernel(psi, 1, -1), -14)
        self.assertEqual(2*2 - (-14)**2, -192)
        base = lambda t: t*t
        mutated = delayed_ramp(base, threshold=9, amplitude=500)
        for t in range(-9, 10):
            self.assertEqual(base(t), mutated(t))
        self.assertEqual(rational_kernel(base, 10, 10), 200)
        self.assertLess(rational_kernel(mutated, 10, 10), 0)
        for t in range(-4, 5):
            for u in range(-4, 5):
                self.assertEqual(rational_kernel(base, t, u),
                                 rational_kernel(mutated, t, u))


if __name__ == "__main__":
    unittest.main()
