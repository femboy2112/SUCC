"""Hostile finite tests for the source-indexed Beck–Chevalley module.

Exact finite data only: explicit carriers, dict maps, powerset sweeps.  No
floats, no randomness, no RH/Weil/Schur content.  The classical theorem
(Beck–Chevalley across pullback squares in FinSet) is checked exhaustively on
small carriers; the new-to-project source-realization firewall is pinned by its
exact ghost witness.
"""
import unittest
from itertools import product

from observational_succ.beck_chevalley_source import (
    BeckChevalleyError, FiniteMap, RealizationCertificate, Square,
    all_predicates, bc_left, bc_right, beck_chevalley_holds,
    beck_chevalley_holds_all, clock_quotient_square, clock_reduction,
    comparison_map, cyclic_carrier, exists_pushforward, fiber_product,
    comparison_is_surjective, find_minimal_counterexample, finite_map,
    firewall_square, formal_fiber_witnesses, is_cartesian, is_commutative,
    is_realization_faithful, predicate, pullback,
    realization_faithful_noncartesian_square, realization_firewall_breaks,
    realize_right,
    source_realized_fiber_witnesses, witness_transport, _all_maps, _named,
)


def square_from(S, Sp, O, Op, q, g, gp, qp, src="declared-test-source"):
    return Square(
        tuple(S), tuple(Sp), tuple(O), tuple(Op),
        finite_map(tuple(S), tuple(O), q),
        finite_map(tuple(Op), tuple(O), g),
        finite_map(tuple(Sp), tuple(S), gp),
        finite_map(tuple(Sp), tuple(Op), qp),
        source_id=src,
    )


class TestBaseChangeOperations(unittest.TestCase):
    def test_exists_pushforward_is_image(self):
        q = finite_map(("a", "b", "c"), ("x", "y"), {"a": "x", "b": "x", "c": "y"})
        self.assertEqual(exists_pushforward(q, predicate(q.domain, {"a"})), frozenset({"x"}))
        self.assertEqual(exists_pushforward(q, predicate(q.domain, {"c"})), frozenset({"y"}))
        self.assertEqual(exists_pushforward(q, predicate(q.domain, {"a", "c"})),
                         frozenset({"x", "y"}))
        self.assertEqual(exists_pushforward(q, frozenset()), frozenset())

    def test_pullback_is_preimage(self):
        g = finite_map(("u", "v", "w"), ("x", "y"), {"u": "x", "v": "y", "w": "y"})
        self.assertEqual(pullback(g, predicate(g.codomain, {"y"})), frozenset({"v", "w"}))
        self.assertEqual(pullback(g, predicate(g.codomain, {"x"})), frozenset({"u"}))
        self.assertEqual(pullback(g, frozenset()), frozenset())

    def test_existential_pullback_adjunction(self):
        # ∃_q F ⊆ G  ⟺  F ⊆ q* G   (the ∃_q ⊣ q* Galois connection), all F,G.
        q = finite_map(("a", "b", "c"), ("x", "y"), {"a": "x", "b": "y", "c": "y"})
        for F in all_predicates(q.domain):
            for G in all_predicates(q.codomain):
                left = exists_pushforward(q, F) <= G
                right = F <= pullback(q, G)
                self.assertEqual(left, right)


class TestCartesianDetection(unittest.TestCase):
    def test_commutativity_detected(self):
        good = square_from(["s0"], ["t0"], ["o0", "o1"], ["p0"],
                           {"s0": "o0"}, {"p0": "o0"}, {"t0": "s0"}, {"t0": "p0"})
        self.assertTrue(is_commutative(good))
        bad = square_from(["s0"], ["t0"], ["o0", "o1"], ["p0"],
                          {"s0": "o1"}, {"p0": "o0"}, {"t0": "s0"}, {"t0": "p0"})
        self.assertFalse(is_commutative(bad))
        self.assertFalse(is_cartesian(bad))

    def test_cartesian_true_on_genuine_fiber_product(self):
        sq = clock_quotient_square(4, 2, 4)
        self.assertTrue(is_commutative(sq))
        self.assertTrue(is_cartesian(sq))
        # comparison map is a bijection onto the fiber product
        phi = comparison_map(sq)
        self.assertEqual(sorted(phi.values()), sorted(fiber_product(sq)))
        self.assertEqual(len(set(phi.values())), len(sq.S_prime))

    def test_cartesian_false_when_s_prime_too_small(self):
        # Fiber product has 2 elements but S' has 1 -> not a pullback.
        sq = square_from(["s0", "s1"], ["t0"], ["o0"], ["p0"],
                         {"s0": "o0", "s1": "o0"}, {"p0": "o0"},
                         {"t0": "s0"}, {"t0": "p0"})
        self.assertTrue(is_commutative(sq))
        self.assertEqual(len(fiber_product(sq)), 2)
        self.assertFalse(is_cartesian(sq))


