"""Quantale-weighted ancestral quotients (OPUS II, CG-1 ... CG-13).

Positive controls, hostile mutations, exhaustive small-model enumeration and
pinned holdout receipts.  Independent oracles: path enumeration without
distributivity (path_sum_oracle), brute-force predicate enumeration, and the
existing Boolean audit in ancestral_observer.py (PAP-01..PAP-05).  Passing is
finite validation, not proof; proofs are in the OPUS_II report.
"""
import math
import random
import unittest
from fractions import Fraction as Fr
from itertools import product

from observational_succ.ancestral_observer import audit_ancestral_observer
from observational_succ.future_safe_quotient import Edge, Machine, State
from observational_succ.observatoris_quantale_quotient import (
    INF, OVERFLOW, QuantaleError, TropicalQuantale, ViterbiQuantale, aggregated_response,
    all_predicates, backward_must_quotient, base_change, boolean, bottleneck_chain,
    check_weighted_ghost, closed_predicates, closure, coarsest_exact_refinement,
    cyclic_monoid, evaluate_polynomial, exists_quotient, finite_support_hom,
    forall_quotient, hereditary_meet, hom_failures, is_closed, is_closed_wrong_side,
    is_exact_partition, left_zero_monoid, lumped_matrix, m3_lattice_monoid, mat_pow,
    mean_quotient, min_length_hom, model, partition_join, partition_meet,
    path_sum_oracle, predicate_closure, pull, push, push_forall, refines, residuated_meet,
    resolvent,
    restricted_growth, saturating_tropical, signed_lumpable, structural_walks, supp,
    truncated_free_monoid, truncated_tropical, walk_polynomial,
)

T, F = True, False
E = frozenset()


def all_relations(V, n, values=None):
    vals = V.elements() if values is None else values
    for vs in product(vals, repeat=n * n):
        yield tuple(tuple(vs[i * n:(i + 1) * n]) for i in range(n))


def bool_rel(n, edges):
    return tuple(tuple((i, j) in edges for j in range(n)) for i in range(n))


def trop_rel(n, weighted):
    R = [[INF] * n for _ in range(n)]
    for (i, j), w in weighted.items():
        R[i][j] = w
    return tuple(tuple(r) for r in R)


def quotient_path(lab, a, b):
    """Breadth-first quotient path a -> b through non-bottom Q edges (test helper)."""
    prev, frontier = {a: None}, [a]
    while frontier:
        nxt = []
        for c in frontier:
            for d in range(lab.m):
                if lab.Q[c][d] != lab.V.bottom and d not in prev:
                    prev[d] = c
                    nxt.append(d)
        frontier = nxt
    path = [b]
    while prev[path[-1]] is not None:
        path.append(prev[path[-1]])
    return tuple(reversed(path))


def vleq_rows(V, *rows):
    return all(all(V.leq(a, b) for a, b in zip(r, s)) for r, s in zip(rows, rows[1:]))


def theorem_battery(test, lab, preds):
    """Every CG statement on one finite model; returns (exact, lumpable, may*=must*,
    unpointed, fully_faithful, backward_exact)."""
    V, n, q = lab.V, lab.n, lab.q
    im = set(q)
    # CG-1: Kleene closure = distributivity-free path oracle = hereditary meets.
    test.assertEqual(path_sum_oracle(V, lab.R), lab.Rs)
    test.assertEqual(path_sum_oracle(V, lab.Q), lab.Qs)
    for x in range(n):
        test.assertTrue(is_closed(V, lab.R, lab.Rs[x]))
        for z in range(n):
            test.assertEqual(hereditary_meet(V, lab.R, x, z, preds), lab.Rs[x][z])
            test.assertEqual(residuated_meet(V, lab.R, x, z, preds), lab.Rs[x][z])
            # CG-2: projection soundness.
            test.assertTrue(V.leq(lab.Rs[x][z], lab.Qs[q[x]][q[z]]))
    # CG-3: (1) <=> (2) <=> (3) <=> (4) <=> (5) <=> (6) <=> left Beck-Chevalley.
    c1 = lab.cond1_all_start()
    MA = forall_quotient(V, lab.Rs, q, lab.m)
    c5 = all(V.leq(lab.Q[a][b], MA[a][b]) for a in im for b in range(lab.m))
    c6 = all(MA[a] == lab.may_profile()[a] for a in im)
    test.assertEqual(
        {c1, lab.cond2_fibre_constant(), lab.cond3_push_preserves_closed(preds),
         lab.cond4_saturation_preserves_closed(preds), c5, c6, lab.left_bc(preds)}, {c1})
    test.assertEqual(MA, lab.must_profile())
    for x in range(n):
        # CG-4: selected-start criterion.
        se = lab.selected_exact(x)
        test.assertEqual(se, lab.selected_criterion(x))
        test.assertEqual(se, lab.selected_saturation_criterion(x))
        # CG-7 sandwich; CG-9 ghost defect at rho_x.
        test.assertTrue(vleq_rows(V, *lab.sandwich(x)))
        test.assertEqual(lab.left_adjoint(lab.Rs[x]), lab.Qs[q[x]])
        test.assertEqual(se, not lab.ghost_reports(x))
    M, S = lab.must_profile(), lab.may_profile()
    for a in im:
        test.assertTrue(vleq_rows(V, lab.QAs[a], M[a], S[a], lab.Qs[a]))
    lump, mm = lab.lumpable(), lab.may_equals_must_on_image()
    unp, ff = lab.unpointed_exact(), lab.fully_faithful()
    if lump:
        test.assertTrue(mm)
    if mm:
        test.assertTrue(c1)
    if c1:
        test.assertTrue(unp)
    # CG-12: whole distance <=> kernel within isomorphism; it implies exactness.
    test.assertEqual(ff, lab.kernel_within_isomorphism())
    if ff:
        test.assertTrue(c1)
    # Unpointed exactness <=> q_!R* transitive on the image.
    trans = all(V.leq(V.tensor(S[a][b], S[b][c]), S[a][c]) for a in im for b in im for c in im)
    test.assertEqual(unp, trans)
    # CG-8: right Beck-Chevalley <=> backward exactness <=> backward coverage.
    bwd = lab.backward_exact()
    test.assertEqual({lab.right_bc(preds), bwd, lab.backward_coverage()}, {bwd})
    QB = backward_must_quotient(V, lab.R, q, lab.m)
    for phi in preds:
        pushed = push(V, phi, q, lab.m)
        test.assertTrue(is_closed(V, lab.QA, pushed))                        # q_! -> must
        test.assertTrue(is_closed(V, QB, push_forall(V, phi, q, lab.m)))     # q_* -> back-must
        test.assertEqual(lab.defect_is_zero(phi), is_closed(V, lab.Q, pushed))
        test.assertTrue(is_closed(V, lab.Q, lab.left_adjoint(phi)))
        test.assertTrue(is_closed(V, lab.Q, lab.right_adjoint(phi)))
    return c1, lump, mm, unp, ff, bwd


