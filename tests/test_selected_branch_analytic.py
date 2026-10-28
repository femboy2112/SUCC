"""Independent finite witnesses for actual same-forcing branch obstructions."""
import unittest
from fractions import Fraction as Q

from observational_succ.finite_fourier_carrier import CyclotomicElement
from observational_succ.lambda_source_duality import (
    Cyclo16, branch_defect, verify_original_history,
)
from observational_succ.selected_branch_analytic import (
    PeriodicGreenSelector, SparsePeriodicGreenSelector, certified_control_cell,
    certified_control_table, rational_selector_approximation,
    sparse_tail_interval, sparse_total_upper,
)


def literal_r(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


class PeriodicArithmetic(unittest.TestCase):
    def test_exact_order_and_complete_coset_on_fresh_exponents(self):
        for k in (2, 3, 4, 6, 8):
            q = 3**k
            for p in (1, 2, q-1):
                control = PeriodicGreenSelector(k, p)
                residues = control.periodic_residues()
                self.assertEqual(len(set(residues)), q//3)
                self.assertEqual(set(residues), set(range(p % 3, q, 3)))
                self.assertEqual(pow(16, control.period, q), 1)
                self.assertNotEqual(pow(16, control.period//3, q), 1)

    def test_cyclotomic_period_sum_independent_of_structural_formula(self):
        for k, p in ((2, 1), (3, 2), (4, 5)):
            control = PeriodicGreenSelector(k, p)
            q, length = control.conductor, control.period
            for h in (0, 1, -2, length-1, length, 2*length):
                actual = CyclotomicElement.scalar(q, 0)
                for n in range(1, length+1):
                    actual += CyclotomicElement.root(q, h*p*pow(16, n, q))
                amplitude, phase = control.periodic_character(h)
                expected = CyclotomicElement.root(q, int(q*phase)).scale(length*amplitude)
                self.assertEqual(actual, expected)

    def test_arbitrarily_large_finite_band_and_surviving_next_mode(self):
        for k in (2, 3, 5, 7):
            control = PeriodicGreenSelector(k)
            for h in range(1, control.period):
                self.assertEqual(control.periodic_character(h), (0, 0))
            self.assertEqual(control.periodic_character(control.period), (1, Q(1, 3)))

    def test_period_tail_budget_and_uniform_green_cost(self):
        control = PeriodicGreenSelector(3)
        for n in (1, 8, 9, 10, 17, 18, 113):
            remainder = n % control.period
            self.assertEqual(control.finite_mode_error_upper(n, 2),
                             Q(min(remainder, control.period-remainder), n)+Q(22, 56*n))
            self.assertEqual(control.finite_mode_error_upper(n, 9), Q(99, 56*n))


class CertifiedRealAndRationalControls(unittest.TestCase):
    def test_tail_intervals_independent_literal_prefix_and_enclosure(self):
        control = PeriodicGreenSelector(3, 2)
        for n in (1, 7, 19, 41):
            cell = certified_control_cell(control, n, 53)
            terms = cell.tail_terms
            a = Q(control.residue(n), control.conductor)
            short = sum((literal_r(n+j)*Q(1, 16**j)
                         for j in range(1, terms+1)), Q())
            cap = literal_r(n+terms+1)*Q(1, 15*16**terms)
            raw_lower, raw_upper = a-short-cap, a-short
            winding = raw_lower.__floor__()
            self.assertEqual((cell.lower_phase, cell.upper_phase),
                             (raw_lower-winding, raw_upper-winding))
            self.assertEqual((16*cell.lower_phase).__floor__(), cell.digit)
            self.assertEqual((16*cell.upper_phase).__floor__(), cell.digit)
            self.assertEqual((53*(16*cell.lower_phase-cell.digit)).__floor__(), cell.tail_bin)
            self.assertEqual((53*(16*cell.upper_phase-cell.digit)).__floor__(), cell.tail_bin)

    def test_late_bins_have_exactly_one_digit_at_every_checked_resolution(self):
        for k, p, n in ((2, 1, 43), (3, 2, 59), (4, 5, 97)):
            control = PeriodicGreenSelector(k, p)
            for m in (control.conductor, control.conductor+1, 4*control.conductor+3):
                cells = tuple(certified_control_cell(control, i, m)
                              for i in range(control.stable_from, n+1))
                defect = branch_defect(tuple(c.representative for c in cells), m, authenticate=False)
                self.assertEqual(defect.chi_squared, 15)
                self.assertTrue(all(sum(c != 0 for c in row) <= 1 for row in defect.counts))
                for h in range(1, 16):
                    self.assertEqual(defect.conditional_mode_energy(h), Cyclo16.one())

    def test_uniform_all_N_conditional_bounds_on_holdout_tables(self):
        for k, p, n, m in ((2, 2, 17, 23), (3, 1, 71, 127), (4, 5, 103, 509)):
            control = PeriodicGreenSelector(k, p)
            table = certified_control_table(control, n, m)
            e_lower, delta_lower = control.energy_lower_bounds(n, m)
            self.assertGreaterEqual(table.defect.chi_squared, delta_lower)
            self.assertGreaterEqual(table.defect.exact_parity_energy(), e_lower)
            e4 = table.defect.conditional_mode_energy(4)
            self.assertEqual(e4.coefficients[1:], (Q(),)*7)
            self.assertGreaterEqual(e4.coefficients[0], e_lower)
            self.assertTrue(table.source_forcing_preserved)
            self.assertFalse(table.authentic_zero_anchor)

    def test_real_initial_interval_excludes_authentic_zero(self):
        for control in (PeriodicGreenSelector(2), PeriodicGreenSelector(3, 2),
                        PeriodicGreenSelector(4, 5)):
            lower, upper = control.initial_interval()
            self.assertTrue(upper < 0 or lower > 0)
            self.assertFalse(control.authentic_zero_anchor)

    def test_same_forcing_rational_approximants_and_exact_backward_formula(self):
        for k, p, n in ((2, 1, 11), (3, 2, 23), (4, 5, 31)):
            control = PeriodicGreenSelector(k, p)
            approximation = rational_selector_approximation(control, n, extra_terms=7)
            state = approximation.initial
            for t, actual in enumerate(approximation.states, 1):
                self.assertEqual(actual, 16*state+literal_r(t))
                partial_tail = sum((literal_r(t+j)*Q(1, 16**j)
                                    for j in range(1, n+7-t+1)), Q())
                self.assertEqual(actual, 16**t*control.endpoint-partial_tail)
                state = actual
            self.assertGreater(approximation.state_error_upper, 0)
            self.assertFalse(verify_original_history(approximation.states))
            real_table = certified_control_table(control, n, control.conductor)
            rational_table = branch_defect(approximation.states, control.conductor, authenticate=False)
            self.assertEqual(real_table.defect.counts, rational_table.counts)

    def test_source_sign_mutation_breaks_independent_recurrence(self):
        approximation = rational_selector_approximation(PeriodicGreenSelector(2), 13)
        n = 5
        changed = literal_r(n)+Q(4, 8*n-4)
        self.assertNotEqual(approximation.states[n-1], 16*approximation.states[n-2]+changed)

    def test_quantifier_and_type_failures_are_not_silently_accepted(self):
        for args in ((True, 1), (1, 1), (3, 3), (3, 27), (3, 0)):
            with self.assertRaises(ValueError):
                PeriodicGreenSelector(*args)
        control = PeriodicGreenSelector(3)
        with self.assertRaises(ValueError):
            control.energy_lower_bounds(10, 26)
        with self.assertRaises(ValueError):
            control.periodic_character(True)
        with self.assertRaises(ValueError):
            certified_control_cell(control, 1, 4097)
        with self.assertRaises(ValueError):
            rational_selector_approximation(control, 0)


class SparseFiniteTypeControls(unittest.TestCase):
    def test_sparse_green_intervals_against_independent_powers(self):
        for n in (0, 1, 7, 31, 63, 127):
            lower, upper = sparse_tail_interval(n, 80)
            direct = sum((Q(1, 16**(2**k-n)) for k in range(10) if 2**k > n), Q())
            self.assertLessEqual(lower, direct)
            self.assertLess(direct, upper)
        for n in (1, 7, 31, 63):
            certified_upper = sum((sparse_tail_interval(t, 64)[1]
                                   for t in range(1, n+1)), Q())
            self.assertLessEqual(certified_upper, sparse_total_upper(n))

    def test_every_bad_time_is_counted_without_future_truncation(self):
        for k in (2, 3, 5, 7):
            control = SparsePeriodicGreenSelector(k)
            self.assertGreaterEqual(16**control.sparse_window, 32*control.conductor)
            for n in (1, 13, 127, 1001, 4096):
                actual_bad = sum(not control.guaranteed_good(t) for t in range(1, n+1))
                self.assertLessEqual(actual_bad, control.exceptional_count_upper(n))

    def test_all_conditional_characters_are_maximal_on_certified_good_times(self):
        for k, n, m in ((2, 97, 19), (3, 113, 101)):
            control = SparsePeriodicGreenSelector(k)
            cells = tuple(certified_control_cell(control, t, m)
                          for t in range(1, n+1) if control.guaranteed_good(t))
            self.assertGreater(len(cells), 0)
            defect = branch_defect(tuple(c.representative for c in cells), m, authenticate=False)
            self.assertEqual(defect.chi_squared, 15)
            for h in range(1, 16):
                self.assertEqual(defect.conditional_mode_energy(h), Cyclo16.one())

    def test_finite_table_obeys_quantified_bounds_uniformly_in_bins(self):
        control = SparsePeriodicGreenSelector(2)
        for n, m in ((113, 9), (137, 53), (151, 257)):
            table = certified_control_table(control, n, m)
            energy, delta = control.energy_lower_bounds(n, m)
            self.assertGreaterEqual(table.defect.exact_parity_energy(), energy)
            self.assertGreaterEqual(table.defect.chi_squared, delta)
            self.assertFalse(table.authentic_zero_anchor)

    def test_sparse_rational_controls_replay_real_cells_with_original_forcing(self):
        for k, n in ((2, 37), (3, 61)):
            control = SparsePeriodicGreenSelector(k)
            approximation = rational_selector_approximation(control, n)
            previous = approximation.initial
            for t, value in enumerate(approximation.states, 1):
                self.assertEqual(value, 16*previous+literal_r(t))
                previous = value
            self.assertFalse(verify_original_history(approximation.states))
            self.assertLess(control.initial_interval()[1], 0)
            real = certified_control_table(control, n, control.conductor)
            rational = branch_defect(approximation.states, control.conductor, authenticate=False)
            self.assertEqual(real.defect.counts, rational.counts)
            self.assertLess(approximation.state_error_upper, Q(1, 16**8))

    def test_sparse_family_preserves_explicit_nonzero_anchor(self):
        with self.assertRaises(ValueError):
            SparsePeriodicGreenSelector(3, 2)
        with self.assertRaises(ValueError):
            sparse_tail_interval(0, 0)


if __name__ == "__main__":
    unittest.main()
