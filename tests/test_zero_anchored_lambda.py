"""Exact independent arithmetic oracles and hostile compiler/certificate controls."""
from dataclasses import replace
from fractions import Fraction as Q
import unittest
from unittest.mock import patch

from observational_succ import c_monoid_succ_embedding as lc
from observational_succ import zero_anchored_lambda as z


def polynomial_source(n):
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def direct_state(n, seed=Q()):
    # A closed finite source sum, not the evaluator's step loop.
    return 16**n*seed+sum((16**(n-j)*polynomial_source(j)
                          for j in range(1, n+1)), Q())


def closure_oracle(term, environment=()):
    """Independent source evaluator: environments, with no de Bruijn shifting."""
    if isinstance(term, z.Literal):
        return Q(term.value)
    if isinstance(term, z.Variable):
        return environment[term.index]
    if isinstance(term, z.Lambda):
        return lambda argument: closure_oracle(term.body, (argument,)+environment)
    if isinstance(term, z.Apply):
        return closure_oracle(term.function, environment)(closure_oracle(term.argument, environment))
    if isinstance(term, z.Primitive):
        if term.name == "origin":
            return lambda seed: (0, seed, seed)
        if term.name == "step":
            return lambda state: (state[0]+1, 16*state[1]+polynomial_source(state[0]+1), state[2])
        if term.name == "recover":
            return lambda state: state[1]/16**state[0]-sum(
                (polynomial_source(j)/16**j for j in range(1, state[0]+1)), Q())
        if term.name == "add":
            return lambda left: lambda right: left+right
        if term.name == "divide16":
            return lambda value: value/16
        if term.name.startswith("forcing:"):
            return polynomial_source(int(term.name.split(":")[1]))
    raise AssertionError("unsupported oracle term")


class EqualitySpoof(str):
    """An in-process payload that compares equal to every claimed string."""
    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False

    __hash__ = str.__hash__


class IntSubclass(int):
    pass


class SourceAuthenticationTests(unittest.TestCase):
    def test_source_spec_is_arithmetic_not_an_arbitrary_label(self):
        self.assertIn("4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)", z.SOURCE_SPEC)
        for digest in ("bbp", "", z.SOURCE_DIGEST[:-1]+"x", None):
            with self.subTest(digest=digest), self.assertRaises(z.CompilerError):
                z.SourceState(0, Q(), source_digest=digest)

    def test_three_seed_recovery_paths(self):
        for n in (0, 1, 2, 5, 13, 31):
            for seed in (Q(), Q(1, 16), Q(-2, 7), Q(111, 37)):
                with self.subTest(n=n, seed=seed):
                    state = z.SourceState(n, direct_state(n, seed), seed)
                    cert = z.certify_state(state, require_zero=False)
                    self.assertEqual(cert.prefix_seed, seed)
                    self.assertEqual(cert.reverse_seed, seed)
                    self.assertEqual(cert.forward_value, state.value)
                    self.assertEqual(cert.original_zero, seed == 0)
                    self.assertTrue(z.verify_source_certificate(cert))

    def test_mutated_state_clock_value_and_seed_fail(self):
        state = z.SourceState(7, direct_state(7))
        for bad in (replace(state, clock=6), replace(state, value=state.value+1),
                    replace(state, seed=Q(1, 16))):
            with self.subTest(bad=bad), self.assertRaises(z.CompilerError):
                z.certify_state(bad, require_zero=False)

    def test_counterseed_cannot_be_declared_zero(self):
        state = z.SourceState(7, direct_state(7, Q(2, 7)), Q(2, 7))
        self.assertFalse(z.certify_state(state, require_zero=False).original_zero)
        with self.assertRaisesRegex(z.CompilerError, "nonzero seed"):
            z.certify_state(state)

    def test_observational_alias_keeps_visible_seed_defect(self):
        for n in (1, 3, 7):
            a = z.SourceState(n, direct_state(n))
            b = z.SourceState(n, direct_state(n, Q(1, 16)), Q(1, 16))
            ca, cb = z.complete_state(a, n+5), z.complete_state(b, n+5)
            self.assertEqual((ca.lower-cb.lower) % 1, 0)
            self.assertEqual(ca.remainder_bound, cb.remainder_bound)
            self.assertEqual(z.certify_state(b, require_zero=False).prefix_seed, Q(1, 16))
            with self.assertRaises(z.CompilerError):
                z.certify_state(b)

    def test_float_bool_and_bad_clocks_rejected(self):
        for n in (True, False, -1, 1.0, "1"):
            with self.subTest(n=n), self.assertRaises(z.CompilerError):
                z.SourceState(n, Q())
        for value in (True, False, 0.0, 0.5, "0", None):
            for field in ("value", "seed"):
                with self.subTest(value=value, field=field), self.assertRaises(z.CompilerError):
                    z.SourceState(0, **({"value": value} if field == "value"
                                      else {"value": Q(), "seed": value}))

    def test_source_certificate_fields_are_replayed(self):
        cert = z.certify_state(z.SourceState(5, direct_state(5)))
        for bad in (replace(cert, prefix_seed=Q(1)), replace(cert, reverse_seed=Q(1)),
                    replace(cert, forward_value=Q(1)), replace(cert, original_zero=False),
                    replace(cert, prefix_seed=False), replace(cert, original_zero=1),
                    replace(cert, status="NORMALITY_PROVED")):
            with self.subTest(bad=bad), self.assertRaises(z.CompilerError):
                z.verify_source_certificate(bad)

    def test_source_status_and_passport_equality_spoofs_are_rejected(self):
        state = z.SourceState(0, Q())
        cert = z.certify_state(state)
        with self.assertRaises(z.CompilerError):
            z.verify_source_certificate(replace(cert, status=EqualitySpoof("NORMALITY_PROVED")))
        with self.assertRaises(z.CompilerError):
            z.SourceState(0, Q(), source_digest=EqualitySpoof("wrong-source"))
        # Replay must also revalidate a previously constructed frozen object.
        object.__setattr__(state, "source_digest", EqualitySpoof("wrong-source"))
        with self.assertRaises(z.CompilerError):
            z.certify_state(state)