class TestQuantaleStructures(unittest.TestCase):
    def test_instances_are_quantales_and_mutation_is_not(self):
        for V in (boolean(), truncated_tropical(3), saturating_tropical(3),
                  bottleneck_chain(4), cyclic_monoid(2), cyclic_monoid(3),
                  left_zero_monoid()):
            self.assertEqual(V.axiom_failures(), [], V.name)
        self.assertFalse(left_zero_monoid().is_commutative())
        bad = m3_lattice_monoid().axiom_failures()
        self.assertTrue(any("distributivity" in b for b in bad))
        self.assertFalse(any("associativity" in b or "unit" in b for b in bad))

    def test_residuals_are_adjoints_exhaustively(self):
        for V in (boolean(), truncated_tropical(3), bottleneck_chain(3), left_zero_monoid()):
            el = V.elements()
            for a, b, c in product(el, repeat=3):
                t = V.leq(V.tensor(a, b), c)
                self.assertEqual(t, V.leq(b, V.ldiv(a, c)))
                self.assertEqual(t, V.leq(a, V.rdiv(c, b)))

    def test_language_quantale_records_ordered_traces(self):
        L = truncated_free_monoid("xy", 2)
        self.assertEqual(len(L.monoid), 8)
        x, y = frozenset({"x"}), frozenset({"y"})
        self.assertEqual(L.tensor(x, y), frozenset({"xy"}))
        self.assertEqual(L.tensor(L.tensor(x, y), x), frozenset({OVERFLOW}))


