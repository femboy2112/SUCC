"""Exact interventions, independent source matrices, intervals and hostile controls."""
from fractions import Fraction as Q
from itertools import combinations
import unittest

from observational_succ.source_faithful_observers import (
    ObserverSourceError, ArithmeticPin, quotient, carry_horizon_partition,
    carry_separator, recover_carry, carry_protocol, pin_arithmetic_entries,
    arithmetic_prime_holdout, off_diagonal_entry, polarized_entry,
)
from observational_succ.reality_pin_arithmetic import arithmetic_matrix_interval
from observational_succ.future_safe_quotient import (
    State, Edge, Machine, minimize, verify_certificate,
)


def contains(band, value):
    return band[0] <= value <= band[1]


def observed_partition(radix, horizon, block):
    """Direct source trajectory grouping, not the production closed formula."""
    groups = {}
    for r in range(radix):
        n = radix*(block-1)+r+1
        # Integer division independently checks the one-based source contract.
        trace = tuple((n+t-1)//radix+1 for t in range(horizon+1))
        groups.setdefault(trace, []).append(r)
    return tuple(map(tuple, groups.values()))


class CarryObserverTests(unittest.TestCase):
    def test_exact_horizon_partition_and_fresh_composite_radices(self):
        for radix in (2, 3, 5, 7, 4, 6, 11, 13):
            for block in (1, 2, 17):
                for h in range(radix+3):
                    expected = carry_horizon_partition(radix, h)
                    self.assertEqual(expected, observed_partition(radix, h, block))
                    self.assertEqual(len(expected), min(radix, h+1))

    def test_smallest_quotient_failure_and_minimal_separators(self):
        self.assertEqual(quotient(1, 2), quotient(2, 2))
        self.assertNotEqual(quotient(2, 2), quotient(3, 2))
        for p in (2, 3, 5, 7, 11):
            for a, b in combinations(range(1, 3*p+1), 2):
                t = carry_separator(a, b, p)
                self.assertNotEqual(quotient(a+t, p), quotient(b+t, p))
                self.assertTrue(all(quotient(a+s, p) == quotient(b+s, p) for s in range(t)))
            self.assertIsNone(carry_separator(p, p, p))

    def test_protocol_exact_cost_and_reconstruction(self):
        for p in (2, 3, 5, 7, 11):
            for n in range(1, 4*p+1):
                result = carry_protocol(n, p, Q(2, 3), Q(1, 7))
                self.assertEqual(result['source_reconstruction'], n)
                self.assertEqual(result['residue'], (n-1) % p)
                self.assertEqual(result['cost'], result['successor_actions']*Q(2, 3)
                                 +result['readings_count']*Q(1, 7))
                self.assertLessEqual(result['successor_actions'], p-1)
                self.assertFalse(result['physical_measurement_authenticated'])

    def test_worst_case_action_lower_bound(self):
        for p in (2, 3, 5, 7, 13):
            # r=0 and r=1 remain aliased before the last required step.
            self.assertEqual(tuple(quotient(1+t, p) for t in range(p-1)),
                             tuple(quotient(2+t, p) for t in range(p-1)))
            self.assertNotEqual(quotient(p, p), quotient(p+1, p))
            self.assertEqual(carry_protocol(1, p)['successor_actions'], p-1)

    def test_malformed_and_false_stopping_mutants_are_rejected(self):
        bad = ((3, 1, (1, 1)), (3, 1, (1, 2, 2)),
               (3, 1, (1, 3)), (3, 1, (2, 2)), (3, 1, (1, 1.0, 1)))
        for args in bad:
            with self.assertRaises(ObserverSourceError):
                recover_carry(*args)
        self.assertEqual(recover_carry(3, 1, (1, 1, 2)), 1)
        with self.assertRaises(ObserverSourceError):
            carry_protocol(1, 2, -1)

    def test_existing_finite_minimizer_agrees_on_closed_clock_control(self):
        # Separate cyclic control. Its theorem is not used for the unwrapped source.
        for p in (2, 3, 5, 7):
            n = 3*p
            machine = Machine(
                tuple(State(str(i), f'clock-{n}', str(i//p)) for i in range(n)),
                ('S',), tuple(Edge(str(i), 'S', str((i+1) % n), Q(1)) for i in range(n)))
            cert = minimize(machine)
            self.assertTrue(verify_certificate(machine, cert))
            self.assertEqual(len(cert.blocks), n)

    def test_null_probe_is_genuinely_coarse(self):
        machine = Machine(tuple(State(str(i), 'same-source', 'constant') for i in range(7)),
                          ('S',), tuple(Edge(str(i), 'S', str((i+1) % 7), Q(1)) for i in range(7)))
        self.assertEqual(len(minimize(machine).blocks), 1)

    def test_carry_origin_mutation_detected(self):
        # Wrong n//p source origin predicts a different earliest separator.
        self.assertEqual(quotient(1, 2), quotient(2, 2))
        self.assertNotEqual(1//2, 2//2)
        with self.assertRaises(ObserverSourceError):
            quotient(True, 2)


class ArithmeticObserverTests(unittest.TestCase):
    def test_polarization_cancels_common_energy_offset(self):
        # Direct quadratic forms in an arbitrary real symmetric rational matrix.
        # The factor 1/2 evaluates normalized +/- states without sqrt arithmetic.
        a = ((Q(7), Q(-2, 3)), (Q(-2, 3), Q(11)))
        gain, bias = Q(5, 7), Q(101)
        plus = gain*(a[0][0]+2*a[0][1]+a[1][1])/2+bias
        minus = gain*(a[0][0]-2*a[0][1]+a[1][1])/2+bias
        self.assertEqual(polarized_entry((plus, plus), (minus, minus)),
                         (gain*a[0][1], gain*a[0][1]))
        eps = Q(1, 1000)
        self.assertTrue(contains(polarized_entry((plus-eps, plus+eps),
                                                (minus-eps, minus+eps)), gain*a[0][1]))
        # A relative-sign swap reverses the extracted entry and is detectable.
        self.assertNotEqual(polarized_entry((minus, minus), (plus, plus)),
                            (gain*a[0][1], gain*a[0][1]))
        self.assertEqual(polarized_entry((plus, plus), (plus, plus)), (0, 0))

    def test_source_entries_match_independent_parent_matrix(self):
        for lam, sigma, gain in ((Q(1), 2, Q(1)), (Q(-2, 3), 3, Q(7, 5)),
                                 (Q(0), 4, Q(2, 7))):
            lo, hi = arithmetic_matrix_interval(11, lam, sigma)
            for i, j in combinations(range(1, 12), 2):
                value = off_diagonal_entry(11, i, j, lam, sigma, gain, Q(123))
                self.assertEqual(value, gain*lo[i-1][j-1])
                self.assertEqual(value, gain*hi[i-1][j-1])

    def test_unknown_gain_and_scalar_offset_recovery(self):
        for lam, sigma, gain, offset in ((Q(1), 2, Q(1), Q(0)),
             (Q(-2, 3), 3, Q(7, 5), Q(100)), (Q(0), 4, Q(2, 7), Q(-99))):
            values = tuple(off_diagonal_entry(11, i, j, lam, sigma, gain, offset)
                           for i, j in ((2, 3), (1, 3), (1, 5)))
            pin = pin_arithmetic_entries(*(tuple((v, v)) for v in values))
            self.assertTrue(contains(pin.sigma, sigma))
            self.assertTrue(contains(pin.gain, gain))
            self.assertTrue(contains(pin.lam, lam))
            self.assertLess(pin.sigma[1]-pin.sigma[0], Q(1, 10**8))
            self.assertFalse(pin.physical_measurement_authenticated)
            # These primes were not used to fit the model.
            for p in (7, 11):
                self.assertTrue(contains(arithmetic_prime_holdout(pin, p), gain/Q(p**sigma)))

    def test_quantitative_noisy_box_contains_fresh_holdout(self):
        lam, sigma, gain = Q(5, 7), 3, Q(4, 3)
        values = (gain*lam, gain/Q(3**sigma), gain/Q(5**sigma))
        eps = Q(1, 10**7)
        pin = pin_arithmetic_entries(*((v-eps, v+eps) for v in values))
        for box, truth in ((pin.sigma, sigma), (pin.gain, gain), (pin.lam, lam)):
            self.assertTrue(contains(box, truth))
        self.assertTrue(contains(arithmetic_prime_holdout(pin, 11), gain/Q(11**sigma)))

    def test_offset_invisible_and_holdout_kills_fitted_counterfeit(self):
        values = tuple(off_diagonal_entry(7, i, j, offset=999)
                       for i, j in ((2, 3), (1, 3), (1, 5)))
        same = tuple(off_diagonal_entry(7, i, j, offset=-23)
                     for i, j in ((2, 3), (1, 3), (1, 5)))
        self.assertEqual(values, same)
        pin = pin_arithmetic_entries(*((v, v) for v in values))
        predicted = arithmetic_prime_holdout(pin, 7)
        self.assertFalse(contains(predicted, Q(2, 49)))
        # Fitting three entries does not forbid this symmetric rank-two perturbation.
        self.assertTrue(contains(predicted, Q(1, 49)))

    def test_common_per_entry_bias_is_not_scalar_operator_offset(self):
        # Two different sigma/gain/bias tuples fit the same y,z and x when
        # 'offset' is incorrectly applied to every reported off-diagonal entry.
        y, z, x = Q(1, 9), Q(1, 25), Q(1)
        sigma2 = 3
        gain2 = (y-z)/(Q(1, 3**sigma2)-Q(1, 5**sigma2))
        bias2 = y-gain2/Q(3**sigma2)
        lam2 = (x-bias2)/gain2
        self.assertEqual(gain2/Q(3**sigma2)+bias2, y)
        self.assertEqual(gain2/Q(5**sigma2)+bias2, z)
        self.assertEqual(gain2*lam2+bias2, x)
        self.assertNotEqual((gain2, bias2, lam2), (1, 0, 1))

    def test_invalid_precision_source_and_prime_controls(self):
        for args in (((1, 1), (Q(1, 3), Q(1, 3)), (Q(1, 5), Q(1, 5))),
                     ((1, 1), (1, 2), (0, 1)),
                     ((1.0, 1.0), (Q(1, 9), Q(1, 9)), (Q(1, 25), Q(1, 25)))):
            with self.assertRaises(ObserverSourceError):
                pin_arithmetic_entries(*args)
        pin = pin_arithmetic_entries((1, 1), (Q(1, 9), Q(1, 9)), (Q(1, 25), Q(1, 25)))
        for bad in (2, 3, 5, 8, 9, True):
            with self.assertRaises(ObserverSourceError):
                arithmetic_prime_holdout(pin, bad)
        with self.assertRaises(ObserverSourceError):
            ArithmeticPin((Q(2), Q(3)), (Q(-1), Q(1)), (Q(0), Q(1)))


if __name__ == '__main__':
    unittest.main()
