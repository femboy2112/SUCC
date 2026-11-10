"""Exact structural tests of the omega-trace beta-reduction interpreter.

Standard library only (fractions, dataclasses, unittest).  No floating point.
Covers: explicit positional syntax, leftmost beta stepper, exact growth law
E_k(m) -> E_k(m+k-2) for k in 2..8, the finite strongly-normalizing compiled
SUCC step, the separate guarded trace for raw Omega_k, the simulation theorem
(commuting square), the reflection/non-alias condition, and the hostile
control that raw Omega_3/4/5 reach no finite normal form within any bounded
budget.
"""
import unittest
from fractions import Fraction as Q

from observational_succ.omega_trace_interpreter import (
    Term,
    Step,
    contract_leftmost,
    reduce_leftmost,
    verify_growth_law,
    growth_law_check,
    bbp_forcing,
    compile_succ_step,
    compiled_orbit,
    guarded_omega_trace,
    observe,
    reflection_non_alias_example,
    count_only_conflation_witness,
    compiled_matches_source,
)


class SyntaxTests(unittest.TestCase):
    def test_positions_are_explicit_addresses(self):
        # E_k(m) has m-1 redexes at addresses 0..m-2; leftmost is always 0.
        for k in range(2, 9):
            for m in range(1, 9):
                t = Term(k=k, m=m)
                self.assertEqual(t.redex_addresses(), tuple(range(m - 1)))
                self.assertEqual(t.is_normal_form(), m == 1)
                self.assertEqual(t.head_unsolvable(), m >= 2)

    def test_validation(self):
        for bad in (-1, 0, 1):
            with self.assertRaises(ValueError):
                Term(k=bad, m=2)
        for bad in (0, -3):
            with self.assertRaises(ValueError):
                Term(k=3, m=bad)
        with self.assertRaises(ValueError):
            contract_leftmost(Term(k=3, m=1))
        with self.assertRaises(ValueError):
            list(reduce_leftmost(Term(k=3, m=2), -1))


class GrowthLawTests(unittest.TestCase):
    def test_growth_law_exact_k_2_to_8(self):
        # E_k(m) -> E_k(m + k - 2) exactly, delta == k-2.
        for k in range(2, 9):
            for m in range(2, 40):
                step = contract_leftmost(Term(k=k, m=m))
                self.assertEqual(step.after.m, m + (k - 2))
                self.assertEqual(step.delta, k - 2)
                self.assertEqual(step.address, 0)
                self.assertEqual(step.before.m, m)

    def test_growth_law_verifier(self):
        self.assertTrue(verify_growth_law())

    def test_omega3_is_unit_succ(self):
        # k=3 gives delta 1: unit syntactic SUCC.
        for m in range(2, 30):
            self.assertEqual(growth_law_check(3, m).delta, 1)
        # k=4 gives delta 2.
        for m in range(2, 30):
            self.assertEqual(growth_law_check(4, m).delta, 2)


class StepperTests(unittest.TestCase):
    def test_leftmost_reduction_sequence(self):
        # E_4(2) -> E_4(4) -> E_4(6) -> ... each step fires address 0.
        t = Term(k=4, m=2)
        steps = list(reduce_leftmost(t, 6))
        self.assertEqual(len(steps), 6)
        self.assertEqual([s.address for s in steps], [0] * 6)
        self.assertEqual([s.delta for s in steps], [2] * 6)
        self.assertEqual([s.after.m for s in steps], [4, 6, 8, 10, 12, 14])

    def test_normal_form_exhausts(self):
        # E_k(1) is already a normal form: zero steps.
        self.assertEqual(list(reduce_leftmost(Term(k=3, m=1), 100)), [])


