"""Exact, calibrated tests for the finite source observer; no asymptotic inference."""

from dataclasses import replace
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import gcd, prod
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import observer as o


FIB_CLOCKS = (55, 89, 144, 233)


def leibniz(matrix):
    n = len(matrix)
    return sum(((-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
                * prod(matrix[i][p[i]] for i in range(n))
                for p in permutations(range(n))), Q())


class FiveChannelTests(unittest.TestCase):
    def test_cauchy_formula_independent_permutation_oracle(self):
        for clocks in ((1, 2, 3, 4), (8, 13, 21, 34), FIB_CLOCKS,
                       (144, 233, 377, 610), (11, 3, 19, 5)):
            c = o.cauchy_matrix(clocks)
            self.assertEqual(o.determinant(c), leibniz(c))
            self.assertEqual(leibniz(c), o.cauchy_determinant(clocks))

    def test_fibonacci_volume_gain_scoped_to_declared_clocks(self):
        ratio = o.cauchy_determinant(FIB_CLOCKS) / o.cauchy_determinant((55, 56, 57, 58))
        self.assertEqual(ratio, Q(18727804072912891802425918399248,
                                 42573062902996830648629875))
        self.assertLess(Q(439897), ratio)
        self.assertLess(ratio, Q(439898))

    def test_jacobian_exact_determinant_and_inverse(self):
        for clocks, horizon in (((1, 2, 3, 4), 4), ((3, 7, 9, 14), 19), (FIB_CLOCKS, 233)):
            j = o.observation_jacobian(clocks, horizon)
            self.assertEqual(leibniz(j), o.cauchy_determinant(clocks))
            inverse = o.inverse(j)
            for k in range(5):
                column = tuple(inverse[i][k] for i in range(5))
                self.assertEqual(o.matvec(j, column), tuple(Q(i == k) for i in range(5)))

    def test_finite_causal_family_recovery(self):
        for coefficients, seed in ((o.BBP_COEFFICIENTS, 0), ((0, 0, 0, 0), 0),
                                   ((Q(2, 3), -7, Q(11, 5), 9), Q(-4, 7))):
            journal = o.make_journal(29, coefficients, seed)
            snapshot = o.observe(journal, (2, 5, 13, 23))
            self.assertEqual(o.recover(snapshot), (tuple(map(Q, coefficients)), Q(seed)))

    def test_anchor_is_finite_and_retains_seed_and_winding(self):
        base = o.make_journal(24)
        alias = o.make_journal(24, seed=Q(1, 16))
        sb, sa = (o.observe(j, (3, 5, 8, 13)) for j in (base, alias))
        self.assertEqual(sa.innovations, sb.innovations)
        self.assertEqual(sa.anchor - sb.anchor, Q(1, 16))
        self.assertEqual(o.recover(sa)[1], Q(1, 16))
        for n in range(1, 25):
            self.assertEqual((alias.states[n] - base.states[n]).denominator, 1)
        self.assertFalse(o.validate_journal(alias, authentic=True))

    def test_source_mutation_and_state_tampering_are_detected(self):
        base = o.make_journal(20)
        self.assertTrue(o.validate_journal(base, authentic=True))
        mutant = o.make_journal(20, coefficients=(5, -2, -1, -1))
        self.assertFalse(o.validate_journal(mutant, authentic=True))
        self.assertEqual(o.recover(o.observe(mutant, (3, 5, 8, 13)))[0], (5, -2, -1, -1))
        states = list(base.states)
        states[7] += 1
        broken = replace(base, states=tuple(states))
        self.assertFalse(o.validate_journal(broken))
        with self.assertRaises(ValueError):
            o.observe(broken, (3, 5, 8, 13))

    def test_advance_is_append_only_and_no_future_observations(self):
        first = o.make_journal(13)
        later = o.advance(first, 8)
        self.assertEqual(later.states[:14], first.states)
        self.assertEqual(later, o.make_journal(21))
        with self.assertRaises(ValueError):
            o.observe(first, (2, 5, 8, 21))

    def test_locked_zero_family_has_same_full_jacobian(self):
        locked = o.make_journal(21, coefficients=(0, 0, 0, 0))
        self.assertTrue(all(value == 0 for value in locked.states))
        self.assertEqual(o.recover(o.observe(locked, (2, 5, 8, 13))), ((0, 0, 0, 0), 0))
        self.assertNotEqual(o.determinant(o.observation_jacobian((2, 5, 8, 13), 21)), 0)
        self.assertFalse(o.validate_journal(locked, authentic=True))

    def test_invalid_clock_control(self):
        for clocks in ((1, 2, 3), (1, 2, 3, 3), (0, 2, 3, 4)):
            with self.assertRaises(ValueError):
                o.cauchy_matrix(clocks)


class PrimeResolutionTests(unittest.TestCase):
    def test_original_prime_budget_exact_receipt(self):
        expected = {2: ((2, 2, 2, 2), 1, 15, 23),
                    3: ((1, 1, 1, 1), 3, 1, 1),
                    5: ((0, 1, 2, 1), 4, 0, 0),
                    7: ((0, 0, 1, 2), 4, 0, 0),
                    11: ((0, 0, 0, 0), 3, 1, 1)}
        for p, result in expected.items():
            chart = o.prime_chart(FIB_CLOCKS, p)
            self.assertEqual((chart.exponents, chart.rank, chart.loss,
                              chart.determinant_valuation), result)

    def test_mod11_wrong_repair_fails_and_correct_preplan_works(self):
        self.assertEqual(o.prime_chart((55, 89, 144, 147), 11).rank, 3)
        self.assertEqual(o.prime_chart((55, 89, 147, 233), 11).rank, 4)

    def test_append_only_mod11_repair(self):
        plan = o.plan_prime_repair(FIB_CLOCKS, 11)
        self.assertEqual(plan.appended_clocks, (235,))
        self.assertEqual(plan.history, FIB_CLOCKS + (235,))
        self.assertEqual(plan.basis_clocks, (55, 89, 233, 235))
        self.assertEqual(o.prime_chart(plan.basis_clocks, 11).rank, 4)
        journal = o.make_journal(233)
        with self.assertRaises(ValueError):
            o.observe(journal, plan.basis_clocks)
        extended = o.advance(journal, 2)
        self.assertEqual(o.recover(o.observe(extended, plan.basis_clocks)),
                         (o.BBP_COEFFICIENTS, 0))

    def test_optional_polar_mod11_repair_is_earlier_and_declared(self):
        plan = o.plan_prime_repair(FIB_CLOCKS, 11, allow_poles=True)
        self.assertEqual(plan.appended_clocks, (234,))
        chart = o.prime_chart(plan.basis_clocks, 11)
        self.assertEqual(chart.rank, 4)
        self.assertGreater(chart.exponents[-1], 0)

    def test_revisit_retained_history_does_not_reverse_source_time(self):
        journal = o.make_journal(233)
        old = o.observe(journal, FIB_CLOCKS)
        repaired = o.observe(journal, (55, 89, 147, 233))
        self.assertEqual((old.horizon, repaired.horizon), (233, 233))
        self.assertEqual(o.prime_chart(repaired.clocks, 11).rank, 4)
        self.assertEqual(o.recover(repaired), (o.BBP_COEFFICIENTS, 0))
        self.assertEqual(journal.states[144]-16*journal.states[143],
                         old.innovations[2])

    def test_seven_requires_polar_chart_for_four_distinct_residues(self):
        ordinary = [m for m in range(1, 8) if all((8 * m - d) % 7 for d in o.POLES)]
        self.assertEqual(len(ordinary), 3)
        with self.assertRaises(ValueError):
            o.plan_prime_repair((1, 5, 6), 7, allow_poles=False)
        for clocks in combinations(range(1, 8), 4):
            chart = o.prime_chart(clocks, 7)
            self.assertEqual(chart.rank, 4)
            self.assertEqual(chart.loss, 0)

    def test_general_prime_residue_theorem_finite_calibration(self):
        for p in (11, 13, 17, 29):
            for clocks in ((1, 2, 3, 4), (p, p + 1, p + 3, p + 5),
                           (2 * p + 2, 4 * p + 4, 7 * p + 6, 9 * p + 7)):
                chart = o.prime_chart(clocks, p)
                self.assertEqual(chart.rank, 4)
                self.assertEqual(chart.loss, 0)

    def test_modular_recovery_with_paid_precision(self):
        coefficients = (Q(7), Q(-13), Q(22), Q(105))
        for p in (2, 3, 5, 7, 11, 29):
            chart = o.prime_chart(FIB_CLOCKS, p)
            for precision in (1, 2, 4):
                measurement_precision = chart.measurement_precision(precision)
                measurements = tuple(o.reduce_p(x, p, measurement_precision)
                                     for x in o.matvec(chart.matrix, coefficients))
                self.assertEqual(o.recover_mod_p(chart, measurements, precision),
                                 tuple(o.reduce_p(c, p, precision) for c in coefficients))

    def test_one_less_digit_fails_on_a_constructed_worst_direction(self):
        for p in (2, 3, 11):
            chart = o.prime_chart(FIB_CLOCKS, p)
            loss, target = chart.loss, 2
            i, j = next((i, j) for i in range(4) for j in range(4)
                        if o.valuation(chart.inverse_matrix[i][j], p) == -loss)
            error = tuple(Q(p ** (target + loss - 1) if k == j else 0) for k in range(4))
            recovered_error = o.matvec(chart.inverse_matrix, error)
            self.assertEqual(o.valuation(recovered_error[i], p), target - 1)
            self.assertNotEqual(o.reduce_p(recovered_error[i], p, target), 0)

    def test_local_prime_gain_need_not_improve_every_other_prime(self):
        repaired = (55, 89, 233, 235)
        self.assertEqual(o.prime_chart(repaired, 11).loss, 0)
        self.assertEqual(o.prime_chart(repaired, 2).loss, 16)
        self.assertEqual(o.prime_chart(repaired, 3).loss, 2)
        self.assertEqual(o.prime_chart(repaired, 5).loss, 1)

    def test_full_seed_channel_budget_is_not_hidden(self):
        for p, seed_loss in ((2, 934), (3, 7), (5, 4), (7, 3), (11, 2)):
            chart = o.prime_chart(FIB_CLOCKS, p)
            budget = o.five_channel_budget(chart, 233, 3)
            self.assertEqual(budget["seed_innovation_loss"], seed_loss)
            self.assertEqual(budget["anchor"], 3)
            self.assertEqual(budget["innovations"], 3 + max(seed_loss, chart.loss))
            a = o.partial_coefficients(233)
            for j in range(4):
                error = tuple(Q(p ** budget["innovations"] if i == j else 0) for i in range(4))
                c_error = o.matvec(chart.inverse_matrix, error)
                s_error = -sum((x * y for x, y in zip(a, c_error)), Q())
                self.assertGreaterEqual(o.valuation(s_error, p), 3)
                self.assertTrue(all(o.valuation(x, p) >= 3 for x in c_error))

    def test_composite_and_unpaid_pole_controls(self):
        with self.assertRaises(ValueError):
            o.prime_chart(FIB_CLOCKS, 6)
        with self.assertRaises(ValueError):
            o.rank_mod_p(o.cauchy_matrix(FIB_CLOCKS), 7)
        with self.assertRaises(ValueError):
            o.plan_prime_repair(FIB_CLOCKS, 3)

    def test_odd_prime_polar_clock_depth_and_small_prime_schedule(self):
        self.assertEqual(tuple(o.polar_clock_depth(p) for p in (3, 5, 7, 11, 29)),
                         (2, 2, 1, 1, 1))
        self.assertEqual(o.plan_polar_repair(FIB_CLOCKS, 3).appended_clocks,
                         (236, 239, 240, 241))
        self.assertEqual(o.plan_polar_repair(FIB_CLOCKS, 5).appended_clocks,
                         (238, 241, 244, 254))

    def test_all_odd_prime_polar_repair_reduces_to_scaled_permutation(self):
        for p in (3, 5, 7, 11, 29):
            depth = o.polar_clock_depth(p)
            for horizon in (1, 13, 233, 1000):
                plan = o.plan_polar_repair((horizon,), p)
                self.assertEqual(len(plan.appended_clocks), 4)
                self.assertEqual(plan.history[:1], (horizon,))
                self.assertGreater(min(plan.appended_clocks), horizon)
                self.assertLessEqual(max(plan.appended_clocks), horizon + p ** depth)
                chart = o.prime_chart(plan.basis_clocks, p)
                reduced = [[o.reduce_p(x, p) for x in row] for row in chart.matrix]
                self.assertTrue(all(sum(x != 0 for x in row) == 1 for row in reduced))
                self.assertTrue(all(sum(reduced[i][j] != 0 for i in range(4)) == 1
                                    for j in range(4)))
                self.assertEqual(chart.rank, 4)
                self.assertEqual(chart.loss, 0)
                self.assertEqual(chart.determinant_valuation, 0)

    def test_small_prime_polar_repair_measures_source_at_no_extra_inverse_cost(self):
        for p in (3, 5):
            plan = o.plan_polar_repair(FIB_CLOCKS, p)
            old = o.make_journal(233)
            with self.assertRaises(ValueError):
                o.observe(old, plan.basis_clocks)
            new = o.advance(old, max(plan.basis_clocks) - old.horizon)
            self.assertEqual(new.states[:len(old.states)], old.states)
            snapshot = o.observe(new, plan.basis_clocks)
            chart = o.prime_chart(plan.basis_clocks, p)
            precision = 3
            self.assertEqual(chart.measurement_precision(precision), precision)
            normalized = tuple(p ** e * y for e, y in zip(chart.exponents, snapshot.innovations))
            residues = tuple(o.reduce_p(y, p, precision) for y in normalized)
            self.assertEqual(o.recover_mod_p(chart, residues, precision),
                             tuple(o.reduce_p(c, p, precision) for c in o.BBP_COEFFICIENTS))
            self.assertEqual(o.recover(snapshot), (o.BBP_COEFFICIENTS, 0))
            self.assertGreater(o.five_channel_budget(chart, new.horizon, precision)
                               ["seed_innovation_loss"], 0)

    def test_insufficient_polar_clock_depth_and_prime_two_controls(self):
        for p in (3, 5):
            shallow_modulus = p ** (o.polar_clock_depth(p) - 1)
            shallow_residues = {d * pow(8, -1, shallow_modulus) % shallow_modulus
                                for d in o.POLES}
            self.assertLess(len(shallow_residues), 4)
        with self.assertRaises(ValueError):
            o.plan_polar_repair(FIB_CLOCKS, 2)
        with self.assertRaises(ValueError):
            o.plan_polar_repair(FIB_CLOCKS, 9)


class UniversalRepairTests(unittest.TestCase):
    def test_exact_consecutive_determinant_including_failed_residue_controls(self):
        for n in (1, 2, 5, 8, 11, 14, 15, 17, 233, 236, 131072, 131078):
            clocks = tuple(range(n, n + 4))
            cleared = o.cleared_cauchy_matrix(clocks)
            expected = 2 ** 19 * 3 ** (n % 3 != 2) * 5 ** (n % 5 == 0)
            self.assertEqual(leibniz(cleared), expected)
            self.assertEqual(o.determinant(cleared), expected)
            scales = o.row_denominator_lcms(clocks)
            self.assertEqual(leibniz(cleared), prod(scales) * o.cauchy_determinant(clocks))

    def test_integer_smith_via_all_minor_gcds(self):
        for n in (2, 8, 11, 14, 233, 131078):
            matrix = o.cleared_cauchy_matrix(tuple(range(n, n + 4)))
            divisors = [1]
            for k in range(1, 5):
                divisor = 0
                for rows in combinations(range(4), k):
                    for columns in combinations(range(4), k):
                        minor = [[matrix[i][j] for j in columns] for i in rows]
                        divisor = gcd(divisor, int(leibniz(minor)))
                divisors.append(divisor)
            self.assertEqual(divisors, [1, 1, 4, 256, 2 ** 19])
            self.assertEqual(tuple(divisors[k] // divisors[k - 1] for k in range(1, 5)),
                             (1, 4, 64, 2048))

    def test_universal_plan_nine_tick_bound_and_preserved_journal(self):
        self.assertEqual(o.plan_universal_repair((0,)).appended_clocks, (2, 3, 4, 5))
        self.assertEqual(o.plan_universal_repair(FIB_CLOCKS).appended_clocks,
                         (236, 237, 238, 239))
        for horizon in range(61):
            plan = o.plan_universal_repair((horizon,))
            self.assertGreater(plan.basis_clocks[0], horizon)
            self.assertLessEqual(plan.basis_clocks[-1], horizon + 9)
            self.assertEqual(plan.history, (horizon,) + plan.appended_clocks)
            self.assertEqual(plan.binary_loss, 11)
            self.assertEqual(leibniz(o.cleared_cauchy_matrix(plan.basis_clocks)), 2 ** 19)
        self.assertEqual(o.plan_universal_repair((2,)).basis_clocks[-1] - 2, 9)
        old = o.make_journal(233)
        plan = o.plan_universal_repair(FIB_CLOCKS)
        with self.assertRaises(ValueError):
            o.observe(old, plan.basis_clocks)
        new = o.advance(old, plan.basis_clocks[-1] - old.horizon)
        self.assertEqual(new.states[:len(old.states)], old.states)
        self.assertEqual(o.recover(o.observe(new, plan.basis_clocks)),
                         (o.BBP_COEFFICIENTS, 0))

    def test_universal_chart_all_sampled_odd_primes_and_binary_debt(self):
        for horizon in (1, 2, 233, 1000, 131072):
            clocks = o.plan_universal_repair((horizon,)).basis_clocks
            cleared = o.cleared_cauchy_matrix(clocks)
            for p in (3, 5, 7, 11, 29, 101):
                self.assertEqual(o.rank_mod_p(cleared, p), 4)
                self.assertEqual(o.prime_chart(clocks, p).loss, 0)
            self.assertEqual(o.rank_mod_p(cleared, 2), 1)
            self.assertEqual(o.prime_chart(clocks, 2).loss, 11)
            self.assertEqual(max(-o.valuation(x, 2) for row in o.inverse(cleared)
                                 for x in row), 11)

    def test_cleared_units_do_not_preserve_real_measurement_noise(self):
        clocks = (236, 237, 238, 239)
        scales = o.row_denominator_lcms(clocks)
        self.assertTrue(all(scale > 1 for scale in scales))
        raw_error = Q(1, 10 ** 12)
        self.assertTrue(all(scale * raw_error > raw_error for scale in scales))
        self.assertNotEqual(o.cauchy_determinant(clocks), 2 ** 19)
        self.assertEqual(prod(scales) * o.cauchy_determinant(clocks), 2 ** 19)


if __name__ == "__main__":
    unittest.main(verbosity=2)
