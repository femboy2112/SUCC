"""Mutation-hardening tests for the pin-bed bound functions.

Each test compares a certified bound with a "truth" quantity computed
independently of the bound under test (direct summation, exact arithmetic,
or a self-contained Machin pi). Targets (mutants this file must kill):
  M1 completed_surface_translation_bound_squared: tail term deleted.
  M2 learning_pinbed.guard_margin: inflated (1.9x).
  M3 b2_scan_alias_bound: 6h^2/M^2 replaced by a linear 3|h|/(2M).
  M4 energy_transfer_bound: divided by 1000.
  M5 Learner.choose_mode: always returns the first menu entry.
"""
import cmath
import math
import unittest
from collections import Counter
from fractions import Fraction as Q

from observational_succ.driven_pinbed_observer import b2_scan_alias_bound
from observational_succ.fourier_yoneda_pinbed import (
    CircleLaw, completed_surface_translation_bound_squared, pin_surface,
    surface_distance_squared)
from observational_succ.learning_pinbed import (
    Learner, guard_margin, guarded_pin, learn_guarded_seed, learn_true_seed,
    oscillator_pin)
from observational_succ.pinbed_oscillator_bridge import (
    energy_pair, energy_transfer_bound, source_history)


def _point_distance_squared(d):
    """||F_0 - F_d||^2 for two Diracs at circle distance d: d^2(1-d)^2/3."""
    d = d % 1
    return d*d*(1-d)*(1-d)/3


def _full_completed_distance_lower(delta, b, rho, terms=400):
    """Partial sum of sum_j rho^j D(b^j delta): a LOWER bound of the full series."""
    return sum((rho**j*_point_distance_squared(b**j*delta) for j in range(terms)),
               Q(0))


class TranslationBoundTailTests(unittest.TestCase):
    def test_point_distance_formula_matches_module_surface_distance(self):
        for d in (Q(1, 100), Q(1, 7), Q(1, 2), Q(2, 3)):
            law0 = CircleLaw(((Q(0), Q(1)),))
            lawd = CircleLaw(((d, Q(1)),))
            self.assertEqual(surface_distance_squared(law0, lawd),
                             _point_distance_squared(d))

    def test_demonstrated_tail_counterexample(self):
        delta, b, rho, depth = Q(1, 100), 2, Q(3, 4), 4
        full = _full_completed_distance_lower(delta, b, rho)
        tailless = delta**2/3*sum(((rho*b*b)**j for j in range(depth+1)), Q(0))
        self.assertGreater(full, tailless)
        self.assertGreaterEqual(
            completed_surface_translation_bound_squared(delta, b, rho, depth), full)

    def test_bound_dominates_full_completed_distance(self):
        for delta in (Q(1, 1000), Q(1, 100), Q(1, 50), Q(1, 7), Q(1, 3),
                      Q(1, 2), Q(9, 10), Q(1)):
            for b in (2, 3, 16):
                for rho in (Q(1, 10), Q(1, 2), Q(3, 4)):
                    full = _full_completed_distance_lower(delta, b, rho)
                    for depth in range(0, 8):
                        bound = completed_surface_translation_bound_squared(
                            delta, b, rho, depth)
                        self.assertGreaterEqual(
                            bound, full, (delta, b, rho, depth))

    def test_tail_is_needed_for_large_depth_independent_of_partial_sum(self):
        # At depth 0 the bound must still cover all terms j >= 1.
        delta, b, rho = Q(1, 100), 2, Q(3, 4)
        full = _full_completed_distance_lower(delta, b, rho)
        self.assertGreaterEqual(
            completed_surface_translation_bound_squared(delta, b, rho, 0), full)


class GuardMarginTests(unittest.TestCase):
    def test_margin_is_half_the_candidate_grid_step(self):
        for depth in range(1, 6):
            for t in range(depth):
                self.assertEqual(guard_margin(depth, t),
                                 Q(1, 2*16**(depth-t)))

    def test_errors_strictly_below_true_margin_decode_correctly(self):
        for depth in (1, 2):
            for t in range(depth):
                margin = Q(1, 2*16**(depth-t))
                for k in range(0, 16**depth, 3 if depth == 2 else 1):
                    ideal = oscillator_pin(k, depth, t)
                    for e in (margin - Q(1, 16**(depth+3)),
                              -(margin - Q(1, 16**(depth+3))), Q(0)):
                        self.assertEqual(guarded_pin(k, depth, t, e), ideal)

    def test_demonstrated_error_beyond_true_margin_flips_digit(self):
        # 3/64 = 1.5 x true margin at depth 1: label flips, so it must be rejected.
        self.assertEqual(oscillator_pin(5, 1, 0), 5)
        self.assertEqual(guarded_pin(5, 1, 0, Q(3, 64)), 6)
        with self.assertRaises(ValueError):
            learn_guarded_seed(1, 5, (Q(3, 64),))

    def test_errors_at_or_above_true_margin_are_rejected(self):
        for depth in (1, 2):
            margin = Q(1, 2*16**depth)  # time 0, the first observation
            for e in (margin, -margin, margin*Q(10001, 10000),
                      -margin*Q(10001, 10000), margin*Q(3, 2), 2*margin):
                errors = (e,) + (Q(0),)*(depth-1)
                with self.assertRaises(ValueError, msg=(depth, e)):
                    learn_guarded_seed(depth, 5, errors)

    def test_accepted_errors_never_yield_a_wrong_seed(self):
        # Soundness sweep: any error the protocol accepts must still identify k.
        for k in range(16):
            for num in range(-40, 41):
                e = Q(num, 256)
                try:
                    learner = learn_guarded_seed(1, k, (e,))
                except ValueError:
                    continue
                self.assertEqual(learner.possible, (k,), (k, e))


