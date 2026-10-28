"""Independent source replay and hostile checks for conditional carry transport."""
from fractions import Fraction as Q
from random import Random
import unittest

from observational_succ.lambda_source_duality import (
    Cyclo16, branch_defect, original_history,
)
from observational_succ.pi_succ_character_intervals import fourier_squared_interval
from observational_succ.selected_branch_transport import (
    ConditionalTable, midpoint_rectangle, record_change_bounds, source_branch_records,
    source_energy_transport_budget, source_signed_certificate, source_tables,
)
from observational_succ.selected_branch_arithmetic import (
    authentic_spill_points, spill_count_upper,
)


def independent_source(N):
    u, values = Q(), []
    for n in range(1, N+1):
        r = Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)
        u = 16*u+r
        values.append(u)
    return tuple(values)


class ConditionalTransportTests(unittest.TestCase):
    def test_native_source_and_literal_records_independently(self):
        states = independent_source(257)
        self.assertEqual(states, original_history(257))
        for M in (1, 3, 16, 37):
            rec = source_branch_records(states, M)
            for n, ((b, j), (a, c)) in enumerate(zip(rec['original'], rec['future']), 1):
                x, y = states[n-1] % 1, states[n] % 1
                r = states[n]-16*states[n-1]
                t = 16*x-j
                self.assertEqual(x, (c+y-r)/16)
                self.assertEqual(t, (y-r) % 1)
                sigma = (M*t+M*r).__floor__()-(M*t).__floor__()
                self.assertEqual(a, (b+sigma) % M)
                if a != b:
                    self.assertGreater(sigma, 0)

    def test_parent_conditional_table_and_cyclotomic_parseval(self):
        states = independent_source(114)
        for M in (2, 5, 11):
            old, future, _ = source_tables(states, M)
            parent = branch_defect(states[:-1], M)
            self.assertEqual(old.chi_squared(), parent.chi_squared)
            for table in (old, future):
                total = sum((table.energy(h) for h in range(1, 16)), Cyclo16.zero())
                self.assertEqual(total, table.chi_squared()*Cyclo16.one())
                self.assertEqual(table.rational_energy(8), table.totient_parity_energy())
            for h in (4, 8, 12):
                self.assertEqual(old.energy(h), parent.conditional_mode_energy(h))

    def test_universal_replacement_bound_with_bin_and_label_mutations(self):
        rng = Random(20261026)
        for N, M in ((1, 1), (7, 3), (19, 6), (43, 12), (79, 7)):
            first = tuple((rng.randrange(M), rng.randrange(16)) for _ in range(N))
            second = list(first)
            for i in range(0, N, 5):
                second[i] = (rng.randrange(M), rng.randrange(16))
            a, b = (ConditionalTable.from_records(records, M) for records in (first, second))
            budget = record_change_bounds(first, second)
            self.assertLessEqual(abs(a.chi_squared()-b.chi_squared()), budget['chi_squared_error'])
            for h in (4, 8, 12, -4, -8):
                self.assertLessEqual(abs(a.rational_energy(h)-b.rational_energy(h)),
                                     budget['mode_energy_error'])

    def test_replacement_constants_are_asymptotically_sharp(self):
        N = 101
        a = ConditionalTable.from_records(((0, 0),)*N, 1)
        b = ConditionalTable.from_records(((0, 0),)*(N-1)+((0, 1),), 1)
        self.assertEqual(a.rational_energy(8)-b.rational_energy(8), Q(4*(N-1), N*N))
        self.assertEqual(a.chi_squared()-b.chi_squared(), Q(32*(N-1), N*N))
        self.assertGreater(a.rational_energy(8)-b.rational_energy(8), Q(3, N))

    def test_row_reassignment_requires_its_own_budget(self):
        a = ConditionalTable.from_records(((0, 0), (0, 1)), 2)
        b = ConditionalTable.from_records(((0, 0), (1, 1)), 2)
        self.assertEqual(a.rational_energy(8), 0)
        self.assertEqual(b.rational_energy(8), 1)
        self.assertEqual(a.chi_squared(), 7)
        self.assertEqual(b.chi_squared(), 15)

    def test_source_spill_budget_covers_joint_changes_and_energy(self):
        for N, M in ((13, 2), (47, 5), (129, 16), (257, 63)):
            before, after, records = source_tables(independent_source(N+1), M)
            actual = record_change_bounds(records['original'], records['future'])
            prior = source_energy_transport_budget(N, M)
            self.assertLessEqual(records['digit_changes'], spill_count_upper(N, 1))
            self.assertLessEqual(records['bin_changes'], spill_count_upper(N, M))
            self.assertLessEqual(actual['changed_records'], prior['changed_records_upper'])
            for h in (4, 8, 12):
                self.assertLessEqual(abs(before.rational_energy(h)-after.rational_energy(h)),
                                     actual['mode_energy_error'])
            self.assertFalse(prior['energy_decay_proved'])

    def test_growing_bins_analytic_budget_at_huge_integer_horizons(self):
        errors = []
        for exponent in (64, 256, 1024):
            N = 1 << exponent
            b = source_energy_transport_budget(N, exponent)
            errors.append(b['mode_energy_error'])
        self.assertTrue(errors[0] > errors[1] > errors[2] > 0)
        self.assertLess(errors[-1], Q(1, 10))

    def test_signed_certificate_against_independent_original_phase_rectangles(self):
        for N, M, h in ((29, 8, 1), (71, 16, -3), (113, 32, 8), (37, 16, 16)):
            states = independent_source(N+1)
            cert = source_signed_certificate(states, M, h)
            _, actual_upper = fourier_squared_interval(states[:-1], h)
            self.assertLessEqual(actual_upper, cert['normalized_modulus_upper']**2)
            self.assertFalse(cert['asymptotic_cancellation_proved'])
            self.assertFalse(cert['pi_normality_proved'])
        cert = source_signed_certificate(independent_source(129), 32, 1)
        self.assertLess(cert['normalized_modulus_upper'], Q(1, 2))

    def test_signed_cross_bin_cancellation_survives_maximal_conditional_energy(self):
        # Three singleton bins, with midpoint phases 1/96 + k/3.
        table = ConditionalTable.from_records(((0, 0), (1, 5), (2, 10)), 3)
        self.assertEqual(table.rational_energy(8), 1)
        self.assertEqual(table.chi_squared(), 15)
        box = midpoint_rectangle(table, 8)
        self.assertLess(max(abs(x) for x in box), Q(1, 10**10))

    def test_source_mutations_fail_closed(self):
        states = independent_source(20)
        mutants = [(Q(),)*20, tuple(u+Q(16**n, 7) for n, u in enumerate(states, 1))]
        mutated = list(states)
        mutated[9] += Q(1, 999)
        mutants.append(tuple(mutated))
        for bad in mutants:
            with self.assertRaises(ValueError):
                source_signed_certificate(bad, 4, 1)

    def test_exact_domains_and_sparse_large_bins(self):
        table = ConditionalTable.from_records(((0, 16), (10**30-1, -1)), 10**30)
        self.assertEqual(len(table.rows), 2)
        self.assertEqual(table.chi_squared(), 15)
        for bad in (True, 1.0, Q(2)):
            with self.assertRaises(ValueError):
                ConditionalTable.from_records(((0, 0),), bad)
        with self.assertRaises(ValueError):
            ConditionalTable(2, 1, ((0, (1,)+(0,)*15),))
        with self.assertRaises(ValueError):
            table.rational_energy(1)
        with self.assertRaises(ValueError):
            source_signed_certificate(independent_source(10), 4, 0)


if __name__ == '__main__':
    unittest.main()