class TestCG1HereditaryCharacterisation(unittest.TestCase):
    def test_weighted_hereditary_meet_exhaustive_small(self):
        cases = 0
        for V, n in ((boolean(), 3), (truncated_tropical(2), 2), (bottleneck_chain(3), 2),
                     (cyclic_monoid(3), 2), (left_zero_monoid(), 2)):
            for k in range(1, n + 1):
                for R in all_relations(V, k):
                    preds = closed_predicates(V, R)
                    Rs = closure(V, R)
                    self.assertEqual(path_sum_oracle(V, R), Rs)
                    for x, z in product(range(k), repeat=2):
                        self.assertEqual(hereditary_meet(V, R, x, z, preds), Rs[x][z])
                        self.assertEqual(residuated_meet(V, R, x, z, preds), Rs[x][z])
                    cases += 1
        self.assertEqual(cases, 2 + 16 + 512 + 4 + 256 + 3 + 81 + 8 + 4096 + 8 + 4096)

    def test_shortest_path_potential_duality_exact_rationals(self):
        V = TropicalQuantale()
        rng = random.Random(20261114)
        for _ in range(60):
            n = 5
            R = tuple(tuple(Fr(rng.randint(1, 9), rng.randint(1, 3)) if rng.random() < 0.4
                            else INF for _ in range(n)) for _ in range(n))
            Rs = closure(V, R)
            self.assertEqual(path_sum_oracle(V, R), Rs)
            for x in range(n):
                self.assertTrue(is_closed(V, R, Rs[x]))       # d(x,.) is feasible
                self.assertEqual(Rs[x][x], 0)                  # and normalised
                for _ in range(5):                             # random feasible potentials
                    seed = [Fr(rng.randint(0, 5)) for _ in range(n)]
                    seed[x] = Fr(0)
                    pot = predicate_closure(V, Rs, seed)
                    self.assertTrue(is_closed(V, R, pot) and pot[x] == 0)
                    for z in range(n):                         # numerically pot(z) <= d(x,z)
                        self.assertTrue(V.leq(Rs[x][z], pot[z]))

    def test_viterbi_relevance_exact_rationals(self):
        V = ViterbiQuantale()
        rng = random.Random(7)
        for _ in range(60):
            n = 5
            R = tuple(tuple(Fr(rng.randint(1, 4), 4) if rng.random() < 0.4 else Fr(0)
                            for _ in range(n)) for _ in range(n))
            Rs = closure(V, R)
            self.assertEqual(path_sum_oracle(V, R), Rs)
            for x in range(n):
                self.assertTrue(is_closed(V, R, Rs[x]))
                for z in range(n):
                    phi = Rs[x]
                    self.assertEqual(V.ldiv(phi[x], phi[z]), Rs[x][z])

    def test_mutation_wrong_side_closedness_computes_reversed_trace(self):
        V = left_zero_monoid()
        a, b = frozenset({"a"}), frozenset({"b"})
        R = ((E, a, E), (E, E, b), (E, E, E))
        self.assertEqual(closure(V, R)[0][2], a)               # path order: a.b = a
        right = closed_predicates(V, R)
        wrong = [p for p in all_predicates(V, 3) if is_closed_wrong_side(V, R, p)]
        self.assertEqual(hereditary_meet(V, R, 0, 2, right), a)
        self.assertEqual(hereditary_meet(V, R, 0, 2, wrong), b)   # reversed: b.a = b
        self.assertEqual(residuated_meet(V, R, 0, 2, right), a)
        self.assertEqual(V.meet(V.rdiv(p[2], p[0]) for p in right), E)  # wrong residual

    def test_mutation_non_distributive_lattice_monoid_breaks_cg1_and_cg3(self):
        V = m3_lattice_monoid()
        O = "0"
        R = ((O, "1", "a", O), (O, O, "b", O), (O, O, O, "c"), (O, O, O, O))
        self.assertEqual(path_sum_oracle(V, R)[0][3], "0")     # (a^c) v (b^c) = 0
        self.assertEqual(hereditary_meet(V, R, 0, 3), "c")     # (a v b) ^ c = c
        self.assertEqual(closure(V, R)[0][3], "c")             # Kleene != path sum
        self.assertFalse(is_closed(V, R, path_sum_oracle(V, R)[0]))
        R3 = (("c", "1", "c"), ("0", "1", "0"), ("a", "c", "0"))
        lab = model(V, R3, (0, 1, 0))
        preds = closed_predicates(V, R3)
        self.assertTrue(lab.cond1_all_start() and lab.cond2_fibre_constant())
        self.assertFalse(lab.cond3_push_preserves_closed(preds))
        self.assertFalse(lab.cond4_saturation_preserves_closed(preds))


class TestCG3ExactnessExhaustive(unittest.TestCase):
    def test_boolean_2594_models_reproduce_pap_and_every_cg_statement(self):
        B = boolean()
        cases, kinds = 0, set()
        for n in range(1, 4):
            for R in all_relations(B, n):
                preds = closed_predicates(B, R)
                edges = tuple((i, j) for i in range(n) for j in range(n) if R[i][j])
                machine = Machine(tuple(State(str(i), "declared-source", "") for i in range(n)),
                                  tuple(str(i) for i in range(n)),
                                  tuple(Edge(str(i), str(j), str(j), Fr(0)) for i, j in edges))
                for q in restricted_growth(n):
                    lab = model(B, R, q)
                    kinds.add(theorem_battery(self, lab, preds))
                    labels = tuple(str(v) for v in q)
                    for x in range(n):
                        audit = audit_ancestral_observer(machine, labels, str(x))
                        self.assertEqual(audit.endpoint_exact, lab.selected_exact(x))
                        self.assertEqual(set(audit.ghost_reports),
                                         {str(b) for b in lab.ghost_reports(x)})
                    cases += 1
        self.assertEqual(cases, 2594)
        # Every implication in the chain is realised strictly somewhere.
        self.assertIn((T, F, T, T, F, T), kinds)   # may*=must* without lumpability
        self.assertIn((T, F, F, T, F, T), kinds)   # exact without may*=must*
        self.assertIn((F, F, F, T, F, T), kinds)   # unpointed without exact
        self.assertIn((T, F, T, T, F, F), kinds)   # forward exact, not backward
        self.assertTrue(any(k[0] is F and k[5] is T for k in kinds))  # backward, not forward

    def test_weighted_two_state_models_exhaustive(self):
        count = 0
        for V in (truncated_tropical(2), saturating_tropical(2), bottleneck_chain(3),
                  cyclic_monoid(2), cyclic_monoid(3), left_zero_monoid()):
            for n in (1, 2):
                for R in all_relations(V, n):
                    preds = closed_predicates(V, R)
                    for q in restricted_growth(n):
                        exact = theorem_battery(self, model(V, R, q), preds)[0]
                        if V.integral:      # integral V: two states never suffice for a ghost
                            self.assertTrue(exact)
                        count += 1
        # |V| + 2|V|^4 per quantale: 516 (x3 four-element), 165, 8200 (x2 eight-element).
        self.assertEqual(count, 3 * 516 + 165 + 2 * 8200)

    def test_three_state_weighted_random_sample(self):
        rng = random.Random(1114)
        for V, samples in ((truncated_tropical(2), 120), (bottleneck_chain(3), 120),
                           (cyclic_monoid(3), 40), (left_zero_monoid(), 40)):
            el = V.elements()
            for _ in range(samples):
                R = tuple(tuple(rng.choice(el) if rng.random() < 0.6 else V.bottom
                                for _ in range(3)) for _ in range(3))
                preds = closed_predicates(V, R)
                for q in restricted_growth(3):
                    theorem_battery(self, model(V, R, q), preds)

    def test_two_state_ghost_needs_a_non_integral_quantale(self):
        V = cyclic_monoid(2)                           # parity of path length
        one = frozenset({1})
        lab = model(V, ((E, one), (E, E)), (0, 0))
        self.assertFalse(lab.selected_exact(1))        # quotient invents odd loops at y
        self.assertEqual(lab.profiles[1], (frozenset({0}),))
        self.assertEqual(lab.Qs[0], (frozenset({0, 1}),))
        self.assertTrue(lab.selected_exact(0))


