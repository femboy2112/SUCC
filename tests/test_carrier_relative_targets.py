"""Exact controls plus independent word-enumeration and policy oracles."""
import itertools as it
import random
import unittest
from dataclasses import replace
from fractions import Fraction as Q

from observational_succ.carrier_relative_targets import (
    Carrier, CarrierError, Instrument, Target, Policy, AlgebraRow,
    ObservableAlgebra, behavioral_partition, shortest_separator, trace,
    observable_algebra, verify_algebra, resolve_target, static_fiber,
    plan_target, verify_policy, prefix_value_interval, target_obstruction, first_step_erasure_obstruction,
)


def op(name, outputs, next_states=None, cost=1, chart=None):
    return Instrument(name, chart or name+":unit", tuple(map(Q, outputs)),
                      tuple(range(len(outputs))) if next_states is None else tuple(next_states), cost)


def target(c, values):
    return Target(c.source, "claim", tuple(map(Q, values)))


def eyes():
    states = tuple(it.product((0, 1), repeat=3))  # red, infrared, inaccessible tag
    c = Carrier("two-wavelengths", 8, (
        op("red", tuple(7+2*x for x, y, h in states), chart="red:units-A"),
        op("infrared", tuple(3*y-1 for x, y, h in states), chart="infrared:units-B")))
    return c, target(c, tuple(x^y for x, y, h in states)), states


def brute_word_classes(c):
    # Pair product automaton: a shortest separating word has <= n² steps.
    equivalent = [[True]*c.size for _ in range(c.size)]
    words = [()]
    for _ in range(c.size*c.size):
        words = [w+(a.name,) for w in words for a in c.instruments]
        for w in words:
            read = [trace(c, i, w)[0] for i in range(c.size)]
            for i in range(c.size):
                for j in range(c.size):
                    equivalent[i][j] &= read[i] == read[j]
    classes, used = [], set()
    for i in range(c.size):
        if i not in used:
            b = tuple(j for j in range(c.size) if equivalent[i][j])
            classes.append(b); used.update(b)
    return tuple(classes)


def brute_policy(c, t, budget, pairs=None):
    # Independent boolean tree-existence oracle, no production planner calls.
    pairs = tuple((i, i) for i in range(c.size)) if pairs is None else pairs
    if len({t.values[i] for i, _ in pairs}) == 1:
        return True
    for a in c.instruments:
        if a.cost <= budget:
            branches = [[(i, a.next_states[s]) for i, s in pairs if a.outputs[s] == y]
                        for y in set(a.outputs[s] for _, s in pairs)]
            if all(brute_policy(c, t, budget-a.cost, tuple(b)) for b in branches):
                return True
    return False