class TestBeckChevalleyClassical(unittest.TestCase):
    def test_cartesian_implies_beck_chevalley_exhaustive(self):
        # CLASSICAL theorem, finite case: every cartesian square satisfies the
        # formal equality for every predicate.  Exhaust all commutative squares
        # with carriers of size <= 2.
        checked_cartesian = 0
        found_noncartesian_failure = False
        sizes = range(1, 3)
        for nO, nOp, nS, nSp in product(sizes, repeat=4):
            O, Op, S, Sp = (_named("o", nO), _named("p", nOp),
                            _named("s", nS), _named("t", nSp))
            for q in _all_maps(S, O):
                for g in _all_maps(Op, O):
                    for gp in _all_maps(Sp, S):
                        for qp in _all_maps(Sp, Op):
                            sq = Square(S, Sp, O, Op, q, g, gp, qp)
                            if not is_commutative(sq):
                                continue
                            if is_cartesian(sq):
                                checked_cartesian += 1
                                self.assertTrue(beck_chevalley_holds_all(sq))
                            elif not beck_chevalley_holds_all(sq):
                                found_noncartesian_failure = True
        self.assertGreater(checked_cartesian, 0)
        # The test discriminates: some non-cartesian square genuinely fails.
        self.assertTrue(found_noncartesian_failure)

    def test_clock_square_cartesian_and_bc_holds_all(self):
        for m, n, mp in [(4, 2, 4), (6, 3, 6), (6, 2, 4), (4, 2, 2), (9, 3, 3), (12, 6, 6)]:
            with self.subTest(m=m, n=n, mp=mp):
                sq = clock_quotient_square(m, n, mp)
                self.assertTrue(is_cartesian(sq))
                self.assertTrue(beck_chevalley_holds_all(sq))

    def test_clock_reduction_requires_divisibility(self):
        with self.assertRaises(BeckChevalleyError):
            clock_reduction(5, 2)
        with self.assertRaises(BeckChevalleyError):
            clock_quotient_square(6, 4, 6)


class TestMinimalCounterexample(unittest.TestCase):
    def test_counterexample_is_noncartesian_and_breaks_equality(self):
        result = find_minimal_counterexample(max_elements=4, allow_empty=False)
        self.assertIsNotNone(result)
        sq, F, L, R = result
        self.assertTrue(is_commutative(sq))
        self.assertFalse(is_cartesian(sq))
        self.assertNotEqual(L, R)                      # the REQUIRED assertion: sides differ
        self.assertEqual(L, bc_left(sq, F))
        self.assertEqual(R, bc_right(sq, F))
        self.assertNotEqual(bc_left(sq, F), bc_right(sq, F))

    def test_counterexample_exact_shape(self):
        sq, F, L, R = find_minimal_counterexample(max_elements=4, allow_empty=False)
        self.assertEqual(sq.S, ("s0", "s1"))
        self.assertEqual(sq.S_prime, ("t0",))
        self.assertEqual(sq.O, ("o0",))
        self.assertEqual(sq.O_prime, ("p0",))
        self.assertEqual(sq.q.table(), {"s0": "o0", "s1": "o0"})
        self.assertEqual(sq.g.table(), {"p0": "o0"})
        self.assertEqual(sq.g_prime.table(), {"t0": "s0"})
        self.assertEqual(sq.q_prime.table(), {"t0": "p0"})
        self.assertEqual(F, frozenset({"s1"}))
        self.assertEqual(L, frozenset({"p0"}))         # g*(∃_q F) = {p0}
        self.assertEqual(R, frozenset())               # ∃_{q'}(g'* F) = {}

    def test_counterexample_is_minimal_total_five(self):
        sq, F, _, _ = find_minimal_counterexample(max_elements=4, allow_empty=False)
        total = len(sq.S) + len(sq.S_prime) + len(sq.O) + len(sq.O_prime)
        self.assertEqual(total, 5)
        # Nothing smaller exists over inhabited carriers: every total-4 inhabited
        # square is all-singleton, hence cartesian, hence BC-true.
        O = S = Op = Sp = ("z0",)
        onemap = {"z0": "z0"}
        singleton = Square(S, Sp, O, Op,
                           finite_map(S, O, onemap), finite_map(Op, O, onemap),
                           finite_map(Sp, S, onemap), finite_map(Sp, Op, onemap))
        self.assertTrue(is_cartesian(singleton))
        self.assertTrue(beck_chevalley_holds_all(singleton))

    def test_empty_carrier_degenerate_minimum(self):
        sq, F, L, R = find_minimal_counterexample(max_elements=4, allow_empty=True)
        total = len(sq.S) + len(sq.S_prime) + len(sq.O) + len(sq.O_prime)
        self.assertEqual(total, 3)
        self.assertEqual(sq.S_prime, ())               # empty source carrier
        self.assertEqual(R, frozenset())               # RHS vacuously empty
        self.assertNotEqual(L, R)
        self.assertFalse(is_cartesian(sq))