class TypedCompilerTests(unittest.TestCase):
    def test_state_compilation_executes_real_steps(self):
        for n in (0, 1, 2, 5, 12):
            for seed in (Q(), Q(1, 16), Q(-2, 7)):
                program = z.compile_state(n, seed)
                result = z.run(program)
                self.assertEqual(result.status, "FINITE_REDUCTION_VERIFIED")
                self.assertEqual(result.value, z.SourceState(n, direct_state(n, seed), seed))
                self.assertEqual(result.beta_steps, n)
                self.assertEqual(result.delta_steps, n+1)
                self.assertFalse(result.statistical_contraction_proved)

    def test_normal_applicative_and_independent_closure_agree(self):
        for n in (0, 1, 4, 9):
            term = z.state_term(n, Q(2, 7))
            compiled = z.compile_term(term)
            left, right = z.run(compiled), z.run(compiled, strategy="applicative")
            raw = closure_oracle(term)
            self.assertEqual(left.value, right.value)
            self.assertEqual((left.value.clock, left.value.value, left.value.seed), raw)

    def test_nested_outer_variable_survives_binder_removal(self):
        # ((lambda s. lambda q. step s) authentic_state) 99.
        term = z.Apply(z.Apply(z.Lambda(z.STATE, z.Lambda(z.RAT,
            z.Apply(z.Primitive("step"), z.Variable(1)))), z.state_term(4)), z.Literal(Q(99)))
        p = z.compile_term(term)
        for strategy in ("normal", "applicative"):
            result = z.run(p, strategy=strategy)
            self.assertEqual(result.value.value, direct_state(5))
            self.assertEqual(result.value.seed, 0)
            self.assertEqual(result.value.clock, 5)
        self.assertEqual(closure_oracle(term), (5, direct_state(5), Q()))

    def test_lambda_substitution_with_nested_bound_arguments(self):
        # (lambda a. (lambda b. lambda c. a+b) a) 3, then apply 7 -> 6.
        add = z.Primitive("add")
        body = z.Apply(z.Lambda(z.RAT, z.Lambda(z.RAT,
                        z.Apply(z.Apply(add, z.Variable(2)), z.Variable(1)))), z.Variable(0))
        term = z.Apply(z.Apply(z.Lambda(z.RAT, body), z.Literal(Q(3))), z.Literal(Q(7)))
        p = z.compile_term(term)
        self.assertEqual(z.run(p).value, Q(6))
        self.assertEqual(z.run(p, strategy="applicative").value, Q(6))
        self.assertEqual(closure_oracle(term), Q(6))

    def test_recover_lambda_compiles_to_literal_zero(self):
        recover = z.Lambda(z.STATE, z.Apply(z.Primitive("recover"), z.Variable(0)))
        for n in (0, 2, 7):
            term = z.Apply(recover, z.state_term(n))
            result = z.run(z.compile_term(term))
            self.assertEqual(result.value, Q())
            self.assertEqual(result.reduct, lc.CONST("q:0/1"))

    def test_guarded_unfoldings_equal_independent_sum(self):
        for n in (0, 1, 7, 23):
            for depth in (0, 1, 2, 5, 11):
                term = z.guarded_tail_term(n, depth)
                p = z.compile_term(term)
                expected = sum((polynomial_source(n+j)/16**j
                                for j in range(1, depth+1)), Q())
                left, right = z.run(p), z.run(p, strategy="applicative")
                self.assertEqual(left.value, expected)
                self.assertEqual(right.value, expected)
                self.assertEqual(closure_oracle(term), expected)
                self.assertEqual(left.beta_steps, depth)
                self.assertEqual(left.delta_steps, 3*depth)

    def test_beta_budget_is_not_a_false_normality_or_failure_claim(self):
        p = z.compile_state(5)
        result = z.run(p, max_steps=3)
        self.assertEqual(result.status, "UNRESOLVED_BUDGET")
        self.assertIsNone(result.value)
        self.assertEqual(result.beta_steps+result.delta_steps, 3)
        self.assertFalse(result.statistical_contraction_proved)
        self.assertEqual(z.run(p, max_steps=11).status, "FINITE_REDUCTION_VERIFIED")

    def test_reduction_strategies_can_spend_different_finite_budgets(self):
        term = z.Apply(z.Lambda(z.RAT, z.Literal(Q(7))), z.guarded_tail_term(0, 5))
        p = z.compile_term(term)
        self.assertEqual(z.run(p, max_steps=1).value, 7)
        self.assertEqual(z.run(p, strategy="applicative", max_steps=1).status,
                         "UNRESOLVED_BUDGET")
        self.assertEqual(z.run(p, strategy="applicative").value, 7)

    def test_mutated_target_code_type_or_passport_rejected(self):
        p = z.compile_state(2)
        for bad in (replace(p, code=lc.CONST("q:0/1")), replace(p, result_type=z.RAT),
                    replace(p, source_digest="wrong"), replace(p, source=z.state_term(3))):
            with self.subTest(bad=bad), self.assertRaises(z.CompilerError):
                z.run(bad)

    def test_target_token_equality_cannot_change_a_literal_result(self):
        p = z.compile_term(z.Literal(Q(5)))
        bad = replace(p, code=lc.CONST(EqualitySpoof("q:0/1")))
        for action in (z.verify_program, z.run):
            with self.assertRaises(z.CompilerError):
                action(bad)
        self.assertEqual(z.run(p).value, Q(5))

    def test_target_node_and_all_field_types_are_validated_recursively(self):
        class TargetSubclass(lc.T):
            pass

        p = z.compile_term(z.Apply(z.Lambda(z.RAT, z.Variable(0)), z.Literal(Q(5))))
        root = p.code
        bad_codes = (
            replace(root, tag=EqualitySpoof("CONST")),
            replace(root, name=EqualitySpoof("")),
            replace(root, idx=True),
            replace(root, idx=IntSubclass(0)),
            replace(root, body=object()),
            replace(root, a=lc.CONST(EqualitySpoof("q:0/1"))),
            replace(root, f=TargetSubclass("CONST", name="q:0/1")),
            replace(root, a=replace(root.a, body=lc.V(0))),
            replace(root, f=replace(root.f, body=replace(root.f.body, name="unused"))),
        )
        for code in bad_codes:
            with self.subTest(code=code), self.assertRaises(z.CompilerError):
                z.run(replace(p, code=code))

    def test_source_ast_type_and_passport_subclasses_are_rejected(self):
        class LiteralSubclass(z.Literal):
            pass

        class ArrowSubclass(z.Arrow):
            pass

        bad_terms = (
            LiteralSubclass(Q(5)),
            z.Apply(z.Lambda(z.RAT, z.Variable(0)), LiteralSubclass(Q(5))),
            z.Lambda(EqualitySpoof("wrong-type"), z.Variable(0)),
            z.Lambda(z.Arrow(z.RAT, EqualitySpoof(z.STATE)), z.Variable(0)),
            z.Lambda(ArrowSubclass(z.RAT, z.RAT), z.Variable(0)),
            z.Primitive(EqualitySpoof("origin")),
            z.Variable(IntSubclass(0)),
        )
        for term in bad_terms:
            with self.subTest(term=term), self.assertRaises(z.CompilerError):
                z.compile_term(term)
        p = z.compile_term(z.Literal(Q(5)))
        for bad in (replace(p, source_digest=EqualitySpoof("wrong")),
                    replace(p, result_type=EqualitySpoof("wrong")),
                    replace(p, source=LiteralSubclass(Q(0)))):
            with self.subTest(bad=bad), self.assertRaises(z.CompilerError):
                z.verify_program(bad)
        with self.assertRaises(z.CompilerError):
            z.run(p, strategy=EqualitySpoof("anything"))

    def test_type_errors_unknown_primitives_and_malformed_inputs(self):
        terms = (z.Variable(0), z.Variable(True), z.Variable(-1), z.Literal(0.0),
                 z.Literal(True), z.Primitive("normality"), z.Primitive("forcing:0"),
                 z.Primitive("forcing:01"), z.Primitive("forcing:-1"),
                 z.Primitive("forcing:1.0"), z.Lambda("fake", z.Variable(0)),
                 z.Apply(z.Primitive("step"), z.Literal(Q())),
                 z.Apply(z.Literal(Q()), z.Literal(Q())), object())
        for term in terms:
            with self.subTest(term=term), self.assertRaises(z.CompilerError):
                z.compile_term(term)

    def test_self_application_is_rejected_by_simple_types(self):
        with self.assertRaises(z.CompilerError):
            z.compile_term(z.Lambda(z.RAT, z.Apply(z.Variable(0), z.Variable(0))))

    def test_changed_source_function_cannot_reuse_fixed_passport(self):
        with patch.object(z, "forcing", lambda n: polynomial_source(n)+Q(1, 7)):
            for p in (z.compile_state(1), z.compile_term(z.guarded_tail_term(0, 1))):
                with self.assertRaisesRegex(z.CompilerError, "four-pole authentication"):
                    z.run(p)

    def test_bad_budget_strategy_and_tail_clocks(self):
        p = z.compile_state(0)
        for budget in (True, -1, 1.0):
            with self.assertRaises(z.CompilerError):
                z.run(p, max_steps=budget)
        with self.assertRaises(z.CompilerError):
            z.run(p, strategy="pretend")
        for clock, depth in ((True, 1), (1, True), (-1, 0), (0, -1)):
            with self.assertRaises(z.CompilerError):
                z.guarded_tail_term(clock, depth)