class TestCG5BaseChange(unittest.TestCase):
    def setUp(self):
        self.L = truncated_free_monoid("xy", 2)
        self.S = saturating_tropical(3)
        self.B = boolean()
        self.len = min_length_hom(2)

    def test_language_cost_boolean_is_a_chain_of_strict_homomorphisms(self):
        self.assertTrue(hom_failures(self.L, self.S, self.len)["strict"])
        self.assertTrue(hom_failures(self.S, self.B, finite_support_hom)["strict"])
        budget = hom_failures(truncated_tropical(3), self.B, finite_support_hom)
        self.assertTrue(budget["oplax"] and not budget["strict"] and not budget["lax"])

    def test_strict_transport_and_commutation_random(self):
        rng = random.Random(42)
        letters = (E, frozenset({"x"}), frozenset({"y"}), frozenset({"x", "y"}))
        for _ in range(150):
            n = rng.choice((3, 4))
            R = tuple(tuple(rng.choice(letters) if rng.random() < 0.5 else E
                            for _ in range(n)) for _ in range(n))
            for q in ((0,) * n, tuple(rng.randrange(2) for _ in range(n)),
                      tuple(rng.randrange(3) for _ in range(n))):
                m = max(q) + 1
                lang = model(self.L, R, q, m)
                cost = model(self.S, base_change(self.len, R), q, m)
                bool_ = model(self.B, base_change(finite_support_hom, cost.R), q, m)
                self.assertEqual(base_change(self.len, lang.Rs), cost.Rs)   # h(R*) = (hR)*
                self.assertEqual(base_change(self.len, lang.Qs), cost.Qs)
                for x in range(n):
                    if lang.selected_exact(x):
                        self.assertTrue(cost.selected_exact(x))
                    if cost.selected_exact(x):
                        self.assertTrue(bool_.selected_exact(x))
                # Graded instance: letter-valued language exactness == lumpability.
                self.assertEqual(lang.cond1_all_start(), lang.lumpable())

    def test_hierarchy_strictness_witnesses(self):
        chain = trop_rel(3, {(0, 1): 1, (1, 2): 1})
        cost = model(self.S, chain, (0, 0, 1))
        self.assertTrue(model(self.B, base_change(finite_support_hom, chain), (0, 0, 1))
                        .cond1_all_start())
        self.assertFalse(cost.selected_exact(0))
        self.assertEqual((cost.profiles[0][1], cost.Qs[0][1]), (2, 1))   # shortcut 2 -> 1
        x, y = frozenset({"x"}), frozenset({"y"})
        lang = model(self.L, ((E, E, x), (E, E, y), (E, E, E)), (0, 0, 1))
        self.assertTrue(model(self.S, base_change(self.len, lang.R), (0, 0, 1)).cond1_all_start())
        self.assertFalse(lang.selected_exact(0))
        self.assertEqual(lang.ghost_defect(lang.Rs[0])[1][1], frozenset({"x", "y"}))
        self.assertEqual(lang.profiles[0][1], x)

    def test_lax_maps_do_not_transport_exactness(self):
        B, Z2 = boolean(), cyclic_monoid(2)
        top = lambda a: frozenset({0, 1}) if a else E
        f = hom_failures(B, Z2, top)
        self.assertTrue(f["lax"] and not f["strict"])
        R = ((F, F), (F, T))
        self.assertTrue(model(B, R, (0, 0)).cond1_all_start())
        self.assertFalse(model(Z2, base_change(top, R), (0, 0)).cond1_all_start())
        # Strict unit and strict joins do not rescue a lax tensor.
        even = lambda A: 0 in A
        f = hom_failures(Z2, B, even)
        self.assertTrue(f["lax"] and not f["strict"])
        R = ((E, E, E), (E, E, frozenset({1})), (frozenset({0}), E, frozenset({1})))
        self.assertTrue(model(Z2, R, (0, 1, 1)).cond1_all_start())
        self.assertFalse(model(B, base_change(even, R), (0, 1, 1)).cond1_all_start())

    def test_oplax_maps_transport_all_start_but_not_selected_start(self):
        T3 = truncated_tropical(3)
        rng = random.Random(3)
        maps = ((T3, T3, lambda a: INF if a == INF else a // 2),
                (T3, boolean(), lambda a: a <= 1),
                (T3, boolean(), finite_support_hom))
        for V, W, h in maps:
            f = hom_failures(V, W, h)
            self.assertTrue(f["oplax"] and not f["strict"])
            rels = list(all_relations(V, 2)) + [
                tuple(tuple(rng.choice(V.elements()) for _ in range(3)) for _ in range(3))
                for _ in range(400)]
            for R in rels:
                for q in restricted_growth(len(R)):
                    lab, labW = model(V, R, q), model(W, base_change(h, R), q)
                    if lab.cond1_all_start():
                        self.assertTrue(labW.cond1_all_start())
                    for x in range(len(R)):    # hereditary selected exactness transports
                        if all(lab.selected_exact(z) for z in lab.support_reachable(x)):
                            self.assertTrue(labW.selected_exact(x))
        half = maps[0][2]
        R = trop_rel(4, {(0, 1): 1, (0, 3): 2, (2, 3): 1})
        q = (0, 1, 1, 2)
        self.assertTrue(model(T3, R, q).selected_exact(0))
        self.assertFalse(model(T3, base_change(half, R), q).selected_exact(0))


class TestCG7MayMustSandwich(unittest.TestCase):
    def test_both_inequalities_strict_at_one_start(self):
        S = saturating_tropical(3)
        lab = model(S, trop_rel(4, {(0, 3): 2, (1, 3): 1}), (0, 0, 0, 1))
        lower, source, upper = (row[1] for row in lab.sandwich(0))
        self.assertEqual((lower, source, upper), (INF, 2, 1))   # d_must >= d_src >= d_may

    def test_refined_chain_each_link_strict(self):
        B = boolean()
        chain = model(B, bool_rel(3, {(0, 1), (1, 2)}), (0, 0, 1))
        self.assertEqual((chain.QAs[0][1], chain.must_profile()[0][1]), (F, T))
        ghost = model(B, bool_rel(3, {(1, 2)}), (0, 0, 1))
        self.assertEqual((ghost.must_profile()[0][1], ghost.may_profile()[0][1]), (F, T))
        split = model(B, bool_rel(4, {(0, 1), (2, 3)}), (0, 1, 1, 2))
        self.assertEqual((split.may_profile()[0][2], split.Qs[0][2]), (F, T))
        self.assertFalse(split.unpointed_exact())

    def test_hierarchy_witnesses(self):
        B = boolean()
        one_fibre = model(B, bool_rel(2, {(0, 1)}), (0, 0))
        self.assertTrue(one_fibre.may_equals_must_on_image() and not one_fibre.lumpable())
        chain = model(B, bool_rel(3, {(0, 1), (1, 2)}), (0, 0, 1))
        self.assertTrue(chain.cond1_all_start() and not chain.may_equals_must_on_image())
        ghost = model(B, bool_rel(3, {(1, 2)}), (0, 0, 1))
        self.assertTrue(ghost.unpointed_exact() and not ghost.cond1_all_start())

    def test_source_value_is_not_a_function_of_may_and_must_closures(self):
        B = boolean()
        ghost = model(B, bool_rel(3, {(1, 2), (1, 0)}), (0, 0, 1))
        fed = model(B, bool_rel(3, {(0, 1), (1, 2)}), (0, 0, 1))
        self.assertEqual((ghost.Q, ghost.QA, ghost.Qs, ghost.QAs),
                         (fed.Q, fed.QA, fed.Qs, fed.QAs))
        self.assertNotEqual(ghost.profiles[0], fed.profiles[0])

    def test_coarsest_exact_refinement_computes_true_source_values(self):
        rng = random.Random(77)
        for V in (boolean(), truncated_tropical(3), cyclic_monoid(3)):
            el = V.elements()
            for _ in range(40):
                n = 4
                R = tuple(tuple(rng.choice(el) if rng.random() < 0.35 else V.bottom
                                for _ in range(n)) for _ in range(n))
                q = tuple(rng.randrange(2) for _ in range(n))
                q = tuple(a if a in q else 0 for a in q)
                fine = coarsest_exact_refinement(V, R, q)
                lab = model(V, R, q, max(q) + 1)
                labf = model(V, R, fine)
                self.assertTrue(labf.cond1_all_start())
                for x in range(n):
                    for b in range(lab.m):
                        blocks = {fine[z] for z in range(n) if q[z] == b}
                        self.assertEqual(lab.profiles[x][b],
                                         V.join(labf.Qs[fine[x]][c] for c in blocks))

    def test_off_image_reports_and_empty_fibres_are_harmless(self):
        B = boolean()
        lab = model(B, bool_rel(3, {(1, 2)}), (0, 0, 2), m=4)    # reports 1, 3 unused
        self.assertEqual(lab.QA[1], (T, T, T, T))                # empty-fibre row is top
        for x in range(3):
            self.assertTrue(vleq_rows(B, *lab.sandwich(x)))
            self.assertFalse(lab.Qs[lab.q[x]][1] or lab.Qs[lab.q[x]][3])


class TestCG8AdjunctionsAndBeckChevalley(unittest.TestCase):
    def test_adjunction_laws_exhaustive_boolean_and_noncommutative(self):
        for V, n in ((boolean(), 3), (left_zero_monoid(), 2)):
            for R in all_relations(V, n):
                preds = closed_predicates(V, R)
                for q in restricted_growth(n):
                    lab = model(V, R, q)
                    clQ = closed_predicates(V, lab.Q)
                    for psi in all_predicates(V, lab.m):     # q^* preserves AND reflects
                        self.assertEqual(is_closed(V, lab.Q, psi),
                                         is_closed(V, lab.R, pull(psi, q)))
                    for phi in preds[:12]:
                        Lp, Rp = lab.left_adjoint(phi), lab.right_adjoint(phi)
                        for psi in clQ[:12]:
                            self.assertEqual(vleq_rows(V, Lp, psi), vleq_rows(V, phi, pull(psi, q)))
                            self.assertEqual(vleq_rows(V, pull(psi, q), phi), vleq_rows(V, psi, Rp))
                    for psi in clQ:                          # counit: L q^* psi = psi on image
                        counit = lab.left_adjoint(pull(psi, q))
                        self.assertEqual(counit, tuple(psi[b] if b in set(q) else V.bottom
                                                       for b in range(lab.m)))
                    # Cl(R) is closed under binary joins and meets.
                    for p1, p2 in zip(preds, preds[1:6]):
                        self.assertTrue(is_closed(V, R, tuple(map(V.join2, p1, p2))))
                        self.assertTrue(is_closed(V, R, tuple(map(V.meet2, p1, p2))))

    def test_q_lower_star_pairs_with_backward_not_forward_must(self):
        B = boolean()
        lab = model(B, bool_rel(3, {(0, 2)}), (0, 1, 1))     # u=0 -> v1=2; v0=1 idle
        phi = (T, F, T)
        self.assertTrue(is_closed(B, lab.R, phi))
        star = push_forall(B, phi, lab.q, lab.m)
        self.assertEqual(star, (T, F))
        self.assertFalse(is_closed(B, lab.QA, star))           # forward must: fails
        self.assertTrue(is_closed(B, backward_must_quotient(B, lab.R, lab.q, lab.m), star))

    def test_forward_and_backward_exactness_are_time_reverses(self):
        B = boolean()
        ghost = model(B, bool_rel(3, {(1, 2)}), (0, 0, 1))
        rev = model(B, bool_rel(3, {(2, 1)}), (0, 0, 1))
        self.assertEqual((ghost.cond1_all_start(), ghost.backward_exact()), (F, T))
        self.assertEqual((rev.cond1_all_start(), rev.backward_exact()), (T, F))
        self.assertFalse(rev.right_bc())


class TestCG9GhostDefect(unittest.TestCase):
    def test_tropical_defect_is_the_shortcut_amount(self):
        S = saturating_tropical(3)
        lab = model(S, trop_rel(3, {(0, 1): 1, (1, 2): 1}), (0, 0, 1))
        pushed, lifted, defect = lab.ghost_defect(lab.Rs[0])
        self.assertEqual((pushed[1], lifted[1], defect[1]), (2, 1, 1))
        self.assertEqual(lab.ghost_reports(0), (1,))
        self.assertEqual(lab.ghost_reports(1), ())
        self.assertEqual(lab.global_defect(), 1)              # worst shortcut, not 0 = k
        lab2 = model(S, trop_rel(3, {(0, 2): 3, (1, 2): 1}), (0, 0, 1))
        self.assertEqual(lab2.global_defect(), 2)             # 3 - 1
        self.assertEqual(model(S, trop_rel(3, {(0, 1): 1}), (0, 1, 1)).global_defect(), 0)

    def test_global_defect_zero_iff_exact_exhaustive(self):
        for V, n in ((boolean(), 3), (truncated_tropical(2), 2), (left_zero_monoid(), 2)):
            for R in all_relations(V, n):
                for q in restricted_growth(n):
                    lab = model(V, R, q)
                    self.assertEqual(V.leq(V.unit, lab.global_defect()), lab.cond1_all_start())

    def test_boolean_defect_lists_invented_endpoints(self):
        B = boolean()
        lab = model(B, bool_rel(3, {(1, 2)}), (0, 0, 1))
        self.assertEqual(lab.ghost_defect(lab.Rs[0])[2], (T, F))
        self.assertEqual(lab.ghost_reports(0), (1,))


class TestCG10CoarsestExactRefinement(unittest.TestCase):
    def test_join_closure_and_coarsest_refinement_exhaustive(self):
        B = boolean()
        meet_failures = 0
        for n in (1, 2, 3):
            parts = list(restricted_growth(n))
            for R in all_relations(B, n):
                Rs = closure(B, R)
                exact = {p for p in parts if is_exact_partition(B, Rs, p)}
                self.assertIn(tuple(range(n)), exact)
                for p in exact:
                    for r in exact:
                        self.assertIn(partition_join(p, r), exact)
                        meet_failures += partition_meet(p, r) not in exact
                for q in parts:
                    c = coarsest_exact_refinement(B, R, q)
                    self.assertIn(c, exact)
                    self.assertTrue(refines(c, q))
                    self.assertTrue(all(refines(p, c) for p in exact if refines(p, q)))
        self.assertEqual(meet_failures, 0)   # meets fail only from four states on

    def test_weighted_coarsest_refinement_random(self):
        V = truncated_tropical(3)
        rng = random.Random(9)
        parts = list(restricted_growth(4))
        for _ in range(60):
            R = tuple(tuple(rng.choice((1, 2, INF, INF)) for _ in range(4)) for _ in range(4))
            Rs = closure(V, R)
            exact = {p for p in parts if is_exact_partition(V, Rs, p)}
            for q in parts[::3]:
                c = coarsest_exact_refinement(V, R, q)
                self.assertIn(c, exact)
                self.assertTrue(all(refines(p, c) for p in exact if refines(p, q)))

    def test_meet_of_exact_partitions_can_fail(self):
        B = boolean()
        R = bool_rel(4, {(0, 0), (0, 3), (1, 0), (1, 2), (2, 3), (3, 0)})
        Rs = closure(B, R)
        p, r = (0, 0, 0, 1), (0, 0, 1, 1)
        self.assertTrue(is_exact_partition(B, Rs, p) and is_exact_partition(B, Rs, r))
        self.assertFalse(is_exact_partition(B, Rs, partition_meet(p, r)))

    def test_selected_start_exact_partitions_have_no_canonical_coarsest(self):
        B = boolean()
        R = bool_rel(4, {(2, 0), (2, 1), (3, 0)})
        p, r = (0, 1, 2, 0), (0, 1, 2, 2)
        self.assertTrue(model(B, R, p).selected_exact(0))
        self.assertTrue(model(B, R, r).selected_exact(0))
        self.assertFalse(model(B, R, partition_join(p, r)).selected_exact(0))


class TestCG11WeightedGhostCertificate(unittest.TestCase):
    def setUp(self):
        self.V = saturating_tropical(3)
        self.R = trop_rel(3, {(0, 1): 1, (1, 2): 1})
        self.q = (0, 0, 1)

    def test_certificate_accepted(self):
        cert = check_weighted_ghost(self.V, self.R, self.q, 2, 0, (0, 1), (0, 1, 2))
        self.assertEqual((cert.path_weight, cert.bound), (1, 2))

    def test_hostile_certificates_rejected(self):
        bad = (((0, 1), (0, 1, 1)),      # bound 1 does not separate
               ((0, 1), (0, 0, 2)),      # not closed: 1 -> 2 escapes
               ((0, 1), (1, 1, 2)),      # root not contained (k = 0 not <= 1)
               ((1,), (0, 1, 2)),        # path does not start at q(x)
               ((), (0, 1, 2)))
        for path, inv in bad:
            with self.assertRaises(QuantaleError):
                check_weighted_ghost(self.V, self.R, self.q, 2, 0, path, inv)

    def test_certificate_complete_on_exhaustive_boolean(self):
        B = boolean()
        for R in all_relations(B, 3):
            for q in restricted_growth(3):
                lab = model(B, R, q)
                for x in range(3):
                    for b in lab.ghost_reports(x):
                        path = quotient_path(lab, q[x], b)
                        cert = check_weighted_ghost(B, R, q, lab.m, x, path, lab.Rs[x])
                        self.assertFalse(cert.bound)


class TestCG12WholeDistance(unittest.TestCase):
    def test_full_faithfulness_and_lumpability_are_incomparable(self):
        B = boolean()
        ff = model(B, bool_rel(3, {(0, 1), (1, 0), (0, 2)}), (0, 0, 1))
        self.assertTrue(ff.fully_faithful() and not ff.lumpable() and ff.cond1_all_start())
        lump = model(B, bool_rel(2, set()), (0, 0))
        self.assertTrue(lump.lumpable() and not lump.fully_faithful())


class TestCG13SignedWeights(unittest.TestCase):
    def test_support_is_lax_on_sums_and_strict_on_products(self):
        vals = [Fr(v) for v in (-2, -1, 0, 1, 2)]
        for a, b in product(vals, repeat=2):
            self.assertEqual(supp(a * b), supp(a) and supp(b))
            self.assertTrue(not supp(a + b) or supp(a) or supp(b))
            if a >= 0 and b >= 0:
                self.assertEqual(supp(a + b), supp(a) or supp(b))
        self.assertFalse(supp(Fr(1) + Fr(-1)))

    def test_net_support_below_structure_with_equality_for_nonnegative(self):
        for n, vals in ((2, (-1, 0, 1)), (3, (-1, 0, 1))):
            for vs in product(vals, repeat=n * n):
                A = tuple(tuple(Fr(vs[i * n + j]) for j in range(n)) for i in range(n))
                nonneg = all(v >= 0 for v in vs)
                for t in (1, 2, 3):
                    P, W = mat_pow(A, t), structural_walks(A, t)
                    for y, x in product(range(n), repeat=2):
                        self.assertTrue(not supp(P[y][x]) or W[y][x])
                        if nonneg:
                            self.assertEqual(supp(P[y][x]), W[y][x])

    def test_minimal_cancellation_two_states(self):
        A = ((Fr(1), Fr(0)), (Fr(1), Fr(-1)))
        self.assertEqual(mat_pow(A, 2)[1][0], 0)
        self.assertTrue(structural_walks(A, 2)[1][0])
        for v in (-2, -1, 1, 2):                            # one state: no cancellation
            for t in (1, 2, 3):
                self.assertNotEqual(mat_pow(((Fr(v),),), t)[0][0], 0)
        for vs in product((-1, 0, 1), repeat=4):            # two states, one step: none
            A2 = ((Fr(vs[0]), Fr(vs[1])), (Fr(vs[2]), Fr(vs[3])))
            P1 = mat_pow(A2, 1)
            self.assertEqual(structural_walks(A2, 1),
                             tuple(tuple(supp(v) for v in r) for r in P1))

    def test_signed_quotient_both_invents_and_deletes(self):
        A = [[Fr(0)] * 4 for _ in range(4)]
        A[2][0], A[2][1], A[3][1] = Fr(1), Fr(-1), Fr(1)   # x->z, x'->z (-1), x'->w
        q = (0, 0, 1, 2)
        src = aggregated_response(A, q, 3, 0, 1)
        Qbar = mean_quotient(A, q, 3)
        self.assertEqual((src[1], Qbar[1][0]), (1, 0))     # deleted response
        self.assertEqual((src[2], Qbar[2][0]), (0, Fr(1, 2)))  # invented response

    def test_lumpability_is_time_graded_exactness(self):
        rng = random.Random(11)
        found_signed_not_boolean = False
        for _ in range(300):
            n = 4
            q = (0, 0, 1, 1)
            A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
            # Force lumpability: make column sums over each fibre agree inside fibres.
            for b_rows in ((0, 1), (2, 3)):
                for x, xp in ((0, 1), (2, 3)):
                    diff = sum(A[z][x] for z in b_rows) - sum(A[z][xp] for z in b_rows)
                    A[b_rows[0]][xp] += diff
            A = tuple(map(tuple, A))
            self.assertTrue(signed_lumpable(A, q, 2))
            Ahat = lumped_matrix(A, q, 2)
            for t in (1, 2, 3):
                P = mat_pow(Ahat, t)
                for x in range(n):
                    self.assertEqual(aggregated_response(A, q, 2, x, t),
                                     tuple(P[b][q[x]] for b in range(2)))
            Bsupp = tuple(tuple(supp(v) for v in r) for r in A)
            boolean_lump = model(boolean(), tuple(zip(*Bsupp)), q).lumpable()
            found_signed_not_boolean |= not boolean_lump
        self.assertTrue(found_signed_not_boolean)
        with self.assertRaises(QuantaleError):
            lumped_matrix(((Fr(0), Fr(0)), (Fr(1), Fr(0))), (0, 0), 1)

    def test_resolvent_lumpability_equals_one_step_lumpability(self):
        # Contrast with CG-3: for idempotent V, lumpability of R* (exactness) is
        # strictly weaker than lumpability of R; the invertible resolvent is not.
        checked = 0
        for vs in product((-1, 0, 1), repeat=9):
            A = tuple(tuple(Fr(vs[3 * i + j]) for j in range(3)) for i in range(3))
            N = resolvent(A)
            if N is None:
                continue
            for q in restricted_growth(3):
                self.assertEqual(signed_lumpable(N, q, max(q) + 1),
                                 signed_lumpable(A, q, max(q) + 1))
                checked += 1
        self.assertGreater(checked, 50000)
        B = boolean()   # the idempotent closure: R* lumpable, R not
        chain = model(B, bool_rel(3, {(0, 1), (1, 2)}), (0, 0, 1))
        self.assertTrue(chain.cond2_fibre_constant() and not chain.lumpable())

    def test_balanced_signs_cannot_cancel(self):
        rng = random.Random(8)
        for _ in range(200):
            n = 4
            P = [[Fr(rng.randint(0, 2)) for _ in range(n)] for _ in range(n)]
            d = [rng.choice((-1, 1)) for _ in range(n)]
            eps = rng.choice((-1, 1))
            A = tuple(tuple(eps * d[i] * P[i][j] * d[j] for j in range(n)) for i in range(n))
            for t in (1, 2, 3, 4):
                Pt, W = mat_pow(A, t), structural_walks(A, t)
                self.assertEqual(tuple(tuple(supp(v) for v in r) for r in Pt), W)

    def test_generic_faithfulness_walk_polynomial(self):
        edges = ((0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (2, 0))
        rng = random.Random(5)
        for t in (1, 2, 3, 4):
            for x, y in product(range(3), repeat=2):
                poly = walk_polynomial(edges, x, y, t)
                self.assertTrue(all(type(c) is int and c > 0 for c in poly.values()))
                A = [[Fr(0)] * 3 for _ in range(3)]
                for _ in range(3):
                    w = {e: Fr(rng.choice((-3, -2, -1, 1, 2, 3)), rng.randint(1, 3)) for e in edges}
                    for (u, v), val in w.items():
                        A[v][u] = val
                    self.assertEqual(evaluate_polynomial(poly, w), mat_pow(A, t)[y][x])
                    self.assertEqual(bool(poly), structural_walks(A, t)[y][x])
                    # One-signed weights cannot cancel: every monomial has sign (-1)^t.
                    neg = {e: -abs(v) for e, v in w.items()}
                    self.assertEqual(evaluate_polynomial(poly, neg) != 0, bool(poly))


if __name__ == "__main__":
    unittest.main()