class TestRealizationFirewall(unittest.TestCase):
    def test_formal_bc_holds_but_realization_broken(self):
        sq, F = firewall_square()
        self.assertTrue(is_commutative(sq))
        self.assertFalse(is_cartesian(sq))
        # FORMAL Beck–Chevalley equality is preserved at this predicate.
        self.assertTrue(beck_chevalley_holds(sq, F))
        self.assertEqual(bc_left(sq, F), bc_right(sq, F))
        self.assertEqual(bc_left(sq, F), frozenset({"p0"}))
        # ... yet the source-realization certificate is BROKEN.
        self.assertTrue(realization_firewall_breaks(sq, F))

    def test_ghost_witness_identity(self):
        sq, F = firewall_square()
        formal = set(formal_fiber_witnesses(sq, F))
        realized = set(source_realized_fiber_witnesses(sq, F))
        self.assertEqual(formal, {("s0", "p0"), ("s1", "p0")})
        self.assertEqual(realized, {("s0", "p0")})
        # The ghost: a legitimate formal witness with no actual S'-element.
        self.assertEqual(formal - realized, {("s1", "p0")})

    def test_realizer_is_deterministic_least_index(self):
        sq, F = firewall_square()
        certs = realize_right(sq, F)
        self.assertEqual(set(certs), {"p0"})
        self.assertIsInstance(certs["p0"], RealizationCertificate)
        self.assertEqual(certs["p0"].witness, "t0")
        self.assertEqual(certs["p0"].over, "s0")

    def test_cartesian_square_has_no_firewall_break(self):
        sq = clock_quotient_square(4, 2, 4)
        for F in all_predicates(sq.S):
            self.assertFalse(realization_firewall_breaks(sq, F))

    def test_realization_faithful_class_strictly_larger_than_cartesian(self):
        # Receipt for the OPEN obligation (doc §8): a NON-cartesian square that
        # is formal-BC for all F AND realization-faithful for all F.  Redundant
        # (over-realized) witnesses are tolerated; only ghosts are forbidden.
        sq = realization_faithful_noncartesian_square()
        self.assertTrue(is_commutative(sq))
        self.assertFalse(is_cartesian(sq))               # phi not injective
        self.assertEqual(fiber_product(sq), (("s0", "p0"),))
        self.assertTrue(beck_chevalley_holds_all(sq))
        for F in all_predicates(sq.S):
            self.assertFalse(realization_firewall_breaks(sq, F))
        self.assertTrue(is_realization_faithful(sq))
        self.assertTrue(comparison_is_surjective(sq))    # faithful but not injective

    def test_faithfulness_equals_comparison_surjectivity_exhaustive(self):
        # DEMONSTRATED elementary proposition: over all commutative squares with
        # carriers of size <= 2, realization-faithful-for-all-F coincides with
        # the comparison map being surjective onto the fiber product.
        checked = 0
        for nO, nOp, nS, nSp in product(range(1, 3), repeat=4):
            O, Op, S, Sp = (_named("o", nO), _named("p", nOp),
                            _named("s", nS), _named("t", nSp))
            for q in _all_maps(S, O):
                for g in _all_maps(Op, O):
                    for gp in _all_maps(Sp, S):
                        for qp in _all_maps(Sp, Op):
                            sq = Square(S, Sp, O, Op, q, g, gp, qp)
                            if not is_commutative(sq):
                                continue
                            checked += 1
                            self.assertEqual(is_realization_faithful(sq),
                                             comparison_is_surjective(sq))
        self.assertGreater(checked, 0)