class CompletionTests(unittest.TestCase):
    def test_two_completion_paths_and_source_tail_bound(self):
        for n in (0, 1, 4, 9):
            for depth in (0, 1, 5, 11):
                for seed in (Q(), Q(-2, 7)):
                    state = z.SourceState(n, direct_state(n, seed), seed)
                    c = z.complete_state(state, n+depth)
                    finite = sum((polynomial_source(j)/16**(j-n)
                                  for j in range(n+1, n+depth+1)), Q())
                    self.assertEqual(c.lower, state.value+finite)
                    self.assertEqual(c.finite_tail, finite)
                    self.assertEqual(c.remainder_bound,
                                     polynomial_source(n+depth+1)/(15*16**depth))
                    self.assertTrue(z.verify_completion_certificate(c))

    def test_enclosures_nest_and_transport_at_common_horizon(self):
        for n in (0, 2, 7):
            c = z.complete_state(z.SourceState(n, direct_state(n)), n+3)
            finer = z.complete_state(c.state, n+7)
            self.assertLess(c.lower, finer.lower)
            self.assertLess(finer.upper, c.upper)
        a = z.complete_state(z.SourceState(3, direct_state(3)), 13)
        b = z.complete_state(z.SourceState(7, direct_state(7)), 13)
        self.assertEqual(b.lower, 16**4*a.lower)
        self.assertEqual(b.upper, 16**4*a.upper)

    def test_boundary_and_mutation_rejection(self):
        c = z.complete_state(z.SourceState(5, direct_state(5)), 9)
        with self.assertRaises(z.CompilerError):
            z.complete_state(c.state, 4)
        for bad in (replace(c, lower=c.lower+Q(1, 100)), replace(c, upper=c.upper+1),
                    replace(c, finite_tail=Q()), replace(c, remainder_bound=Q()),
                    replace(c, horizon=10), replace(c, status="NORMALITY_PROVED")):
            with self.subTest(bad=bad), self.assertRaises(z.CompilerError):
                z.verify_completion_certificate(bad)
        zero = z.complete_state(z.SourceState(0, Q()), 0)
        with self.assertRaises(z.CompilerError):
            z.verify_completion_certificate(replace(zero, lower=False))

    def test_mutated_tail_budget_rejected(self):
        with patch.object(z, "source_tail_budget", lambda n: Q()):
            with self.assertRaisesRegex(z.CompilerError, "tail budget"):
                z.complete_state(z.SourceState(0, Q()), 2)

    def test_completion_status_equality_spoof_is_rejected(self):
        c = z.complete_state(z.SourceState(0, Q()), 2)
        with self.assertRaises(z.CompilerError):
            z.verify_completion_certificate(replace(c, status=EqualitySpoof("NORMALITY_PROVED")))


if __name__ == "__main__":
    unittest.main()
