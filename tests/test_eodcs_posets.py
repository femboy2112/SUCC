"""Hostile finite-poset syntax/semantic synthesis tests (stdlib unittest)."""
import unittest
from itertools import product

from observational_succ.relational_model_genetics import GeneticsError
from observational_succ.finite_poset_synthesis import (
    FinitePoset, PosetFunctor, PairedPosetSource, chain, all_functors,
    all_isomorphisms, natural_transformation, check_adjunction,
    infer_right_adjoint, is_order_quotient, synthesize_with_obstructions,
    quotient_demo,
)


class TestFinitePosetSynthesis(unittest.TestCase):
    def setUp(self):
        self.a = chain("a", "b", "c")
        self.b = chain("cold", "warm")
        self.table = PairedPosetSource(
            "same-source", 0, "ordered", self.a, self.b,
            (("s0", "a", "cold"), ("s1", "b", "cold"),
             ("s2", "c", "warm")), True)

    def test_first_grammar_disproved_by_cardinality(self):
        self.assertEqual(all_isomorphisms(self.a, self.b), ())
        r = synthesize_with_obstructions(self.table)
        self.assertEqual(r.obstruction, "cardinality-precludes-bijection")
        self.assertEqual(r.resulting_grammar, "finite-poset-functor")
        self.assertTrue(r.source_class_certified)
        self.assertEqual(r.unique.images, ("cold", "cold", "warm"))

    def test_source_counterexamples_really_exclude_candidates(self):
        r = synthesize_with_obstructions(self.table)
        self.assertTrue(r.exclusions)
        oracle = self.table.oracle()
        for witness in r.exclusions:
            self.assertNotEqual(witness.predicted, witness.actual)
            self.assertEqual(witness.actual, oracle[witness.tested_input])
        self.assertEqual(set(r.probes), set(self.a.objects))

    def test_a_real_adjunction_and_quotient_discovered(self):
        r = synthesize_with_obstructions(self.table)
        self.assertEqual(r.right_adjoint.images, ("b", "c"))
        self.assertTrue(check_adjunction(r.unique, r.right_adjoint))
        self.assertTrue(r.order_quotient)
        self.assertEqual(quotient_demo()["fibers"], [["a", "b"], ["c"]])

    def test_complete_source_coverage_is_not_a_flag_only(self):
        with self.assertRaises(GeneticsError):
            PairedPosetSource("s", 0, "b", self.a, self.b,
                              (("s0", "a", "cold"),), True)

    def test_partial_source_keeps_live_rivals_and_no_certificate(self):
        t = PairedPosetSource("s", 0, "b", self.a, self.b,
                             (("s0", "a", "cold"),), False)
        r = synthesize_with_obstructions(t)
        self.assertEqual(len(r.candidates), 3)
        self.assertFalse(r.source_class_certified)
        self.assertIsNone(r.right_adjoint)
        self.assertIsNone(r.unique)

    def test_no_valid_functor_escapes_by_changing_the_source(self):
        a, b = chain("a", "b"), chain("cold", "warm")
        t = PairedPosetSource("s", 1, "b", a, b,
                             (("s0", "a", "warm"), ("s1", "b", "cold")), True)
        r = synthesize_with_obstructions(t)
        self.assertEqual(r.candidates, ())
        self.assertFalse(r.source_class_certified)
        self.assertEqual(r.obstruction, "source-refutes-every-isomorphism")

    def test_mutated_nonmonotone_functor_cannot_be_constructed(self):
        with self.assertRaises(GeneticsError):
            PosetFunctor(chain("a", "b"), chain("0", "1"), ("1", "0"))

    def test_isomorphism_must_reflect_order(self):
        two_discrete = FinitePoset(("a", "b"), frozenset(
            {("a", "a"), ("b", "b")}))
        self.assertEqual(all_isomorphisms(two_discrete, chain("0", "1")), ())

    def test_naturality_components_not_assumed_by_similar_names(self):
        f = PosetFunctor(self.a, self.b, ("cold", "cold", "warm"))
        g = PosetFunctor(self.a, self.b, ("warm", "warm", "warm"))
        self.assertTrue(natural_transformation(f, g))
        self.assertFalse(natural_transformation(g, f))
        with self.assertRaises(GeneticsError):
            natural_transformation(f, PosetFunctor(self.b, self.a, ("a", "c")))

    def test_composition_typed_and_preserves_monotonicity(self):
        f = PosetFunctor(self.a, self.b, ("cold", "cold", "warm"))
        g = PosetFunctor(self.b, chain("x", "y", "z"), ("x", "z"))
        h = f.then(g)
        self.assertEqual(h.images, ("x", "x", "z"))
        with self.assertRaises(GeneticsError):
            g.then(f)

    def test_a_left_functor_need_not_have_a_right_adjoint(self):
        f = PosetFunctor(self.a, self.b, ("warm", "warm", "warm"))
        self.assertIsNone(infer_right_adjoint(f))
        self.assertFalse(is_order_quotient(f))

    def test_surjective_functor_not_automatically_order_quotient(self):
        a = FinitePoset(("a", "b"), frozenset(
            {("a", "a"), ("b", "b")}))
        f = PosetFunctor(a, chain("x", "y"), ("x", "y"))
        self.assertFalse(is_order_quotient(f))

    def test_adjoint_oracle_exhaustively_all_small_chain_functors(self):
        # Independent RHS formula: G(y) must be the largest x with F(x)<=y.
        for na in (1, 2, 3):
            for nb in (1, 2, 3):
                a = chain(*(str(i) for i in range(na)))
                b = chain(*(str(i) for i in range(nb)))
                for f in all_functors(a, b):
                    g = infer_right_adjoint(f)
                    expected = []
                    for y in b.objects:
                        valid = [x for x in a.objects if b.le(f(x), y)]
                        if not valid:
                            expected = None
                            break
                        expected.append(valid[-1])
                    if expected is None:
                        self.assertIsNone(g)
                    else:
                        self.assertIsNotNone(g)
                        self.assertEqual(g.images, tuple(expected))

    def test_adjunction_falsifier_exhaustive_hom_pairs(self):
        r = synthesize_with_obstructions(self.table)
        g = r.right_adjoint
        self.assertEqual(sum(check_adjunction(r.unique, x)
                             for x in all_functors(self.b, self.a)), 1)
        self.assertTrue(all(self.b.le(r.unique(x), y) == self.a.le(x, g(y))
                            for x, y in product(self.a.objects, self.b.objects)))

    def test_corrupted_poset_laws_fail_closed(self):
        with self.assertRaises(GeneticsError):
            FinitePoset(("a", "b"), frozenset({("a", "a")}))
        with self.assertRaises(GeneticsError):
            FinitePoset(("a", "b"), frozenset(
                {("a", "a"), ("b", "b"), ("a", "b"), ("b", "a")}))
        with self.assertRaises(GeneticsError):
            FinitePoset(("a", "b", "c"), frozenset(
                {("a", "a"), ("b", "b"), ("c", "c"),
                 ("a", "b"), ("b", "c")}))

    def test_mismatched_epoch_not_promoted_to_parent_source(self):
        t = PairedPosetSource("same-source", 2, "ordered", self.a, self.b,
                             self.table.observations, True)
        r = synthesize_with_obstructions(t)
        self.assertEqual(r.epoch, 2)
        self.assertNotEqual(r.epoch, synthesize_with_obstructions(self.table).epoch)


if __name__ == "__main__":
    unittest.main()
