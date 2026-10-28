"""Exact identities, source mutations and contraction-direction controls."""
import cmath
from fractions import Fraction as Q
import math
import unittest

from observational_succ import ladder_shift_audit as audit
from observational_succ import succ_internal_matrix_walk as mw


class LadderShiftIdentityTests(unittest.TestCase):
    def test_general_identity_signed_forces_and_radices(self):
        for radix in (2, 3, 16):
            for frequency in (-7, -1, 1, 3):
                forces = (Q(1, 3), Q(-2, 5), Q(0), Q(7, 11))
                states = [Q(2, 7)]
                for force in forces:
                    states.append(radix * states[-1] + force)
                receipt = audit.ladder_shift_audit(states, forces,
                                                  frequency, radix)
                self.assertEqual(receipt.residual, mw.PhasePoly.zero())
                self.assertEqual(receipt.forcing_l1, Q(1, 3) + Q(2, 5) + Q(7, 11))

    def test_authentic_source_exact_at_several_horizons(self):
        for n in (1, 2, 8, 17):
            for h in (-3, 1, 4):
                receipt = audit.authentic_ladder_audit(n, h)
                self.assertEqual(receipt.residual, mw.PhasePoly.zero())
                self.assertLess(receipt.forcing_l1, audit.BBP_FORCING_TAIL_UPPER)
                self.assertLessEqual(receipt.normalized_bound,
                                     audit.authentic_linear_shift_bound(n, h))

    def test_history_mutation_is_rejected(self):
        forces = (Q(1, 3), Q(2, 5))
        states = (Q(0), Q(1, 3), Q(16, 3) + Q(2, 5))
        self.assertEqual(audit.ladder_shift_audit(states, forces, 1).residual,
                         mw.PhasePoly.zero())
        with self.assertRaises(ValueError):
            audit.ladder_shift_audit(states, (forces[0], forces[1] + 1), 1)

    def test_missing_forcing_or_reversed_sign_fails(self):
        receipt = audit.authentic_ladder_audit(4, 1)
        self.assertNotEqual(receipt.difference - receipt.endpoint,
                            mw.PhasePoly.zero())
        self.assertNotEqual(receipt.difference - receipt.endpoint
                            + receipt.forcing_defect, mw.PhasePoly.zero())

    def test_exact_multiplicative_orbit_is_pure_endpoint(self):
        states = [Q(1, 7) * 16**n for n in range(9)]
        receipt = audit.ladder_shift_audit(states, [Q(0)] * 8, 3)
        self.assertEqual(receipt.forcing_defect, mw.PhasePoly.zero())
        self.assertEqual(receipt.difference, receipt.endpoint)
        self.assertEqual(receipt.normalized_bound, Q(1, 4))

    def test_independent_complex_evaluation_calibrates_bound(self):
        # Direct cmath phases are a separate numerical calibration only.
        n, h = 23, 2
        states, state = [], Q()
        for k in range(1, n + 2):
            state = 16 * state + mw.authentic_r(k)
            states.append(state)
        def e(x):
            return cmath.exp(2j * math.pi * float(x % 1))
        left = sum(e(16 * h * x) - e(h * x) for x in states[:-1]) / n
        receipt = audit.authentic_ladder_audit(n, h)
        self.assertLessEqual(abs(left), float(receipt.normalized_bound) + 1e-14)