class CompiledSUCCStepTests(unittest.TestCase):
    def test_source_forcing_exact(self):
        self.assertEqual(bbp_forcing(1), Q(47, 15))
        for j in range(1, 40):
            self.assertGreater(bbp_forcing(j), 0)
            self.assertLess(bbp_forcing(j), Q(4, j * j))

    def test_simulation_square(self):
        # normal_form(compile(U,n)) == 16*U + r(n+1) exactly.
        for n in range(0, 40):
            u = Q(0)
            for t in range(n):
                self.assertTrue(compiled_matches_source(u, t))
                u = 16 * u + bbp_forcing(t + 1)
            self.assertTrue(compiled_matches_source(u, n))

    def test_compiled_orbit_matches_selected_state(self):
        # Iterated compiled step reproduces the exact source orbit U_0..U_N.
        N = 25
        steps = compiled_orbit(N, Q(0))
        self.assertEqual(len(steps), N)
        u = Q(0)
        for t, step in enumerate(steps):
            u = 16 * u + bbp_forcing(t + 1)
            self.assertEqual(step.normal_form(), u)
        # Known closed form: U_n = sum_{j=1}^n 16^(n-j) r(j).
        for n in range(1, N + 1):
            closed = sum((16 ** (n - j) * bbp_forcing(j) for j in range(1, n + 1)), Q())
            self.assertEqual(steps[n - 1].normal_form(), closed)

    def test_compiled_trace_is_positional_and_finite(self):
        step = compile_succ_step(5, Q(3))
        self.assertEqual(len(step.trace), 3)  # fixed length -> strong normalization
        self.assertEqual([e.address for e in step.trace], [0, 1, 2])
        self.assertEqual(step.normal_form(), 16 * Q(3) + bbp_forcing(6))


class GuardedOmegaTests(unittest.TestCase):
    def test_guarded_trace_reports_no_normal_form(self):
        for k in (2, 3, 4, 5, 8):
            report = guarded_omega_trace(k, budget=20)
            self.assertFalse(report.has_finite_normal_form)
            self.assertEqual(len(report.prefixes), 20)
            # Each prefix is a leftmost step firing address 0.
            self.assertEqual([s.address for s in report.prefixes], [0] * 20)

    def test_omega2_identity_loop(self):
        # omega_2 omega_2 -> omega_2 omega_2 exactly; no normal form either.
        report = guarded_omega_trace(2, budget=5)
        self.assertFalse(report.has_finite_normal_form)
        self.assertEqual([s.after.m for s in report.prefixes], [2, 2, 2, 2, 2])

    def test_hostile_control_no_finite_normal_form(self):
        # Raw Omega_3/4/5 must NOT reach a finite normal form within any
        # bounded step budget; the stepper refuses to terminate to normal form.
        for k in (3, 4, 5):
            for budget in (0, 1, 10, 500):
                report = guarded_omega_trace(k, budget)
                self.assertFalse(report.has_finite_normal_form)
                # The reducer never yields a normal form within budget.
                steps = list(reduce_leftmost(Term(k=k, m=2), budget))
                self.assertEqual(len(steps), budget)
                if steps:
                    # every after-term still has a redex (m >= 2), never normal.
                    self.assertTrue(all(s.after.m >= 2 for s in steps))


class ReflectionTests(unittest.TestCase):
    def test_positional_trace_is_finer_than_count_only(self):
        # E_4(2) and E_3(3) both land on copy count 4 but differ in arity/delta.
        a, b = count_only_conflation_witness()
        self.assertEqual(a.k, 4)
        self.assertEqual(b.k, 3)
        step_a = contract_leftmost(a)
        step_b = contract_leftmost(b)
        self.assertEqual(step_a.after.m, 4)
        self.assertEqual(step_b.after.m, 4)  # count-only would conflate
        self.assertNotEqual(step_a.delta, step_b.delta)  # positional separates
        self.assertNotEqual(step_a.after.k, step_b.after.k)

    def test_observe_produces_full_positional_trace(self):
        t = Term(k=3, m=2)
        obs = observe(t, budget=5)
        self.assertEqual(obs.k, 3)
        self.assertEqual(obs.addresses, (0, 0, 0, 0, 0))
        # copy counts grow by 1 each step: 3,4,5,6,7
        self.assertEqual(obs.copy_counts, (3, 4, 5, 6, 7))

    def test_reflection_example_types(self):
        a, b = reflection_non_alias_example()
        self.assertEqual(a.k, 3)
        self.assertEqual(b.k, 4)
        self.assertNotEqual(a.k, b.k)


if __name__ == "__main__":
    unittest.main()
