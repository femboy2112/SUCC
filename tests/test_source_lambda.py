"""Independent finite-hostile controls for the source-indexed lambda calculus."""
import unittest
from fractions import Fraction as Q
from math import gcd, lcm
from itertools import product

from observational_succ.source_lambda import (
    AccessGap, Atlas, App, Bool, BOOL, BudgetGap, Compatible, Eq,
    First, Forget, FuncT, Join, Lam, LambdaError, Pair, PairT,
    Passport, PrimeMul, Project, Read, Report, ReportT, Residue, ResidueT,
    Second, Select, Succ, Sum, TypeFault, Var, check,
    compare_observers, execute, signed_witness,
)

P = Passport("SUCC-lambda-fixture", 7, "modular-Z")


class LambdaCoreTests(unittest.TestCase):
    def setUp(self):
        self.atlas = Atlas.from_integer(P, 17, (2, 3, 4, 5, 6, 8, 12))

    def test_beta_reduction_with_bound_variable(self):
        expr = App(Lam(ResidueT(8), Sum(Var(0), Succ(Var(0)))), Residue(8, 3))
        self.assertEqual(execute(expr, self.atlas).value, 7)

    def test_de_bruijn_nested_closure(self):
        expr = App(App(Lam(ResidueT(7), Lam(ResidueT(7),
                               Sum(Var(1), Var(0)))), Residue(7, 4)), Residue(7, 5))
        self.assertEqual(execute(expr, self.atlas).value, 2)

    def test_latent_observation_is_statically_propagated(self):
        f = Lam(ResidueT(5), Sum(Var(0), Forget(Read(5))))
        self.assertEqual(check(f, P).may_read, frozenset())
        self.assertEqual(check(f, P).type, FuncT(ResidueT(5), ResidueT(5), frozenset((5,))))
        expression = App(f, Residue(5, 2))
        self.assertEqual(check(expression, P).may_read, frozenset((5,)))
        result = execute(expression, self.atlas)
        self.assertEqual(result.value, (2 + 17) % 5)
        self.assertEqual(result.observed, (5,))

    def test_projection_is_derived_not_a_new_observation(self):
        out = execute(Project(Read(12), 4), self.atlas)
        self.assertEqual(out.observed, (12,))
        self.assertEqual(out.may_read, frozenset((12,)))
        self.assertEqual((out.value.modulus, out.value.value), (4, 1))
        self.assertEqual(out.value.lineage, ("replay:recorded:12", "derived:project:12->4"))

    def test_crt_join_general_and_non_coprime(self):
        for a, b in ((3, 5), (4, 6), (2, 12), (12, 8), (6, 6)):
            expr = Join(Read(a), Read(b))
            r = execute(expr, self.atlas)
            self.assertEqual(r.value.modulus, lcm(a, b))
            self.assertEqual(r.value.value, 17 % lcm(a, b))
            self.assertEqual(r.observed, (a, b))
            self.assertTrue(r.value.lineage[-1].startswith("derived:crt:"))

    def test_explicit_crt_does_not_invent_recorded_lcm_probe(self):
        tiny = Atlas.from_integer(P, 17, (3, 5))
        with self.assertRaises(AccessGap):
            execute(Read(15), tiny)
        result = execute(Join(Read(3), Read(5)), tiny)
        self.assertEqual(result.value.value, 2)
        self.assertEqual(result.observed, (3, 5))
        self.assertNotIn(15, result.observed)

    def test_coherence_exposed_in_bool(self):
        out = execute(Compatible(Read(4), Read(6)), self.atlas)
        self.assertEqual(out.type, BOOL)
        self.assertTrue(out.value)

    def test_derived_arithmetic_not_new_measurement(self):
        program = PrimeMul(3, Succ(Forget(Read(8))))
        out = execute(program, self.atlas)
        self.assertEqual(out.value, 3 * ((17 + 1) % 8) % 8)
        self.assertEqual(out.observed, (8,))
        self.assertEqual(out.type, ResidueT(8))

    def test_exact_affine_relation_with_true_prime(self):
        for n, p, v in product((5, 7, 11), (2, 3, 5), range(5)):
            left = PrimeMul(p, Succ(Residue(n, v)))
            right = PrimeMul(p, Residue(n, v))
            for _ in range(p):
                right = Succ(right)
            self.assertEqual(execute(left, self.atlas).value,
                             execute(right, self.atlas).value)

    def test_pairs_and_select(self):
        pair = Pair(Residue(4, 2), Bool(True))
        self.assertEqual(execute(First(pair), self.atlas).value, 2)
        self.assertTrue(execute(Second(pair), self.atlas).value)
        self.assertEqual(check(pair, P).type, PairT(ResidueT(4), BOOL))
        out = execute(Select(Bool(True), Residue(3, 2), Forget(Read(3))), Atlas(P, ()))
        self.assertEqual(out.value, 2)
        self.assertEqual(out.observed, ())
        self.assertEqual(out.may_read, frozenset((3,)))

    def test_duplicate_read_is_counted_but_not_new_source_row(self):
        out = execute(Pair(Read(3), Read(3)), self.atlas)
        self.assertEqual(out.observed, (3, 3))
        self.assertEqual(out.may_read, frozenset((3,)))

    def test_closed_execution_marks_no_global_claim(self):
        r = execute(Read(2), self.atlas)
        self.assertFalse(r.globally_complete)
        self.assertEqual(r.status, "FINITE_MODEL_EXECUTED")
        self.assertEqual(r.passport, P)