class LadderLogicalDirectionTests(unittest.TestCase):
    def test_exact_source_tail_bound_independent_combined_formula(self):
        total = Q()
        for n in range(2, 300):
            # Independent combined four-pole expression, not the engine's formula.
            force = Q(120*n*n - 89*n + 16,
                      (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertGreater(force, 0)
            self.assertLessEqual(force, Q(15, (8*n-7)*(8*n-6)))
            total += force
        self.assertLess(total, audit.BBP_FORCING_TAIL_UPPER)
        self.assertEqual(audit.BBP_FORCING_TAIL_UPPER,
                         15 * (Q(1, 81) + Q(1, 72)))

    def test_strict_contraction_premise_would_already_give_one_over_N(self):
        self.assertEqual(audit.bound_if_contraction(1000, 1, Q(1, 2)),
                         Q(1027, 108000))
        self.assertEqual(audit.bound_if_contraction(2000, 1, Q(1, 2)),
                         Q(1027, 216000))
        self.assertFalse(audit.ladder_contraction_proved)
        self.assertFalse(audit.pi_normality_proved)

    def test_moving_frequency_quantifier_is_not_silently_fixed(self):
        self.assertLess(audit.authentic_normalized_shift_bound(1000000, 100),
                        Q(1, 1000))
        self.assertLess(audit.authentic_normalized_shift_bound(1000000, 1000000),
                        Q(1, 250))
        self.assertEqual(audit.authentic_normalized_shift_bound(1000000, 1000000**2),
                         Q(2))

    def test_saturated_force_bound_before_summation(self):
        h = 10000
        receipt = audit.authentic_ladder_audit(80, h)
        independently_saturated = sum(
            (min(Q(2), Q(105*h, 64*n*n)) for n in range(1, 81)), Q())
        self.assertLessEqual(receipt.forcing_phase_bound, independently_saturated)
        # A prefix plus the integral-tail certificate bounds the infinite sum.
        split = 100
        finite_cap = 2 * split + Q(105*h, 64*split)
        self.assertLessEqual(independently_saturated, finite_cap)
        self.assertLess(audit.authentic_normalized_shift_bound(10000, h),
                        audit.authentic_linear_shift_bound(10000, h))

    def test_high_frequency_contraction_does_not_bound_starting_mode(self):
        # Positive 3-atom law at 0, 1/48, 1/24: all 16^k modes, k>=1,
        # vanish exactly, while mode 1 is nonzero. This is not claimed
        # to be a time-stationary BBP orbit; it isolates the direction error.
        states = (Q(0), Q(1, 48), Q(1, 24))
        def average(h):
            return sum((mw.formal_character(h, x) for x in states),
                       mw.PhasePoly.zero()) / 3
        start = mw.source_cyclotomic_quotient(average(1), 48)
        self.assertNotEqual(start.polynomial, (Q(0),))
        for k in range(1, 6):
            higher = mw.source_cyclotomic_quotient(average(16**k), 48)
            self.assertEqual(higher.polynomial, (Q(0),))

    def test_stationary_nonnormal_control_does_not_contract(self):
        states = [Q(0)] * 10
        receipt = audit.ladder_shift_audit(states, [Q(0)] * 9, 1)
        self.assertEqual(receipt.residual, mw.PhasePoly.zero())
        self.assertEqual(sum((mw.formal_character(1, x) for x in states[:-1]),
                             mw.PhasePoly.zero()) / 9, mw.PhasePoly.one())

    def test_unbounded_frequency_limsup_fails_at_common_conductor(self):
        for n in (1, 4, 8):
            states = tuple(mw.original_state(k) for k in range(1, n + 1))
            conductor = math.lcm(*(x.denominator for x in states))
            for multiple in (1, 2, 17):
                h = multiple * conductor
                for frequency in (h, 16*h):
                    average = sum((mw.formal_character(frequency, x)
                                   for x in states), mw.PhasePoly.zero()) / n
                    self.assertEqual(average, mw.PhasePoly.one())

    def test_malformed_inputs_rejected(self):
        for length in (0, -1, True, 1.5):
            with self.assertRaises(ValueError):
                audit.authentic_normalized_shift_bound(length, 1)
        for h in (0, True, 1.0):
            with self.assertRaises(ValueError):
                audit.authentic_normalized_shift_bound(10, h)
        for q in (Q(-1, 3), Q(1), Q(2), 0.5):
            with self.assertRaises(ValueError):
                audit.bound_if_contraction(10, 1, q)
        with self.assertRaises(ValueError):
            audit.ladder_shift_audit([0], [], 1)
        with self.assertRaises(ValueError):
            audit.ladder_shift_audit([0, 1], [], 1)
        with self.assertRaises(ValueError):
            audit.ladder_shift_audit([0, 1], [1], 1, radix=1)


if __name__ == "__main__":
    unittest.main()
