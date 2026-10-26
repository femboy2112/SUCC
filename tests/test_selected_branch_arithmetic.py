"""Independent source, refractory-boundary, and carry mutation controls."""
from fractions import Fraction as Q
import unittest

from observational_succ.selected_branch_arithmetic import (
    authentic_spill_points, carry_branch_comparison,
    endpoint_totient_parity_energy, quarter_opposition_overlap, rational_dyadic_energy,
    spill_count_upper, spill_cutoff, spill_refractory_length,
)
from observational_succ.integer_bbp_carrier import source_states
from observational_succ.lambda_source_duality import (
    BranchDefect, Cyclo16, branch_fourier, verify_original_history,
)


def literal_force(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def generic_chi(rows):
    N = sum(map(sum, rows))
    return sum((Q(16*sum(c*c for c in row), N*sum(row))
                for row in rows if sum(row)), Q())-1


class SelectedBranchArithmeticTests(unittest.TestCase):
    def test_original_source_and_scaled_spills_against_integer_engine(self):
        independent = source_states(258)
        for scale in (1, 17, 4096):
            points = authentic_spill_points(257, scale)
            for point, previous, current in zip(points, independent[1:], independent[2:]):
                previous_q = Q(previous.numerator, previous.conductor)
                current_q = Q(current.numerator, current.conductor)
                self.assertEqual(point.original_lift, previous_q)
                self.assertEqual(point.original_forcing, literal_force(point.branch_index+1))
                self.assertEqual(point.scaled_literal_carry,
                                 (scale*current_q).__floor__()-16*(scale*previous_q).__floor__())
                self.assertEqual(point.spill,
                                 (16*((scale*previous_q) % 1)+scale*literal_force(point.branch_index+1)).__floor__()
                                 -(16*((scale*previous_q) % 1)).__floor__())
            self.assertLessEqual(sum(point.spill > 0 for point in points),
                                 spill_count_upper(257, scale))
        self.assertTrue(any(point.spill > 1 for point in authentic_spill_points(17, 4096)))

    def test_every_observed_scaled_spill_has_the_proved_zero_carry_interval(self):
        for scale in (3, 37, 1024):
            points = authentic_spill_points(512, scale)
            for index, point in enumerate(points):
                if point.spill:
                    for future in points[index+1:index+1+point.forced_zero_carry_steps]:
                        self.assertEqual(future.scaled_literal_carry, 0)

    def test_forced_spill_changed_seed_near_upper_boundary(self):
        # Independent fractional recurrence; force c=16 and j=15, preserving
        # every subsequent original forcing. This is NOT the zero-seed source.
        for k, scale in ((3, 1), (9, 1), (33, 1), (129, 1), (513, 1), (33, 17), (129, 257)):
            r = scale*literal_force(k)
            phase = 1-r/16000
            digit = (16*phase).__floor__()
            total = 16*phase+r
            self.assertEqual(digit, 15)
            self.assertEqual(total.__floor__(), 16)
            phase = total % 1
            self.assertEqual(phase, Q(999, 1000)*r)
            length = spill_refractory_length(k, scale)
            for ell in range(1, length+1):
                total = 16*phase+scale*literal_force(k+ell)
                self.assertLess(total, 1, (k, scale, ell))
                phase = total
        self.assertEqual([spill_refractory_length(k) for k in (3, 9, 33, 129, 513)],
                         [1, 2, 3, 4, 5])

    def test_positivity_without_decay_does_not_imply_sparse_spills(self):
        # x=1/32, r=17/32 is a fixed forced phase, with j=0,c=1 every step.
        x, r = Q(1, 32), Q(17, 32)
        for _ in range(32):
            self.assertEqual((16*x).__floor__(), 0)
            self.assertEqual((16*x+r).__floor__(), 1)
            self.assertEqual((16*x+r) % 1, x)
        self.assertFalse(verify_original_history((x,)*32))
        self.assertGreater(r, Q(15, 64*31**2))

    def test_cutoff_is_exact_integer_fourth_root_and_bounds_holdout_packing(self):
        for N in (1, 2, 17, 128, 1025):
            for scale in (1, 7, N, N*N, N*N+123):
                root = spill_cutoff(N, scale)-1
                self.assertLessEqual(root**4, scale*N*N)
                self.assertGreater((root+1)**4, scale*N*N)
                self.assertLessEqual(spill_count_upper(N, scale), N)
                # Greedy packing of ANY spill tape satisfying refractory intervals.
                k, packing = 2, []
                while k <= N+1:
                    packing.append(k)
                    k += spill_refractory_length(k, scale)+1
                self.assertLessEqual(len(packing), spill_count_upper(N, scale))
        self.assertLess(spill_count_upper(10**8, 10**8), 10**8)

    def test_arbitrary_cutoff_bound_against_actual_source(self):
        for N, scale in ((97, 1), (173, 31), (257, 257)):
            actual = sum(point.spill > 0 for point in authentic_spill_points(N, scale))
            for cutoff in (2, 3, 7, 31, N, N+1, N+2):
                self.assertLessEqual(actual, spill_count_upper(N, scale, cutoff))

    def test_same_bin_digit_carry_energy_and_endpoint_totient_identity(self):
        for N, bins in ((31, 3), (128, 7), (257, 13)):
            comparison = carry_branch_comparison(N, bins)
            digit, carry = comparison.digit_defect, comparison.carry_defect
            for h in (4, 8, 12, -4):
                digit_energy = rational_dyadic_energy(digit.counts, h)
                carry_energy = rational_dyadic_energy(carry.counts, h)
                self.assertEqual(digit.conditional_mode_energy(h), Cyclo16.one()*digit_energy)
                self.assertEqual(carry.conditional_mode_energy(h), Cyclo16.one()*carry_energy)
                self.assertLessEqual(abs(digit_energy-carry_energy),
                                     comparison.universal_mode_energy_error_upper)
            self.assertEqual(endpoint_totient_parity_energy(carry.counts),
                             rational_dyadic_energy(carry.counts, 8))
            self.assertEqual(rational_dyadic_energy(carry.counts, 4),
                             (1+rational_dyadic_energy(carry.counts, 8))/2
                             -4*quarter_opposition_overlap(carry.counts))
            self.assertLessEqual(abs(digit.chi_squared-carry.chi_squared),
                                 comparison.universal_chi_squared_error_upper)

    def test_quarter_turn_is_not_determined_by_parity_energy(self):
        # Equal even/odd masses can have maximal surviving quarter-turn magnitude.
        first = ((8, 8)+(0,)*14,)
        second = ((4, 4, 4, 4)+(0,)*12,)
        self.assertEqual(rational_dyadic_energy(first, 8), 0)
        self.assertEqual(rational_dyadic_energy(second, 8), 0)
        self.assertEqual(rational_dyadic_energy(first, 4), Q(1, 2))
        self.assertEqual(rational_dyadic_energy(second, 4), 0)
        self.assertEqual(quarter_opposition_overlap(first), 0)
        self.assertEqual(quarter_opposition_overlap(second), Q(1, 8))

    def test_single_carry_relabel_costs_and_literal_sixteen(self):
        for size in (2, 7, 19, 100):
            for old in range(16):
                first = [0]*16
                first[old] = size
                second = first.copy()
                second[old] -= 1
                second[(old+1) % 16] += 1
                for h in (4, 8, 12):
                    self.assertLessEqual(abs(rational_dyadic_energy((first,), h)
                                             -rational_dyadic_energy((second,), h)), Q(4, size))
                self.assertLessEqual(abs(generic_chi((first,))-generic_chi((second,))), Q(32, size))
        # Carry 16's character is that of residue zero; it must not be discarded.
        self.assertEqual(Cyclo16.zeta(8*16), Cyclo16.one())
        self.assertEqual(Cyclo16.zeta(8*15), -Cyclo16.one())

    def test_invalid_observers_and_tables_are_rejected(self):
        for call in (lambda: spill_refractory_length(1),
                     lambda: spill_count_upper(0),
                     lambda: spill_count_upper(5, 0),
                     lambda: spill_cutoff(True),
                     lambda: authentic_spill_points(2000),
                     lambda: carry_branch_comparison(2000),
                     lambda: carry_branch_comparison(5, 0),
                     lambda: rational_dyadic_energy(((0,)*16,), 8),
                     lambda: rational_dyadic_energy(((1,)*16,), 2),
                     lambda: rational_dyadic_energy(((1,)*15,), 8)):
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