class FiberTests(unittest.TestCase):
    def test_two_eyes_resolve_target_not_hidden_identity(self):
        c, t, states = eyes()
        one = static_fiber(c, ((c.source, "red", "red:units-A", Q(9)),))
        self.assertEqual(resolve_target(c, t, one).status, "AMBIGUOUS")
        both = static_fiber(c, ((c.source, "red", "red:units-A", Q(9)),
                               (c.source, "infrared", "infrared:units-B", Q(-1))))
        self.assertEqual(len(both), 2)
        r = resolve_target(c, t, both)
        self.assertEqual((r.status, r.values, r.minimax_error), ("IDENTIFIED", (Q(1),), Q(0)))
        self.assertEqual({states[i][2] for i in both}, {0, 1})

    def test_possible_true_is_not_identified_true(self):
        c = Carrier("hidden", 2, ())
        r = resolve_target(c, target(c, (0, 1)), (0, 1))
        self.assertEqual(r.status, "AMBIGUOUS")
        self.assertIn(Q(1), r.values)
        self.assertEqual(r.minimax_error, Q(1, 2))
        self.assertEqual(behavioral_partition(c), ((0, 1),))

    def test_pairwise_gluing_does_not_imply_joint_gluing(self):
        states = ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0))
        c = Carrier("even-parity", 4, tuple(op(str(k), [s[k] for s in states]) for k in range(3)))
        readings = tuple((c.source, str(k), str(k)+":unit", Q(1)) for k in range(3))
        for pair in it.combinations(readings, 2):
            self.assertTrue(static_fiber(c, pair))
        impossible = static_fiber(c, readings)
        self.assertEqual(impossible, ())
        self.assertEqual(resolve_target(c, target(c, (1, 1, 1, 1)), impossible).status, "INCOHERENT")

    def test_minimax_radius_is_exact_and_sharp(self):
        c = Carrier("numeric", 4, ())
        r = resolve_target(c, target(c, (-3, 0, 2, 7)), (0, 1, 2, 3))
        self.assertEqual((r.midpoint, r.minimax_error), (Q(2), Q(5)))
        for guess in map(Q, range(-10, 11)):
            self.assertGreaterEqual(max(abs(guess-v) for v in r.values), 5)

    def test_wrong_sources_charts_and_invasive_joint_reading_rejected(self):
        c, t, _ = eyes()
        for source, chart in (("fake", "red:units-A"), (c.source, "infrared:units-B")):
            with self.assertRaises(CarrierError):
                static_fiber(c, ((source, "red", chart, 9),))
        destructive = Carrier("d", 2, (op("p", (0, 1), (0, 0)),))
        with self.assertRaises(CarrierError):
            static_fiber(destructive, (("d", "p", "p:unit", 0),))
        with self.assertRaises(CarrierError):
            resolve_target(c, Target("fake", "P", t.values), (0,))

    def test_units_change_values_not_equivalence(self):
        c, t, _ = eyes()
        transformed = Carrier(c.source, c.size, tuple(replace(a, chart=a.chart+":new",
            outputs=tuple(-5*x+Q(7, 3) for x in a.outputs)) for a in c.instruments))
        self.assertEqual(behavioral_partition(c), behavioral_partition(transformed))
        self.assertEqual(len(observable_algebra(c).rows), len(observable_algebra(transformed).rows))
        with self.assertRaises(CarrierError):
            verify_algebra(transformed, observable_algebra(c))

    def test_close_is_not_an_equivalence_relation(self):
        a, b, c = Q(0), Q(3, 4), Q(3, 2)
        self.assertLessEqual(abs(a-b), 1)
        self.assertLessEqual(abs(b-c), 1)
        self.assertGreater(abs(a-c), 1)


