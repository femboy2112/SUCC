"""Exact controls for the positive carry/conductor counterfeit and rigidity."""
from fractions import Fraction as Q
from math import lcm
import unittest

from observational_succ.bbp_positive_carry_control import (
    backward_phase_prefix, positive_carry_control,
    positive_control_tail_constants, quartic_conductor_lower,
)
from observational_succ.integer_bbp_carrier import source_states
from observational_succ.succ_internal_matrix_walk import authentic_r


class PositiveCarryControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.points = positive_carry_control(512)

    def test_independent_literal_source_and_carry_replay(self):
        source = control = Q()
        for row in self.points:
            n = row.time
            literal = Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
            next_source = 16*source+literal
            self.assertEqual(row.authentic_lift, next_source)
            self.assertEqual(row.authentic_forcing, literal)
            source_carry = (16*(source % 1)+literal).__floor__()
            control_carry = (16*(control % 1)+row.control_forcing).__floor__()
            self.assertEqual(row.carry, source_carry)
            self.assertEqual(control_carry, source_carry)
            self.assertEqual(row.control_lift, 16*control+row.control_forcing)
            source, control = next_source, row.control_lift

    def test_exact_common_conductor_against_integer_source(self):
        integers = source_states(512)
        cumulative = 1
        for row, integer in zip(self.points, integers[1:]):
            cumulative = lcm(cumulative, row.control_forcing.denominator)
            self.assertEqual(row.common_conductor, integer.conductor)
            self.assertEqual(cumulative, integer.conductor)
            self.assertEqual(row.common_conductor % row.control_phase.denominator, 0)

    def test_positive_forcing_floor_lifts_and_zero_events(self):
        for row in self.points:
            self.assertGreater(row.control_forcing, 0)
            self.assertLess(row.control_forcing, 17)
            self.assertEqual(row.control_lift.__floor__(), row.authentic_lift.__floor__())
            self.assertGreaterEqual(row.control_phase, 0)
            self.assertLessEqual(row.control_phase, row.authentic_lift % 1)
            self.assertEqual(row.control_phase == 0, row.authentic_zero_phase)
            self.assertLess(abs(row.control_lift-row.authentic_lift), 1)

    def test_reset_rule_and_changed_source_not_mislabelled(self):
        self.assertEqual(self.points[0].control_forcing, Q(46,15))
        self.assertNotEqual(self.points[0].control_forcing, authentic_r(1))
        previous = Q()
        for row in self.points:
            expected = (Q() if row.authentic_zero_phase else
                        max(Q(1,row.common_conductor),
                            16*previous-row.carry+Q(1,row.common_conductor)))
            self.assertEqual(row.control_phase, expected)
            if row.reset:
                self.assertIn(row.control_phase, (Q(), Q(1,row.common_conductor)))
            previous = row.control_phase
        self.assertTrue(any(row.control_forcing > 1 for row in self.points[256:]))

    def test_repairs_negative_forcing_in_previous_carry_control(self):
        old, new = self.points[12], self.points[13]
        previous_shortcut = Q(old.authentic_lift.__floor__())+Q(1,old.common_conductor)
        next_shortcut = Q(new.authentic_lift.__floor__())+Q(1,new.common_conductor)
        self.assertLess(next_shortcut-16*previous_shortcut, 0)
        self.assertEqual(new.carry, 0)
        self.assertEqual(new.control_forcing, Q(1,new.common_conductor))
        self.assertGreater(new.control_phase, 16*old.control_phase)

    def test_source_quartic_lower_on_independent_prefix(self):
        for row in self.points:
            self.assertGreater(row.common_conductor, quartic_conductor_lower(row.time))
            self.assertGreater(row.authentic_forcing, Q(1,16*row.time**2))

    def test_large_index_prime_power_and_reset_constant_holdouts(self):
        for n in (19999,20000,20001,20010,65537,1000003):
            self.assertGreater(authentic_r(n), Q(1,16*n*n))
            product = 1
            for p in (7,11,13,17):
                power = 1
                while power*p <= 2*n-1:
                    power *= p
                product *= power
                if power > 1:
                    force = authentic_r((power+1)//2)
                    self.assertEqual(force.denominator % power, 0)
            self.assertGreater(product, quartic_conductor_lower(n))
        constants = positive_control_tail_constants()
        self.assertLess(constants["zero_run_phase_constant"]/20000**2, Q(1,16))
        self.assertGreater(Q(16**9,32*20001**2),1)
        self.assertFalse(constants["authentic_four_pole_forcing"])
        self.assertFalse(constants["vanishing_forcing_preserved"])

    def test_actual_zero_carry_run_bound(self):
        # Check the finite instances of the independently proved all-N bound.
        last_nonzero = 0
        for row in self.points:
            if row.carry:
                last_nonzero = row.time
            else:
                length = row.time-last_nonzero
                self.assertLess(16**length, 256*(last_nonzero+1)**2)

    def test_backward_common_carry_identity_at_unfitted_windows(self):
        for start, depth in ((0,1),(0,8),(7,23),(31,64),(257,127)):
            old_diff = (Q() if start == 0 else
                        self.points[start-1].control_phase-self.points[start-1].authentic_lift%1)
            end = self.points[start+depth-1]
            end_diff = end.control_phase-end.authentic_lift%1
            tape = tuple(row.control_forcing-row.authentic_forcing
                         for row in self.points[start:start+depth])
            prefix = backward_phase_prefix(tape, depth)
            self.assertEqual(old_diff, prefix+end_diff/16**depth)
            self.assertLess(abs(old_diff-prefix), Q(1,16**depth))

    def test_full_seed_limit_is_retained_by_bounded_lift_difference(self):
        for n in (1,17,65,257,511):
            row = self.points[n-1]
            self.assertLess(abs(row.control_lift/16**n-row.authentic_lift/16**n),
                            Q(1,16**n))

    def test_invalid_inputs(self):
        for n in (-1,True,2001):
            with self.assertRaises(ValueError):
                positive_carry_control(n)
        with self.assertRaises(ValueError):
            backward_phase_prefix((0.5,),1)
        with self.assertRaises(ValueError):
            backward_phase_prefix((),1)


if __name__ == "__main__":
    unittest.main()
