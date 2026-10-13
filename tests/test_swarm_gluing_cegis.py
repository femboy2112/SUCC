"""X03 independent finite oracle and adversarial projection controls."""

from itertools import product
import unittest

from observational_succ.swarm_gluing_cegis import (
    FiniteTable, LocalRelation, TypedGrammar, global_sections, lift_relations,
    minimal_unsat_core, monotone_cegis, triangle_problem,
)


def oracle(source, relations):
    """Independent assignment/dictionary join, not the solver's predicate code."""
    answers = []
    for row in source.rows:
        assignment = dict(zip(source.variables, row))
        if all(tuple(assignment[v] for v in relation.scope) in relation.allowed
               for relation in relations):
            answers.append(row)
    return tuple(answers)


class GluingCegisTests(unittest.TestCase):
    def test_grammar_core_does_not_prune_source_retaining_extension(self):
        source = FiniteTable.cartesian(("x",), ((0, 1),))
        restricted = FiniteTable(("x",), ((0, 1),), ((0,),))
        relation = LocalRelation("one", ("x",), ((1,),))
        old = monotone_cegis(TypedGrammar(source, restricted), (relation,))
        self.assertEqual(old["core"], ("one",))
        self.assertEqual(old["core_scope"], "GRAMMAR_IMAGE")
        self.assertFalse(old["core_source_verified"])
        extended = monotone_cegis(TypedGrammar(source, source), (relation,))
        self.assertEqual(extended["status"], "SAT_SOURCE")
        self.assertEqual(extended["original_witness"], (1,))
        self.assertIsNone(extended["core_scope"])
        opposite = LocalRelation("zero", ("x",), ((0,),))
        impossible = monotone_cegis(TypedGrammar(source, source), (relation, opposite))
        self.assertEqual(impossible["core_scope"], "SOURCE")
        self.assertTrue(impossible["core_source_verified"])

    def test_all_binary_triangle_families_against_independent_join(self):
        source, _ = triangle_problem()
        pairs = tuple(product((0, 1), repeat=2))
        relations = tuple(tuple(pair for j, pair in enumerate(pairs) if mask & (1 << j))
                          for mask in range(16))
        scopes = (("x", "y"), ("y", "z"), ("x", "z"))
        for tables in product(relations, repeat=3):
            constraints = tuple(LocalRelation(str(j), scope, table)
                                for j, (scope, table) in enumerate(zip(scopes, tables)))
            expected = oracle(source, constraints)
            result = monotone_cegis(TypedGrammar(source, source), constraints)
            self.assertEqual(global_sections(source, constraints), expected)
            self.assertEqual(result["status"], "SAT_SOURCE" if expected else "UNSAT_SOURCE")
            self.assertLessEqual(len(result["rejections"]), 3)
            self.assertEqual(len(result["learned"]), len(set(result["learned"])))
            if expected:
                self.assertIn(result["original_witness"], expected)
            else:
                core = tuple(r for r in constraints if r.name in result["core"])
                self.assertFalse(oracle(source, core))
                for removed in core:
                    self.assertTrue(oracle(source, tuple(r for r in core if r != removed)))

    def test_pairwise_support_agreement_has_minimal_three_constraint_obstruction(self):
        source, constraints = triangle_problem()
        for i, left in enumerate(constraints):
            for right in constraints[i + 1:]:
                overlap = tuple(v for v in left.scope if v in right.scope)
                l = {tuple(row[left.scope.index(v)] for v in overlap) for row in left.allowed}
                r = {tuple(row[right.scope.index(v)] for v in overlap) for row in right.allowed}
                self.assertEqual(l, r)
        self.assertEqual(minimal_unsat_core(source, constraints),
                         ("xy_equal", "yz_equal", "xz_unequal"))

    def test_surjective_hidden_variables_preserve_all_subproblem_satisfiability(self):
        source, constraints = triangle_problem()
        extension = FiniteTable(source.variables + ("hidden",), source.domains + ((0, 1),),
                                tuple(row + (h,) for row in source.rows for h in (0, 1)))
        grammar = TypedGrammar(source, extension)
        for mask in range(8):
            selected = tuple(r for j, r in enumerate(constraints) if mask & (1 << j))
            lifted = lift_relations(grammar, selected)
            projected = {row[:3] for row in global_sections(extension, lifted)}
            self.assertEqual(projected, set(global_sections(source, selected)))
        self.assertEqual(minimal_unsat_core(extension, constraints),
                         minimal_unsat_core(source, constraints))
        self.assertEqual(monotone_cegis(grammar, constraints)["status"], "UNSAT_SOURCE")

    def test_deterministic_probe_graph_preserves_obstruction_and_positive_source(self):
        source, constraints = triangle_problem()
        extension = FiniteTable(source.variables + ("parity",), source.domains + ((0, 1),),
                                tuple(row + (sum(row) % 2,) for row in source.rows))
        grammar = TypedGrammar(source, extension)
        self.assertEqual(monotone_cegis(grammar, constraints)["status"], "UNSAT_SOURCE")
        self.assertEqual(monotone_cegis(grammar, constraints[:2])["status"], "SAT_SOURCE")

    def test_incomplete_grammar_cannot_certify_original_source_unsat(self):
        source = FiniteTable.cartesian(("x",), ((0, 1),))
        grammar = TypedGrammar(source, FiniteTable(("x",), ((0, 1),), ((0,),)))
        relation = LocalRelation("one", ("x",), ((1,),))
        result = monotone_cegis(grammar, (relation,))
        self.assertEqual(result["status"], "UNSAT_GRAMMAR")
        self.assertEqual(global_sections(source, (relation,)), ((1,),))

    def test_nonsurjective_restriction_can_destroy_core_minimality(self):
        source = FiniteTable.cartesian(("x",), ((0, 1),))
        constraints = (LocalRelation("zero", ("x",), ((0,),)),
                       LocalRelation("one", ("x",), ((1,),)))
        restricted = FiniteTable(("x",), ((0, 1),), ((0,),))
        self.assertEqual(minimal_unsat_core(source, constraints), ("zero", "one"))
        self.assertEqual(minimal_unsat_core(restricted, constraints), ("one",))

    def test_forgetting_a_rejection_cycles_but_monotone_search_terminates(self):
        source = FiniteTable.cartesian(("x",), ((0, 1),))
        constraints = (LocalRelation("zero", ("x",), ((0,),)),
                       LocalRelation("one", ("x",), ((1,),)))
        last_only, trace = (), []
        for _ in range(8):
            proposed = oracle(source, last_only)[0]
            trace.append(proposed[0])
            last_only = next((r,) for r in constraints if proposed not in r.allowed)
        self.assertEqual(trace, [0, 1] * 4)
        result = monotone_cegis(TypedGrammar(source, source), constraints)
        self.assertEqual(result["status"], "UNSAT_SOURCE")
        self.assertEqual(len(result["rejections"]), 2)
        self.assertEqual(result["core"], ("one", "zero"))

    def test_constraint_relaxation_changes_the_original_problem(self):
        source, constraints = triangle_problem()
        self.assertFalse(global_sections(source, constraints))
        relaxed = constraints[:2] + (LocalRelation("xz_unequal", ("x", "z"),
                                                 tuple(product((0, 1), repeat=2))),)
        self.assertEqual(global_sections(source, relaxed), ((0, 0, 0), (1, 1, 1)))
        self.assertNotEqual(constraints, relaxed)

    def test_original_static_section_does_not_license_destructive_history(self):
        source = FiniteTable.cartesian(("a", "b"), ((0, 1),) * 2)
        constraints = (LocalRelation("a_one", ("a",), ((1,),)),
                       LocalRelation("b_one", ("b",), ((1,),)))
        self.assertEqual(global_sections(source, constraints), ((1, 1),))
        lawful = []
        for original in source.rows:
            a, b = original
            first_report, current = a, (a, 0)  # reading a erases b
            second_report = current[1]
            if (first_report, second_report) == (1, 1):
                lawful.append(original)
        self.assertFalse(lawful)

    def test_typed_source_provenance_failures_reject(self):
        source = FiniteTable(("x",), ((0, 1),), ((0,),))
        invented = FiniteTable(("x",), ((0, 1),), ((1,),))
        with self.assertRaises(ValueError):
            monotone_cegis(TypedGrammar(source, invented), ())
        with self.assertRaises(ValueError):
            monotone_cegis(TypedGrammar(source, FiniteTable(("z",), ((0, 1),), ((0,),))), ())
        with self.assertRaises(ValueError):
            global_sections(source, (LocalRelation("bad", ("x",), ((2,),)),))
        with self.assertRaises(ValueError):
            global_sections(source, (LocalRelation("bad", ("missing",), ((0,),)),))
        same = LocalRelation("same", ("x",), ((0,),))
        with self.assertRaises(ValueError):
            global_sections(source, (same, same))

    def test_empty_grammar_and_empty_original_are_distinguished(self):
        source = FiniteTable.cartesian(("x",), ((0, 1),))
        empty = FiniteTable(("x",), ((0, 1),), ())
        self.assertEqual(monotone_cegis(TypedGrammar(source, empty), ())["status"], "UNSAT_GRAMMAR")
        self.assertEqual(monotone_cegis(TypedGrammar(empty, empty), ())["status"], "UNSAT_SOURCE")


if __name__ == "__main__":
    unittest.main()