class TestWitnessTransport(unittest.TestCase):
    def test_clock_witness_transport_explicit(self):
        sq = clock_quotient_square(4, 2, 4)
        F = predicate(sq.S, {1, 3})                    # odd residues of Z/4
        left, right = witness_transport(sq, F, 1)      # o' = 1 in Z/4
        self.assertEqual(left, 1)                       # s = 1 ∈ F, q(1) = 1 = g(1)
        self.assertEqual(right, (1, 1))                 # s' = (1,1) ∈ S', g'=1, q'=1
        self.assertEqual(sq.g_prime.apply(right), left)
        self.assertEqual(sq.q_prime.apply(right), 1)
        self.assertIn(1, bc_left(sq, F))
        self.assertIn(1, bc_right(sq, F))

    def test_witness_transport_absent_when_lhs_empty(self):
        sq = clock_quotient_square(4, 2, 4)
        F = predicate(sq.S, set())                      # empty predicate
        self.assertEqual(witness_transport(sq, F, 1), (None, None))

    def test_transport_matches_predicate_membership(self):
        # For a cartesian square, o' is in the LHS iff transport yields a witness.
        sq = clock_quotient_square(6, 3, 6)
        F = predicate(sq.S, {2, 5})
        for o_prime in sq.O_prime:
            left, right = witness_transport(sq, F, o_prime)
            in_lhs = o_prime in bc_left(sq, F)
            self.assertEqual(in_lhs, left is not None)
            if in_lhs:
                self.assertIsNotNone(right)             # cartesian => transport succeeds


class TestValidationAndFirewall(unittest.TestCase):
    def test_malformed_map_rejected(self):
        with self.assertRaises(BeckChevalleyError):
            FiniteMap(("a", "a"), ("x",), (("a", "x"),))         # non-distinct domain
        with self.assertRaises(BeckChevalleyError):
            finite_map(("a",), ("x",), {"a": "z"})               # image escapes codomain
        with self.assertRaises(BeckChevalleyError):
            finite_map(("a", "b"), ("x",), {"a": "x"})           # not total

    def test_predicate_support_must_be_inside_carrier(self):
        with self.assertRaises(BeckChevalleyError):
            predicate(("a", "b"), {"c"})

    def test_pushforward_pullback_domain_guards(self):
        q = finite_map(("a",), ("x",), {"a": "x"})
        with self.assertRaises(BeckChevalleyError):
            exists_pushforward(q, frozenset({"z"}))              # not a subset of domain
        with self.assertRaises(BeckChevalleyError):
            pullback(q, frozenset({"z"}))                        # not a subset of codomain

    def test_source_has_no_float_random_or_rh(self):
        # Firewall self-check: no floating-point / randomness / RH machinery in
        # CODE.  We scan for code-level tokens that cannot occur in a prose
        # disclaimer (the module docstring legitimately mentions "no RH / Weil /
        # Schur" and "no floats", so matching those bare words would be a false
        # positive).
        import observational_succ.beck_chevalley_source as mod
        with open(mod.__file__, "r", encoding="utf-8") as fh:
            text = fh.read().lower()
        for banned in ("import random", "random.", "float(", "import numpy",
                       "numpy.", "math.sqrt", ".seed(", "riemann", "zeta("):
            self.assertNotIn(banned, text)

    def test_cyclic_carrier_bounds(self):
        self.assertEqual(cyclic_carrier(3), (0, 1, 2))
        with self.assertRaises(BeckChevalleyError):
            cyclic_carrier(0)


if __name__ == "__main__":
    unittest.main()
