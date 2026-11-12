"""Arithmetic, laziness, capture, budget and mutation probes for the observer."""
from dataclasses import replace
from fractions import Fraction
import unittest

import lambda_observer as lo
from observational_succ.c_monoid_succ_embedding import (
    ABS, APP, CONST, PAIR, T, V, beta_redex,
)


def marking_primes(limit):
    """Independent finite Eratosthenes marking oracle for these tests only."""
    flags = [True] * (limit + 1)
    flags[0:2] = [False, False]
    for factor in range(2, limit + 1):
        if flags[factor]:
            for multiple in range(factor * factor, limit + 1, factor):
                flags[multiple] = False
    return tuple(index for index, flag in enumerate(flags) if flag)


def is_closed(term, depth=0):
    if term.tag == "VAR":
        return term.idx < depth
    if term.tag == "ABS":
        return is_closed(term.body, depth + 1)
    if term.tag in ("APP", "PAIR"):
        return is_closed(term.f, depth) and is_closed(term.a, depth)
    if term.tag in ("FST", "SND"):
        return is_closed(term.f, depth)
    return term.tag == "CONST"


def constants(term):
    if term.tag == "CONST":
        return {term.name}
    if term.tag == "ABS":
        return constants(term.body)
    if term.tag in ("APP", "PAIR"):
        return constants(term.f) | constants(term.a)
    if term.tag in ("FST", "SND"):
        return constants(term.f)
    return set()


def replace_false_with_true(term):
    if term == lo.FALSE:
        return lo.TRUE
    changes = {}
    for field in ("body", "f", "a"):
        child = getattr(term, field)
        if child is not None:
            changes[field] = replace_false_with_true(child)
    return replace(term, **changes) if changes else term