class ObservableMatrixTests(unittest.TestCase):
    def test_product_closure_retains_cross_eye_information(self):
        c, t, _ = eyes()
        alg = observable_algebra(c)
        self.assertTrue(verify_algebra(c, alg))
        self.assertEqual(len(alg.rows), 4)  # not 8: invisible tag remains
        self.assertTrue(any(r.rule == "product" for r in alg.rows))
        coeff = alg.express(c, t)
        self.assertIsNotNone(coeff)
        self.assertEqual(tuple(sum((coef*row.values[i] for coef, row in zip(coeff, alg.rows)), Q())
                               for i in range(c.size)), t.values)
        tag = target(c, tuple(h for x, y, h in eyes()[2]))
        self.assertIsNone(alg.express(c, tag))

    def test_action_pullback_opens_new_probe_path(self):
        c = Carrier("future", 3, (op("look", (0, 0, 1)), op("step", (0, 0, 0), (1, 2, 2))))
        alg = observable_algebra(c)
        self.assertEqual(len(alg.rows), 3)
        self.assertTrue(any(r.rule == "pull" for r in alg.rows))
        self.assertEqual(shortest_separator(c, 0, 1), (2, ("step", "look")))
        self.assertIsNone(shortest_separator(c, 1, 1))

    def test_source_fingerprint_prevents_same_label_spoof(self):
        c = Carrier("name", 2, (op("look", (0, 1)),))
        fake = Carrier("name", 2, (op("look", (0, 0)),))
        self.assertNotEqual(c.fingerprint, fake.fingerprint)
        with self.assertRaises(CarrierError):
            verify_algebra(fake, observable_algebra(c))

    def test_corrupted_and_incomplete_recipes_rejected(self):
        c, _, _ = eyes()
        a = observable_algebra(c)
        broken = replace(a.rows[-1], values=(Q(17),)*8)
        with self.assertRaises(CarrierError):
            verify_algebra(c, replace(a, rows=a.rows[:-1]+(broken,)))
        with self.assertRaises(CarrierError):
            verify_algebra(c, replace(a, rows=a.rows[:-1]))
        future = AlgebraRow("pull", (100, "red"), a.rows[-1].values)
        with self.assertRaises(CarrierError):
            verify_algebra(c, replace(a, rows=a.rows[:-1]+(future,)))

    def test_all_234_single_instrument_models_against_word_oracle(self):
        cases = 0
        for n in (1, 2, 3):
            for transitions in it.product(range(n), repeat=n):
                for outputs in it.product((0, 1), repeat=n):
                    c = Carrier("exhaustive", n, (op("a", outputs, transitions),))
                    blocks = behavioral_partition(c)
                    self.assertEqual(blocks, brute_word_classes(c))
                    algebra = observable_algebra(c)
                    self.assertEqual(len(algebra.rows), len(blocks))
                    for tv in it.product((0, 1), repeat=n):
                        tt = target(c, tv)
                        constant = all(len({tv[i] for i in b}) == 1 for b in blocks)
                        self.assertEqual(algebra.express(c, tt) is not None, constant)
                        self.assertEqual(target_obstruction(c, tt) is None, constant)
                    for x in range(n):
                        for y in range(n):
                            sep = shortest_separator(c, x, y)
                            same = any(x in b and y in b for b in blocks)
                            self.assertEqual(sep is None, same)
                            if sep is not None:
                                self.assertNotEqual(trace(c, x, sep[1])[0], trace(c, y, sep[1])[0])
                    cases += 1
        self.assertEqual(cases, 234)

    def test_weighted_separator_is_minimum_cost_not_first_found(self):
        c = Carrier("cost", 2, (op("expensive", (0, 1), cost=5), op("cheap", (1, 0), cost=1)))
        self.assertEqual(shortest_separator(c, 0, 1), (1, ("cheap",)))

    def test_state_relabelling_covariance(self):
        c = Carrier("gauge", 3, (op("p", (0, 0, 1)), op("a", (0, 0, 0), (1, 2, 2))))
        permutation = (2, 0, 1)  # new index -> old index
        inverse = {v: i for i, v in enumerate(permutation)}
        altered = Carrier(c.source, 3, tuple(Instrument(a.name, a.chart,
            tuple(a.outputs[i] for i in permutation),
            tuple(inverse[a.next_states[i]] for i in permutation), a.cost) for a in c.instruments))
        for x in range(3):
            for y in range(3):
                self.assertEqual(shortest_separator(c, x, y), shortest_separator(altered, inverse[x], inverse[y]))