class AliasBoundTests(unittest.TestCase):
    @staticmethod
    def _alias_error(law, pins, mode):
        """|2 pi^2 h^2 Y_h - m_h| with Y_h summed directly from pin_surface."""
        y = sum((complex(pin_surface(law, Q(j, pins)))
                 * cmath.exp(-2j*math.pi*mode*j/pins) for j in range(pins)), 0j)/pins
        z = 2*math.pi**2*mode*mode*y
        m = sum(complex(p)*cmath.exp(-2j*math.pi*mode*float(x))
                for x, p in law.atoms)
        return abs(z - m)

    def test_demonstrated_delta0_counterexample(self):
        err = self._alias_error(CircleLaw(((Q(0), Q(1)),)), 4, 2)
        self.assertAlmostEqual(err, math.pi**2/4 - 1, places=9)
        self.assertGreater(err, 3*2/(2*4))  # linear mutant bound 0.75
        self.assertLessEqual(err, float(b2_scan_alias_bound(4, 2)))

    def test_alias_bound_dominates_actual_error_near_band_edge(self):
        laws = (CircleLaw(((Q(0), Q(1)),)),
                CircleLaw(((Q(1, 4), Q(1)),)),
                CircleLaw(((Q(0), Q(1, 2)), (Q(1, 2), Q(1, 2)))),
                CircleLaw(((Q(0), Q(1, 3)), (Q(1, 3), Q(1, 3)), (Q(2, 3), Q(1, 3)))))
        for pins in (4, 6, 8, 10, 12, 16, 20):
            for mode in range(1, pins//2 + 1):
                bound = float(b2_scan_alias_bound(pins, mode))
                for law in laws:
                    err = self._alias_error(law, pins, mode)
                    self.assertLessEqual(err, bound + 1e-12, (pins, mode))

    def test_delta0_band_edge_error_exceeds_any_linear_candidate(self):
        # h = M/2: actual error stays above 3h/(2M) = 3/4 for every even M.
        for pins in (4, 6, 8, 10, 20, 40):
            err = self._alias_error(CircleLaw(((Q(0), Q(1)),)), pins, pins//2)
            self.assertGreater(err, 0.75, pins)
            self.assertLessEqual(err, float(b2_scan_alias_bound(pins, pins//2)))


def _pi_scaled(digits):
    """floor(pi * 10^digits) by Machin: pi = 16 atan(1/5) - 4 atan(1/239)."""
    guard = 20
    scale = 10**(digits + guard)

    def arctan_inv(x):
        term = total = scale//x
        n, sign = 1, 1
        while term:
            term //= x*x
            n += 2
            sign = -sign
            total += sign*(term//n)
        return total
    return (16*arctan_inv(5) - 4*arctan_inv(239))//10**guard


class EnergyTransferBoundTests(unittest.TestCase):
    DIGITS = 400
    PI_INT = _pi_scaled(DIGITS)

    def _completed_pi_epoch(self, a_epoch):
        """Exact rationals 16^(k-1) pi mod 1 for k in [A,2A): completed-pi side."""
        scale = 10**self.DIGITS
        return tuple(Q((16**(k-1)*self.PI_INT) % scale, scale)
                     for k in range(a_epoch, 2*a_epoch))

    def test_pi_helper_is_pi(self):
        self.assertTrue(str(self.PI_INT).startswith("31415926535897932384626433832795"))

    def test_energy_difference_within_bound_on_real_epochs(self):
        golden = (5**0.5 - 1)/2
        for aperture in (golden, 0.25, 0.5, 0.9):
            for epoch in (4, 8, 16, 32, 64):
                source = source_history(2*epoch)[epoch:2*epoch]
                completed = self._completed_pi_epoch(epoch)
                diff = abs(energy_pair(source, aperture)
                           - energy_pair(completed, aperture))
                self.assertLessEqual(
                    diff, energy_transfer_bound(aperture, epoch),
                    (aperture, epoch))


class ChooseModeMenuTests(unittest.TestCase):
    @staticmethod
    def _worst_bin(learner, time, mode):
        counts = Counter(oscillator_pin(i, learner.depth, time, mode)
                         for i in learner.possible)
        return max(counts.values())

    def test_minimax_choice_beats_first_menu_entry(self):
        learner = Learner.full_grid(1)
        for menu in ((2, 1), (8, 4, 1), (4, 2), (8, 2, 5)):
            worst = {h: self._worst_bin(learner, 0, h) for h in menu}
            best = min(worst.values())
            chosen = learner.choose_mode(0, menu)
            self.assertEqual(worst[chosen], best, menu)
        self.assertGreater(self._worst_bin(learner, 0, 2),
                           self._worst_bin(learner, 0, 1))
        self.assertEqual(learner.choose_mode(0, (2, 1)), 1)
        self.assertEqual(learner.choose_mode(0, (4, 2)), 2)

    def test_learning_with_nondefault_menu_identifies_seed(self):
        learner = learn_true_seed(1, 7, (2, 1))
        self.assertEqual(learner.possible, (7,))
        self.assertEqual(learner.transcript[0].harmonic, 1)

    def test_no_discriminating_mode_returns_none(self):
        learner = Learner.full_grid(2).observe(0, 1, oscillator_pin(7, 2, 0, 1))
        # mode 1 at t=0 carries no further information on the survivors.
        self.assertIsNone(learner.choose_mode(0, (1,)))
        self.assertEqual(learner.choose_mode(0, (1, 2)), 2)


if __name__ == "__main__":
    unittest.main()
