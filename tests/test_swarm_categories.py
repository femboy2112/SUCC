"""Independent word/section enumeration and hostile controls for A01--A08."""
import itertools
import unittest
from fractions import Fraction

from observational_succ.swarm_categories import (
    CategoryError, FiniteDynamics, InstrumentArrow, ReportComparison,
    belief_update, canonical_labels, compose_permutation, discrete_kan,
    directed_resource_distance, finite_relation_glue, holonomy_sections,
    inverse_permutation, map_belief, observational_ultrametric, quotient,
    refines, repair_base_change, saturated_subset, separation_depth,
    source_morphism, stable, stable_refinement,
)
from observational_succ.yoneda import (
    DivisibilityCategory, PathCategory, representable_natural_transform,
    validate_yoneda,
)


def partitions(n):
    """Independent restricted-growth enumeration of every set partition."""
    def generate(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for value in range(max(prefix, default=-1) + 2):
            yield from generate(prefix + [value])
    yield from generate([])


def word_relation(source, initial):
    """Pair-product bound, literal words; never calls partition refinement."""
    words = tuple(w for k in range(source.count ** 2 + 1)
                  for w in itertools.product(source.actions, repeat=k))
    signatures = tuple(tuple(initial[source.word_state(s, w)] for w in words)
                       for s in range(source.count))
    return tuple(signatures.index(signature) for signature in signatures)


def source(n, reports, tables):
    actions = tuple("a" + str(i) for i in range(len(tables)))
    return FiniteDynamics("complete-exact-test", reports, actions, tables, actions)


class SwarmCategoriesTests(unittest.TestCase):
    def test_unavailable_action_rejected_before_support_filter(self):
        model = source(2, (0, 1), ((0, 1),))
        for belief, report in ((frozenset(), 0), (frozenset({(0, 0)}), 1)):
            with self.assertRaisesRegex(CategoryError, "Unavailable action"):
                belief_update(model, belief, "missing", report)
        self.assertEqual(belief_update(model, frozenset(), "a0", 0), frozenset())

    def test_unary_exhaustive_coreflection_and_word_oracle(self):
        cases = 0
        all_partitions = tuple(partitions(3))
        for reports in itertools.product(range(2), repeat=3):
            for table in itertools.product(range(3), repeat=3):
                model = source(3, reports, (table,))
                repairs = {}
                for initial in all_partitions:
                    actual, steps = stable_refinement(model, initial)
                    expected = canonical_labels(word_relation(model, initial))
                    self.assertEqual(actual, expected)
                    self.assertLessEqual(steps, 3 - len(set(initial)))
                    self.assertTrue(stable(model, actual))
                    self.assertTrue(refines(actual, initial))
                    self.assertEqual(stable_refinement(model, actual)[0], actual)
                    for candidate in all_partitions:
                        if stable(model, candidate):
                            self.assertEqual(refines(candidate, initial),
                                             refines(candidate, actual))
                    repairs[initial] = actual
                    cases += 1
                for fine in all_partitions:
                    for coarse in all_partitions:
                        if refines(fine, coarse):
                            self.assertTrue(refines(repairs[fine], repairs[coarse]))
        self.assertEqual(cases, 1080)

    def test_two_action_exhaustive_oracle(self):
        cases = 0
        for reports in itertools.product(range(2), repeat=2):
            for flat in itertools.product(range(2), repeat=4):
                model = source(2, reports, (flat[:2], flat[2:]))
                for initial in partitions(2):
                    self.assertEqual(stable_refinement(model, initial)[0],
                                     canonical_labels(word_relation(model, initial)))
                    cases += 1
        self.assertEqual(cases, 128)

    def test_fibred_coreflection_nonsurjective_exhaustive_base_change(self):
        cases = 0
        for right_reports in itertools.product(range(2), repeat=3):
            for right_table in itertools.product(range(3), repeat=3):
                right = source(3, right_reports, (right_table,))
                for mapping in itertools.product(range(3), repeat=2):
                    for left_table in itertools.product(range(2), repeat=2):
                        left = source(2, tuple(right_reports[y] for y in mapping), (left_table,))
                        if source_morphism(left, right, mapping):
                            for labels in partitions(3):
                                lhs, rhs = repair_base_change(left, right, mapping, labels)
                                self.assertEqual(lhs, rhs)
                                cases += 1
        self.assertEqual(cases, 7200)

    def test_report_only_source_map_does_not_transport_repair(self):
        left = source(2, (0, 0), ((0, 1),))
        right = source(3, (0, 0, 1), ((0, 2, 2),))
        mapping = (0, 1)
        self.assertFalse(source_morphism(left, right, mapping))
        initial = tuple(right.reports[y] for y in mapping)
        left_repair = stable_refinement(left, initial)[0]
        right_repair = stable_refinement(right)[0]
        pulled_repair = tuple(right_repair[y] for y in mapping)
        self.assertNotEqual(left_repair, canonical_labels(pulled_repair))
        with self.assertRaises(CategoryError):
            repair_base_change(left, right, mapping, right.reports)

    def test_separate_universal_repairs_do_not_compose_once(self):
        reports = (0, 0, 0, 1)
        a, b = (0, 0, 3, 0), (0, 2, 0, 0)
        A = source(4, reports, (a,))
        B = source(4, reports, (b,))
        joint = source(4, reports, (a, b))
        sequential = stable_refinement(A, stable_refinement(B)[0])[0]
        self.assertEqual(sequential, (0, 0, 1, 2))
        self.assertFalse(stable(B, sequential))
        self.assertEqual(stable_refinement(joint)[0], (0, 1, 2, 3))
        self.assertEqual(joint.transcript(0, ('a1', 'a0')), (0, 0, 0))
        self.assertEqual(joint.transcript(1, ('a1', 'a0')), (0, 0, 1))

    def test_complete_source_contract_rejects_missing_actions_and_states(self):
        with self.assertRaises(CategoryError):
            FiniteDynamics("missing-action", (0, 0), ("a",), ((0, 1),), ("a", "b"))
        with self.assertRaises(CategoryError):
            FiniteDynamics("missing-state", (0, 0), ("a",), ((0,),), ("a",))
        with self.assertRaises(CategoryError):
            source(2, (0, 0), ((0, 2),))
        with self.assertRaises(CategoryError):
            source(2, (0, 0), ((0, True),))

    def test_false_quotient_dies_under_hidden_future_action(self):
        model = source(3, (0, 0, 1), ((0, 2, 2),))
        with self.assertRaises(CategoryError):
            quotient(model, (0, 0, 1))
        self.assertEqual(stable_refinement(model)[0], (0, 1, 2))
        self.assertEqual(model.transcript(0, ("a0",)), (0, 0))
        self.assertEqual(model.transcript(1, ("a0",)), (0, 1))

    def test_origin_current_belief_transport_all_subsets(self):
        model = source(3, (0, 0, 1), ((2, 2, 2), (1, 0, 2)))
        labels, _ = stable_refinement(model)
        reduced = quotient(model, labels)
        pairs = tuple(itertools.product(range(3), repeat=2))
        cases = 0
        for mask in range(1 << len(pairs)):
            belief = frozenset(p for i, p in enumerate(pairs) if mask >> i & 1)
            for action in model.actions:
                for report in (0, 1):
                    self.assertEqual(map_belief(belief_update(model, belief, action, report), labels),
                                     belief_update(reduced, map_belief(belief, labels), action, report))
                    cases += 1
        self.assertEqual(cases, 2048)

    def test_unsaturated_pullback_has_minimal_counterexample(self):
        model = source(2, (0, 0), ((0, 0),))
        labels, _ = stable_refinement(model)
        reduced = quotient(model, labels)
        target = {1}
        direct = {x for x in range(2) if model.step(x, "a0") in target}
        abstract_target = {labels[x] for x in target}
        naive = {x for x in range(2) if reduced.step(labels[x], "a0") in abstract_target}
        self.assertEqual(direct, set())
        self.assertEqual(naive, {0, 1})
        self.assertNotEqual(saturated_subset(target, labels), frozenset(target))

    def test_original_claim_not_endpoint_claim_after_reset(self):
        model = source(2, (0, 1), ((0, 0),))
        belief = frozenset(((0, 0), (1, 1)))
        zero = belief_update(model, belief, "a0", 0)
        one = belief_update(model, belief, "a0", 1)
        self.assertEqual(zero, frozenset(((0, 0),)))
        self.assertEqual(one, frozenset(((1, 0),)))
        self.assertEqual({c for _, c in zero}, {c for _, c in one})
        self.assertNotEqual({o for o, _ in zero}, {o for o, _ in one})

    def test_restricted_yoneda_fullness_and_faithfulness_are_separate(self):
        thin = DivisibilityCategory((1, 2, 3))
        report = validate_yoneda(thin, 2, 3, probes=(1,))
        self.assertEqual(report["source_hom_count"], 0)
        self.assertEqual(report["natural_transform_count"], 1)
        self.assertFalse(report["surjective"])
        paths = PathCategory((1, 2, 3, 6), (2, 3))
        parallel = paths.hom(1, 6)
        self.assertEqual(len(parallel), 2)
        hidden = [representable_natural_transform(paths, f, (6,)) for f in parallel]
        self.assertEqual(hidden[0], hidden[1])
        visible = [representable_natural_transform(paths, f, (1,)) for f in parallel]
        self.assertNotEqual(visible[0], visible[1])

    def test_pairwise_compatible_relations_need_not_glue(self):
        equality = ((0, 0), (1, 1))
        inequality = ((0, 1), (1, 0))
        local = ((('x', 'y'), equality), (('y', 'z'), equality), (('x', 'z'), inequality))
        for i, (ci, ri) in enumerate(local):
            for cj, rj in local[i + 1:]:
                overlap = tuple(v for v in ci if v in cj)
                self.assertEqual({tuple(row[ci.index(v)] for v in overlap) for row in ri},
                                 {tuple(row[cj.index(v)] for v in overlap) for row in rj})
        self.assertEqual(finite_relation_glue(('x', 'y', 'z'), (0, 1), local), ())
        positive = local[:2] + ((('x', 'z'), equality),)
        self.assertEqual(finite_relation_glue(('x', 'y', 'z'), (0, 1), positive),
                         ((0, 0, 0), (1, 1, 1)))

    def test_permutation_holonomy_against_independent_section_enumeration(self):
        perms = tuple(itertools.permutations(range(3)))
        gauges = ((1, 0, 2), (0, 2, 1), (1, 2, 0))
        for p, q, r in itertools.product(perms, repeat=3):
            edges = (('e0', 0, 1, p), ('e1', 1, 2, q), ('e2', 2, 0, r))
            verdict = holonomy_sections((0, 1, 2), edges, 3, ('e0', 'e1', 'e2'))
            brute = tuple(s for s in itertools.product(range(3), repeat=3)
                          if all(s[v] == g[s[u]] for _, u, v, g in edges))
            self.assertEqual(set(verdict['sections']), set(brute))
            changed = tuple((eid, u, v, compose_permutation(gauges[v],
                              compose_permutation(g, inverse_permutation(gauges[u]))))
                            for eid, u, v, g in edges)
            transformed = holonomy_sections((0, 1, 2), changed, 3, ('e0', 'e1', 'e2'))
            self.assertEqual(set(transformed['sections']),
                             {tuple(gauges[v][s[v]] for v in (0, 1, 2)) for s in brute})

    def test_nonabelian_holonomy_sign_and_source_coverage_mutations(self):
        cycle = (1, 2, 0)
        edges = (('loop', 0, 0, cycle),)
        verdict = holonomy_sections((0,), edges, 3, ('loop',))
        self.assertEqual(verdict['root_values'], ())
        self.assertEqual(sum(cycle[i] > cycle[j] for i in range(3) for j in range(i + 1, 3)) % 2, 0)
        with self.assertRaises(CategoryError):
            holonomy_sections((0,), (), 3, ('loop',))
        repaired = holonomy_sections((0,), (('loop', 0, 0, (0, 1, 2)),), 3, ('loop',))
        self.assertEqual(repaired['root_values'], (0, 1, 2))

    def test_discrete_kan_fiber_formulas_and_empty_context(self):
        left, right = discrete_kan((0, 0), ((10, 11), (20,)), 2)
        self.assertEqual(left, (((0, 10), (0, 11), (1, 20)), ()))
        self.assertEqual(right, (((10, 20), (11, 20)), ((),)))
        self.assertEqual(2 ** len(left[0]), (2 ** 2) * (2 ** 1))
        self.assertEqual(len(right[0]) ** 2, (2 ** 2) * (1 ** 2))
        with self.assertRaises(CategoryError):
            discrete_kan((0, 1), ((10,),), 2)

    def test_abstract_language_extension_cannot_invent_source_decoder(self):
        coarse = (0, 0)
        fine = (0, 1)
        decoders = tuple(itertools.product(range(2), repeat=1))
        self.assertFalse(any(all(d[coarse[x]] == fine[x] for x in range(2)) for d in decoders))

    def test_instrument_horizontal_vertical_interchange_and_strict_units(self):
        I = InstrumentArrow(2, 2, (1, 0), ((0,), (1,)), ((0,), (1,)), 1)
        J = InstrumentArrow(2, 2, (1, 0), ((2,),), ((2,), (2,)), 1)
        K = InstrumentArrow(2, 2, (1, 0), ((3,),), ((3,), (3,)), 1)
        p, pp = ReportComparison(I, J, (0, 0)), ReportComparison(J, K, (0,))
        self.assertEqual(p.then(pp).horizontal(p.then(pp)),
                         p.horizontal(p).then(pp.horizontal(pp)))
        self.assertEqual(I.then(J).then(K), I.then(J.then(K)))
        self.assertEqual(InstrumentArrow.identity(2).then(I), I)
        self.assertEqual(I.then(InstrumentArrow.identity(2)), I)
        self.assertEqual(I.then(I).reports, ((0, 1), (1, 0)))
        with self.assertRaises(CategoryError):
            ReportComparison(I, InstrumentArrow.identity(2), (0, 0))

    def test_same_endpoint_histories_can_have_different_reports(self):
        A = InstrumentArrow(2, 2, (0, 0), ((0,), (1,)), ((0,), (1,)), 1)
        B = InstrumentArrow(2, 2, (0, 0), ((2,),), ((2,), (2,)), 1)
        self.assertEqual(A.then(B).transition, B.then(A).transition)
        self.assertNotEqual(A.then(B).reports, B.then(A).reports)

    def test_raw_separation_cost_fails_triangle_but_ultrametric_survives(self):
        model = source(5, (0, 0, 1, 0, 0), ((0, 3, 2, 4, 2),))
        self.assertEqual(separation_depth(model, 0, 1), 4)
        self.assertEqual(separation_depth(model, 0, 2), 1)
        self.assertEqual(separation_depth(model, 1, 2), 1)
        self.assertGreater(4, 1 + 1)
        for x, y, z in itertools.product(range(5), repeat=3):
            self.assertLessEqual(observational_ultrametric(model, x, z),
                                 max(observational_ultrametric(model, x, y),
                                     observational_ultrametric(model, y, z)))
        self.assertEqual(observational_ultrametric(model, 0, 0), 0)

    def test_free_resource_geometry_exact_triangle_and_negative_cost_gate(self):
        d = directed_resource_distance(3, ((0, 1, Fraction(1, 3)), (1, 2, Fraction(2, 3)), (0, 2, 5)))
        self.assertEqual(d[0][2], 1)
        self.assertIsNone(d[2][0])
        for x, y, z in itertools.product(range(3), repeat=3):
            if d[x][y] is not None and d[y][z] is not None:
                self.assertIsNotNone(d[x][z])
                self.assertLessEqual(d[x][z], d[x][y] + d[y][z])
        with self.assertRaises(CategoryError):
            directed_resource_distance(2, ((0, 1, -1),))
        with self.assertRaises(CategoryError):
            directed_resource_distance(2, ((0, 1, 0.5),))


if __name__ == '__main__':
    unittest.main()