class HostileBoundaryTests(unittest.TestCase):
    def test_invalid_rows_not_canonical_or_sorted(self):
        for rows in (((2, 2),), ((3, 0), (2, 1)), ((2, -1),), ((3, 1), (3, 1))):
            with self.subTest(rows=rows), self.assertRaises(LambdaError):
                Atlas(P, rows)

    def test_actual_crt_inconsistency_is_rejected(self):
        with self.assertRaisesRegex(LambdaError, "CRT coherence"):
            Atlas(P, ((2, 0), (4, 1)))

    def test_valid_nontrivial_crt_fixture(self):
        a = Atlas(P, ((4, 3), (6, 5)))
        self.assertEqual(execute(Join(Read(4), Read(6)), a).value.value, 11)

    def test_source_change_epoch_cannot_forge_agreement(self):
        other = Atlas.from_integer(Passport(P.source_id, P.epoch + 1), 17, (3,))
        with self.assertRaises(TypeFault):
            compare_observers(Read(3), Atlas.from_integer(P, 17, (3,)), other)
        with self.assertRaises(TypeFault):
            check(Project(Var(0), 3), P, (ReportT(other.passport, 3),))

    def test_wrong_modulus_projection(self):
        with self.assertRaisesRegex(TypeFault, "divisibility"):
            check(Project(Read(6), 4), P)

    def test_missing_source_row_not_falsehood(self):
        with self.assertRaises(AccessGap):
            execute(Read(7), Atlas(P, ((3, 1),)))

    def test_malformed_programs(self):
        for term in (Var(0), Var(-1), Read(1), Residue(4, 4), Residue(4, True),
                     Eq(Residue(2, 1), Residue(3, 1)),
                     App(Lam(ResidueT(2), Var(0)), Residue(3, 1)),
                     Succ(Read(2)), PrimeMul(6, Residue(7, 3)),
                     Select(Residue(2, 1), Bool(True), Bool(False)),
                     First(Bool(True)), Lam("fake-type", Var(0)),
                     Lam(ReportT(Passport("other", 7), 3), Var(0))):
            with self.subTest(term=repr(term)), self.assertRaises(LambdaError):
                check(term, P)

    def test_non_prime_independent_jet_gate(self):
        for composite in (4, 6, 9, 15, 21, True):
            with self.subTest(composite=composite), self.assertRaises(LambdaError):
                check(PrimeMul(composite, Residue(11, 1)), P)

    def test_fuel_and_probe_budget_expiration(self):
        a = Atlas.from_integer(P, 3, (5,))
        with self.assertRaises(BudgetGap):
            execute(Succ(Residue(5, 2)), a, max_steps=1)
        with self.assertRaises(BudgetGap):
            execute(Read(5), a, max_read_bits=2)

    def test_no_float_or_bool_fixture(self):
        for bad in (True, 2.0):
            with self.assertRaises(LambdaError):
                Atlas.from_integer(P, bad, (2,))