class PrimeLambdaObserverTests(unittest.TestCase):
    def test_finite_closed_program_has_no_prime_oracle(self):
        self.assertTrue(is_closed(lo.PRIME_PROGRAM))
        names = constants(lo.PRIME_PROGRAM)
        self.assertEqual(names, {"gt", "mul", "mod", "eq", "succ",
                                 "nat:0", "nat:2"})
        self.assertEqual(len(lo.program_sha256()), 64)

    def test_literal_fixed_point_unfolding(self):
        # W_F is the reduct of Curry Y F; W_F -> F W_F literally.
        f = CONST("opaque-F")
        w = beta_redex(APP(lo.Y, f))
        self.assertIsNotNone(w)
        self.assertEqual(beta_redex(w), APP(f, w))

    def test_capture_avoiding_inherited_beta(self):
        # (lambda x. lambda y. x) z -> lambda y. z.  z stays free.
        redex = APP(ABS(ABS(V(1))), V(0))
        result, beta, delta, status = lo.reduce_term(redex, 1)
        self.assertEqual(result, ABS(V(1)))
        self.assertEqual((beta, delta, status), (1, 0, "COMPLETE"))

    def test_trial_division_on_primes_composites_and_squares(self):
        oracle = set(marking_primes(220))
        for n in (2, 3, 4, 5, 9, 15, 25, 49, 97, 121, 143, 169, 199, 221):
            term = APP(APP(lo.TRIAL, lo.nat(n)), lo.nat(2))
            result, beta, delta, status = lo.reduce_term(term, 100_000)
            self.assertEqual(status, "COMPLETE")
            self.assertEqual(result, lo.TRUE if n in oracle else lo.FALSE, n)
            self.assertGreater(beta, 0)
            self.assertGreater(delta, 0)

    def test_first_thirty_primes_against_marking_sieve(self):
        receipt = lo.prime_prefix(30, 1_000_000)
        self.assertEqual(receipt.status, "COMPLETE")
        self.assertEqual(receipt.values, marking_primes(127)[:30])
        self.assertEqual(receipt.requested_count, 30)
        self.assertGreater(receipt.beta_steps, 0)
        self.assertGreater(receipt.delta_steps, 0)
        self.assertLessEqual(receipt.beta_steps + receipt.delta_steps,
                             receipt.max_steps)

    def test_zero_count_and_zero_budget(self):
        empty = lo.prime_prefix(0, 0)
        self.assertEqual((empty.status, empty.values), ("COMPLETE", ()))
        self.assertEqual(empty.beta_steps + empty.delta_steps, 0)
        unknown = lo.prime_prefix(1, 0)
        self.assertEqual((unknown.status, unknown.values), ("UNKNOWN", ()))
        self.assertEqual(unknown.beta_steps + unknown.delta_steps, 0)

    def test_exact_budget_boundary_and_partial_prefix(self):
        first = lo.prime_prefix(1)
        steps = first.beta_steps + first.delta_steps
        at_boundary = lo.prime_prefix(1, steps)
        self.assertEqual(at_boundary.values, (2,))
        self.assertEqual(at_boundary.status, "COMPLETE")
        below = lo.prime_prefix(1, steps - 1)
        self.assertEqual((below.status, below.values), ("UNKNOWN", ()))
        partial = lo.prime_prefix(3, steps)
        self.assertEqual((partial.status, partial.values), ("UNKNOWN", (2,)))
        self.assertEqual(partial.beta_steps + partial.delta_steps, steps)

    def test_lazy_pair_does_not_force_divergent_tail(self):
        self_application = ABS(APP(V(0), V(0)))
        omega = APP(self_application, self_application)
        program = PAIR(lo.nat(7), omega)
        one = lo.run_stream_prefix(program, 1, 1)
        self.assertEqual((one.status, one.values), ("COMPLETE", (7,)))
        self.assertEqual((one.beta_steps, one.delta_steps), (0, 1))
        two = lo.run_stream_prefix(program, 2, 25)
        self.assertEqual((two.status, two.values), ("UNKNOWN", (7,)))
        self.assertEqual(two.beta_steps + two.delta_steps, 25)

    def test_unused_church_branch_is_lazy(self):
        self_application = ABS(APP(V(0), V(0)))
        omega = APP(self_application, self_application)
        term = APP(APP(lo.TRUE, lo.nat(17)), omega)
        result, beta, delta, status = lo.reduce_term(term, 2)
        self.assertEqual((result, beta, delta, status),
                         (lo.nat(17), 2, 0, "COMPLETE"))

    def test_composite_acceptance_mutation_is_detected(self):
        mutant = replace_false_with_true(lo.PRIME_PROGRAM)
        bad = lo.run_stream_prefix(mutant, 5, 100_000)
        self.assertEqual(bad.status, "COMPLETE")
        self.assertEqual(bad.values, (2, 3, 4, 5, 6))
        self.assertNotEqual(bad.values, marking_primes(20)[:5])
        self.assertNotEqual(bad.program_sha256, lo.program_sha256())
        # The authentic entrypoint still rejects those composite candidates.
        self.assertEqual(lo.prime_prefix(5).values, (2, 3, 5, 7, 11))

    def test_exact_integer_interfaces(self):
        for bad in (True, False, -1, 2.0, Fraction(2), "2", None):
            with self.subTest(value=bad):
                with self.assertRaises(ValueError):
                    lo.prime_prefix(bad)
                with self.assertRaises(ValueError):
                    lo.prime_prefix(1, bad)
                with self.assertRaises(ValueError):
                    lo.nat(bad)

    def test_malformed_arithmetic_is_not_silently_unknown(self):
        with self.assertRaises(ValueError):
            lo.reduce_term(APP(APP(CONST("mod"), lo.nat(5)), lo.nat(0)))
        with self.assertRaises(ValueError):
            lo.reduce_term(APP(CONST("succ"), lo.TRUE))
        with self.assertRaises(ValueError):
            lo.run_stream_prefix(lo.nat(4), 1)
        with self.assertRaises(TypeError):
            lo.run_stream_prefix(object(), 1)


if __name__ == "__main__":
    unittest.main()