class ExecutableAccessTests(unittest.TestCase):
    def test_pairwise_separation_is_not_single_run_decidability(self):
        c = Carrier("destructive", 3, (op("a", (1, 0, 0), (0, 0, 0)),
                                       op("b", (0, 1, 0), (0, 0, 0))))
        t = target(c, (0, 0, 1))
        self.assertEqual(behavioral_partition(c), ((0,), (1,), (2,)))
        self.assertIsNotNone(observable_algebra(c).express(c, t))
        for i, j in it.combinations(range(3), 2):
            self.assertIsNotNone(shortest_separator(c, i, j))
        obstruction = first_step_erasure_obstruction(c, t)
        self.assertEqual(len(obstruction), 2)
        for name, outcome, i, j, merged in obstruction:
            a = c.operation(name)
            self.assertEqual((a.outputs[i], a.outputs[j]), (outcome, outcome))
            self.assertEqual((a.next_states[i], a.next_states[j]), (merged, merged))
            self.assertNotEqual(t.values[i], t.values[j])
        for budget in range(7):
            self.assertIsNone(plan_target(c, t, budget).policy)
        # Repair only the intervention law, not the truth table.
        noninvasive = Carrier(c.source, c.size, tuple(replace(a, next_states=(0, 1, 2)) for a in c.instruments))
        self.assertEqual(plan_target(noninvasive, t, 2).worst_cost, 2)
        self.assertIsNone(first_step_erasure_obstruction(noninvasive, t))

    def test_preserve_original_target_not_post_measurement_truth(self):
        c = Carrier("erase", 2, (op("reset", (0, 0), (0, 0)),))
        t = target(c, (0, 1))
        self.assertIsNone(plan_target(c, t, 5).policy)
        with self.assertRaises(CarrierError):
            verify_policy(c, t, Policy(None, "reset", ((Q(0), Policy(Q(0), None)),)), 1)

    def test_target_policy_without_full_source_reconstruction(self):
        c, t, _ = eyes()
        self.assertIsNone(plan_target(c, t, 1).policy)
        result = plan_target(c, t, 2)
        self.assertEqual(result.worst_cost, 2)
        self.assertEqual(verify_policy(c, t, result.policy, 2), 2)

    def test_constant_target_needs_no_probe(self):
        c = Carrier("constant", 4, ())
        self.assertEqual(plan_target(c, target(c, (7,)*4), 0).worst_cost, 0)
        self.assertEqual(len(behavioral_partition(c)[0]), 4)

    def test_4096_policy_cells_against_independent_tree_search(self):
        options = [(out, nxt) for out in it.product((0, 1), repeat=2)
                   for nxt in it.product(range(2), repeat=2)]
        cases = 0
        for (o1, n1), (o2, n2) in it.product(options, repeat=2):
            c = Carrier("policy-grid", 2, (op("a", o1, n1), op("b", o2, n2)))
            for values in it.product((0, 1), repeat=2):
                t = target(c, values)
                for budget in range(4):
                    r = plan_target(c, t, budget)
                    self.assertEqual(r.policy is not None, brute_policy(c, t, budget))
                    if r.policy is not None:
                        self.assertEqual(verify_policy(c, t, r.policy, budget), r.worst_cost)
                        if r.worst_cost:
                            self.assertFalse(brute_policy(c, t, r.worst_cost-1))
                    cases += 1
        self.assertEqual(cases, 4096)

    def test_false_policy_and_missing_branch_rejected(self):
        c = Carrier("p", 2, (op("read", (0, 1)),))
        t = target(c, (0, 1))
        with self.assertRaises(CarrierError):
            verify_policy(c, t, Policy(Q(0), None), 1)
        with self.assertRaises(CarrierError):
            verify_policy(c, t, Policy(None, "read", ((Q(0), Policy(Q(0), None)),)), 1)
        with self.assertRaises(CarrierError):
            plan_target(c, t, -1)


class CompletionAndValidationTests(unittest.TestCase):
    def test_nested_value_enclosures_do_not_require_hidden_tag_recovery(self):
        digits = (2, 4, 3, 15, 6)
        previous = (Q(0), Q(1))
        for n in range(len(digits)+1):
            bounds = prefix_value_interval(digits[:n])
            self.assertLessEqual(previous[0], bounds[0])
            self.assertGreaterEqual(previous[1], bounds[1])
            self.assertEqual(bounds[1]-bounds[0], Q(1, 16**n))
            previous = bounds

    def test_finite_prefix_cannot_select_tail_digit_frequency(self):
        prefix = (2, 4, 3, 15, 6)
        lo, hi = prefix_value_interval(prefix)
        scale = 16**len(prefix)
        left = lo+Q(1, 15*scale)  # eventually all 1s
        right = lo+Q(14, 15*scale)  # eventually all Es
        self.assertTrue(lo < left < right < hi)
        self.assertLess(right-left, Q(1, scale))
        def first_digits(value, count):
            digits = []
            for _ in range(count):
                value *= 16
                digit = value.numerator//value.denominator
                digits.append(digit); value -= digit
            return tuple(digits)
        self.assertEqual(first_digits(left, 15), prefix+(1,)*10)
        self.assertEqual(first_digits(right, 15), prefix+(14,)*10)

    def test_reject_bad_source_shapes(self):
        for args in (("", 1, ()), ("x", 0, ()), ("x", True, ())):
            with self.assertRaises(CarrierError): Carrier(*args)
        for a in (Instrument("x", "c", (0.0,), (0,)), op("x", (0,), (1,)), op("x", (0,), cost=0)):
            with self.assertRaises(CarrierError): Carrier("a", 1, (a,))
        with self.assertRaises(CarrierError): prefix_value_interval((16,))
        with self.assertRaises(CarrierError): prefix_value_interval((True,))


if __name__ == "__main__":
    unittest.main()