class FiniteSupportTests(unittest.TestCase):
    def test_indistinguishable_small_probes_with_hidden_deep_difference(self):
        a = Atlas.from_integer(P, 0, (2, 3, 5))
        b = Atlas.from_integer(P, 6, (2, 3, 5))
        eq = compare_observers(Forget(Read(2)), a, b)
        self.assertEqual(eq.status, "CERTIFIED_FINITE_AGREEMENT")
        self.assertEqual(eq.footprint, frozenset((2,)))
        self.assertTrue(eq.same_output)
        not_certified = compare_observers(Forget(Read(5)), a, b)
        self.assertEqual(not_certified.status, "NOT_CERTIFIED")
        self.assertIsNone(not_certified.same_output)
        self.assertFalse(not_certified.globally_complete)

    def test_full_footprint_is_required_even_with_lazy_unreachable_branch(self):
        a = Atlas.from_integer(P, 0, (2,))
        b = Atlas.from_integer(P, 0, (2,))
        expression = Select(Bool(True), Forget(Read(2)), Forget(Project(Read(6), 2)))
        self.assertEqual(execute(expression, a).value, 0)
        out = compare_observers(expression, a, b)
        self.assertEqual(out.status, "ACCESS_GAP")

    def test_function_value_not_false_extensionality(self):
        a, b = (Atlas.from_integer(P, s, (3,)) for s in (0, 1))
        with self.assertRaisesRegex(TypeFault, "function-valued"):
            compare_observers(Lam(ResidueT(3), Forget(Read(3))), a, b)

    def test_all_small_probe_menus_have_hidden_integer_pair(self):
        for moduli in ((2,), (2, 3), (2, 3, 4, 6), (2, 3, 5, 7)):
            m = lcm(*moduli)
            a = Atlas.from_integer(P, 0, moduli)
            b = Atlas.from_integer(P, m, moduli)
            program = Pair(Forget(Read(moduli[0])), Forget(Read(moduli[-1])))
            self.assertEqual(compare_observers(program, a, b).status,
                             "CERTIFIED_FINITE_AGREEMENT")
            self.assertNotEqual(m, 0)
            # A later modulus m+1 distinguishes integers 0 and m.
            deeper = Atlas.from_integer(P, m, (m + 1,))
            self.assertEqual(execute(Forget(Read(m+1)), deeper).value, m)

    def test_randomized_seed_holdout_on_crt_join(self):
        for seed in (-97, -2, 0, 1, 13, 527):
            for m, n in ((4, 6), (3, 7), (8, 12), (5, 10)):
                a = Atlas.from_integer(P, seed, (m, n) if m != n else (m,))
                r = execute(Join(Read(m), Read(n)), a)
                self.assertEqual(r.value.value, seed % lcm(m, n))
                self.assertEqual(r.value.modulus, lcm(m, n))


class FiniteSignTests(unittest.TestCase):
    def test_exact_negative_witness_does_not_promote_global_weil(self):
        cert = signed_witness(((1, 2), (2, 1)), (1, -1))
        self.assertEqual(cert.energy, Q(-2))
        self.assertEqual(cert.status, "EXACT_FINITE_NEGATIVE")
        self.assertTrue(cert.finite_only)
        self.assertFalse(cert.source_is_authenticated)
        self.assertFalse(cert.proves_rh)

    def test_positive_finite_form_not_universal_positive_certificate(self):
        cert = signed_witness(((2, 0), (0, 3)), (1, 1))
        self.assertEqual(cert.energy, 5)
        self.assertEqual(cert.status, "NOT_NEGATIVE")
        self.assertTrue(cert.finite_only)

    def test_no_float_or_asymmetry_or_zero_vector(self):
        for matrix, vector in ((((1.0,),), (1,)), (((True,),), (1,)),
                               (((0, 1), (0, 0)), (1, 1)),
                               (((1,),), (0,)), (((1, 2),), (1, 2))):
            with self.subTest(matrix=matrix), self.assertRaises(LambdaError):
                signed_witness(matrix, vector)

    def test_fraction_exact(self):
        cert = signed_witness(((Q(1, 6),),), (Q(1, 3),))
        self.assertEqual(cert.energy, Q(1, 54))


if __name__ == "__main__":
    unittest.main()
